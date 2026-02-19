---
topic_id: 9043
title: "How To Change Window Level Programmatically"
date: 2019-11-06
url: https://discourse.slicer.org/t/9043
---

# How to change window/level programmatically

**Topic ID**: 9043
**Date**: 2019-11-06
**URL**: https://discourse.slicer.org/t/how-to-change-window-level-programmatically/9043

---

## Post #1 by @giovform (2019-11-06 13:30 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="1" data-topic="7284">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"><a href="https://discourse.slicer.org/t/recent-improvements-in-window-level-management/7284/1">Recent improvements in window/level management</a></div>
<blockquote>
<p>Ctrl + left-click-and-drag sets optimal window/level for the selected region. Pressing Escape or right-click during the drag cancels the operation.</p>
</blockquote>
</aside>
<p>Hi Andras, how could I set the window/level region programmatically, and apply the optimal window/level afterwards?</p>

---

## Post #2 by @lassoan (2019-11-06 13:33 UTC)

<p>See example in script repository: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Change_window.2Flevel_.28brightness.2Fcontrast.29_or_colormap_of_a_volume">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Change_window.2Flevel_.28brightness.2Fcontrast.29_or_colormap_of_a_volume</a></p>

---

## Post #3 by @giovform (2019-11-06 13:55 UTC)

<p>Yes, I knew that example, but what I wanted is to auto window/level using a selected region, just like when we press ‘Ctrl’ and drag the mouse.</p>

---

## Post #4 by @lassoan (2019-11-06 16:03 UTC)

<p>The logic is implemented in vtkImageHistogramStatistics. If you don’t want to use GUI then you can use that class directly from your scripts. You can have a look at the <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/DisplayableManager/vtkMRMLWindowLevelWidget.cxx#L576">window/level widget’s source code</a> as an example how it is used there.</p>

---

## Post #5 by @giovform (2019-11-07 16:36 UTC)

<p>The code snippet for anyone that might be interested (selecting a rectangle at the specified positions on the background of the Green slice viewer and applying Window Level):</p>
<pre><code>widget = slicer.vtkMRMLWindowLevelWidget()
widget.SetSliceNode(getNode('vtkMRMLSliceNodeGreen'))
widget.SetMRMLApplicationLogic(slicer.app.applicationLogic())
widget.UpdateWindowLevelFromRectangle(0, [60,60], [45,45])</code></pre>

---
