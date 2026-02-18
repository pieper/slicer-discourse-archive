# Wrong resolution after 'Segmentation geometry'

**Topic ID**: 25732
**Date**: 2022-10-17
**URL**: https://discourse.slicer.org/t/wrong-resolution-after-segmentation-geometry/25732

---

## Post #1 by @michielzeeuw (2022-10-17 14:58 UTC)

<p>Hi all,</p>
<p>We developed an automatic segmentation model for tumors in the liver. The output we get is in nifti file and still needs to corrected in Slicer 3D.<br>
I upload the scan (nifti.gz) and segmentation (nifti) in Slicer 3D: sometimes from a specific slice I can’t draw/erase anymore. This problem we solved by choosing ‘Segmentation geometry’ and choosing current scan (512x512).<br>
However, when I want to use those adjusted segmentations for volumetric assessment, I get an error, and this is because the resolution was changed in the process…</p>
<p>Can anyone help me out?</p>
<p>Regards,<br>
Michiel</p>

---

## Post #2 by @lassoan (2022-10-17 15:06 UTC)

<aside class="quote no-group" data-username="michielzeeuw" data-post="1" data-topic="25732">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/34f0e0/48.png" class="avatar"> michielzeeuw:</div>
<blockquote>
<p>I upload the scan (nifti.gz) and segmentation (nifti) in Slicer 3D</p>
</blockquote>
</aside>
<p>What is the geometry (origin, spacing, and axis directions) of the scan and segmentation file?</p>
<p>Nifti has a serious issue that it can store multiple geometries in a single file and these geometries may contradict each other. Did you use sform, qform, or both to specify geometry?</p>
<p>Is there a reason for choosing nifti format, which allows this redundant/inconsistent geometry definition? This problem is unique to the nifti file format, so you can choose any other research file format (for example: nrrd) to avoid such complications.</p>
<aside class="quote no-group" data-username="michielzeeuw" data-post="1" data-topic="25732">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/34f0e0/48.png" class="avatar"> michielzeeuw:</div>
<blockquote>
<p>However, when I want to use those adjusted segmentations for volumetric assessment, I get an error, and this is because the resolution was changed in the process…</p>
</blockquote>
</aside>
<p>Where do you get an error? What is the error message?</p>

---

## Post #3 by @michielzeeuw (2022-10-25 13:55 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="25732">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>geometries</p>
</blockquote>
</aside>
<p>The resolution of the nifti.gz CT scan is 512x512, and of the pre-segmentation in niftii is also 512x512. Ergo, it should be the same resolution.<br>
When I upload both to Slicer 3D, I cannot adjust or draw segmentations besides in a certain box. And when I export the adjusted segmentation, the resolution has changed.</p>
<p>I do not get an error, but the output of our volumetric model is wrong (counts too many lesions).</p>

---

## Post #4 by @lassoan (2022-10-25 18:51 UTC)

<p>You can store very images with very different geometry (origin, spacing, axis directions) in a 512x512 grid. It seems that geometry of the segmentation’s binary labelmap representation does not match the geometry of the input image that you are currently using. The segmentation’s geometry is automatically set based on the first image you select, but you can change it anytime.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#cannot-paint-outside-some-boundaries">“Cannot paint outside some boundaries” section</a> of the Segment Editor module documentation (or other sections in that FAQ) provides a bit more details and describes what you can do about it.</p>

---
