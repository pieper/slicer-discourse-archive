# Slicer code completion for python

**Topic ID**: 227
**Date**: 2017-04-28
**URL**: https://discourse.slicer.org/t/slicer-code-completion-for-python/227

---

## Post #1 by @brhoom (2017-04-28 22:44 UTC)

<p>Hi,<br>
How can I add Slicer libs to LiClipse so I can get some code complettion like the one I get in the debugger.<br>
Have a nice weekend!</p>

---

## Post #2 by @lassoan (2017-04-28 23:36 UTC)

<p>We’ve tried this a couple of times with partial success (search in the slicer mailing list archives in nabble for details; and in general about C++ or VTK code completion in Python).</p>
<p>The main issue is that for code completion the IDE must know your variable types. During debugging you know variable types exactly, so code completion is straightforward. However, while you are editing the code, it is impossible to know the variable type (the same variable can contain various types of data, depending on what inputs the method was called with). Most IDEs have some heuristics that try to guess variable types but it doesn’t work very well if you use lots of C++ wrapped classes.</p>

---

## Post #3 by @Saima (2018-07-30 08:06 UTC)

<p>Hi,<br>
I am trying to setup IDE for slicer debug in Liclipse. I followed the steps in video:</p><div class="youtube-onebox lazy-video-container" data-video-id="WR6dD1uHIN0" data-video-title="Let's Code - #1 - Setting up python debugging in Slicer" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=WR6dD1uHIN0" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/WR6dD1uHIN0/maxresdefault.jpg" title="Let's Code - #1 - Setting up python debugging in Slicer" width="" height="">
  </a>
</div>

<p>When I connect slicer to server using python debugger. it connects without halting and I dont have to resume it through liclipse.</p>
<p>I tried to debug template generated from python scripted modules. Its giving me these errors:</p>
<p>Traceback (most recent call last):<br>
File “D:\Slicer 4.9.0-2018-04-01\bin\Lib\site-packages\vtkmodules\vtkCommonKit.py”, line 5, in <br>
from .vtkCommonKitPython import *<br>
ImportError: DLL load failed: The specified module could not be found.</p>
<p>During handling of the above exception, another exception occurred:</p>
<p>Traceback (most recent call last):<br>
File “D:\Slicer coding\MyFirstExtension\FirstPythonModule\FirstPythonModule.py”, line 3, in <br>
import vtk<br>
File “D:\Slicer 4.9.0-2018-04-01\bin\Lib\site-packages\vtk.py”, line 32, in <br>
all_spec.loader.exec_module(all_m)<br>
File “D:\Slicer 4.9.0-2018-04-01\bin\Lib\site-packages\vtkmodules\all.py”, line 7, in <br>
from .vtkCommonKit import *<br>
File “D:\Slicer 4.9.0-2018-04-01\bin\Lib\site-packages\vtkmodules\vtkCommonKit.py”, line 9, in <br>
from vtkCommonKitPython import *<br>
ImportError: DLL load failed: The specified module could not be found.</p>
<p>How to fix this issue?<br>
Please reply</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e2a81d7a2452bd23af11501d93eef88afc7f7dc6.png" data-download-href="/uploads/short-url/wl65MRW3xD8rdygGs5kbmwaXALc.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e2a81d7a2452bd23af11501d93eef88afc7f7dc6_2_690x388.png" alt="image" data-base62-sha1="wl65MRW3xD8rdygGs5kbmwaXALc" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e2a81d7a2452bd23af11501d93eef88afc7f7dc6_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e2a81d7a2452bd23af11501d93eef88afc7f7dc6_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e2a81d7a2452bd23af11501d93eef88afc7f7dc6_2_1380x776.png 2x" data-dominant-color="DEE7EE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 716 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2018-07-30 10:05 UTC)

<p>Python remote debugging (when you connect the debugger to a running Slicer) works without any limitations - breakpoints, variablele inspector, interactive console, stack trace, auto-complete, API documentation, etc.</p>
<p>You cannot run a module by itself, without running Slicer. However, with latest nightly builds, you get some features - auto-complete, API documentation, etc. if you specify PythonSlicer.exe (included in Slicer install package) as Python interpreter in your IDE.</p>

---
