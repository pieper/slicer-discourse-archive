---
topic_id: 2871
title: "Import Volume By Projections"
date: 2018-05-22
url: https://discourse.slicer.org/t/2871
---

# Import volume by projections

**Topic ID**: 2871
**Date**: 2018-05-22
**URL**: https://discourse.slicer.org/t/import-volume-by-projections/2871

---

## Post #1 by @Svensen7 (2018-05-22 11:35 UTC)

<p>I have three dcm files for each projection.<br>
Is it a way to open them together ? Because Slicer loads only one file, rather then three.</p>

---

## Post #2 by @lassoan (2018-05-22 11:39 UTC)

<p>You can load them one by one and select the axial, sagittal, coronal slice in the corresponding slide views. If planes are oblique then you may need to click “Rotate to volume plane” button in the slice view controller.</p>

---

## Post #3 by @Svensen7 (2018-05-22 12:33 UTC)

<p>Thanks, I could load them together for visualization purposes, however to conduct segmentation I should specify the master volume.<br>
Slicer shows me that I have three independent volumes, rather than one…</p>

---

## Post #4 by @lassoan (2018-05-22 13:28 UTC)

<p>3 orthogonal slices is very sparse data for creating a 3D segmentation but there are some tools in 3D Slicer that can help.</p>
<p>First of all, you need to create a master volume that is large enough to contain your final segmentation result. You can use Crop volume module to create a new volume based on an existing single-slice 3D volume, just by making the region of interest box large enough.</p>
<p>If you have projection images, you can create a 3D model by using Scissors effect. On the first projection you use “Fill inside” mode then on all other slices you use “Erase outside”. We used this to reconstruct breast tumors from a few X-ray projections. It did not produce accurate segmentation, but it showed very nicely how limited amount of information is in these few projections.</p>
<p>You may also try “Surface cut” effect (provided by SegmentEditorExtraEffects extension). This allows you to create 3D segmentation by marking points on arbitrarily positioned 2D slices. We use this very successfully to create breast tumor models from tracked free-hand ultrasound images.</p>

---

## Post #5 by @Svensen7 (2018-05-23 05:22 UTC)

<p>Maybe I’ve explained it a little bit unclear…<br>
Yes, I have three dcm files, however each dcm file contains a SERIES of slices.<br>
So each file contains all cross sections for corresponding projection.</p>
<p>So the question now is how to combine these series into the one master volume.</p>

---

## Post #6 by @lassoan (2018-05-23 05:39 UTC)

<p>OK, so you actually have cross-sectional images. Not projections. I guess you have those kind of volumes where you have high-resolution slices with huge gaps between them (spacing between slices is a magnitude larger than pixel spacing within the slice).</p>
<p>Unfortunately, it is a very difficult problem to create high-resolution data from these sparse slices, since in general you have no way of knowing what is between slices. If you have a priori information about the image content then you may be able to reconstruct super-resolution images, but I am not aware of such algorithms in Slicer (or in libraries that Slicer includes). For a similar question, somebody recommended <a href="https://github.com/gift-surg/NiftyMIC">NiftyMIC</a> toolkit.</p>

---

## Post #7 by @Svensen7 (2018-05-24 06:06 UTC)

<p>Thanks. the actual series are here: <a href="https://yadi.sk/d/o_wg3RoP3WSmA8" rel="nofollow noopener">https://yadi.sk/d/o_wg3RoP3WSmA8</a><br>
It seems that the gaps are not so big…<br>
What do you think, could the volume be reconstructed from these series ?</p>

---

## Post #8 by @lassoan (2018-05-24 19:27 UTC)

<p>These images are exported incorrectly, as screenshots. It has many disadvantages compared to the actual CT scan: the image has only 256 gray levels instead of thousands, so the contrast is very low; there are burnt-in text annotations, which make part of your image unusable; pixel size and other metadata is missing from the files, etc. Therefore, I would recommend to export the original volume instead of screenshots.</p>
<p>You can still do some things with this low-quality data set. You can estimate voxel size and enter it in Volumes module to make fix image distortion:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4eca9323f9ec0cf600796d5e6ac736107e412e50.png" data-download-href="/uploads/short-url/bf1fWq2fAzSNIivWnFKCzYlYIwM.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4eca9323f9ec0cf600796d5e6ac736107e412e50_2_690x373.png" alt="image" data-base62-sha1="bf1fWq2fAzSNIivWnFKCzYlYIwM" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4eca9323f9ec0cf600796d5e6ac736107e412e50_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4eca9323f9ec0cf600796d5e6ac736107e412e50_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4eca9323f9ec0cf600796d5e6ac736107e412e50_2_1380x746.png 2x" data-dominant-color="7B7A81"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 239 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You have to convert the color image to grayscale, using “Vector to Scalar volume” module. You can then visualize the converted volume using volume rendering:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da9e2ad1a040a8c90a5cd503386b0ca02b146a97.jpeg" data-download-href="/uploads/short-url/vbYXxAMaNodaFuQU2ayGDBkUNBZ.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/da9e2ad1a040a8c90a5cd503386b0ca02b146a97_2_690x373.jpg" alt="image" data-base62-sha1="vbYXxAMaNodaFuQU2ayGDBkUNBZ" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/da9e2ad1a040a8c90a5cd503386b0ca02b146a97_2_690x373.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/da9e2ad1a040a8c90a5cd503386b0ca02b146a97_2_1035x559.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/da9e2ad1a040a8c90a5cd503386b0ca02b146a97_2_1380x746.jpg 2x" data-dominant-color="8E8D90"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 440 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
