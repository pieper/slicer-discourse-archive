# How i can calculate overall volume of air and lattice

**Topic ID**: 36251
**Date**: 2024-05-18
**URL**: https://discourse.slicer.org/t/how-i-can-calculate-overall-volume-of-air-and-lattice/36251

---

## Post #1 by @Vikram (2024-05-18 12:42 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55a490daa4a7312bd545b1510a88a85e14a7b5ad.png" data-download-href="/uploads/short-url/cdDagOTyaxTeC4cqYexwCe3f7cN.png?dl=1" title="STATICS CUBIC 4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55a490daa4a7312bd545b1510a88a85e14a7b5ad_2_690x307.png" alt="STATICS CUBIC 4" data-base62-sha1="cdDagOTyaxTeC4cqYexwCe3f7cN" width="690" height="307" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55a490daa4a7312bd545b1510a88a85e14a7b5ad_2_690x307.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55a490daa4a7312bd545b1510a88a85e14a7b5ad_2_1035x460.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/55a490daa4a7312bd545b1510a88a85e14a7b5ad_2_1380x614.png 2x" data-dominant-color="F7F5F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">STATICS CUBIC 4</span><span class="informations">1885×841 61 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
HI I read , but i did not understand there is deferent parameter in this figure , actually i want to calculate overall volume of air and lattice in segmented image , but in this volume LM , Volume cs , surface area , which one i can chose to calculate overall concentration</p>

---

## Post #2 by @mikebind (2024-05-18 23:07 UTC)

<p>The distinctions are described in the documentation, found here:<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html</a></p>
<p>LM is the volume based on counting voxels in the label map representation.  CS is the volume based on the region enclosed by the closed surface representation.  These should always be similar, but can differ slightly due to smoothing applied to the surface representation.   Which you should use for your purposes depends on whether you consider the label map or surface representations to be more reliable.  In any case, it generally should make only very little difference which one you use.</p>

---
