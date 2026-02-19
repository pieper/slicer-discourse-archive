---
topic_id: 15823
title: "Is Slicerjupyter Broken On Macos Due To Argon2 Cffi Again"
date: 2021-02-03
url: https://discourse.slicer.org/t/15823
---

# Is SlicerJupyter broken on macOS due to argon2-cffi (again?)

**Topic ID**: 15823
**Date**: 2021-02-03
**URL**: https://discourse.slicer.org/t/is-slicerjupyter-broken-on-macos-due-to-argon2-cffi-again/15823

---

## Post #1 by @pll_llq (2021-02-03 21:12 UTC)

<p>Hi,</p>
<p>This problem was mentioned here on the forum a couple of times already and some fixes that were made actually worked just a month ago.</p>
<p>Forum posts:</p><aside class="quote quote-modified" data-post="6" data-topic="15082">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/a87d85/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/problems-running-slicerjupyter-on-macos/15082/6">Problems running SlicerJupyter on MacOS</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Solved! I reinstalled and it launched right into the localhost webpage for Jupyter notebook. I was also able to update pip by calling PythonSlicer instead of python-real. Perhaps this warrants an update of the warning output? 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/650e77a78c8b4ad4a9308ae6927c09212bfa5bd5.jpeg" data-download-href="/uploads/short-url/epZdGFuAxCaDJ4uXOyMGNVBe0wl.jpeg?dl=1" title="image" rel="noopener nofollow ugc">[image]</a> 

Collecting pillow 
Using cached Pillow-8.0.1-cp36-cp36m-macosx_10_10_x86_64.whl (2.2 MB) 
Installing collected packages: pillow 
Attempting uninstall: pillow 
Found existing installation: Pillow 8.0.1 
Uninstalling Pillow-8.0.1: 
Successfully uninstalled Pillow-…
  </blockquote>
</aside>
<aside class="quote quote-modified" data-post="15" data-topic="13386">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/y/a6a055/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/slicer-jupyter-integration-installing-python-packages/13386/15">Slicer/Jupyter integration: installing python packages</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Pandas has no problem, but ipycanvas, ipywidgets, and ipyevents all give the same error message below, and when I try the command suggested in the warning in terminal, it aborts it 
[errormessage2]
  </blockquote>
</aside>
<aside class="quote quote-modified" data-post="4" data-topic="12867">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/open3d-pip-install-error-on-mac/12867/4">Open3d pip_install error on Mac</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I installed Open3D on Windows and observed that it had to install a whole bunch of packages where some specify specific dependency versions and others don’t. 

Installing collected packages: parso, jedi, backcall, wcwidth, prompt-toolkit, decorator, pygments, colorama, pickleshare, ipython-genutils, traitlets, ipython, tornado, pywin32, jupyter-core, python-dateutil, pyzmq, jupyter-client, ipykernel, prometheus-client, pywinpty, terminado, MarkupSafe, jinja2, pycparser, cffi, argon2-cffi, Send2T…
  </blockquote>
</aside>

<p>Commit that addressed the issue</p><aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/SlicerJupyter/commit/75d59c38eafebc9a380b7f82571ba92d35d2d15c">
  <header class="source">

      <a href="https://github.com/Slicer/SlicerJupyter/commit/75d59c38eafebc9a380b7f82571ba92d35d2d15c" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/SlicerJupyter</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/SlicerJupyter/commit/75d59c38eafebc9a380b7f82571ba92d35d2d15c" target="_blank" rel="noopener nofollow ugc">re #39: Bundle argon2-cffi python package</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2020-12-17" data-time="05:37:57" data-timezone="UTC">05:37AM - 17 Dec 20 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener nofollow ugc">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="changed 2 files with 9 additions and 1 deletions">
        <a href="https://github.com/Slicer/SlicerJupyter/commit/75d59c38eafebc9a380b7f82571ba92d35d2d15c" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+9</span>
          <span class="removed">-1</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This package is needed to run Jupyter server inside Slicer and no wheels are ava<span class="show-more-container"><a href="https://github.com/Slicer/SlicerJupyter/commit/75d59c38eafebc9a380b7f82571ba92d35d2d15c" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">ilable for Python-3.6.7 on Mac.
If Python version in Slicer is updated then this package may be removed from the extension.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I was using Jupyter Lab inside Slicer in December and January. To my big surprize when I tried to setup a jupyter environment in the freshly downloaded Nightly build the problem came back.<br>
Jupyter notebook server doesn’t launch from inside slicer and jupyter lab cannot be installed because it can’t build argon2-cffi.<br>
So the workaround of installing an older version of notebook (6.0.3) works for the notebook server and Jupyter Lab can be installed after that, but now it stopped running. So the workaround doesn’t work any more.</p>
<pre><code class="lang-auto">File "/Applications/MedicalImaging/Slicer.app/Contents/lib/Python/lib/python3.6/sysconfig.py", line 421, in _init_posix
    _temp = __import__(name, globals(), locals(), ['build_time_vars'], 0)
