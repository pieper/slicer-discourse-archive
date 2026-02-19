---
topic_id: 8635
title: "Clone Markups Node"
date: 2019-10-01
url: https://discourse.slicer.org/t/8635
---

# Clone markups node

**Topic ID**: 8635
**Date**: 2019-10-01
**URL**: https://discourse.slicer.org/t/clone-markups-node/8635

---

## Post #1 by @ezemikulan (2019-10-01 15:29 UTC)

<p>Hi, I need to clone a markups node but I can’t find a way to do it. I know that for volumes there is (using python):</p>
<blockquote>
<p>slicer.vtkSlicerVolumesLogic().CloneVolume()</p>
</blockquote>
<p>I would like to know if there’s a similar method for markups, as I would like to make multiple copies of a set of markups and apply different transforms to them.</p>
<p>Thanks for your help. Cheers,</p>

---

## Post #2 by @Sam_Horvath (2019-10-01 15:41 UTC)

<p>Example code for this can be found here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Clone_a_node" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Clone_a_node</a></p>
<pre><code># Get a node from SampleData that we will clone
import SampleData
nodeToClone = SampleData.SampleDataLogic().downloadMRHead()

# Clone the node
shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
itemIDToClone = shNode.GetItemByDataNode(nodeToClone)
clonedItemID = slicer.modules.subjecthierarchy.logic().CloneSubjectHierarchyItem(shNode, itemIDToClone)
clonedNode = shNode.GetItemDataNode(clonedItemID)</code></pre>

---

## Post #3 by @ezemikulan (2019-10-02 07:50 UTC)

<p>Thanks, it works perfectly.</p>

---
