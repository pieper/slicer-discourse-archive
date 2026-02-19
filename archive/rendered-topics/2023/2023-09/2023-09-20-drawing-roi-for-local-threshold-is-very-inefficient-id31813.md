---
topic_id: 31813
title: "Drawing Roi For Local Threshold Is Very Inefficient"
date: 2023-09-20
url: https://discourse.slicer.org/t/31813
---

# Drawing ROI for local threshold is very inefficient?

**Topic ID**: 31813
**Date**: 2023-09-20
**URL**: https://discourse.slicer.org/t/drawing-roi-for-local-threshold-is-very-inefficient/31813

---

## Post #1 by @benalb (2023-09-20 20:22 UTC)

<p>I’m trying to adapt this methodology performed in AnalyzeDirect to Slicer3D.</p>
<p>(Video of methodology in supplementary data)<br>
<a>https://link.springer.com/article/10.1007/s00234-016-1720-z#Sec22:~:text=XLSX%2022%20kb)-,ESM%205,-(MOV%2013673%20kb</a></p>
<p>In this article (<a href="https://doi.org/10.1007/s00234-016-1720-z" class="inline-onebox" rel="noopener nofollow ugc">Software output from semi-automated planimetry can underestimate intracerebral haemorrhage and peri-haematomal oedema volumes by up to 41&nbsp;% | SpringerLink</a>), the author draws with a pen tool the ROI to restrict segmentation to an area, clicks on the scan to add a seed, and adjusts the upper threshold in HU units. As the upper limit is adjusted, more of the scan is segmented starting from the seed.</p>
<p>The ROI is very important as the boundary between edema and background (normal tissue) is not just based on contrast, but also requires judgement by comparison on the contralateral side. Similar intensities outside the ROI are not wanted in the segmentaton. Their method is slice by slice.</p>
<p>I tried using the tools in the markups tab to draw the ROI. Local threshold fills in 3D, but setting the ROI in 3D is very time consuming. The eraser tool has to be used a lot.</p>
<p>I’ve also tried level tracing, but I can’t see the intensity under the cursor in the data probe when hovering in the level tracing tool. This means that if I want to have a maximum HU unit that cannot be exceeded, I have to first create a segmentation with a brush, and then use it as a mask for segmentation.</p>
<p>The last solution I can think of is to paint another segmentation as a mask.</p>
<p>Perhaps the video that I linked is sort of something like active contouring in ITK Snap? Thresholding first, then growing from a bubble.</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2023-09-22 19:03 UTC)

<p>What you describe seems to be what “Grow from seeds” effect provides. You can limit the considered region by cropping the volume before starting segmentation, or during segmentation you can specify an intensity range or select an editable region. See detailed step-by-step neurosurgical planning tutorial <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Neurosurgical_Planning_Tutorial">here</a>.</p>

---

## Post #3 by @benalb (2023-09-24 05:28 UTC)

<p>Thanks. I can see how 3d slicer’s grow from seeds is slightly different (can’t see how changes in editable intensity range affects the segmentation in real time, as there is less focus on the edge boundary), but I can also see how it has the same functionality (the ‘background’ label acts as an ROI)</p>

---
