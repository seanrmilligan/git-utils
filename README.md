# Git Utils

## Dependencies

- python3

## Usage

This tool takes in one of several flags, as well as a relative or absolute path. It then recursively searches that path and reports back information on any git repos it found at or under that path.

Supported Actions:
- List repositories in a directory.
- List repositories with uncommitted changes in a directory.
- List repositories with unpushed changes in a directory.
- List remotes for repositories in a directory.

Examples:

Listing uncommmitted repositories:

```
sean@computer $ ./gitutils --list-uncommitted /home/sean/projects/
/home/sean/projects/git-utils
sean@computer $
```

Listing remotes:

```
sean@computer $ ./gitutils --list-remotes /home/sean/projects/
/home/sean/projects/git-utils:
origin	git@github.com:sean/git-utils.git (fetch)
origin	git@github.com:sean/git-utils.git (push)

/home/sean/projects/fictitious-local-project:
no remotes

sean@computer $
```

The power of these commands come from chaining them with other tools such as grep.
- List repositories with no remote: `./gitutils --list-remotes /home/sean/projects/ | grep "no remotes" -B 1`
- List only repositories on github.com: `./gitutils --list-remotes /home/sean/projects/ | grep github -B 1`

## Motivation
I organize my various repositories under one directory, `/home/sean/projects/`. Within that, each directory may be a repo or a grouping directory under which appear several repos. This is done for organizational (in)sanity. Example:

```
/home/sean/projects/
 |
 +-small-project/ (repo)
 +-large-project/
 |  |
 |  +-large-project-db-server-code/ (repo)
 |  +-large-project-api-server-code/ (repo)
 |  +-large-project-website-code/ (repo)
 |
 +-small-project-two/ (repo)
```

Over time it became cumbersome to manage whether I have committed, pushed, set up remotes, etc. on each repository. This is especially noticeable when moving to or setting up a new computer, or switching to a new git hosting service (github v. gitlab v. bitbucket v. ...). Not frequent scenarios, but for those who enjoy doing a clean install of their OS from time to time this may come in handy.

