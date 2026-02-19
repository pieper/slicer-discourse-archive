---
topic_id: 38201
title: "How To Add Segmentation To A Specific Frame In Sequence Brow"
date: 2024-09-04
url: https://discourse.slicer.org/t/38201
---

# How to add segmentation to a specific frame in sequence browser

**Topic ID**: 38201
**Date**: 2024-09-04
**URL**: https://discourse.slicer.org/t/how-to-add-segmentation-to-a-specific-frame-in-sequence-browser/38201

---

## Post #1 by @maniron (2024-09-04 11:06 UTC)

<p>Kindly help me out with adding my model segmentation output to a sequence browser to a specific frame . I have been trying to find a solution for along if any one have a solution let me know</p>

---

## Post #2 by @maniron (2024-09-04 12:03 UTC)

<p>Kindly help me out with adding my model segmentation output to a sequence browser to a specific frame . I have been trying to find a solution for along if any one have a solution let me know</p>

---

## Post #3 by @lassoan (2024-09-12 03:33 UTC)

<p>See a complete example how you can segment each frame of a volume sequence and store the segmentation result in a segmentation sequence in <a href="https://github.com/lassoan/SlicerTotalSegmentator/blob/main/TotalSegmentator/TotalSegmentator.py">TotalSegmentator</a>.</p>

---

## Post #4 by @maniron (2024-09-17 06:29 UTC)

<p>Thanks for responding <a class="mention" href="/u/lassoan">@lassoan</a> , can you please guide me where exactly i can find, and wanted to know how can we save sequence browser segmentation, As I tested it is saving only one frame mask for DICOM 2D + time, but in NRRD type file I could see it was saving mask for the whole volume</p>
<p>And I want to know how can I get segmentation details for a specific frame in sequence browser (DICOM 2D + time)</p>
<blockquote>
<p>segmentationSequenceNode = slicer.util.getNode(‘Sequence_1’)<br>
segmentationNodeForFrame = segmentationSequenceNode.GetNthDataNode(refIndex)<br>
segmentation = segmentationNodeForFrame.GetSegmentation()<br>
segVal = segmentation.GetNumberOfSegments()<br>
segmentId = “Segment_” + str(segVal)<br>
segmentId = segmentationNodeForFrame.GetSegmentation().GetSegmentIdBySegmentName(segmentId)<br>
# Get segment as numpy array<br>
segVal = slicer.util.arrayFromSegmentInternalBinaryLabelmap(segmentationNodeForFrame, segmentId)</p>
</blockquote>
<p>This was the code I used to get segmentation for a specific frame in sequence browser, Is this correct way</p>

---

## Post #5 by @lassoan (2024-09-17 13:54 UTC)

<p>You need to implement DICOM export of time sequences yourself. It should not be complicated, you just need to export each time point with the appropriate timestamp, with the same series instance UID.</p>
<p>You can look up any DICOM metadata from the <code>DICOM.instanceUIDs</code> attribute of the volume. See the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#access-tag-of-a-scalar-volume-loaded-from-dicom">script repository</a> for a complete example.</p>

---
