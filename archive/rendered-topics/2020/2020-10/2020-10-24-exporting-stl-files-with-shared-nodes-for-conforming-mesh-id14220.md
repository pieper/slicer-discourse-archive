# Exporting STL files with shared nodes for conforming mesh

**Topic ID**: 14220
**Date**: 2020-10-24
**URL**: https://discourse.slicer.org/t/exporting-stl-files-with-shared-nodes-for-conforming-mesh/14220

---

## Post #1 by @Tekk_ya (2020-10-24 10:54 UTC)

<p>Hi everyone,<br>
I have a question related to have a conforming mesh. I have segmented the regions that are watertight and have applied joint smoothing on the segments. I was wondering if it would be possible to export the segmented regions as STL files with shared nodes in their contact interfaces.</p>
<ul>
<li>If it there is any possible way to do it in 3DSlicer, would you please let me know which module I should use for it?</li>
<li>I have another general question about the STL files with shared nodes. Is it possible to reduce the meshes and remeshing them in the same manner that someone can do with the separated STL files with no shared nodes in between? (I am planning to remesh it in software such as MeshLab, Meshmixer, etc)</li>
<li>Would be any difference in creating volumetric meshes for such geometries that are sharing nodes in between the contact interface?</li>
</ul>
<p>Thanks for your help</p>

---

## Post #2 by @lassoan (2020-10-24 17:20 UTC)

<p>All these are solved by SegmentMesher extension. It creates a volumetric multi-material mesh with shared nodes at the boundary.</p>

---

## Post #3 by @Tekk_ya (2020-10-25 12:55 UTC)

<p>Dear Andras,</p>
<p>Thank you for your useful reply.</p>
<p>I had two different purposes for posting this question, the first was to generate volumetric meshes with conforming meshes in the contact regions which your reply answered my question and I will definitely try to generate the volumetric meshes using the SegmentMesher extension, as you suggested.<br>
The second one was to export the segmentations as surface meshes with shared nodes at the contact interfaces as I need to remesh those surface meshes in another software. Please note that for this second purpose, I am not planning to generate any volumetric meshes for the geometries and I only need the surface meshes. Do you have any suggestions for generating the surface meshes with shared nodes in the contact regions?</p>
<p>Thank you in advance for your help</p>

---

## Post #4 by @lassoan (2020-10-25 13:44 UTC)

<p>Mesh that you crate with “Export to files” in Segment Editor or Segmentations module are already have points that are very close to each other. You might have the points slightly closer to each other if you export the segmentation to labelmap and create models using Model Maker module.</p>
<p>What kind of remeshing are you planning to do, with what software? Decimation to simplify the meshes (for smaller size and faster rendering and picking)? Or fix errors for 3D printing? Does these remeshing operations preserve shared points between segments?</p>

---

## Post #5 by @Tekk_ya (2020-10-25 14:59 UTC)

<p>Dear Andras,</p>
<p>Thank you for your quick response. I am planning to use MeshLab or MeshMixer to reduce the meshes and have adaptive meshes, and then combine/merge them together as a single STL file. Finally, import the combines mesh into another software.</p>
<p>To be honest, I know that there are some “shape preserve” options in Meshmixer. However, I haven’t used any STL files with shared points between two geometries before. Therefore, I am not sure how it would handle such files.</p>
<p>My main concern is that when I export the watertight segments as separate STL files with no shared nodes in between,  after remeshing and high mesh reduction process on one of the objects, the points on the contact region might get far from each other, and there would be gaps in the contact regions which may cause some undesired holes in the combined STL file. Therefore, I was looking for some way to have shared nodes in the contact regions.</p>

---

## Post #6 by @tsehrhardt (2020-10-26 19:03 UTC)

<p>Have you tried combining the meshes–in Meshlab use “Flatten Visible layers” and then applying Poisson Surface Reconstruction? If the models are close enough to each other, it should try to “wrap” all the parts into one mesh.</p>

---

## Post #7 by @Tekk_ya (2021-04-09 13:11 UTC)

<p>Dear Andras,</p>
<p>I know that it is an old post, but I want to understand that how the export module works for exporting watertight segments. Could you please let me know if I export the watertight segmented regions from the 3Dslice,</p>
<ol>
<li>
<p>Would I have watertight geometries? Or there might be tiny gaps/overlaps? and if so, could I have any estimation of the sizes of these gaps wrt to data resolution and voxel size? Probably less than half a voxel size?</p>
</li>
<li>
<p>Would I have conforming meshes in the contacting area? something like duplicated nodes in the contacting interfaces.</p>
</li>
<li>
<p>In the case of using “SegmentMesher” extension, would it be possible to only extract the surface meshes including the nodes in the contacting region, and then instead of the shared nodes have duplicated nodes in the contacting interfaces?</p>
</li>
</ol>
<p>Best,</p>

---

## Post #8 by @lassoan (2021-04-14 03:49 UTC)

<aside class="quote no-group" data-username="Tekk_ya" data-post="7" data-topic="14220">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tekk_ya/48/3548_2.png" class="avatar"> Tekk_ya:</div>
<blockquote>
<p>Would I have watertight geometries? Or there might be tiny gaps/overlaps? and if so, could I have any estimation of the sizes of these gaps wrt to data resolution and voxel size? Probably less than half a voxel size?</p>
</blockquote>
</aside>
<p>When you export multimaterial meshes then you always need to balance between smooth boundaries and having gaps/overlaps. You can control choose between these by adjusting surface smoothing (0 smoothing will result in no gaps/overlaps but staircase artifacts; high smoothing will remove all staircase artifacts but there may be small holes and overlaps between segments).</p>
<aside class="quote no-group" data-username="Tekk_ya" data-post="7" data-topic="14220">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tekk_ya/48/3548_2.png" class="avatar"> Tekk_ya:</div>
<blockquote>
<p>Would I have conforming meshes in the contacting area? something like duplicated nodes in the contacting interfaces.</p>
</blockquote>
</aside>
<p>Yes, if you set smoothing to zero.</p>
<aside class="quote no-group" data-username="Tekk_ya" data-post="7" data-topic="14220">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tekk_ya/48/3548_2.png" class="avatar"> Tekk_ya:</div>
<blockquote>
<p>In the case of using “SegmentMesher” extension, would it be possible to only extract the surface meshes including the nodes in the contacting region, and then instead of the shared nodes have duplicated nodes in the contacting interfaces?</p>
</blockquote>
</aside>
<p>You can extract outer surface of a volumetric mesh by applying <a href="https://vtk.org/doc/nightly/html/classvtkGeometryFilter.html">vtkGeometryFilter</a>.</p>

---
