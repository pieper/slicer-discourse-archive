---
topic_id: 29834
title: "How To Select Python Interpreter In Slicer On Vscode"
date: 2023-06-05
url: https://discourse.slicer.org/t/29834
---

# How to select python interpreter in Slicer on VSCode?

**Topic ID**: 29834
**Date**: 2023-06-05
**URL**: https://discourse.slicer.org/t/how-to-select-python-interpreter-in-slicer-on-vscode/29834

---

## Post #1 by @wrc (2023-06-05 08:24 UTC)

<p>Hello, I failed to select python interpreter in Slicer on VSCode. The system is MacOS 13.4. I also tried other IDE but no success. However, I can run python script by python interpreter in Slicer from Terminal.</p>
<p>Here is the error information:</p>
<pre><code class="lang-auto">[error] [Error: Command failed: /Applications/Slicer.app/Contents/bin/PythonSlicer -I /Users/admin/.vscode/extensions/ms-python.python-2023.8.0/pythonFiles/get_output_via_markers.py /Users/admin/.vscode/extensions/ms-python.python-2023.8.0/pythonFiles/interpreterInfo.py
error: Application is NOT executable [/Applications/Slicer.app/Contents/bin/./python-real]
Usage
  PythonSlicer [options]

Options
  --launcher-help                                 Display help
  --launcher-version                              Show launcher version information
  --launcher-verbose                              Verbose mode
  --launch                                        Specify the application to launch
  --launcher-detach                               Launcher will NOT wait for the application to finish
  --launcher-no-splash                            Hide launcher splash
  --launcher-timeout                              Specify the time in second before the launcher kills the application. -1 means no timeout (default: -1)
  --launcher-load-environment                     Specify the saved environment to load.
  --launcher-dump-environment                     Launcher will print environment variables to be set, then exit
  --launcher-show-set-environment-commands        Launcher will print commands suitable for setting the parent environment (i.e. using 'eval' in a POSIX shell), then exit
  --launcher-additional-settings                  Additional settings file to consider
  --launcher-additional-settings-exclude-groups   Comma separated list of settings groups that should NOT be overwritten by values in User and Additional settings. For example: General,Application,ExtraApplicationToLaunch
  --launcher-ignore-user-additional-settings      Ignore additional user settings
  --launcher-generate-exec-wrapper-script         Generate executable wrapper script allowing to set the environment
  --launcher-generate-template                    Generate an example of setting file

at ChildProcess.exithandler (node:child_process:409:12)
at ChildProcess.emit (node:events:513:28)
at maybeClose (node:internal/child_process:1112:16)
at ChildProcess._handle.onexit (node:internal/child_process:304:5)] {
  code: 1,
  killed: false,
  signal: null,
  cmd: '/Applications/Slicer.app/Contents/bin/PythonSlicer -I /Users/admin/.vscode/extensions/ms-python.python-2023.8.0/pythonFiles/get_output_via_markers.py /Users/admin/.vscode/extensions/ms-python.python-2023.8.0/pythonFiles/interpreterInfo.py'
}
</code></pre>

---

## Post #2 by @lassoan (2023-06-16 16:38 UTC)

<p>VSCode’s interpreter check failure is fixed in recent Slicer Preview Releases. Let us know how it works.</p>

---

## Post #3 by @wrc (2023-08-22 07:24 UTC)

<p>Unfortunately, it is not fixed in Slicer 5.4.0</p>

---

## Post #4 by @jcfr (2023-08-22 16:19 UTC)

<p>For reference, this was tentatively fixed in this commit:</p>
<ul>
<li><a href="https://github.com/Slicer/Slicer/commit/0cf480de8721d685b5b97746032136e54501fc50" class="inline-onebox">BUG: Fix launching .py files using Slicer with -I argument · Slicer/Slicer@0cf480d · GitHub</a></li>
</ul>

---

## Post #5 by @jcfr (2023-08-22 16:20 UTC)

<p><a class="mention" href="/u/wrc">@wrc</a> To help us understand, was the fixed we integrated working and did it recently started to fail again?</p>

---

## Post #6 by @wrc (2023-08-23 02:14 UTC)

