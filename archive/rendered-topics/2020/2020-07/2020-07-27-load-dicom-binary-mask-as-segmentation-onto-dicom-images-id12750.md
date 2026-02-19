---
topic_id: 12750
title: "Load Dicom Binary Mask As Segmentation Onto Dicom Images"
date: 2020-07-27
url: https://discourse.slicer.org/t/12750
---

# Load dicom binary mask as segmentation onto dicom images

**Topic ID**: 12750
**Date**: 2020-07-27
**URL**: https://discourse.slicer.org/t/load-dicom-binary-mask-as-segmentation-onto-dicom-images/12750

---

## Post #1 by @Nick555 (2020-07-27 20:12 UTC)

<p>I have a dicom CT series, and a binary mask series (with same number of slices as dicom series), with only the tumors having a value of 1 in the mask. So if the tumor is on slice 10, then only those pixels on slice 10 will have a value of 1, while all other pixels will be 0.</p>
<p>I would like to load the dicom CT images, and overlay the binary mask series on it (as a segmentation), and run the Radiomics module on it.</p>
<p>Can you please help me do that?</p>
<p>Operating system:Windows<br>
Slicer version:4.10.2<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2020-07-27 20:15 UTC)

<p>If the “mask series” is valid DICOM then Slicer should be able to read it the same way as it can load the CT. How the mask is stored? As a DICOM segmentation object or as a fake CT image?</p>
<p>I would recommend to use the most recent Slicer Preview release as it contains lots of fixes and improvements compared to Slicer-4.10.2.</p>

---

## Post #3 by @Nick555 (2020-07-27 20:31 UTC)

<p>Thank you for your response. The dicom segmentation file has the same dicom tags as the original image, except different dicom tags below</p>
<ul>
<li>SeriesDescription</li>
<li>SeriesNumber</li>
<li>SeriesInstanceUID</li>
</ul>
<p>I am able to read the two series. I just need to load the mask as segmentation to put onto the original CT image to run the Radiomics module.</p>

---

## Post #4 by @lassoan (2020-07-27 20:38 UTC)

<p>You can convert a “CT” to segmentation node by segmenting it with a threshold of 0.5. If you don’t want to use the Segment Editor then you can convert it to labelmap (Volumes module / Volume information / Convert to labelmap -&gt; Convert) then in Data module, right-click and choose “Convert labelmap to segmentation node”. You can also do this by a few lines of Python code.</p>
<p>In the long term, I would not recommend to use fake CT volumes for storing segmentation, but to use proper DICOM segmentation objects instead. Then they would be directly read as segmentation nodes and would be compatible with other DICOM-compliant software. If you don’t care about DICOM compliance then simply save the segmentation into a NRRD file, which can be loaded directly as segmentation node.</p>

---
