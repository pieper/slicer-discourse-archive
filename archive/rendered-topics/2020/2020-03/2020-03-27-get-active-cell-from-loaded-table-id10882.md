# Get active cell from loaded table

**Topic ID**: 10882
**Date**: 2020-03-27
**URL**: https://discourse.slicer.org/t/get-active-cell-from-loaded-table/10882

---

## Post #1 by @smrolfe (2020-03-27 23:38 UTC)

<p>I’d like to access the active (highlighted) cell in a table in the MRML scene from the Python interactor. I thought this property might be in the vtkMRMLTableNode or vtkMRMLTableViewNode. Is there someplace else I should look? Thanks!</p>

---

## Post #2 by @lassoan (2020-03-28 01:53 UTC)

<p>You can get selected column indices using <a href="http://apidocs.slicer.org/master/classqMRMLTableView.html#a28f7ca3bf653ed03342789ad348f19b9">qMRMLTableView::selectedMRMLTableColumnIndices()</a>`. Feel free to add more methods (for example to return (row,col) indices, or use more Python-friendly return types) and send a pull request.</p>
<p>Table view also has a <code>selectionChanged()</code> signal that you can observe to get notified when selection is changed.</p>

---

## Post #3 by @smrolfe (2020-03-28 03:11 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>. I can get the qMRMLTableView when I instantiate the widget, could you explain how to get it from the scene?</p>

---

## Post #4 by @lassoan (2020-03-28 21:57 UTC)

<p>Would you like to access a table view that is in the view layout?</p>
<p>You can access it by calling <code>slicer.app.layoutManager().tableWidget(0).tableView()</code>.</p>

---

## Post #5 by @smrolfe (2020-03-30 15:18 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>! This works perfectly.</p>

---
