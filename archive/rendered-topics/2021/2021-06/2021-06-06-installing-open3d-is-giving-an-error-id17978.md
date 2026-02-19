---
topic_id: 17978
title: "Installing Open3D Is Giving An Error"
date: 2021-06-06
url: https://discourse.slicer.org/t/17978
---

# Installing open3d is giving an error

**Topic ID**: 17978
**Date**: 2021-06-06
**URL**: https://discourse.slicer.org/t/installing-open3d-is-giving-an-error/17978

---

## Post #1 by @bcolbert (2021-06-06 20:22 UTC)

<p>I am attempting to use ALPACA. When using this tool for the first time I am prompted that open3D will be installed. I allow it do do this but then I get a series of errors which are beyond my ability to troubleshoot. Any suggestions would be very welcome.</p>
<pre><code class="lang-auto">o3d installed
Collecting git+https://github.com/agporto/pycpd.git@development
  Cloning https://github.com/agporto/pycpd.git (to revision development) to c:\users\ben\appdata\local\temp\pip-req-build-xye84wj1
  ERROR: Error [WinError 2] The system cannot find the file specified while executing command git clone -q https://github.com/agporto/pycpd.git 'C:\Users\Ben\AppData\Local\Temp\pip-req-build-xye84wj1'
ERROR: Cannot find command 'git' - do you have 'git' installed and in your PATH?
WARNING: You are using pip version 20.3.3; however, version 21.1.2 is available.
You should consider upgrading via the 'C:\Users\Ben\AppData\Local\NA-MIC\Slicer 4.11.20210226\bin\python-real.exe -m pip install --upgrade pip' command.
Traceback (most recent call last):
  File "C:/Users/Ben/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/SlicerMorph/lib/Slicer-4.11/qt-scripted-modules/ALPACA.py", line 60, in __init__
    from pycpd import DeformableRegistration
ModuleNotFoundError: No module named 'pycpd'
</code></pre>

---

## Post #2 by @bcolbert (2021-06-07 12:39 UTC)

<p>I am attempting to use ALPACA. When using this tool for the first time I am prompted that open3D will be installed. I allow it do do this but then I get a series of errors which are beyond my ability to troubleshoot. Any suggestions would be very welcome.</p>
<pre><code class="lang-auto">o3d installed
Collecting git+https://github.com/agporto/pycpd.git@development
  Cloning https://github.com/agporto/pycpd.git (to revision development) to c:\users\ben\appdata\local\temp\pip-req-build-xye84wj1
  ERROR: Error [WinError 2] The system cannot find the file specified while executing command git clone -q https://github.com/agporto/pycpd.git 'C:\Users\Ben\AppData\Local\Temp\pip-req-build-xye84wj1'
ERROR: Cannot find command 'git' - do you have 'git' installed and in your PATH?
WARNING: You are using pip version 20.3.3; however, version 21.1.2 is available.
You should consider upgrading via the 'C:\Users\Ben\AppData\Local\NA-MIC\Slicer 4.11.20210226\bin\python-real.exe -m pip install --upgrade pip' command.
Traceback (most recent call last):
  File "C:/Users/Ben/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/SlicerMorph/lib/Slicer-4.11/qt-scripted-modules/ALPACA.py", line 60, in __init__
    from pycpd import DeformableRegistration
ModuleNotFoundError: No module named 'pycpd'
</code></pre>

---

## Post #3 by @lassoan (2021-06-07 12:39 UTC)



---

## Post #4 by @muratmaga (2021-06-07 15:24 UTC)

<p><a class="mention" href="/u/bcolbert">@bcolbert</a><br>
For a brief period we used git to install open3d, which unfortunately wasn’t as commonly available. Looks like you installed the SlicerMorph during that time. Please update your SlicerMorph installation following <a href="https://github.com/SlicerMorph/SlicerMorph#updating-slicermorph">this instructions</a>.</p>
<p>Open the python window, and type or copy/paste these commands</p>
<pre><code class="lang-auto">pip_install('notebook==6.0.3')
pip_install('open3d==0.10.0')
pip_install('pycpd')
</code></pre>
<p>and then try using alpaca</p>

