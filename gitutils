#!/usr/bin/env python3

# library code
import os
import sys

# project code
from git_commands import *

descr = '    This tool recursively searches for git repositories within a directory,\n    returning information based on the selected operation.'
usageargs = [
	'    --list-remotes',
	'        List the remote repo URL(s) for each git repo in DIR.',
	'    --list-repos',
	'        List the absolute path for each git repo in DIR.',
	'    --list-uncommited',
	'        List the repos for which there are uncommitted changes in DIR.',
	'    --list-unpushed',
	'        List the repos for which there are unpushed changes in DIR.',
	'    DIR',
	'        The directory to recursively search for git repositories.',
	''
]
usageopts = [
    '    {:s} --list-remotes DIR',
    '    {:s} --list-repos DIR',
    '    {:s} --list-uncommitted DIR',
    '    {:s} --list-unpushed DIR',
    ''
]
error_str = '[Error]'
invalid_argc_str = 'Invalid number of arguments.'
invalid_param_str = 'Parameter: {:s} is not a valid option.'
invalid_path_str = 'The specified path ({:s}) does not exist.'
info_str = '[Info]'
resources_str = 'For more information, see {:s} --help'

debug = True

def traverse(path, func):
	os.chdir(path)

	if repo(path):
		func(path)
	else:
		for dir in subdirs(path):
			traverse(dir, func)

def list_remotes(path):
	print('{:s}:\n{:s}'.format(path, remote(path)))

def list_repos(path):
	print(path)

def list_uncommitted(path):
	if not committed(path):
		print(path)

def list_unpushed(path):
	if not pushed(path):
		print(path)

def subdirs(path):
	# list() is apparently faster than the equivalent list comprehension due to C optimization
	# return [os.path.join(path, item) for item in os.listdir(path) if os.path.isdir(os.path.join(path, item))]
    return list(os.path.join(path, item) for item in os.listdir(path) if os.path.isdir(os.path.join(path, item)))

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
			traverse(path, list_uncommitted)
		elif operation == "--list-unpushed":
			traverse(path, list_unpushed)
		elif operation == "--list-remotes":
			traverse(path, list_remotes)
		elif operation == "--list-repos":
			traverse(path, list_repos)
		else:
			warn(invalid_param_str.format(operation), progname)
	else:
		warn(invalid_argc_str, progname)



# see unpushed commits to the upstream for the current branch only