---
topic_id: 2910
title: "Load Table From Txt Format"
date: 2018-05-23
url: https://discourse.slicer.org/t/2910
---

# Load table from txt format

**Topic ID**: 2910
**Date**: 2018-05-23
**URL**: https://discourse.slicer.org/t/load-table-from-txt-format/2910

---

## Post #1 by @Davide_Punzo (2018-05-23 15:42 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>what is the syntax for a table in txt format to be properly loaded?</p>
<p>For example I have this table <a href="https://www.dropbox.com/s/eqwrs03bohn4bs4/WEIN069_cat.txt?dl=0" rel="nofollow noopener">https://www.dropbox.com/s/eqwrs03bohn4bs4/WEIN069_cat.txt?dl=0</a><br>
and it will loaded as only one column (also in the case that I remove the first 4 lines).</p>
<p>Has the syntax to follow strict rules? and in that case is there anywhere some documentation or example that shows the syntax?</p>
<p>Or instead is it possible to give to the table reader which is the separator between columns, etc…?</p>

---

## Post #2 by @dzenanz (2018-05-23 15:47 UTC)

<p>Slicer supports tab separated values (.tsv) and comma separated values (.csv). Import your text file into a spreadsheet program using fixed-width columns, then save it as either a CSV or TSV.</p>

---

## Post #3 by @lassoan (2018-05-23 16:13 UTC)

<p>If you need to read such files regularly then reading of such text files could be implemented in VTK CSV file reader (vtkDelimitedTextReader) and exposed in Slicer.</p>

---

## Post #4 by @Davide_Punzo (2018-05-24 08:27 UTC)

<p>Ok, thanks for the info</p>

---
