---
topic_id: 6192
title: "Convert Model To Volume Rendering"
date: 2019-02-22
url: https://discourse.slicer.org/t/6192
---

# Convert model to volume rendering

**Topic ID**: 6192
**Date**: 2019-02-22
**URL**: https://discourse.slicer.org/t/convert-model-to-volume-rendering/6192

---

## Post #1 by @Nicholas.jacobson (2019-02-22 03:14 UTC)

<p>Hi all, is there a way to convert a model into a volume rendering? I’m trying to load a stl and ply and convert it into a volume rendering for bitmap generation. Any ideas how to make this work? Guessing <a class="mention" href="/u/lassoan">@lassoan</a> is the best person to understand what I’m trying to accomplish.</p>

---

## Post #2 by @Hamburgerfinger (2019-02-22 04:03 UTC)

<p>You can 1) import your model 2) convert it to segmentation 3) convert the segmentation to a label map and finally 4) convert the label map to a scalar volume which can be volume rendered like any other volume.</p>

---

## Post #3 by @Nicholas.jacobson (2019-02-25 15:59 UTC)

<p>Thanks <a class="mention" href="/u/hamburgerfinger">@Hamburgerfinger</a> this method does not seem to work for ply imports. It hangs up my computer. I’ve got a ply import similar to a tractography bundle.</p>

---

## Post #4 by @lassoan (2019-03-18 13:12 UTC)

<p>You can import a model loaded from .ply file to segmentation. It may take long, depending on how complex the model is and what resolution you set for the segmentation’s binary labelmap representation. If you have any specific issue then let us know.</p>
<p>The exported volume will be binary, with no colors, so I’m not sure that this conversion would be useful for you.</p>

---
