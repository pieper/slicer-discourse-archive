---
topic_id: 7051
title: "Popup Table Selection Change"
date: 2019-06-06
url: https://discourse.slicer.org/t/7051
---

# Popup table selection change

**Topic ID**: 7051
**Date**: 2019-06-06
**URL**: https://discourse.slicer.org/t/popup-table-selection-change/7051

---

## Post #1 by @holmesrb (2019-06-06 11:39 UTC)

<p>I am developing an extension to display the results of some neuro image processing which involves reading a CSV file into a table. I need the table to be a popup and the following code snippet from the slicer website does this:</p>
<pre><code>slicer.util.loadNodeFromFile(selectedTableFile, "TableFile", {})        
tableModuleWidget = slicer.modules.tables.createNewWidgetRepresentation()
tableModuleWidget.setMRMLScene(slicer.app.mrmlScene())
tableModuleWidget.show()  
</code></pre>
<p>What I want to do next is to detect a table selection change and return the contents of column 1 of the newly selected row. I can then load a particular image based on the cell contents.</p>
<p>If I create a table node which is part of the main UI I can read a CSV file and populate the table easiliy enough and then run code when the table selection is changed using the line below. This does not work for the tableModuleWidget as created above. Is there a way to do this please?</p>
<p>self.roiTable.itemSelectionChanged.connect(lambda: self.roiTableSelectionChange())</p>
<p>Many thanks</p>

---

## Post #2 by @lassoan (2019-06-06 13:00 UTC)

<p><code>createnewwidgetrepresentation</code> should not be used by modules, as module widgets are usually implemented so that they assume that there is only a single instance of them.</p>
<p>Instead, you can use a <code>slicer.qMRMLTableView()</code> or maybe a <code>slicer.qMRMLTableWidget()</code>. However, in general, I would advise against popups, as it disrupts the user’s workflow, and instead display the table in your module widget, in the view layout (either choose an existing layout that already has a table view in it, or define a new custom layout), or at least put the widget in a dockable window and dock it somewhere in the application window (for example, see <a href="https://github.com/SlicerRt/SlicerDebuggingTools/tree/master/NodeInfo">NodeInfo module</a> in DebuggingTools extension).</p>
<aside class="quote no-group" data-username="holmesrb" data-post="1" data-topic="7051">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/holmesrb/48/1825_2.png" class="avatar"> holmesrb:</div>
<blockquote>
<p>What I want to do next is to detect a table selection change and return the contents of column 1 of the newly selected row</p>
</blockquote>
</aside>
<p>For developers’ convenience, a simple <code>selectionChanged()</code> signal has been added to the table <code>qMRMLTableView</code> that you can connect to callback functions. Also, <code>qMRMLTableView</code> is a <a href="https://doc.qt.io/qt-5/qtableview.html"><code>QTableView</code></a>, so you can connect callbacks to selection model changes as you would do on any regular QTableView object.</p>
<p>Jumping to segment based when a table table cell is selected is implemented in <a href="https://github.com/QIICR/QuantitativeReporting/blob/master/QuantitativeReporting/QuantitativeReporting.py">QuantitativeReporting extension</a>, you can use that as an example.</p>

---

## Post #3 by @holmesrb (2019-06-08 15:09 UTC)

<p>Many thanks for the quick response - that works very well.</p>

---
