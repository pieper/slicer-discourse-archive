---
topic_id: 6940
title: "Calculating Dvhs For Models"
date: 2019-05-27
url: https://discourse.slicer.org/t/6940
---

# Calculating DVHs for models

**Topic ID**: 6940
**Date**: 2019-05-27
**URL**: https://discourse.slicer.org/t/calculating-dvhs-for-models/6940

---

## Post #1 by @aseman (2019-05-27 17:43 UTC)

<p>Slicer version:4.10.1<br>
Hi 3D slicer experts and all<br>
Is it possible to calculate DVHs for models( instead of segments ) using Dose Volume Histogram module?<br>
Thanks a lot</p>

---

## Post #2 by @cpinter (2019-05-27 18:17 UTC)

<p>DVH module only accepts segmentations as input, but it’s very easy to convert models to segmentation:</p>
<ul>
<li>In Models module, right-click the scene and choose ‘Insert hierarchy’</li>
<li>Go to Data module, select the models, and drag&amp;drop them under the hierarchy (will be called ‘Model Hierarchy’ by default</li>
<li>Right-click the hierarchy, and choose ‘Convert model hierarchy to segmentation node’</li>
</ul>

---
