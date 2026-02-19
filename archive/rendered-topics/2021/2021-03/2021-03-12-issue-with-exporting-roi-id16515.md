---
topic_id: 16515
title: "Issue With Exporting Roi"
date: 2021-03-12
url: https://discourse.slicer.org/t/16515
---

# Issue with exporting ROI

**Topic ID**: 16515
**Date**: 2021-03-12
**URL**: https://discourse.slicer.org/t/issue-with-exporting-roi/16515

---

## Post #1 by @Charlotte (2021-03-12 22:15 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.11 and 4.13<br>
Expected behavior: ROI to match with CT image size<br>
Actual behavior: ROI is in wrong location and of the wrong size</p>
<p>Hi, I am working on a project which requires me to compare the ROIs created by different software and compare them on LifeX to perform radiomics analysis. The ROIs I have exported from CERR and MICE toolkit all match perfectly in LifeX, however that exported from Slicer is rotated and of the wrong size and resolution. I have used the following instructions to export the ROI in both Nifti and NRRD format: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html" class="inline-onebox" rel="noopener nofollow ugc">Segmentations — 3D Slicer documentation</a></p>
<p>The data set I am using is the following: <a href="https://github.com/theibsi/data_sets/tree/master/ibsi_1_validation/dicom/STS_001/CT" class="inline-onebox" rel="noopener nofollow ugc">data_sets/ibsi_1_validation/dicom/STS_001/CT at master · theibsi/data_sets · GitHub</a></p>
<p>As you can see, the original CT image dimensions are 198x202x59 whereas that of the mask exported from Slicer are 239x248x264. Are there any specific setting I could use to obtain a binary mask that has the same size as the CT matrix?</p>
<p>Many thanks for your help!</p>

---

## Post #2 by @lassoan (2021-03-14 04:23 UTC)

<p>A post was merged into an existing topic: <a href="/t/issue-with-mask-exported-from-slicer/16517">Issue with mask exported from Slicer </a></p>

---

## Post #3 by @lassoan (2021-03-14 04:23 UTC)



---