---

## Post #5 by @bcolbert (2021-06-08 09:44 UTC)

<p>Worked great. Thanks!</p>

---

## Post #6 by @bcolbert (2022-04-22 14:06 UTC)

<p>Sorry to revice an old post but I am having a similar error. When I run the command lines you suggested I now get an error on: pip_install(‘open3d==0.10.0’):</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "C:\Users\Benjamin Colbert\AppData\Local\NA-MIC\Slicer 4.13.0-2022-02-20\bin\Python\slicer\util.py", line 3155, in pip_install
    _executePythonModule('pip', args)
  File "C:\Users\Benjamin Colbert\AppData\Local\NA-MIC\Slicer 4.13.0-2022-02-20\bin\Python\slicer\util.py", line 3130, in _executePythonModule
    logProcessOutput(proc)
  File "C:\Users\Benjamin Colbert\AppData\Local\NA-MIC\Slicer 4.13.0-2022-02-20\bin\Python\slicer\util.py", line 3099, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['C:/Users/Benjamin Colbert/AppData/Local/NA-MIC/Slicer 4.13.0-2022-02-20/bin/../bin\\PythonSlicer.EXE', '-m', 'pip', 'install', 'open3d==0.10.0']' returned non-zero exit status 1.
</code></pre>
<p>Is there a solution to this?</p>

---

## Post #7 by @jamesobutler (2022-04-22 14:12 UTC)

<p>It appears you have switched from using Slicer 4.11.20210226 to now using Slicer 4.13.0-2022-02-20. This corresponds with a switch from Python 3.6 to Python 3.9. <code>open3d</code> does not have Python 3.9 whl files to install with version 0.10.0 as that version was released prior to Python 3.9 being released.</p>
<p>You should not manually install <code>open3d</code> if you are using a recent Slicer preview build. You should let the SlicerMorph extension install it for you when requested. I would suggest installing the latest Slicer Preview build as the one you currently have is about 2 months old now and also will get latest SlicerMorph.</p>

---

## Post #8 by @bcolbert (2022-04-22 16:15 UTC)

<p>I downloaded the new version, installed slicermorph and auto3dgm and then ran Alpaca and accepted the prompt for installing the open3d library and it hangs up and I get the following error in Python:</p>
<pre><code class="lang-auto">ERROR: Invalid requirement: 'C:/Users/Benjamin'
WARNING: You are using pip version 22.0.3; however, version 22.0.4 is available.
You should consider upgrading via the 'C:\Users\Benjamin Colbert\AppData\Local\NA-MIC\Slicer 4.13.0-2022-04-19\bin\python-real.exe -m pip install --upgrade pip' command.
Traceback (most recent call last):
  File "C:/Users/Benjamin Colbert/AppData/Local/NA-MIC/Slicer 4.13.0-2022-04-19/NA-MIC/Extensions-30789/SlicerMorph/lib/Slicer-4.13/qt-scripted-modules/ALPACA.py", line 147, in __init__
    slicer.util.pip_install(wheelPath)
  File "C:\Users\Benjamin Colbert\AppData\Local\NA-MIC\Slicer 4.13.0-2022-04-19\bin\Python\slicer\util.py", line 3363, in pip_install
    _executePythonModule('pip', args)
  File "C:\Users\Benjamin Colbert\AppData\Local\NA-MIC\Slicer 4.13.0-2022-04-19\bin\Python\slicer\util.py", line 3337, in _executePythonModule
    logProcessOutput(proc)
  File "C:\Users\Benjamin Colbert\AppData\Local\NA-MIC\Slicer 4.13.0-2022-04-19\bin\Python\slicer\util.py", line 3306, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['C:/Users/Benjamin Colbert/AppData/Local/NA-MIC/Slicer 4.13.0-2022-04-19/bin/../bin\\PythonSlicer.EXE', '-m', 'pip', 'install', 'C:/Users/Benjamin', 'Colbert/AppData/Local/NA-MIC/Slicer/cache/SlicerIO/open3d-0.14.1+816263b-cp39-cp39-win_amd64.whl']' returned non-zero exit status 1.

