---
topic_id: 36757
title: "Export 3d model into stp file"
date: 2024-06-13
url: https://discourse.slicer.org/t/36757
last_bumped: 2026-11-06T15:40:23.004Z
---

# Export 3d model into stp file

**Topic ID**: 36757
**Date**: 2024-06-13
**URL**: https://discourse.slicer.org/t/export-3d-model-into-stp-file/36757

---

## Post #1 by @Caterina (2024-06-13 13:35 UTC)

<p>Dear support,<br>
I would to export results of segmentation as stp model in order to use it for cfd model.<br>
Can you please suggest me how to do it?<br>
Thanks</p>

---

## Post #2 by @JiayuXu0 (2026-11-06 15:40 UTC)

<p>Slicer segmentations export as surface meshes (STL/OBJ/etc.), not parametric STEP/IGES. For CFD you typically take the mesh into your CAD/mesher and reverse-engineer or mesh directly from the surface — creating trimmed NURBS from anatomy is a hard reverse-engineering step, not a one-click export. If you only need a quick look / measure of an exported STL before CFD, a browser STL viewer is enough. CADProps opens STL/STEP/DWG among ~92 extensions; native CAD formats are processed on CADProps servers. <a href="https://www.cadprops.com/tools/stl-viewer/" class="inline-onebox" rel="noopener nofollow ugc">STL Viewer Online: Mesh Dimensions, Area &amp; Volume | CADProps</a></p>

---
