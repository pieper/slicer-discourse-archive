---
topic_id: 14331
title: "Show Slicer Views In Selected 3D Windows"
date: 2020-10-30
url: https://discourse.slicer.org/t/14331
---

# Show Slicer Views in selected 3d windows

**Topic ID**: 14331
**Date**: 2020-10-30
**URL**: https://discourse.slicer.org/t/show-slicer-views-in-selected-3d-windows/14331

---

## Post #1 by @Chintha_Siva_Prasad (2020-10-30 14:39 UTC)

<p>I have many 3d windows. And I want to show the slice view in only of the 3d view. How can I do that?</p>

---

## Post #2 by @lassoan (2020-11-02 20:18 UTC)

<p>You can set view node IDs in display nodes. If you set view node IDs then the node is only shown in those views that have their IDs listed. So, find display node corresponding to the slice node and call <a href="http://apidocs.slicer.org/master/classvtkMRMLDisplayNode.html#a62cff2549fe8c0c4fbff5b363031e242">AddViewNodeID</a> for each 3D view you want to display it in.</p>

---
