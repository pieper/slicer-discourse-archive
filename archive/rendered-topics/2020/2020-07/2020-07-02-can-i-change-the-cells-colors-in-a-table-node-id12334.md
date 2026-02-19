---
topic_id: 12334
title: "Can I Change The Cells Colors In A Table Node"
date: 2020-07-02
url: https://discourse.slicer.org/t/12334
---

# Can I change the cells colors in a table node?

**Topic ID**: 12334
**Date**: 2020-07-02
**URL**: https://discourse.slicer.org/t/can-i-change-the-cells-colors-in-a-table-node/12334

---

## Post #1 by @Fernando (2020-07-02 09:11 UTC)

<p>Hi all,</p>
<p>I would like to set custom background and font colors in the cells of my table, to get something like <a href="https://support.microsoft.com/en-us/office/use-conditional-formatting-to-highlight-information-fed60dfa-1d3f-4e13-9ecb-f1951ff89d7f" rel="nofollow noopener">conditional formatting</a> in MS Excel. Is this possible? I’ve been looking into the docs for <a href="https://vtk.org/doc/nightly/html/classvtkTable.html" rel="nofollow noopener"><code>vtkTable</code></a>, but couldn’t find anything useful.</p>

---

## Post #2 by @Fernando (2020-07-02 09:16 UTC)

<p>Also, vaguely related to this topic: is there any event I can monitor for “cell clicked”?</p>

---

## Post #3 by @mikebind (2021-03-26 16:49 UTC)

<p>I would like to know the answer to Fernando’s question as well.</p>
<p>As an alternative, you can get some of this functionality with a Qt QTableWidget.  Specifically, you can connect the ‘cellClicked(int,int)’ signal on a QTableWidget with a callback, where the ints are the row and column of the clicked cell of the table.  You can control the background color and choose from a couple shading patterns of QTableWidgetItem (the widgets that go in QTableWidget cells) using QBrush.  I went down this road on a project, but I have not been able to figure out how to capture a right-click on the table cells using Qt, which is keeping me from being able to add some much-desired features.</p>
<p>If there are other approaches out there that people have used, I’d appreciate hearing about them. Thanks!</p>

---

## Post #4 by @lassoan (2021-03-26 17:29 UTC)

<p>qMRMLTableView is publicly inherits from QTableView, so you have access to the full Qt API, can get notifications about selection change, recolor items, etc.</p>
<p>While getting any information is always safe, changing information in the table at Qt level can cause inconsistency between MRML and the Qt widget. If you only make modifications that the qMRMLTableView does not care about (e.g., change of background colors) then there should be no harmful interference.</p>
<p>If it turns out that there are some commonly needed features that are not easy to implement (or not practical to maintain) in external code then we can add that to the qMRMLTableView.</p>
<ul>
<li>Cell clicked (selection change): it is easy to connect to signals of the selection model from outside code, so there should not be a pressing need to add this to the qMRMLTableView API. However, if you think that it is too complicated then we can expose simplified signals in qMRMLTableView.</li>
<li>Custom formatting (background color, font, etc.) for an entire column would be relatively easy to implement in tables, because we can already store arbitrary per-column metadata, but I’m not sure how commonly needed feature is this.</li>
<li>Conditional formatting: It should not be too hard to implement this in external code (when the table node is modified then run through the cells and adjust item properties in the table view). A narrow version of this could be added into a display node, where colormaps could map cell values to font or cell background colors (and maybe other lookup tables could be added for setting font size, etc.). This would probably take 1-2 weeks to implement.</li>
</ul>
<p>You can add any of these ideas as feature requests and see how many <a href="https://discourse.slicer.org/t/about-the-feature-requests-category/30">votes</a> they collect and we’ll prioritize them accordingly.</p>

---

## Post #5 by @mikebind (2021-03-26 18:18 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> .  Do you have suggestions for how to capture right-clicks on table cells?  I’d like to use this to spawn a context menu that allowed various actions (tagging a cell with a label, jumping slices to an associated location, etc).  I think I can handle the rest of the coding if I can detect that a click was a right-click and what table cell was clicked on (row index and column index would be sufficient).  I had already implemented that left-clicking on a cell triggered jumping slice viewers to an associated location, but I would really like to implement some other options when interacting with the table, and having right-clicking give a menu of options seems like a natural way to do that to me, but I have been stuck because I have not been able to figure out in the Qt documentation how to detect a right-click specifically (cellClicked seems to respond to any kind of click).</p>

---

## Post #6 by @pieper (2021-03-26 19:39 UTC)

<p>You might need to catch the right click event using lower level qwidget event filters and then find the cell manually.  I’m not sure you can do that with PythonQt, but could probably add it cleanly t the C++ code with an event filter.</p>

---

## Post #7 by @mikebind (2021-03-26 21:47 UTC)

<p>Thanks for the suggestions.  I managed to find the right google terms today and found this very helpful link: <a href="https://wiki.python.org/moin/PyQt/Handling%20context%20menus" class="inline-onebox" rel="noopener nofollow ugc">PyQt/Handling context menus - Python Wiki</a></p>
<p>Based on that, I was able to figure out the first step to capturing what I want by the following:</p>
<pre><code>tableWidget = qt.QTableWidget
tableWidget.setContextMenuPolicy(qt.Qt.CustomContextMenu)
tableWidget.customContextMenuRequested.connect(self.onTableContextMenuRequest)
</code></pre>
<p>After this, when the user right-clicks in the table, self.onTableContextMenuRequest() is called with the position of the click within the table widget as arguments.  Next step will be to find the table cell at that location and display a context menu at that location, which I think I can figure out how to do.</p>
<p>Thanks for the help!</p>

---

## Post #8 by @pieper (2021-03-26 22:24 UTC)

<p>Looks like you are on the right track!</p>

---

## Post #10 by @lassoan (2021-03-26 22:35 UTC)

<p>You can find several examples for this in Slicer source code. You can get the item by calling <code>QModelIndex index = this-&gt;indexAt(point)</code>.</p>

---
