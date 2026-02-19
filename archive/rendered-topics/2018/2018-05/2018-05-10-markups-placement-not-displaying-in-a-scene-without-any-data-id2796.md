---
topic_id: 2796
title: "Markups Placement Not Displaying In A Scene Without Any Data"
date: 2018-05-10
url: https://discourse.slicer.org/t/2796
---

# Markups placement not displaying in a scene without any data

**Topic ID**: 2796
**Date**: 2018-05-10
**URL**: https://discourse.slicer.org/t/markups-placement-not-displaying-in-a-scene-without-any-data/2796

---

## Post #1 by @roozbehshams (2018-05-10 19:48 UTC)

<p>I’ve realized when trying to add markups fiducials in persistent mode, the display is not updated properly.<br>
This happens only when there is no data in the scene. When adding fiducials, they won’t show up unless:</p>
<ul>
<li>A fiducial is placed in another panel,</li>
<li>The Modified() function of the markups node is called.<br>
To reproduce it, in an empty scene, choose the fiducial placement tool in persistent mode, place a few in one panel (the first one will show up). The rest will only show up if another fiducial is placed in another panel.</li>
</ul>

---

## Post #2 by @lassoan (2018-05-14 03:14 UTC)

<p>I was able to reproduce the issue based on your description. We are in the process of reworking markup widgets, so I’m not sure anyone would have time to work on fixing the existing widgets. However, you can manually trigger a rendering update after each fiducial placement like this:</p>
<pre><code>layoutManager = slicer.app.layoutManager()
for sliceViewName in layoutManager.sliceViewNames():
  layoutManager.sliceWidget(sliceViewName).sliceView().renderWindow().Render()</code></pre>

---
