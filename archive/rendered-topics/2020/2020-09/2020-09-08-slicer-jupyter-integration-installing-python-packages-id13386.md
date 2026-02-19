---
topic_id: 13386
title: "Slicer Jupyter Integration Installing Python Packages"
date: 2020-09-08
url: https://discourse.slicer.org/t/13386
---

# Slicer/Jupyter integration: installing python packages

**Topic ID**: 13386
**Date**: 2020-09-08
**URL**: https://discourse.slicer.org/t/slicer-jupyter-integration-installing-python-packages/13386

---

## Post #1 by @yoomi (2020-09-08 03:23 UTC)

<p>Hello,</p>
<p>I’m having trouble integrating 3D Slicer with Jupyter on my computer. I installed both Slicer and Jupyter, but am stuck on installing python packages. When I paste the below into the python interactor in Slicer as instructed here (<a href="https://github.com/Slicer/SlicerJupyter/blob/master/README.md" rel="nofollow noopener">https://github.com/Slicer/SlicerJupyter/blob/master/README.md</a>), I get the error that pip_install is invalid syntax.</p>
<p>Thanks so much for your help</p>
<pre><code class="lang-auto">import os
if os.name=='nt':
    # There are no official pyzmq wheels for Python-3.6 for Windows, so we have to install manually
    pip_install("https://files.pythonhosted.org/packages/94/e1/13059383d21444caa16306b48c8bf7a62331ca361d553d2119696ea67119/pyzmq-19.0.0-cp36-cp36m-win_amd64.whl")
else:
    # PIL may be corrupted on linux, reinstall from pillow
    pip_install('--upgrade pillow --force-reinstall')
pip_install("ipywidgets pandas ipyevents ipycanvas")
</code></pre>

---

## Post #2 by @lassoan (2020-09-08 03:24 UTC)

<p>What operating system do you use?<br>
What error message do you get?</p>

---

## Post #3 by @yoomi (2020-09-08 13:27 UTC)

<p>I’m on a Mac OS, and the specific error message is</p>
<p>File “”, line 7<br>
pip_install(“ipywidgets pandas ipyevents ipycanvas”)<br>
^<br>
SyntaxError: invalid syntax</p>

---

## Post #4 by @lassoan (2020-09-08 13:32 UTC)

<p>Probably the console is confused by the indentations. Either copy-paste the last line separately, or just copy-paste the two lines relevant for macOS:</p>
<pre><code class="lang-auto">pip_install('--upgrade pillow --force-reinstall')
pip_install('ipywidgets pandas ipyevents ipycanvas')
</code></pre>

---

## Post #5 by @yoomi (2020-09-08 13:49 UTC)

<p>Hi Andras,</p>
<p>That gives me the error that<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
NameError: name ‘pip_install’ is not defined</p>
<p>Is there something I should do in addition to “import os” before executing these lines? I’m just following the instructions from the readme.</p>
<p>Thanks so much for your help.</p>

---

## Post #6 by @lassoan (2020-09-08 13:51 UTC)

<p>You need to copy-paste these lines in 3D Slicer’s Python console.</p>

---

## Post #7 by @yoomi (2020-09-08 13:52 UTC)

<p>Is that separate from the python interactor? I’m typing it into the Python interactor at the bottom of the screen</p>

---

## Post #8 by @lassoan (2020-09-08 13:57 UTC)

<p>Yes, the Python interactor at the bottom of the Slicer application window shows a console of Slicer’s Python environment. Are there any error messages in the console before you type the command? Can you post a screenshot of how everything looks after you typed the command?</p>
<p>Could you try with <code>slicer.util.pip_install</code> instead of just <code>pip_install</code>?</p>

---

## Post #9 by @yoomi (2020-09-08 14:00 UTC)

<p>Hi Andras,</p>
<p>There is no error message before I type the command. Do I need to import pip into this environment before I get started? I tried it with slicer.util.pip_install, and this is what I get</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac7eb58312d4aaa540538be2f26d2e3d55a0d43f.png" data-download-href="/uploads/short-url/oBXB3O4ns1eDWHCooNwOj4YCmNV.png?dl=1" title="errormessage" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac7eb58312d4aaa540538be2f26d2e3d55a0d43f_2_517x96.png" alt="errormessage" data-base62-sha1="oBXB3O4ns1eDWHCooNwOj4YCmNV" width="517" height="96" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac7eb58312d4aaa540538be2f26d2e3d55a0d43f_2_517x96.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac7eb58312d4aaa540538be2f26d2e3d55a0d43f_2_775x144.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac7eb58312d4aaa540538be2f26d2e3d55a0d43f_2_1034x192.png 2x" data-dominant-color="F8EAEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">errormessage</span><span class="informations">1062×200 24.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @lassoan (2020-09-08 14:03 UTC)

<p>Which Slicer version do you use?</p>

---

## Post #11 by @yoomi (2020-09-08 14:06 UTC)

<p>This is 3D slicer 4.10.2</p>

---

## Post #12 by @lassoan (2020-09-08 14:07 UTC)

<p>OK, that explains everything. You need to use a recent Slicer Preview Release.</p>

---

## Post #13 by @yoomi (2020-09-08 15:27 UTC)

<p>Hi Andras,</p>
<p>that worked – thanks! – but now when I try to pip_install(‘ipywidgets pandas ipyevents ipycanvas’) I get the error that “could not build wheels for argon-cffi which use PEP517 and cannot be installed directly”. Do you know what might be going on?</p>
<p>Thanks</p>

---

## Post #14 by @lassoan (2020-09-08 15:34 UTC)

<p>Can you copy here the actual error message?</p>
<p>Could you run pip_install for each package separately to see which one triggers the error?</p>

---

## Post #15 by @yoomi (2020-09-08 15:46 UTC)

<p>Pandas has no problem, but ipycanvas, ipywidgets, and ipyevents all give the same error message below, and when I try the command suggested in the warning in terminal, it aborts it</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/34982a2dbc1766d8dada7185ebb49a41df610590.png" data-download-href="/uploads/short-url/7vgQ4NIqCC9Or46aGoytXaqJeJW.png?dl=1" title="errormessage2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34982a2dbc1766d8dada7185ebb49a41df610590_2_690x108.png" alt="errormessage2" data-base62-sha1="7vgQ4NIqCC9Or46aGoytXaqJeJW" width="690" height="108" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34982a2dbc1766d8dada7185ebb49a41df610590_2_690x108.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34982a2dbc1766d8dada7185ebb49a41df610590_2_1035x162.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34982a2dbc1766d8dada7185ebb49a41df610590_2_1380x216.png 2x" data-dominant-color="262626"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">errormessage2</span><span class="informations">1404×221 26 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #16 by @lassoan (2020-09-08 16:33 UTC)

<p>Thank you for all these information.</p>
<p>I searched for this error on the web and it seems that Jupyter recently switched to argon2-cffi crypto library to increase its security. Unfortunately, this library does not have binary package (wheel) for Python-3.6.7 on MacOS, that’s why you get the error.</p>
<p>You have a few options:</p>
<p><strong>Option A:</strong> Let anaconda get/build the wheel for you. Install anaconda and type the following commands:</p>
<pre><code class="lang-bash">conda create -n slicerhelper python=3.6.7
conda activate slicerhelper
pip install argon2-cffi
</code></pre>
<p>After this, pip_install command in Slicer should succeed.</p>
<p><strong>Option B.</strong> Find a download site for Python-3.6.7 macOS wheel for argon2-cffi and specify that using pip_install.</p>
<p><strong>Option C.</strong> Use a Jupyter version that did not depend on argon2-cffi, by specifying an earlier version of ipywidgets or jupyter in pip_install</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> Do you have any comment on this? Could we upgrade Slicer to Python-3.7? Or, could we build an argon2-cffi Python-3.6.7 macOS wheel and make it available for download?</p>

---

## Post #17 by @yoomi (2020-09-08 16:42 UTC)

<p>Let me give this a try, thank you!</p>

---

## Post #18 by @jcfr (2020-09-08 16:51 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="16" data-topic="13386">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Do you have any comment on this? Could we upgrade Slicer to Python-3.7?</p>
</blockquote>
</aside>
<p>While we could work with the upstream <code>argon2-cffi</code> project to have wheels, I suggest instead to spend time updating the python version used in Slicer from 3.6 to 3.7 (or 3.8).</p>
<p>This has been discussed here:</p>
<ul>
<li><a href="https://github.com/Slicer/Slicer/issues/5014" class="inline-onebox">Update Python version from 3.6.7 to 3.9.10 · Issue #5014 · Slicer/Slicer · GitHub</a></li>
</ul>
<p>In the meantime, the community is helping to update from 3.6.7 to 3.6.12:</p>
<ul>
<li><a href="https://github.com/Slicer/Slicer/pull/5161" class="inline-onebox">ENH: Change python version to 3.6.12 by BishopWolf · Pull Request #5161 · Slicer/Slicer · GitHub</a></li>
<li><a href="https://github.com/python-cmake-buildsystem/python-cmake-buildsystem/pull/270" class="inline-onebox">ENH: Added support for python 3.6.8 to 3.6.12 by BishopWolf · Pull Request #270 · python-cmake-buildsystem/python-cmake-buildsystem · GitHub</a></li>
</ul>

---

## Post #19 by @yoomi (2020-09-08 17:33 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Option A worked, and I was able to get through the installation instructions on the readme, but now that Jupyter kernel and Slicer are connected, I tested this in Jupyter</p>
<pre><code class="lang-auto">import JupyterNotebooksLib as slicernb
slicernb.ViewDisplay()
</code></pre>
<p>and got this error message in my terminal, but nothing happens in my Jupyter notebook (no error message) or in Slicer</p>
<p>ERROR: during execute_request</p>
<p>make_tuple(): unable to convert arguments to Python object (compile in debug mode for details)</p>

---

## Post #20 by @lassoan (2020-09-08 18:28 UTC)

<p>I was able to reproduce the issue. Most probably it is because of a recent upgrade of XEUS-Python kernel. I’ll investigate it a bit more and revert to the last known working version if I cannot figure out how to fix it.</p>

---

## Post #21 by @yoomi (2020-09-08 20:01 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> thanks so much, will look forward!</p>

---

## Post #22 by @lassoan (2020-09-09 15:23 UTC)

<p>I’ve reverted to last working version yesterday, so SlicerJupyter should work on MacOS on Slicer Preview Release you download today.</p>
<p>In the meantime, I’ve submitted a <a href="https://github.com/jupyter-xeus/xeus-python/pull/320">fix to xeus-jupyter</a> if it gets integrated then we should be able to switch back to latest version again. I’m still investigating Windows build issue.</p>

---

## Post #23 by @yoomi (2020-09-10 14:42 UTC)

<p>Hi Andras,</p>
<p>SlicerJupyter seems to work now, except that hitting Tab doesn’t bring up the available methods by class. Do you know how I could fix this? Thanks</p>

---

## Post #24 by @klarlund (2020-09-14 11:56 UTC)

<p>Type your line of code directly in the Python console of 3D slicer (where tab-completion works, at least for me) then copy/paste into Jupyter. Curiously, “itk” (with “import itk”) seems to give usable tab-completion in my Slicer/Jupyter setup, but almost anything else fails.</p>

---

## Post #25 by @lassoan (2020-09-14 13:02 UTC)

<aside class="quote no-group" data-username="klarlund" data-post="24" data-topic="13386">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/klarlund/48/7962_2.png" class="avatar"> klarlund:</div>
<blockquote>
<p>Type your line of code directly in the Python console of 3D slicer (where tab-completion works, at least for me) then copy/paste into Jupyter</p>
</blockquote>
</aside>
<p>Tab-completion, documentation, etc. should all work well - see it on Binder: <a href="https://github.com/Slicer/SlicerJupyter#option-1-run-using-binder" class="inline-onebox">GitHub - Slicer/SlicerJupyter: Extension for 3D Slicer that allows the application to be used from Jupyter notebook</a></p>
<p>We recently updated our Python kernel base library (xeus-python), which has some trouble with Jedi integration and therefore features that rely on code inspection are currently broken. Hopefully we can fix them in the next few days.</p>
<p>Until then, you can use a Slicer version from a couple of weeks before. I’ve just tried this version and it works well: <a href="https://download.slicer.org/?date=2020-08-10" class="inline-onebox">Download 3D Slicer | 3D Slicer</a></p>

---

## Post #26 by @klarlund (2020-09-14 16:42 UTC)

<p>I was on 8-13 and tab completion didn’t work there; I’ll wait for the fix! The integration is otherwise hugely useful. Thanks.</p>

---

## Post #27 by @lassoan (2020-09-14 16:45 UTC)

<p>Could you try 2020-08-10? What operating system do you use? Does tab completion work in Binder?</p>

---

## Post #28 by @lassoan (2020-09-14 20:00 UTC)

<p>I’ve pushed a fix, please try it in tomorrow’s Slicer Preview Release (you need to uninstall and reinstall SlicerJupyter if no new Slicer core is released).</p>

---

## Post #29 by @lassoan (2020-09-15 12:15 UTC)

<p>The change was not fully successful yesterday. I’ve refined it today and hopefully it’ll be all good tomorrow. Until then, there is a workaround to make auto-complete work. Run this in Slicer’s Python environment (in a notebook cell or in Slicer’s Python console):</p>
<pre><code>pip_install('parso==0.7.1')</code></pre>

---

## Post #30 by @lassoan (2020-09-17 02:07 UTC)

<p>Latest Slicer Preview Release confirmed to work well (including auto-complete, method documentation, etc.).</p>

---