ModuleNotFoundError: No module named '_sysconfigdata__darwin_darwin'
Traceback (most recent call last):
</code></pre>
<p>The funny thing that just about a month ago I was simply running jupyterlab inside slicer with all the nice plugins working “out of the box”.</p>
<p>What would be the advice to solve this? Build, maintain and manually install the macOS wheels for python3.6 or wait a little because support for python 3.7+ is coming during in some foreseeable future?<br>
Maybe there is some other solution?</p>

---

## Post #2 by @jamesobutler (2021-02-03 21:39 UTC)

<p>For <code>argon2-cffi</code> specifically, there are only wheels available on PyPI for Python 2.7 and Python 3.7 specifically. In the forseeable future we would be updating to probably the latest stable release of Python which is 3.9 at the moment.  Therefore I don’t think you’re going to have any long term success installing this package with a wheel from PyPI on macOS. It doesn’t appear that is priority for maintainers of that package to create wheels on Intel mac or Apple silicon mac.</p>
<p>I’m not sure what the factory build machine is doing to manually build <code>argon2-cffi</code> and what the macOS compatibility is for the wheel it is making. <a class="mention" href="/u/lassoan">@lassoan</a> Was it built manually on the factory?</p>

---

## Post #3 by @pll_llq (2021-02-03 21:50 UTC)

<p>Thanks for the input <a class="mention" href="/u/jamesobutler">@jamesobutler</a><br>
I don’t run into argon2-cffi issues when using jupyter lab for data science tasks in python 3.9 outside slicer. I use pip in that environment and <code>argon2_cffi-20.1.0-cp37-abi3-macosx_10_6_intel.whl</code> works fine.</p>

---

## Post #4 by @pll_llq (2021-02-03 21:57 UTC)

<p>A workaround that worked for me just now is to use the Slicer kernel from Jupyter Lab that’s installed outside of Slicer.</p>

---

## Post #5 by @lassoan (2021-02-04 02:17 UTC)

<p>I’ve added argon2-cffi Python package to the SlicerJupyter extension In December. I’ve just installed latest Slicer Preview Release on a macOS system and Jupyter server from Slicer’s Python environment (started by the JupyterKernel module) worked well.</p>
<p>Last time I updated xeus it had some incompatibility issues with latest jedi. These issues were resolved, so I now <a href="https://github.com/Slicer/SlicerJupyter/commit/93d12ddfb35d21bdfb873325a2b6f6a787ef6ae9#diff-22624a9f5056e473738160e13b432c9ad12b653e3fcd274885c392f7a7c0cbfb">updated xeus and all dependencies to their latest stable version</a>. I’ve tested and it works on Windows. It would be great if you could test SlicerJupyter in the Slicer Preview Release tomorrow on macOS and linux.</p>

---

## Post #6 by @pll_llq (2021-02-04 20:45 UTC)

<p>Hey <a class="mention" href="/u/lassoan">@lassoan</a> , I’ve just downloaded the .dmg that’s available on Slicer website as the nightly build (version 2020-02-03) and when I install JupyterKernel from the extension manager and press “Launch notebook server” button in the extension UI the error is printed to the python console <a href="https://gist.github.com/piiq/7bbf45de0fe8748ed950044460ba0e8c" rel="noopener nofollow ugc">full log here</a>.</p>
<p>The workaround that works for me on macOS 11.1:</p>
<ol start="0">
<li>Install JupyterKernel extension</li>
<li>Manually install older version of jupyter notebook via python interpreter (<code>pip_install('notebook=6.0.3')</code>)</li>
<li>Install jupyter lab with all the perks in an environment outside slicer (a brew-python venv for example)</li>
<li>Register a new kernel in the external environment using the command from the JupyterKernel Slicer module UI. The kernel should appear on the launcher page and in kernel selection dropdown menus as Slicer-4.13)</li>
<li>Use the Slicer 4.13 kernel to connect to the slicer environment from Jupyter Lab</li>
</ol>
<p>I assume that moving to a more recent version of python will fix this issue and this migration is “around the corner”. I would love to help testing this out.</p>

---

## Post #7 by @lassoan (2021-02-05 03:12 UTC)

