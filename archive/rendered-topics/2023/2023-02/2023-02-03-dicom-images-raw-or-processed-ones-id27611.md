# DICOM images, raw or processed ones

**Topic ID**: 27611
**Date**: 2023-02-03
**URL**: https://discourse.slicer.org/t/dicom-images-raw-or-processed-ones/27611

---

## Post #1 by @Mahsa1 (2023-02-03 09:46 UTC)

<p>Hi,<br>
I have requested the CT-scan (DICOM format) images from the clinic. They asked me if I need the raw images or processed ones. Could you please tell me which type of images are needed to import 3D Slicer?</p>

---

## Post #2 by @lassoan (2023-02-03 09:52 UTC)

<p>Processing usually means that the image is resampled at lower resolution along 3 axes. This processing is done to reduce data size and make image reviewing more convenient in 2D image viewers, but it may remove some details from the image and prevent high-resolution 3D reconstruction.</p>
<p>Since Slicer is a 3D image viewer, this lossy post-processing operation is not necessary. You can expect to get higher quality images if you <strong>ask for the raw images</strong>.</p>

---

## Post #3 by @pieper (2023-02-03 10:01 UTC)

<p>Sometimes “raw” may refer to the original projection images, which is not what Slicer works with, so be sure to get the reconstructed slice images from the CT, which are typically the “raw” data as <a class="mention" href="/u/lassoan">@lassoan</a> describes.  You don’t want “processed” if this means pre-computed derived images.  Read up on CT on wikipedia or elsewhere if this is still unclear to you.</p>

---

## Post #4 by @lassoan (2023-02-03 10:20 UTC)

<p>Yes, it is true that for cone-beam CT (that is used for most dental 3D imaging and some intra-operative imaging), the raw image may mean the original X-ray projection images, which contain the most details but they are not viewable in 3D (they need to be reconstructed with complex computational methods that Slicer does not have). In this case, just to be safe, ask for both the raw and processed images.</p>
<p>Most diagnostic CTs are acquired on multi-slice CT scanners, in which raw acquisition data is not image, so in this case raw <em>image</em> may only mean the high-resolution reconstructed image slices that Slicer can read. Since raw/original data is often deleted soon after acquisition, in this case the safest bet is to ask for the raw images as soon as you can and then check if it loads correctly in Slicer. If everything looks good then you don’t need the processed images. If you have trouble viewing the data in Slicer and you cannot resolve the issues by asking help on this forum then you may ask for the processed images as well.</p>

---

## Post #5 by @Mahsa1 (2023-02-04 22:57 UTC)

<p>Thanks a lot for the explanation and your help.</p>

---

## Post #6 by @Mahsa1 (2023-02-04 22:58 UTC)

<p>thank you for your reply and clarification.</p>

---
