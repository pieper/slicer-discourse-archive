---
topic_id: 7739
title: "Obtain Voxels Coordinate Of An Image"
date: 2019-07-24
url: https://discourse.slicer.org/t/7739
---

# Obtain voxels coordinate of an image

**Topic ID**: 7739
**Date**: 2019-07-24
**URL**: https://discourse.slicer.org/t/obtain-voxels-coordinate-of-an-image/7739

---

## Post #1 by @Mohsen_Taheri (2019-07-24 10:23 UTC)

<p>Hi,</p>
<p>I used 3d slicer to segment a part of a brain image (from a *.nrrd file) and I need to obtain the the voxel coordinates of the segmentation. Actually I need the coordinates of all the inner and boundary voxels as a list like {[x1,y1,z1],…,[xn,yn,zn]} and the order of the coordinates is not important.<br>
I appreciate if any one could help me.</p>

---

## Post #2 by @lassoan (2019-07-24 13:21 UTC)

<p>You can export the segmentation as labelmap volume and then voxels as a numpy array using <code>slicer.util.arrayFromVolume</code>. If you need voxel IJK coordinates then you can use this <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_volume_voxel_coordinates_from_markup_fiducial_RAS_coordinates" rel="nofollow noopener">example</a>.</p>
<p>Note that storing a segmentation by listing coordinates of all its points is an extremely inefficient representation to read, write, and process. Are you sure this is what you need? What do you plan to do with the coordinate list?</p>

---

## Post #3 by @Mohsen_Taheri (2019-07-24 15:50 UTC)

<p>Thanks for the quick reply,<br>
As a matter of fact I need voxelized visualization and in addition I need to use the norm distance between different voxels for some data analysis purpose, for these reasons I considered to have a list of coordinate so I can find for example the mean point of the voxels and etc.</p>

---

## Post #4 by @lassoan (2019-07-24 16:23 UTC)

<p>Unless you have very sparse data (e.g., few ten points in a grid containing millions of points), computations can be implemented much more efficiently if points are represented in a rectilinear grid rather than as a list of random coordinates. Computing center of gravity, distance map, Hausdorff distance, etc. are all available for labelmap representation and you don’t even need to think about implementing, testing, and maintaining them.</p>

---

## Post #5 by @Mohsen_Taheri (2019-07-24 17:01 UTC)

<p>Let me be more precise, imagine I have a segmentation and I want to select for example 5 specific points (they are not on the boundary) from the segmentation and then find the mean value of them (call it M), after that I want to measure the distance of all the segmentation’s voxels to the point M<br>
the questions are</p>
<ol>
<li>How to find the coordinates of the 5 points</li>
<li>How to find the coordinates of the segmentation’s voxels</li>
</ol>

---

## Post #6 by @lassoan (2019-07-24 20:09 UTC)

<aside class="quote no-group" data-username="Mohsen_Taheri" data-post="5" data-topic="7739">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mohsen_taheri/48/4108_2.png" class="avatar"> Mohsen_Taheri:</div>
<blockquote>
<p>How to find the coordinates of the 5 points</p>
</blockquote>
</aside>
<p>You can specify points using markups and use this <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_volume_voxel_coordinates_from_markup_fiducial_RAS_coordinates">script to get IJK coordinates</a>.</p>
<aside class="quote no-group" data-username="Mohsen_Taheri" data-post="5" data-topic="7739">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mohsen_taheri/48/4108_2.png" class="avatar"> Mohsen_Taheri:</div>
<blockquote>
<p>How to find the coordinates of the segmentation’s voxels</p>
</blockquote>
</aside>
<p>You can export all segments to a merged labelmap and use the script referenced above. Or, slightly modify the script to use segmentation node instead of volume node (the difference is that you need to retrieve VTK image data from the segmentation object stored in the segmentation node; instead of getting it from a volume node).</p>

---

## Post #7 by @Mohsen_Taheri (2019-07-24 20:27 UTC)

<p>Thank you Andras that was really Helpful <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=9" title=":pray:" class="emoji" alt=":pray:"></p>

---
