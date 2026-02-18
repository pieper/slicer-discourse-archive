# How to duplicate a vtkMRMLScalarVolumeNode using Python?

**Topic ID**: 28758
**Date**: 2023-04-05
**URL**: https://discourse.slicer.org/t/how-to-duplicate-a-vtkmrmlscalarvolumenode-using-python/28758

---

## Post #1 by @sunshine (2023-04-05 15:48 UTC)

<p>Hi everyone,</p>
<p>I am trying to duplicate a vtkMRMLScalarVolumeNode:<br>
<code>node_CopyVolume = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLScalarVolumeNode')</code></p>
<p>What can I do to copy the volume data from <code>node_OriginVolume</code> to the <code>node_CopyVolume</code>, so that <code>node_CopyVolume</code> can be displayed in the 3D view when <code>node_OriginVolume</code> is changed or removed?</p>
<p>Thank you so much in advance!</p>

---

## Post #2 by @pieper (2023-04-05 15:59 UTC)

<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository/volumes.html#clone-a-volume" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository/volumes.html#clone-a-volume</a></p>

---

## Post #5 by @sunshine (2023-04-05 19:17 UTC)

<p>Hi Steve,</p>
<p>Thank you so much for your help!</p>
<p>I tested two ways of cloning the ScalarVolume:</p>
<ol>
<li>Following the way you showed me:</li>
</ol>
<pre><code class="lang-auto">volumesLogic = slicer.modules.volumes.logic()
node_Copy= volumesLogic.CloneVolume(slicer.mrmlScene, node_Origin, "Cloned volume")
</code></pre>
<ol start="2">
<li>The method to copy any type of node:</li>
</ol>
<pre><code class="lang-auto">shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
itemIDToClone_X  = shNode.GetItemByDataNode(node_Origin)
clonedItemID_X = slicer.modules.subjecthierarchy.logic().CloneSubjectHierarchyItem(shNode, itemIDToClone_X)
node_Copy = shNode.GetItemDataNode(clonedItemID_X);    node_Copy.SetName("Cloned volume")
</code></pre>
<p>However, after I got <code>node_Copy </code>, neither of the two copied ScalarVolume can be displayed under a transform hierarchy. I was only able to display them in 2D window with Axial plane setting, however, never be able to put them under a Linear Transform.</p>
<p>Could you please help me solve the problem, and let me know how to show the cloned ScalarVolume in 3D?</p>

---

## Post #6 by @pieper (2023-04-05 21:16 UTC)

<p>The CloneVolume method at least should give you a normal volume node that should work the same as the source.  I haven’t tried the subject hierarchy version but it should be the same as cloning with the context menu in the Data module so you could experiment with that to see if you get the same kind of node with code that you get manually.</p>
<p>Generally, it’s best if you can provide the shortest possible snippet that replicates any issues you see using public data (using the SampleData module).  Something that anyone can paste in the the python console to replicate.  Then we can see what’s happening and give you advice.</p>

---

## Post #7 by @sunshine (2023-04-05 23:42 UTC)

<p>Thank you, <a class="mention" href="/u/pieper">@pieper</a> !</p>
<p>Yes, I can make the <code>node_Copy</code> display in the 3D view when toggling it in one of the three 2D windows (red, green, yellow).</p>
<p>However, ever since the 2D window changed the view, the ScalarVolume will disappear.</p>
<p>How can I display all more than 3 ScalarVolumes in the 3D window?<br>
Say if I would like to display 10 ScalarVolumes at the same time in 3D slicer, all duplicated and transformed from the original one, is that possible?</p>

---

## Post #8 by @pieper (2023-04-06 19:30 UTC)

<p>You may need to review some of the tutorials and examples to see what’s available currently built in to Slicer.  If it’s not available you may need to write custom code to display the 10 volumes the way you want them.</p>

---
