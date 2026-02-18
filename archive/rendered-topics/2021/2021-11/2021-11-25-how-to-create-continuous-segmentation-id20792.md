# How to create continuous segmentation

**Topic ID**: 20792
**Date**: 2021-11-25
**URL**: https://discourse.slicer.org/t/how-to-create-continuous-segmentation/20792

---

## Post #1 by @Maya (2021-11-25 23:23 UTC)

<p>Hi everyone. I‘m working on a project where I‘d like to visualize the pleural surface that is in contact with the ablation zone after percutaneous lung ablation.</p>
<p>I segmented the ablation zone (green) as well as the pleural surface in contact with it (red) manually in the axial view using segment editor.</p>
<p>While the ablation zone is displayed as a continuous object, the pleura is not visualized continually.</p>
<p>Could someone please explain to me how I can make it so that the red lines are connected with each other (so that they form a surface)?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab0ea4f569428e4f13d41585b47d00f1ae533ef1.jpeg" data-download-href="/uploads/short-url/opf1pT9UOAjiQ8W7ftLM2sizOBH.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ab0ea4f569428e4f13d41585b47d00f1ae533ef1_2_666x500.jpeg" alt="image" data-base62-sha1="opf1pT9UOAjiQ8W7ftLM2sizOBH" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ab0ea4f569428e4f13d41585b47d00f1ae533ef1_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ab0ea4f569428e4f13d41585b47d00f1ae533ef1_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ab0ea4f569428e4f13d41585b47d00f1ae533ef1_2_1332x1000.jpeg 2x" data-dominant-color="97989B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1440 192 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I‘d appreciate any help with this!</p>
<p>Best,<br>
Maya</p>

---

## Post #2 by @lassoan (2021-11-26 03:59 UTC)

<p>Do you segment each slice manually; draw scribbles and use Grow from seeds; or segment a few slices and interpolate using Fill between slices?</p>

---

## Post #5 by @lassoan (2021-11-28 05:40 UTC)

<aside class="quote no-group quote-post-not-found" data-username="Maya" data-post="3" data-topic="20792">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/cab0a1/48.png" class="avatar"> Maya:</div>
<blockquote>
<p>When I use apply the features you recommend, I get the following result, which is not what I intended.</p>
</blockquote>
</aside>
<p>If there is no image brightness difference between adjacent structures then you need to provide a lot of scribbles for “Grow from seeds” to get a nice result. In this case, it may be better to use “Fill between slices”.</p>
<aside class="quote no-group quote-post-not-found" data-username="Maya" data-post="4" data-topic="20792">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/cab0a1/48.png" class="avatar"> Maya:</div>
<blockquote>
<p>is it possible to only apply „fill between slices“ to a certain segmentation and not all?</p>
</blockquote>
</aside>
<p>“Fill between slices” is only applied to the currently visible segments, so you can exclude any segments by hiding them. You may need to enable segments to overlapping (Modify other segments → Allow overlap or Overwrite visible) to prevent overwriting of hidden segments.</p>

---

## Post #7 by @lassoan (2021-11-30 03:10 UTC)

<p>According to the DICOM standard, slice thickness tag does not play any role in reconstruction of 3D geometry from 2D slices. Only the slice position, orientation, pixel spacing, and number of rows and columns tags can be considered - and this is what Slicer does.</p>
<p>Accuracy of distance, area, and volume computation in 3D Slicer has been successfully validated many times, but it is always the user’s responsibility validate the workflow for each study. Even the simplest data acquisition and measurement workflow involves many hardware and software components and it has to be tested that all the pieces work well together. This is not specific to open-source software, but has to be done for all commercial, FDA-approved software and hardware, too.</p>

---
