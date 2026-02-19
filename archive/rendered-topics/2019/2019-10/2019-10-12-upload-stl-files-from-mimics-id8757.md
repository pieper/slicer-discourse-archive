---
topic_id: 8757
title: "Upload Stl Files From Mimics"
date: 2019-10-12
url: https://discourse.slicer.org/t/8757
---

# upload STL files from Mimics

**Topic ID**: 8757
**Date**: 2019-10-12
**URL**: https://discourse.slicer.org/t/upload-stl-files-from-mimics/8757

---

## Post #1 by @f.rota (2019-10-12 15:58 UTC)

<p>Hi, I am working on 3d Slicer to make segmentations of the knee on MR images. The other colleagues work on Mimics. When I export my segmentation as an .stl file and they open it on Mimics, the 3d model is not overlapped to the MRI. The same problem happens when I upload their models on 3d slicer. Are there any tools that can solve this problem? What are they?<br>
I attach you an example.<br>
Thank you.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c7fac62bc5d2a79f32d605c58391692d6486b07.jpeg" data-download-href="/uploads/short-url/446UiR3Xl13cg7KTmwH1LAfMM4v.jpeg?dl=1" title="femur" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c7fac62bc5d2a79f32d605c58391692d6486b07_2_690x472.jpeg" alt="femur" data-base62-sha1="446UiR3Xl13cg7KTmwH1LAfMM4v" width="690" height="472" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c7fac62bc5d2a79f32d605c58391692d6486b07_2_690x472.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1c7fac62bc5d2a79f32d605c58391692d6486b07_2_1035x708.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c7fac62bc5d2a79f32d605c58391692d6486b07.jpeg 2x" data-dominant-color="52535C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">femur</span><span class="informations">1232×844 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2019-10-12 16:00 UTC)

<p>Probably Mimics assumes that mesh point coordinates are in LPS coordinates system. To create such an STL file, choose to use LPS coordinate system when you export your segments using “Export to files”.</p>

---
