# Open3d pip_install issue

**Topic ID**: 16377
**Date**: 2021-03-04
**URL**: https://discourse.slicer.org/t/open3d-pip-install-issue/16377

---

## Post #1 by @muratmaga (2021-03-04 20:05 UTC)

<p>Posting on behalf of a user.</p>
<p>They had a difficulty installing SlicerMorph extension. When we looked into it, the computer is in Greek locale (and the user folder contain greek alphabet letters). We tried installing C:\Slicer\Slicer 4.11.20210226.</p>
<p>As far as I can tell, Slicer works. But pip_install gives this error message.</p>
<p><strong>&gt;&gt;&gt; pip_install(‘open3d==0.10’)</strong></p>
<p><strong>error: Application does NOT exists [C:/Slicer/Slicer 4.11.20210226/bin/./python-real.exe]</strong></p>
<p>Usage</p>
<p>PythonSlicer [options]</p>
<p>Options</p>
<p>–launcher-help Display help</p>
<p>–launcher-version Show launcher version information</p>
<p>–launcher-verbose Verbose mode</p>
<p>–launch Specify the application to launch</p>
<p>–launcher-detach Launcher will NOT wait for the application to finish</p>
<p>–launcher-no-splash Hide launcher splash</p>
<p>–launcher-timeout Specify the time in second before the launcher kills the application. -1 means no timeout (default: -1)</p>
<p>–launcher-load-environment Specify the saved environment to load.</p>
<p>–launcher-dump-environment Launcher will print environment variables to be set, then exit</p>
<p>–launcher-show-set-environment-commands Launcher will print commands suitable for setting the parent environment (i.e. using ‘eval’ in a POSIX shell), then exit</p>
<p>–launcher-additional-settings Additional settings file to consider</p>
<p>–launcher-additional-settings-exclude-groups Comma separated list of settings groups that should NOT be overwritten by values in User and Additional settings. For example: General,Application,ExtraApplicationToLaunch</p>
<p>–launcher-ignore-user-additional-settings Ignore additional user settings</p>
<p>–launcher-generate-exec-wrapper-script Generate executable wrapper script allowing to set the environment</p>
<p>–launcher-generate-template Generate an example of setting file</p>
<p>Traceback (most recent call last):</p>
<p>File “”, line 1, in </p>
<p>File “C:\Slicer\Slicer 4.11.20210226\bin\Python\slicer\util.py”, line 2876, in pip_install</p>
<p>_executePythonModule(‘pip’, args)</p>
<p>File “C:\Slicer\Slicer 4.11.20210226\bin\Python\slicer\util.py”, line 2851, in _executePythonModule</p>
<p>logProcessOutput(proc)</p>
<p>File “C:\Slicer\Slicer 4.11.20210226\bin\Python\slicer\util.py”, line 2820, in logProcessOutput</p>
<p>raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)</p>
<p>subprocess.CalledProcessError: Command ‘[‘C:/Slicer/Slicer 4.11.20210226/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, ‘open3d==0.10’]’ returned non-zero exit status 1.</p>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>

---

## Post #2 by @lassoan (2021-03-04 20:11 UTC)

<p>This is a known issue:</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/issues/5383" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/5383" target="_blank" rel="noopener">SimpleITK is not available on Windows if Slicer is installed in a path that contains special characters</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-01-10" data-time="17:02:39" data-timezone="UTC">05:02PM - 10 Jan 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">SimpleITK is not available if Slicer is installed in a path that contains special (non-ASCII) characters.
The reason is that CPython 3.6...</p>
</div>

<div class="labels">
    <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">type:bug</span>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>The workaround is to install Slicer in a folder that only contains ASCII characters.</p>

---

## Post #3 by @muratmaga (2021-03-04 20:54 UTC)

<p>But it is: The second installation folder was C:\Slicer\Slicer 4.11.20210226</p>
<p>and that’s where the nighlighted error is coming from:</p>

---

## Post #4 by @jamesobutler (2021-03-04 22:20 UTC)

