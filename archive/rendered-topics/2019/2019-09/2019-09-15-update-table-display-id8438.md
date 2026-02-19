---
topic_id: 8438
title: "Update Table Display"
date: 2019-09-15
url: https://discourse.slicer.org/t/8438
---

# Update Table display?

**Topic ID**: 8438
**Date**: 2019-09-15
**URL**: https://discourse.slicer.org/t/update-table-display/8438

---

## Post #1 by @Amine (2019-09-15 22:32 UTC)

<p>Hi, i used this function to display a table node on the layout but it only works on the first table display, and not when the table is updated (same function as in SegmentStatistics module):</p>
<pre><code>def showTable(table):
    currentLayout = slicer.app.layoutManager().layout
    layoutWithTable = slicer.modules.tables.logic().GetLayoutWithTable(currentLayout)
    slicer.app.layoutManager().setLayout(layoutWithTable)
    slicer.app.applicationLogic().GetSelectionNode().SetActiveTableID(table.GetID())
    slicer.app.applicationLogic().PropagateTableSelection()

table = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTableNode")
table.AddColumn()
table.AddEmptyRow()
table.AddEmptyRow()

table.GetTable().GetColumn(0).SetValue(0, str(58))
table.GetTable().GetColumn(0).SetValue(1, str(20))
showTable(table)
</code></pre>
<p>Up to now it displays fine, then when i update the table there is no response (until i hide and show the table on hiearchy, leading me to think the table is properly updated but doesen’t show up due to some refreshing problem?):</p>
<pre><code>table.GetTable().GetColumn(0).SetValue(0, str(150))
table.GetTable().GetColumn(0).SetValue(1, str(190))
showTable(table)</code></pre>

---

## Post #2 by @lassoan (2019-09-16 02:06 UTC)

<p>What you describe is not a bug but a feature. VTK data objects are optimized for bulk updates.</p>
<p>If you use the VTK API then you need to signal that you have finished all your modifications by calling Modified() on the data object (<code>table.GetTable().Modified()</code>).</p>
<p>Alternatively, you can use convenience functions of the table node, for example <code>table.SetCellText(0, 0, "150")</code>.</p>

---

## Post #3 by @Amine (2019-09-16 02:39 UTC)

<p>Thank you, that worked perfectly.<br>
is there any difference when adding <code>StartModify()</code> and <code>EndModify()</code> as well? as in segment statistics Scripted module (i couldn’t find any documentation concerning it):</p>
<blockquote>
<p>tableWasModified = table.StartModify()<br>
(… modifications…)<br>
table.Modified()<br>
table.EndModify(tableWasModified)</p>
</blockquote>

---

## Post #4 by @lassoan (2019-09-16 02:52 UTC)

<p>By calling Start/EndModify, you can update all table node properties in bulk (not just table values but also node name, column types, etc.).</p>

---

## Post #5 by @Amine (2019-09-16 02:58 UTC)

<p>Then it might be handy too, Thanks for your answer.</p>

---
