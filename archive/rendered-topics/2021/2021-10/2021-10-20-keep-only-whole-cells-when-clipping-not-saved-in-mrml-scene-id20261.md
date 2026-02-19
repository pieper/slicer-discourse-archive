---
topic_id: 20261
title: "Keep Only Whole Cells When Clipping Not Saved In Mrml Scene"
date: 2021-10-20
url: https://discourse.slicer.org/t/20261
---

# "Keep only whole cells when clipping" not saved in mrml scene file

**Topic ID**: 20261
**Date**: 2021-10-20
**URL**: https://discourse.slicer.org/t/keep-only-whole-cells-when-clipping-not-saved-in-mrml-scene-file/20261

---

## Post #1 by @hherhold (2021-10-20 12:02 UTC)

<p>This is somewhat relevant to <a href="https://discourse.slicer.org/t/clipping-of-models-is-too-slow/8788" class="inline-onebox">Clipping of models is too slow</a>.</p>
<p>Enabling “Keep only whole cells when clipping” speeds up the clipping a lot for complex models. This setting, however, is not saved in the scene file, making scene loading very slow for complex projects saved with clipping enabled.</p>
<p>Is there a way to add this? Happy to give it a shot if someone could point me in the right direction on where to start.</p>
<p>Thanks!</p>
<p>-Hollister</p>

---

## Post #2 by @hherhold (2021-10-20 12:08 UTC)

<p>Oops, make that <a href="https://discourse.slicer.org/t/window-resize-with-model-clipping-enabled-is-extremely-slow/20208" class="inline-onebox">Window resize with model clipping enabled is extremely slow</a> as the more relevant post. Sorry about that.</p>

---

## Post #3 by @lassoan (2021-10-21 04:17 UTC)

<p>Good catch. I’ve fixed the scene reader now. The fix will be available in the Slicer Preview Release that you download on Friday or later.</p>

---

## Post #4 by @hherhold (2021-10-21 11:55 UTC)

<p>Awesome - thanks a lot!!!</p>

---
