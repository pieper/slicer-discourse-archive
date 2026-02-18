# Generating 3D segmentation from MR or CT images

**Topic ID**: 4604
**Date**: 2018-10-31
**URL**: https://discourse.slicer.org/t/generating-3d-segmentation-from-mr-or-ct-images/4604

---

## Post #1 by @Mohammed_Alahmari (2018-10-31 14:03 UTC)

<p>Operating system:Windows<br>
Slicer version:4.8.1<br>
Expected behavior:<br>
Actual behavior:<br>
Hi there, I’m a beginner and want to use the slicer to measure the volumes of chordoma and vestibular schwannoma before and after radiotherapy. can I load a series of MR or CT images (axial, sagittal or coronal) having not too many slides, let’s say around 50 slides and generate a 3D volume segmentation? because when I loaded the axial series of my MR images with around 50 slides, it appeared clear in the red slice scene and the yellow and green scene were so blurred not like the sample data available in the slicer. can I still generate a 3D segmentation for a tumour if this is the data I have?</p>

---

## Post #2 by @lassoan (2018-10-31 14:11 UTC)

<p>Although you will certainly miss details due to large distance between slices, you can still create 3D Segmentation. For improved image quality, use Slicer-4.10 and specify <em>isotropic spacing</em> for your segmentation as shown below:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/70d6417d79d6afaa2326ec4ce1c0e0d25b2a859d.png" data-download-href="/uploads/short-url/g6cw5V7cafoMy9iaq4RG9FOzkSh.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/70d6417d79d6afaa2326ec4ce1c0e0d25b2a859d.png" alt="image" data-base62-sha1="g6cw5V7cafoMy9iaq4RG9FOzkSh" width="523" height="500" data-dominant-color="F1EDEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">703×672 72.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @Mohammed_Alahmari (2018-10-31 16:02 UTC)

<p>Thanks Andras for your quick response and much appreciated!</p>
<p>Best regards</p>
<p>Mohammed</p>

---

## Post #4 by @lassoan (2018-12-19 21:07 UTC)

<p>3 posts were merged into an existing topic: <a href="/t/manual-segmentation/5149/2">Manual segmentation </a></p>

---
