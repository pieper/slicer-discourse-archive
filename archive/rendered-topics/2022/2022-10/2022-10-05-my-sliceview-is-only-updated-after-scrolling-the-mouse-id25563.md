# My SliceView is only updated after scrolling the mouse

**Topic ID**: 25563
**Date**: 2022-10-05
**URL**: https://discourse.slicer.org/t/my-sliceview-is-only-updated-after-scrolling-the-mouse/25563

---

## Post #1 by @Niels (2022-10-05 20:17 UTC)

<p>In my module I change areas of my volume by clicking with the mouse in one of the slice views (red/green/blue). This works fine.</p>
<p>But all changes are reflected in all the views, except the view that I actually click in.<br>
The view is updated when I scroll a tiny little step forward and backward.</p>
<p>Is there a python way of updating/refreshing the slice view? like a modified method that we use for volumes or a display node?</p>

---

## Post #2 by @Niels (2022-10-11 19:29 UTC)

<p>solved it, I force an update of the views using this</p>
<pre><code>layoutManager = slicer.app.layoutManager()
for sliceViewName in layoutManager.sliceViewNames():
  sliceWidget = layoutManager.sliceWidget(sliceViewName);
  sliceLogic = sliceWidget.sliceLogic()
  sliceNode = sliceLogic.GetSliceNode()
  sliceNode.Modified()
</code></pre>

---

## Post #3 by @lassoan (2022-10-19 06:40 UTC)

<p>Slicer does not know when you are finished with your numpy array modifications. Therefore, when you are done with your changes in a volume node via numpy, you must call <code>slicer.util.arrayFromVolumeModified()</code> function, as described in the <a href="https://github.com/Slicer/Slicer/blob/main/Base/Python/slicer/util.py#L1627"><code>slicer.util.arrayFromVolume()</code> function documentation</a>.</p>

---
