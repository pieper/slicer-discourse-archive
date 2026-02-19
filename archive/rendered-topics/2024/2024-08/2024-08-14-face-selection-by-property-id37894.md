---
topic_id: 37894
title: "Face Selection By Property"
date: 2024-08-14
url: https://discourse.slicer.org/t/37894
---

# Face Selection by Property

**Topic ID**: 37894
**Date**: 2024-08-14
**URL**: https://discourse.slicer.org/t/face-selection-by-property/37894

---

## Post #1 by @evaherbst (2024-08-14 20:17 UTC)

<p>Hello,</p>
<p>I have a few questions about face selection.</p>
<ol>
<li>Is there a tool to select faces by clicking on them / with a lasso?</li>
<li>Do methods exist do grow this selection?</li>
<li>Are there methods to select faces based on angles between faces? E.g. to detect edges?</li>
</ol>
<p><a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> I saw you implemented a “select by points” tool in the Dynamic modeler - once I select the faces I would want to export them similarly to a new surface. Have you done any work with face selection beyond the distance based selection in that tool?</p>
<p>The application is to try to select regions based on changes in curvature and then export the selected faces as a new surface mesh.</p>
<p>Thanks,<br>
Eva</p>

---

## Post #2 by @mau_igna_06 (2024-08-15 00:29 UTC)

<p>I think there is a property of the <code>vtkFastMarchingGeodesicDistance</code> that allows you to grow a seed using a defined cellsScalarArray. I remember that the paper that presented this geodesic distance filter showed using curvature (calculated from the curvature filters on vtk examples) to “weight” the growing “speed” as you want</p>
<p>HIH</p>

---

## Post #3 by @lassoan (2024-08-15 05:18 UTC)

<p>You can use the <code>Curve cut</code> tool in Dynamic Modeler module with constraint the curve to the surface and preferring going through high‐curvature points:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="nLva95ZF4ko" data-video-title="Extract one side of a closed surface mesh" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=nLva95ZF4ko" target="_blank" class="video-thumbnail" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/nLva95ZF4ko/maxresdefault.jpg" title="Extract one side of a closed surface mesh" width="690" height="388">
  </a>
</div>

<p>You can combine this with cutting planes and other curves to partition complex surfaces.</p>
<p>It would not be hard to adapt “Grow from seeds” algorithm to surface meshes. It would allow painting a surface by placing one or few markup points on each region. A student with  C++ and VTK experience could implement it in a couple of months (could be a nice Masters project).</p>

---

## Post #4 by @mau_igna_06 (2024-08-15 12:13 UTC)

<p>It would be nice to have faces selection tool just like Blender or this one:</p><div class="youtube-onebox lazy-video-container" data-video-id="15bMrsYD1-4" data-video-title="Automate your workflow – Example of a surgical guide design" data-video-start-time="151" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=15bMrsYD1-4&amp;t=151" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/15bMrsYD1-4/maxresdefault.jpg" title="Automate your workflow – Example of a surgical guide design" width="690" height="388">
  </a>
</div>


---

## Post #5 by @lassoan (2024-08-15 12:28 UTC)

<p><code>Curve cut</code> and <code>Select by points</code> dynamic modeler tools cover the “draw” and “paint” style selections quite well. They are both parametric editing tools, allowing fine-tuning and corrections anytime, which is generally considered to be superior to direct editing (that is shown in the Materialise video above). Usability of the current dynamic modeler tools is not optimal, because we did not develop the Dynamic Modeler module for end users, but to have a parametric editor “engine” for a future “Model Editor” module. The “Model Editor” will work similarly to the “Segment Editor” module, but will opearate on models instead of segmentations.</p>

---

## Post #6 by @evaherbst (2024-08-15 16:31 UTC)

<p>Thanks both!</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> I’ll try the curve cut method you proposed, looks good!</p>
<p><a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> yes I was also thinking of the Blender functionality.</p>
<p>The node selection approach I was thinking of was this tool in Artisynth, in which you can select regions based on the angles between faces (right now only nodes can be selected, not faces): <a href="https://www.artisynth.org/manuals/index.jsp" class="inline-onebox" rel="noopener nofollow ugc">Help - Eclipse Platform</a></p>
<p>Looking forward to a Model Editor in the future.<br>
If at some point I have a suitable master’s student I will also consider this as a project.</p>
<p>Thanks!<br>
Eva</p>

---

## Post #7 by @pieper (2024-08-15 16:51 UTC)

<p>I have also seen people have good luck accessing the point normals from the polydata as a numpy array and then assigning selection scalars based on simple clustering of the normals.  This works when the models are fairly smooth and the edges are fairly distinct.</p>

---

## Post #8 by @evaherbst (2024-08-15 16:59 UTC)

