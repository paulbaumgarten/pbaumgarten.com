# Setup your computer

`sudo apt install git`

# Create new repository (project)

All git commands will only work when you are in the local folder of a git repo.

## Setup SSH first

* Generate a key pair
* To keep it simple for now, go without the password when prompted.

```bash
ssh-keygen -f ~/.ssh/github  -t rsa -C "your@mail.com"
cat ~/.ssh/github.pub
```

* Copy the print out of your public key
* Login to Github
* Tools / account settings / SSH keys / Add SSH key
* Paste the key in the `key` box, click `Add key`
* You can now use the SSH clone URL when cloning a repo to your local machine, allowing you to bypass entering a username/password.

## Create repo via github

* Create new repo (tick "with README.md")
* Copy and paste the repo git address

On your computer,

`git clone https://github.com/username/repo-project.git`

More fully,

`git clone username@host:/path/to/repository`

Will create a new folder (child of the current working folder) with the name of the repo, and all it's contents.

## Create repo via local computer

```bash
git init                        # initialise current folder as a git repo (locally)
git init folder_name            # create folder_name and initialise as a git repo (locally)
```

To link the local repo to a cloud repo, you'll then need to:

* Replace USERNAME and PROJECTNAME as relevant

```bash
curl -u 'USERNAME' https://api.github.com/user/repos -d '{"name":"PROJECTNAME"}'
git remote add origin git@github.com:USERNAME/PROJECTNAME.git
git remote -v               # Verify
git push origin master      # Push to cloud repo
```

## Configure your repo

To configure for all repos in your local user name space

`git config --global user.email "pbaumgarten@gmail.com"`
`git config --global user.name "paulbaumgarten"`

To force a different configu for a local repo

`git config --local user.email "pbaumgarten@gmail.com"`
`git config --local user.name "paulbaumgarten"`

# Status

```bash
git status                      # What is different between our local folder and the repo
```

# Adding files to a project

Git will not automatically assume that just because a file exists in your project folder that it should be tracking it. You have to manually specify the additional file(s) when you create them using one of these methods:

```bash
git add filename.ext            # Add file for tracking
git add .                       # Add all files in local directory for tracking
git add -A                      # Add all files in local tree for tracking
```

# Commiting changes and uploading to the cloud

```bash
git commit -a -m "message"      # Save/commit all local changes to the local repo.
git push                        # Push any locally commited changes up to the cloud.
```

# Sync down from the cloud

```bash
git pull                        # Pull down changes from the cloud to your local repo and folder.
```

# Recommended workflow

Before starting work on a project:

* `git pull`                    # Retrieve any new changes from the cloud repo
* Do your work
* `git add -A`                  # Add any new files
* `git commit -a -m "all in a day's work"` # Save changes
* `git push`                    # Upload to the cloud repo

# Merge conflicts

If you get a merge conflict error after a push/pull,

* open the file with the reported conflict
* compare the two versions
* make the corrected changes
* delete the helper text it placed in the file
* save the file

```bash
git add -A
git commit -m "merge confilct fixed"    # or similar message
git push
```

# Versions

```bash
# See versions of the repo
git log --pretty=oneline        # see commit messages and hash of past versions
# To restore the most recently commited version of a file
git checkout HEAD -- <filename>
# To restore a previously commited version of a file using its hash
git checkout <hash> -- <filename>
```

# Ignore files

If you plan on using `git add -A`, there are likely files/folders you will want git to ignore. Files like caches, binary build files, and any files containing passwords/authentication codes etc.

Create a `.gitignore` file in the root folder of your repository.

Example content might be:

```text
__pycache__/
secrets.json
config.py
```

# Cleanup git history

Make the current commit the only (initial) commit in a Git repository?

(ie: use this to remove git history prior to converting a private repo to public)

```bash
git checkout --orphan newBranch
git add -A # Add all files and commit them
git commit -m "clear history"
git branch -D master  # Deletes the master branch
git branch -m master  # Rename the current branch to master
git push -f origin master  # Force push master branch to github
git gc --aggressive --prune=all     # remove the old files
```

* From https://stackoverflow.com/questions/9683279/make-the-current-commit-the-only-initial-commit-in-a-git-repository/13102849#13102849

# References

Scott Robertson (2007-08) Git in 5 Minutes: Putting the Basics Straight
https://classic.scottr.org/presentations/git-in-5-minutes/

Gary Robinson (2014) Git In Two Minutes (For A Solo Developer)
http://www.garyrobinson.net/2014/10/git-in-two-minutes-for-a-solo-developer.html

LearnCode.academy (2014) Github Tutorial For Beginners - Github Basics for Mac or Windows & Source Control Basics
https://www.youtube.com/watch?v=0fKg7e37bQE

jdblischak (2014) SSH Keys for GitHub
https://jdblischak.github.io/2014-09-18-chicago/novice/git/05-sshkeys.html