<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerMorph/SlicerMorph/blob/f1c77cbcdef718c7503833f9aee9263e5a916eef/ALPACA/ALPACA.py#L55-L57" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/SlicerMorph/blob/f1c77cbcdef718c7503833f9aee9263e5a916eef/ALPACA/ALPACA.py#L55-L57" target="_blank" rel="noopener nofollow ugc">SlicerMorph/SlicerMorph/blob/f1c77cbcdef718c7503833f9aee9263e5a916eef/ALPACA/ALPACA.py#L55-L57</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="55" style="counter-reset: li-counter 54 ;">
<li>if slicer.util.confirmOkCancelDisplay("ALPACA requires the open3d library. Installation may take a few minutes"):</li>
<li>  slicer.util.pip_install('notebook==6.0.3')</li>
<li>  slicer.util.pip_install('open3d==0.10.0')</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>In SlicerMorph there was specific installing of certain Open3D dependency packages first to avoid the install of Open3D getting a later version of <code>notebook</code>. This was done because on some platforms like macOS the dependency couldn’t build the package from source.<br>
re: <a href="https://discourse.slicer.org/t/open3d-pip-install-error-on-mac/12867/4" class="inline-onebox">Open3d pip_install error on Mac - #4 by jamesobutler</a></p>
<p>I remember Open3D having a laundry list of dependencies. Maybe something has changed in the similar manner where it is having to build a wheel that struggles with greek locale, or a dependent package was updated and resulted in changes.</p>

---

## Post #5 by @muratmaga (2021-03-04 22:33 UTC)

<p>Seems bizarre and non-repo. Now the user reports after deleting the contents of the folder and rerunning all the installation steps, everything is working fine. Thanks for the input.</p>

---

## Post #6 by @jamesobutler (2021-03-04 22:35 UTC)

<p>There have been other situations of users who have built wheels successfully using a system python after it was not successful using Slicer’s python. Then when they try to install again from within Slicer it will pull that cached wheel and then it installs successfully in Slicer.</p>

---

## Post #7 by @user_ghost (2021-06-08 06:03 UTC)

<p>when i used  /PythonSlice to  install open3d in linux.   i can not import open3d from the CIL in slicer .</p>

---

## Post #8 by @muratmaga (2021-06-08 13:09 UTC)

<p>what happens when you type:</p>
<pre><code class="lang-auto">pip_install('open3d')
import open3d 
</code></pre>
<p>in the python console?</p>

---

## Post #9 by @lassoan (2021-06-08 14:50 UTC)

<p>For a mid/long-term solution: Open3D’s scope is so fuzzy (essentially “everything that our lab does”) and developers are so reckless in bringing in dependencies that it will be practically impossible to keep it working on all platforms all the time. I would recommend to request the developers to split up the package and/or reduce their dependencies and if they are not willing to do this then look for alternatives.</p>

---

## Post #10 by @jamesobutler (2021-06-08 15:09 UTC)

<p>Open3D==0.13.0 has a reasonable requirements.txt, but it is their requirements_jupyter.txt that brings in all those extra requirements that lead to issues.</p>
<p><a href="https://github.com/intel-isl/Open3D/blob/v0.13.0/python/requirements.txt" rel="noopener nofollow ugc">requirements.txt</a></p>
<pre><code class="lang-auto">setuptools&gt;=40.8.0
wheel&gt;=0.36.0
numpy&gt;=1.18.0
</code></pre>
<p><a href="https://github.com/intel-isl/Open3D/blob/v0.13.0/python/requirements_jupyter.txt" rel="noopener nofollow ugc">requirements_jupyter.txt</a></p>
<pre><code class="lang-auto">ipywidgets&gt;=7.6.0
pygments&gt;=2.7.4
jupyter_packaging~=0.10
jupyterlab&gt;=3.0.0,==3.*
</code></pre>

---

## Post #11 by @lassoan (2021-06-08 18:44 UTC)

<p>Look at these vendored third-party dependencies: <a href="https://github.com/intel-isl/Open3D/tree/master/3rdparty" class="inline-onebox">Open3D/3rdparty at master · intel-isl/Open3D · GitHub</a>. It is a lot and all messy (lots of hardware-dependent libraries; some libraries are brought in using submodules, some as superbuild, some are just copy-pasted; some are really big). OpenCV is quite bad in this regard, too (probably Open3D developers got their “best practices” from there) but at least you can see that OpenCV developers only vendorize a small set of carefully chosen third-party libraries and other third-party libraries are in a separate repository, organized into optional modules.</p>
<p>Open3D is increasingly looking like an application and not a library and such it is not well suited to be used as part of another application. It has some useful content, but to make it usable as a library, it would need to split up, cleaned up, and put together in a more disciplined way.</p>

---
