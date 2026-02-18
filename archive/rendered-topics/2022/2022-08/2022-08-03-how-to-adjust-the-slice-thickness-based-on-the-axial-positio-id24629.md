# How to adjust the slice thickness based on the axial position

**Topic ID**: 24629
**Date**: 2022-08-03
**URL**: https://discourse.slicer.org/t/how-to-adjust-the-slice-thickness-based-on-the-axial-position/24629

---

## Post #1 by @Chenglin_Zhu (2022-08-03 23:41 UTC)

<p>Hi all,</p>
<p>The goal is to calculate kidney volume accurately based on the MRI. Sometimes, the abdomen MRI and pelvis MRI are composed to capture the complete kidneys. However, there could be an overlapping region between the abdomen and pelvis MRI scans, so the kidney tends to be overestimated if we do segmentations on the raw composed images.</p>
<p>Obviously, one solution is to remove dicoms from the overlapping region in pelvis scans and then combine it with the abdomen scans. We hope to include images from both sets of scans as the images from the overlapping region potentially decrease the slice thickness and enable a more accurate volume measurement.<br>
For example, the slice thickness is 6mm for both the axial abdomen and axial pelvis scans. Abdomen scans have the axial positions of 4,10,…,130, 136,142,148 while Pelvis scans have axial positions of 127,133,139,145,… Then the IDEAL composed scans have images with axial positions of  4,10,16…,127,130,133,136,139,142,145,148…with varying slice thickness: 6mm for the nonoverlapping region and 3mm for the overlapping regions.</p>
<p>The 3D slicer loads the dicoms in the correct order (based on the axial position), but the slice thickness between all slices is 6 mm. Is there a way to manually/automatically adjust the slice thickness based on the axial position?<br>
Here is the coronal view of the composed axial scans. The overlapping region was shown as the alternating bands of pixels.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b8f4aa6cf431254e78e59758ee4c1bf0cb4930d.jpeg" data-download-href="/uploads/short-url/aMqOi0MUiFXD7AOVjqPOoOUp5z7.jpeg?dl=1" title="Screen Shot 2022-08-03 at 19.39.30" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b8f4aa6cf431254e78e59758ee4c1bf0cb4930d_2_490x499.jpeg" alt="Screen Shot 2022-08-03 at 19.39.30" data-base62-sha1="aMqOi0MUiFXD7AOVjqPOoOUp5z7" width="490" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b8f4aa6cf431254e78e59758ee4c1bf0cb4930d_2_490x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b8f4aa6cf431254e78e59758ee4c1bf0cb4930d_2_735x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b8f4aa6cf431254e78e59758ee4c1bf0cb4930d_2_980x998.jpeg 2x" data-dominant-color="464742"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-08-03 at 19.39.30</span><span class="informations">1214×1238 199 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks a lot!</p>

---

## Post #2 by @pieper (2022-08-04 13:42 UTC)

<p>You can try CropVolume to extract the overlapping regions and then average them (easiest using numpy - see the script repository) and then put them back together with CropVolume and numpy or the <a href="https://discourse.slicer.org/t/combine-two-volumes-into-one-using-python/23152/5">module described here</a>.</p>

---
