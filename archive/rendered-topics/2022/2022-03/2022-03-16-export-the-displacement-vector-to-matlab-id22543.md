---
topic_id: 22543
title: "Export The Displacement Vector To Matlab"
date: 2022-03-16
url: https://discourse.slicer.org/t/22543
---

# Export the displacement vector to matlab

**Topic ID**: 22543
**Date**: 2022-03-16
**URL**: https://discourse.slicer.org/t/export-the-displacement-vector-to-matlab/22543

---

## Post #1 by @dingyangyuan (2022-03-16 17:16 UTC)

<p>I want to export the output vector field to the MATLAB. I used the B spline registration in Plastimatch module, and saved the Output vector field DVF in nrrd.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf16cfc0297a7acea042b9a24d08f923d898b041.png" alt="image" data-base62-sha1="rgs4mkklnqP6uIhhDzOZcwu4oDL" width="442" height="98"><br>
Then I read the DVF.nrrd using nrrdread.m. I compared the vector field shown in the Transforms module with the result of the corresponding voxel obtained by the MATLAB. And the two vector fields were completely different. Not the difference between positive and negative signs. Can you give some advice on how to export the vector field to the MATLAB correctly?</p>

---

## Post #2 by @dingyangyuan (2022-03-16 02:24 UTC)

<p>Hi<br>
I am doing the same thing with you.  I want to register two 3D CT volumes using B spline registration in Plastimatch module and use the displacement vector field in MATLAB.<br>
The ‘Output vector field’ was saved as .nrrd format.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5aee723432b4e3f648f32057213346ff690d3990.png" alt="image" data-base62-sha1="cYpQ7VHrdO9geD0w7Kku8PdTIOc" width="377" height="72"><br>
Then I read the dvf.nrrd using the nrrdread, and got the resullt as follows.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a4bb34ddaa6d74a8630d0b529de7f30710ee8f8b.png" alt="image" data-base62-sha1="nvhonDuJFGNAnq7eHSYAFTdXA6L" width="600" height="109"></p>
<p>I want to check whether the vector field read in MATLAB is the same with the vector field shown in Transforms module.   And they were completely different.  Was your result right? What  unit is the exported nrrd file? mm or pixel?</p>

---

## Post #3 by @lassoan (2022-03-17 00:42 UTC)

<p>There are many things you need to pay close attention to:</p>
<ul>
<li>you need to take into account the grid origin, spacing, axis directions to look up the correct matrix index</li>
<li>the matrix index may be offset by 1 in MATLAB (MATLAB starts indexing from 1)</li>
<li>the order of indices may be inverted (i, j, k vs. k, j, i)</li>
<li>physical coordinates and displacements may be in LPS or RAS coordinate system</li>
</ul>
<p>Compared to Python and Python-wrapped toolkits (ITK, VTK, etc.) and applications (such as 3D Slicer) MATLAB is very limited when it comes to visualizing, processing, transforming 3D images. What is the rationale for trying to use MATLAB? Could you do your processing in Slicer’s Python environment instead? What is the overall goal of your project?</p>

---

## Post #4 by @dingyangyuan (2022-03-17 01:43 UTC)

<p>I want to use the vector field in matrad - an open source dose calculation for radiotherapy treatment planning. What is the unit of the output vector field, mm or pixel?</p>

---

## Post #5 by @lassoan (2022-03-17 02:50 UTC)

<aside class="quote no-group" data-username="dingyangyuan" data-post="4" data-topic="22543">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/7ba0ec/48.png" class="avatar"> dingyangyuan:</div>
<blockquote>
<p>What is the unit of the output vector field, mm or pixel?</p>
</blockquote>
</aside>
<p>Everything is in millimeter.</p>
<p>If matrad has trouble reading in standard displacement fields then you can apply the displacement to any images, contours, dose maps, etc. in Slicer and hopefully matrad at least can read those. Note that you can also use <a href="http://slicerrt.github.io/">SlicerRT</a> for deformations, dose accumulation, DVH computation, DVH comparison, RT plan visualization, etc. SlicerRT also has some basic dose computation engines, but if those are not sufficient then you can use matrad to compute the dose and to the rest of the analysis via GUI or Python scripting using SlicerRT.</p>

