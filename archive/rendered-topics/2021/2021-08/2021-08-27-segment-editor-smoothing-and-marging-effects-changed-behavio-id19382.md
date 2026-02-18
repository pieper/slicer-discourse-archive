# Segment editor Smoothing and marging effects changed behavior from 4.11 to 4.13

**Topic ID**: 19382
**Date**: 2021-08-27
**URL**: https://discourse.slicer.org/t/segment-editor-smoothing-and-marging-effects-changed-behavior-from-4-11-to-4-13/19382

---

## Post #1 by @caioath (2021-08-27 02:26 UTC)

<p>Hi all</p>
<p>4.11<br>
Running smoothing effect using a certain intensity range, it would get rid of every labeled voxel that was outside of the editable intensity range.<br>
Margin effect would remove every labeled voxel outside of the editable intensity range and would also perform the shrinking or growing within the range<br>
So both would perform their operations but would also clean wrongly labeled voxels, which is very interesting while doing manual segmentation.</p>
<p>4.13<br>
Both margin and smoothing effects ignore labelled voxels that are out of the Editable intensity range.<br>
Images bellow show the different behavior of the different versions for the same task (median smoothing within the same intensity range and same kernel (3px))</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/5322f152993b2b46b2e8c7d822db77df3162e1b9.png" data-download-href="/uploads/short-url/bRsuEl4iDgEhoijsmx74GBQCrdT.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/5322f152993b2b46b2e8c7d822db77df3162e1b9_2_342x250.png" alt="image" data-base62-sha1="bRsuEl4iDgEhoijsmx74GBQCrdT" width="342" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/5322f152993b2b46b2e8c7d822db77df3162e1b9_2_342x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/5322f152993b2b46b2e8c7d822db77df3162e1b9_2_513x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/5322f152993b2b46b2e8c7d822db77df3162e1b9_2_684x500.png 2x" data-dominant-color="313A40"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">930×678 64.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is this an expected behavior? If so, does anyone can give me a hint to easily erase all the voxels that are out of a certain intensity range?</p>
<p>Thanks</p>
<p>Caio</p>

---
