# Change editortrigger using subjectHierarchyItemFlags()

**Topic ID**: 35425
**Date**: 2024-04-11
**URL**: https://discourse.slicer.org/t/change-editortrigger-using-subjecthierarchyitemflags/35425

---

## Post #1 by @zina (2024-04-11 05:43 UTC)

<p>Operating system: windows 10<br>
Slicer version:5.6.1 r32438 / 117ce5f<br>
Expected behavior:<br>
Actual behavior:<br>
I have only qMRMLSubjectHierarchyTreeView( not a widget) I have to change edit enable for some rows , leaving other no editable.<br>
I know I have to set flag something  like this:<br>
caliper_row.setFlags(caliper_row.flags() | qt.ItemIsEditable), if I would have widget. But in my case, I probably have to use ui.caliper_subject_hierarchy.model().qMRMLSubjectHierarchyTreeView but :1) it did not recognize this function 2) how to set flag in it. If somebody have example, it will help.</p>

---
