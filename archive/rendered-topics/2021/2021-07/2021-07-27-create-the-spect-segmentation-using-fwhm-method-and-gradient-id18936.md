---
topic_id: 18936
title: "Create The Spect Segmentation Using Fwhm Method And Gradient"
date: 2021-07-27
url: https://discourse.slicer.org/t/18936
---

# Create the SPECT segmentation using fwhm method and gradientweight function (Matlab)

**Topic ID**: 18936
**Date**: 2021-07-27
**URL**: https://discourse.slicer.org/t/create-the-spect-segmentation-using-fwhm-method-and-gradientweight-function-matlab/18936

---

## Post #1 by @akmal871026 (2021-07-27 02:56 UTC)

<p>Hi all,</p>
<p>Anyone can help me to develop one method for SPECT segmentation?</p>
<p>First, we have to find the distance boundary of the volume using fwhm method.</p>
<p>Second, we use gradientweight function (Matlab) to calculate the VOI of the volume?</p>
<p>Anyone can help me?</p>

---

## Post #2 by @lassoan (2021-08-03 17:53 UTC)

<p>You can implement a small Python script that measures these volumes fully automatically (or from manually specified seed points).</p>
<p>You can find examples in the script repository for <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-value-of-a-volume-at-specific-voxel-coordinates">accessing voxels of a volume</a>, <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-histogram-of-a-segmented-region">compute histogram of a segmented region</a>, etc.</p>
<p>You can get the image gradient by using <a href="https://vtk.org/doc/nightly/html/classvtkImageGradient.html">vtkImageGradient VTK filter</a>.</p>
<p>Let us know if you have any specific questions (how to get some data, how to compute something, etc.).</p>

---
