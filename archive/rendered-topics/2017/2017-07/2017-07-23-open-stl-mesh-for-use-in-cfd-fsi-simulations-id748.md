---
topic_id: 748
title: "Open Stl Mesh For Use In Cfd Fsi Simulations"
date: 2017-07-23
url: https://discourse.slicer.org/t/748
---

# "open" STL mesh for use in CFD & FSI simulations

**Topic ID**: 748
**Date**: 2017-07-23
**URL**: https://discourse.slicer.org/t/open-stl-mesh-for-use-in-cfd-fsi-simulations/748

---

## Post #1 by @mitenp (2017-07-23 16:22 UTC)

<p>Hi,</p>
<p>Am looking to generate STL of carotid artery with open ends. 3DSlicer STL has the ends closed.</p>
<p>Have seen technique using “Margin” etc to add wall thickness. However, this is more suitable for printing the artery vessel.</p>
<p>I’m looking to use the STL to generate a mesh for a CFD and add extentions etc.</p>
<p>Is there a way to clip the ends to open them ?</p>
<p>Miten</p>

---

## Post #2 by @lassoan (2017-07-23 16:27 UTC)

<p>Do you need a volumetric mesh or just a surface mesh? If you just need an open surface mesh then export the closed surface mesh from segmentation and cut of the closed ends with another module. There is model cut extension (or something similar) that can do this. If you don’t find that then let me know and I’ll look up the exact extension/module name.</p>

---

## Post #3 by @Patel_Miten (2017-07-24 00:14 UTC)

<p>Hi Andras,</p>
<p>Just a surface mesh.</p>
<p>Had a look for extension “module cut” and nothing familiar/similar found. Appreciate if you can locate the exact name.</p>
<p>Thanks,</p>
<p>Miten</p>

---

## Post #4 by @hina-shah (2017-07-24 00:38 UTC)

<p>Hi Miten,</p>
<p>You can use “Easy Clip” <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/EasyClip">extension</a>. This can cut loaded models using predetermined planes.</p>

---
