---
topic_id: 34623
title: "Exporting To As Gltf Changes Names"
date: 2024-02-29
url: https://discourse.slicer.org/t/34623
---

# Exporting to as GLTF changes names

**Topic ID**: 34623
**Date**: 2024-02-29
**URL**: https://discourse.slicer.org/t/exporting-to-as-gltf-changes-names/34623

---

## Post #1 by @MuckYu (2024-02-29 18:34 UTC)

<p>I am trying to export the centerline from a scene with a python script.</p>
<p>OBJ/STL etc. don’t export the centerline at all.</p>
<p>So I have to use GLTF - which works fine so far.<br>
The problem here is that it exports the whole scene - including camera, bounding box, arrows, mesh etc.</p>
<p>And then it’s naming everything mesh0, mesh1, mesh2 …</p>
<p>I need a way to isolate the centerline curve somehow.</p>
<p>How can I do this?<br>
Is there a way to only export the curve with the gltfexporter?<br>
Or otherwise have the names etc. so that I can isolate it that way later?</p>

---
