---
topic_id: 27126
title: "Is There A Way To Convert Markups To Volume"
date: 2023-01-09
url: https://discourse.slicer.org/t/27126
---

# Is there a way to convert Markups to Volume?

**Topic ID**: 27126
**Date**: 2023-01-09
**URL**: https://discourse.slicer.org/t/is-there-a-way-to-convert-markups-to-volume/27126

---

## Post #1 by @nnzzll (2023-01-09 11:39 UTC)

<p>I got a ScalarVolumeNode and a FiducialNode with aboslute glyph size like the screenshot below<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/fffaa08f16b88e2dbb55a7268798d4512a18847d.png" data-download-href="/uploads/short-url/AwuIIoV8C8pvxDn6jv0CwaK5G9L.png?dl=1" title="Screenshot from 2023-01-09 19-27-16" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/fffaa08f16b88e2dbb55a7268798d4512a18847d_2_690x384.png" alt="Screenshot from 2023-01-09 19-27-16" data-base62-sha1="AwuIIoV8C8pvxDn6jv0CwaK5G9L" width="690" height="384" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/fffaa08f16b88e2dbb55a7268798d4512a18847d_2_690x384.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/fffaa08f16b88e2dbb55a7268798d4512a18847d_2_1035x576.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/fffaa08f16b88e2dbb55a7268798d4512a18847d_2_1380x768.png 2x" data-dominant-color="9F9FD1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2023-01-09 19-27-16</span><span class="informations">1420×791 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Is there a way to convert the <code>vtkMRMLMarkupsFiducialNode</code> to a <code>vtkMRMLLabelmapVolumeNode</code>?</p>
<p>I suppose that if I can get the polydata of the FiducialNode,  I can convert it to a <code>SegmentationNode</code> then convert the <code>SegmentationNode</code> to a binary labelmap, is it possible?</p>

---

## Post #2 by @cpinter (2023-01-09 14:40 UTC)

<aside class="quote no-group" data-username="nnzzll" data-post="1" data-topic="27126">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/nnzzll/48/16350_2.png" class="avatar"> nnzzll:</div>
<blockquote>
<p>I suppose that if I can get the polydata of the FiducialNode, I can convert it to a <code>SegmentationNode</code> then convert the <code>SegmentationNode</code> to a binary labelmap, is it possible?</p>
</blockquote>
</aside>
<p>This is what I’d do. Make sure you have a different model node for each fiducial, and have them in a folder in subject hierarchy, then you can convert them to a segmentation node right-clicking the folder.</p>

---

## Post #3 by @nnzzll (2023-01-10 02:02 UTC)

<p>Now the problem is how to get the polydata from FiducialNode?</p>
<p>I tried the <code>GetScalarDataSet()</code> method of <code>vtkMRMLMarkupsFiducialDisplayNode</code>, but it returned polygon line rather than spheres</p>

---

## Post #4 by @cpinter (2023-01-11 13:05 UTC)

<p>I remember this question having been answered recently in the forum. Please do a search for it.</p>

---
