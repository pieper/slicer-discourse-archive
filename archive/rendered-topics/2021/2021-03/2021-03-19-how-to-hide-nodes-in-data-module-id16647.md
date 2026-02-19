---
topic_id: 16647
title: "How To Hide Nodes In Data Module"
date: 2021-03-19
url: https://discourse.slicer.org/t/16647
---

# How to hide nodes in data module

**Topic ID**: 16647
**Date**: 2021-03-19
**URL**: https://discourse.slicer.org/t/how-to-hide-nodes-in-data-module/16647

---

## Post #1 by @akshay_pillai (2021-03-19 16:27 UTC)

<p>Operating system: windows 10<br>
Slicer version: 4.11</p>
<p>Is there any way to programmatically toggle the visibility of nodes in the data module? If so , how?</p>

---

## Post #2 by @Sunderlandkyl (2021-03-19 17:58 UTC)

<p>You can use the SetDisplayVisibility() function. If you want finer control over display options, you can access the display node with GetDisplayNode().</p>
<p>vtkMRMLDisplayableNode doc:<br>
<a href="https://apidocs.slicer.org/master/classvtkMRMLDisplayableNode.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://apidocs.slicer.org/master/classvtkMRMLDisplayableNode.html</a></p>

---
