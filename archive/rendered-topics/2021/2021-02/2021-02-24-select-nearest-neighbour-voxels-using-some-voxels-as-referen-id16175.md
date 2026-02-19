---
topic_id: 16175
title: "Select Nearest Neighbour Voxels Using Some Voxels As Referen"
date: 2021-02-24
url: https://discourse.slicer.org/t/16175
---

# Select nearest neighbour voxels using some voxels as reference?

**Topic ID**: 16175
**Date**: 2021-02-24
**URL**: https://discourse.slicer.org/t/select-nearest-neighbour-voxels-using-some-voxels-as-reference/16175

---

## Post #1 by @Saima (2021-02-24 08:05 UTC)

<p>Hi,<br>
Is there a possibility to select nearest neighbor voxels in an MRI based on the label-map. For-example I have the voxels based on some label. then I need to find nearest neighbour voxels that dont belong to voxels identified through label.</p>
<p>I found this<br>
import numpy<br>
volume = array(‘Volume’)<br>
label = array(‘Volume-label’)<br>
points  = numpy.where( label == 1 )  # or use another label number depending on what you segmented<br>
values  = volume[points] # this will be a list of the label values<br>
values.mean() # should match the mean value of LabelStatistics calculation as a double-check<br>
numpy.savetxt(‘values.txt’, values)</p>
<p>with above I can have voxel values defined by the label-map. how can I get voxel values in the nearest neighbor using these voxel values as reference.</p>

---

## Post #2 by @lassoan (2021-02-25 06:47 UTC)

<p>It is simpler to compute nearest neighbor from the closed surface representation of the segmentation.</p>

---

## Post #3 by @Saima (2021-02-25 07:01 UTC)

<p>Hi Andras,<br>
Any direction to help. Is there any thing available in slicer already.</p>
<p>Thank you</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #4 by @Saima (2021-02-25 07:59 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="16175">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>rom the closed surface representation o</p>
</blockquote>
</aside>
<p>Hi Andras,<br>
I investigated a little more into this. When I get closed surface some of the voxels in the segmentation are not included in the closed surface.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5f0ee5b773248f7b448959cc78a8d5ea0747d54a.jpeg" data-download-href="/uploads/short-url/dyVhb4XYMQS9b6haTu3Vtgcqrpw.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5f0ee5b773248f7b448959cc78a8d5ea0747d54a_2_355x500.jpeg" alt="image" data-base62-sha1="dyVhb4XYMQS9b6haTu3Vtgcqrpw" width="355" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5f0ee5b773248f7b448959cc78a8d5ea0747d54a_2_355x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5f0ee5b773248f7b448959cc78a8d5ea0747d54a.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5f0ee5b773248f7b448959cc78a8d5ea0747d54a.jpeg 2x" data-dominant-color="7F6959"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">503×708 61.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then I read this script online</p>
<h2><a name="p-55248-measure-distance-of-points-from-surface-1" class="anchor" href="#p-55248-measure-distance-of-points-from-surface-1" aria-label="Heading link"></a>Measure distance of points from surface</h2>
<p>But will this affect the accuracy of selection of nearest neighbor cells.</p>
<p>Is there a way to work at the voxels level.</p>
<p>Thanks you</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #5 by @lassoan (2021-02-25 13:15 UTC)

<p>You can turn off surface smoothing or do an exhaustive search for closest voxel in a small neighborhood of the closest mesh point.</p>

---

## Post #6 by @Saima (2021-02-26 03:17 UTC)

<p>Hi Andras,<br>
When I do not include surface smoothing still the results are attached here not include some of the voxels. How can I do the exhaustive search for closest voxels. Any relevant code example?</p>
<p>thank you</p>
<p>Regards,<br>
Saima Safdar</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26eaa623cf4666059c8c51cf3a3f57945be05884.png" alt="image" data-base62-sha1="5ygSndcWKk1yRI6UrHMGmJ8nvTe" width="534" height="397"></p>

---

## Post #7 by @lassoan (2021-02-26 03:50 UTC)

<aside class="quote no-group" data-username="Saima" data-post="6" data-topic="16175">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>When I do not include surface smoothing still the results are attached here not include some of the voxels.</p>
</blockquote>
</aside>
<p>The single voxel difference that you see is most likely not a real difference in 3D, just because a mesh is sliced differently than a labelmap. If a subvoxel error matters for you then it means that the binary labelmap’s voxel size is too large. In general, a voxel size should be 5-10x smaller than your error tolerance.</p>
<aside class="quote no-group" data-username="Saima" data-post="6" data-topic="16175">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>How can I do the exhaustive search for closest voxels. Any relevant code example?</p>
</blockquote>
</aside>
<p>You can use the examples in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository">script repository</a> for IJK voxel position from RAS position then you can use standard numpy indexing for retrieving a small neighborhood of voxels around that IJK position, and walk through all the voxels and fine the one that is non-zero and closest to the selected position.</p>

---

## Post #8 by @Saima (2021-02-26 05:10 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="7" data-topic="16175">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<aside class="quote no-group" data-username="Saima" data-post="6" data-topic="16175">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>voxels.</p>
</blockquote>
</aside>
<p>The single voxel difference that you see is most likely not a real difference in 3D, just because a mesh is sliced differently than a labelmap. If a subvoxel error matters for you then it means that the binary labelmap’s voxel size is too large. In general, a voxel size should be 5-10x smaller than your error tolerance.</p>
</blockquote>
</aside>
<p>Is there a way to change the voxel size in 3D Slicer? how can I change voxel size and remove any error that is happening.</p>

---

## Post #9 by @Saima (2021-02-26 05:38 UTC)

<p>Hi Andras,<br>
Any relevant code example to compute nearest neighbor from closed surface.</p>

---

## Post #10 by @lassoan (2021-02-26 12:56 UTC)

<p>I don’t think I can give further help with this. You should be able to find examples for iterating through elements of a 3D array, computing distance between two points, and finding minimum value in an iteration.</p>

---

## Post #11 by @Saima (2021-03-04 06:16 UTC)

<p>Hi Andras,<br>
Is there any code example to start with for computing nearest neighbor from closed surface representation.</p>
<p>" It is simpler to compute nearest neighbor from the closed surface representation of the segmentation"</p>

---

## Post #12 by @lassoan (2021-04-06 13:49 UTC)

<p>You can get the closed surface representation as a vtkPolyData and then find the closest point the same way as for vtkPolyData retrieved from model nodes (using VTK locator classes).</p>

---
