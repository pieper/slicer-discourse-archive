---
topic_id: 26087
title: "Slicer Kernel For Jupyter Notebook And Python Debugger Setup"
date: 2022-11-05
url: https://discourse.slicer.org/t/26087
---

# Slicer kernel for jupyter notebook and python debugger setup in vscode

**Topic ID**: 26087
**Date**: 2022-11-05
**URL**: https://discourse.slicer.org/t/slicer-kernel-for-jupyter-notebook-and-python-debugger-setup-in-vscode/26087

---

## Post #1 by @wRossw (2022-11-05 21:11 UTC)

<p>Hi,</p>
<p>I have a few questions for getting a working setup of the jupyter notebook extension and Slicer working within VSCode. I’m still fairly new to making the switch from MATLAB to python, so some of these may be fairly obvious questions I am missing.</p>
<p>My main questions are:</p>
<ol>
<li>How to make sure I am pointing to the correct kernel to run a .ipynb file within vscode</li>
<li>How to enable a debugger for jupyter lab in either vscode or within jupyter lab when running a slicer kernel</li>
</ol>
<p><strong>For the first question:</strong><br>
Currently on my Mac I recently installed Slicer 5.0.3 which I think overwrote Slicer 4.11. When running a jupyter notebook in jupyter lab with a slicer 5.0 kernel, the notebook works as expected. However, my Mac (and our lab’s PC I’ve set this up on) seems to think there are two available slicer kernels<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61be39a87a5e361457c36368dc9553dfae72579c.png" alt="image" data-base62-sha1="dWFRXrwVrF2vF86mg7zYYZJSbko" width="267" height="252"></p>
<p>When trying to run a jupyternotebook in vscode, it seems to only recognize the 4.11 kernel, and when I check the directory it is pointing the executable file it points to I believe should now be 5.0</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/9492cba01d70f5f907d74294c52ca703d1fa99b1.png" data-download-href="/uploads/short-url/lclaKlcwpSW9ElZHtQDodjhPj0d.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/9492cba01d70f5f907d74294c52ca703d1fa99b1_2_690x240.png" alt="image" data-base62-sha1="lclaKlcwpSW9ElZHtQDodjhPj0d" width="690" height="240" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/9492cba01d70f5f907d74294c52ca703d1fa99b1_2_690x240.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/9492cba01d70f5f907d74294c52ca703d1fa99b1_2_1035x360.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/9492cba01d70f5f907d74294c52ca703d1fa99b1_2_1380x480.png 2x" data-dominant-color="282828"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1867×651 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><strong>For the second question:</strong><br>
From what I read, it seems that a debugger for a .ipynb (<a href="https://github.com/SlicerRt/SlicerDebuggingTools" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerRt/SlicerDebuggingTools: Extension for 3D Slicer containing various tools for module development and debugging</a> ) is different than the python debugger (<a href="https://github.com/SlicerRt/SlicerDebuggingTools" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerRt/SlicerDebuggingTools: Extension for 3D Slicer containing various tools for module development and debugging</a> )? Is this true and is it possible to setup debugging with a slicer kernel?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/9275d2a56d63df788913451935a841cdf2c582e0.png" alt="image" data-base62-sha1="kTE8ZbpqSen3kd8QX6LUYIXKITu" width="264" height="80"></p>
<p><strong>A minor question</strong>: when I launch vscode with the 4.11 kernel, it wants to launch 4 instances of slicer that shutdown quickly, and reduce to one running instance, but I’m wondering if there’s a way to get stop this behavior<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d38d0f6948e02b6a98f0c8470088ac744abb73d7.png" alt="image" data-base62-sha1="ubsXUEgfEZfTWuU8vKaP7KzT6w7" width="111" height="241"></p>
<p>I really appreciate the help! Please, let me know how to proceed or if there are posts I might have missed that address this.</p>
<p>Best</p>

---

## Post #2 by @pll_llq (2022-11-06 09:44 UTC)

<p>Last time I tried VSCode had poor support for xeus kernels (slicer’s kernel is one of those). The workaround would be to use the VSCode remote jupyter kernel extension and launch the slicer-jupyter docker container. Then you should be able to connect to the kernel in the container from vscode</p>

---

## Post #3 by @wRossw (2022-11-07 16:39 UTC)

<p>Hi Theadore,</p>
<p>Thank you this is very helpful to know! I will likely just stick with jupyterlab then instead of VS code since it seems to be a good working setup. At least until there is better support for xeus.</p>
<p>Do you have any suggestions for getting a debugger working in jupyter lab with a xeus kernel?</p>

---

## Post #4 by @lassoan (2022-11-07 18:17 UTC)

<p>There is an issue with the debugger causing a deadlock when attached - see <a href="https://github.com/Slicer/SlicerJupyter/issues/69" class="inline-onebox">Add JupyterLab debugger support · Issue #69 · Slicer/SlicerJupyter · GitHub</a>. It is a complex issue and <a href="https://slicer.readthedocs.io/en/latest/developer_guide/debugging/python.html">there are alternative debuggers that you can use</a>, so I’m not sure when it is going to be resolved.</p>

---

## Post #5 by @wRossw (2022-11-07 18:34 UTC)

<p>Great! Thanks for the help both!</p>

---

## Post #6 by @wRossw (2022-11-10 22:57 UTC)

<p>I have quick question. I tried following the steps outlined in <a href="https://github.com/SlicerRt/SlicerDebuggingTools" rel="noopener nofollow ugc">https://github.com/SlicerRt/SlicerDebuggingTools</a> but may be missing something.</p>
<p>Setting up the following json file for a remote attachment for the debugger.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e4a44444cf35190a10f21f547635e1be8339e86.png" data-download-href="/uploads/short-url/baAmdhSGU04bwN4WzvsiDQwe22O.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e4a44444cf35190a10f21f547635e1be8339e86.png" alt="image" data-base62-sha1="baAmdhSGU04bwN4WzvsiDQwe22O" width="690" height="305" data-dominant-color="FBFCFB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">934×413 14.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I get the following connection error:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/628ce470a3d23715204a33456b855638d5a5b180.png" alt="image" data-base62-sha1="e3OEsqV36XroM1S0fhMfzYVKSZ2" width="482" height="75"></p>
<p>I also tried following some of the advice on this thread (<a href="https://discourse.slicer.org/t/developing-slicer-modules-in-visual-studio-visual-studio-code/9496/20">https://discourse.slicer.org/t/developing-slicer-modules-in-visual-studio-visual-studio-code/9496/20</a>) for setting up the correct python paths and autocomplete paths for vscode, but haven’t quite been able get autocompletion to work or recognize “import slicer” for example. From my understanding of this thread, it seems that getting a debugging connection alone will allow autocompletion?</p>
<p>Any help would be much appreciated! thanks!</p>

---

## Post #7 by @lassoan (2022-11-12 04:18 UTC)

<p>To start debugging, you need to click “Connect” in Slicer before you can attach in VS Code. Follow exactly <a href="https://github.com/SlicerRt/SlicerDebuggingTools#start-debugging-1">these steps</a>.</p>
<p>What may be confusing is that the VS Code screenshot shows all 4 clicks that you need to make in VS Code. For initial setup you only need to click 1 and 2. Click 3 and 4 are for for starting debugging and they should be clicked after “Connect” button was clicked in Slicer.</p>

---
