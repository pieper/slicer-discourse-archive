---
topic_id: 31936
title: "Strange Memory Leak Related With Volumenode And Segmentation"
date: 2023-09-27
url: https://discourse.slicer.org/t/31936
---

# Strange Memory leak related with volumeNode and segmentationNode

**Topic ID**: 31936
**Date**: 2023-09-27
**URL**: https://discourse.slicer.org/t/strange-memory-leak-related-with-volumenode-and-segmentationnode/31936

---

## Post #1 by @StephenLeePeng (2023-09-27 15:49 UTC)

<p>Environment: Slicer 4.13, Linux Ubuntu 20.04.</p>
<p>Background:<br>
Recently, I worked with a project, need to load some nii.gz file, vtp file.<br>
nii.gz file is loaded as vtkMRMLScalarVolumeNode, as the vtp file is loaded by Model, then transform to vtkSegmentationNode.</p>
<p>nii.gz file was generated from a series dcm files by simpleITK, which shape is: 512x512x700, about 350MB.<br>
vtp files was segmented from volume, every vtp file is small part of volume.</p>
<p>Firstly, Iily, I load vtp file as segmentationNode, every vtp file cause memory usage increased 15MB ~ 45MB, the memory is decided by the long and short diameter of segment.<br>
Then I will load another nii.gz file, which is the same patient dcm series, to compare two dcm series change, to help doctor exam the patient.<br>
Also, I will load some vtp files segmented from latter nii.gz file.<br>
The layout will changed at the same time, from classic FourUp layout to customed two group layout, every group has a 3d view and a slice view.</p>
<p>I will switch between two layout frequently. From FourUp layout to customed layout, or customed layout to FourUp layout.<br>
So, I need frequently RemoveNode or clear Scene, then Load nii.gz and vtp file again.</p>
<p>To my confuse, when I Remove the volumeNode, and related displayNode and storageNode, Remove segmentationNode, and clear Scene. And I set the variables to None or empty dict, but the memory usage will not decrease, or decrease only a little, less than loaded memory usage.</p>
<p>Because the memory usage can not decreased to one patient series consumption, So If I reload another series again, the memory will continue to grow up. Finally, the all memory usage will up to<br>
4 ~ 5GB.</p>
<p>And I have read some related topics, and have checked the codes.<br>
There have no Factory method, such as CreateDefaultStorageNode.</p>
<p>Some Clue:<br>
I look the Node Information, and see the volumeNode has 1 reference Count, but the vtkImageData has about 14 reference count.<br>
So I want to know, how I can watch the refercece count from, or is this reason caused the memory leak when I RemoveNode?<br>
How can clean the memry fully or most percent when I RemoveNode and Clear Scene.<br>
<a class="mention" href="/u/lassoan">@lassoan</a>  <a class="mention" href="/u/pieper">@pieper</a></p>
<p>One more question.<br>
The base memory consuption of Slicer app is 700MB above. How can I decrease this basic memory consuption to decrease the highest memory usage of my app.</p>
<p>Any advice will be appreciated.</p>

---

## Post #2 by @lassoan (2023-09-27 16:55 UTC)

<p>The memory “used” by a process may not be decreased immediately if you have enough RAM and no other process needs it. So, what you see may or may not be an actual memory leak.</p>
<p>Can you provide a script that we can easily run that reproduces infinitely growing memory usage? (download some sample data, load it, add a segmentation, close scene, etc. - in a loop)</p>

---
