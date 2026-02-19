---
topic_id: 19490
title: "Qmrmllistwidget Lists Nodes Of One Type"
date: 2021-09-03
url: https://discourse.slicer.org/t/19490
---

# qMRMLListWidget lists nodes of one type

**Topic ID**: 19490
**Date**: 2021-09-03
**URL**: https://discourse.slicer.org/t/qmrmllistwidget-lists-nodes-of-one-type/19490

---

## Post #1 by @wabwan25 (2021-09-03 04:40 UTC)

<p>I use qtdesigner to create a list widget to list model nodes in the scene, then a user can select multiple items for process.  I use qMRMLListWidget, however, the function setMRMLScene(vtkMRMLScene*) lists all the nodes. How can I configure the widget to only show one type of nodes?  The class has very limited functions, how can i get selected nodes in the list?   Any suggestion to implement multiple selection of nodes of one type?  Thank you very much!</p>

---

## Post #2 by @lassoan (2021-09-03 04:55 UTC)

<p>qMRMLListWidget does not support filtering by node type. Probably you want to use a qMRMLNodeComboBox instead.</p>

---
