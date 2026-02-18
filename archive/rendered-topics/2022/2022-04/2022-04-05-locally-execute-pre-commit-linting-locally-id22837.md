# Locally execute pre-commit linting locally

**Topic ID**: 22837
**Date**: 2022-04-05
**URL**: https://discourse.slicer.org/t/locally-execute-pre-commit-linting-locally/22837

---

## Post #1 by @jcfr (2022-04-05 14:35 UTC)

<p>Following pull request <a href="https://github.com/Slicer/Slicer/pull/6262">PR-6262</a>, we integrated a linting workflow to our continuous integration.</p>
<p>Waiting we update the <code>Utilities/SetupForDevelopment.sh</code> to automatically install the requirements,  the linting could be performed locally following these steps:</p>
<pre><code class="lang-bash">pip install pre-commit
</code></pre>
<pre><code class="lang-bash">cd Slicer
pre-commit run --all-files
</code></pre>

---

## Post #2 by @jcfr (2022-04-05 14:56 UTC)

<p>And to install the tool within the Slicer environment:</p>
<pre><code class="lang-bash">./Slicer-Release/python-install/bin/PythonSlicer -m pip install pre_commit
</code></pre>
<p>and to perform the check:</p>
<pre><code class="lang-bash">cd Slicer
../Slicer-Release/python-install/bin/PythonSlicer -m pre_commit run --all-files
</code></pre>

---

## Post #3 by @lassoan (2022-04-06 15:54 UTC)

<p>Thank you <a class="mention" href="/u/jcfr">@jcfr</a>, this is very useful. I’ve tried to execute this on Windows and I got two errors:</p>
<ol>
<li>The script complained that <code>DLLs</code> folder is missing.</li>
</ol>
<ul>
<li>In Slicer install tree: <code>c:\\Users\\andra\\AppData\\Local\\NA-MIC\\Slicer 4.13.0-2022-03-19\\lib\\Python\DLLs</code>
</li>
<li>In Slicer build tree: <code>C:\\D\\S4R\\python-install\\DLLs</code>
</li>
</ul>
<p>I created an empty folder at the not found location and restarted the script and it seemed to solve this issue.</p>
<ol start="2">
<li>
<code>pythonw.exe</code> not found</li>
</ol>
<p>I copied <code>PythonSlicer.exe</code> to <code>pythonw.exe</code> and it seemed to solve this issue.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> do you know what may require this folder and file? Should we add them to the build tree or add a module to the Sandbox (DebuggingTools or DeveloperToolsForExtensions) extension that can create these folders, install the pre-commit package, and run the checks on a single click?</p>

---