</code></pre>

---

## Post #9 by @jamesobutler (2022-04-22 16:59 UTC)

<aside class="quote no-group" data-username="bcolbert" data-post="8" data-topic="17978">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bcolbert/48/11162_2.png" class="avatar"> bcolbert:</div>
<blockquote>
<p><code>PythonSlicer.EXE', '-m', 'pip', 'install', 'C:/Users/Benjamin', 'Colbert/AppData/Local/NA-MIC/Slicer/cache/SlicerIO/open3d-0.14.1+816263b-cp39-cp39-win_amd64.whl']' returned non-zero exit status 1.</code></p>
</blockquote>
</aside>
<p>The problem originates due to a space located in the path (“Benjamin Colbert”) to the custom open3d-0.14.1 whl file that was installed. This space inappropriately leads it to be split into different arguments.</p>
<p>A quick workaround would be to relocate “C:/Users/Benjamin Colbert/AppData/Local/NA-MIC/Slicer/cache/SlicerIO/open3d-0.14.1+816263b-cp39-cp39-win_amd64.whl” to “C:/open3d-0.14.1+816263b-cp39-cp39-win_amd64.whl” and then do <code>slicer.util.pip_install(r"C:\open3d-0.14.1+816263b-cp39-cp39-win_amd64.whl")</code>.</p>

---

## Post #10 by @lassoan (2022-04-24 05:34 UTC)

<p>I’ve improved the <code>pip_install</code> function so that it supports installing a downloaded wheel from a folder that has spaces in the name. The path either has to be quoted or provided as a list:</p>
<pre><code class="lang-auto">wheelPath = 'C:/Users/Benjamin Colbert/AppData/Local/NA-MIC/Slicer/cache/SlicerIO/open3d-0.14.1+816263b-cp39-cp39-win_amd64.whl'

# Option A: Quote the string (quoted strings are not split)
slicer.util.pip_install(f'"{wheelPath}"')

# Option B: Provide arguments as list (input argument is not split)
slicer.util.pip_install([wheelPath])
</code></pre>
<p>SlicerMorph needs to be updated accordingly - I’ve submitted a fix:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/SlicerMorph/SlicerMorph/pull/206">
  <header class="source">

      <a href="https://github.com/SlicerMorph/SlicerMorph/pull/206" target="_blank" rel="noopener">github.com/SlicerMorph/SlicerMorph</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/SlicerMorph/SlicerMorph/pull/206" target="_blank" rel="noopener">Fix open3d install when cache folder name contains space</a>
    </h4>

    <div class="branches">
      <code>SlicerMorph:master</code> ← <code>lassoan:patch-2</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-04-24" data-time="05:35:37" data-timezone="UTC">05:35AM - 24 Apr 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="1 commits changed 1 files with 3 additions and 1 deletions">
        <a href="https://github.com/SlicerMorph/SlicerMorph/pull/206/files" target="_blank" rel="noopener">
          <span class="added">+3</span>
          <span class="removed">-1</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Fixes the issue of pip_install splitting up input wheel path at spaces.
See htt<span class="show-more-container"><a href="https://github.com/SlicerMorph/SlicerMorph/pull/206" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ps://discourse.slicer.org/t/installing-open3d-is-giving-an-error/17978/10?u=lassoan</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #11 by @muratmaga (2022-04-25 01:04 UTC)

<p>Thanks Andras. This is now merged.</p>

---