<p>argon2-cffi is included in the <a href="http://slicer.kitware.com/midas3/api/rest?method=midas.bitstream.download&amp;name=29684-macosx-amd64-SlicerJupyter-git93d12dd-2021-02-03.tar.gz&amp;checksum=bba20c798d12d20b98b5ba723ea9b2af">extension package</a>.</p>
<p>The regression is caused by the recent update of Slicer that makes is a portable application.</p>
<p>It seems that the launcher converts relative paths to absolute paths differently depending on how Slicer is started. After installing latest Slicer Preview Release and installing SlicerJupyter extension, result of <code>import sys; sys.path</code> is the following:</p>
<p>If you start /⁨Applications⁩/Slicer-20210203.app/⁨Contents/⁨MacOS⁩ from a terminal:</p>
<blockquote>
<p>[‘/Applications/Slicer-20210203.app/Contents/bin/Python/slicer’, ‘/Applications/Slicer-20210203.app/Contents/MacOS/Extensions-29684/SlicerJupyter/lib/Slicer-4.13/qt-scripted-modules’, ‘/Applications/Slicer-20210203.app/Contents/MacOS/Extensions-29684/SlicerJupyter/lib/python3.6/site-packages’, ‘/Applications/Slicer-20210203.app/Contents/lib/Slicer-4.13’, ‘/Applications/Slicer-20210203.app/Contents/lib/Slicer-4.13/qt-scripted-modules’, ‘/Applications/Slicer-20210203.app/Contents/lib/Slicer-4.13/qt-loadable-modules’, ‘/Applications/Slicer-20210203.app/Contents/lib/vtkTeem’, ‘/Applications/Slicer-20210203.app/Contents/bin/Python’, ‘/Applications/Slicer-20210203.app/Contents/lib/Slicer-4.13/qt-loadable-modules/Python’, ‘/Applications/Slicer-20210203.app/Contents/lib/Python/lib/python3.6’, ‘/Applications/Slicer-20210203.app/Contents/lib/Python/lib/python3.6/lib-dynload’, ‘/Applications/Slicer-20210203.app/Contents/lib/Python/lib/python3.6/site-packages’, ‘/Applications/Slicer-20210203.app/Contents/lib/Python/lib/python36.zip’, ‘/Applications/Slicer-20210203.app/Contents/lib/Python/lib/python3.6/plat-darwin’, ‘/Applications/Slicer-20210203.app/Contents/lib/Python/lib/python3.6/lib-tk’, ‘/Applications/Slicer-20210203.app/Contents/lib/Python/lib/python3.6/site-packages/SimpleITK-2.0.1-py3.6-macosx-10.13-x86_64.egg’, ‘/Applications/Slicer-20210203.app/Contents/Extensions-29684/SlicerJupyter/lib/Slicer-4.13/qt-scripted-modules’, ‘/Applications/Slicer-20210203.app/Contents/lib/Slicer-4.13/qt-scripted-modules/SubjectHierarchyPlugins’, ‘/Applications/Slicer-20210203.app/Contents/Extensions-29684/SlicerJupyter/lib/Slicer-4.13/qt-loadable-modules’, ‘/Applications/Slicer-20210203.app/Contents/Extensions-29684/SlicerJupyter/lib/Slicer-4.13/qt-loadable-modules’]</p>
</blockquote>
<p>If you double-click on Slicer-20210203 in the Finder:</p>
<blockquote>
<p>[‘/Applications/Slicer-20210203.app/Contents/bin/Python/slicer’, ‘/Extensions-29684/SlicerJupyter/lib/Slicer-4.13/qt-scripted-modules’, ‘/Extensions-29684/SlicerJupyter/lib/python3.6/site-packages’, ‘/Applications/Slicer-20210203.app/Contents/lib/Slicer-4.13’, ‘/Applications/Slicer-20210203.app/Contents/lib/Slicer-4.13/qt-scripted-modules’, ‘/Applications/Slicer-20210203.app/Contents/lib/Slicer-4.13/qt-loadable-modules’, ‘/Applications/Slicer-20210203.app/Contents/lib/vtkTeem’, ‘/Applications/Slicer-20210203.app/Contents/bin/Python’, ‘/Applications/Slicer-20210203.app/Contents/lib/Slicer-4.13/qt-loadable-modules/Python’, ‘/Applications/Slicer-20210203.app/Contents/lib/Python/lib/python3.6’, ‘/Applications/Slicer-20210203.app/Contents/lib/Python/lib/python3.6/lib-dynload’, ‘/Applications/Slicer-20210203.app/Contents/lib/Python/lib/python3.6/site-packages’, ‘/Applications/Slicer-20210203.app/Contents/lib/Python/lib/python36.zip’, ‘/Applications/Slicer-20210203.app/Contents/lib/Python/lib/python3.6/plat-darwin’, ‘/Applications/Slicer-20210203.app/Contents/lib/Python/lib/python3.6/lib-tk’, ‘/Applications/Slicer-20210203.app/Contents/lib/Python/lib/python3.6/site-packages/SimpleITK-2.0.1-py3.6-macosx-10.13-x86_64.egg’, ‘/Applications/Slicer-20210203.app/Contents/Extensions-29684/SlicerJupyter/lib/Slicer-4.13/qt-scripted-modules’, ‘/Applications/Slicer-20210203.app/Contents/lib/Slicer-4.13/qt-scripted-modules/SubjectHierarchyPlugins’, ‘/Applications/Slicer-20210203.app/Contents/Extensions-29684/SlicerJupyter/lib/Slicer-4.13/qt-loadable-modules’, ‘/Applications/Slicer-20210203.app/Contents/Extensions-29684/SlicerJupyter/lib/Slicer-4.13/qt-loadable-modules’]</p>
</blockquote>
<p>Note the incorrect path of site-packages:</p>
<ul>
<li>started from terminal: <code>/Applications/Slicer-20210203.app/Contents/MacOS/Extensions-29684/SlicerJupyter/lib/python3.6/site-packages</code> → there is an extra <code>MacOS</code></li>
<li>started from Finder: <code>/Extensions-29684/SlicerJupyter/lib/python3.6/site-packages</code> → missing <code>/Applications/Slicer-20210203.app/Contents</code></li>
</ul>
<p>Since the site-packages folder path is incorrect, pip cannot to find the existing argon2 package and that’s why it tries to build it.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> Could you have a look at this? Do you know what can cause the different behavior? Probably this single line needs to be changed but I don’t know how the launcher works on macOS and what would be the proper path to use:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/commontk/AppLauncher/blob/9931394cf50c72083ab0b20ea443f1cc591f7752/Base/ctkAppLauncher.cpp#L545">
  <header class="source">

      <a href="https://github.com/commontk/AppLauncher/blob/9931394cf50c72083ab0b20ea443f1cc591f7752/Base/ctkAppLauncher.cpp#L545" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/commontk/AppLauncher/blob/9931394cf50c72083ab0b20ea443f1cc591f7752/Base/ctkAppLauncher.cpp#L545" target="_blank" rel="noopener">commontk/AppLauncher/blob/9931394cf50c72083ab0b20ea443f1cc591f7752/Base/ctkAppLauncher.cpp#L545</a></h4>



    <pre class="onebox"><code class="lang-cpp">
      <ol class="start lines" start="535" style="counter-reset: li-counter 534 ;">
          <li>foreach(const QString&amp; path, paths)</li>
          <li>  {</li>
          <li>  if (path.isEmpty())</li>
          <li>    {</li>
          <li>    continue;</li>
          <li>    }</li>
          <li>  QFileInfo fileInfo(path);</li>
          <li>  if (fileInfo.isRelative())</li>
          <li>    {</li>
          <li>    // make absolute path by appending to SlicerHome</li>
          <li class="selected">    absolutePaths &lt;&lt; QDir(q-&gt;launcherDir()).filePath(path);</li>
          <li>    }</li>
          <li>  else</li>
          <li>    {</li>
          <li>    // already absolute path</li>
          <li>    absolutePaths &lt;&lt; path;</li>
          <li>    } </li>
          <li>  }</li>
          <li>QString value = absolutePaths.join(this-&gt;PathSep);</li>
          <li>this-&gt;reportInfo(QString("Setting env. variable [%1]:%2").arg(key, value));</li>
          <li>if (env.contains(key))</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #8 by @jcfr (2021-02-11 05:43 UTC)

