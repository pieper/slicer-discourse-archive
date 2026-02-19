---
topic_id: 14448
title: "Slicer 4 11 20200930 Cant Import Pip Installed Pillow On Lin"
date: 2020-11-05
url: https://discourse.slicer.org/t/14448
---

# Slicer-4.11.20200930: Can't import pip-installed Pillow on Linux

**Topic ID**: 14448
**Date**: 2020-11-05
**URL**: https://discourse.slicer.org/t/slicer-4-11-20200930-cant-import-pip-installed-pillow-on-linux/14448

---

## Post #1 by @Fernando (2020-11-05 15:42 UTC)

<p>Hi all,</p>
<p>I can’t run the line below in the current Linux stable (and preview) release, after running <code>pip_install('Pillow')</code>:</p>
<pre><code class="lang-python">&gt;&gt;&gt; from PIL import Image
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "/home/fernando/opt/Slicer-4.11.20200930-linux-amd64/lib/Python/lib/python3.6/site-packages/PIL/Image.py", line 94, in &lt;module&gt;
    from . import _imaging as core
ImportError: /home/fernando/opt/Slicer-4.11.20200930-linux-amd64/lib/Python/lib/python3.6/site-packages/PIL/_imaging.cpython-36m-x86_64-linux-gnu.so: ELF load command address/offset not properly aligned
&gt;&gt;&gt; 
</code></pre>
<p>Do you know what could be happening?</p>

---

## Post #2 by @jamesobutler (2020-11-05 16:55 UTC)

<p>Does <code>from PIL import Image</code> not work from a fresh download of the current Slicer Stable?</p>
<p>You shouldn’t have to install Pillow as it is is already installed as part of the <code>External_python-dicom-requirements</code> project.<br>
</p><aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/v4.11.20200930/SuperBuild/External_python-dicom-requirements.cmake#L45-L52" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/v4.11.20200930/SuperBuild/External_python-dicom-requirements.cmake#L45-L52" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/v4.11.20200930/SuperBuild/External_python-dicom-requirements.cmake#L45-L52</a></h4>
<pre class="onebox"><code class="lang-cmake"><ol class="start lines" start="45" style="counter-reset: li-counter 44 ;">
<li>#  - Pillow-7.2.0-cp36-cp36m-win_amd64.whl</li>
<li>#  - Pillow-7.2.0-cp36-cp36m-macosx_10_10_x86_64.whl</li>
<li>#  - Pillow-7.2.0-cp36-cp36m-manylinux1_x86_64.whl</li>
<li>#  - Pillow-7.2.0-cp36-cp36m-manylinux2014_aarch64.whl</li>
<li>pillow==7.2.0 --hash=sha256:ffe538682dc19cc542ae7c3e504fdf54ca7f86fb8a135e59dd6bc8627eae6cce \</li>
<li>              --hash=sha256:ec29604081f10f16a7aea809ad42e27764188fc258b02259a03a8ff7ded3808d \</li>
<li>              --hash=sha256:0a80dd307a5d8440b0a08bd7b81617e04d870e40a3e46a32d9c246e54705e86f \</li>
<li>              --hash=sha256:06aba4169e78c439d528fdeb34762c3b61a70813527a2c57f0540541e9f433a8</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Fernando (2020-11-06 16:55 UTC)

<p>Hi, <a class="mention" href="/u/jamesobutler">@jamesobutler</a>.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="14448">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Does <code>from PIL import Image</code> not work from a fresh download of the current Slicer Stable?</p>
</blockquote>
</aside>
<p>Correct, it doesn’t. Here is a (hopefully) MWE:</p>
<pre data-code-wrap="bash"><code class="lang-bash">curl --silent --output slicer_stable_linux.tar.gz --location https://download.slicer.org/bitstream/1341035
tar zxf slicer_stable_linux.tar.gz
Slicer-4.11.20200930-linux-amd64/Slicer --ignore-slicerrc --no-splash --no-main-window -c "from PIL import Image"
</code></pre>
<p>Output:</p>
<pre data-code-wrap="python-traceback"><code class="lang-python-traceback">Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/tmp/Slicer-4.11.20200930-linux-amd64/lib/Python/lib/python3.6/site-packages/PIL/Image.py", line 94, in &lt;module&gt;
    from . import _imaging as core
