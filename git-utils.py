#!/usr/bin/env python3

import os
import re
import subprocess
import sys

descr = '    This tool recursively searches for git repositories within a directory,\n    returning information based on the selected operation.'
usageargs = [
	'    --list-remotes',
	'        List the remote repo URL(s) for each git repo in DIR.',
	'    --list-uncommited',
	'        List the repos for which there are uncommitted changes in DIR.',
	'    DIR',
	'        The directory to recursively search for git repositories.',
	''
]
usageopts = ['    {:s} --list-remotes DIR', '    {:s} --list-uncommitted DIR']
error_str = '[Error]'
invalid_argc_str = 'Invalid number of arguments.'
invalid_param_str = 'Parameter: {:s} is not a valid option.'
invalid_path_str = 'The specified path ({:s}) does not exist.'
info_str = '[Info]'
resources_str = 'For more information, see {:s} --help'

debug = True

def list_remotes(path):
	os.chdir(path)

	if repo(path):
		print('{:s}: {:s}'.format(path, remote(path))) 
	else:
		for dir in subdirs(path):
			list_remotes(dir)

def list_uncommitted(path):
	os.chdir(path)

	if repo(path):
		if not up_to_date(path):
			print(path)
	else:
		for dir in subdirs(path):
			list_uncommitted(dir)

def repo(path):
	success_code = 0

	with open('/dev/null', 'w') as null_file:	
		process = subprocess.run(["git", "status"], stdout=null_file, stderr=null_file)

	return process.returncode is success_code

def remote(path):
	pattern = re.compile("git@(.*)\.git")

	with open('/dev/null', 'w') as null_file:
		process = subprocess.run(["git", "remote", "-v"], stdout=subprocess.PIPE, stderr=null_file)

	matches = re.search(pattern, str(process.stdout, 'utf-8'))
	
	return matches.group(0) if matches else "no remote"

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
	print("NAME")
	print(progname)
	print()
	print("DESCRIPTION")
	print(descr)
	print()
	print("USAGE")
	for line in usageopts:
		print(line.format(progname))
	print()
	print("PARAMETERS")
	for line in usageargs:
		print(line)

if __name__ == '__main__':
	progname = sys.argv[0]
	argc = len(sys.argv)

	if argc is 1 or '--help' in sys.argv:
		helpmenu(progname)
	elif argc is 3:
		operation = sys.argv[1]
		path = os.path.abspath(sys.argv[2])
		if operation == "--list-uncommitted":
			list_uncommitted(path)
		elif operation == "--list-remotes":
			list_remotes(path)
		else:
			warn(invalid_param_str.format(operation), progname)
	else:
		warn(invalid_argc_str, progname)
		