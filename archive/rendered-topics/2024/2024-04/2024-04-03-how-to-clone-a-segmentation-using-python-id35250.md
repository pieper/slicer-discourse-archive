---
topic_id: 35250
title: "How To Clone A Segmentation Using Python"
date: 2024-04-03
url: https://discourse.slicer.org/t/35250
---

# How to clone a segmentation using Python

**Topic ID**: 35250
**Date**: 2024-04-03
**URL**: https://discourse.slicer.org/t/how-to-clone-a-segmentation-using-python/35250

---

## Post #1 by @Matteboo (2024-04-03 11:55 UTC)

<p>Hello,<br>
I have the segmentation of an anatomical structure.<br>
I want to clone that segmentation to apply a transform on a copy in order to analyze the impact of the transform.</p>
<pre><code class="lang-auto">segmentation_cancer_contracted=slicer.vtkMRMLSegmentationNode()
segmentation_cancer_contracted.Copy(segmentation_cancer)
slicer.mrmlScene.AddNode(segmentation_cancer_contracted)
segmentation_cancer_contracted.Copy(segmentation_cancer)
segmentation_cancer_contracted.SetName("Cancer contracted")
segmentation_cancer_contracted.SetAndObserveTransformNodeID(transformNode.GetID())
segmentation_cancer_contracted.HardenTransform()
</code></pre>
<p>This create a second segmentation but it seems to be linked to the original one. For example when I hide one, both hide.</p>
<p>I want something similar to the “clone” option when right clicking the segmentation. I understand that I have to use vtkSlicerSubjectHierarchyModuleLogic::CloneSubjectHierarchyItem but I don’t understand the input</p>
<p>Any help would be greatly appreciated</p>

---

## Post #2 by @cpinter (2024-04-03 12:34 UTC)

<p>The script repository is an incredible source of knowledge.</p>
<p>Here’s the relevant script:<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#clone-a-node" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#clone-a-node</a></p>
<aside class="quote no-group" data-username="Matteboo" data-post="1" data-topic="35250">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/matteboo/48/66548_2.png" class="avatar"> Matteboo:</div>
<blockquote>
<p>when I hide one, both hide</p>
</blockquote>
</aside>
<p>The cloning function does not provide this, on purpose, because it can cause problems if the content of the two segmentations start to differ. But it you insist on this, you can se the display node of the original to be the display node of the clone as well. Or you can add an observer on the display node and synchronize visibility or whatever property you’d like.</p>

---

## Post #3 by @Matteboo (2024-04-03 13:35 UTC)

<p>Thanks you, I was able to find the solution <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20"></p>
<p>Here is the working code</p>
<p><code>shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene) itemIDToClone = shNode.GetItemByDataNode(segmentation_cancer) clonedItemID = slicer.modules.subjecthierarchy.logic().CloneSubjectHierarchyItem(shNode, itemIDToClone) segmentation_cancer_contracted = shNode.GetItemDataNode(clonedItemID) segmentation_cancer_contracted.SetName("Cancer contracted") segmentation_cancer_contracted.GetSegmentation().GetNthSegment(0).SetName("cancer contracted") segmentation_cancer_contracted.SetAndObserveTransformNodeID(inverse_transform.GetID()) segmentation_cancer_contracted.HardenTransform()</code></p>

---
