---
topic_id: 21506
title: "Saving A Segmentation And Input Volume In One File"
date: 2022-01-18
url: https://discourse.slicer.org/t/21506
---

# Saving a segmentation and input volume in one file

**Topic ID**: 21506
**Date**: 2022-01-18
**URL**: https://discourse.slicer.org/t/saving-a-segmentation-and-input-volume-in-one-file/21506

---

## Post #1 by @3Dslicerhelp (2022-01-18 02:42 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11.20200930</p>
<p>Hello,</p>
<p>I uploaded a CT dicom image set into Slicer and segmented a region of interest. Now, I would like to save both my input volume and segmentation into a single file (preferably .nrrd). Is there a way I am able to do this?</p>
<p>I have attempted to export my segmentation as a labelmap; however, this only saves the segmentation without the CT dicoms. I need the 3D CT volume with the segmentation included as my label.</p>
<p>My end goal is to use these .nrrd files as inputs for a deep learning model that requires labelled image sets.</p>
<p>Thanks,<br>
K.</p>

---

## Post #2 by @3Dslicerhelp (2022-01-19 15:09 UTC)

<p>I uploaded a CT dicom image set into Slicer and segmented a region of interest. Now, I would like to save both my input volume and segmentation into a single file (preferably .nrrd). Is there a way I am able to do this?</p>
<p>I have attempted to export my segmentation as a labelmap; however, this only saves the segmentation without the CT dicoms. I need the 3D CT volume with the segmentation included as my label.</p>
<p>My end goal is to use these .nrrd files as inputs for a deep learning model that requires labelled image sets.</p>
<p>Thanks!</p>

---

## Post #3 by @lassoan (2022-01-27 06:59 UTC)

<p>Normally you save the input CT volume and the segmentation as separate files - see all the deep learning data sets that you can find online. This makes sense because the scalar type of the volumes are often different (16-bit for CT, 8-bit for labelmap), the entropy of a CT and a labelmap is vastly different, so you can compress them better if you store them as two separate files, the correspondence between a CT and segmentation is not always 1-to-1 (there can be several segmentations for a CT, for example, by different experts), etc.</p>

---

## Post #4 by @rbumm (2022-01-27 10:35 UTC)

<p>To package mrml, ct.nrrd and segmentation.nrrd into one MRB file you can click this symbol:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61b690c7a704da2986adbaa72f5962ccfc8dd653.png" data-download-href="/uploads/short-url/dWpsumMW5txJDkalNYiGa9lSnRx.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61b690c7a704da2986adbaa72f5962ccfc8dd653_2_690x401.png" alt="image" data-base62-sha1="dWpsumMW5txJDkalNYiGa9lSnRx" width="690" height="401" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/1/61b690c7a704da2986adbaa72f5962ccfc8dd653_2_690x401.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61b690c7a704da2986adbaa72f5962ccfc8dd653.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61b690c7a704da2986adbaa72f5962ccfc8dd653.png 2x" data-dominant-color="D2D2D2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">700×407 79.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
