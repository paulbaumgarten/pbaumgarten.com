# Github Desktop walkthrough

Github, at it's core, is a version tracking tool. Additionally it allows synchronising (backups) to the Github servers, and collaboration (sharing) with others. The version tracking is particularly powerful as it lets you review your work at any point in history, so if you make changes you wish to un-do you can.

A repository is the most basic element of GitHub. They're easiest to imagine as a project's folder. A repository contains all of the project files (including documentation), and stores each file's revision history. Repositories can have multiple collaborators and can be either public or private. ([source](https://help.github.com/en/articles/github-glossary#repository))

## Pre-requisites

1. Create an account with [https://github.com/](https://github.com/) (free plan is fine)
2. Download and install [Github Desktop](https://desktop.github.com/)
3. Open Github Desktop and sign in.

## New project & repository

Ideally you would use Github to create your empty repository/project before you commence work on it.

1. File menu / New repository.
2. The "repository name" will be the name used to create a folder for your project. The "local path" is the parent folder that will contain the project folder.
3. It is highly recommended to choose your language in the "Git ignore" profile rather than leaving it as None. This will tell Git to ignore files certain temporary files your language uses that don't need to be backed up.
4. Work on your project, and then check the section for *saving new changes to existing repository* when ready.

## Existing project (not yet turned into a git repository)

When you have a project you are ready to backup to Github &/or share with me watch my [video walk through](https://www.youtube.com/watch?v=4dMliXK6mjM) or follow the following steps:

1. File menu / Add local repository (even though, technically the repository doesn't yet exist pick this optioin)
2. The "repository name" will be the name used to create a folder for your project. The "local path" is the parent folder that will contain the project folder.
3. Click "Publish repository" for a pop up screen to appear.
4. You can keep "Keep this code private" set to on.
5. Click "Publish repository" on the pop up screen.

## Saving new changes to existing repository

1. Open Github Desktop and select your repository from the pulldown list.
2. You will be presented a list of files that have changed. You may review the changes.
3. You must enter a summary. While getting used to Github, you can keep it simple (eg: "changed files"). Ideally you will be adding a meaningful description of what has changed, so browsing through the history of your project becomes easier later.
4. Click "Commit to master" to confirm the changes.
5. Click "Push origin" to actually perform the upload.
 
## Share project with me

1. Go to [https://github.com/](github.com), login, go to **Your repositories**, & open the relevant repository.
2. Click Settings
3. Click Collaborators. Enter "paulbaumgarten" as a collaborator, click "Add collaborator".

