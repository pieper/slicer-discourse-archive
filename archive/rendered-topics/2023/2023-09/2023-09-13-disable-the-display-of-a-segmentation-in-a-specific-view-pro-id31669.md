---
topic_id: 31669
title: "Disable The Display Of A Segmentation In A Specific View Pro"
date: 2023-09-13
url: https://discourse.slicer.org/t/31669
---

# Disable the display of a segmentation in a specific view programmatically.

**Topic ID**: 31669
**Date**: 2023-09-13
**URL**: https://discourse.slicer.org/t/disable-the-display-of-a-segmentation-in-a-specific-view-programmatically/31669

---

## Post #1 by @waromero (2023-09-13 04:11 UTC)

<p>Hello!</p>
<p>In the UI of the <em>Segmentations</em> module it is possible to configure per-view visibility of a segmentation.<br>
(Segmentations / Advanced / Views → uncheck view of interest ).</p>
<p>I am interested in doing the same thing programmatically.</p>
<p>I could not find out the class/attribute that contains the method to enable/disable the display of segmentation in a specific view.</p>
<p>Thanks !</p>

---

## Post #2 by @ungi (2023-09-13 22:26 UTC)

<p>Hi, display nodes usually have this function called SetViewNodeIDs(…), which expects a list of view IDs where the visibility will apply.</p>
<p>E.g., if you make a segmentation with the default name “Segmentation” then this is how you would make sure the segmentation is only visible in the green 2D view, but not in the red or yellow:</p>
<pre><code class="lang-auto">displayNode = slicer.util.getNode("Segmentation").GetDisplayNode()
displayNode.SetViewNodeIDs(["vtkMRMLSliceNodeGreen"])
</code></pre>

---
