# How to copy one segment from a segmentation node to a different segmentation with code?

**Topic ID**: 19286
**Date**: 2021-08-20
**URL**: https://discourse.slicer.org/t/how-to-copy-one-segment-from-a-segmentation-node-to-a-different-segmentation-with-code/19286

---

## Post #1 by @akshay_pillai (2021-08-20 15:43 UTC)

<p>I’m trying to copy a segment from one segmentation to another, but I don’t know how to do it automatically in my code. I know that we can drag and drop in the data module, but is there a way to do this with code?</p>

---

## Post #2 by @mau_igna_06 (2021-08-20 16:24 UTC)

<p>A workaround could be to export all the segments of Segmentation1 as LabelMap and import it to Segmentation2, then delete all the undesired segments from Segmentation2</p>

---

## Post #3 by @akshay_pillai (2021-08-20 16:27 UTC)

<p>yes, that would work but I just wanted to know if I could avoid doing that and just move one segment.</p>

---

## Post #4 by @lassoan (2021-08-20 18:51 UTC)

<p>Yes, you can copy/move segments between segmentations. You can <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features">track down how it is implemented in Slicer core</a> and replicate that in your script.</p>

---

## Post #5 by @Sergio (2023-08-04 18:25 UTC)

<p>Do you have an example of the script used to do this?</p>
<p>Thanks in advance.</p>

---

## Post #6 by @connorh (2024-09-17 04:50 UTC)

<p>I needed to figure this out myself - for anyone in the future that needs this:</p>
<pre><code class="lang-auto">destSeg = getNode("segmentDestination") #the vtkMRMLSegmentationNode you want the target in
sourceSeg = getNode("segmentSource") # the vtkMRMLSegmentationNode that it's coming from
segmentID = "yourDesiredSegID" #the ID of your segment
removeFromSource = False #whether you want to delete the segment from the source
destSeg.GetSegmentation().CopySegmentFromSegmentation(sourceSeg.GetSegmentation(),segmentID,removeFromSource) 
</code></pre>

---
