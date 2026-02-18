# Detect subject hierarchy node deletion before its children get deleted

**Topic ID**: 27517
**Date**: 2023-01-28
**URL**: https://discourse.slicer.org/t/detect-subject-hierarchy-node-deletion-before-its-children-get-deleted/27517

---

## Post #1 by @Albi (2023-01-28 15:38 UTC)

<p>In a custom module I would like to detect the deletion of an item to take appropriate action before its children gets deleted. I observed that the signal SubjectHierarchyItemAboutToBeRemovedEvent of the item is emitted after the deletion of the childrens. Is there a way to detect that the item will be deleted before its childrens ?</p>
<p>To reproduce:</p>
<ul>
<li>Load <a href="https://www.slicer.org/wiki/SampleData" class="inline-onebox" rel="noopener nofollow ugc">SampleData - Slicer Wiki</a> MR-head.nrrd</li>
<li>Create a segmentation</li>
<li>In Data module, drag and drop segmentation on MR-head volume (to have segementation as children of MR-head)</li>
<li>Observe event with the following python snippet:</li>
</ul>
<pre><code class="lang-python">shNode=slicer.app.mrmlScene().GetSubjectHierarchyNode()

@vtk.calldata_type(vtk.VTK_INT)
def onShItemAboutToBeRemoved(caller, event, removedItem):
  removedNode = shNode.GetItemDataNode(removedItem) if removedItem else None
  if removedNode is not None and removedNode.IsA('vtkMRMLNode'):
    print("About to remove node = ", removedNode.GetName())

shNode.AddObserver(shNode.SubjectHierarchyItemAboutToBeRemovedEvent, onShItemAboutToBeRemoved)
</code></pre>
<p>Delete MR-head</p>
<p>Result:<br>
About to remove node =  Segmentation<br>
About to remove node =  MR-head</p>

---

## Post #2 by @cpinter (2023-02-09 09:59 UTC)

<p>Would it help if we changed the SH code so that the about to remove event is invoked first on the parents? I don’t see any harm in that; it makes sense to “announce” the deletion of an object before the ones that its own deletion causes.</p>
<p>What do you think <a class="mention" href="/u/lassoan">@lassoan</a> ?</p>

---
