# How to turn off the visibility of 3D models

**Topic ID**: 22143
**Date**: 2022-02-23
**URL**: https://discourse.slicer.org/t/how-to-turn-off-the-visibility-of-3d-models/22143

---

## Post #1 by @WilliamDaniel (2022-02-23 21:01 UTC)

<p>Hello!<br>
Hope you are doing well!<br>
As shown in figure below, I’ve created a ‘Segmentation’ node for ‘MRHead’ which contains two segments: Segment_1(with threshold 50-279), Segment_2(with threshold 80-279).</p>
<ol>
<li>I imported this segmentation node into the model module using the following code:</li>
</ol>
<pre><code class="lang-auto">shNode = slicer.mrmlScene.GetSubjectHierarchyNode()
exportFolderItemId = shNode.CreateFolderItem(shNode.GetSceneItemID(), 'HEAD')
segmentationNode1 = getNode("Segmentation")
slicer.modules.segmentations.logic().ExportAllSegmentsToModels(segmentationNode1, exportFolderItemId)
</code></pre>
<p>But after I run the above code, the models’ visibility of the two segments are turned on by default. How to turn off the visibility of the two segmented models using python separately?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9980d643902c27d08471a44116ede285d419df7.png" data-download-href="/uploads/short-url/zC0EXMO7pW5GmFl2BvozIKKIIFp.png?dl=1" title="Figure12" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9980d643902c27d08471a44116ede285d419df7_2_517x303.png" alt="Figure12" data-base62-sha1="zC0EXMO7pW5GmFl2BvozIKKIIFp" width="517" height="303" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9980d643902c27d08471a44116ede285d419df7_2_517x303.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9980d643902c27d08471a44116ede285d419df7_2_775x454.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9980d643902c27d08471a44116ede285d419df7_2_1034x606.png 2x" data-dominant-color="C0C4D9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Figure12</span><span class="informations">1192×699 152 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/98ba7819002405c09a24277fffaf79264db36003.png" data-download-href="/uploads/short-url/lN65c36tACxAMCUigdner2jHkqf.png?dl=1" title="Figure13" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/98ba7819002405c09a24277fffaf79264db36003_2_508x375.png" alt="Figure13" data-base62-sha1="lN65c36tACxAMCUigdner2jHkqf" width="508" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/98ba7819002405c09a24277fffaf79264db36003_2_508x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/98ba7819002405c09a24277fffaf79264db36003_2_762x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/98ba7819002405c09a24277fffaf79264db36003_2_1016x750.png 2x" data-dominant-color="CBCDDD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Figure13</span><span class="informations">1023×754 153 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="2">
<li>How to remove a segment in this segmentation node programmatically? For example, how to delete the second segment node(Segment_2)?</li>
</ol>
<p>Grateful for your help in advance!</p>

---

## Post #2 by @lassoan (2022-02-24 07:07 UTC)

<aside class="quote no-group" data-username="WilliamDaniel" data-post="1" data-topic="22143">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/williamdaniel/48/13425_2.png" class="avatar"> WilliamDaniel:</div>
<blockquote>
<p>But after I run the above code, the models’ visibility of the two segments are turned on by default. How to turn off the visibility of the two segmented models using python separately?</p>
</blockquote>
</aside>
<p>See how to iterate through the nodes in the subject hierarchy folder in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#traverse-children-of-a-subject-hierarchy-item">this example</a>.</p>
<p>You can hide a model node by calling <code>modelNode.GetDisplayNode().SetVisibility(False)</code>.</p>
<aside class="quote no-group" data-username="WilliamDaniel" data-post="1" data-topic="22143">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/williamdaniel/48/13425_2.png" class="avatar"> WilliamDaniel:</div>
<blockquote>
<p>How to remove a segment in this segmentation node programmatically? For example, how to delete the second segment node(Segment_2)?</p>
</blockquote>
</aside>
<p>It is probably better not to export the node in the first place. You can achieve that by using <a href="http://apidocs.slicer.org/master/classvtkSlicerSegmentationsModuleLogic.html#aefebd46381fb8fcbea556ae1a0503f57"> ExportSegmentsToModels that takes a segment ID list</a>; or hiding the segments you don’t want to export and use <a href="http://apidocs.slicer.org/master/classvtkSlicerSegmentationsModuleLogic.html#adde8a67557a69a6a7be6cf36bc3ec3e4">ExportVisibleSegmentsToModels</a>.</p>

---
