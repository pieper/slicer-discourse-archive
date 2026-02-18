# Nifti file sform and Slicer image origin seem to disagree

**Topic ID**: 7711
**Date**: 2019-07-22
**URL**: https://discourse.slicer.org/t/nifti-file-sform-and-slicer-image-origin-seem-to-disagree/7711

---

## Post #1 by @mikebind (2019-07-22 21:28 UTC)

<p>Hello, I have a nifti file (.nii.gz), and when I load it in Slicer, the Volumes module reports IJK to RAS direction matrix is diagonal with -1,1,1 on the diagonal, and an origin of approx 124,78,-142 mm.  However, when I open the same file with another tool (BioImage Suite) which has the ability to display the nifti header information, it displays the sform as</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>x=</th>
<th>(   -0.488   +0.000   +0.000 +124.756 )</th>
</tr>
</thead>
<tbody>
<tr>
<td>y =</td>
<td>(   +0.000   -0.488   +0.000 +328.256 )</td>
</tr>
<tr>
<td>z =</td>
<td>(   +0.000   +0.000   +1.000 -142.000)</td>
</tr>
</tbody>
</table>
</div><p>This sform is consistent with the voxel dimensions listed in both Slicer and BioImage Suite of 0.488, 0.488, 1.00 mm, but seems to disagree in both the direction (note the negative sign in the 2,2 position) and offset (note 328 vs 78) of the second dimension (the anterior-posterior axis).  Quantitatively, the offsets differ by the image size in the AP direction (512 voxels x 0.488 mm = 250 mm; and the BioImage Suite-reported offset (origin second dimension) is exactly 250 mm greater than the Slicer-reported offset).  I  am confused about where this difference might be coming from.  I suspect BioImage Suite is simply reporting the sform as it is recorded in the nifti file, and Slicer is doing some additional interpretation, but I’m not sure how to check that or figure out what exactly Slicer is doing during import of this file.  The nifti file was generated from an original dicom by dcm2niix.</p>
<p>I would be grateful for help with understanding where this difference might be coming from. Thanks for taking a look.</p>

---

## Post #2 by @pieper (2019-07-22 21:54 UTC)

<p>Have you looked through this? <a href="https://www.slicer.org/wiki/Coordinate_systems" rel="nofollow noopener">https://www.slicer.org/wiki/Coordinate_systems</a></p>

---

## Post #3 by @mikebind (2019-07-23 15:04 UTC)

<p>Yes, I have, thanks.</p>
<p>Upon further investigation with MATLAB’s niftiinfo, it appears that it is BioImage Suite, not Slicer, which is altering the raw sform code.  I still don’t know why it is happening, but Slicer is doing what I expect, so I no longer have a question for the Slicer community.</p>
<p>Thanks <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
