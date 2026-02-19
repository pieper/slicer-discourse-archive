---
topic_id: 14959
title: "Segment Mesher To Generate Volumetric Mesh Offset Issue"
date: 2020-12-09
url: https://discourse.slicer.org/t/14959
---

# Segment Mesher to generate volumetric mesh - Offset issue

**Topic ID**: 14959
**Date**: 2020-12-09
**URL**: https://discourse.slicer.org/t/segment-mesher-to-generate-volumetric-mesh-offset-issue/14959

---

## Post #1 by @suranga (2020-12-09 11:25 UTC)

<p>I’m using a publicly available dataset which consists of both CT volume and corresponding segmentation mask in nifti format. This image volume consists of below set of categories.</p>
<p>0: Background (None of the following organs)<br>
1: Liver<br>
2: Bladder<br>
3: Lungs<br>
4: Kidneys<br>
5: Bone<br>
6: Brain</p>
<p>I need to generate the volumetric liver for each CT volume and then project their coordinates to the DRR image plane.</p>
<p>As the first step, I have first converted the multi-organ segmentation mask image to a 3D binary mask image for the first CT volume by substituting non-liver intensities to zero for all the slices and fed this into 3D slicer to generate the tetrahedral mesh for the liver (see the attached images) using the Segment Mesher extension. I have here generated the TetGen-based volumetric mesh.</p>
<p>After that I have projected vertex coordinates of the volumetric liver onto the DRR image plane of the corresponding CT volume (DRR image taken by applying Syddon-Jacob Ray tracing algorithm in ITK), but they are not aligned as you can see in the attached image.</p>
<p>My question is that, in 3D slicer, when producing the volumetric mesh, does it encounter the original image origin and pixel spacing ? Or adding any offset to the volumetric mesh ?</p>
<p>(I have implemented an algorithm to project each 3D vertex coordinate of the volumetric mesh onto the DRR plane in the same way that the Syddon-Jacob algorithm does. I am convinced that this vertex projection is correct because I have done testing manually as well )</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/96c2891ef5546320013d641ee8a7b2e072552fd1.png" data-download-href="/uploads/short-url/lvGpuLvaBxVLYxs1Nml3RYPSqjf.png?dl=1" title="3D_Slicer_liver_mesh" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96c2891ef5546320013d641ee8a7b2e072552fd1_2_690x327.png" alt="3D_Slicer_liver_mesh" data-base62-sha1="lvGpuLvaBxVLYxs1Nml3RYPSqjf" width="690" height="327" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96c2891ef5546320013d641ee8a7b2e072552fd1_2_690x327.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96c2891ef5546320013d641ee8a7b2e072552fd1_2_1035x490.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96c2891ef5546320013d641ee8a7b2e072552fd1_2_1380x654.png 2x" data-dominant-color="686970"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3D_Slicer_liver_mesh</span><span class="informations">1915×909 89.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5bb2b6da4422acd0c50d65da7c9d72e3a369441c.jpeg" data-download-href="/uploads/short-url/d5clhThAC4gw4CXRl5HeUDglcmw.jpeg?dl=1" title="volume-10_aligned" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5bb2b6da4422acd0c50d65da7c9d72e3a369441c_2_500x500.jpeg" alt="volume-10_aligned" data-base62-sha1="d5clhThAC4gw4CXRl5HeUDglcmw" width="500" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5bb2b6da4422acd0c50d65da7c9d72e3a369441c_2_500x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5bb2b6da4422acd0c50d65da7c9d72e3a369441c_2_750x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5bb2b6da4422acd0c50d65da7c9d72e3a369441c_2_1000x1000.jpeg 2x" data-dominant-color="202017"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">volume-10_aligned</span><span class="informations">1024×1024 81 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @suranga (2020-12-10 12:50 UTC)

