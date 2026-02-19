---
topic_id: 2430
title: "Observe Gui Table Updates In Python"
date: 2018-03-26
url: https://discourse.slicer.org/t/2430
---

# Observe GUI table updates in Python

**Topic ID**: 2430
**Date**: 2018-03-26
**URL**: https://discourse.slicer.org/t/observe-gui-table-updates-in-python/2430

---

## Post #1 by @fuantomu (2018-03-26 19:50 UTC)

<p>Hello,<br>
I’ve searched and tried for several hours now but I can’t seem to figure this out. I use  vtkMRMLTableNode for the table and qMRMLTableView for the GUI. How can I add an observer to the table that reacts on adding/modifying values in the cells. The only thing I found is ReferenceModifiedEvent in the vtkMRMLTableViewNode, but I couldn’t get that one to work.<br>
Also, another question I had regarding tables are column types. I set the type of one of my columns to 1 (which as I understand it is a bool) but I don’t know how to change the cell values in the code now (SetCellText returns errors)</p>
<p>I hope you can understand my problem and thanks in advance for any help!</p>

---

## Post #2 by @lassoan (2018-03-26 21:22 UTC)

<p>What you described should work. Could you send a link to your source code?</p>

---

## Post #3 by @fuantomu (2018-03-26 22:13 UTC)

<p><a href="https://pastebin.com/raw/pXRf2aVD" class="onebox" target="_blank" rel="nofollow noopener">https://pastebin.com/raw/pXRf2aVD</a></p>
<p>This is the code I use for the table</p>

---

## Post #4 by @lassoan (2018-03-27 00:43 UTC)

<p>It seems that you try to create a point list widget. There is already such widget, with lots of features and configuration options: <a href="http://apidocs.slicer.org/master/classqSlicerSimpleMarkupsWidget.html">qSlicerSimpleMarkupsWidget</a>.</p>
<pre><code># Create a markup fiducial list
fidNode=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode")
fidNode.CreateDefaultDisplayNodes()
fidNode.AddFiducial(35,10,12)
fidNode.AddFiducial(15,0,5)
fidNode.AddFiducial(0,0,3)
# Create a list widget
fidListWidget=slicer.qSlicerSimpleMarkupsWidget()
fidListWidget.setMRMLScene(slicer.mrmlScene)
fidListWidget.jumpToSliceEnabled = True
fidListWidget.setCurrentNode(fidNode)
fidListWidget.show()
</code></pre>
<p>In your code the main issue was the you’ve observed the wrong event. This will work:</p>
<pre><code># Create table node
tableNode =  slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTableNode")
col=tableNode.AddColumn()
col.SetName('Name')
col=tableNode.AddColumn()
col.SetName('Visible')
col=tableNode.AddColumn(vtk.vtkFloatArray())
col.SetName('Number')
tableNode.SetColumnType('Visible',vtk.VTK_BIT)
tableNode.AddEmptyRow()
tableNode.AddEmptyRow()
tableNode.AddEmptyRow()
tableNode.SetCellText(1,0,"ok")
tableNode.SetCellText(1,1,"1")

# Table view
tableView=slicer.qMRMLTableView()
tableView.setMRMLScene(slicer.mrmlScene)
tableView.setMRMLTableNode(tableNode)
tableView.show()

# Observe modifications

def tableModified(caller, event):
  print("Table modified")

observerTag = tableNode.AddObserver(vtk.vtkCommand.ModifiedEvent, tableModified)</code></pre>

---

## Post #5 by @fuantomu (2018-03-27 12:09 UTC)

<p>Oh wow, I didn’t know there was something like that already. Thanks a lot! I will probably implement it later but for now I’ll try to get a better understanding first.<br>
On a side node: Is it possible to get the row id that was modified via calldata or a similar function to slicer.clickedMarkupIndex? vtk.VTK_INT seems to crash slicer when calling the tableModified function.</p>

---

## Post #6 by @lassoan (2018-03-27 13:04 UTC)

<aside class="quote no-group" data-username="fuantomu" data-post="5" data-topic="2430">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/8c91f0/48.png" class="avatar"> fuantomu:</div>
<blockquote>
<p>Is it possible to get the row id that was modified</p>
</blockquote>
</aside>
<p>See these examples:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_a_notification_if_a_markup_point_position_is_modified" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_a_notification_if_a_markup_point_position_is_modified</a></p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Manipulating_objects_in_the_slice_viewer" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Manipulating_objects_in_the_slice_viewer</a></p>

---

## Post #7 by @fuantomu (2018-03-27 17:14 UTC)

<p>Thank you very much - I ended up using the widget you suggested and everything is working fine now <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
