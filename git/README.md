# Git Workflow Guide (GitHub & GitLab)


This guide explains the basic Git workflow for working with GitHub and GitLab, including repository creation, local work, and pushing changes.



## GitHub Workflow

1. Create a repository on GitHub: 
    Go to GitHub → New repository
    Choose a repository name
    Do NOT add:
        README
        .gitignore

Click Create repository:

2. Clone the repository to your computer

git clone https://github.com/USERNAME REPO.git

3. Work locally
  Edit files
  Add or delete files

4. Push changes to GitHub
git add .
git commit -m "Short clear message"
git push

5. Next time you work
git pull
# edit files
git add .
git commit -m "What you changed"
git push

6. One-time setup (folder already exists locally)
cd your-folder
git init
git remote add origin https://github.com/USERNAME/REPO.git
git branch -M main
git add .
git commit -m "Initial commit"
git push -u origin main

## GitLab Workflow

1. Create a repository on GitLab

  Go to GitLab → New project
  Select Blank project
    Choose a project name
    Do NOT initialize with:
      README
      .gitignore
    
  
  Click Create project

2. Clone the repository to your computer

git clone https://gitlab.com/USERNAME/REPO.git


3. Work locally

  Edit files
  Add or delete files

4. Push changes to GitLab
git add .
git commit -m "Short clear message"
git push

5. Next time you work
git pull
# edit files
git add .
git commit -m "What you changed"
git push

6. One-time setup (folder already exists locally)
cd your-folder
git init
git remote add origin https://gitlab.com/USERNAME/REPO.git
git branch -M main
git add .
git commit -m "Initial commit"
git push -u origin main

## Notes

 1. Replace USERNAME and REPO with your actual values.
 2. Use clear, meaningful commit messages.
 3. Always run git pull before starting new work.

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