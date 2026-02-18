# Advice for (Semi-) Automated Segmentation of Neurovasculature

**Topic ID**: 22545
**Date**: 2022-03-16
**URL**: https://discourse.slicer.org/t/advice-for-semi-automated-segmentation-of-neurovasculature/22545

---

## Post #1 by @jdh (2022-03-16 17:52 UTC)

<p>Hello,</p>
<p>I have been using Slicer to segment the neurovasculature from MRI datasets of several patients. The focus is on the vessels of the circle of Willis, but I also need to include some of the smaller/darker peripheral vessels in the segmentation. My general approach has been a very manual one where I use a fairly conservative threshold and then use the segment editor tools to add in the missing vessels. As you can imagine, this can be very time consuming.</p>
<p>I am wondering which tools are recommended for a more automated approach for segmenting the vessels missed by the thresholding.</p>
<p>I have tried using the VMTK modules (Vesselness filter and Level Set Segmentation) in slicer v4.10, but I either get poor results or I crash my machine as the algorithms try to allocate my entire RAM. Have these tools been updated to be more resource friendly or is there anyway to estimate the require RAM (I currently have 16 GB on my machine, but an upgrade to 32 GB is possible).</p>
<p>Are the tools in the segment editor better for individually segmenting several branches? I could use the “fill between slices tool” to reduce the number of slices I need to work on, but my understanding is that this does not consider the image data when lofting the volume between the marked slices.</p>
<p>Any advice to help speed up my segmentation workflow would be greatly appreciated.</p>
<p>Thanks!<br>
JDH</p>

---

## Post #2 by @lassoan (2022-03-16 19:39 UTC)

<p>Difficulty of segmenting neurovasculature greatly depends on the image quality (voxel size and noise) and usage of contrast.</p>
<p>If you have high-resolution, low-noise images with and without contrast agent then segmentation becomes a trivial task (subtraction+thresholding) - see for example <a href="https://lassoan.github.io/SlicerSegmentationRecipes/VesselSegmentationBySubtraction/">this segmentation recipe</a>.</p>
<p>If you don’t have control over the acquired images (you cannot request improved image quality that would make the images easier to segment) then you can still make the segmentation much faster and accurate than simple threshold painting.</p>
<p>For example, you can speed up your segmentation by using “Grow from seeds” effect. This effect takes into account the “Editable intensity range”, so if you set that correctly then you just need to keep painting “vessel” and “non-vessel” seeds until all the vessels of interest are segmented.</p>
<p>You could also train neural networks to segment vessels or at least enhance their visibility before segmentation, but investing into creating training data and tuning networks probably only pays off if you need to segment at hundreds of data sets.</p>

---
