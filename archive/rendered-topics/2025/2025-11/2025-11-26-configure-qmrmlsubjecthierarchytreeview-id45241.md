# Configure qMRMLSubjectHierarchyTreeView?

**Topic ID**: 45241
**Date**: 2025-11-26
**URL**: https://discourse.slicer.org/t/configure-qmrmlsubjecthierarchytreeview/45241

---

## Post #1 by @mau_igna_06 (2025-11-26 16:45 UTC)

<p>Hi,</p>
<p>Is it possible to hide all empty folders and markupNodes with no control points from a qMRMLSubjectHierarchyTreeView ?</p>
<p>Thank you</p>

---

## Post #2 by @cpinter (2025-12-01 09:42 UTC)

<blockquote>
<p>Is it possible to hide all empty folders</p>
</blockquote>
<p>You can use the <code>showEmptyHierarchyItems</code> property in the proxy model.</p>
<blockquote>
<p>markupNodes with no control points</p>
</blockquote>
<p>I’d probably change the default markup node to have a certain attribute, and then when a control point is added, remove that attribute (or change the value). Use it in conjunction with <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/SubjectHierarchy/Widgets/qMRMLSubjectHierarchyTreeView.h#L96">excludeNodeAttributeNamesFilter</a></p>

---
