---
topic_id: 11530
title: "Pop Value From Table"
date: 2020-05-13
url: https://discourse.slicer.org/t/11530
---

# Pop value from table

**Topic ID**: 11530
**Date**: 2020-05-13
**URL**: https://discourse.slicer.org/t/pop-value-from-table/11530

---

## Post #1 by @PaoloZaffino (2020-05-13 21:16 UTC)

<p>Hi all,<br>
I havev a question about table.<br>
I have a table with two columns and I want to pop the last value, shift all the elements and insert a new value just for a single column.<br>
Basically I need to have always the same number of rows, but I want to add a new value and removing the last one.<br>
Which is the most efficient way to do this?</p>
<p>Thanks a lot!<br>
Paolo</p>

---

## Post #2 by @Davide_Punzo (2020-05-14 14:49 UTC)

<p>The columns of a table are vtk arrays.</p>
<p>For example, in the documentation <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Plots" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Plots</a> are vtkFloatArray.</p>
<p>The vtk arrays should have an InsertTuple method, which should insert the new value at a certain index, see (<a href="https://vtk.org/doc/nightly/html/classvtkDataArray.html#a00d044d0893988ffc753e86fc5247ba8" rel="nofollow noopener">https://vtk.org/doc/nightly/html/classvtkDataArray.html#a00d044d0893988ffc753e86fc5247ba8</a> <a href="https://vtk.org/doc/nightly/html/classvtkDataArray.html#af545503feb6c030a851f824d937e9869" rel="nofollow noopener">https://vtk.org/doc/nightly/html/classvtkDataArray.html#af545503feb6c030a851f824d937e9869</a>).</p>
<p>For removing the last value, you can use the Resize method.</p>
<p>P.S.: you get the column with the method GetColumn from  table = tableNode.GetTable(). After modifying the vtk array, for updating the table and plot, you need to call table.Modify().</p>

---