<p>Thanks Steve! By clustering do you mean checking the change in normals over n faces, instead of just calculating the normals difference between two adjanet faces?<br>
I was thinking of that approach as well…</p>
<p>The humerus is a bit tricky since the edges are not super sharp. I am trying to isolate the articular surface.</p>
<p>Here is using Andras’s approach, unfortunately that doesn’t work well:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/95af91f3d79f6df2c71f8fc978e641a5df8b8698.png" data-download-href="/uploads/short-url/lmbiCzZTpVSCJakG7Unx2Ue2aUg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/95af91f3d79f6df2c71f8fc978e641a5df8b8698_2_562x500.png" alt="image" data-base62-sha1="lmbiCzZTpVSCJakG7Unx2Ue2aUg" width="562" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/95af91f3d79f6df2c71f8fc978e641a5df8b8698_2_562x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/95af91f3d79f6df2c71f8fc978e641a5df8b8698_2_843x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/95af91f3d79f6df2c71f8fc978e641a5df8b8698_2_1124x1000.png 2x" data-dominant-color="999699"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1172×1041 163 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>That is why I think face selection and growing is nice, with some constraint based on normals - so I can avoid it going past the first concave area and spreading into the convex area.</p>

---

## Post #9 by @pieper (2024-08-15 17:21 UTC)

<p>The place where I saw clustering the normals working well was in isolating the top and bottom plates of a vertebral body, where there was a clear distinction between the normals pointing up or down vs the ones on the side.  I agree the femural head isn’t as cleanly defined.  Which edges are you trying to define?</p>

---

## Post #10 by @mau_igna_06 (2024-08-15 17:23 UTC)

<p>Here is an algorithm I think may work: Place a fiducial, take the nearest cell of the model to that seed, save the normal of that cell, calculate the normal of all other cells, compare the angle between the normals using the threshold criteria you want, save results on a cellArray, use that for vtkThreshold filter</p>
<p>There are examples online (those instructions may not be thoroughgoing)</p>

---

## Post #11 by @evaherbst (2024-08-15 17:33 UTC)

<p>Thank you! Yes, I was thinking a similar approach if I were to make it from scratch.</p>
<p>I’ll look into it/have my fall student work on it.</p>
<p>Thank you!<br>
Eva</p>

---

## Post #12 by @evaherbst (2024-08-15 17:39 UTC)

<p>Thanks Steve!<br>
I just saw someone present this (I think using slicer) at CMBBE - I think it was Prof. Andersen.</p>
<p>I am trying to do something like this (I selected it manually but am exploring options to automate). Currently trying to decide whether to go down Slicer or Blender or Artisynth route.<br>
I am not sure how well it will work on the humerus, might need additional constraints such as distance from seed etc so it does not grow too much.</p>
<p>As you can see the boundary curvature changes are quite subtle</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/189175ec9d3e9cfd1303537fa56a7ecad20ec84f.png" data-download-href="/uploads/short-url/3vl6EnqjzZQtZvrcm5ekCBWftEz.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/189175ec9d3e9cfd1303537fa56a7ecad20ec84f_2_567x500.png" alt="image" data-base62-sha1="3vl6EnqjzZQtZvrcm5ekCBWftEz" width="567" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/189175ec9d3e9cfd1303537fa56a7ecad20ec84f_2_567x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/189175ec9d3e9cfd1303537fa56a7ecad20ec84f_2_850x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/189175ec9d3e9cfd1303537fa56a7ecad20ec84f_2_1134x1000.png 2x" data-dominant-color="A2A0A7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1302×1147 147 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cb5ed228f1e5e00ded66d673708a7fe237a5dfe8.png" data-download-href="/uploads/short-url/t164ViyZq5pz8MCe7sq8qP77iWY.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb5ed228f1e5e00ded66d673708a7fe237a5dfe8_2_556x500.png" alt="image" data-base62-sha1="t164ViyZq5pz8MCe7sq8qP77iWY" width="556" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb5ed228f1e5e00ded66d673708a7fe237a5dfe8_2_556x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb5ed228f1e5e00ded66d673708a7fe237a5dfe8_2_834x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cb5ed228f1e5e00ded66d673708a7fe237a5dfe8_2_1112x1000.png 2x" data-dominant-color="A19FA8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1289×1158 156 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @muratmaga (2024-08-16 17:43 UTC)

<aside class="quote no-group" data-username="evaherbst" data-post="12" data-topic="37894">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/evaherbst/48/65595_2.png" class="avatar"> evaherbst:</div>
<blockquote>
<p>As you can see the boundary curvature changes are quite subtle</p>
</blockquote>
</aside>
<p>Did you run uniform remesh on this model? It seems vertices are quite sparse, and if you want to have smooth curve at the diaphysis you might have to work with a higher resolution mesh (at least those high curvature areas).</p>

---

## Post #14 by @evaherbst (2024-08-23 12:25 UTC)

