# Help with planning a path for biopsy using axial and saggital cuts (mark up a line or cylinder)

**Topic ID**: 14287
**Date**: 2020-10-28
**URL**: https://discourse.slicer.org/t/help-with-planning-a-path-for-biopsy-using-axial-and-saggital-cuts-mark-up-a-line-or-cylinder/14287

---

## Post #1 by @roger_hightower (2020-10-28 12:34 UTC)

<p>Thank you so much for taking this question. I would like to plan a path for insertion of a biopsy probe on axial and sagittal images. I do not need anything in 3D rendering. Is there a simple way to do this? I would like to, for instance, mark something up in the axial and then be able to modify it in sagittal. For instance, with a brain biopsy. Thank you. It would look like a small 3D cylinder when inserted. Thank you.</p>

---

## Post #2 by @lassoan (2020-10-28 12:49 UTC)

<p>You can use the Path Explorer module in SlicerIGT extension for this. You specify entry point and target point and create a path from them by clicking “Add path”. To explore multiple paths, you can define multiple entry and target points and add paths for arbitrary combinations of them.</p>
<p>You can then select a path in Visualization section and click on the red, yellow, green buttons to enable reslicing using that plane.</p>
<p>Tips and tricks:</p>
<ul>
<li>you need to enable slice intersections to see where the perpendicular view intersects the path</li>
<li>disable reslicing on the plane where you want to adjust the target/entry point on (you can click on a target or entry point to show that position in all slices)</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d659e2777f30848fab19f422b725ecbcb57643ce.jpeg" data-download-href="/uploads/short-url/uAeKQBtz47A0wRBI9tjnY4vD3Bk.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d659e2777f30848fab19f422b725ecbcb57643ce_2_690x420.jpeg" alt="image" data-base62-sha1="uAeKQBtz47A0wRBI9tjnY4vD3Bk" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d659e2777f30848fab19f422b725ecbcb57643ce_2_690x420.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d659e2777f30848fab19f422b725ecbcb57643ce_2_1035x630.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d659e2777f30848fab19f422b725ecbcb57643ce_2_1380x840.jpeg 2x" data-dominant-color="8F8F91"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1374 659 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @roger_hightower (2020-10-28 13:47 UTC)

<p>Thank you very much. If I have a full body MRI, how can I create an ROI that only encompasses the head/brain? Thank you again.</p>

---

## Post #4 by @lassoan (2020-10-29 13:54 UTC)

<p>You can crop your volume to a specified region using Crop volume module.</p>

---
