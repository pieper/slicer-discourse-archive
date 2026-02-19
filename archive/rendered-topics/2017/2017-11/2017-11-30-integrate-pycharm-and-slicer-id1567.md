---
topic_id: 1567
title: "Integrate Pycharm And Slicer"
date: 2017-11-30
url: https://discourse.slicer.org/t/1567
---

# Integrate pycharm and Slicer

**Topic ID**: 1567
**Date**: 2017-11-30
**URL**: https://discourse.slicer.org/t/integrate-pycharm-and-slicer/1567

---

## Post #1 by @darekdev (2017-11-30 17:31 UTC)

<p>Operating system: Arch Linux<br>
Slicer version: newest<br>
Expected behavior: working debugging, want to use imports in pycharm and code completion<br>
Actual behavior: debugging doesn’t work, can’t import slicer or vtk or qt in pycharm (code completion)</p>
<p>Hello,</p>
<p>I work 2 years with Slicer and I made some modules but I can’t never integrate pycharm and Slicer-SuperBuild with 100%. What should I do? Because when I add vtk, qt, slicer paths to pycharm interpreter path that doesn’t work. Is it possible? And I can’t run debugging process. When I click connect in Slicer(debugging plugin) then nothing happen: Slicer doesn’t freeze.<br>
Can’t find any relevant tutorial in Internet. I appreciate any suggestion.</p>
<p>Thank you<br>
Darek</p>

---

## Post #2 by @ungi (2017-12-01 16:52 UTC)

<p>Hello Darek,</p>
<p>I use PyCharm to debug Slicer on a daily basis. I run it on Windows, but I think it should work the same way, because python should be the same.<br>
There are instructions on how to set up Slicer and PyCharm on the website of the DebuggingTools extension:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/DebuggingTools" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/DebuggingTools</a><br>
Some important steps to do before you can use the debugger:</p>
<ul>
<li>In PyCharm, set up and start a “Python Remote Debug” server on localhost with a port number e.g. 5678</li>
<li>In Slicer specify the egg file of PyCharm in the Python Debugger module, and set the same port number<br>
If the connection is successful, you will see a note in the PyCharm debugger console. And break points should work after that (no need to restart anything).</li>
</ul>
<p>Code completion usually doesn’t work in the PyCharm code editor main window. The reason is that some python modules are loaded in runtime, so there is no way for PyCharm to know at any time what python modules are available. But if you pause the program execution with a breakpoint, you can use the debugger console to type code, and code completion will work correctly. That is because PyCharm knows at that time what modules are currently loaded.</p>
<p>I hope this helps,<br>
Tamas</p>

---

## Post #3 by @Amy_Morton (2024-12-05 16:46 UTC)

<p><a class="mention" href="/u/ungi">@ungi</a><br>
‘If the connection is successful’</p>
<p>Are there troubleshooting resources when the connection is unsuccessful?</p><aside class="quote quote-modified" data-post="2" data-topic="40458">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/amy_morton/48/67318_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/troubleshooting-pycharm-debug-egg-file-path-configuration-in-3dslicer/40458/2">Troubleshooting PyCharm Debug Egg File Path Configuration in 3DSlicer</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    I’ve been experiencing similar issues getting my Slicer Python Debug connection to PyCharm up and running. 
Windows 10 Enterprise 19045.5131 
Slicer 5.6.2 
PyCharm 2024.3 (Pro) 
I had previously installed PyCharm 2024.2.4 and encountered the .egg issue. I also found the stackoverflow thread on extracting- but the path wath still pointed to _attach_proces… under the  .egg dir. I uninstalled .2.4 and installed 2024.3. 
In PyCharm I configured the remote debugger 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/51c464cbd27764a7f52a39b09947575f24ac90db.png" data-download-href="/uploads/short-url/bFlrHhpENNQMlud4KWp19A2ZkkX.png?dl=1" title="image" rel="noopener nofollow ugc">[image]</a> 
and I successfully built…
  </blockquote>
</aside>


---

## Post #4 by @ungi (2024-12-05 22:38 UTC)

<p>Hi Amy,<br>
I switched to VS Code a few years ago and I’m not using PyCharm anymore. There are some troubleshooting suggestions on this page, but I don’t remember running into such issues: <a href="https://github.com/SlicerRt/SlicerDebuggingTools" rel="noopener nofollow ugc">SlicerRt/SlicerDebuggingTools: Extension for 3D Slicer containing various tools for module development and debugging</a><br>
If you are considering switching to VS Code too, I can highly recommend it and happy to give you a demo too.<br>
Tamas</p>

---

## Post #5 by @Amy_Morton (2024-12-06 00:22 UTC)

<p>I was previously using vs code for other python projects- I would gladly take the demo offer!</p>
<p>Thank you!<br>
Let me know when a zoom call might be convenient for you?</p>

---

## Post #6 by @lassoan (2024-12-06 02:58 UTC)

<p>PyCharm developers often break their debugger (happens about once a year). The problem and workaround in their latest version is described here: <a href="https://github.com/SlicerRt/SlicerDebuggingTools/issues/19" class="inline-onebox">Problems with Pycharm 2024.3 - Does not connect · Issue #19 · SlicerRt/SlicerDebuggingTools · GitHub</a></p>
<p>I switched to VS Code a few years ago, too. PyCharm has a little extra convenience that the debugger can automatically reconnect when you restart Slicer (while if you use VS Code then you need to click to connect each time) and the PyCharm debugging console looks more like a regular Python console (while in VS Code the console has a separate single line for input, which takes some time to get used to). However, I switched to VS Code for debugging because I use VS Code for everything else anyway and remote debugging requires PyCharm professional version (you need to pay if you are not student or educator).</p>

---

## Post #7 by @Amy_Morton (2024-12-06 15:23 UTC)

<p>Thank-you both! I’ll switch to VSCode via <a href="https://github.com/SlicerRt/SlicerDebuggingTools/blob/master/README.md" rel="noopener nofollow ugc">the instructions</a> and follow back</p>

---

## Post #8 by @Amy_Morton (2024-12-06 17:31 UTC)

<p>Hurray! VSCode was such a more straightforward configuration!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/212e85a011d4d97c5577aae7f6f56476954b43d2.png" data-download-href="/uploads/short-url/4JxqCAzrrwbTlVH4Psk07GZV9K2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/212e85a011d4d97c5577aae7f6f56476954b43d2_2_690x367.png" alt="image" data-base62-sha1="4JxqCAzrrwbTlVH4Psk07GZV9K2" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/212e85a011d4d97c5577aae7f6f56476954b43d2_2_690x367.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/212e85a011d4d97c5577aae7f6f56476954b43d2_2_1035x550.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/212e85a011d4d97c5577aae7f6f56476954b43d2_2_1380x734.png 2x" data-dominant-color="242425"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1880×1000 156 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
