---
topic_id: 19331
title: "Fit Sliceview Zoom"
date: 2021-08-24
url: https://discourse.slicer.org/t/19331
---

# Fit SliceView Zoom

**Topic ID**: 19331
**Date**: 2021-08-24
**URL**: https://discourse.slicer.org/t/fit-sliceview-zoom/19331

---

## Post #1 by @apparrilla (2021-08-24 08:57 UTC)

<p>Hi everyone!<br>
I´m trying to fit a reformat slice view to volume size.<br>
I´ve finded slicer.util.setSliceViewerLayers(volumeNode, fit=True) but it reset also position and orientation. I´ve tried also sliceLogic.FitSliceToAll() but with same results.<br>
Is there any way to just fit zoom of slice view?<br>
Thanks on advance</p>

---

## Post #2 by @riep (2021-08-25 07:45 UTC)

<p>Hi Angel,<br>
If you want to avoid rotation, you could use.</p>
<blockquote>
<p>appLogic = slicer.app.applicationLogic()<br>
appLogic.FitSliceToAll(True, False)</p>
</blockquote>
<p>However, I would say that position change is the normal behavior.</p>

---

## Post #3 by @lassoan (2021-09-05 02:06 UTC)

<p>If you want to center the volume except you want to keep the current slice offset (just zoom in/out and pan to center the volume but keep the current slice) then you can save the slice offset before centering and then restore it:</p>
<pre><code class="lang-python">sliceLogic = slicer.app.applicationLogic().GetSliceLogicByLayoutName("Red")
offset = sliceLogic.GetSliceOffset()
sliceLogic.FitSliceToAll()
sliceLogic.SetSliceOffset(offset)
</code></pre>

---
