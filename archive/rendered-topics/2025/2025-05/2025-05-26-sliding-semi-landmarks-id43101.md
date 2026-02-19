---
topic_id: 43101
title: "Sliding Semi Landmarks"
date: 2025-05-26
url: https://discourse.slicer.org/t/43101
---

# Sliding semi-landmarks

**Topic ID**: 43101
**Date**: 2025-05-26
**URL**: https://discourse.slicer.org/t/sliding-semi-landmarks/43101

---

## Post #1 by @elg67 (2025-05-26 12:11 UTC)

<p>Hiya! I’m currently trying to apply sliding semi-landmarks to a dataset (x20 crania/scapulae/clavicles/pelvises) with fixed landmarks already applied. I tried to use the curves to create SSL between landmarks as per Rolfe et al., 2021, however this approach took a lot of time and would slow down the application, therefore I deemed it inefficient. Is there another approach (e.g. using PseudoLM) that would allow me to create the same number of SSL per structure in the same position (e.g. mid-point between landmarks A and B etc…) and replicate this using ALPACA? Thanks <img src="https://emoji.discourse-cdn.com/twitter/folded_hands.png?v=14" title=":folded_hands:" class="emoji" alt=":folded_hands:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @muratmaga (2025-05-26 16:00 UTC)

<p>The answer depends on area you are trying to landmark as well as your landmark distribution. Without seeing that it is hard for me to suggest something, but you might want to give the recent grid landmarks a try.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerMorph/Tutorials/blob/main/GridBasedLandmarking/README.md">
  <header class="source">

      <a href="https://github.com/SlicerMorph/Tutorials/blob/main/GridBasedLandmarking/README.md" target="_blank" rel="noopener nofollow ugc">github.com/SlicerMorph/Tutorials</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerMorph/Tutorials/blob/main/GridBasedLandmarking/README.md" target="_blank" rel="noopener nofollow ugc">GridBasedLandmarking/README.md</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/SlicerMorph/Tutorials/blob/main/GridBasedLandmarking/README.md" rel="noopener nofollow ugc"><code>main</code></a>
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



  This file has been truncated. <a href="https://github.com/SlicerMorph/Tutorials/blob/main/GridBasedLandmarking/README.md" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @elg67 (2025-05-28 13:48 UTC)

<p>Hiya Murat,</p>
<p>That’s excellent, I will give this a go on my structures!</p>
<p>Are there any modifications I need to make to the .json file if I’m exporting these sliding semi-landmarks, e.g. saving as ‘description:semi’ when merging, changes to R code when exporting etc…?</p>

---

## Post #4 by @elg67 (2025-05-29 13:19 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/6912c3ecda1580770164dc399570327efc565ddc.jpeg" data-download-href="/uploads/short-url/eZwl0SfsRyKVX0F6mIdjh89JzL6.jpeg?dl=1" title="cranium_SSL" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/6912c3ecda1580770164dc399570327efc565ddc_2_574x500.jpeg" alt="cranium_SSL" data-base62-sha1="eZwl0SfsRyKVX0F6mIdjh89JzL6" width="574" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/6912c3ecda1580770164dc399570327efc565ddc_2_574x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/6912c3ecda1580770164dc399570327efc565ddc_2_861x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/6912c3ecda1580770164dc399570327efc565ddc_2_1148x1000.jpeg 2x" data-dominant-color="A8A497"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">cranium_SSL</span><span class="informations">1441×1255 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69eaee9774fd42a12efdc5fb2f8d76d450821959.jpeg" data-download-href="/uploads/short-url/f6ZtnBvwn6efE8MuwXer4qVNcwx.jpeg?dl=1" title="sg_SSL" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69eaee9774fd42a12efdc5fb2f8d76d450821959_2_456x500.jpeg" alt="sg_SSL" data-base62-sha1="f6ZtnBvwn6efE8MuwXer4qVNcwx" width="456" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69eaee9774fd42a12efdc5fb2f8d76d450821959_2_456x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69eaee9774fd42a12efdc5fb2f8d76d450821959_2_684x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69eaee9774fd42a12efdc5fb2f8d76d450821959_2_912x1000.jpeg 2x" data-dominant-color="A9A4A2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">sg_SSL</span><span class="informations">1348×1476 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb2e4904820ef52c115421c4c5a204c7f2f7d3de.jpeg" data-download-href="/uploads/short-url/zQ30FcSqSg9iVp7Pl3CcGPTZsAe.jpeg?dl=1" title="pelvis_SSL" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb2e4904820ef52c115421c4c5a204c7f2f7d3de_2_652x500.jpeg" alt="pelvis_SSL" data-base62-sha1="zQ30FcSqSg9iVp7Pl3CcGPTZsAe" width="652" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb2e4904820ef52c115421c4c5a204c7f2f7d3de_2_652x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb2e4904820ef52c115421c4c5a204c7f2f7d3de_2_978x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb2e4904820ef52c115421c4c5a204c7f2f7d3de_2_1304x1000.jpeg 2x" data-dominant-color="999894"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pelvis_SSL</span><span class="informations">1872×1435 173 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’ve attached images of my semilandmarks so far - they appear to be more uniformly distributed than the PseudoLM generated LMs and allow me to capture specific areas (e.g. the birth canal), however I’m concerned by the time taken to complete each one as well as the relatively low number of SLMs compared to automated methods - is this sustainable?</p>
<p>Many Thanks,<br>
Eve</p>

---

## Post #5 by @muratmaga (2025-05-30 01:24 UTC)

<aside class="quote no-group" data-username="elg67" data-post="4" data-topic="43101">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/ecb155/48.png" class="avatar"> elg67:</div>
<blockquote>
<p>I’m concerned by the time taken to complete each one as well as the relatively low number of SLMs compared to automated methods - is this sustainable?</p>
</blockquote>
</aside>
<p>This is something only you can decide. PseudoLMGenerator is fast, but cannot generate same number of landmark on every sample. So you will have to use a method to transfer those landmarks to individual subjects. You can do that via ALPACA (which uses a point-cloud registration) or projectSemiLMs (which uses a landmarks to transfer).</p>
<p>The other alternative is a new extension we introduced: DenseCorrespondenceAnalysis (DeCA). You will need some fixed landmarks to start the process, but then it will both build a template and then transfer semi-landmarks to the subjects. See <a href="https://github.com/SlicerMorph/SlicerDenseCorrespondenceAnalysis?tab=readme-ov-file" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerMorph/SlicerDenseCorrespondenceAnalysis: Dense Correspondence Analysis for Surfaces</a> (and the tutorial linked there).</p>
<p>ps. Couple issues.</p>
<ol>
<li>You are not creating sliding landmark. You are generating semi-landmarks. Sliding is a technique used during the superimposition of landmarks, and specifically applied to the landmarks designated as “semi or pseudoLMs” (io.e., they are not fixed)</li>
<li>You should not analyze landmarks that belong to different anatomical systems jointly. A major assumption in the analysis is that landmarks designate a single rigid body. Cranium and mandible together is not a single rigid body (they rotate with respect to each other through TMJ).</li>
</ol>

---
