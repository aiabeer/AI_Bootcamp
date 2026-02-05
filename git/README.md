# Git Workflow Guide (GitHub & GitLab)


This guide explains the basic Git workflow for working with GitHub and GitLab, including repository creation, local work, and pushing changes.

## Table of Contents
GitHub setup
GitLab setup
Branching & Merging
Merge Conflicts
Git Reset
Git Rebase
Git Stash
## GitHub Workflow

### Create a repository on GitHub: 
    1. Go to GitHub → New repository
    2. Choose a repository name
    Do NOT add:
        README
        .gitignore
    3. Click Create repository

### Clone the repository to your computer

```shell
git clone https://github.com/USERNAME REPO.git
```

### Work locally
  Edit files
  Add or delete files

### Push changes to GitHub
```shell
git add .
git commit -m "Short clear message"
git push
```

### Next time you work
```shell
git pull
```

### edit files

```shell
git add .
git commit -m "What you changed"
git push
```

### One-time setup (folder already exists locally)
```shell
cd your-folder
git init
git remote add origin https://github.com/USERNAME/REPO.git
git branch -M main
git add .
git commit -m "Initial commit"
git push -u origin main
```

## GitLab Workflow

### Create a repository on GitLab

  1. Go to GitLab → New project
  2. Select Blank project
  3. Choose a project name
    Do NOT initialize with:
      README
      .gitignore
  4. Click Create project

### Clone the repository to your computer

```shell
git clone https://gitlab.com/USERNAME/REPO.git
```

### Work locally

  Edit files
  Add or delete files

### Push changes to GitLab

```shell
git add .
git commit -m "Short clear message"
git push
```

### Next time you work

```shell
git pull
```

### edit files

```shell
git add .
git commit -m "What you changed"
git push
```

### One-time setup (folder already exists locally)

```shell
cd your-folder
git init
git remote add origin https://gitlab.com/USERNAME/REPO.git
git branch -M main
git add .
git commit -m "Initial commit"
git push -u origin main
```

## Branching & Merging
### Creating and Switching Branches

```shell
# Create a new branch
git branch feature-branch

# Switch to the new branch
git checkout feature-branch

# Create and switch in one command
git checkout -b feature-branch

# List all branches
git branch

# Delete a branch (local)
git branch -d feature-branch
```
### Merging Branches

```shell
# Switch to main branch
git checkout main

# Merge feature-branch into main
git merge feature-branch

# Push merged changes
git push
```
### Merge Conflicts
Understanding Merge Conflicts
Merge conflicts occur when Git cannot automatically resolve differences between branches.

Resolving Merge Conflicts

1. Identify conflicted files:
    ```shell
    git status
    ```
2. Open conflicted files:
    Look for conflict markers
    <<<<<<< HEAD
    Your current branch code
    =======
    Incoming branch code
    ">>>>>>> branch-name"

3. Edit files to keep desired code
    Remove conflict markers (<<<<<<<, =======, >>>>>>>)

4. Mark as resolved and commit

    ```shell
    git add .
    git commit -m "Resolved merge conflict"
    ```
## Git Reset
### Types of Reset
    ```shell
    # Soft reset - moves HEAD but keeps changes staged
    git reset --soft HEAD~1

    # Mixed reset (default) - moves HEAD, unstages changes
    git reset --mixed HEAD~1

    # Hard reset - moves HEAD, discards all changes
    git reset --hard HEAD~1

    # Reset specific file
    git reset HEAD filename.txt

    # Reset to specific commit
    git reset --hard commit-hash
    ```
### Common Reset Scenarios
    ```shell
    # Undo last commit but keep changes
    git reset --soft HEAD~1

    # Undo last commit and unstage changes
    git reset HEAD~1

    # Discard all local changes
    git reset --hard HEAD

    # Discard specific file changes
    git checkout -- filename.txt
    ```
## Git Rebase
### Basic Rebase

    ```shell
    # Update feature branch with main branch changes
    git checkout feature-branch
    git rebase main

    # Continue after resolving conflicts
    git rebase --continue

    # Abort rebase
    git rebase --abort

    # Interactive rebase (last 3 commits)
    git rebase -i HEAD~3
    ```

## Git Stash
### Stashing Changes
    ```shell
    # Stash uncommitted changes
    git stash

    # Stash with message
    git stash save "Work in progress"

    # List stashes
    git stash list

    # Apply latest stash (keeps stash)
    git stash apply

    # Apply specific stash
    git stash apply stash@{2}

    # Apply and remove from stash list
    git stash pop

    # Remove specific stash
    git stash drop stash@{1}

    # Clear all stashes
    git stash clear

    # Create a branch from stash
    git stash branch new-branch-name
    ```
### Stash Options
    ```shell
    # Stash including untracked files
    git stash -u

    # Stash including ignored files
    git stash -a

    # View stash content
    git stash show stash@{0}

    # View full diff of stash
    git stash show -p stash@{0}
    ```

## Best Practices
1. Commit Often: Small, logical commits

2. Write Clear Messages: Use imperative mood

3. Pull Before Push: Always pull latest changes

4. Use Branches: Keep main branch stable

5. Review Before Merge: Check changes before merging

6. Backup Before Reset: Use git stash or create backup branches


## Usefull links 

* [link SSH to your github](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/)
* [15 min. to Learn Git](https://try.github.io)
* [Self learning tool](https://skills.github.com) for Git launched in 2018 by GitHub
* [Learn Git branching](http://learngitbranching.js.org)
* [Codeschool - Git](https://www.codeschool.com/learn/git)
* [Learn Enough Command Line to Be Dangerous](http://www.learnenough.com/command-line/) (Try to read through the entire tutorial)
* [Simple explanation of git](http://rogerdudler.github.io/git-guide/index.nl.html)
* [Codeschool - Git ](https://www.codeschool.com/learn/git)
* [Codecademy - Git (more limited)](https://www.codecademy.com/courses/learn-git/lessons/git-workflow/exercises/hello-git)
* [Git Pro Book](http://git-scm.com/book/en/v2)
* [Using Git in Team](https://jameschambers.co.uk/git-team-workflow-cheatsheet)
* [Using Git for Data Science](https://valohai.com/blog/git-for-data-science/)
* [Mastering Markdown](https://guides.github.com/features/mastering-markdown/)
* [Git-tips](https://github.com/git-tips/tips)
* [Bitbucket Complete tutorial](https://www.atlassian.com/git/tutorials/learn-git-with-bitbucket-cloud)
* [markdown-cheatsheet](https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf)
* [syncing-a-fork](https://help.github.com/articles/syncing-a-fork/)
* [How to do a pull request?](https://services.github.com/on-demand/intro-to-github/create-pull-request)

* [Add an SSH key to GitLab](https://docs.gitlab.com/ee/user/ssh.html)
* [GitLab Basics Tutorial](https://docs.gitlab.com/ee/gitlab-basics/)
* [GitLab Official CheatSheet](https://about.gitlab.com/images/press/git-cheat-sheet.pdf)
* [Effective Code Reviews with Merge Requests](https://docs.gitlab.com/ee/user/project/merge_requests/)
* [GitLab Flavored Markdown (GLFM)](https://docs.gitlab.com/ee/user/markdown.html)
* [Introduction to GitLab CI/CD](https://docs.gitlab.com/ee/ci/introduction/)
* [Forking a Project in GitLab](https://docs.gitlab.com/ee/user/project/repository/forking_workflow.html)
* [How to create a Merge Request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)