# Is it possible to segment one organ from multiple volumes?

**Topic ID**: 1246
**Date**: 2017-10-19
**URL**: https://discourse.slicer.org/t/is-it-possible-to-segment-one-organ-from-multiple-volumes/1246

---

## Post #1 by @Diana (2017-10-19 10:59 UTC)

<p>I have multiple MRI volume data, one volume is clear in coronal view, but has bad resolution in the rest two views, then another volume is clear in transversal view, but has bad resolution in others. I would like to know if it is possible to segment a model with the use of slices from one volume in one directoin, and slices from another volume in another direction. The volumes are spatially identical, they were taken within one measurment.</p>
<p>thank you for any responses</p>

---

## Post #2 by @lassoan (2017-10-19 14:35 UTC)

<p>Yes, you can do this using Segment editor module. Before you start segmenting, create a volume that has the desired resolution:</p>
<ul>
<li>Go to Crop Volume module</li>
<li>Select isotropic voxel size by checking Isotropic spacing checkbox</li>
<li>Recommended: set the region of interest to be just slightly larger than your region of interest (this will reduce memory need and processing time during segmentation)</li>
<li>Click Apply</li>
<li>Go to Segment Editor volume and select this new cropped&amp;resampled volume as Master volume (may be selected by default)</li>
</ul>
<p>The master volume that you select first will determine the resolution of your segmentation, that is why it is important to select the cropped&amp;resampled volume first. After that you can freely switch between master volumes.</p>

---
