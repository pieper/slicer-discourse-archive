---
topic_id: 5921
title: "Points And Surface Interaction Between Segment Node And Mode"
date: 2019-02-25
url: https://discourse.slicer.org/t/5921
---

# Points and surface interaction between segment node and model node

**Topic ID**: 5921
**Date**: 2019-02-25
**URL**: https://discourse.slicer.org/t/points-and-surface-interaction-between-segment-node-and-model-node/5921

---

## Post #1 by @SebastianE93 (2019-02-25 16:02 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11.0<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Sorry for my question, i’m a newby</p>
<p>I’m trying to determine how many points of the surface of a vtkMRMLSegmentationNode is interacting with a vtkModelNode.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/2X/a/a02137308fd73a3213a147ff36b63f8599b65fff.png" data-download-href="/uploads/short-url/mQzyG4WxdTmlu4oM8w5xYLV0oa3.png?dl=1" title="Captura.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a02137308fd73a3213a147ff36b63f8599b65fff.png" alt="Captura.PNG" width="690" height="366" data-dominant-color="E7E5EC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura.PNG</span><span class="informations">1131×600 4.58 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>In the image I try to explain better. The cylinder is passing through the cube and I want to know witch is the surface percentage that is touching the cube (red surface 60%) and witch is not (40%).</p>
<p>Thanks you in advance !</p>

---

## Post #2 by @SebastianE93 (2019-02-21 20:11 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11.0<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Sorry for my question, i’m a newby</p>
<p>I’m trying to determine how many points of the surface of a vtkMRMLSegmentationNode is interacting with a vtkModelNode.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a02137308fd73a3213a147ff36b63f8599b65fff.png" data-download-href="/uploads/short-url/mQzyG4WxdTmlu4oM8w5xYLV0oa3.png?dl=1" title="Captura" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a02137308fd73a3213a147ff36b63f8599b65fff.png" alt="Captura" data-base62-sha1="mQzyG4WxdTmlu4oM8w5xYLV0oa3" width="690" height="366" data-dominant-color="E7E5EC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura</span><span class="informations">1131×600 4.58 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>In the image I try to explain better. The cylinder is passing through the cube and I want to know witch is the surface percentage that is touching the cube (red surface 60%) and witch is not (40%).</p>
<p>Thanks you in advance !</p>

---

## Post #3 by @cpinter (2019-02-25 16:36 UTC)

<p>The only method I know of currently is to use the collision detection filter. It takes two vtkPolyData objects and the output is the number of contacts. It cannot tell you surface area of the contact, but can also give you the list of points that are colliding. An example of usage can be found here:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerRt/SlicerRT/blob/master/RoomsEyeView/Logic/vtkSlicerRoomsEyeViewModuleLogic.cxx#L636-L638" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/SlicerRT/blob/master/RoomsEyeView/Logic/vtkSlicerRoomsEyeViewModuleLogic.cxx#L636-L638" target="_blank" rel="nofollow noopener">SlicerRt/SlicerRT/blob/master/RoomsEyeView/Logic/vtkSlicerRoomsEyeViewModuleLogic.cxx#L636-L638</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="636" style="counter-reset: li-counter 635 ;">
<li>// Set up collision detection between components
</li>
<li>this-&gt;GantryTableTopCollisionDetection-&gt;SetInput(0, gantryModel-&gt;GetPolyData());
</li>
<li>this-&gt;GantryTableTopCollisionDetection-&gt;SetInput(1, tableTopModel-&gt;GetPolyData());
</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
Please be mindful that in Slicer, MRML nodes may be under transforms, and those need to be applied using vtkTransformPolyDataFilter so that the vtkPolyData objects (used both in model nodes and segmentation nodes’ closed surface representation) are in the right coordinate system (as shown in Slicer). The example I linked to above also contains this step.</p>
<p>Also please note that the integration of this class into VTK is in progress, if you don’t want to use SlicerRT, see this MR: <a href="https://gitlab.kitware.com/vtk/vtk/merge_requests/4527" rel="nofollow noopener">https://gitlab.kitware.com/vtk/vtk/merge_requests/4527</a><br>
Until then, you’ll need to use SlicerRT’s own class.</p>

---

## Post #4 by @SebastianE93 (2019-02-28 00:47 UTC)

<p>Thanks you!! it seems right, I will try</p>

---
