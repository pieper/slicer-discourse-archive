# Growth plate segmentation - same intensity as surrounding tissues

**Topic ID**: 42602
**Date**: 2025-04-17
**URL**: https://discourse.slicer.org/t/growth-plate-segmentation-same-intensity-as-surrounding-tissues/42602

---

## Post #1 by @mariammtch (2025-04-17 11:54 UTC)

<p>Hi. I have 7 different timepoint (so variable in size) CT data without contrast. I need to mark the gap (meant to be a growth plate) between the bony parts (marked in beige in the screenshot) . It is not uniform so 3D painting doesn’t really help as it includes other gaps inside the segment. I have tried wrap solidify method but when I use it either the software crushes or I get something very inaccurate:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/59fb49a2dfcb0650a90bc63e413213663645df07.jpeg" data-download-href="/uploads/short-url/cQ0SjXcA1K1oYW85LLzomGo4zZl.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59fb49a2dfcb0650a90bc63e413213663645df07_2_476x500.jpeg" alt="image" data-base62-sha1="cQ0SjXcA1K1oYW85LLzomGo4zZl" width="476" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59fb49a2dfcb0650a90bc63e413213663645df07_2_476x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/9/59fb49a2dfcb0650a90bc63e413213663645df07_2_714x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/59fb49a2dfcb0650a90bc63e413213663645df07.jpeg 2x" data-dominant-color="36352D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">723×758 182 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I tried coding as well but it somehow overlaps bone segment instead of filling the gap. This is the code I used:</p>
<pre><code class="lang-auto">import slicer
import vtk
import SimpleITK as sitk
import sitkUtils

# 1. Get your segmentation node
segmentationNode = slicer.util.getNode("Segmentation")  # Replace with your segmentation name

# 2. Export segmentation to labelmap (binary image)
labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, labelmapVolumeNode)

# 3. Convert to SimpleITK image
image = sitkUtils.PullVolumeFromSlicer(labelmapVolumeNode)

# 4. Fill gap between two segments (cartilage should be in between)
# We will use morphological closing (dilate then erode) to fill the gap
# Increase kernel size if gap is large
filledImage = sitk.BinaryMorphologicalClosing(image, [5]*3)

# 5. Extract cartilage as the difference (filled - original)
cartilage = sitk.Subtract(filledImage, image)

# 6. Push the cartilage mask as a new labelmap node
cartilageLabelmap = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode", "CartilageMask")
sitkUtils.PushVolumeToSlicer(cartilage, targetNode=cartilageLabelmap)

# 7. Import the cartilage mask into the original segmentation as a new segment
slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(cartilageLabelmap, segmentationNode)
segmentationNode.GetSegmentation().GetNthSegment(segmentationNode.GetSegmentation().GetNumberOfSegments() - 1).SetName("Cartilage")

# 8. Optional: Change cartilage color
cartilageSegmentID = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName("Cartilage")
segmentationNode.GetSegmentation().GetSegment(cartilageSegmentID).SetColor(0.0, 1.0, 1.0)  # Cyan
</code></pre>
<p>Ideally, I am looking for an automated method as I will have to segment out 80 growth plates.</p>
<p>Thanks in advance</p>

---

## Post #2 by @lassoan (2025-04-17 12:03 UTC)

<p>A simple method is to segment the bones (each in a separate segment, no need to make them solid, simple Threshold effect + Island effect / Split islands may be sufficient, but if not then you can use Grow from seeds effect), dilate them by a few millimeters (Margin effect, adjust masking settings to allow overlap). Growth plates are the regions where multiple dilated segments overlap (you can get them with Logical operators effect).</p>

---

## Post #3 by @mariammtch (2025-04-22 10:32 UTC)

<p>Hi,</p>
<p>Million thanks for this. It is working in younger aged groups but as an individual grows, the gap is not empty but some bony connections start to appear and splitting islands doesn’t work in that case as they are recognised as one whole structure. Would you have any suggestion for these kind of semi-connected bone pieces with the growth plate between them? Connection % between bone parts increases till the growth plate closure</p>
<p>Thanks in advance!</p>

---
