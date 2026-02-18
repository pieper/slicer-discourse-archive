# 3D Slicer Hardware requirements

**Topic ID**: 9937
**Date**: 2020-01-24
**URL**: https://discourse.slicer.org/t/3d-slicer-hardware-requirements/9937

---

## Post #1 by @manjula (2020-01-24 17:25 UTC)

<p>As i understand 3D Slicer is mainly built on VTK and ITK.  I understand answers to the following will depend on the type of data and size of data and what you are going to do with it but in general is it possible to tell,</p>
<p>How do you decide on the optimal physical RAM ?</p>
<p>How do you decide on the optimal GPU and VRAM ?</p>
<p>Is the volume rendering mainly calculated in the CPU and only the final stages is done on the GPU ?</p>
<p>What calculations are done by the CPU and what calculations are mainly done by the GPU ?</p>
<p>What basic functions mainly depend on CPU resources and what functions mainly depend on GPU resources ?</p>

---

## Post #2 by @muratmaga (2020-01-24 20:58 UTC)

<p>This somes pretty often, I wonder if need to make this a FAQ?</p>
<p>All calculations are done on CPU, except for 3D rendering, which can be done on GPU.</p>
<p>HW requirements depends entirely on your dataset. HW requirements of a  clinical 256x256x256 typical MR scan will easily be handled any recent laptop.</p>
<p>Optimal RAM is usually 6-10X of the largest dataset you are planning to work on.</p>
<p>GPU Texture memory (VRAM) should be larger than your largest dataset (eg., working with 2GB data, get  VRAM &gt; 4GB).</p>
<p>GPU openGL HW capabilities should also match the texture dimensions of your dataset (check from <a href="https://openGL.gpuinfo.org" rel="nofollow noopener">https://openGL.gpuinfo.org</a>)</p>
<p>If you set the volume rendering option is set to GPU RAycasting, all rendering is done on GPU. If it is set to CPU Raycasting, only CPU is used (whether you have dedicated GPU or not).</p>

---

## Post #3 by @lassoan (2020-01-24 23:23 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="9937">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>This somes pretty often, I wonder if need to make this a FAQ?</p>
</blockquote>
</aside>
<p>Recommended hardware page is here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/HardwareConfiguration" class="inline-onebox">Documentation/Nightly/SlicerApplication/HardwareConfiguration - Slicer Wiki</a></p>
<p>I’ve updated it using <a class="mention" href="/u/muratmaga">@muratmaga</a>’s comments above.</p>

---
