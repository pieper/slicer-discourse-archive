---
topic_id: 48525
title: "After midline mirroring of the ROI, how to edit the resulting mirrored region?"
date: 2026-10-15
url: https://discourse.slicer.org/t/48525
last_bumped: 2026-10-15T15:29:57.479Z
---

# After midline mirroring of the ROI, how to edit the resulting mirrored region?

**Topic ID**: 48525
**Date**: 2026-10-15
**URL**: https://discourse.slicer.org/t/after-midline-mirroring-of-the-roi-how-to-edit-the-resulting-mirrored-region/48525

---

## Post #1 by @Gargantua (2026-10-15 15:02 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/733674b800aee76ac27136f771382ee098579173.jpeg" data-download-href="/uploads/short-url/grdzZ3oKC1cvFOz3rvi4KjKsx3l.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/733674b800aee76ac27136f771382ee098579173_2_690x459.jpeg" alt="image" data-base62-sha1="grdzZ3oKC1cvFOz3rvi4KjKsx3l" width="690" height="459" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/733674b800aee76ac27136f771382ee098579173_2_690x459.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/733674b800aee76ac27136f771382ee098579173_2_1035x688.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/733674b800aee76ac27136f771382ee098579173_2_1380x918.jpeg 2x" data-dominant-color="ACACAC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1279 261 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>For the obtained mirrored region, can areas with HU values less than 20 be ignored using the threshold function, or erased with the eraser tool?</p>

---

## Post #2 by @Rei_Kurosawa (2026-10-15 15:27 UTC)

<p>Both routes work, and the Segment Editor documentation covers both:</p>
<p><strong>1. Threshold effect.</strong> The documentation says to use the Threshold effect to determine a threshold range and then either save the result to the selected segment or use it as the “Editable intensity range”. If you set the lower bound to 20 HU and apply it to the mirrored segment, the segment keeps only voxels at 20 HU and above, so the HU&lt;20 areas are dropped in one step. This rewrites the segment contents; the module saves undo states before each effect (last 10 by default), so you can step back if the range was off.</p>
<p><strong>2. Eraser with masking.</strong> Under “Masking options”, the “Editable intensity range” setting limits changes to areas where the source volume’s voxels fall inside the chosen intensity range. With the range starting at 20 HU, the eraser only touches voxels within that band and leaves the low-HU parts alone while you clean up manually. The same documentation notes the intensity range can be previewed with the Threshold effect before you commit to it.</p>
<p>For a one-shot cleanup of the whole mirrored region I would try route 1 first; route 2 is the better fit if you only want to remove specific spots.</p>

---

## Post #3 by @mikebind (2026-10-15 15:29 UTC)

<p>Yes, for most segment editor tools, you can set masking settings so that changes can only be made in areas meeting certain criteria.   One of these settings can be an intensity range.  See <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#masking-options" rel="noopener nofollow ugc">this page</a> and read the section on masking settings. You can set your eraser brush size to be 3D and very large while masking the editing to values below 20, and easily edit your segment.<br>
Alternatively, you can achieve the same thing using logical operators (a different segment editor tool).  You can create a new segment, threshold it to regions less than 20, and then logically subtract that new segment from your original segment.</p>

---
