# Save image of 3d view

**Topic ID**: 2666
**Date**: 2018-04-23
**URL**: https://discourse.slicer.org/t/save-image-of-3d-view/2666

---

## Post #1 by @anandmulay3 (2018-04-23 13:34 UTC)

<p>i have already have a script for creating and saving segments using slicer 4.9, i need a image of the 3D view of the model, so i can get a reference image of the 3D model created by script. anyone here who already did this , please share the code lines…</p>
<p>Thanks.</p>

---

## Post #2 by @lassoan (2018-04-23 13:40 UTC)

<p>There are several examples for this in the Slicer script repository: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Capture">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Capture</a>.</p>

---

## Post #3 by @anandmulay3 (2018-04-23 14:30 UTC)

<p>yeah its working , but now problem is model is not at the center of the view so output image came with no actual 3D model in it.</p>

---

## Post #4 by @lassoan (2018-04-23 15:42 UTC)

<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Center_the_3D_View_on_the_Scene" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Center_the_3D_View_on_the_Scene</a></p>

---

## Post #5 by @anandmulay3 (2018-04-24 10:10 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> ,<br>
but still i cant see my object model in the image just a blank 3d view scene.</p>
<p>also the thing is i want to use  --no-window mode for my script , any idea how it will take a snap of the 3D model then.</p>

---

## Post #6 by @lassoan (2018-04-24 12:59 UTC)

<p>If you use <code>--no-window</code> then there will be no GUI and you have to create a render window, renderer, actor, mapper, set up display properties, camera, and capture the render window. It is perfectly doable, there are <a href="https://lorensen.github.io/VTKExamples/site/">lots of examples</a> for these. You’ll probably see your custom render window appearing for a moment. Depending on your environment, you might be able to create an off-screen render window, which does not show up on your desktop at all.</p>
<p>However, it may be simpler to just keep the main window - you can disable the splash screen and hide the main window as soon as it is created, so you would only see a window appearing for a moment.</p>

---

## Post #7 by @anandmulay3 (2018-04-24 14:22 UTC)

<p>yeah, i can see in your examples to create render window setup needs lots of elements,<br>
how can we disable splash screen and main window? its sounds easy way…</p>

---

## Post #8 by @lassoan (2018-04-25 01:26 UTC)

<p>You can disable splash screen by adding <code>--no-splash</code> and <code>--launcher-no-splash</code>. See list of all options here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Launcher">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Launcher</a></p>

---

## Post #9 by @anandmulay3 (2018-05-14 10:46 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a> i have tried to setup all the things i.e. camera, mappper , actor , render window , renederer and set of display properties from one of your example( cameraModel1.py).</p>
<p>So now the thing is i tried to set threeDView window to the new render window it working fine in GUI mode , but as i said i want it in <code>--no-window</code> mode, so i tried to run it and error occurs when we try to get threeDView window; as expected, without that line i can render the window which pops for a sec. and then i capture that windows and it disappears.</p>
<p>now my query is - How can i set my segments as an Actor to that render-window?/ How can i show /render the segment in this renderwindow?</p>

---

## Post #10 by @lassoan (2018-05-14 13:33 UTC)

<aside class="quote no-group" data-username="anandmulay3" data-post="9" data-topic="2666">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ac8455/48.png" class="avatar"> anandmulay3:</div>
<blockquote>
<p>How can i set my segments as an Actor to that render-window?</p>
</blockquote>
</aside>
<p>You can get the segment as vtkPolyData using <a href="http://apidocs.slicer.org/master/classvtkMRMLSegmentationNode.html#a71ebfa4439ec3ebdf57994888f572623">GetClosedSurfaceRepresentation</a> method and follow basic <a href="https://lorensen.github.io/VTKExamples/site/">VTK examples</a> to set up rendering for that polydata.</p>

---
