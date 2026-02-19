---
topic_id: 14189
title: "How To Change The Format Of The Column And Celltext Of A Tab"
date: 2020-10-21
url: https://discourse.slicer.org/t/14189
---

# How to change the format of the Column and CellText of a table

**Topic ID**: 14189
**Date**: 2020-10-21
**URL**: https://discourse.slicer.org/t/how-to-change-the-format-of-the-column-and-celltext-of-a-table/14189

---

## Post #1 by @jj31 (2020-10-21 17:00 UTC)

<p>I would like to change the format of the font (bold, size, family, etc) for both the title and the CellText of a TableNode. I would also like to fix the width of the Table (something like Column width).  Using the lines below, I can define the text for the column and the rows. However, I haven’t been able to figure out how to adjust the format. Any suggestions?</p>
<p>slicer.vtkMRMLTableNode().AddColumn().SetName(“column text”)<br>
slicer.vtkMRMLTableNode().SetCellText(0,0,“row text”)</p>

---

## Post #2 by @lassoan (2020-10-21 17:15 UTC)

<p>Table nodes can store name, type, and additional metadata (description, unit, null value, any other custom field).</p>
<p>Table widget (<code>slicer.qMRMLTableWidget</code>) currently does not support any formatting, such as font type or size, but since you can store arbitrary column metadata, this would not be very hard to implement.</p>
<p>For cell-level custom formatting, probably the best approach would be to introduce a new html or markdown data type, which would be rendered using QTextDocument (see <a href="https://stackoverflow.com/questions/1956542/how-to-make-item-view-render-rich-html-text-in-qt">1</a> or <a href="https://www.codesd.com/item/how-to-make-qtableview-fast-with-html-formatted-and-clickable-cells.html">2</a> for examples).</p>
<p>If you decide to work on implementing any of these then we can help you getting started and reviewing and integrating the end result. If you want to rich table display without any Slicer core development, then you can simple create a table in html and display it using slicer.qSlicerWebWidget.</p>

---

## Post #3 by @jj31 (2020-10-23 00:25 UTC)

<p>Thanks, Andras. I will look into these examples in more detail and get back if I need any help.</p>

---
