---
topic_id: 11482
title: "Multiple Voi In Pyradiomics"
date: 2020-05-10
url: https://discourse.slicer.org/t/11482
---

# Multiple VOI in pyradiomics

**Topic ID**: 11482
**Date**: 2020-05-10
**URL**: https://discourse.slicer.org/t/multiple-voi-in-pyradiomics/11482

---

## Post #1 by @codecrazer (2020-05-10 08:44 UTC)

<p>If there were multiple VOIs and the pipeline extraction were used, but only Image and Mask were specified. The label column were not used. What will happen?</p>

---

## Post #2 by @JoostJM (2020-05-14 05:12 UTC)

<p>Then the default settings take effect: label with value 1, or first segment is used to calculate features.</p>

---

## Post #3 by @codecrazer (2020-05-14 05:28 UTC)

<p>It there any way to check how many segmentation in the nrrd file? I have a multiple ROI nrrd, and I delete all other segmentation except one, could I check if there is only one segmentation in the file by code? Thanks for your help!</p>

---

## Post #4 by @JoostJM (2020-05-23 14:15 UTC)

<p>If it’s a segmentation generated in Slicer then yes, quite easy:</p>
<pre><code class="lang-auto">import SimpleITK as sitk
ma = sitk.ReadImage('path/to/segmentation.seg.nrrd')
n_seg = ma.GetNumberOfComponentsPerPixel()
</code></pre>

---
