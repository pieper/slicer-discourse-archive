# View 3 CT scans that are orthogonal perspectives of the same scan

**Topic ID**: 31814
**Date**: 2023-09-20
**URL**: https://discourse.slicer.org/t/view-3-ct-scans-that-are-orthogonal-perspectives-of-the-same-scan/31814

---

## Post #1 by @benalb (2023-09-20 20:22 UTC)

<p>I have figured out a way to do this, but I would appreciate if anyone with experience could tell me if I’ve done it right.</p>
<p>The CT scans in my dataset consist of the axial, sagittal, and coronal perspectives in separate files. Although I perform segmentation on the axial perspective, viewing the other perspectives are important for accurate segmentation.</p>
<p>How I view the 3 scans of different perspectives is as follows:</p>
<ol>
<li>Load the axial, sagittal and coronal scans in the DICOM viewer</li>
<li>Go to “View Controllers” and change the Green view to show the coronal scan and the Yellow view to show the sagittal scan. <strong>I leave the dropdown next to the file name as “reformat”, instead of changing it to axial, sagittal or coronal</strong></li>
</ol>
<p>Is leaving it in “reformat” the appropriate way to do this?<br>
Also, I notice Slicer 3D performs gantry tilt correction. If I use the linked crosshair, will it actually point to the right spot in the sagittal and coronal scans, since they are separate scans and not just 3d reconstructions of the original scan?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2023-09-22 18:53 UTC)

<aside class="quote no-group" data-username="benalb" data-post="1" data-topic="31814">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/c2a13f/48.png" class="avatar"> benalb:</div>
<blockquote>
<p>The CT scans in my dataset consist of the axial, sagittal, and coronal perspectives in separate files. Although I perform segmentation on the axial perspective, viewing the other perspectives are important for accurate segmentation.</p>
</blockquote>
</aside>
<p>Unfortunately, many hospitals discard the original thin-slice CTs and only save 3 volumes with thick slices. This is not a problem for human readers, as they review the image in the 3 standard orientations, but for any 3D processing, segmentation, visualization, these 3 volumes contain much less information than the original volume.</p>
<aside class="quote no-group" data-username="benalb" data-post="1" data-topic="31814">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/c2a13f/48.png" class="avatar"> benalb:</div>
<blockquote>
<p>Although I perform segmentation on the axial perspective, viewing the other perspectives are important for accurate segmentation.</p>
</blockquote>
</aside>
<p>You cannot recover the information that is lost when they deleted the original thin-slice image. If you want to get highest-quality segmentaitons then you have to demand imaging technicians to save the original high-resolution 3D image not just these thick-slice reconstructions.</p>
<aside class="quote no-group" data-username="benalb" data-post="1" data-topic="31814">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/c2a13f/48.png" class="avatar"> benalb:</div>
<blockquote>
<p>I leave the dropdown next to the file name as “reformat”, instead of changing it to axial, sagittal or coronal</p>
</blockquote>
</aside>
<p>You don’t need to worry about this, Segment Editor will automatically align the view planes to match the closest axis of segmentation’s internal labelmap image when you start editing the segmentation.</p>
<aside class="quote no-group" data-username="benalb" data-post="1" data-topic="31814">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/c2a13f/48.png" class="avatar"> benalb:</div>
<blockquote>
<p>Also, I notice Slicer 3D performs gantry tilt correction. If I use the linked crosshair, will it actually point to the right spot in the sagittal and coronal scans, since they are separate scans and not just 3d reconstructions of the original scan?</p>
</blockquote>
</aside>
<p>Yes, Slicer will show the correct positions in all views. However, if you do segmentation, I would recommend to choose the volume from the 3 that contains the most useful details, harden the transform and resample the volume to have isotropic resolution (same resolution along all 3 axes) using Crop Volume module, and then use this volume as source volume for segmentation. Hardening the transform makes it easier to use the segmentation results in other software (not all software can apply non-linear transforms on images and segmentations) and the isotropic resolution allows storing finer details in the segmentation than what can be stored in a thick-slice volume.</p>

---

## Post #3 by @benalb (2023-09-24 05:08 UTC)

<p>Thanks for the detailed response! I’m doing segmentation on the axial volume as it is what’s done in literature.</p>
<p>Also, I must have characterised it wrongly, but it wasn’t gantry tilt, but rather the correction for uneven spacing between slices.<br>
“Images are not equally spaced (a difference of -0.999998 vs 3 in spacings was detected).  Slicer will apply a transform to this series trying to regularize the volume. Please use caution.”<br>
Would you also recommend hardening this transform?<br>
If I do not harden this transform, how would it affect the segmentation exported as a NIFTI file?</p>
<p>Lastly, is it important to resample the volume to have isotropic resolution if the segmentations are in 1 plane only? Currently, my segmentation output has fine resolution in the axial plane, but coarse resolution in the other planes, and this matches the idea of a thick-slice axial volume.</p>
<p>I would think that resampling would be adding detail in the superior-inferior axis that doesn’t exist, duplicating isotropic voxels up to the slice thickness, and not affecting the volume calculation anyways. Perhaps you are saying that I could use the coronal and sagittal scans as segmentation references, and when painting them in, the isotropic segmentation (based on the resampled axial scan) can pick up the detail?</p>
<p>Is it possible to resample and combine all 3 CT scans?</p>

---
