# Changing visibility of 3D Cube and 3D Axis Label through Python

**Topic ID**: 3650
**Date**: 2018-08-03
**URL**: https://discourse.slicer.org/t/changing-visibility-of-3d-cube-and-3d-axis-label-through-python/3650

---

## Post #1 by @brynpitt (2018-08-03 21:50 UTC)

<p>Hello all,</p>
<p>I am trying to change the visibility of the 3D Cube and the 3D Axis Labels (in the 3D View) using Python. I want to do this because I am trying to customize the appearance of the main window at launch.</p>
<p>I have been able to find find functions to set all the other aspects of the appearance through slicer.util and slicer.app, but I haven’t found the way to change things inside the view windows themselves. If someone could point me in the right direction, I would really appreciate it.</p>
<p>Thanks,<br>
Bryn</p>

---

## Post #2 by @lassoan (2018-08-03 23:41 UTC)

<p>These view properties are stored in the view node. See <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Change_3D_view_background_color">this example</a> of how to modify a property.</p>

---

## Post #3 by @hemmer (2025-05-07 15:09 UTC)

<p>As the link went dead, and just for reference, I achieved this by:</p>
<pre><code class="lang-auto">layoutManager = slicer.app.layoutManager()
threeDWidget = layoutManager.threeDWidget(0)
threeDView = threeDWidget.threeDView()
threeDView.mrmlViewNode().SetAxisLabelsVisible(False)
threeDView.mrmlViewNode().SetBoxVisible(False)
</code></pre>

---
