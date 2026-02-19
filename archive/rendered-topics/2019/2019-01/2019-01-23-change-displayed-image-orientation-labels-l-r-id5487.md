---
topic_id: 5487
title: "Change Displayed Image Orientation Labels L R"
date: 2019-01-23
url: https://discourse.slicer.org/t/5487
---

# Change displayed image orientation labels (L, R, ...)

**Topic ID**: 5487
**Date**: 2019-01-23
**URL**: https://discourse.slicer.org/t/change-displayed-image-orientation-labels-l-r/5487

---

## Post #1 by @ghnguyen (2019-01-23 14:38 UTC)

<p>Hi,</p>
<p>Is there a way to rename the orientation marker in the slice viewports (Not flipping or changing direction, just simply changing the naming system)? I was able to change the names of the axes in the 3D view (e.g. “Anterior” to “Ventral”) and the orientation marker there is updated accordingly but the ones on the slices are not and still have RAS markers.</p>
<p>Thanks,<br>
Giang</p>

---

## Post #2 by @lassoan (2019-01-23 18:31 UTC)

<p>You need to set labels for each slice view, too:</p>
<pre><code class="lang-auto">getNode('vtkMRMLSliceNodeRed').SetAxisLabel(2,"Dorsal")
getNode('vtkMRMLSliceNodeRed').SetAxisLabel(3,"Ventral")
</code></pre>
<p>You can change settings in all slice views and modify the default for new slice views as shown in this example: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Change_default_slice_view_orientation" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Change_default_slice_view_orientation</a></p>

---