<p>In windows PC, it was fine. But in MacOS, it showed the same error in Slicer 5.4.0.</p>

---

## Post #7 by @jcfr (2023-08-23 02:24 UTC)

<p>Thanks for the follow up.</p>
<p>If I understand your comment, the fix originally integrated fixed the issue on Windows but never fixed it on macOS ?</p>
<p>We are trying to understand if this is a recent regression or not. So any additional details would be helpful.</p>
<p>After the fix integrated by <a class="mention" href="/u/lassoan">@lassoan</a>  and linked above, did it ever work on macOS using the Preview build ?</p>
<p>Could you include screenshot and step by step to illustrate how you configure the interpreter in VS Code ?</p>

---

## Post #8 by @wrc (2023-08-23 06:35 UTC)

<p>Sorry, I don’t know whether this problem has been solved before. I haven’t found the link to download the previous preview build (2023.5.18) so that I cannot test it. Here is the screenshot:<br>
click 3.9.6 64-bit<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c333781f7793ffe10c04f6974619faaecc2ef85e.png" data-download-href="/uploads/short-url/rQPnv5jZSEXUb8vmdcqEpF9GMKq.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c333781f7793ffe10c04f6974619faaecc2ef85e_2_690x91.png" alt="1" data-base62-sha1="rQPnv5jZSEXUb8vmdcqEpF9GMKq" width="690" height="91" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c333781f7793ffe10c04f6974619faaecc2ef85e_2_690x91.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c333781f7793ffe10c04f6974619faaecc2ef85e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c333781f7793ffe10c04f6974619faaecc2ef85e.png 2x" data-dominant-color="242424"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">970×128 9.17 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
click enter interpreter path…<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6abb1bf0cd5f3839526639ceff1d7745ac3b1b64.png" data-download-href="/uploads/short-url/febusMkMbJdfwd370sP6Ohk5iYs.png?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6abb1bf0cd5f3839526639ceff1d7745ac3b1b64.png" alt="2" data-base62-sha1="febusMkMbJdfwd370sP6Ohk5iYs" width="689" height="125" data-dominant-color="2E2F31"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1194×218 15.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
input the path of PythonSlicer<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/578c6ad38337f6698760363bce61189d4ca7ca4a.png" data-download-href="/uploads/short-url/cuunIEMnABO1DjId4JYkEjfERK2.png?dl=1" title="3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/578c6ad38337f6698760363bce61189d4ca7ca4a.png" alt="3" data-base62-sha1="cuunIEMnABO1DjId4JYkEjfERK2" width="689" height="73" data-dominant-color="303336"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3</span><span class="informations">1194×128 5.17 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @lassoan (2023-08-23 06:55 UTC)

<p>VS Code added a whole lot more operations to the interpreter check, which would require some more work to succeed. The “fix” in Slicer-5.4 should prevent Slicer instances to get started and get stuck with a popup, but not sufficient for VS Code current interpreter checks to complete successfully.</p>
<p>Getting a successful interpreter check would make a big difference when all the pyi files from VTK, ITK, Slicer, etc. are properly installed because we could then have auto-complete, documentation, etc. in the code editor. So, we should fix the interpreter check it when we have the pyi files in the Slicer installation package.</p>

---

## Post #10 by @jcfr (2023-08-23 12:45 UTC)

<blockquote>
<p>when all the pyi files from VTK, ITK, Slicer, etc. are properly installed</p>
</blockquote>
<p>For reference, this is tracked in the following issue:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/6690">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/6690" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/6690" target="_blank" rel="noopener">Improve auto-completion support</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-11-21" data-time="23:43:33" data-timezone="UTC">11:43PM - 21 Nov 22 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener">
          <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Type: Enhancement
        </span>
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Domain: Autocomplete
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">* [ ] https://github.com/Slicer/Slicer/issues/6686
* [ ] https://github.com/Sli<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">cer/Slicer/pull/6892
  * [ ] https://github.com/Slicer/Slicer/issues/6688
  * [ ] https://github.com/Slicer/Slicer/issues/6689
* [ ] https://github.com/Slicer/Slicer/issues/6875
* [ ] Add support for auto-completion of Qt-based classes</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
