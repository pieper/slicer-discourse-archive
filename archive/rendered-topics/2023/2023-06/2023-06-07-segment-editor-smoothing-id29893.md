# Segment Editor smoothing

**Topic ID**: 29893
**Date**: 2023-06-07
**URL**: https://discourse.slicer.org/t/segment-editor-smoothing/29893

---

## Post #1 by @tsehrhardt (2023-06-07 12:18 UTC)

<p>Is the smoothing algorithm in the “Show 3D” button of the Segment Editor using Taubin smoothing? I have seen recommendations to turn off smoothing and export the model to apply Taubin smoothing in external software like Meshlab, but when I tried that, it basically looks the same as the Segment Editor smoothing.</p>

---

## Post #2 by @muratmaga (2023-06-07 16:54 UTC)

<aside class="quote no-group" data-username="tsehrhardt" data-post="1" data-topic="29893">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tsehrhardt/48/18470_2.png" class="avatar"> tsehrhardt:</div>
<blockquote>
<p>Is the smoothing algorithm in the “Show 3D” button of the Segment Editor using Taubin smoothing</p>
</blockquote>
</aside>
<p>I do not know, you can check the source code for it. My understanding is these are very generic and standard image processing operations that has been around very long and results shouldn’t differ much between platforms (speed may differ due to optimizations). So i don’t think it is better to do those in meshlab or elsewhere.</p>
<p>For me, there are two specific cases where I avoid smoothing in segment editor:</p>
<ol>
<li>
<p>For large datasets (many gigabyte voxels) it will slow you down during interactive segmentation (e.g., if you are using paint every change will try to be rendered in 3D, and then smoothened).</p>
</li>
<li>
<p>For really thin structures (1-2 voxel diameter), 3D surface rendering with default smoothing options may remove them or create discontinuities.</p>
</li>
</ol>
<p>If I am dealing either of the situations, I usually disable the smoothing, complete my segmentation and use the surface toolbox to generate the smoothened model. I am not sure whether there are other situations where disabling the smoothing makes sense.</p>

---

## Post #3 by @tsehrhardt (2023-06-08 11:49 UTC)

<p>Ok thanks. Yes it doesn’t seem logical to me to use external software for smoothing. With medical scans, I have found that resampling the volume or oversampling the segmentation improves the detail enough to balance what gets smoothed, as described in the docs.</p>

---
