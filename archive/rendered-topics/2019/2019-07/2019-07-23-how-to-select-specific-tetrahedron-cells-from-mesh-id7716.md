---
topic_id: 7716
title: "How To Select Specific Tetrahedron Cells From Mesh"
date: 2019-07-23
url: https://discourse.slicer.org/t/7716
---

# How to select specific tetrahedron cells from mesh

**Topic ID**: 7716
**Date**: 2019-07-23
**URL**: https://discourse.slicer.org/t/how-to-select-specific-tetrahedron-cells-from-mesh/7716

---

## Post #1 by @Saima (2019-07-23 03:44 UTC)

<p>If you have a mesh created from segmentmesher. how can you select the tetrahedron cells.</p>

---

## Post #2 by @adamrankin (2019-07-23 12:41 UTC)

<p>With the mouse? By index? How do you want to select the cell?</p>

---

## Post #3 by @adamrankin (2019-07-23 13:42 UTC)

<p>Two possible examples at the VTK level that might help are:</p>
<p><a href="https://lorensen.github.io/VTKExamples/site/Cxx/Picking/HighlightSelection/" class="onebox" target="_blank" rel="nofollow noopener">https://lorensen.github.io/VTKExamples/site/Cxx/Picking/HighlightSelection/</a><br>
<a href="https://lorensen.github.io/VTKExamples/site/Cxx/Picking/HighlightSelectedPoints/" class="onebox" target="_blank" rel="nofollow noopener">https://lorensen.github.io/VTKExamples/site/Cxx/Picking/HighlightSelectedPoints/</a></p>

---

## Post #4 by @Saima (2019-07-24 05:02 UTC)

<p>how to select with the mouse in the slicer scene, selecting cells and then coloring it and then having those cells and their positions in a file</p>

---

## Post #5 by @lassoan (2019-07-24 13:14 UTC)

<p>You can use a picker to get cell IDs from mouse coordinates (see links that <a class="mention" href="/u/adamrankin">@adamrankin</a> provided above). You can retrieve cell positions based on the IDs from the VTK mesh object. Add a cell array to your mesh and set different values for selected and non-selected cells. You can use this array to color the selected and non-selected cells differently.</p>

---

## Post #6 by @Saima (2019-07-25 08:28 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="7716">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>IDs from mouse coordina</p>
</blockquote>
</aside>
<p>how to interact with the 3d slice view of slicer. I have a mesh in 3d slice view. need to select some cells from it and change the colors of those selected cells.</p>
<p>I tried using the vtkcellpicker, but I dont understand the addobserver.</p>
<p>the addobserver of vtkcellpicker takes 2 arguments. first is the event and second is the method. Am I right?</p>
<p>Please help further. are there any examples related to slicer 3d view</p>

---

## Post #7 by @lassoan (2019-07-25 18:23 UTC)

<p>This example should do most of what you need:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_scalar_values_at_surface_of_a_model" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_scalar_values_at_surface_of_a_model</a></p>

---

## Post #8 by @Saima (2021-02-09 21:56 UTC)

<p>Hi andras,<br>
How to select tetrahedrons in a mesh using another mesh through a python script.</p>
<p>Thank you</p>
<p>Regards,<br>
Saima safdar</p>

---

## Post #9 by @lassoan (2021-02-10 02:22 UTC)

<p>You can follow this example: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Select_cells_of_a_model_using_markups_fiducial_points" class="inline-onebox">Documentation/Nightly/ScriptRepository - Slicer Wiki</a></p>
<p>In a volumetric mesh, cells are tetrahedra, so probably the code will work without modification.</p>

---

## Post #10 by @Saima (2021-02-23 06:51 UTC)

<p>Hi Andras,<br>
After selecting tetrahedrons. How to remove the selected tetrahedrons and have the unstructured grid remain without those deleted ones. example removing tumore cells from the brain mesh. how to retain the brain geometry.</p>
<p>regards,<br>
Saima Safdar</p>

---

## Post #11 by @lassoan (2021-02-23 13:10 UTC)

<p>You can either use vtkThreshold (cells that need to be deleted are identified by the value of a designated cell data array) or vtkExtractCells (cells that need to be deleted are identified by a cell ID list).</p>

---

## Post #12 by @Saima (2021-02-25 06:30 UTC)

<p>Hi Andras,<br>
Could you please see the post</p><aside class="quote quote-modified" data-post="1" data-topic="16175">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/select-nearest-neighbour-voxels-using-some-voxels-as-reference/16175">Select nearest neighbour voxels using some voxels as reference?</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Hi, 
Is there a possibility to select nearest neighbor voxels in an MRI based on the label-map. For-example I have the voxels based on some label. then I need to find nearest neighbour voxels that dont belong to voxels identified through label. 
I found this 
import numpy 
volume = array(‘Volume’) 
label = array(‘Volume-label’) 
points  = numpy.where( label == 1 )  # or use another label number depending on what you segmented 
values  = volume[points] # this will be a list of the label values 
v…
  </blockquote>
</aside>

<p>I created it seperately as I could not find any thing related to it on the forum.</p>
<p>Thank you</p>
<p>Regards,<br>
Saima Safdar</p>

---
