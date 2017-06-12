import subprocess

def pushed(path):
	# git log --branches --not --remotes
	# returns any commit on any branch that was not pushed to remote
	#
	# git log @{u}..
	# returns only commits on the current branch that were not pushed to remote
	with open('/dev/null', 'w') as null_file:
		process = subprocess.run(["git", "log", "--branches", "--not", "--remotes"], stdout=subprocess.PIPE, stderr=null_file)

	return True if not str(process.stdout, 'utf-8') else False

def repo(path):
	success_code = 0

	with open('/dev/null', 'w') as null_file:	
		process = subprocess.run(["git", "status"], stdout=null_file, stderr=null_file)

	return process.returncode is success_code

def remote(path):
	with open('/dev/null', 'w') as null_file:
		process = subprocess.run(["git", "remote", "-v"], stdout=subprocess.PIPE, stderr=null_file)
	
	remotes = str(process.stdout, 'utf-8')
	return remotes if remotes else "no remotes\n"

def committed(path):
	with open('/dev/null', 'w') as null_file:
		process = subprocess.run(["git", "status"], stdout=subprocess.PIPE, stderr=null_file)
	
	return True if "nothing to commit" in str(process.stdout, 'utf-8') else False