---

## Post #6 by @dingyangyuan (2022-03-17 03:44 UTC)

<p>Thank you for your quick reply！I think I still need to use matrad. I also have some questions.<br>
1 What is the difference between ‘Output B-spline transform’ and ‘Output vector field’?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/ae9b5f98656cdb337b7bebd03c88b04f623fa181.png" alt="image" data-base62-sha1="oUDXSOFs4V1ZXbSVTQ4CVZebp3X" width="399" height="71"><br>
2 Whether the calculated vector is backward mapping or forward mapping? Is the vector field a mapping from moving volume to fixed volume?<br>
3 The calculated vector field is in mm units. Is the saved nrrd file also in mm units? During the save process, is there a coordinate conversion?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0c0d0afdf7fa692d028b1ac05a30b12d9771334.png" alt="image" data-base62-sha1="pdD8DWOcemLhOdAfSreA75ECu9u" width="622" height="251"></p>
<p>4 When I read the nrrd file using nrrdread.m, I also obtain an ijkToLPSTransform matrix. is it used to transform pixel units (ijk coordinate system ) to mm uints (physical LPS coordinate system)?  Am I to understand that the data read by nrrdread.m is in pixel units?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b428e13eb0be98ffb8e38ed950f43e6b2e6d417.png" alt="image" data-base62-sha1="jRWXDaNPYmPBf54iUWvXILZOwjt" width="616" height="86"></p>

---

## Post #7 by @lassoan (2022-03-17 04:54 UTC)

<aside class="quote no-group" data-username="dingyangyuan" data-post="6" data-topic="22543">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/7ba0ec/48.png" class="avatar"> dingyangyuan:</div>
<blockquote>
<p>What is the difference between ‘Output B-spline transform’ and ‘Output vector field’?</p>
</blockquote>
</aside>
<p>B-spline transform contains B-spline coefficients, while the vector field contain displacement vectors.</p>
<aside class="quote no-group" data-username="dingyangyuan" data-post="6" data-topic="22543">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/7ba0ec/48.png" class="avatar"> dingyangyuan:</div>
<blockquote>
<p>Whether the calculated vector is backward mapping or forward mapping? Is the vector field a mapping from moving volume to fixed volume?</p>
</blockquote>
</aside>
<p>Image registration always computes vector from the fixed to the moving image. You can easily compute the inverse transform in Transforms module in Slicer (click “Invert” button then and then use Convert section to export to a new displacement field).</p>
<aside class="quote no-group" data-username="dingyangyuan" data-post="6" data-topic="22543">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/7ba0ec/48.png" class="avatar"> dingyangyuan:</div>
<blockquote>
<p>The calculated vector field is in mm units. Is the saved nrrd file also in mm units? During the save process, is there a coordinate conversion?</p>
</blockquote>
</aside>
<p>Physical coordinate system units is always millimeters, regardless of what file format is used.</p>
<aside class="quote no-group" data-username="dingyangyuan" data-post="6" data-topic="22543">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/7ba0ec/48.png" class="avatar"> dingyangyuan:</div>
<blockquote>
<p>When I read the nrrd file using nrrdread.m, I also obtain an ijkToLPSTransform matrix. is it used to transform pixel units (ijk coordinate system ) to mm uints (physical LPS coordinate system)? Am I to understand that the data read by nrrdread.m is in pixel units?</p>
</blockquote>
</aside>
<p>Everything is in physical units. You just need IJK to LPS transform to get the index of the matrix element where the displacement vector has to be read from.</p>

---

## Post #8 by @dingyangyuan (2022-03-17 07:06 UTC)

<p>I active the ‘dvf’ vector field (the corresponding nrrd file is read in matlab) in the Transforms module. The values shown in the ‘Displacement vector RAS’ is the vector field value not the B-spline coefficients, right? And what is the difference between ‘Transform to patient’ and ‘Transform from patient’? Thank you very much!</p>

---

## Post #9 by @lassoan (2022-08-04 06:22 UTC)

<p>Yes, “Displacement vector RAS” contains the actual displacement vector values. Transform to/from a coordinate system indicates the direction (“from” transform is the inverse of the “to” transform).</p>

---
