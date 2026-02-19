---
topic_id: 34879
title: "Converting Ply Mesh To 3Mf"
date: 2024-03-13
url: https://discourse.slicer.org/t/34879
---

# Converting PLY Mesh to 3mf

**Topic ID**: 34879
**Date**: 2024-03-13
**URL**: https://discourse.slicer.org/t/converting-ply-mesh-to-3mf/34879

---

## Post #1 by @Chubby_Chicken08 (2024-03-13 20:33 UTC)

<p>How do I convert a PLY Mesh with color into a 3mf model that I can load into a PowerPoint while retaining color? When I open the PLY Mesh on PP it has no color, but when I open it on slicer it has color. I’m new to this, so this might be a simple solution.</p>

---

## Post #2 by @lassoan (2024-03-17 02:59 UTC)

<p>You don’t need 3mf to import colored 3d meshes into powerpoint. Instead, you can use glTF.  Unfortunately, powerpoint requires the binary variant of glTF (.glb file format) and VTK’s glTF exporter can only text variant of glTF (.gltf file format). You can convert from .glTF to .glb outside of Slicer, for example using <a href="https://products.aspose.app/3d/conversion/gltf-to-glb">https://products.aspose.app/3d/conversion/gltf-to-glb</a></p>

---
