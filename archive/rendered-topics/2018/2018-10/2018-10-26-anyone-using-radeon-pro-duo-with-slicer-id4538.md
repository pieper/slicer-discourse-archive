# Anyone using Radeon Pro Duo with Slicer?

**Topic ID**: 4538
**Date**: 2018-10-26
**URL**: https://discourse.slicer.org/t/anyone-using-radeon-pro-duo-with-slicer/4538

---

## Post #1 by @muratmaga (2018-10-26 06:26 UTC)

<p>Hi,</p>
<p>I am interested in this card, primarily for the large amount VRAM (2x16GB) it offers. My previous experience with AMD cards was less than ideal, but that was almost 10 years ago.<br>
<a href="https://www.amd.com/en/products/professional-graphics/radeon-pro-duo-polaris" class="onebox" target="_blank" rel="nofollow noopener">https://www.amd.com/en/products/professional-graphics/radeon-pro-duo-polaris</a></p>
<p>Any input would be much appreciated.</p>

---

## Post #2 by @pieper (2018-10-26 13:19 UTC)

<p>I have no direct experience with that card, but I use the two-AMD FirePro D700 6144 MB configuration on a mac pro with no problems.  OpenGL support on all cards and chips is pretty good these days due to the extensive conformance test suites.</p>

---

## Post #3 by @chir.set (2018-10-27 18:39 UTC)

<p>My experience witn an AMD RX480 with 8GB RAM on Linux is very satisfactory. I doubt many people on this list are using such a bleeding edge video adapter.</p>
<p>Perhaps it’s for excessively huge volumes only. But then you may hit OpenGL limits such as :</p>
<blockquote>
<p>ERROR: OpenGL MAX_3D_TEXTURE_SIZE is 2048</p>
</blockquote>
<p>or</p>
<blockquote>
<p>Warning: In /home/arc/src/Slicer-SuperBuild/VTKv9/Rendering/VolumeOpenGL2/vtkOpenGLVolumeRGBTable.h, line 144<br>
vtkObject (0x560a8efde870): This OpenGL implementation does not support the required texture size of 32768, falling back to maximum allowed, 16384.This may cause an incorrect color table mapping.</p>
</blockquote>
<p>The first one prevents creation of any Volume Rendering view. The second one does not affect user experience.</p>
<p>It’s up to your data and requirements.</p>

---

## Post #4 by @chir.set (2018-10-28 08:05 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="3" data-topic="4538">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>bleeding edge video adapter</p>
</blockquote>
</aside>
<p>(This refers to the Radeon Pro Duo, of course.)</p>

---

## Post #5 by @muratmaga (2018-10-29 05:22 UTC)

<p><a class="mention" href="/u/chir.set">@chir.set</a> and <a class="mention" href="/u/pieper">@pieper</a>: thanks for the input. Yes, it is primarily to use it with high-resolution data from research microCT scanners, which tend to be 2000^3 or larger.</p>
<p>Think I will order one and test it.</p>

---