<p>This issue described by <a class="mention" href="/u/lassoan">@lassoan</a> has been fixed in</p>
<aside class="onebox githubcommit">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/commit/bdd75f0f2fc175b1e50ff5db2e1ad5904fa0f98e" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/bdd75f0f2fc175b1e50ff5db2e1ad5904fa0f98e" target="_blank" rel="noopener">BUG: Update CTKAppLauncher from 0.1.28 to 29 to fix extension loading on macOS</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2021-02-11" data-time="05:31:48" data-timezone="UTC">05:31AM - 11 Feb 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener">
          <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
        
      </div>

      <div class="lines" title="changed 3 files with 6 additions and 6 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/bdd75f0f2fc175b1e50ff5db2e1ad5904fa0f98e" target="_blank" rel="noopener">
          <span class="added">+6</span>
          <span class="removed">-6</span>
        </a>
      </div>
    </div>

  </div>
</div>


  <div class="github-row">
    <pre class="github-content" style="white-space: normal;">This commit updates the launcher to ensure relative paths are property
resolved by prepending the launcher directory when found in extension
settings files...</pre>
  </div>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #9 by @lassoan (2021-02-11 19:16 UTC)

<p>Thanks a lot <a class="mention" href="/u/jcfr">@jcfr</a>!</p>
<p><a class="mention" href="/u/pll_llq">@pll_llq</a> could you test if Jupyter launches correctly (without the need of setting up an external Python environment) in the Slicer Preview Release that you download tomorrow or later? Thank you.</p>

---

## Post #10 by @pll_llq (2021-02-12 12:10 UTC)

<p>Hi, Just tested this on 4.13.0-2021-02-11.<br>
There’s no problems with argon2-cffi but the Notebook server didn’t launch.<br>
The pip part of the install process went OK but the launch failed on a later stage (when jupyter tries to enable the ipyevents extension)</p>
<pre><code class="lang-auto">subprocess.CalledProcessError: Command '['/Applications/MedicalImaging/Slicer.app/Contents/bin/../bin/PythonSlicer', '-m', 'jupyter', 'nbextension', 'enable', '--py', 'ipyevents']' returned non-zero exit status 1.
</code></pre>
<p>because of</p>
<pre><code class="lang-auto">ImportError: dlopen(/Applications/MedicalImaging/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/zmq/backend/cython/constants.cpython-36m-darwin.so, 1): Library not loaded: @loader_path/../../.dylibs/libzmq.5.dylib
  Referenced from: /Applications/MedicalImaging/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/zmq/backend/cython/constants.cpython-36m-darwin.so
  Reason: Incompatible library version: constants.cpython-36m-darwin.so requires version 8.0.0 or later, but libzmq.5.dylib provides version 5.0.0