<p>I did but not high enough. Just tried it again and the results are much much better, thanks so much for the tip.<br>
Still a bit overshooting the articular surface but will get a student working on refining this. Thanks all for your help!</p>
<p>Best,<br>
Eva</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c9b7e386b1e96ba0484e0b25ff33dcc161e70d8.png" data-download-href="/uploads/short-url/k3RZgzzORewEIM7E7Py3DfWx4jS.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c9b7e386b1e96ba0484e0b25ff33dcc161e70d8_2_495x500.png" alt="image" data-base62-sha1="k3RZgzzORewEIM7E7Py3DfWx4jS" width="495" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c9b7e386b1e96ba0484e0b25ff33dcc161e70d8_2_495x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c9b7e386b1e96ba0484e0b25ff33dcc161e70d8_2_742x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c9b7e386b1e96ba0484e0b25ff33dcc161e70d8_2_990x1000.png 2x" data-dominant-color="9FA0A9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1107×1118 98.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff627731c2d372dc25f82f39a3d359cca31112c1.png" data-download-href="/uploads/short-url/AreIqoZHkQiz8oXuvgiGO0VM2lj.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff627731c2d372dc25f82f39a3d359cca31112c1_2_597x500.png" alt="image" data-base62-sha1="AreIqoZHkQiz8oXuvgiGO0VM2lj" width="597" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff627731c2d372dc25f82f39a3d359cca31112c1_2_597x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff627731c2d372dc25f82f39a3d359cca31112c1_2_895x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff627731c2d372dc25f82f39a3d359cca31112c1.png 2x" data-dominant-color="A2A29F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">951×796 77.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #15 by @lassoan (2024-08-24 07:21 UTC)

<p>Looking at the images above, it seems to me that the boundary of the articular surface is not marked everywhere by sudden change in the surface normal direction (see green arrows). No matter how you smooth the normals or constrain region growing, you would not get the actual articular surface in these areas.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9fd7ebd1567452d2b0c3001f9ea7c6c13f3b2cb0.jpeg" data-download-href="/uploads/short-url/mO2wERyu0HzrRUhJucpeiiJ9UFq.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9fd7ebd1567452d2b0c3001f9ea7c6c13f3b2cb0_2_553x500.jpeg" alt="image" data-base62-sha1="mO2wERyu0HzrRUhJucpeiiJ9UFq" width="553" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9fd7ebd1567452d2b0c3001f9ea7c6c13f3b2cb0_2_553x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9fd7ebd1567452d2b0c3001f9ea7c6c13f3b2cb0_2_829x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9fd7ebd1567452d2b0c3001f9ea7c6c13f3b2cb0.jpeg 2x" data-dominant-color="A5A3AB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">868×784 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Instead, you could determine what part of the mesh is the articular surface by rotating the mesh around a bit around an axis and keep that mesh regions that is close to the original (non-rotated) surface. The center of rotation on the surface (marked with an <code>X</code> in the image) and the axis orientation can be easilty set approximately. You only need 4 parameters (shift of the center of rotation on the surface in two directions; tilting of the rotation axis in two directions) to get the true, optimal center of rotation axis position from the initial guess, which is a simple optimization problem (small number of unknowns, smooth objective function, fast computation of the maximized value). It should be very easy to write a small Python function that computes the size of the articular surface for the current axis position and angle (by rotating the surface a bit, computing distance using polydata distance filter, applying threshold filter, getting largest connected component) and use it in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#specify-a-sphere-by-multiple-control-points">scipy.optimize</a>. The axis position and orientation could be very useful for computing many other metrics for the joint.</p>

---

## Post #16 by @evaherbst (2024-08-26 17:17 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a> for your input!</p>
<p>One goal of isolating the articular surface is to then fit a sphere to estimate the center of rotation of the humeral head.<br>
I didn’t think of first estimating a rotational axis roughly through the center and using that to get the articular surface- it is a nice idea. I will explore it.</p>
<p>Yes, there is no sudden change in normals at this region, rather a slight change in concavity, but I would need to test if this is consistent enough to detect and use.</p>
<p>Thanks again!<br>
Eva</p>

---

## Post #17 by @lassoan (2024-08-26 21:18 UTC)

<p>I suggested to compute overlap of the surface with itself after slight rotation because I did not want to assume a spherical surface. But if you can assume that the articular surface is a sphere then the task is even simpler. You still have just 4 unknowns (sphere center position in 3D, radius), and if you implement a Python function that computes the goodness of the fit (e.g., number of mesh points that are closer to the sphere surface than a small threshold), then scipy.optimize should be able to compute those unknowns.</p>

---

## Post #18 by @evaherbst (2024-08-27 10:04 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>! The articular region is almost spherical - I saw a study showing it is slightly elliptical but I think it depends on the patient. This idea is really nice as well - going by number of points close to a sphere surface (instead of minimizing mean error to surface which would presumably place the sphere more in the center of the proximal bone including the trochanters).</p>
<p>Thanks again!<br>
Eva</p>

---

## Post #19 by @evaherbst (2024-09-02 15:56 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Just an update - thanks again for your suggestions. I have a student starting in October on this project, we will keep you updated on how well the different methods work</p>

---
