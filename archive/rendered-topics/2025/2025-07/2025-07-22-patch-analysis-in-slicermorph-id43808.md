---
topic_id: 43808
title: "Patch Analysis In Slicermorph"
date: 2025-07-22
url: https://discourse.slicer.org/t/43808
---

# Patch Analysis in SlicerMorph

**Topic ID**: 43808
**Date**: 2025-07-22
**URL**: https://discourse.slicer.org/t/patch-analysis-in-slicermorph/43808

---

## Post #1 by @Jones (2025-07-22 14:32 UTC)

<p>Is it possible to collect semi-landmarks as patches in SlicerMorph? I can’t figure out how to do this with the Markups function. Thank you very much for your help.</p>

---

## Post #2 by @muratmaga (2025-07-22 15:09 UTC)

<p>Yes, you can use the PlaceLandmarkGrid functionality, which makes use of SurfaceMarkups. See the tutorial here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/Tutorials/blob/main/GridBasedLandmarking/README.md">
  <header class="source">

      <a href="https://github.com/SlicerMorph/Tutorials/blob/main/GridBasedLandmarking/README.md" target="_blank" rel="noopener">github.com/SlicerMorph/Tutorials</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/Tutorials/blob/main/GridBasedLandmarking/README.md" target="_blank" rel="noopener">GridBasedLandmarking/README.md</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/SlicerMorph/Tutorials/blob/main/GridBasedLandmarking/README.md" rel="noopener"><code>main</code></a>
</div>


      <pre><code class="lang-md"># Grid-based landmarking
This tutorial describes how to create a series of grid patches using the `PlaceLandmarkGrid` module that can be combined into a set of labeled manual landmarks and semi-landmarks using the `MergeMarkups` module.

To use this method, you will need a 3D model(s) and its accompanying set of fixed landmarks. For this tutorial download the mouse skull models and landmarks posted here: [mouse skull sample data](https://github.com/SlicerMorph/Mouse_Models/tree/newModels/newModels).

----

## PlaceLandmarkGrid
This module can be used to generate, visualize, and interactively edit square patches of semi-landmarks by specifying four corner points on a model. A template grid with a user-specified number of semi-landmark points is registered to the corner points via a thin-plate-spline deformation and the vertices of the sampling grid are projected to the surface of the model along the normal vector of the patch at that point. 

The corners of the grid can be selected using two different methods.
1. Placing a new landmark point
2. Selecting the position from an existing landmark point.

This tutorial will demonstrate both methods. After placement of the grids, the `PlaceLandmarkGrid` module will be used to merge the patches together into a single landmark node and remove overlapping points.

### Place grid by placing points in the scene
1. Open to the `PlaceLandmarkGrid` module. If this is the first time you have opened it, you will need to wait for a short time while necessary Python libraries are installed. Load `A_J_Skull.fcsv` and `A_J_Skull.ply` from the sample data folder `newModels` into Slicer.
&lt;img src="./images/DownloadData.png"&gt;

</code></pre>



  This file has been truncated. <a href="https://github.com/SlicerMorph/Tutorials/blob/main/GridBasedLandmarking/README.md" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Jones (2025-07-22 17:35 UTC)

<p>Thank you so much for your help.</p>

---
