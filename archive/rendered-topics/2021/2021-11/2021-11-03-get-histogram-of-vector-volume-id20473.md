---
topic_id: 20473
title: "Get Histogram Of Vector Volume"
date: 2021-11-03
url: https://discourse.slicer.org/t/20473
---

# Get histogram of vector volume

**Topic ID**: 20473
**Date**: 2021-11-03
**URL**: https://discourse.slicer.org/t/get-histogram-of-vector-volume/20473

---

## Post #1 by @toyama (2021-11-03 14:19 UTC)

<p>I tried to get the histogram of the R, A, and S axes of the DVF of the contour thing by modifying the code that you taught me before.</p><aside class="quote" data-post="1" data-topic="19008">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/82dd89/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/negative-values-in-dvf-histogram/19008">Negative Values in DVF Histogram</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    We are looking for a histogram of the DVF. 
The DVF should not have any negative values, but when I calculated the histogram from the DVF created by the transform module, it took negative values. 
What do these negative values mean? 
Also, I am converting a REG file created by MIMmaestro into a vector field by the transform module. 
Will this procedure create the same creation in 3DSlicer as the one created in MIMmaestro? 
I hope you can answer my question.
  </blockquote>
</aside>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b5b99a4efcd3cd1ba04d71a6fbc99dff32fe0a4e.png" data-download-href="/uploads/short-url/pVC4BpccpOK8U3LH9GNnP8YM8rA.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b5b99a4efcd3cd1ba04d71a6fbc99dff32fe0a4e.png" alt="image" data-base62-sha1="pVC4BpccpOK8U3LH9GNnP8YM8rA" width="690" height="248" data-dominant-color="E9EAEA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">979×352 45.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, I wrote the following code, but an error occurred.<br>
I would like to know if there is any improvement.</p>
<blockquote>
<blockquote>
<blockquote>
<p>labelValue = 1<br>
Loading with imageIOName: GDCM</p>
<p>labelmapVolumeNode =slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLLabelMapVolumeNode”)<br>
volumeNode = getNode(‘Displacement Field’)<br>
labelmapVolumeNode = getNode(‘LabelMapVolume’)<br>
segmentationNode = getNode(‘segmentation’)<br>
segmentId = ‘box’<br>
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, labelmapVolumeNode, volumeNode)<br>
True<br>
volumeArray = slicer.util.arrayFromVolume(volumeNode)<br>
labelArray = slicer.util.arrayFromVolume(labelmapVolumeNode)<br>
import numpy as np<br>
histogram = np.histogram(arrayFromVolume(volumeNode), bins=100)<br>
histogramInSegment = histogram[arrayFromSegmentBinaryLabelmap(segmentationNode, segmentId) != 0]<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
TypeError: only integer scalar arrays can be converted to a scalar index</p>
</blockquote>
</blockquote>
</blockquote>
<p>In addition, I have two questions.<br>
(1) What is the unit of the X-axis of DVF?<br>
Is it in mm or cm?<br>
(2) I would also like to know which axes A, S, and R in 3DSlicer represent respectively.</p>

---

## Post #2 by @lassoan (2021-11-04 03:46 UTC)

<aside class="quote no-group" data-username="toyama" data-post="1" data-topic="20473">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/82dd89/48.png" class="avatar"> toyama:</div>
<blockquote>
<p>histogramInSegment = histogram[arrayFromSegmentBinaryLabelmap(segmentationNode, segmentId) != 0]</p>
</blockquote>
</aside>
<p>There is a fundamental issue with this line. It seems that you want to filter parts of the histogram using spatial positions, which is impossible, because the histogram bins contain voxel count for the entire input array. You need to select the voxels that you are interested in before computing the histogram.</p>
<aside class="quote no-group" data-username="toyama" data-post="1" data-topic="20473">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/82dd89/48.png" class="avatar"> toyama:</div>
<blockquote>
<p>What is the unit of the X-axis of DVF?</p>
</blockquote>
</aside>
<p>In DICOM and by default in Slicer, all length units are millimeter.</p>
<aside class="quote no-group" data-username="toyama" data-post="1" data-topic="20473">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/82dd89/48.png" class="avatar"> toyama:</div>
<blockquote>
<p>I would also like to know which axes A, S, and R in 3DSlicer represent respectively.</p>
</blockquote>
</aside>
<p>Patient coordinate system directions, as defined in the DICOM standard (A = anterior = -posterior; S = superior; R = right = -left).</p>

---
