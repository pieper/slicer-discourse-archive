---
topic_id: 29342
title: "3D Slicer And Compatibility Of Its Data To Unity"
date: 2023-05-08
url: https://discourse.slicer.org/t/29342
---

# 3D slicer and compatibility of its data to Unity

**Topic ID**: 29342
**Date**: 2023-05-08
**URL**: https://discourse.slicer.org/t/3d-slicer-and-compatibility-of-its-data-to-unity/29342

---

## Post #1 by @Nafise_Hasoomi (2023-05-08 05:10 UTC)

<p>Hello everybody, If I need to convert isodoes map in the Slicer RT module to OBJ or FBX format, what format would do you recommend to select for easier converting to OBJ or FBX. I want to use data in Unity.</p>

---

## Post #2 by @lassoan (2023-05-10 04:50 UTC)

<p>The easiest is to use OBJ. FBX is not an open file format, therefore there are not many good free readers/writers for it in free software.</p>
<p>Unity struggles if you have more than about 50k points in mesh, so most likely you need to decimate or remesh your model before exporting. If you export only a few segments then you can remesh using Surface Toolbox module’s Uniform remeshing option. If you want to export many segments with a single click then you can use SlicerOpenAnatomy extension’s OpenAnatomy export module. It has built-in model simplification (using quadric decimation).</p>

---

## Post #3 by @Bill_Blakesley (2024-09-06 09:53 UTC)

<p>More specifically, Unity can easily handle scenes with more than 65k polygons. It just has an annoying 65k limit for a single mesh. Unity will break up a mesh exceeding this limit on import just fine. Polygon reduction can be used to avoid this. If your use case doesn’t require automation, manually breaking the mesh up in a DCC app is a good option for more control.</p>

---
