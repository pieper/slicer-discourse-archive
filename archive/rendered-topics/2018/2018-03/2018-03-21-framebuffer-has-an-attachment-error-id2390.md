# Framebuffer has an attachment error

**Topic ID**: 2390
**Date**: 2018-03-21
**URL**: https://discourse.slicer.org/t/framebuffer-has-an-attachment-error/2390

---

## Post #1 by @muratmaga (2018-03-21 18:43 UTC)

<p>I have a volume that I had successfully rendered once. When I turn rendering on/off, I start receiving this exact error and get a solid white 3D rendering window.</p>
<p>This is on a i7 laptop with intel and nvidia GPU. I made the settings to use nvidia for the slicer-real.exe.</p>
<p>Warning: In D:\D\P\Slicer-481\Libs\MRML\Core\vtkObserverManager.cxx, line 131<br>
vtkObserverManager (000001A79CC91C10): The same object is already observed with the same priority. The observation is kept as is.</p>
<p>framebuffer has an attachment error<br>
framebuffer has an attachment error<br>
framebuffer has an attachment error<br>
framebuffer has an attachment error<br>
after try to load the texture ERROR (x501) Invalid value<br>
framebuffer has an attachment error<br>
framebuffer has an attachment error<br>
framebuffer has an attachment error<br>
framebuffer has an attachment error</p>

---

## Post #2 by @lassoan (2018-03-21 19:21 UTC)

<p>What is the volume size in voxels? How much GPU memory did you set in the volume rendering module?</p>

---

## Post #3 by @muratmaga (2018-03-21 20:00 UTC)

<p>This card has 4GB of memory, which is what I set in Slicer. Volume is 412x664x370 and has short data type.<br>
It happens after I tried to render a dataset that was too big. But this volume itself should fit the memory.</p>

---

## Post #4 by @lassoan (2018-03-21 21:20 UTC)

<p>Try to decrease the GPU memory allocation to 1-2GB.</p>

---
