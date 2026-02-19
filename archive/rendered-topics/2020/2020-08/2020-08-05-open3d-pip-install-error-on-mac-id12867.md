---
topic_id: 12867
title: "Open3D Pip Install Error On Mac"
date: 2020-08-05
url: https://discourse.slicer.org/t/12867
---

# Open3d pip_install error on Mac

**Topic ID**: 12867
**Date**: 2020-08-05
**URL**: https://discourse.slicer.org/t/open3d-pip-install-error-on-mac/12867

---

## Post #1 by @smrolfe (2020-08-05 21:40 UTC)

<p>I’ve been installing open3d on my Mac Catalina using:</p>
<p><code>slicer.util.pip_install('open3d==0.9.0')</code></p>
<p>with no problem up until about 2 days ago. With today’s preview I’m getting the following errors:</p>
<pre><code>/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc -pthread -Wall -g -fPIC -msse2 -Iextras/libargon2/src/../include -Iextras/libargon2/src/blake2 -c extras/libargon2/src/argon2.c -o build/temp.macosx-10.13-x86_64-3.6/extras/libargon2/src/argon2.o
  extras/libargon2/src/argon2.c:18:10: fatal error: 'string.h' file not found
  #include &lt;string.h&gt;
           ^~~~~~~~~~
  1 error generated.
  error: command '/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc' failed with exit status 1
  ----------------------------------------
  ERROR: Failed building wheel for argon2-cffi
Failed to build argon2-cffi
ERROR: Could not build wheels for argon2-cffi which use PEP 517 and cannot be installed directly
WARNING: You are using pip version 20.1.1; however, version 20.2.1 is available.
You should consider upgrading via the '/Applications/Slicer.app/Contents/bin/./python-real -m pip install --upgrade pip' command.
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "/Applications/Slicer.app/Contents/bin/Python/slicer/util.py", line 2444, in pip_install
    _executePythonModule('pip', args)
  File "/Applications/Slicer.app/Contents/bin/Python/slicer/util.py", line 2420, in _executePythonModule
    logProcessOutput(proc)
  File "/Applications/Slicer.app/Contents/bin/Python/slicer/util.py", line 2392, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['/Applications/Slicer.app/Contents/bin/../bin/PythonSlicer', '-m', 'pip', 'install', 'open3d==0.9.0']' returned non-zero exit status 1.
</code></pre>
<p>The first version where I can replicate this issue is from 2 days ago. The Windows preview versions install with no problem.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> I believe you are using open3d on a Mac, is this something you’ve seen?</p>

---

## Post #2 by @pieper (2020-08-05 22:08 UTC)

<p>Hi <a class="mention" href="/u/smrolfe">@smrolfe</a> - I’ve been using open3d on windows, where this problem doesn’t happen.</p>
<p>But I think I recognize the issue.  Mac no longer have the standard headers in /usr/include, so you need to set this variable in your environment when you start Slicer:</p>
<p><code>export SDKROOT=/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.15.sdk</code></p>
<p>The only change I can think is that this is a side effect of turning off the <a href="https://github.com/Slicer/Slicer/commit/7c6039021224cf1e9a1d594d9b258ab12e8e6e74">ParameterSerializer</a>, but that was a week ago now.  Are you sure it’s a change in Slicer and not something else?</p>
<p>More info at this issue:</p>
<p><a href="https://mantisarchive.slicer.org/view.php?id=4681">https://mantisarchive.slicer.org/view.php?id=4681</a> (old mantis link)</p>
<p>Git follow up:<br>
</p><aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/issues/4681" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/4681" target="_blank" rel="noopener">No /usr/include on macOS Mojave</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-13" data-time="01:05:06" data-timezone="UTC">01:05AM - 13 Mar 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2020-06-05" data-time="14:11:38" data-timezone="UTC">02:11PM - 05 Jun 20 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/slicerbot" target="_blank" rel="noopener">
          <img alt="slicerbot" src="https://avatars3.githubusercontent.com/u/10277015?v=4" class="onebox-avatar-inline" width="20" height="20">
          slicerbot
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">This issue was created automatically from an original Mantis Issue. Further discussion may take place here.</p>
</div>

<div class="labels">
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @smrolfe (2020-08-05 22:25 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a> I went back and tried some archived versions and the first one with this problem is 4.11.0-2020-07-24 r29227 / 38b40eb from 6 days ago.</p>

---

## Post #4 by @jamesobutler (2020-08-05 22:28 UTC)

<p>I installed Open3D on Windows and observed that it had to install a whole bunch of packages where some specify specific dependency versions and others don’t.</p>
<blockquote>
<p>Installing collected packages: parso, jedi, backcall, wcwidth, prompt-toolkit, decorator, pygments, colorama, pickleshare, ipython-genutils, traitlets, ipython, tornado, pywin32, jupyter-core, python-dateutil, pyzmq, jupyter-client, ipykernel, prometheus-client, pywinpty, terminado, MarkupSafe, jinja2, pycparser, cffi, argon2-cffi, Send2Trash, zipp, importlib-metadata, attrs, pyrsistent, jsonschema, nbformat, testpath, webencodings, bleach, defusedxml, mistune, entrypoints, pandocfilters, nbconvert, notebook, widgetsnbextension, ipywidgets, open3d</p>
</blockquote>
<p>In this case the <code>notebook</code> package starting with version 6.1.0 added the <code>argon2-cffi</code> dependency which doesn’t have a macOS wheel available for the latest release which is why it had to build a wheel from source which it failed at in your output.  Notebook version 6.1.0 was released July 31st which explains why you ran into this issue just recently.</p>

---

## Post #5 by @smrolfe (2020-08-05 22:44 UTC)

<p>Thanks <a class="mention" href="/u/jamesobutler">@jamesobutler</a> that makes sense. I had fixed my Open3D version, but did not check for changes in the dependancies.</p>
<p>To test this, I installed the previous version of Notebook first:</p>
<pre><code>slicer.util.pip_install('notebook==6.0.3')
slicer.util.pip_install('open3d==0.9.0')
</code></pre>
<p>And it now installs without error. I think this solution will work for now.</p>

---

## Post #6 by @pieper (2020-08-05 23:31 UTC)

<p>Great detective work!</p>

---
