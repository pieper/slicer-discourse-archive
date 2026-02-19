---
topic_id: 31619
title: "Clone Markups Node Fails During Custom Module Cleanup"
date: 2023-09-08
url: https://discourse.slicer.org/t/31619
---

# Clone markups node fails during custom module cleanup

**Topic ID**: 31619
**Date**: 2023-09-08
**URL**: https://discourse.slicer.org/t/clone-markups-node-fails-during-custom-module-cleanup/31619

---

## Post #1 by @Patrick_Li (2023-09-08 13:55 UTC)

<p>I use this code to clone a ClosedCurveMarkups node</p>
<pre><code class="lang-auto"># Clone the node
itemIDToClone = shNode.GetItemByDataNode(dataNode)
clonedItemID = slicer.modules.subjecthierarchy.logic().CloneSubjectHierarchyItem(shNode, itemIDToClone)
clonedNode = self.shNode.GetItemDataNode(clonedItemID)
</code></pre>
<p>In all other instances, the node clones without issue. When I invoke this code to clone and save the node after the user closes the application, however, it fails, with clonedItemID always returning a 0. Is there a way to resolve or circumvent this?</p>

---

## Post #2 by @lassoan (2023-09-10 01:56 UTC)

<p>I’ve created a curve node and ran this:</p>
<pre><code class="lang-python">shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)
itemIDToClone = shNode.GetItemByDataNode(dataNode)
clonedItemID = slicer.modules.subjecthierarchy.logic().CloneSubjectHierarchyItem(shNode, itemIDToClone)
clonedNode = shNode.GetItemDataNode(clonedItemID)
print(clonedItemID)
print(clonedNode)
</code></pre>
<p>It cloned the curve node currectly. <code>clonedItemID</code> was valid (non-zero). <code>clonedNode</code> was valid. Saved and loaded the scene. The original and the cloned curve both loaded correctly. So, I don’t see any issues. Maybe <code>self.shNode</code> in your code contains some old subject hierarchy node.</p>

---
