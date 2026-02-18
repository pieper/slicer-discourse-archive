# How do I get the ID number from subject hierarchy information for a segmentation?

**Topic ID**: 16780
**Date**: 2021-03-26
**URL**: https://discourse.slicer.org/t/how-do-i-get-the-id-number-from-subject-hierarchy-information-for-a-segmentation/16780

---

## Post #1 by @akshay_pillai (2021-03-26 16:45 UTC)

<p>I want to get the ID number present in the subject hierarchy information. I want to do that to access the children segments through the ID number. Heres a picture of what I want to get using python. How can I do this? <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a42a98c2916843fbab780c502793e83285c7aa4.png" data-download-href="/uploads/short-url/aAW9G86AMEXu0RU9EBiCUvSg3vm.png?dl=1" title="id" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a42a98c2916843fbab780c502793e83285c7aa4.png" alt="id" data-base62-sha1="aAW9G86AMEXu0RU9EBiCUvSg3vm" width="690" height="425" data-dominant-color="F5F7F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">id</span><span class="informations">696×429 16.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @mau_igna_06 (2021-03-26 17:09 UTC)

<p>Hi. You can do it like this:</p>
<pre><code class="lang-auto">shNode = slicer.mrmlScene.GetSubjectHierarchyNode()
segmentationItemID = shNode.GetItemByName("Segmentation")
</code></pre>

---

## Post #3 by @akshay_pillai (2021-03-26 17:12 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="2" data-topic="16780">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<pre><code class="lang-auto">shNode = slicer.mrmlScene.GetSubjectHierarchyNode()
segmentationItemID = shNode.GetItemByName("Segmentation")
</code></pre>
</blockquote>
</aside>
<p>Thanks, that’s great. How can I do this for the children?</p>

---

## Post #4 by @mau_igna_06 (2021-03-26 17:59 UTC)

<p>There is a segmentation data node, there isn’t a segment data node for each segment<br>
You can access segments from a segmentation like this:</p>
<pre><code class="lang-auto">segmentationDataNode = shNode.GetItemDataNode(segmentationItemID)

segmentIDinPosition0 = segmentationDataNode.GetSegmentation().GetNthSegmentID(0)
segmentInPosition0 = segmentationDataNode.GetSegmentation().GetSegment(segmentIDinPosition0)

upperAirwaySegmentID = segmentationDataNode.GetSegmentation().GetSegmentIdBySegmentName('upper_airway')
upperAirwaySegment = segmentationDataNode.GetSegmentation().GetSegment(upperAirwaySegmentID)
</code></pre>

---

## Post #5 by @koeglfryderyk (2022-05-09 21:21 UTC)

<p>Is there a way of doing this by vtk ID, so that the name of the segmentation doesn’t have to be used, as it can be ambiguous?</p>

---

## Post #6 by @lassoan (2022-05-10 04:22 UTC)

<p>Yes, sure, the segment ID is stored in the <code>segmentID</code> attribute of the subject hierarchy item:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/18562ecef4efeff7f3df486111e95d10faedc631.png" data-download-href="/uploads/short-url/3ti6wkE99NCSLEi3YKJ1EnEm3E5.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18562ecef4efeff7f3df486111e95d10faedc631_2_400x500.png" alt="image" data-base62-sha1="3ti6wkE99NCSLEi3YKJ1EnEm3E5" width="400" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18562ecef4efeff7f3df486111e95d10faedc631_2_400x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18562ecef4efeff7f3df486111e95d10faedc631_2_600x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/18562ecef4efeff7f3df486111e95d10faedc631_2_800x1000.png 2x" data-dominant-color="EFF2F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">987×1233 62 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @Thibaut_Faller (2022-08-02 15:15 UTC)

<p>You may use <em><strong>GetItemAttribute</strong></em> method to get the segmentID from the vtk ID:</p>
<pre><code class="lang-auto">shNode = slicer.mrmlScene.GetSubjectHierarchyNode()
segmentID = shNode.GetItemAttribute(vtkID, "segmentID")
</code></pre>

---
