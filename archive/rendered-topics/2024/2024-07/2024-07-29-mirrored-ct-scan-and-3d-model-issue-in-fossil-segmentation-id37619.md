---
topic_id: 37619
title: "Mirrored Ct Scan And 3D Model Issue In Fossil Segmentation"
date: 2024-07-29
url: https://discourse.slicer.org/t/37619
---

# Mirrored CT Scan and 3D Model Issue in Fossil Segmentation

**Topic ID**: 37619
**Date**: 2024-07-29
**URL**: https://discourse.slicer.org/t/mirrored-ct-scan-and-3d-model-issue-in-fossil-segmentation/37619

---

## Post #1 by @JaredAmudeo (2024-07-29 22:59 UTC)

<p>I have been working on the segmentation of a fossil for a while, and now that I have finished segmenting the entire body, I have realized by comparing images of the fossil and the images obtained from the medical scanner that the digital files, including the CT scans and thus the segmentation and 3D models, are mirrored. For example, in the ventral view, the two ischia are presented parallelly such that in photographs of the material and physically, the left ischium is below the right ischium, but in the segmentation, they are reversed, with the left over the right. Another example: the last caudal vertebra is broken, and in the sediment, the fragment is displaced to the right as indicated by both the fossil and the photographs, but in the segmentation, both in the CT scan views and the 3D view, it appears to the left. How can I solve this?</p>
<p>Many thanks in advance,</p>
<p>Jared.</p>

---

## Post #2 by @muratmaga (2024-07-30 01:12 UTC)

<p>This is a very common problem in research microCT because there is no convention for how to orient the samples, how the slices are reconstructed (is the left of the image is the left side of the specimen or the rights side of the specimen) and more importantly which anatomical (or coordinate) axis the increasing slice numbers describe. This is not a Slicer problem, but a data problem and happens in every 3D imaging software when working with such data.</p>
<p>In SlicerMorph we emphasize that you need to independently verify that you <strong>correctly</strong> imported the sample by visualizing it in 3D and finding the asymmetrical structure and confirming it  by observing the same on the specimen (and if specimen is not available, then by a photograph or something) before you proceed with segmentation or any other process (e.g., landmarking) that will create secondary data from the image data.</p>
<p>Since you already created the segmentation, reimporting the data will not be feasible for you. I suggest creating a linear transform in which the third diagonal element is -1 and then assign both your original volume and segmentation to it. If you can confirm that this indeed fixed your mirroring issue, then you can harden the transforms and save your datasets at that point.</p>

---

## Post #3 by @JaredAmudeo (2024-07-30 09:27 UTC)

<p>Hello! Thank you very much for your prompt response. I must admit part of the fault for not having paid close attention to the parameters before starting the segmentation. Thank you very much for the advice; it will be useful from now on. Changing the third 1 on the diagonal of the matrix seems to have solved it, but the segmentations in the 3D view appear black. How can I fix that?</p>

---

## Post #4 by @muratmaga (2024-07-30 22:22 UTC)

<p>You might have to turn on/off the 3D visibility, and retry.</p>
<p>If you can share your scene (as an MRB) with all your data in it, I can try to take alook.</p>

---

## Post #5 by @JaredAmudeo (2024-07-31 05:53 UTC)

<p>Unfortunately, I still cannot share the information and files until the work is published. However, I can leave these images that describe the behavior. Both are segmentations of the ischia; I have not yet converted them into models. When performing the linear transformation, the preview in the 3D view remains black, even after deactivating and reactivating it. Both images are in ventral view<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8cda1a643b1df9be53ff1764e5017c91df785fad.png" data-download-href="/uploads/short-url/k628273OQOjmwIqPAxSkUp6179H.png?dl=1" title="Ischia transformed ventral view" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8cda1a643b1df9be53ff1764e5017c91df785fad_2_690x450.png" alt="Ischia transformed ventral view" data-base62-sha1="k628273OQOjmwIqPAxSkUp6179H" width="690" height="450" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8cda1a643b1df9be53ff1764e5017c91df785fad_2_690x450.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8cda1a643b1df9be53ff1764e5017c91df785fad_2_1035x675.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8cda1a643b1df9be53ff1764e5017c91df785fad_2_1380x900.png 2x" data-dominant-color="9699CE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Ischia transformed ventral view</span><span class="informations">1477×964 10.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b74ac25203d9a53a43c1093775b88520ff311c7.png" data-download-href="/uploads/short-url/3USRoFdZ4eA2YPvC5SXsIkzZ8R9.png?dl=1" title="Ischia without transforming" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b74ac25203d9a53a43c1093775b88520ff311c7_2_690x450.png" alt="Ischia without transforming" data-base62-sha1="3USRoFdZ4eA2YPvC5SXsIkzZ8R9" width="690" height="450" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b74ac25203d9a53a43c1093775b88520ff311c7_2_690x450.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b74ac25203d9a53a43c1093775b88520ff311c7_2_1035x675.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/b/1b74ac25203d9a53a43c1093775b88520ff311c7_2_1380x900.png 2x" data-dominant-color="999ACF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Ischia without transforming</span><span class="informations">1477×964 52.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2024-07-31 09:30 UTC)

<p>The problem with mirroring transforms (or any linear transformation with a matrix that has a negative determinant) is that it turns surfaces inside out and so the surface appears black.</p>
<p>If you harden the transform on the segmentation and then recreate the closed surface representation then the coloring should return to normal.</p>

---

## Post #7 by @JaredAmudeo (2024-07-31 09:58 UTC)

<p>Thank you very much for your prompt response. After hardening the files, I was able to see the segments in color again in the 3D view without performing the second step you mentioned. Is it necessary to carry out that step, or can I consider the problem solved? Also, if it is necessary, in which module can I perform that task?</p>

---

## Post #8 by @muratmaga (2024-08-01 00:16 UTC)

<p>Problem is solved. Just save both of files (i.e., the segmentation and the original volume).</p>

---

## Post #9 by @JaredAmudeo (2024-08-01 00:22 UTC)

<p>Thank you very much for your help.</p>
<p>Best regards,</p>
<p>Jared.</p>

---
