---
topic_id: 1641
title: "Interpreting Segmentation Nrrd Files"
date: 2017-12-12
url: https://discourse.slicer.org/t/1641
---

# Interpreting segmentation nrrd files

**Topic ID**: 1641
**Date**: 2017-12-12
**URL**: https://discourse.slicer.org/t/interpreting-segmentation-nrrd-files/1641

---

## Post #1 by @dcantor (2017-12-12 00:28 UTC)

<p>Hello,</p>
<p>I am segmenting prostates with Slicer and now I want to post-process my segmentations. So I read the nrrd segmentation files with my python code. I have a case where I have one file with one segmentation and two segments corresponding to two lesions. I notice that:</p>
<ol>
<li>
<p>in the nrrd file the <strong>data</strong> is 4-d array where the first dimension seems to correspond to the segment in a multi-segment segmentation. (is that the case?)</p>
</li>
<li>
<p>The header <strong>dimension</strong> header is now 4 (instead of 3) I am assuming that is because each segment/lesion is stored in its own array.</p>
</li>
<li>
<p>The <strong>spaces direction</strong> header is an array with 4 elements now, whereas the first element of the array is ‘none’ and the other three elements are 3-d vectors. I assume this is to match the fact that data is now a 4-d matrix  (is that the case?)</p>
</li>
<li>
<p>The <strong>sizes</strong> header is also 4-d and it seems that the first coordinate corresponds to the number of segments and the other three are the minimum common cube that contain the segments.</p>
</li>
</ol>
<p>Are my assumptions correct?</p>
<p>Thanks,</p>
<p>D</p>

---

## Post #2 by @lassoan (2017-12-12 01:04 UTC)

<p>Yes, all the above are correct. Segmentation is stored in a 4D array (segment index and 3 spatial dimensions) because segments may overlap.</p>

---

## Post #3 by @ihnorton (2017-12-12 01:50 UTC)

<p>In case you haven’t seen it: <a href="https://github.com/mhe/pynrrd">pynrrd</a>.</p>

---

## Post #4 by @pieper (2017-12-13 17:18 UTC)

<p>If you know the segments don’t overlap you could export to a labelmap (to store as a 3D nrrd or nifti which is sometimes more compatible with other software).</p>

---

## Post #5 by @tbillah (2019-06-14 19:59 UTC)

<p>Let’s look at the following key value pair for a segment NRRD header:</p>
<p>Segment0_Extent:=7 110 376 473 383 572</p>
<p>What does the above key value pair mean? 7 should be the 7th volume, but what do the following numbers mean?</p>
<p>Again, what does the following imply?</p>
<p>Segmentation_ReferenceImageExtentOffset:=114 108 88</p>
<p>Is the Offset in IJK or world coordinates?</p>
<p>Reference to any TUTORIAL would be helpful.</p>

---

## Post #6 by @tbillah (2019-06-14 20:13 UTC)

<p>Thanks for <a class="mention" href="/u/fedorov">@fedorov</a>. I guess part of the answer is <a href="https://vtk.org/doc/nightly/html/classvtkImageData.html#a9cfc94cd8d5c96656222b1ec0f3595c5" rel="nofollow noopener">here</a> .</p>

---

## Post #7 by @cpinter (2019-06-14 20:18 UTC)

<p>The segmentation 4D nrrd file is considered Slicer-specific, to enable single-file export/import of whole labelmap based segmentations. So there are no tutorials, because we don’t intend this to be used directly, but through the Slicer storage infrastructure.</p>
<p>The extent does not start at 0 because segments do not store the whole reference image geometry, only the non-empty part of the segment labelmap (“effective extent”).<br>
(The vtkImageData::Extent variable that you linked just now explains what an extent is, but it does not explain the effective extent used for segments)</p>
<p>I suggest that instead of trying to read this 4D nrrd, you export the segmentation as a labelmap within Slicer and save that in a usual 3D nrrd. Of course any overlap information will be lost (if you’re concerned about this you can export the segments in individual labelmaps too with some python scripting).<br>
There are many topics describing how to do this programmatically, such as <a href="https://discourse.slicer.org/t/export-segmentation-to-labelmap-using-python/6801">this</a> or <a href="https://discourse.slicer.org/t/get-label-map-node-from-segmentation-node/1137">this</a>. If you want to do this from the UI then here’s the easiest way<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b310ff8dc8ffe9c4a910511c42c4e70e99cf2fdc.png" alt="image" data-base62-sha1="py5SV2YdFx54Fe7gBhD09goxik4" width="473" height="330"><br>
but you can find more options in the Segmentations module</p>

---

## Post #8 by @tbillah (2019-06-14 20:24 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="7" data-topic="1641">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>I suggest that instead of trying to read this 4D nrrd</p>
</blockquote>
</aside>
<p>Thanks. I am loading the segmentation file (i.e. header) in Python. I need to apply transform (warp/affine) on your segmentation file which is why understanding each key-value pair is important to me.</p>
<p>In case missed, what does the following mean? Is it in IJK?</p>
<blockquote>
<p>Segmentation_ReferenceImageExtentOffset:=114 108 88</p>
</blockquote>

---

## Post #9 by @lassoan (2019-06-14 20:29 UTC)

<p>Most private metadata fields in the 4D .seg.nrrd file is for performance improvement only (so that we don’t need to recompute effective extents of frames), so you can safely ignore them. But probably we should document them somewhere anyway. I’ll specify those fields and add a link here.</p>

---

## Post #10 by @fedorov (2019-06-14 20:31 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="1641">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>But probably we should document them somewhere anyway.</p>
</blockquote>
</aside>
<p>I suggest it makes sense to do it here:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.10/SlicerApplication/SupportedDataFormat" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/4.10/SlicerApplication/SupportedDataFormat</a></p>

---

## Post #11 by @lassoan (2019-06-17 17:57 UTC)

<p>I’ve added description here: <a href="https://github.com/Slicer/Slicer/blob/e7d91177d4873dfde90e47df336be8487bff6c5d/Libs/MRML/Core/vtkMRMLSegmentationStorageNode.h#L56-L122" rel="nofollow noopener">https://github.com/Slicer/Slicer/blob/e7d91177d4873dfde90e47df336be8487bff6c5d/Libs/MRML/Core/vtkMRMLSegmentationStorageNode.h#L56-L122</a></p>
<p>I’ve added links from the <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/SupportedDataFormat" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/SupportedDataFormat</a> pages to the specification of the custom fields.</p>

---
