# Crop volume to a single slice

**Topic ID**: 4483
**Date**: 2018-10-22
**URL**: https://discourse.slicer.org/t/crop-volume-to-a-single-slice/4483

---

## Post #1 by @melsha3rawy (2018-10-22 03:41 UTC)

<p>Operating system: win10 64bit<br>
Slicer version:4.10<br>
Expected behavior: NA<br>
Actual behavior: can I crop one slice (dicom) to get a specific feature.</p>

---

## Post #2 by @lassoan (2018-10-22 03:43 UTC)

<aside class="quote no-group" data-username="melsha3rawy" data-post="1" data-topic="4483">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/ecccb3/48.png" class="avatar"> melsha3rawy:</div>
<blockquote>
<p>can I crop one slice (dicom) to get a specific feature</p>
</blockquote>
</aside>
<p>I don’t know how this relates to the topic title (template matching), but you can crop a volume using Crop volume module.</p>

---

## Post #3 by @melsha3rawy (2018-10-22 17:29 UTC)

<p>i would like to crop only one slice then I will use it as a template later in matching the same feature in other slices, sorry for confusing title</p>

---

## Post #4 by @lassoan (2018-10-22 22:53 UTC)

<p>You’ll get inaccurate 3D alignment if you only use a single 2D slice for alignment of images.</p>
<p>You can fully automatically align two images of different patients (either rigidly or using warping transform) using SlicerElastix extension. <em>General registration (BRAINS)</em> module that is bundled with Slicer may be usable, too, but usually it requires more parameter tweaking.</p>
<p>If you prefer not to do intensity-based registration then you can align images based on anatomical landmarks using <em>Landmark registration</em> module or SlicerIGT extension’s <em>Fiducial registration wizard</em> module.</p>

---
