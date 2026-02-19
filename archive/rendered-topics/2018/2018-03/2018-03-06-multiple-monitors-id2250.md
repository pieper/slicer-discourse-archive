---
topic_id: 2250
title: "Multiple Monitors"
date: 2018-03-06
url: https://discourse.slicer.org/t/2250
---

# Multiple monitors

**Topic ID**: 2250
**Date**: 2018-03-06
**URL**: https://discourse.slicer.org/t/multiple-monitors/2250

---

## Post #1 by @Jason_Gellis (2018-03-06 14:17 UTC)

<p>Is there any way to split the red, green, yellow, and 3d screen to another monitor? It would be nice to keep the modules on one screen and images on another. Thank you.</p>

---

## Post #2 by @lassoan (2018-03-06 14:33 UTC)

<p>For multi-monitor setups, we usually stretch the application window to cover all screens that we want to use and drag-and-drop the vertical splitters to be at the edge of the monitor. Several layouts have vertical splitters, but none of them would allow you to split 3 slice views. For that, you need to copy-paste the code below into the Python console to define and switch to a custom layout:</p>
<pre><code>customLayout = """
&lt;layout type="horizontal" split="true"&gt;
 &lt;item&gt;
  &lt;view class="vtkMRMLSliceNode" singletontag="Red"&gt;
   &lt;property name="orientation" action="default"&gt;Axial&lt;/property&gt;
     &lt;property name="viewlabel" action="default"&gt;R&lt;/property&gt;
   &lt;property name="viewcolor" action="default"&gt;#F34A33&lt;/property&gt;
  &lt;/view&gt;
 &lt;/item&gt;
 &lt;item&gt;
  &lt;view class="vtkMRMLSliceNode" singletontag="Green"&gt;
   &lt;property name="orientation" action="default"&gt;Axial&lt;/property&gt;
   &lt;property name="viewlabel" action="default"&gt;G&lt;/property&gt;
   &lt;property name="viewcolor" action="default"&gt;#6EB04B&lt;/property&gt;
  &lt;/view&gt;
 &lt;/item&gt;
 &lt;item&gt;
  &lt;view class="vtkMRMLSliceNode" singletontag="Yellow"&gt;
   &lt;property name="orientation" action="default"&gt;Axial&lt;/property&gt;
   &lt;property name="viewlabel" action="default"&gt;Y&lt;/property&gt;
   &lt;property name="viewcolor" action="default"&gt;#EDD54C&lt;/property&gt;
  &lt;/view&gt;
 &lt;/item&gt;
 &lt;item&gt;
  &lt;view class="vtkMRMLViewNode" singletontag="1"&gt;
   &lt;property name="viewlabel" action="default"&gt;1&lt;/property&gt;
  &lt;/view&gt;
 &lt;/item&gt;
&lt;/layout&gt;
"""
  
customLayoutId=555

layoutManager = slicer.app.layoutManager()
layoutManager.layoutLogic().GetLayoutNode().AddLayoutDescription(customLayoutId, customLayout)                                         
layoutManager.setLayout(customLayoutId)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/16af4c4c4a1b22c1b590b949b3aa39262b05ebe9.jpeg" data-download-href="/uploads/short-url/3eG4Soqt3FvKrPVtJ5Q3XzGDC09.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/16af4c4c4a1b22c1b590b949b3aa39262b05ebe9_2_690x184.jpeg" alt="image" data-base62-sha1="3eG4Soqt3FvKrPVtJ5Q3XzGDC09" width="690" height="184" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/16af4c4c4a1b22c1b590b949b3aa39262b05ebe9_2_690x184.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/16af4c4c4a1b22c1b590b949b3aa39262b05ebe9_2_1035x276.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/16af4c4c4a1b22c1b590b949b3aa39262b05ebe9_2_1380x368.jpeg 2x" data-dominant-color="9E959C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3802×1018 618 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @pieper (2018-03-06 15:36 UTC)

<p>Also something like this works to split a widget out of the main window:</p>
<pre><code class="lang-auto">slicer.app.layoutManager().sliceWidget('Red').setParent(None)
slicer.app.layoutManager().sliceWidget('Red').show()
</code></pre>
<p>The widget gets reparented to the main window when you change the layout.</p>

---

## Post #4 by @lassoan (2018-03-08 17:16 UTC)

<p>You can also create a completely independent slice widget (that will not be reparented to the main window) as shown here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Show_a_slice_view_outside_the_view_layout">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Show_a_slice_view_outside_the_view_layout</a></p>
<p>It requires some API changes that I’ve just added, so it’ll work with nightly Slicer builds that you download tomorrow or later.</p>

---
