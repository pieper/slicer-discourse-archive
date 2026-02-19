---
topic_id: 11474
title: "N4Itk Mri Bias Correction Standard Error The Number Of Contr"
date: 2020-05-09
url: https://discourse.slicer.org/t/11474
---

# N4ITK MRI Bias correction standard error:  The number of control points must be greater than the spline order.

**Topic ID**: 11474
**Date**: 2020-05-09
**URL**: https://discourse.slicer.org/t/n4itk-mri-bias-correction-standard-error-the-number-of-control-points-must-be-greater-than-the-spline-order/11474

---

## Post #1 by @Igcha (2020-05-09 07:41 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.10.2 r28257<br>
Expected behavior: N4ITK MRI Bias correction filtering on images<br>
Actual behavior:<br>
The N4ITK MRI Bias correction filter on .png Angio X ray images doesn’t work because of the following error message.<br>
I can’t find in 3D Slicer the parameter to set number of control points @ a number greater than the spline order of the The N4ITK MRI Bias correction filter.  where is it ?   Not on the The N4ITK MRI Bias correction filter parameters.  Where else ?<br>
Can someone help me ?</p>
<p>N4ITK MRI Bias correction standard error:</p>
<p>itk::ExceptionObject (000000E92A4FAF18)</p>
<p>Location: “unknown”</p>
<p>File: d:\d\s\slicer-4102-build\itk\modules\filtering\imagegrid\include\itkBSplineScatteredDataPointSetToImageFilter.hxx</p>
<p>Line: 250</p>
<p>Description: itk::ERROR: BSplineScatteredDataPointSetToImageFilter(00000245766E5520): The number of control points must be greater than the spline order.</p>

---

## Post #2 by @lassoan (2020-05-10 04:05 UTC)

<p>Do you mean you are trying to apply MRI bias correction on a 2D angio image? That might not work as the bias correction algorithm is specifically developed for 3D MR volumes.</p>
<p>What is the clinical problem that you are trying to solve?</p>
<p>If you just want to equalize the image intensity then you can use Simple Filters module’s AdaptiveHistogramEqualizationFilter.</p>

---

## Post #3 by @Igcha (2020-05-10 07:12 UTC)

<p>Yes, I tried to apply MRI N4 Bias correction filter to angio X-rays 2D coronary arteries images.  My goal is to have better results to diagnostic coronary artery disease (i.e. stenosis) with Deep Learning supervised CNN models.  I’ve good results on type artery classification but poor results on disease diagnostic and my DL network doesn’t converge.  Someone advise me to use N4 bias correction and I test it with Simple ITK N4 Bias correction Python algorithm and it works, but results of Deep Learning training algorithm with Bias correction filtered images were worth than with original images.  Then I tried with 3D Slicer to set different parameters trying to have better results.  Which filter do you advise me ? Simple Filters module’s AdaptiveHistogramEqualizationFilter.  According me the final aim of the filter without speaking of segmentation is to make the coronary artery tree more visible on the X-rays angiograms than the spine, ribs and tissues.</p>

---
