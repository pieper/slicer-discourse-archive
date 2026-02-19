---
topic_id: 8580
title: "Loading A Color Table In C"
date: 2019-09-26
url: https://discourse.slicer.org/t/8580
---

# Loading a color table in c++

**Topic ID**: 8580
**Date**: 2019-09-26
**URL**: https://discourse.slicer.org/t/loading-a-color-table-in-c/8580

---

## Post #1 by @rbahegne (2019-09-26 12:35 UTC)

<p>Hello, it seems rather simple but i did not manage to manually load a color table in c++.</p>
<p>I would like also if possible to set manually the min and max.</p>
<p>Thanks</p>

---

## Post #2 by @rbahegne (2019-09-26 13:19 UTC)

<p>Nevermind I found it :</p>
<blockquote>
<p>vtkMRMLMultiVolumeDisplayNode* mvD = mVolumeNode-&gt;GetMultiVolumeDisplayNode();<br>
mvD-&gt;AutoWindowLevelOff();<br>
mvD-&gt;SetAndObserveColorNodeID(“vtkMRMLColorTableNodeFileColdToHotRainbow.txt”);<br>
mvD-&gt;SetWindowLevelMinMax(35,50);</p>
</blockquote>

---
