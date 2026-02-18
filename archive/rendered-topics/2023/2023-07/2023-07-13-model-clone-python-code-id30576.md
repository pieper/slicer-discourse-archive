# Model Clone (Python Code)

**Topic ID**: 30576
**Date**: 2023-07-13
**URL**: https://discourse.slicer.org/t/model-clone-python-code/30576

---

## Post #1 by @Muhammed_Fatih_Talu (2023-07-13 09:22 UTC)

<p>After converting the segmentation node to the model, I want to clone the model.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b845f01715c70ee62cf0f6a02ea3807862e81de.png" alt="image" data-base62-sha1="hCGkCNeZuORdi4oKZjWZbjugfCK" width="390" height="117"></p>
<pre><code class="lang-auto">shNode = slicer.mrmlScene.GetSubjectHierarchyNode()
ModelsID = shNode.CreateFolderItem(shNode.GetSceneItemID(), "Models")
slicer.modules.segmentations.logic().ExportAllSegmentsToModels(segmentationNode, ModelsID)

shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
nodeToClone = slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLModelNode')
itemIDToClone = shNode.GetItemByDataNode(nodeToClone)
clonedItemID = slicer.modules.subjecthierarchy.logic().CloneSubjectHierarchyItem(shNode, itemIDToClone)
clonedNode = shNode.GetItemDataNode(clonedItemID)
</code></pre>
<p>The error:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/cecafdb2124cb443a75c759678e860b360f85810.png" data-download-href="/uploads/short-url/tvngr7IlAi3Ig60GgXdA9myNOBW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/cecafdb2124cb443a75c759678e860b360f85810.png" alt="image" data-base62-sha1="tvngr7IlAi3Ig60GgXdA9myNOBW" width="690" height="168" data-dominant-color="FBE3E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">740×181 4.96 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
