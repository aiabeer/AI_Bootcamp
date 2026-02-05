<h1>Git Workflow Guide (GitHub & GitLab)</h1>

<p>This guide explains the basic Git workflow for working with <strong>GitHub</strong> and <strong>GitLab</strong>, including repository creation, local work, and pushing changes.</p>

<hr>

<h2>GitHub Workflow</h2>

<h3>1. Create a repository on GitHub</h3>
<ol>
  <li>Go to <strong>GitHub → New repository</strong></li>
  <li>Choose a repository name</li>
  <li><strong>Do NOT</strong> add:
    <ul>
      <li>README</li>
      <li>.gitignore</li>
    </ul>
  </li>
  <li>Click <strong>Create repository</strong></li>
</ol>

<h3>2. Clone the repository to your computer</h3>
<pre><code>git clone https://github.com/USERNAME/REPO.git
cd REPO</code></pre>

<h3>3. Work locally</h3>
<ul>
  <li>Edit files</li>
  <li>Add or delete files</li>
</ul>

<h3>4. Push changes to GitHub</h3>
<pre><code>git add .
git commit -m "Short clear message"
git push</code></pre>

<h3>5. Next time you work</h3>
<pre><code>git pull
# edit files
git add .
git commit -m "What you changed"
git push</code></pre>

<h3>6. One-time setup (folder already exists locally)</h3>
<pre><code>cd your-folder
git init
git remote add origin https://github.com/USERNAME/REPO.git
git branch -M main
git add .
git commit -m "Initial commit"
git push -u origin main</code></pre>

<hr>

<h2>GitLab Workflow</h2>

<h3>1. Create a repository on GitLab</h3>
<ol>
  <li>Go to <strong>GitLab → New project</strong></li>
  <li>Select <strong>Blank project</strong></li>
  <li>Choose a project name</li>
  <li><strong>Do NOT</strong> initialize with:
    <ul>
      <li>README</li>
      <li>.gitignore</li>
    </ul>
  </li>
  <li>Click <strong>Create project</strong></li>
</ol>

<h3>2. Clone the repository to your computer</h3>
<pre><code>git clone https://gitlab.com/USERNAME/REPO.git
cd REPO</code></pre>

<h3>3. Work locally</h3>
<ul>
  <li>Edit files</li>
  <li>Add or delete files</li>
</ul>

<h3>4. Push changes to GitLab</h3>
<pre><code>git add .
git commit -m "Short clear message"
git push</code></pre>

<h3>5. Next time you work</h3>
<pre><code>git pull
# edit files
git add .
git commit -m "What you changed"
git push</code></pre>

<h3>6. One-time setup (folder already exists locally)</h3>
<pre><code>cd your-folder
git init
git remote add origin https://gitlab.com/USERNAME/REPO.git
git branch -M main
git add .
git commit -m "Initial commit"
git push -u origin main</code></pre>

<hr>

<h2>Notes</h2>
<ul>
  <li>Replace <code>USERNAME</code> and <code>REPO</code> with your actual values.</li>
  <li>Use clear, meaningful commit messages.</li>
  <li>Always run <code>git pull</code> before starting new work.</li>
</ul>
