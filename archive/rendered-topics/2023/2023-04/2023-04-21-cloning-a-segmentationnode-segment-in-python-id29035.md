# Cloning a SegmentationNode segment in Python

**Topic ID**: 29035
**Date**: 2023-04-21
**URL**: https://discourse.slicer.org/t/cloning-a-segmentationnode-segment-in-python/29035

---

## Post #1 by @pearsonm (2023-04-21 00:11 UTC)

<p>I am working on a module where I make a make a binary labelmap on a 2d view with the scissors rectangle tool. The next step is to cut the rectangle into 3 regions for further processing.</p>
<p>My first approach was to add 3 segments with AddEmptySegment and then use SetExtent to resize the rectangles. This is not being reflected in the segmentation node so I am obviously missing something.</p>
<p>I worked out that I can do this manually by right-clicking on the mask in Subject Hierarchy in the Data module and selecting Clone. I can then rename the segment and modify Extent.</p>
<p>Is it possible to perform the clone from Python? I looked at the SubjectHierarchy code but could not work it out.</p>

---

## Post #2 by @pearsonm (2023-04-21 01:19 UTC)

<p>I worked it out, if the original mask is (62, 71, 69, 102, 0, 11) the upper region is</p>
<pre><code class="lang-auto">slicer.mrmlScene.GetNodeByID("vtkMRMLSegmentationNode1").GetSegmentation().AddEmptySegment("upper")
s0 = slicer.mrmlScene.GetNodeByID("vtkMRMLSegmentationNode1").GetSegmentation().GetNthSegment(0)
s1 = slicer.mrmlScene.GetNodeByID("vtkMRMLSegmentationNode1").GetSegmentation().GetNthSegment(1)
s1.DeepCopy(s0)
slicer.mrmlScene.GetNodeByID("vtkMRMLSegmentationNode1").GetSegmentation().GetNthSegment(1).SetName("upper")
slicer.mrmlScene.GetNodeByID("vtkMRMLSegmentationNode1").GetSegmentation().GetNthSegment(1).GetRepresentation("Binary labelmap").SetExtent([62, 71, 69, 80, 0, 11])
</code></pre>

---

## Post #3 by @cpinter (2023-05-04 08:51 UTC)

<p>You can clone an item via code like this</p>
<p><code>clonedItemID = slicer.modules.subjecthierarchy.logic().CloneSubjectHierarchyItem(shNode, itemID)</code></p>

---

## Post #4 by @pearsonm (2023-05-04 10:39 UTC)

<p>Thanks, that is a much easier way to do it.</p>

---

## Post #5 by @pearsonm (2023-05-17 04:23 UTC)

<p>I found a problem using the suggested method on a segmentation. If you load sample data and create a segmentation with Segment Editor the clone is not valid</p>
<pre><code class="lang-auto">import SampleData
node = SampleData.SampleDataLogic().downloadMRHead()
</code></pre>
<p>Switch to Segment Editor and create a segmentation</p>
<pre><code class="lang-auto">segmentationNode = slicer.mrmlScene.GetNodeByID("vtkMRMLSegmentationNode1")
shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
segmentationID = shNode.GetItemByDataNode(segmentationNode)
segmentID = shNode.GetItemChildWithName(segmentationID, "Segment_1")
clonedItemID = slicer.modules.subjecthierarchy.logic().CloneSubjectHierarchyItem(shNode, segmentID)
</code></pre>
<p>The result is Segment_1 Copy but it is not a valid segment<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5bae7474aa03e3e3d6986f8a23dddfdb48f68f8c.png" data-download-href="/uploads/short-url/d53duV5TZKWWSpxYhiKJct5yr8g.png?dl=1" title="step2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5bae7474aa03e3e3d6986f8a23dddfdb48f68f8c_2_690x154.png" alt="step2" data-base62-sha1="d53duV5TZKWWSpxYhiKJct5yr8g" width="690" height="154" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5bae7474aa03e3e3d6986f8a23dddfdb48f68f8c_2_690x154.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5bae7474aa03e3e3d6986f8a23dddfdb48f68f8c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5bae7474aa03e3e3d6986f8a23dddfdb48f68f8c.png 2x" data-dominant-color="DDE7EE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">step2</span><span class="informations">797×179 20.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>If I right-click on Segment_1 and choose Clone then the clone is a valid copy. Should the 2 methods be equivalent?</p>

---
