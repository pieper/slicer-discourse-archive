---
topic_id: 243
title: "Refinement Of Stl Files"
date: 2017-05-02
url: https://discourse.slicer.org/t/243
---

# Refinement of stl files

**Topic ID**: 243
**Date**: 2017-05-02
**URL**: https://discourse.slicer.org/t/refinement-of-stl-files/243

---

## Post #1 by @virajbelekar (2017-05-02 13:12 UTC)

<p>Hello,</p>
<p>I saved a .stl file of the portal vein system from my CT scan. So basically a .stl file is a 2D surface mesh of the geometry. The thing is, this mesh which I have generated is very fine having very small elements. I do not want such a refined 2D file. Is there any way to control the refinement of the file?</p>
<p>Thanks and Regards<br>
Viraj</p>

---

## Post #2 by @ihnorton (2017-05-02 13:44 UTC)

<p>If you are using the “Model Maker” module, you can reduce the number of triangles during surface generation with the “Decimation” parameter.</p>

---

## Post #3 by @arankin (2017-05-02 14:03 UTC)

<p>Optionally, you can post-process with MeshLab. They have a number of pre-made filters for polygon reduction.</p>
<p>Adam</p>

---

## Post #4 by @ihnorton (2017-05-02 14:38 UTC)

<p>See also the Surface Toolbox:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/SurfaceToolbox" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Modules/SurfaceToolbox</a></p>

---

## Post #5 by @virajbelekar (2017-05-02 16:13 UTC)

<p>I am using segment editor followed by the segmentation module!</p>

---

## Post #6 by @lassoan (2017-05-02 16:18 UTC)

<p>In Segmentations module, you can reduce number of triangles in the surface mesh by the following steps:</p>
<ul>
<li>click <code>Update</code> button in the <code>Closed surface</code> row in <code>Representations</code> section</li>
<li>click <code>Binary labelmap -&gt; Closed surface</code> path</li>
<li>double-click on the value in the <code>Decimation factor</code> line, and enter a value of 0.8 (value between 0.0-1.0; the larger the value, the less triangles you’ll have in the mesh)</li>
<li>click <code>Convert</code>
</li>
</ul>
<p>You can convert from Segmentation to Model node by using the <code>Export/Import segments</code> section and then use Surface toolbox module to further smooth or decimate the mesh.</p>

---
