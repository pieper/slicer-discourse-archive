# How to get GPU texture id(or handle) or texture buffer?

**Topic ID**: 17760
**Date**: 2021-05-24
**URL**: https://discourse.slicer.org/t/how-to-get-gpu-texture-id-or-handle-or-texture-buffer/17760

---

## Post #1 by @liku (2021-05-24 12:27 UTC)

<p>I loaded sample data and displayed volume in 3D view.<br>
Now I need to get texture buffer of this volume to do some process.<br>
Is there a method to get GPU texture buffer or texture id?</p>

---

## Post #2 by @lassoan (2021-05-24 13:06 UTC)

<p>When you load a volume into the scene, it is stored into CPU memory only.</p>
<p>Individual reformatted slices are uploaded to GPU (when you display the volume in slice views).</p>
<p>The entire volume is uploaded to the GPU if you display it using GPU volume rendering. You can run custom GLSL shaders on it (see Slicer Prism extension), but I am not sure if you can get access to the buffer (check out VTK and the Volume Rendering module for details).</p>
<p>What is your overall goal?</p>

---

## Post #3 by @liku (2021-05-24 07:06 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11</p>
<p>I loaded the sample data and displayed the volume in 3D view by choosing “VTK GPU Ray Casting”.</p>
<p>Now I need to get texture id or texture buffer to do other process.<br>
Is there a way to get it?</p>

---

## Post #5 by @lassoan (2021-05-24 16:00 UTC)

<p>Let us know what you want to achieve and then we can give further guidance.</p>

---

## Post #6 by @liku (2021-05-25 06:05 UTC)

<p>Thanks for reply.</p>
<p>We have a c++ library that performs image processing on textures.<br>
So I need texture buffer (or id or handle) as input parameter.</p>

---

## Post #7 by @pieper (2021-05-25 11:29 UTC)

<p>This is a challenge because VTK manages the OpenGL state to support a wide range of visualization options so you’ll need to study that code carefully to integrate it.  I had some prototypes working with earlier versions of VTK but haven’t tried with vtk 9 that Slicer currently uses.  It would be helpful to have a formula for this kind of operation, so if you make progress please share back some documentation or example code.  Starting with SlicerPrism as Andras suggested may get you started.</p>

---

## Post #8 by @lassoan (2021-05-25 11:46 UTC)

<aside class="quote no-group" data-username="liku" data-post="6" data-topic="17760">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/c2a13f/48.png" class="avatar"> liku:</div>
<blockquote>
<p>We have a c++ library that performs image processing on textures.</p>
</blockquote>
</aside>
<p>I don’t think you can implement processing on the GPU in C++.</p>
<p>If it is really C++ then it runs on the CPU and you don’t need to transfer the image to the GPU.</p>
<p>If the library is actually in GLSL then PRISM or the GPU image processing filter in vtkAddon are good examples.</p>
<p>If the library uses OpenCL then you can find examples for how to create a processing filter from it in ITK.</p>
<p>If you have Cuda code then I would recommend to port it to GLSL or OpenCL for compatibility with non-NVidia hardware, but if I remember well there are some Cuda examples in the VASST extension.</p>

---

## Post #9 by @liku (2021-05-26 01:23 UTC)

<p>Thanks for suggestion. I’ll look into Slicer Prism extension.</p>

---

## Post #10 by @liku (2021-05-26 01:26 UTC)

<p>Yes, the library uses OpenCL.<br>
Thanks for suggestion.</p>

---
