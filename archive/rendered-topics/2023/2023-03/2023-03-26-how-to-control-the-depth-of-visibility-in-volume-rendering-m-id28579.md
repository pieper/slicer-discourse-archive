---
topic_id: 28579
title: "How To Control The Depth Of Visibility In Volume Rendering M"
date: 2023-03-26
url: https://discourse.slicer.org/t/28579
---

# How to control the depth of visibility in volume rendering mode?

**Topic ID**: 28579
**Date**: 2023-03-26
**URL**: https://discourse.slicer.org/t/how-to-control-the-depth-of-visibility-in-volume-rendering-mode/28579

---

## Post #1 by @neurosignal (2023-03-26 02:54 UTC)

<p>Dear team,<br>
I have two DICOM volumes, one for the head MRI and another with several binary spots or masks. Using the Volume rendering, when inspecting the overlay on a slice using the ROI’s control points, very deep spots are also visible. How to control the depth of visibility?<br>
Thanks in advance.</p>

---

## Post #2 by @lassoan (2023-03-26 03:11 UTC)

<p>In Slicer, these “binary spots or masks” are called “segmentation”. If they are stored appropriately in DICOM as “Segmentation object” then they are loaded as segmentation. If they are loaded as a fake CT or MRI volume then you can convert to label volume in Volumes module and then <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#import-an-existing-segmentation-from-volume-file">convert that label volume into a segmentation using Data module</a>.</p>
<p>I would recommend to visualize the head MRI by segmenting the brain surface or other relevant structures.</p>
<p>If you want to visualize the head MRI using volume rendering then you can go to Volume Rendering module and adjust the “scalar opacity mapping” in the “Advanced” section.</p>

---

## Post #3 by @neurosignal (2023-03-27 14:15 UTC)

<p>Awesome <a class="mention" href="/u/lassoan">@lassoan</a>.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74f637b466e5799295fabe8be84977b36920ff9c.png" data-download-href="/uploads/short-url/gGGU87MvHDBdUYTZXBZsW3aZ3E8.png?dl=1" title="join_src37" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74f637b466e5799295fabe8be84977b36920ff9c_2_690x479.png" alt="join_src37" data-base62-sha1="gGGU87MvHDBdUYTZXBZsW3aZ3E8" width="690" height="479" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74f637b466e5799295fabe8be84977b36920ff9c_2_690x479.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74f637b466e5799295fabe8be84977b36920ff9c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74f637b466e5799295fabe8be84977b36920ff9c.png 2x" data-dominant-color="9A8EA7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">join_src37</span><span class="informations">875×608 387 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>That worked.<br>
However, now the segments “outside the ROI” are also visible. I just wanted to see the segments on the slice, neither above nor below that slice. In contrast to the previous attempt with the “fake MRI volume,” I am unable to generate ROI for a segment.<br>
Could you suggest any workaround?<br>
Thanks.</p>

---

## Post #4 by @lassoan (2023-03-27 15:21 UTC)

<aside class="quote no-group" data-username="neurosignal" data-post="3" data-topic="28579">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/neurosignal/48/65389_2.png" class="avatar"> neurosignal:</div>
<blockquote>
<p>However, now the segments “outside the ROI” are also visible</p>
</blockquote>
</aside>
<p>Volume rendering ROI has no effect on how segments are displayed.</p>
<aside class="quote no-group" data-username="neurosignal" data-post="3" data-topic="28579">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/neurosignal/48/65389_2.png" class="avatar"> neurosignal:</div>
<blockquote>
<p>I just wanted to see the segments on the slice, neither above nor below that slice.</p>
</blockquote>
</aside>
<p>This is what slice views show you. You can show slice views in 3D, too, but it is rare that someone relies on that, because it is much harder to review slices in the 3D view (they occlude each other, hard to zoom in, etc.).</p>
<aside class="quote no-group" data-username="neurosignal" data-post="3" data-topic="28579">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/neurosignal/48/65389_2.png" class="avatar"> neurosignal:</div>
<blockquote>
<p>I am unable to generate ROI for a segment.</p>
</blockquote>
</aside>
<p>I don’t understand what you mean by ROI that could be “generated” for a segment. In Slicer, ROI refers to <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#glossary">a box-shaped region in 3D</a>,  but I don’t think you want a bounding box.</p>
<p>Just a few guesses: If you want to see the segment in a slice then you already have that in slice views. You can show a slice view in 3D views by clicking on the slice view’s eye icon in the view controller (above the slice view). If you want to fill the slice view then you can export the segmentation to a labelmap volume. If you want to crop the 3D model of the segment then you can export the segmentation to a model node and enable clipping in Models module.</p>

---

## Post #5 by @neurosignal (2023-03-28 03:19 UTC)

<p>Thank you very much, <a class="mention" href="/u/lassoan">@lassoan</a> .<br>
My needs are met now when the slices are shown in the 3D viewer and the whole screen stays in four-up mode.</p>

---
