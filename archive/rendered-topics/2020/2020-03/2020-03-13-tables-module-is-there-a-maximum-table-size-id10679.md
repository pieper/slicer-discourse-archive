# Tables Module: is there a maximum table size?

**Topic ID**: 10679
**Date**: 2020-03-13
**URL**: https://discourse.slicer.org/t/tables-module-is-there-a-maximum-table-size/10679

---

## Post #1 by @wieke.prummel (2020-03-13 18:39 UTC)

<p>Hi,</p>
<p>I have a question regarding the Tables Module.</p>
<p>I am trying to import an Excel File of size 78x78, but it only displays 78x64…<br>
At first I thought it was only a display default, but when I try to access the data I can’t seem to access all values after rows and columns 64. Is this supposed to happen?</p>
<p>Thank you!</p>
<p>Wieke</p>

---

## Post #2 by @lassoan (2020-03-18 03:25 UTC)

<p>There is no limitation on the number of columns. Maybe your table did not have a unique name (value in first row) for each column.</p>

---

## Post #3 by @wieke.prummel (2020-03-23 19:26 UTC)

<p>Thank you very much! That was indeed the issue!</p>
<p>Does this mean I always have to put a header (first row) by default in order to upload a matrix ?<br>
I added a header with strings and now all the data loads correctly.</p>
<p>Best,<br>
Wieke</p>

---

## Post #4 by @lassoan (2020-03-23 19:29 UTC)

<p>Yes, each column of the table must have a unique, non-empty name.</p>

---
