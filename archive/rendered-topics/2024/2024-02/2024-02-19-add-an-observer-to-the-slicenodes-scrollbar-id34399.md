---
topic_id: 34399
title: "Add An Observer To The Slicenodes Scrollbar"
date: 2024-02-19
url: https://discourse.slicer.org/t/34399
---

# Add an observer to the SliceNode's scrollbar

**Topic ID**: 34399
**Date**: 2024-02-19
**URL**: https://discourse.slicer.org/t/add-an-observer-to-the-slicenodes-scrollbar/34399

---

## Post #1 by @waromero (2024-02-19 15:40 UTC)

<p>Hello!</p>
<p>I would like to add an observer to the scrollbar events of a given view. I cannot find the right event to add the callback function.</p>
<pre><code class="lang-auto">viewerNode = slicer.util.getNode("vtkMRMLSliceDisplayNode1") # Or should that be the vtkMRMLSliceNode class?
observerID = viewerNode.AddObserver(&lt;WHICH_CLASS__WHICH_METHOD&gt;, onScrollbarChanged)
</code></pre>
<p>The callback function:</p>
<pre><code class="lang-auto">def onScrollbarChanged(observer,eventID):
    print(&lt;SLICE_INDEX&gt;)
</code></pre>
<p>Thank you!</p>

---

## Post #2 by @Sam_Horvath (2024-02-19 20:20 UTC)

<p>So, this will give you the qt object the represents the slider for a particular view (the red slice in this case)</p>
<p><code>slider = slicer.app.layoutManager().sliceWidget("Red").sliceController().sliceOffsetSlider()</code></p>
<p>you can then do something like:<br>
<code>slicer.app.layoutManager().sliceWidget("Red").sliceController().sliceOffsetSlider().valueIsChanging.connect(lambda x : print(x))</code></p>

---

## Post #3 by @CyprienB (2024-02-23 14:17 UTC)

<p><strong>Operating system</strong>: Fedora Linux 39<br>
<strong>Slicer Version</strong>: 5.6.1</p>
<p>Hello,<br>
The method mentioned by Sam_Horvath  <em>valueIsChanging</em> was not working for. I have added an Observer on the slice Logic and it works fine.</p>
<blockquote>
<p>sliceLogic = slicer.app.layoutManager().sliceWidget(“Red”).sliceLogic()<br>
sliceLogic.AddObserver(vtk.vtkCommand.ModifiedEvent, lambda caller, event: print(“test”))</p>
</blockquote>
<p>However, I have noticed that this function will be triggered thrice so you should add a criteria to your function.</p>
<p>Cyprien</p>

---
