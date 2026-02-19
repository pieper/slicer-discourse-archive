---
topic_id: 20162
title: "In Developing A Loadable Module How Can I Use The Screen On"
date: 2021-10-15
url: https://discourse.slicer.org/t/20162
---

# In developing a loadable module, how can I use the screen on the right except ui on the left side of the display module?

**Topic ID**: 20162
**Date**: 2021-10-15
**URL**: https://discourse.slicer.org/t/in-developing-a-loadable-module-how-can-i-use-the-screen-on-the-right-except-ui-on-the-left-side-of-the-display-module/20162

---

## Post #1 by @kookoo9999 (2021-10-15 00:29 UTC)

<p>Thank you so much for your help every time <a class="mention" href="/u/lassoan">@lassoan</a> .<br>
This weekend, I’m going to try the Simple ITK-related Error Fix that you mentioned last time.</p>
<p>In developing a loadable module, how can I use the screen on the right except ui on the left side of the display module?</p>
<p>When developing a loadable-module, is it correct to create a loadable-module source for the extension wizard through slicer-build\Slicer.exe in the development order, then build a source through CMake and modify and use binary files? Or do I have to build through CMake whenever I modify the source code?</p>
<p>I am developing a loadable module (simple AR module using real-time computer vision) using c+±based VS Qt tool in visual studio (on Windows10). Is there a function that provides support such as real-time computer vision, video processing, or real time streaming within 3D Slicer? If there is, I would like to use it first.<br>
And is there a way to debug each module when running Slicer in Debug mode through S4D\Slicer-build\Slicer.exe --VisualStudioProject?</p>
<p>Also, I want to use the display area on the right except for the UI part of the Slicer screen, but I don’t know their names and don’t know how to use them. Can you tell me how to use this part?</p>
<p>And can I use the data of module A when I run module B? For example, through Volume, Volume Rendering.I rent dcm files in the 3D, 2D display area, and how can I use (reuse) this displayed, rented image or video in the module I created?</p>
<p>If the goal is to use the resulting data from other modules, we would like to obtain the coordinates of a specific object in the video and then use these coordinates to use the displayed images and coordinates in Volume Rendering.</p>

---
