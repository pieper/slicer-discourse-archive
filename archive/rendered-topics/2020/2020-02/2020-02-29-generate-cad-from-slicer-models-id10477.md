# Generate cad from slicer models

**Topic ID**: 10477
**Date**: 2020-02-29
**URL**: https://discourse.slicer.org/t/generate-cad-from-slicer-models/10477

---

## Post #1 by @Aep93 (2020-02-29 02:54 UTC)

<p>Hello all,<br>
Is there any way to fit NURBS or do similar tasks to convert the slicer models or segmentations into cad files?</p>

---

## Post #2 by @lassoan (2020-02-29 04:21 UTC)

<p>No, we don’t have a solution reverse-engineering anatomical shapes to parametric/NURBS surfaces within Slicer. Usually you import the mesh that you created in Slicer into your CAD software and you reverse-engineer manually there. Some CAD software has automatic methods that work for simple shapes.</p>

---

## Post #3 by @Aep93 (2020-02-29 04:52 UTC)

<p>Thank you  very much for your response.<br>
Do you know any open source cad software that I can use for the geometries that are not necessarily simple?</p>

---

## Post #4 by @lassoan (2020-02-29 20:06 UTC)

<p><a href="https://www.blender.org/">Blender</a> can do everything (it is the “3D Slicer” of 3D modeling), so I’m quite sure it can do this, too. There are commercial solutions that are freely available if you are in an academic institution (e.g., Autodesk Fusion 360).</p>

---

## Post #5 by @Aep93 (2020-02-29 20:29 UTC)

<p>Thank you very much for your help.</p>

---

## Post #6 by @manjula (2020-03-01 13:19 UTC)

<p>This too will help</p>
<div class="lazyYT" data-youtube-id="eXct_7k779Q" data-youtube-title="Point Cloud Visualizer  - Blender" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>

---

## Post #7 by @Aep93 (2020-03-01 17:21 UTC)

<p>Thank you very much for your help. But does it help to convert the cloud of points to cad files?<br>
To me it seems that it is just related to modify the cloud on points and not converting them.</p>

---

## Post #8 by @manjula (2020-03-01 17:25 UTC)

<aside class="quote no-group" data-username="Aep93" data-post="7" data-topic="10477">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aep93/48/5990_2.png" class="avatar"> Aep93:</div>
<blockquote>
<p>and</p>
</blockquote>
</aside>
<p>This does not,  but combination of 3D Slicer,  Blender and FreeCAD should be able to do most of the conversions necessary.</p>

---

## Post #9 by @Aep93 (2020-03-01 17:36 UTC)

<p>Thanks for your answer. Based on what I understood, we can get ply files from slicer and then import them into blender (in the toolbox you sent). There we can maybe reduce the intensity of the points(?) and export a new ply file. Then use freecad to convert the ply to cad files? Do you think this may work?</p>

---

## Post #10 by @manjula (2020-03-01 18:17 UTC)

<p>Well up to importing the ply to FreeCAD will surely work. Then ply to CAD in FreeCAD i have never tried.</p>

---

## Post #11 by @lassoan (2020-03-01 19:08 UTC)

<p>Slicer exports segmentation as a surface mesh, not just as a cloud of points. Therefore, for manipulating segmentations in Blender you don’t need point cloud visualization tool (you would only need it if you had surface scans or other point cloud data set as input).</p>

---
