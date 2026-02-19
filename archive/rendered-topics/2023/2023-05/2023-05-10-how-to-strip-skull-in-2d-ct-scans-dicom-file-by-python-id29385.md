---
topic_id: 29385
title: "How To Strip Skull In 2D Ct Scans Dicom File By Python"
date: 2023-05-10
url: https://discourse.slicer.org/t/29385
---

# How to strip skull in 2D CT scans dicom file by python ?

**Topic ID**: 29385
**Date**: 2023-05-10
**URL**: https://discourse.slicer.org/t/how-to-strip-skull-in-2d-ct-scans-dicom-file-by-python/29385

---

## Post #1 by @ShangWeiKuo (2023-05-10 00:44 UTC)

<p>Hello.</p>
<p>I’ve installed itk-skullstripping by using <strong>pip install itk-skullstripping</strong>.</p>
<p>However. I have no idea the methods to use this package to strip skull in python.</p>
<p>My file is 2D CT scans and in the format of dicom.</p>
<p>You help is appreciated in advance.</p>

---

## Post #2 by @lassoan (2023-05-10 00:55 UTC)

<p>Skull stripping usually refers to removing everything outside the brain in MRI images. Probably itk-skullstripping performs this operation. In CT images the problem is completely different, much easier, as the skull can be segmented by simple global thresholding.</p>
<p>You can find a fully automatic method (you need to run automatic steps, which can be easilty automated) for 3D. The problem is harder to implement in 2D and CT image acquisitions are very rarely limited to a single slice, but if needed then you could develop a similar method (segment the skull, close the gaps, and extract the largest cavity).</p>

---
