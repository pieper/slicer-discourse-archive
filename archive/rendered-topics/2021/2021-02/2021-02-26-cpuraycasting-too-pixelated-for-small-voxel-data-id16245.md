---
topic_id: 16245
title: "Cpuraycasting Too Pixelated For Small Voxel Data"
date: 2021-02-26
url: https://discourse.slicer.org/t/16245
---

# CpuRaycasting too pixelated for small voxel data

**Topic ID**: 16245
**Date**: 2021-02-26
**URL**: https://discourse.slicer.org/t/cpuraycasting-too-pixelated-for-small-voxel-data/16245

---

## Post #1 by @muratmaga (2021-02-26 17:50 UTC)

<p>We will be running our SlicerMOrph workshop using cloud resources, which doesn’t have a GPU. I have been testing CPUraycasting. While large voxel spacing rendering quality is good. For small voxel data seems very noisy. This seems to replicate both in the stable and the preview. Is there a solution for this?<br>
CPU:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d5eb5bd3d21a230de4a0449d47b46f9b0ff9b1d.jpeg" alt="image" data-base62-sha1="djZjPnkXKX887bntTGHmnEdy6ap" width="415" height="291"></p>
<p>same with GPU<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a9870897b5cab9efb0fc8da14c49fe4494cd93d.jpeg" alt="image" data-base62-sha1="huwQO2lH3Bm6ELoCHv9LpIl4qTj" width="431" height="311"></p>
<p>same volume with CPU rendering spacing increased by 10X  (0.035 to 0.35mm)<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40cc1c76223150503bcad487c41789a2cca1cdd3.jpeg" alt="image" data-base62-sha1="9fdRAktmOv81keScqT6uZczG94n" width="450" height="291"></p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a></p>

---

## Post #2 by @pieper (2021-02-26 20:23 UTC)

<p>Unfortunately there probably are some ray casting heuristics that don’t work well across scales.</p>
<p>For many environments you can enable GPU even if there’s no hardware and the software fallback will still work - I take it this didn’t work for you on your virtual system?</p>
<p>For example GPU ray cast mode works in this docker even though it’s not hardware:<br>
<code>docker run --rm -p 8080:8080 stevepieper/slicer-morph:4.11.20200930</code> connecting to <code>localhost:8080</code></p>
<p>Not sure if there’s a short-term fix otherwise, but if you post the sample data we could determine if this is a Slicer thing or is reproducible in native VTK.</p>

---

## Post #3 by @muratmaga (2021-02-26 20:24 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="16245">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>For many environments you can enable GPU even if there’s no hardware and the software fallback will still work - I take it this didn’t work for you on your virtual system?</p>
</blockquote>
</aside>
<p>It works ok up to a limit. For large datasets, GPU software rendering is way too slow. Performance is much better on CPU, when you have enough cores.</p>

---

## Post #4 by @muratmaga (2021-02-26 20:26 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="16245">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Not sure if there’s a short-term fix otherwise, but if you post the sample data we could determine if this is a Slicer thing or is reproducible in native VTK.</p>
</blockquote>
</aside>
<p>It is the sample data we distribute with slicermorph: <a href="https://github.com/SlicerMorph/SampleData/blob/master/sample_Skyscan_mCT_reconstruction.zip" class="inline-onebox">SampleData/sample_Skyscan_mCT_reconstruction.zip at master · SlicerMorph/SampleData · GitHub</a> it is 0.035mm isotropic voxel.</p>

---

## Post #5 by @lassoan (2021-02-26 20:35 UTC)

<p>The CPU volume renderer in VTK does not take into account the user matrix (that we use to position, orient, and scale the volume). It would be hard to change this, because it is a complex mechanism and the CPU renderer is not developed anymore in VTK. However, we can work around this by passing just the scaling to the volume renderer, and use the user matrix only for positioning and scaling. I’ll send a pull request with this workaround.</p>
<p>There is a difference between the GPU and CPU volume renderer in that after scaling, the CPU-rendered volume becomes more transparent (as it should), while the GPU-rendered version does not. Probably the GPU volume renderer transfer function evaluation code does not take into account the user transform when evaluating the transfer functions, which may be justified if we consider user transform as a way to position/scale the rendered object (in that case, the same workaround should be applied to it as for the CPU renderer).</p>
<p>Note that the GPU volume renderer has already many more features than the CPU volume renderer (for example, custom shaders), and the gap will get even wider in the future.</p>

---

## Post #6 by @muratmaga (2021-02-26 20:37 UTC)

<p>Thanks Andras. I will try when you can fix the issue.</p>
<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="16245">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Note that the GPU volume renderer has already many more features than the CPU volume renderer (for example, custom shaders), and the gap will get even wider in the future.</p>
</blockquote>
</aside>
<p>Unfortunately, economically it is 3-4 times as expensive to have the same cloud server with the GPU (and the only thing GPU is used for rendering, which is a small but important part of the course). Yes, normally we always use the GPU rendering (hence never was aware of this issue until now).</p>

---

## Post #7 by @lassoan (2021-02-26 20:41 UTC)

<p>I’ve pushed the <a href="https://github.com/Slicer/Slicer/commit/717b7c4a99028583ebcb55e248701367baf5bce6">fix</a>. It will be in the Slicer Preview Release tomorrow. It would be great if you could test it (I wanted to give it some more testing and send a pull request, but accidentally pushed it directly to the master).</p>

---
