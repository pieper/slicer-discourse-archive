# Fuse and register 2 MR Sequences covering different anatomical regions

**Topic ID**: 27686
**Date**: 2023-02-07
**URL**: https://discourse.slicer.org/t/fuse-and-register-2-mr-sequences-covering-different-anatomical-regions/27686

---

## Post #1 by @Tatyana_Ivanovskaya (2023-02-07 19:56 UTC)

<p>Operating system: Ubuntu 20.04<br>
Slicer version: 5.2.1</p>
<p>Dear All,<br>
i have 2 MR T1-weighted sequences from the same patient. One sequence is 1x1x1 mm^3 head scan, the other is a neck scan with a  resolution 0.78x0.78x4.8 mm^3.<br>
I need to get an image, where the 2 above sequences are resampled to the same resolution and stitched together with the correspondent regions to be registered, if possible.<br>
The resampling part is pretty clear, but I am a bit lost how to proceed next.</p>
<p>The goal behind the whole process is to allow the user mark certain landmark points and perform some measurements in the combined image.<br>
Thank you!</p>

---

## Post #2 by @lassoan (2023-02-08 20:49 UTC)

<p>First you need to register the two images. If there is sufficiently large overlap then you can use automatic image-based registration (SlicerElastix or SlicerANTs), you just need to crop both images to the region that overlap. If automatic registration is not robust enough then you can use landmark registration based on manually defined landmarks.</p>
<p>After the images are in correct position, you can use <a href="https://github.com/PerkLab/SlicerSandbox#stitch-volumes">Stitch volumes</a> module in Sandbox extension to merge them.</p>

---

## Post #3 by @Tatyana_Ivanovskaya (2023-02-08 22:04 UTC)

<p>Thank you!<br>
I have a question about the crop, since i am still missing something.<br>
Let’s say, i crop the image1 to crop1 and image2 to crop2, then the crops 1 and 2 are registered.<br>
How can i then add the rest of image1 and image2?</p>

---

## Post #4 by @lassoan (2023-02-08 22:32 UTC)

<p>Registration computes a transform that aligns the moving image to the fixed image. You can compute this transform from a part of the image and then apply the transform to the entire image.</p>

---

## Post #5 by @Tatyana_Ivanovskaya (2023-02-11 09:24 UTC)

<p>Thank you for the explanation!</p>
<p>How big should be the overlap and the size of the crop region? Is there some rule of thumb?</p>

---