</code></pre>
<p>Full log <a href="https://gist.github.com/piiq/5087bf13d647ada2b61e18eafd668189" rel="noopener nofollow ugc">here</a></p>

---

## Post #11 by @jcfr (2021-02-14 03:39 UTC)

<aside class="quote no-group" data-username="pll_llq" data-post="10" data-topic="15823">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pll_llq/48/9408_2.png" class="avatar"> pll_llq:</div>
<blockquote>
<p><code>Reason: Incompatible library version: constants.cpython-36m-darwin.so requires version 8.0.0 or later, but libzmq.5.dylib provides version 5.0.0</code></p>
</blockquote>
</aside>
<p>Look like we need to update zmq library here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/SlicerJupyter/blob/93d12ddfb35d21bdfb873325a2b6f6a787ef6ae9/SuperBuild/External_ZeroMQ.cmake#L29">
  <header class="source">

      <a href="https://github.com/Slicer/SlicerJupyter/blob/93d12ddfb35d21bdfb873325a2b6f6a787ef6ae9/SuperBuild/External_ZeroMQ.cmake#L29" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/SlicerJupyter/blob/93d12ddfb35d21bdfb873325a2b6f6a787ef6ae9/SuperBuild/External_ZeroMQ.cmake#L29" target="_blank" rel="noopener">Slicer/SlicerJupyter/blob/93d12ddfb35d21bdfb873325a2b6f6a787ef6ae9/SuperBuild/External_ZeroMQ.cmake#L29</a></h4>



    <pre class="onebox"><code class="lang-cmake">
      <ol class="start lines" start="19" style="counter-reset: li-counter 18 ;">
          <li>if(NOT DEFINED ${proj}_DIR AND NOT ${CMAKE_PROJECT_NAME}_USE_SYSTEM_${proj})</li>
          <li></li>
          <li>  ExternalProject_SetIfNotDefined(</li>
          <li>    ${CMAKE_PROJECT_NAME}_${proj}_GIT_REPOSITORY</li>
          <li>    "${EP_GIT_PROTOCOL}://github.com/zeromq/libzmq.git"</li>
          <li>    QUIET</li>
          <li>    )</li>
          <li></li>
          <li>  ExternalProject_SetIfNotDefined(</li>
          <li>    ${CMAKE_PROJECT_NAME}_${proj}_GIT_TAG</li>
          <li class="selected">    "v4.3.2"</li>
          <li>    QUIET</li>
          <li>    )</li>
          <li></li>
          <li>  set(EP_SOURCE_DIR ${CMAKE_BINARY_DIR}/${proj})</li>
          <li>  set(EP_BINARY_DIR ${CMAKE_BINARY_DIR}/${proj}-build)</li>
          <li>    </li>
          <li>  ExternalProject_Add(${proj}</li>
          <li>    ${${proj}_EP_ARGS}</li>
          <li>    GIT_REPOSITORY "${${CMAKE_PROJECT_NAME}_${proj}_GIT_REPOSITORY}"</li>
          <li>    GIT_TAG "${${CMAKE_PROJECT_NAME}_${proj}_GIT_TAG}"</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #12 by @lassoan (2021-02-14 20:58 UTC)

<p>I’ve updated to latest version (v4.3.4) and unfortunately nothing has changed. <a class="mention" href="/u/jcfr">@jcfr</a> do you have any idea what could be the issue?</p>

---

## Post #13 by @pll_llq (2021-02-16 19:08 UTC)

<p>I’ve tried to test SlicerJupyter on linux to validate that the problem is mac-only, but on on the latest nightly the extension was not mentioned in the extension manager. Was it taken down, or is there something I’m missing on linux?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4abc6bf15562fc40c42dc4503a8d8bc38e6593a0.jpeg" data-download-href="/uploads/short-url/aF91vyHgo7jDGhSgoqdyk6SY0EM.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4abc6bf15562fc40c42dc4503a8d8bc38e6593a0_2_687x500.jpeg" alt="image" data-base62-sha1="aF91vyHgo7jDGhSgoqdyk6SY0EM" width="687" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4abc6bf15562fc40c42dc4503a8d8bc38e6593a0_2_687x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4abc6bf15562fc40c42dc4503a8d8bc38e6593a0_2_1030x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4abc6bf15562fc40c42dc4503a8d8bc38e6593a0.jpeg 2x" data-dominant-color="DCE3E8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1260×916 194 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>p.s. this is a laptop with ubuntu 18</p>

---

## Post #14 by @lassoan (2021-02-16 19:33 UTC)

<p>You can monitor the status of all extension builds on the <a href="http://slicer.cdash.org/index.php?project=SlicerPreview">dashboard</a>.</p>
<p>It seems that gcc bails out on some type check (<code>xeus/src/xdap_tcp_client.cpp:192:44: error: no matching function for call to ‘zmq::message_t::message_t(std::string&amp;)’</code>). Probably upgrading xeus or downgrading zmq will fix the issue. I’ll have quick loook.</p>

---

## Post #15 by @lassoan (2021-02-17 00:46 UTC)

<p>There is a <a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=Jupyter">SlicerJupyter build error</a> on the linux factory:</p>
<pre><code class="lang-nohighlight">[  7%] Building CXX object CMakeFiles/xeus-static.dir/src/xdap_tcp_client.cpp.o
/.../SlicerJupyter-build/xeus/src/xdap_tcp_client.cpp: In member function ‘void xeus::xdap_tcp_client::init_tcp_socket(const string&amp;)’:
xeus/src/xdap_tcp_client.cpp:192:44: error: no matching function for call to ‘zmq::message_t::message_t(std::string&amp;)’
             m_socket_id = zmq::message_t(id);
                                            ^
In file included from cppzmq/zmq_addon.hpp:27:0,
                 from xeus/src/xdap_tcp_client.cpp:1:
</code></pre>
<p>Since I cannot reproduce the error on my linux machine (clean Ubuntu 20.04 install with freshly-built Slicer, with all default options) it is very hard to figure out what exactly is wrong and how to fix it.</p>
<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> Could you have a look at it? The fix may be as simple as adding some constant casting.</p>

---

## Post #16 by @Sam_Horvath (2021-02-17 14:15 UTC)

<p>Sure, I can take a look at it</p>

---

## Post #17 by @Sam_Horvath (2021-02-17 14:59 UTC)

<p>So:</p>
<p>Changing this line:</p><aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/jupyter-xeus/xeus/blob/3369bc7f1ced8d85c47a9a069677c8719557bc2e/src/xdap_tcp_client.cpp#L192" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/jupyter-xeus/xeus/blob/3369bc7f1ced8d85c47a9a069677c8719557bc2e/src/xdap_tcp_client.cpp#L192" target="_blank" rel="noopener nofollow ugc">jupyter-xeus/xeus/blob/3369bc7f1ced8d85c47a9a069677c8719557bc2e/src/xdap_tcp_client.cpp#L192</a></h4>
<pre class="onebox"><code class="lang-cpp"><ol class="start lines" start="182" style="counter-reset: li-counter 181 ;">
<li>    return zmq::message_t(m_socket_id.data&lt;const char&gt;(), m_socket_id.size());</li><li>}</li><li></li><li>void xdap_tcp_client::init_tcp_socket(const std::string&amp; tcp_end_point)</li><li>{</li><li>    if (m_dap_tcp_type == dap_tcp_type::client)</li><li>    {</li><li>        m_tcp_socket.connect(tcp_end_point);</li><li>        size_t id_size = 256;</li><li>        std::string id = m_tcp_socket.get(zmq::sockopt::routing_id, id_size);</li><li class="selected">        m_socket_id = zmq::message_t(id);</li><li>    }</li><li>    else</li><li>    {</li><li>        m_tcp_socket.bind(tcp_end_point);</li><li>        (void)m_tcp_socket.recv(m_socket_id);</li><li>        zmq::message_t msg;</li><li>        (void)m_tcp_socket.recv(msg);</li><li>    }</li><li>}</li><li></li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>to:</p>
<p><code>m_socket_id = zmq::message_t(id.data(), id.size());</code></p>
<p>fixes the build error.  The breaking change was introduced in SlicerJupyter here:</p><aside class="onebox githubcommit">
  <header class="source">
      <a href="https://github.com/Slicer/SlicerJupyter/commit/93d12ddfb35d21bdfb873325a2b6f6a787ef6ae9" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/SlicerJupyter</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/SlicerJupyter/commit/93d12ddfb35d21bdfb873325a2b6f6a787ef6ae9" target="_blank" rel="noopener nofollow ugc">Update xeus and all dependencies to latest stable versions</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2021-02-04" data-time="02:12:13" data-timezone="UTC">02:12AM - 04 Feb 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener nofollow ugc">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
        
      </div>

      <div class="lines" title="changed 6 files with 6 additions and 24 deletions">
        <a href="https://github.com/Slicer/SlicerJupyter/commit/93d12ddfb35d21bdfb873325a2b6f6a787ef6ae9" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+6</span>
          <span class="removed">-24</span>
        </a>
      </div>
    </div>

  </div>