<p>Issue is resolved. The issue is with the label mask in the original dataset. I have centred the label mask when loading it by enabling options in the 3D slicer and the issue is fixed.</p>
<p>Does Slicer has a way to downsample the number of nodes ? If so how ?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7a8e45e0d1c2772dbf15179c44610ab3a38ccc2.jpeg" data-download-href="/uploads/short-url/sugRHDahmkoU5MLZwHyJPMJwSfU.jpeg?dl=1" title="volume-10_aligned_slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c7a8e45e0d1c2772dbf15179c44610ab3a38ccc2_2_500x500.jpeg" alt="volume-10_aligned_slicer" data-base62-sha1="sugRHDahmkoU5MLZwHyJPMJwSfU" width="500" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c7a8e45e0d1c2772dbf15179c44610ab3a38ccc2_2_500x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c7a8e45e0d1c2772dbf15179c44610ab3a38ccc2_2_750x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c7a8e45e0d1c2772dbf15179c44610ab3a38ccc2_2_1000x1000.jpeg 2x" data-dominant-color="252516"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">volume-10_aligned_slicer</span><span class="informations">1024×1024 98.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @suranga (2020-12-17 12:34 UTC)

<p>Does Slicer has a way to down-sample the number of nodes ? If so how ? I’m asking this because I need to reduce the number of nodes that represents the volumetric liver mesh.</p>

---

## Post #4 by @lassoan (2020-12-17 21:06 UTC)

<p>Yes, there are several modules for resampling and decimation. What is your input and output data types (surface mesh, volumetric mesh, labelmap volume, or grayscale volume)?</p>

---

## Post #5 by @suranga (2020-12-17 21:31 UTC)

<p>The input to the 3D slicer is a labelmap image volume actually it is a binary mask volume and the output should be a volumetric mesh.</p>

---

## Post #6 by @lassoan (2020-12-17 21:50 UTC)

<p>You can convert the labelmap into a segmentation node (right-click in Data module) and use Segment Mesher module to create volumetric mesh. There are several parameters to adjust to change the resolution.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a81228b75d520debcd301894735519f9e48aa2d.jpeg" data-download-href="/uploads/short-url/8lymxKQgFmhrNgxUthN7kO5Xcy9.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a81228b75d520debcd301894735519f9e48aa2d_2_690x419.jpeg" alt="image" data-base62-sha1="8lymxKQgFmhrNgxUthN7kO5Xcy9" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a81228b75d520debcd301894735519f9e48aa2d_2_690x419.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a81228b75d520debcd301894735519f9e48aa2d_2_1035x628.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a81228b75d520debcd301894735519f9e48aa2d_2_1380x838.jpeg 2x" data-dominant-color="9FA1A3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1371 527 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1bc3a9effc5e4de2a33af1d6199f3f07fb471205.jpeg" data-download-href="/uploads/short-url/3XC6atqzKQ73qkqhfLJZ6lCjbI9.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1bc3a9effc5e4de2a33af1d6199f3f07fb471205_2_690x419.jpeg" alt="image" data-base62-sha1="3XC6atqzKQ73qkqhfLJZ6lCjbI9" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1bc3a9effc5e4de2a33af1d6199f3f07fb471205_2_690x419.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1bc3a9effc5e4de2a33af1d6199f3f07fb471205_2_1035x628.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1bc3a9effc5e4de2a33af1d6199f3f07fb471205_2_1380x838.jpeg 2x" data-dominant-color="9FA1A3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1372 535 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae34501cfbe23b42c73aa37ef63ec5335a44b5a8.jpeg" data-download-href="/uploads/short-url/oR59UlAiCQsnZYCZQjvMBpkG6Hm.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ae34501cfbe23b42c73aa37ef63ec5335a44b5a8_2_690x419.jpeg" alt="image" data-base62-sha1="oR59UlAiCQsnZYCZQjvMBpkG6Hm" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ae34501cfbe23b42c73aa37ef63ec5335a44b5a8_2_690x419.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ae34501cfbe23b42c73aa37ef63ec5335a44b5a8_2_1035x628.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ae34501cfbe23b42c73aa37ef63ec5335a44b5a8_2_1380x838.jpeg 2x" data-dominant-color="9EA1A2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1370 545 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
