---
topic_id: 8829
title: "Cannot Save Binary Mask Of Annottated Images From Segmentati"
date: 2019-10-18
url: https://discourse.slicer.org/t/8829
---

# Cannot save binary mask of annottated images from Segmentation module

**Topic ID**: 8829
**Date**: 2019-10-18
**URL**: https://discourse.slicer.org/t/cannot-save-binary-mask-of-annottated-images-from-segmentation-module/8829

---

## Post #1 by @Pinar_Uskaner_Hepsag (2019-10-18 08:53 UTC)

<p>I am very new in Slicer. I want to save binary masks of annotated images. I cannot save binary masks of all annotated images using export binary label map in segmentations module. When ı right click in the DATA module and tell the export to dicom, I can see the binary mask of the only one image all other segmented slices are seen as white not like a binary mask. What I am doing wrong?</p>

---

## Post #2 by @lassoan (2019-10-22 13:27 UTC)

<p>Are you sure you need the segmentation results in DICOM format?<br>
You can save the segmentation as labelmap by right-clicking on the segmentation in Data module to export to binary labelmap then use menu: File / Save to save as nrrd file.</p>

---

## Post #3 by @Pinar_Uskaner_Hepsag (2019-10-23 05:45 UTC)

<p>No. I do not need to the segmentation results in DICOM format. But I just want to check binary results. How can I visualize nrrd file? Or How can I see binary images ?</p>
<p>Thanks,</p>
<p>Pinar</p>

---

## Post #4 by @muratmaga (2019-10-23 05:54 UTC)

<p>As Andras said, after segmentation all you need to do is to right click on your segment name in the Data module, and export it to a binary label map.</p>
<p>After that if you want to save the labelmap as NRRD or NIFTI, just use the regular Save dialog box.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c90079f90db9576e1815155814adffd64e6d3339.png" data-download-href="/uploads/short-url/sG8ZwE2eI55SyuAJKaX29c2hE5b.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c90079f90db9576e1815155814adffd64e6d3339_2_690x349.png" alt="image" data-base62-sha1="sG8ZwE2eI55SyuAJKaX29c2hE5b" width="690" height="349" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c90079f90db9576e1815155814adffd64e6d3339_2_690x349.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c90079f90db9576e1815155814adffd64e6d3339.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c90079f90db9576e1815155814adffd64e6d3339.png 2x" data-dominant-color="CACDCD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">933×472 72.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