</div>


  <div class="github-row">
    <pre class="github-content" style="white-space: normal;">Hopefully this solves some compatibility problems that a user reported on macOS</pre>
  </div>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>and in Xeus here:</p>
<aside class="onebox githubcommit">
  <header class="source">
      <a href="https://github.com/jupyter-xeus/xeus/commit/42a1e053d9ca2921ba3b9bba7b7c84075eaf10cf" target="_blank" rel="noopener nofollow ugc">github.com/jupyter-xeus/xeus</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/jupyter-xeus/xeus/commit/42a1e053d9ca2921ba3b9bba7b7c84075eaf10cf" target="_blank" rel="noopener nofollow ugc">Upgraded to cppzmq 4.7.1</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2020-11-07" data-time="06:05:10" data-timezone="UTC">06:05AM - 07 Nov 20 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/JohanMabille" target="_blank" rel="noopener nofollow ugc">
          <img alt="JohanMabille" src="https://avatars.githubusercontent.com/u/6754742?v=4" class="onebox-avatar-inline" width="20" height="20">
          JohanMabille
        </a>
        
      </div>

      <div class="lines" title="changed 10 files with 21 additions and 26 deletions">
        <a href="https://github.com/jupyter-xeus/xeus/commit/42a1e053d9ca2921ba3b9bba7b7c84075eaf10cf" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+21</span>
          <span class="removed">-26</span>
        </a>
      </div>
    </div>

  </div>
