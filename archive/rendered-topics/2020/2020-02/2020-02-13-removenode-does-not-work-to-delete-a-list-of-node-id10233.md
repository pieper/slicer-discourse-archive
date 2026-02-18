# RemoveNode does not work to delete a list of node

**Topic ID**: 10233
**Date**: 2020-02-13
**URL**: https://discourse.slicer.org/t/removenode-does-not-work-to-delete-a-list-of-node/10233

---

## Post #1 by @tbuikr (2020-02-13 02:28 UTC)

<p>I have two buttons: <code>Add</code> and <code>Delete</code>. The <code>Add</code> uses to add a node, while the <code>Delete</code> is for node removing. The <code>Add</code> function is implemented as follows:</p>
<pre><code class="lang-auto">self.roiNodes =[]
for i in range (10):
    node = slicer.vtkMRMLAnnotationROINode()
    node.SetXYZ(0, 0, 0)
    node.SetRadiusXYZ(25, 25, 25)
    node.Initialize(slicer.mrmlScene)
    node.SetName("A")            
    self.node_list.append(node)
</code></pre>
<p>The delete function will delete the node base on the seletected row in the table (10 rows)</p>
<pre><code class="lang-auto">slicer.mrmlScene.RemoveNode(self.node_list[self.table.currentRow()])
self.table.removeRow(self.table.currentRow())
self.node_list.pop(self.table.currentRow())
</code></pre>
<p>The add function works well, while the delete function does not work. Any wrong implementation in my code? Thanks</p>

---

## Post #2 by @lassoan (2020-02-13 02:39 UTC)

<p>There is no way we can determine where the problem is without seeing all the source code that is involved. If you cannot share tour module’s source code then create a self-contained script that reproduces the unexpected behavior.</p>

---

## Post #3 by @jamesobutler (2020-02-13 02:55 UTC)

<p>Only thing I could guess from your snippet is that the current row in <code>self.node_list.pop(self.table.currentRow())</code> is no longer the same as the above lines because you removed the table row in the line above.</p>

---
