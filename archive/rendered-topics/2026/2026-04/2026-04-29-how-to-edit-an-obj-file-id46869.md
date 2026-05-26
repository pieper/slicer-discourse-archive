---
topic_id: 46869
title: "how to edit an obj file "
date: 2026-04-29
url: https://discourse.slicer.org/t/46869
last_bumped: 2026-04-30T10:24:37.051Z
---

# how to edit an obj file 

**Topic ID**: 46869
**Date**: 2026-04-29
**URL**: https://discourse.slicer.org/t/how-to-edit-an-obj-file/46869

---

## Post #1 by @ellenku (2026-04-29 15:45 UTC)

<p>Hello!</p>
<p>I have a bunch of cranial endocast saved in obj form. I want to try to section of the cerebellum region, and I think this should be possible in maybe segment editor. However, since the obj is mesh model, i cannot edit it in segment editor. How could I get to meausure the surface area and volume of only a section of the endocast?</p>

---

## Post #2 by @ebrahim (2026-04-29 16:08 UTC)

<p>It may load as a model node, but then you can convert it to a segmentation node and do all the segmentation-related things with it like segment editing and segment statistics.</p>
<p>You can import directly to segmentation also, rather than converting: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#import-an-existing-segmentation-from-model-surface-mesh-file" class="inline-onebox">Segmentations — 3D Slicer documentation</a></p>

---

## Post #3 by @ThomasVanParys (2026-04-30 10:24 UTC)

<p>You can edit surface meshes (e.g., OBJ, PLY, STL) using the ‘Dynamic Modeler’ module: <a href="https://github.com/Slicer/Slicer/blob/main/Docs/user_guide/modules/dynamicmodeler.md" class="inline-onebox" rel="noopener nofollow ugc">Slicer/Docs/user_guide/modules/dynamicmodeler.md at main · Slicer/Slicer · GitHub</a>. You should be able to select most of the cerebellum this way.</p>

---