</div>




  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Why its breaking:  not sure.  There is a conversion constructor that should handle this:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/zeromq/cppzmq/blob/f428fee37426888532b55da152e99de510c8361a/zmq.hpp#L470" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/zeromq/cppzmq/blob/f428fee37426888532b55da152e99de510c8361a/zmq.hpp#L470" target="_blank" rel="noopener nofollow ugc">zeromq/cppzmq/blob/f428fee37426888532b55da152e99de510c8361a/zmq.hpp#L470</a></h4>
<pre class="onebox"><code class="lang-hpp"><ol class="start lines" start="460" style="counter-reset: li-counter 459 ;">
<li>             typename = typename std::enable_if&lt;</li><li>               detail::is_range&lt;Range&gt;::value</li><li>               &amp;&amp; ZMQ_IS_TRIVIALLY_COPYABLE(detail::range_value_t&lt;Range&gt;)</li><li>               &amp;&amp; !detail::is_char_type&lt;detail::range_value_t&lt;Range&gt;&gt;::value</li><li>               &amp;&amp; !std::is_same&lt;Range, message_t&gt;::value&gt;::type&gt;</li><li>    explicit message_t(const Range &amp;rng) :</li><li>        message_t(detail::ranges::begin(rng), detail::ranges::end(rng))</li><li>    {</li><li>    }</li><li></li><li class="selected">    explicit message_t(const std::string &amp;str) : message_t(str.data(), str.size()) {}</li><li></li><li>#if CPPZMQ_HAS_STRING_VIEW</li><li>    explicit message_t(std::string_view str) : message_t(str.data(), str.size()) {}</li><li>#endif</li><li></li><li>#endif</li><li></li><li>#ifdef ZMQ_HAS_RVALUE_REFS</li><li>    message_t(message_t &amp;&amp;rhs) ZMQ_NOTHROW : msg(rhs.msg)</li><li>    {</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>but it doesn’t seem to be.</p>

---

## Post #18 by @lassoan (2021-02-17 15:12 UTC)

<p>Thanks a lot <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a>, this is exactly the information I needed!</p>

---

## Post #19 by @lmcheukying (2021-09-05 09:12 UTC)

<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> I’m new to this. Cloud you please elaborate on how to solve the problem for mac users?</p>
<p>I also got the error message “Incompatible library version: constants.cpython-36m-darwin.so requires version 8.0.0 or later, but libzmq.5.dylib provides version 5.0.0” when I install “pip_install(‘jupyterlab’)<br>
slicer.util._executePythonModule(‘jupyter’,[‘labextension’,‘install’,’<span class="mention">@jupyter-widgets</span>/jupyterlab-manager’,‘ipycanvas’,‘ipyevents’])”.</p>
<p>You mentioned that we could change some lines to upgrade and solve this problem, but actually how to do that? like which file?</p>
<p>Thank you!</p>

---

## Post #20 by @pll_llq (2021-09-05 09:23 UTC)

<p>Hi, if you like using Jupyter Lab in general (not just for Slicer based research) and you have a Jupyter Lab environment on your local machine that you work with - you can create a Slicer Kernel for that local Jupyter Lab. It will be separate from Slicer but you will be able to use the Slicer environment from there.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4f98290ee48b2af930f586cf311ac86dbe8f1e1.png" data-download-href="/uploads/short-url/pOYw52RhTSTn42uvC2oVHPSaRS9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4f98290ee48b2af930f586cf311ac86dbe8f1e1_2_579x500.png" alt="image" data-base62-sha1="pOYw52RhTSTn42uvC2oVHPSaRS9" width="579" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4f98290ee48b2af930f586cf311ac86dbe8f1e1_2_579x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4f98290ee48b2af930f586cf311ac86dbe8f1e1_2_868x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4f98290ee48b2af930f586cf311ac86dbe8f1e1.png 2x" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1016×876 41.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This works for me just fine (apart from Jedi code completion being extremely slow on macOS for some reason).</p>
<p>You can install the Slicer kernel using the command that’s generated by the JupyterKernel extension. See the “Jupyter server in external Python environment” section of the module UI.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42f1a5e9a75d9028ab3e3b02a23f03f7c9499a20.png" data-download-href="/uploads/short-url/9ydeZ7WYc2CgGGe7WPnFfOZVpMk.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/42f1a5e9a75d9028ab3e3b02a23f03f7c9499a20_2_690x214.png" alt="image" data-base62-sha1="9ydeZ7WYc2CgGGe7WPnFfOZVpMk" width="690" height="214" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/42f1a5e9a75d9028ab3e3b02a23f03f7c9499a20_2_690x214.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/42f1a5e9a75d9028ab3e3b02a23f03f7c9499a20_2_1035x321.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42f1a5e9a75d9028ab3e3b02a23f03f7c9499a20.png 2x" data-dominant-color="EAEAEA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1150×358 38.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #21 by @lmcheukying (2021-09-05 09:38 UTC)

