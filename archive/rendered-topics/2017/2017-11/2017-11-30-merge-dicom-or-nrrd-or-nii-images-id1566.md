# Merge dicom or nrrd or nii images

**Topic ID**: 1566
**Date**: 2017-11-30
**URL**: https://discourse.slicer.org/t/merge-dicom-or-nrrd-or-nii-images/1566

---

## Post #1 by @Daniel_Frenzel (2017-11-30 16:46 UTC)

<p>I want to merge sub-MRI images of a patient to one bigger file.<br>
I noticed that neither MITK nor ITK-Snap are suitable to merge images.<br>
C3d also fails because the sub-images have different sizes.<br>
Is it possible to merge MRI images anyhow?</p>
<p>Operating system: Windows<br>
Slicer version:4.8</p>

---

## Post #2 by @lassoan (2017-11-30 17:11 UTC)

<p>It takes a couple of steps but it is certainly possible.</p>
<ul>
<li>First you need to create an image that is large enough to contain the merged image. To achieve this, create a large enough ROI that contains all the images and use <code>Crop Volume</code> module grow the first image to the size of this ROI (you need to enable <code>Interpolated cropping</code> to allow an image to grow beyond its original size).</li>
<li>You can merge these images by simply adding them using Add scalar volumes module. If the images overlap then you can blank out overlapping region in one of the image using Segment <code>Editor module</code>'s <code>Mask Volume</code> effect (available in SegmentEditorExtraEffects extension).</li>
</ul>
<p>Most likely you’ll see seams at the boundary of the two image. You can reduce that by image registration (if there is enough image overlap; using SlicerElastix extension), but for a seamless image you need to blending with gradually changing weight (alpha channel). To get this seamless image, create a binary mask by thresholding (Threshold scalar volume module) then smooth it (Gaussian blur image filter). You can then write a few-line Python script that appends alpha channel to your scalar volume and blends the images (using vtkImageBlend and (using vtkImageAppend filter). It may sound complicated but all these steps can all be done fully automatically by a few ten lines of Python script.</p>

---

## Post #3 by @Daniel_Frenzel (2017-12-01 08:54 UTC)

<p>I haven’t used slicer 3D before, because I used MITK. I was just reading that slicer may have the possibility to do so. However, I am not sure where to define ROIs in 4.8. Using google sends me to a version 3 documentation.</p>

---

## Post #4 by @lassoan (2017-12-01 12:20 UTC)

<p>See for example this post: <a href="https://discourse.slicer.org/t/set-target-region-for-image-resampling/894/2?u=lassoan">Set target region for image resampling</a></p>

---

## Post #6 by @brhoom (2020-02-26 08:00 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> if this is still not available, I think I will try to make an extension for this. I may need this feature in my work.</p>
<p>Here is the idea:</p>
<ol>
<li>get the size, spacing, and origin, datatype of the input images.
<ul>
<li>we create a copy of the high-quality image and resample it to the second less quality image.</li>
<li>or we do the opposite, this could be user input.</li>
</ul>
</li>
<li>create a new large image using information from step 1</li>
<li>add the resampled image and the second image to the larger image.
<ul>
<li>this should use a modified version of add scalar e.g. new image(x,y,z) = max(image1(x,y,z),image2(x,y,z))</li>
</ul>
</li>
</ol>

---

## Post #7 by @lassoan (2020-02-26 12:25 UTC)

<p>Sounds good! Use latest Slicer Preview Release and “scripteddesigner” module template in Extension Wizard.</p>

---

## Post #8 by @thomshaw92 (2021-05-14 01:21 UTC)

<p>Hey <a class="mention" href="/u/brhoom">@brhoom</a>  did you ever complete this?<br>
Would be great to be able to use it (i have 5 slabs of the same participant that need to be stitched together) <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #9 by @doc-xie (2021-10-26 01:48 UTC)

<p>Hi Lassoan,<br>
I have merged the two volumes with Crop Volume-SegmentEditor-Add scalar Volumes modules with your advice. After the two volumes of the same patient were combined together, the result had different HU in bone or brain tissue.<br>
What the problem about this? Is there any error in the steps?<br>
Thanks!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe6931856a5a64311a148d818c381acafc65a9b8.png" data-download-href="/uploads/short-url/AiCEvGv6ui43GQrevvzv3QGuhcs.png?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe6931856a5a64311a148d818c381acafc65a9b8_2_363x500.png" alt="Screenshot" data-base62-sha1="AiCEvGv6ui43GQrevvzv3QGuhcs" width="363" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe6931856a5a64311a148d818c381acafc65a9b8_2_363x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe6931856a5a64311a148d818c381acafc65a9b8_2_544x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe6931856a5a64311a148d818c381acafc65a9b8.png 2x" data-dominant-color="2C2C2C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">652×896 49 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @lassoan (2021-10-26 03:29 UTC)

<p>Do you have different intensity values in the combined volume than in the original volumes?</p>

---

## Post #11 by @doc-xie (2021-10-26 06:46 UTC)

<p>Hi Lassoan,<br>
The scalar range of one volume is -1024~1947 and the other is -1024~3071. Before combination, the Window/Level of them were all set to CT-brain in Volume module. But the superior part and the inferior part were shown in different intensity(superior in CT- brain, inferior in CT-bone).<br>
Thanks,<br>
Dr.Xie</p>

---

## Post #12 by @doc-xie (2021-10-28 01:08 UTC)

<p>Hi Lassoan,<br>
I have solved the issue with Crop Volumes and Add Scalar Volumes module.  Maybe the problem about the different intensity is the improper size of the ROI.<br>
Thanks,<br>
Dr.Xie</p>

---

## Post #13 by @lassoan (2022-10-20 15:10 UTC)

<p>Just in case somebody comes across this topic now: <a class="mention" href="/u/mikebind">@mikebind</a> recently contributed the <a href="https://github.com/PerkLab/SlicerSandbox#stitch-volumes">Stitch Volumes module</a> for stitching multiple volumes into one. It is available in Sandbox extension.</p>

---
