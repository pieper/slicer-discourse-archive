# Python debugging in Visual Studio Code

**Topic ID**: 2928
**Date**: 2018-05-25
**URL**: https://discourse.slicer.org/t/python-debugging-in-visual-studio-code/2928

---

## Post #1 by @lassoan (2018-05-25 05:47 UTC)

<p><a href="https://code.visualstudio.com/">Visual Studio Code</a> is an awesome source code editor and IDE - free, multi-platform (Windows, Linux, and Mac), and highly extensible.</p>
<p>Support has been added in recent versions of Slicer to connect from Visual Studio Code to Slicer’s embedded Python interpreter and <a href="https://code.visualstudio.com/docs/editor/debugging">add breakpoints, inspect variables, run the code step-by-step, etc</a>. See more information and setup instructions <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/DebuggingTools#Debugging_in_VisualStudio_Code">here</a>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4eb97be5565aeabd194dc0a8bd1f0d727cc9026.png" data-download-href="/uploads/short-url/wF7Cl7lb8PvJ8BOu6Y0mZyfXovI.png?dl=1" title="Screenshot of a debugging session"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e4eb97be5565aeabd194dc0a8bd1f0d727cc9026_2_690x441.png" alt="Screenshot of a debugging session" data-base62-sha1="wF7Cl7lb8PvJ8BOu6Y0mZyfXovI" width="690" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e4eb97be5565aeabd194dc0a8bd1f0d727cc9026_2_690x441.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e4eb97be5565aeabd194dc0a8bd1f0d727cc9026_2_1035x661.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e4eb97be5565aeabd194dc0a8bd1f0d727cc9026_2_1380x882.png 2x" data-dominant-color="312F2E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot of a debugging session</span><span class="informations">3000×1920 642 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @gstarbuck (2019-01-11 20:38 UTC)

<p>Has anyone been able to get this work with Slicer 4.8.1 and the current VSCode? I am not able to. I follow the steps exactly and Slicer just keeps hanging, vscode starts and then stops the debugger and gives no output.</p>
<p>One thing that’s different is that I get a warning in vscode in the launch.json file, it says, “Property secret is not allowed”. Am I supposed to somehow specify a different Python interpreter or something?</p>
<p>There doesn’t seem to be any online help for slicer/vscode, and I don’t want to have to install Eclipse just for this. Thanks!</p>

---

## Post #3 by @lassoan (2019-01-11 22:42 UTC)

<p>Slicee-4.8 is more than a year old! Latest VS Code uses new version of Python debugger libraries that are incompatible with old versions.</p>
<p>You need to use at least Slicer-4.10 with recent VS Code releases.</p>

---

## Post #4 by @riep (2020-09-10 07:19 UTC)

<p>Hi everyone,</p>
<p>I am updating this thread. I am trying to use VSCode 1.48 (last version) and Slicer-4.11. I have followed<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/DebuggingTools#Debugging_in_VisualStudio_Code" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/DebuggingTools#Debugging_in_VisualStudio_Code</a>. Except some minor changes in VSCode I was able to follow through all the steps. However when I started the python debugging server on Slicer side, and started the debugging session in VSCode nothing seemed to happen.</p>
<p>I am trying to debug this code just for the test:</p>
<p>markupsNode = getNode(‘plan’)<br>
normal = [ 0, 0, 0 ]<br>
markupsNode.GetNormal(normal)</p>
<p>Do I miss something when debugging a python code that does not start at Slicer startup. Is it possible to do such thing ?</p>
<p>Thanks in advance for your help!<br>
Pierre</p>

---

## Post #5 by @lassoan (2020-09-10 12:23 UTC)

<p>You can do step-by-step debugging by attaching to Slicer’s Python environment from the debugger and putting a breakpoint into your code. If you want to step through your code then probably you need to create a skeleton module using Extension wizard and copy-paste the code there. It also allows you to relead and run the code (using Reload and Reload&amp;test buttons in the module GUI).</p>

---

## Post #6 by @riep (2020-09-10 12:42 UTC)

<p>Thanks, any experience with last version of VSCode and recent Slicer?<br>
I’ll try to investigate the issue, it may be a config issue (eventhough there is not much to configure ^^ ).<br>
I’ll let you know if I can resolve this.</p>

---

## Post #7 by @Yj_S (2020-09-21 07:52 UTC)

<p>I got a problem to attach. I use vscode 1.49 and slicer 4.11. I follow the instruction to attach but when I click “start debugging”, it seems success, because the slicer dialog disappear. But nothing happens in vscode, no variables showed in vscode. Could anybody give any suggestions? Is this the problem about vscode version?</p>

---

## Post #8 by @Yj_S (2020-09-21 08:38 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/9195156d76f37f9684f499f507fc1cd9f4fa3b01.png" data-download-href="/uploads/short-url/kLSDTTmBmMwYcvGn5JGxEwPfSsF.png?dl=1" title="图像 1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/9195156d76f37f9684f499f507fc1cd9f4fa3b01_2_690x381.png" alt="图像 1" data-base62-sha1="kLSDTTmBmMwYcvGn5JGxEwPfSsF" width="690" height="381" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/9195156d76f37f9684f499f507fc1cd9f4fa3b01_2_690x381.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/9195156d76f37f9684f499f507fc1cd9f4fa3b01_2_1035x571.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/9195156d76f37f9684f499f507fc1cd9f4fa3b01_2_1380x762.png 2x" data-dominant-color="252323"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">图像 1</span><span class="informations">1854×1024 49.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @Yj_S (2020-09-21 08:41 UTC)

<p>That’s very confusing. Even when I change the vscode version to 1.29 or 1.35, it’s still the same.  Really need some advice!  Thanks.</p>

---

## Post #10 by @lassoan (2020-09-21 18:15 UTC)

<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/DebuggingTools#Debugging_in_VisualStudio_Code">DebuggingTools extension documentation</a> describes how to <em>attach</em> a debugger to a running Slicer application instance. In this case, you don’t run a script but you put breakpoint(s) into the code and execution is paused when that line is reached. A that point you can open the console, step through the code, and run commands there.</p>
<p>If you want to run script in Slicer’s Python environment then I would recommend to use Jupyter notebooks, using <a href="https://github.com/Slicer/SlicerJupyter">SlicerJupyter extension</a>.</p>
<p>You may be able to execute some simplified scripts in Slicer’s Python environment, without starting the application, but this would be limited to using libraries, such as MRML, vtkITK, and vtkSegmentationCore, and some module logics. It might be interesting to see how Slicer can be used like this (essentially, as a set of Python libraries), but since attaching a debugger and using Jupyter notebooks seems to cover needs of most people, we don’t have plans to work on this in the near future.</p>

---