<p><a class="mention" href="/u/pll_llq">@pll_llq</a> I’m also using Jupyter Lab and created a Slicer Kernal from SlicerJupyter extension.</p>
<p>When I run “import JupyterNotebooksLib as slicernb slicernb.ViewDisplay()”, the content can be shown in Jupyter Lab.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/edacdc06d35684c373b0db6be8a9a9074571985f.jpeg" data-download-href="/uploads/short-url/xUzvDiiD8OgnJIAsYqcHG5Djyrl.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/edacdc06d35684c373b0db6be8a9a9074571985f_2_690x325.jpeg" alt="image" data-base62-sha1="xUzvDiiD8OgnJIAsYqcHG5Djyrl" width="690" height="325" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/edacdc06d35684c373b0db6be8a9a9074571985f_2_690x325.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/edacdc06d35684c373b0db6be8a9a9074571985f_2_1035x487.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/edacdc06d35684c373b0db6be8a9a9074571985f_2_1380x650.jpeg 2x" data-dominant-color="63606E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1814×856 60.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But when I try the interactive view widget “slicernb.ViewInteractiveWidget()”, it showed “Error displaying widget: model not found”. <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2cfa66b53eb3e1b065b6f06807638fc50352d585.png" alt="image" data-base62-sha1="6pTuqE7SlAqxPem25qHDLvujbI9" width="622" height="206"></p>
<p>I don’t know if it is related to the failed installation of  “pip_install(‘jupyterlab’)<br>
slicer.util._executePythonModule(‘jupyter’,[‘labextension’,‘install’,’<span class="mention">@jupyter-widgets</span>/jupyterlab-manager’,‘ipycanvas’,‘ipyevents’])”.</p>
<p>Do you have any idea to fix this problem?</p>

---

## Post #22 by @pll_llq (2021-09-05 09:45 UTC)

<p>AFAIK the interactive widget was made for the kernel to work in containers and with binder (<a class="mention" href="/u/lassoan">@lassoan</a> might correct me here). Those are environments where you don’t have direct access to the Slicer GUI. If you are using the local Slicer this interactivity is not expected to work inside the lab because you have full access to the actual Slicer GUI.</p>
<p>What is the environment you would like to set up? Are you using a local or a remote computer?</p>

---

## Post #23 by @lmcheukying (2021-09-05 09:51 UTC)

<p><a class="mention" href="/u/pll_llq">@pll_llq</a> I’m using a local computer. Is there any other way for me to use the interactive widget in my Jupyter Lab? Or it is impossible to do that?</p>

---

## Post #24 by @pll_llq (2021-09-05 09:58 UTC)

<p>You have full interactivity with the Slicer GUI. Is there any particular need to have interactivity in the Lab while the full Slicer GUI is around?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d843e40d98b1a5b58de3492a3790b48002a971df.jpeg" data-download-href="/uploads/short-url/uRaAwkesoZ3WlB1qLToUNPSKag7.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d843e40d98b1a5b58de3492a3790b48002a971df_2_690x412.jpeg" alt="image" data-base62-sha1="uRaAwkesoZ3WlB1qLToUNPSKag7" width="690" height="412" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d843e40d98b1a5b58de3492a3790b48002a971df_2_690x412.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d843e40d98b1a5b58de3492a3790b48002a971df_2_1035x618.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d843e40d98b1a5b58de3492a3790b48002a971df_2_1380x824.jpeg 2x" data-dominant-color="707073"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1147 128 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #25 by @lassoan (2021-09-05 19:39 UTC)

<p>You can get interactive 3D views at multiple levels.</p>
<ul>
<li>Level 1. View objects + standard widgets</li>
<li>Level 2. View widgets</li>
<li>Level 3. Interactive view widgets</li>
<li>Level 4. Remote application window view</li>
</ul>
<p>Level 1-3 works locally, without having to set up a remote desktop server. Level 4 only makes sense when you don’t have access to the desktop where 3D Slicer is running (e.g., when the notebook server is a cloud computer that you don’t have remote desktop access to - such as Binder).</p>

---
