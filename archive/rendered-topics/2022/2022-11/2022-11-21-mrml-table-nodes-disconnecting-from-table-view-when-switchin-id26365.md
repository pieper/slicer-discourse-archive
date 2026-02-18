# MRML table nodes disconnecting from table view when switching layouts

**Topic ID**: 26365
**Date**: 2022-11-21
**URL**: https://discourse.slicer.org/t/mrml-table-nodes-disconnecting-from-table-view-when-switching-layouts/26365

---

## Post #1 by @StephenCrowell (2022-11-21 21:33 UTC)

<p>In my scripted module, I have two mrml table nodes saved as variables. When data is loaded from a server,  the table nodes are modified and the changes are displayed. This works normally until the user switches to another module and back to my module. The table nodes still exist inside slicer; however, the table displays no data and the table views’ table node is set to None. The code can for table node creation and connection to the table view can be found <a href="https://github.com/stephencrowell/SlicerEHRSandbox/blob/7aa1fd7c64336143efeb37cb5c71f9fe76d04810/FHIRReader/FHIRReader.py#L186" rel="noopener nofollow ugc">here</a>.</p>
<p>My first question is this intended functionality or is the way I am using table nodes incorrect?</p>
<p>I was able to find a workaround for this issue by using the <code>enter</code> function to reconnect the table node to the table view. Assuming the interaction described above is intended, is this the proper way to handle table node re-connection?</p>
<p>Below is a small script you can run to reproduce this issue.</p>
<pre><code class="lang-auto">    layoutManager = slicer.app.layoutManager()
    layoutManager.setLayout(35)
    
    table_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTableNode")
    table_node.SetName("TestName")
    
    col1 = vtk.vtkStringArray()
    col1.SetName("Column 1")
    col1.InsertNextValue("Test1")
    
    col2 = vtk.vtkStringArray()
    col2.SetName("Column 2")
    col2.InsertNextValue("Test2")
    
    table_node.AddColumn(col1)
    table_node.AddColumn(col2)
    
    layoutManager.tableWidget(0).tableView().setMRMLTableNode(table_node)
</code></pre>

---

## Post #2 by @StephenCrowell (2022-11-28 20:49 UTC)

<p>Updated the script and added two images showing the expected table and actual table after the layout switch.</p>
<pre data-code-wrap="python"><code class="lang-python">layoutManager = slicer.app.layoutManager()
layoutManager.setLayout(slicer.vtkMRMLLayoutNode.SlicerLayout3DTableView)

table_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTableNode")
table_node.SetName("TestName")

col1 = vtk.vtkStringArray()
col1.SetName("Column 1")
col1.InsertNextValue("Test1")

col2 = vtk.vtkStringArray()
col2.SetName("Column 2")
col2.InsertNextValue("Test2")

table_node.AddColumn(col1)
table_node.AddColumn(col2)

layoutManager.tableWidget(0).tableView().setMRMLTableNode(table_node)

# Switch to a layout without table view
layoutManager.setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutCompareGridView)

# Switch back to a layout with the table view
layoutManager.setLayout(slicer.vtkMRMLLayoutNode.SlicerLayout3DTableView)
</code></pre>
<div class="md-table">
<table>
<thead>
<tr>
<th>Expected</th>
<th>Actual</th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1747e5d470a0f0a4d319a9baf27bd018f66b51a.png" data-download-href="/uploads/short-url/wat14lNNKSHS6NT2TKYP7FXCucq.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e1747e5d470a0f0a4d319a9baf27bd018f66b51a_2_581x500.png" alt="image" data-base62-sha1="wat14lNNKSHS6NT2TKYP7FXCucq" width="581" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e1747e5d470a0f0a4d319a9baf27bd018f66b51a_2_581x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1747e5d470a0f0a4d319a9baf27bd018f66b51a.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1747e5d470a0f0a4d319a9baf27bd018f66b51a.png 2x" data-dominant-color="FDFCFA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">689×592 5.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></td>
<td></td>
</tr>
</tbody>
</table>
</div>

---

## Post #3 by @lassoan (2022-12-01 06:31 UTC)

<p>Thank you, this script made it very easy to reproduce the unexpected behavior and see what was wrong.</p>
<p>This line accesses a low-level widget property and changes which table is shown in the table view:</p>
<pre><code>layoutManager.tableWidget(0).tableView().setMRMLTableNode(table_node)
</code></pre>
<p>However, this property is controlled by nodes in the scene. As soon as the window is refreshed, the property is set again from the scene.</p>
<p>You need to set the displayed node in the table view node like this:</p>
<pre><code> layoutManager.tableWidget(0).tableView().mrmlTableViewNode().SetTableNodeID(table_node.GetID())
</code></pre>
<p>The syntax could be a bit simpler, but the <code>mrmlTableViewNode</code> method was not exposed in the table widget. I’ve updated the Python wrapping and from tomorrow this will work, too (in Slicer Preview Releases):</p>
<pre><code>layoutManager.tableWidget(0).mrmlTableViewNode().SetTableNodeID(table_node.GetID())
</code></pre>

---

## Post #4 by @StephenCrowell (2022-12-01 19:46 UTC)

<p>That solves the issue perfectly. Thanks!</p>

---
