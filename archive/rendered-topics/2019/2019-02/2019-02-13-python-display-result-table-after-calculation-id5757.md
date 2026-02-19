---
topic_id: 5757
title: "Python Display Result Table After Calculation"
date: 2019-02-13
url: https://discourse.slicer.org/t/5757
---

# Python: display result Table after calculation

**Topic ID**: 5757
**Date**: 2019-02-13
**URL**: https://discourse.slicer.org/t/python-display-result-table-after-calculation/5757

---

## Post #1 by @Alex_Vergara (2019-02-13 16:07 UTC)

<p>Is there a way to display the result table by default?<br>
I have created it but it is hidden by default, I must go to Data module and open the eye manually. I want to do this in my python script. The table shall be displayed in the tables widget.</p>
<p>If I try to force by widget logic this happens</p>
<pre><code class="lang-python">&gt;&gt;&gt; slicer.qMRMLTableWidget().setMRMLTableViewNode(tablenode)
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
TypeError: method requires a vtkMRMLTableViewNode, a vtkMRMLTableNode was provided.
</code></pre>
<p>And there is nothing like setMRMLTableNode.</p>

---

## Post #2 by @Alex_Vergara (2019-02-13 18:09 UTC)

<p>I also tried the following:</p>
<pre><code class="lang-python">&gt;&gt;&gt; tableview = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLTableViewNode')
&gt;&gt;&gt; tableview.SetTableNodeID(tablenode.GetID())
&gt;&gt;&gt; slicer.qMRMLTableWidget().setMRMLTableViewNode(tableview)
&gt;&gt;&gt; slicer.mrmlScene.AddNode(tableview)
(MRMLCorePython.vtkMRMLTableViewNode)0x124ee34c8
</code></pre>
<p>but still nothing</p>

---

## Post #3 by @Alex_Vergara (2019-02-14 09:47 UTC)

<p>This example shos how to do this with plots (<a href="https://gist.github.com/hherhold/0492146f70ef0fc511b7b21410264481" rel="nofollow noopener">https://gist.github.com/hherhold/0492146f70ef0fc511b7b21410264481</a>) but I want to do it with tables<br>
I tried the equivalent procedure but it does not work: The tableWidget.mrmlTableViewNode() method does not exists. It has however the tableWidget.setMRMLTableViewNode(), but no way to get it.<br>
What am I missing here?</p>

---

## Post #4 by @Alex_Vergara (2019-02-14 10:08 UTC)

<p>This was harder than I thought, but finally came to a working code:</p>
<pre><code class="lang-python">    # Creation of your table
    resultsTableNode = (...)
    # Create the layout manager to show the table
    layoutManager = slicer.app.layoutManager()
    layoutTable = slicer.modules.tables.logic().GetLayoutWithTable(layoutManager.layout)
    layoutManager.setLayout(layoutTable)
    # Create the table widget and assign the table
    tablewidget = layoutManager.tableWidget(0)
    tableview = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLTableViewNode')
    tableview.SetTableNodeID(resultsTableNode.GetID())
    tablewidget.setMRMLTableViewNode(tableview)
</code></pre>

---

## Post #5 by @Alex_Vergara (2019-02-14 10:37 UTC)

<p>Hmm, If I call this repetitively with another table it does not work, it creates more tableviews but the tablewidget is not refreshed.  So I keep researching</p>

---

## Post #6 by @Alex_Vergara (2019-02-14 11:24 UTC)

<p>Deep, very deep in the Slicer source code, there is the SegmentStatistic module which contains the answer, it is obscured</p>
<pre><code class="lang-python">def showTable(self, table):
    """
    Switch to a layout where tables are visible and show the selected table
    """
    currentLayout = slicer.app.layoutManager().layout
    layoutWithTable = slicer.modules.tables.logic().GetLayoutWithTable(currentLayout)
    slicer.app.layoutManager().setLayout(layoutWithTable)
    slicer.app.applicationLogic().GetSelectionNode().SetActiveTableID(table.GetID())
    slicer.app.applicationLogic().PropagateTableSelection()
</code></pre>

---

## Post #7 by @lassoan (2019-02-14 13:29 UTC)

<p>You can also use <code>slicer.modules.plots.logic().ShowChartInLayout(plotChartNode)</code> as shown in this example in script repository: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_histogram_plot_of_a_volume" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_histogram_plot_of_a_volume</a></p>

---

## Post #8 by @Alex_Vergara (2019-02-14 14:46 UTC)

<p>What do you mean? Is this also working with table nodes?</p>

---

## Post #9 by @lassoan (2019-02-14 16:28 UTC)

<p>You are right, it’s only for charts, the same kind of <a href="https://github.com/Slicer/Slicer/blob/e18cc7b6df0df3c6626aff8b80568ab75695f580/Modules/Loadable/Plots/Logic/vtkSlicerPlotsLogic.cxx#L107-L137" rel="nofollow noopener">“show” utility function</a> could be added to tables module logic.</p>

---
