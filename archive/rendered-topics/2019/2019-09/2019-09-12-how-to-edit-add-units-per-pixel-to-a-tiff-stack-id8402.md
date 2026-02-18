# how to Edit/add units per pixel to a Tiff stack?

**Topic ID**: 8402
**Date**: 2019-09-12
**URL**: https://discourse.slicer.org/t/how-to-edit-add-units-per-pixel-to-a-tiff-stack/8402

---

## Post #1 by @Louis_Kammerer (2019-09-12 12:58 UTC)

<p>Operating system:windows 10<br>
Slicer version:4.10.1<br>
Expected behavior:no units<br>
Actual behavior:unrealistic units</p>
<p>I am using a file composed of a stack of tiff images from uMRI that I merged using FIJI. When I open this file in slicer it works well. when I use the ruler I get a measurement that is not accurate. I know the size of each pixel, for instance 39x39x39 in microns. Is there a way to add this information?<br>
Thanks</p>

---

## Post #2 by @pieper (2019-09-12 13:50 UTC)

<p>I don’t think you can add it to the tiff, but if you save in nrrd or nifti format then the spacing can be preserved.</p>

---

## Post #3 by @lassoan (2019-09-12 14:00 UTC)

<aside class="quote no-group" data-username="Louis_Kammerer" data-post="1" data-topic="8402">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/louis_kammerer/48/4709_2.png" class="avatar"> Louis_Kammerer:</div>
<blockquote>
<p>I know the size of each pixel, for instance 39x39x39 in microns. Is there a way to add this information?</p>
</blockquote>
</aside>
<p>You can edit spacing information manually in Volumes module / Volume Information section. I agree with <a class="mention" href="/u/pieper">@pieper</a> that you should choose an image format that can store at least the most basic image geometry information (origin, spacing, axis directions).</p>

---

## Post #4 by @Louis_Kammerer (2019-09-12 14:47 UTC)

<p>Thanks that worked! I have been saving as NRRD just loading the original as a tiff. of course any segments I made no longer fit the original and won’t give me accurate measurements, is there any way to scale them?</p>

---

## Post #5 by @lassoan (2019-09-12 14:58 UTC)

<p>You can scale the image and segmentation by applying the same linear transform using Transforms module (scaling factors are the 3 first values in the diagonal of the 4x4 transformation matrix).</p>

---

## Post #6 by @pieper (2019-09-12 22:06 UTC)

<p>Or you can export them as labelmap volume nodes and edit the spacing in the volumes module like you did for the background.  Then you can re-import them as segmentation.  (Import export controls are at the bottom of the Segmentations module).</p>

---

## Post #7 by @Louis_Kammerer (2019-12-04 05:33 UTC)

<p>Do you know  a way to make the linear transform reduce by 3 decimal places? right now I can only get two in the boxes.</p>
<p>When I import the exported labelmap nodes I can’t select them as an active volume to change their image spacing.</p>

---

## Post #8 by @lassoan (2019-12-04 07:37 UTC)

<p>You can press <kbd>Ctrl</kbd>+<kbd>+</kbd> to increase the number of displayed digits.</p>

---
