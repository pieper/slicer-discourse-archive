---
topic_id: 8384
title: "Surface Opacity Jump"
date: 2019-09-11
url: https://discourse.slicer.org/t/8384
---

# Surface opacity jump

**Topic ID**: 8384
**Date**: 2019-09-11
**URL**: https://discourse.slicer.org/t/surface-opacity-jump/8384

---

## Post #1 by @rprueckl (2019-09-11 15:44 UTC)

<p>When changing the opacity of a surface, the first step from fully opaque to ‘just a little transparent’ (i.e. from 1.00 to 0.99) causes a relatively big visual difference, whereas the change from 0.99 to 0.98 causes no visible difference. I was looking at a model of the skull generated from the CT of the ‘CT-MR Brain’ sample dataset.<br>
I wonder whether there is a possibility to make the transition between fully opaque and ‘a bit transparent’ smoother?</p>

---

## Post #2 by @pieper (2019-09-11 19:16 UTC)

<p>If your model has a lot of internal structure then you may need to enable depth peeling in order to get predictable rendering.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.3/SlicerApplication/MainApplicationGUI#3D_Viewer" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.3/SlicerApplication/MainApplicationGUI#3D_Viewer</a></p>

---
