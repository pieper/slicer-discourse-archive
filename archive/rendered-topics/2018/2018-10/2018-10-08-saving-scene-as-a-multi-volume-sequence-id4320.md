# Saving scene as a multi volume sequence

**Topic ID**: 4320
**Date**: 2018-10-08
**URL**: https://discourse.slicer.org/t/saving-scene-as-a-multi-volume-sequence/4320

---

## Post #1 by @Melanie (2018-10-08 13:06 UTC)

<p>Hi, How could I save a multi volume sequence ( output volumes and output transforms) so I can retrieve the scene. I saved scene as mrml and nothing loads , output volumes seq.nrrd loads but does not have my fiducial markers on it. Thanks<br>
Also if I increase the voxel size or down sampling dicom data how will that affect accuracy of a fiducial marker placed please. thanks</p>

---

## Post #2 by @lassoan (2018-10-08 14:32 UTC)

<aside class="quote no-group" data-username="Melanie" data-post="1" data-topic="4320">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/35a633/48.png" class="avatar"> Melanie:</div>
<blockquote>
<p>How could I save a multi volume sequence ( output volumes and output transforms) so I can retrieve the scene. I saved scene as mrml and nothing loads , output volumes seq.nrrd loads but does not have my fiducial markers on it. Thanks</p>
</blockquote>
</aside>
<p>We need more information. What Slicer version do you use, how do you create sequence, fiducial markers, …? Can you also share the scene that does not load?</p>
<aside class="quote no-group" data-username="Melanie" data-post="1" data-topic="4320">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/35a633/48.png" class="avatar"> Melanie:</div>
<blockquote>
<p>Also if I increase the voxel size or down sampling dicom data how will that affect accuracy of a fiducial marker placed please. thank</p>
</blockquote>
</aside>
<p>Markup fiducials are stored in RAS coordinate system, independently from the volume. So, resolution of the volume does not directly affect accuracy of point placement. Of course, if the image is more blurry then it may be more difficult for users to identify anatomical points accurately.</p>

---

## Post #3 by @Melanie (2018-10-08 14:57 UTC)

<p>hank you very much Prof Lasso. Could I do this for a volume sequence (4D CT data set) using volumes module please.</p>

---

## Post #4 by @lassoan (2018-10-09 15:25 UTC)

<p>You can resample an entire volume sequence using “Crop volume sequence” module.</p>

---
