# different image dimentions in two cMRI scans of the same swine

**Topic ID**: 17323
**Date**: 2021-04-26
**URL**: https://discourse.slicer.org/t/different-image-dimentions-in-two-cmri-scans-of-the-same-swine/17323

---

## Post #1 by @Omer_Bahary (2021-04-26 06:04 UTC)

<p>Hello,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3da70f1c5460c6f05697c2f62c68ba060789aca0.png" data-download-href="/uploads/short-url/8Np2Yy6SGjOWe1exJYtbsG0hFSM.png?dl=1" title="healthy-dimensions" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3da70f1c5460c6f05697c2f62c68ba060789aca0.png" alt="healthy-dimensions" data-base62-sha1="8Np2Yy6SGjOWe1exJYtbsG0hFSM" width="689" height="251" data-dominant-color="303030"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">healthy-dimensions</span><span class="informations">1223×446 15.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>? is there a way to fix this? the 3D models of each segmentation are not in the same scale.</p>
<ol start="2">
<li>In addition, in one of the sets (“uh-dimensions”) “fill between slices” function in the segmentation editor does not work well. is there maybe a connections to the image dimensions?</li>
</ol>

---

## Post #2 by @lassoan (2021-04-26 23:16 UTC)

<p>Image dimensions and total size of the image does not depend on the specimen size, only on the imaging protocol. Physical size of an object (= object size in voxels multiplied by the voxel size) is expected to be similar if the same specimen is imaged.</p>
<p>Note that both images are single slice volumes, so you cannot really do any volume measurements, only areas and distances. It is also possible that the slices are not in the exactly same anatomical location, so you may find significant size differences.</p>
<p>What is your overall goal with these images? What is the clinical application? What would you like to measure or compare?</p>

---

## Post #3 by @Omer_Bahary (2021-05-01 13:17 UTC)

<p>Hey lassoan, thanks for the respond.<br>
I am creating a 3d model of the heart in two stages of a heart condition (hfpef) by segmentation of the scans in healthy and unhealthy states (the two scans in the previous mesaage). This is why the differences in dimensions presented in the previous message are odd. Any insights?<br>
Regards,<br>
Omer</p>

---

## Post #4 by @lassoan (2021-05-01 13:43 UTC)

<p>It seems you have 2D (maybe 2D+t) images. How do you plan to create 3D model from them? Do you have 3D volumes as well?</p>
<p>2D images can be taken of different parts of the heart, so it is normal to have some size differences, but physical size should be at least the same magnitude in all images.</p>

---
