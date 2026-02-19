---
topic_id: 24661
title: "How Can I Get The Widget Called Vtkmrmlsliceintersectionwidg"
date: 2022-08-06
url: https://discourse.slicer.org/t/24661
---

# How can I get the widget called "vtkMRMLSliceIntersectionWidget" in python?

**Topic ID**: 24661
**Date**: 2022-08-06
**URL**: https://discourse.slicer.org/t/how-can-i-get-the-widget-called-vtkmrmlsliceintersectionwidget-in-python/24661

---

## Post #1 by @zhang_ming (2022-08-06 02:11 UTC)

<pre><code class="lang-auto">sliceViewLabel = "Red"
sliceViewWidget = slicer.app.layoutManager().sliceWidget(sliceViewLabel)
displayableManager = sliceViewWidget.sliceView().displayableManagerByClassName("**vtkMRMLScalarBarDisplayableManager**")
w = displayableManager.GetWindowLevelWidget()
</code></pre>
<p>as showed the code to get window&amp;level ViewWidget is available in python.<br>
but when I try to get <strong>vtkMRMLSliceIntersectionWidget</strong> , I can’t find api in doc, can any help me? when this step finished, the left mouse clice_and_drag to shift between 2d pic will be finished</p>

---
