# How to threshold only one slice in the DICOM Module

**Topic ID**: 10602
**Date**: 2020-03-09
**URL**: https://discourse.slicer.org/t/how-to-threshold-only-one-slice-in-the-dicom-module/10602

---

## Post #1 by @Vincent_C (2020-03-09 19:42 UTC)

<p>Hi all,</p>
<p>I have loaded a 3D- CT scan into Slicer using the DICOM module. How can I apply thresholding to only one slice?</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2020-03-09 21:18 UTC)

<p>There are many ways to do it. What would you like to achieve?</p>

---

## Post #3 by @Vincent_C (2020-03-09 22:08 UTC)

<p>Hi Andras,</p>
<p>Thanks for the reply. I want to achieve accurate segmentation of muscle, SAT and VAT of the entire thoracolumbar region from T1 - L5. The method I was planning was to threshold 17 mid-vertebra slices and manually correcting them, then using the Fill between slice effect to propagate to the other slices and finally manually correcting them again. Is this a solid method to achieve the highest accuracy segmentation for a high resolution CT-volume? I am open to other suggestions :).</p>
<p>Thanks</p>

---

## Post #4 by @lassoan (2020-03-09 23:58 UTC)

<p>Manual correction typically takes much longer time than specifying a region from scratch. So, I would definitely not recommend to create an initial “segmentation” with simple thresholding.</p>
<p>Instead, I would recommend to try these options:</p>
<ul>
<li>Paint effect with appropriate “Editable intensity range”. You can find the correct threshold range in Threshold effect and then click “Use for masking”.</li>
<li>Draw effect, potentially with “Editable intensity range”.</li>
<li>Level tracing effect.</li>
</ul>
<p>You may try to pre-process the image to reduce noise and make regions more homogeneous. For example, try Anisotropic Diffusion filters (in Filtering / Denoising category), or various other filters in Simple Filters module.</p>

---

## Post #5 by @Vincent_C (2020-03-10 01:39 UTC)

<p>Great thanks for the suggestions! I still want to experiment thresholding at a single slice. You mentioned there are many ways to do this for a CT scan loaded using the DICOM module?</p>

---

## Post #6 by @lassoan (2020-03-10 01:46 UTC)

<p>The easiest to see how bad the result is if you use simple thresholding is to threshold the entire volume, using Threshold effect. If you really want to threshold only a handful of slices, then you can set editable intensity range in Threshold effect, click Use for masking, then use Paint effect with a huge brush (so that you can easily cover the entire slice with a single click or a short paintstroke).</p>

---

## Post #7 by @Vincent_C (2020-03-10 03:18 UTC)

<p>Hi Andras,</p>
<p>Your fast responses are always much appreciated! Thanks.</p>

---
