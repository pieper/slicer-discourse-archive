# qMRMLSubjectHeirarchyTreeView customization

**Topic ID**: 24619
**Date**: 2022-08-03
**URL**: https://discourse.slicer.org/t/qmrmlsubjectheirarchytreeview-customization/24619

---

## Post #1 by @priya.vada4 (2022-08-03 14:17 UTC)

<p>Hi</p>
<p>I am interested in using the qMRMLSubjectHeirarchyTree widget as part of my module to list the mrmlmodelnodes in the scene with the inbuilt features of enabling visibility and changing color. Would it be possible to add a custom field to this widget to display the results of certain computations specific for each model programmatically.</p>
<p>I see that there is a “Description” field as part of the widget. I am able to modify the contents of the Description column for each model through the GUI. Could someone let me know how I could change this field programmatically to display the results of the computation for each model listed in the tree.</p>
<p>Thanks<br>
Priya</p>

---

## Post #2 by @Sunderlandkyl (2022-08-03 15:48 UTC)

<p>You could try modifying the underlying model to add additional columns to the view. I’m not sure how well it would work with the qMRMLSubjectHierarchyModel.</p>
<p>The value in the description column can be changed with:</p>
<pre><code class="lang-auto">node.SetDescription("XYZ")
</code></pre>

---
