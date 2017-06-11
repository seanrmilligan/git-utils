#!/usr/bin/env python3

import os
import subprocess
import sys

descr = 'This tool takes a path to a directory containing git repositories, and returns only the repositories which have uncommitted changes.'
usage = 'usage: {:s} DIR'
usageargs = ['\tDIR   The directory to recursively search for git repos.']
error_str = '[Error]'
invalid_argc_str = 'Invalid number of arguments.'
invalid_path_str = 'The specified path ({:s}) does not exist.'
info_str = '[Info]'
resources_str = 'For more information, see {:s} --help'

debug = True

def check(path):
	os.chdir(path)

	if repo(path):
		if not up_to_date(path):
			print(path)
	else:
		for dir in subdirs(path):
			check(dir)

def repo(path):
	success_code = 0

	with open('/dev/null', 'w') as null_file:	
		process = subprocess.run(["git", "status"], stdout=null_file, stderr=null_file)

	return process.returncode is success_code

def up_to_date(path):
	with open('/dev/null', 'w') as null_file:
		process = subprocess.run(["git", "status"], stdout=subprocess.PIPE, stderr=null_file)
	
	return True if "nothing to commit" in str(process.stdout, 'utf-8') else False

def subdirs(path):
	# list() apparently faster than the equivalent list comprehension due to C optimization
	return [os.path.join(path, item) for item in os.listdir(path) if os.path.isdir(os.path.join(path, item))]
    # return list(os.listdir(path) if os.path.isdir(os.path.join(path, item)))

def warn(warning, progname):
	print('{:s} {:s}'.format(error_str, warning))
	print(resources_str.format(progname))

def inform(info):
	if (debug):
		print('{:s} {:s}'.format(info_str, info))

def helpmenu(progname):
	print(descr)
	print()
	print(usage.format(progname))
	for line in usageargs:
		print(line)

if __name__ == '__main__':
	progname = sys.argv[0]
	argc = len(sys.argv)

	if argc is 1 or '--help' in sys.argv:
		helpmenu(progname)
	elif argc is 2:
		abs_path = os.path.abspath(sys.argv[1])
		check(abs_path)
	else:
		warn(invalid_argc_str, progname)
		