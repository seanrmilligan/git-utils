# Git Utils

## Motivation
Laziness.

Real motivation:
I organize my various repositories under one directory, say `/home/sean/projects/`. Under that, a directory may be a repo or a group of directories which are repos. This is done to help collect related repositories that are part of one overarching project. Example:

```
/home/sean/projects/
 |
 +-small-project/ (repo)
 |
 +-large-project/
 |  |
 |  +-large-project-db-server-code/ (repo)
 |  |
 |  +-large-project-api-server-code/ (repo)
 |  |
 |  +-large-project-website-code/ (repo)
 |
 +-small-project-two/ (repo)
```

Over time it has become cumbersome to manage whether I have committed, pushed, set up remotes, etc. on each repository. This is especially noticeable at times of moving to or setting up a new computer, or switching to a new git hosting service as the primary git service (github v. gitlab v. ...). Not frequent scenarios, but for those who enjoy doing a clean install of their OS from time to time this may come into more frequent usage.

## Usage

This tool takes in one of several flags, as well as a relative or absolute path, recursively searches that path, and reports back flag-specific information on any git repos it found at or under that path.