ImportError: /tmp/Slicer-4.11.20200930-linux-amd64/lib/Python/lib/python3.6/site-packages/PIL/_imaging.cpython-36m-x86_64-linux-gnu.so: ELF load command address/offset not properly aligned
Info: In /work/Stable/Slicer-0/Libs/MRML/Core/vtkMRMLScene.cxx, line 316
vtkMRMLScene (0x2bc2420): vtkMRMLScene::Clear
</code></pre>

---

## Post #4 by @lassoan (2020-11-17 16:14 UTC)

<p>I had to apply this fix in the Slicer docker image to resolve this error:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/SlicerDocker/blob/275973c21dc70822ac0f70495baa6fc89b86a30a/slicer-notebook/install.sh#L56-L61" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/SlicerDocker/blob/275973c21dc70822ac0f70495baa6fc89b86a30a/slicer-notebook/install.sh#L56-L61" target="_blank" rel="noopener">Slicer/SlicerDocker/blob/275973c21dc70822ac0f70495baa6fc89b86a30a/slicer-notebook/install.sh#L56-L61</a></h4>
<pre class="onebox"><code class="lang-sh"><ol class="start lines" start="56" style="counter-reset: li-counter 55 ;">
<li># Fix ImportError: ...python3.6/site-packages/PIL/_imaging.cpython-36m-x86_64-linux-gnu.so: ELF load command address/offset not properly aligned</li><li># by forcing reinstalling pillow (a properly maintained fork of PIL).</li><li>$slicer_executable \</li><li>  --disable-cli-modules \</li><li>  --disable-scripted-loadable-modules \</li><li>  -c "pip_install('--upgrade pillow --force-reinstall'); pip_install('ipywidgets pandas ipyevents ipycanvas')"</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #5 by @jcfr (2020-11-17 17:13 UTC)

<p>To address the problem with the latest stable, the following should be done:</p>
<pre><code class="lang-auto">cd Slicer-4.11.20200930-linux-amd64
./bin/PythonSlicer -c "from slicer.util import pip_install; pip_install('--upgrade pillow --force-reinstall')"
</code></pre>
<h3>Before</h3>
<pre><code class="lang-auto">./bin/PythonSlicer -c "import PIL; print(PIL.__version__); from PIL import Image"
7.2.0
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/home/jcfr/Downloads/Slicer-4.11.0-2020-09-30-linux-amd64/lib/Python/lib/python3.6/site-packages/PIL/Image.py", line 94, in &lt;module&gt;
    from . import _imaging as core
ImportError: /home/jcfr/Downloads/Slicer-4.11.0-2020-09-30-linux-amd64/lib/Python/lib/python3.6/site-packages/PIL/_imaging.cpython-36m-x86_64-linux-gnu.so: ELF load command address/offset not properly aligned
</code></pre>
<h3>After</h3>
<pre><code class="lang-auto">./bin/PythonSlicer -c "import PIL; print(PIL.__version__); from PIL import Image"
8.0.1
</code></pre>

---

## Post #6 by @Fernando (2020-12-10 09:21 UTC)

<p>This is also happening with <code>scipy</code>. Shall I open an issue about this on GitHub?</p>

---

## Post #7 by @Sam_Horvath (2021-02-15 22:57 UTC)

<p>The same workaround will work for scipy.  It would be great if you could open an issue.</p>

---

## Post #8 by @Fernando (2021-02-23 16:13 UTC)

<p>I just saw this. I suppose this can be tracked in <a href="https://github.com/Slicer/Slicer/issues/5474" class="inline-onebox" rel="noopener nofollow ugc">Importing the numpy C-extensions failed. [slicer 4.11.20200930, archlinux] · Issue #5474 · Slicer/Slicer · GitHub</a></p>

---
