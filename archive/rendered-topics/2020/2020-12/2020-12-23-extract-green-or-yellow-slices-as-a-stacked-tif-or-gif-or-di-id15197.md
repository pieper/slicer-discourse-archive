---
topic_id: 15197
title: "Extract Green Or Yellow Slices As A Stacked Tif Or Gif Or Di"
date: 2020-12-23
url: https://discourse.slicer.org/t/15197
---

# Extract Green or Yellow slices as a stacked tif or gif or DICOM files

**Topic ID**: 15197
**Date**: 2020-12-23
**URL**: https://discourse.slicer.org/t/extract-green-or-yellow-slices-as-a-stacked-tif-or-gif-or-dicom-files/15197

---

## Post #1 by @qubalee (2020-12-23 12:58 UTC)

<p>Hi,</p>
<p>I am trying to export both green and yellow views (as separated files) from a 3D volume, but I could not do it. When I convert it to DICOM, I got it from the Red view only. Is there any one can help in this?</p>
<p>thanks in advance<br>
Abdullah</p>

---

## Post #2 by @qubalee (2020-12-23 14:29 UTC)

<p>Hi there,</p>
<p>I am facing an issue with extracting a stacked tif file. I would like to extract a stacked tif or gif or DICOM files from one view only or each view separately, i.e., G or Y, but I could not make it.</p>
<p>I’d appreciate any help from you.</p>
<p>Thanks</p>

---

## Post #3 by @lassoan (2020-12-23 15:37 UTC)

<p>If you export a 3D volume then it should not matter how the volume axes (IJK) are assigned to physical axis directions (RAS/LPS). What are you trying to achieve?</p>

---

## Post #4 by @qubalee (2020-12-23 16:43 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="15197">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>(IJK)</p>
</blockquote>
</aside>
<p>Thanks, Lassoan, for your response.<br>
We are studying the variation among different orientations, IJK. The issue is not about calculating the volume, but something else. Is there any way to do it in Slicer?</p>
<p>Thanks again<br>
Abdullah</p>

---

## Post #5 by @lassoan (2020-12-23 16:47 UTC)

<aside class="quote no-group" data-username="qubalee" data-post="4" data-topic="15197">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/qubalee/48/9314_2.png" class="avatar"> qubalee:</div>
<blockquote>
<p>The issue is not about calculating the volume, but something else. Is there any way to do it in Slicer?</p>
</blockquote>
</aside>
<p>Since in Slicer you can do almost everything that is possible in medical image computing, the answer is most likely “yes”. Of course I can only guess, because I don’t know what you would like to do.</p>
<p>If you need want to study the effect of voxel spacing then you can use “Resample scalar volume” module to resample the input volume with arbitrary spacing along each axis.</p>

---

## Post #6 by @qubalee (2020-12-23 16:55 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="15197">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you need want to study the effect of voxel spacing then you can use</p>
</blockquote>
</aside>
<p>Our study takes it slice by slice. So, we measure the area in 2D for each slice in each orientation.<br>
I don’t know yet how to export my files as a stacked tif or how to calculate the areas of each orientation in slicer.</p>

---

## Post #7 by @lassoan (2020-12-23 17:40 UTC)

<p>I assume you use Python for image segmentation on one slice at a time. For this, it does not matter what axes you chose as IJK because you can get the slices in any orientation, by numpy indexing. For example, you can get slices from the volume like this:</p>
<pre><code class="lang-python">sagittalSlice = voxels[sliceIndex,:,:]
coronalSlice = voxels[:,sliceIndex,:]
axialSlice = voxels[:,:,sliceIndex]
</code></pre>
<p>If you work with 3D data then you can probably get better results using networks that get the entire 3D data set. Check out <a href="https://monai.io/">MONAI</a>.</p>

---

## Post #8 by @qubalee (2020-12-23 17:43 UTC)

<p>Thanks, Lassoan.<br>
I will try it now.</p>

---

## Post #9 by @qubalee (2021-07-10 04:03 UTC)

<p>For the record, I solved this issue using screen capture, see below.</p>
<ul>
<li>Go to <em>Modules</em> &gt; <em>Utilities</em> &gt; <em>Screen Capture</em>.</li>
<li>Input; Change <em>Master view to Green</em> (Coronal) or Yellow (Sagittal).</li>
<li>Output; Select your prefered <em>output directory</em>
</li>
<li>Click <em>Capture</em>.</li>
</ul>

---
