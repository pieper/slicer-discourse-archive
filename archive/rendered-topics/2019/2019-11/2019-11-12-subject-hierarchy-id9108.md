# Subject hierarchy

**Topic ID**: 9108
**Date**: 2019-11-12
**URL**: https://discourse.slicer.org/t/subject-hierarchy/9108

---

## Post #1 by @Ludovic_Ferrer (2019-11-12 00:17 UTC)

<p>Hi everyone,<br>
I have some issues with subject hierarchy in scripted-CLI. Basically, I created a QMRMLSubjectHierarchyTreeView to store ScalarVolume and TransformNode I use or create.<br>
My trouble is that I can’t make a node jump from one folder to an other despite the fact that I changed the parent node of the node I am interested to move to an other tree folder.<br>
I follow <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Subject_hierarchy" rel="nofollow noopener">this</a> unsuccessfully.</p>
<pre><code>for pet_node in getModalityVolumeNode('PT'):
sh = slicer.mrmlScene.GetSubjectHierarchyNode()
pet = sitkUtils.PullVolumeFromSlicer(pet_node)
rs_pet = sitk.RescaleIntensity(pet)
new_node_name = 'rs_'+pet_node.GetName()
slicer.mrmlScene.AddNewNodeByClass('vtkMRMLScalarVolumeNode', new_node_name)
sitkUtils.PushVolumeToSlicer(rs_pet, targetNode=new_node_name, name=new_node_name)
new_node = slicer.util.getNode(new_node_name)
new_node.SetAndObserveTransformNodeID(pet_node.GetTransformNodeID())
sh.SetItemParent(sh.GetItemByDataNode(new_node),  sh.GetItemParent(sh.GetItemByDataNode(pet_node)))
</code></pre>
<p>The last line modified the parent node ID for the current node but the change isn’t reflected in the gui. Did I missed a step ?<br>
Any hints would be appreciated.<br>
Regards</p>

---

## Post #2 by @lassoan (2019-11-12 00:46 UTC)

<p>There have been some regressions a few weeks ago in the Preview Release that are now fixed. Please try again with the latest Preview Release and let us know if it still does not work as expected.</p>

---

## Post #3 by @Ludovic_Ferrer (2019-11-12 07:41 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a>.<br>
That’s working now.<br>
Regards</p>

---
