# Populating qMRMLSubjectHierarchyTreeView

**Topic ID**: 10776
**Date**: 2020-03-22
**URL**: https://discourse.slicer.org/t/populating-qmrmlsubjecthierarchytreeview/10776

---

## Post #1 by @Joshua_Jacobs (2020-03-22 02:52 UTC)

<p>I am writing an extension to display objects in a tree hierarchy from a nested python dictionary.</p>
<p>Is there a good guide for presenting nodes to the Subject Hierarchy Tree View with icons, data, context menus, and so forth?</p>
<p>Thank You,</p>
<p>Josh J</p>

---

## Post #2 by @cpinter (2020-03-22 10:45 UTC)

<p>Subject hierarchy automatically imports any supported nodes. This support is provided by subject hierarchy plugins. They determine what node they can own, what icon it will have, how they are displayed, and what functions they offer through context menus. If some existing plugins interfere with your plans, then you may choose a higher confidence when deciding ownership, or you can even disable plugins. You can find more information here:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Data#Information_for_Developers" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Modules/Data#Information_for_Developers</a></p>

---

## Post #3 by @Joshua_Jacobs (2020-03-22 13:36 UTC)

<p>Gotcha.</p>
<p>I have a datastore with a different hierarchy that I am working to write a Slicer plugin interface for.  Looks like I may need to think a bit more about how it will interface with the various Slicer hierarchies.</p>
<p>Thank You,</p>
<p>J.</p>

---
