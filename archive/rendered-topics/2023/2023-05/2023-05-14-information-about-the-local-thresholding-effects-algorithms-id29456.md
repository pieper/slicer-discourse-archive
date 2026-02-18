# Information about the local thresholding effect's algorithms

**Topic ID**: 29456
**Date**: 2023-05-14
**URL**: https://discourse.slicer.org/t/information-about-the-local-thresholding-effects-algorithms/29456

---

## Post #1 by @paolo (2023-05-14 11:28 UTC)

<p>Hi everyone!<br>
I’m using the local threshold effect to segment different kinds of tissues (eg. lung parenchyma), and I was wondering about how does the segmentation algorithms work in the extension.<br>
I read that the effect adds connected voxels to segments that are within a specified threshold (that could be selected either manually or automatically) by performing a flood fill based on masking, growcut or watershed. So, my question is: how is the starting point (i.e. the point from which the connected voxels within the intensity range are added) of the algorithms chosen? And, is there any difference with simple thresholding if I don’t ctrl+left click? In other words, once the theshold is selcted, is the flood fill automatic or I necessary have to manually ctrl+left click?<br>
Thank you!</p>
<p>Paolo</p>

---

## Post #2 by @rbumm (2023-05-14 18:11 UTC)

<p>Hi Paolo,</p>
<p>Simply set the thresholds until the structure that you want to segment is homogeneously filled, then Ctrl+ left-click into the organ/structure/tumor you want to segment. The fill should be automatic. Please remember to select the segment that you want to be affected and that this segment is visible. Please uncheck “Editable intensity range”. Play with the diameter setting. 3mm is good for a medium-sized lung tumor.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72ed76d031ff999d6cc77d54f834a514e712be78.png" data-download-href="/uploads/short-url/goHc9ZXSNH0b2oobB93DwmzYXmE.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72ed76d031ff999d6cc77d54f834a514e712be78_2_603x500.png" alt="image" data-base62-sha1="goHc9ZXSNH0b2oobB93DwmzYXmE" width="603" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72ed76d031ff999d6cc77d54f834a514e712be78_2_603x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/72ed76d031ff999d6cc77d54f834a514e712be78_2_904x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72ed76d031ff999d6cc77d54f834a514e712be78.png 2x" data-dominant-color="D4CBB2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">978×810 276 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @paolo (2023-05-14 20:05 UTC)

<p>Thank you! Your screenshot was very useful!</p>

---
