---
topic_id: 37351
title: "Convert File Of Vtk Of Segment Mesher"
date: 2024-07-13
url: https://discourse.slicer.org/t/37351
---

# Convert file of .vtk of Segment Mesher

**Topic ID**: 37351
**Date**: 2024-07-13
**URL**: https://discourse.slicer.org/t/convert-file-of-vtk-of-segment-mesher/37351

---

## Post #1 by @khajta (2024-07-13 10:13 UTC)

<p>I am a new of using Segment Mesher and mesh phantom. I can export the segmented organ using Cleaver method and save as .vtk. However, the input for phits program need .node and .ele. How to convert this file?</p>

---

## Post #2 by @lassoan (2024-07-13 20:26 UTC)

<p>There are lots of mesh conversion tools that can convert between various file formats. Slicer can write volumetric meshes as VTK unstructured grid in .vtk or .vtu format. The .node/.ele format is tetgen tetrahedral mesh. For example, you can use <a href="https://github.com/nschloe/meshio">meshio</a>.</p>

---

## Post #3 by @khajta (2024-07-14 02:09 UTC)

<p>Thank you for your reply. I try to search this issue and I found that TetGen is a toll for this task as well. Which one is easy to use in your opinion?</p>

---

## Post #4 by @lassoan (2024-07-14 02:38 UTC)

<p>Segment mesher can use Cleaver or TetGen for mesh generation. Cleaver tend to work better for creating meshes from medical image segmentations, while TetGen may perform a bit better if you want to create volumetric mesh for parts designed in CAD software. TetGen has restrictive license that may prevent you from using it in commercial projects, while Cleaver has no such limitation.</p>
<p>There are hundreds of other volumetric meshing tools, such as netgen (but that has restrictive license, too) ot fTetWild (a robust, high-quality volumetric mesher with non-restrictive license).</p>

---

## Post #5 by @khajta (2024-07-14 03:57 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="37351">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>esher can use Cleaver or TetGen for mesh generation. Cleaver tend to work better for creating meshes from medical image segmentations, while TetGen may perform a bit better if you want to create volumetric mesh for parts designed in CAD software. TetGen has restrictive license that may prevent you from using it in commercial projects, while Cleaver has no such limitation.</p>
<p>There are hundreds of other volumetric meshing tools, such as netgen (but that has restrictiv</p>
</blockquote>
</aside>
<p>Thank you very much.</p>

---
