---
topic_id: 4256
title: "Intersection Between Model And Volume To Select Voxels"
date: 2018-10-02
url: https://discourse.slicer.org/t/4256
---

# Intersection between model and volume to select voxels

**Topic ID**: 4256
**Date**: 2018-10-02
**URL**: https://discourse.slicer.org/t/intersection-between-model-and-volume-to-select-voxels/4256

---

## Post #1 by @Niels (2018-10-02 13:45 UTC)

<p>I have a generated a surface model by applying vtkMarchingCubes on a loaded volume. The next step I would like to perform is to identify which voxels intersect with the triangles that were generated. I was thinking of starting with iterating the vertices to see which voxels overlap and do some triangle intersect from there but I am not sure if that is the best method. Doe anybody know if there is a better way to select voxels that are inside, outside or on the contour of  a model? I am using python.</p>

---

## Post #2 by @cpinter (2018-10-02 13:49 UTC)

<p>What are you trying to achieve in general? I have the feeling that there should be an easier way for that in Slicer compared to low-level VTK programming.</p>

---

## Post #3 by @Niels (2018-10-02 13:58 UTC)

<p>Yes, you might be right. I would like to dilate the outer layer of the scan to replace this gradient-artifact in the scan with the color of the inside voxels. So only the replacing of this thin outer layer and leave the inside voxels untouched.</p>

---

## Post #4 by @Niels (2018-10-02 14:00 UTC)

<p>I found this Module: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/VolumeClip" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/VolumeClip</a></p>
<p>So my guess is that in slicer there must be a way to identify which voxels are inside a model?</p>

---

## Post #5 by @cpinter (2018-10-02 14:15 UTC)

<p>There is a complete infrastructure for this in the past few years called Segmentations. If you convert your model to a segmentation then set the reference volume to your volume in Segmentations module, then you can do all kinds of computations and editing.</p>
<p>How I’d do it:</p>
<ul>
<li>Use latest 4.9.0 nightly</li>
<li>Create new segmentation node in Segmentations module</li>
<li>In Representations section make Closed surface as master (because you want to have control over the geometry of the labelmap afterwards)</li>
<li>Import model in Import/Export section</li>
<li>In Representations section long-click Create and choose Advanced create</li>
<li>Click the only path in the top part</li>
<li>Click Specify geometry button in the bottom part</li>
<li>Select your volume</li>
</ul>
<p>Now you have a segmentation node which contains the labelmap representation of your model in the exact grid as your volume. Now you can do all kinds of things with it in the Segment Editor module (click yes when it asks if you want to change master to labelmap), such as dilation in the Margin effect. If you only need the dilated part then you can use Logical operators to copy the original segment, dilate the copy, and subtract the original from the dilated. You can calculate statistics in the Segment Statistics module.</p>

---

## Post #6 by @Niels (2018-10-02 14:44 UTC)

<p>Hi cpinter, thanks for the quick reply. I am not familiar with segmentations, I will try the steps you specify. If I understand correctly a segment model is created from the model that can be assigned to the volume to perform segment operations? In the end I would like to automate this process in a script and use the marchingcubes isovalue as a guide for automatically regenerating this segmentation.</p>

---

## Post #7 by @cpinter (2018-10-02 14:50 UTC)

<p>You can do the whole segmentation in Segment Editor, and then you don’t have to even start from a model. You can do all that from python.</p>
<p>Here’s some information about Segmentations:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Segmentations" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Modules/Segmentations</a><br>
And about driving Segment Editor from python:<br>
<a href="https://discourse.slicer.org/search?q=segment%20editor%20python">https://discourse.slicer.org/search?q=segment%20editor%20python</a> (this is just a discourse search, please use this resource, a lot of questions have been answered already)<br>
I think for your use case you can do the segmentation as a simple threshold, it gives you the same geometry as an isosurface (both are directly based on voxel intensity).</p>

---
