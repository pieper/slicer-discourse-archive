# Combine Models(difference operation) sometimes result empty mesh?

**Topic ID**: 19169
**Date**: 2021-08-12
**URL**: https://discourse.slicer.org/t/combine-models-difference-operation-sometimes-result-empty-mesh/19169

---

## Post #1 by @StephenLeePeng (2021-08-12 15:27 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> , I have searched surface cut for some time.<br>
I loaded a liver stl model, then I created a closed curve in Markups module, and generate a Baffle model in Baffle Planner module(in SlicerHeart extension), then I switch to Combine Models(in Sandbox extension).<br>
First, I set liver model as input model A, set baffle model as input model B, operation set “Intersection(A&amp;B)”, set “create new model” as Output model. And I can quickly get the intersection result model, named Model_1 about 5 seconds.<br>
Finally, I want to get the result by liver model subtract Model_1, so I choose liver as input model A, Model_1 as input model B, operation set Difference(A-B), set “create new model” as Output model. After click Apply button, the process is running and for a long time, about 1200 seconds, compute finished, Model_2 generated, but it is empty mesh.<br>
I searched from community, and find some related link:</p><aside class="onebox githubissue" data-onebox-src="https://github.com/zippy84/vtkbool/issues/40">
  <header class="source">

      <a href="https://github.com/zippy84/vtkbool/issues/40" target="_blank" rel="noopener nofollow ugc">github.com/zippy84/vtkbool</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/zippy84/vtkbool/issues/40" target="_blank" rel="noopener nofollow ugc">Difference of meshes sometimes an empty mesh</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-02-18" data-time="20:38:37" data-timezone="UTC">08:38PM - 18 Feb 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener nofollow ugc">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">In some cases we get an error message like "Contact ends suddenly at point ..." <span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">and the resulting mesh is empty.

For example:
- subtracting fibula.vtk from guide.vtk results in an empty mesh
- subtracting fibula-dec.vtk from guide-dec.vtk (decimated versions of the two larger data sets) results in an empty mesh

Download meshes from [here](https://1drv.ms/u/s!Arm_AFxB9yqHxYZ1BTAseTBQ95r18w?e=1vriwJ).</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
Above link mentioned some ideas to solve this problem, such as " <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/issues/35" rel="noopener nofollow ugc">Remove non-manifold edges</a>", vtkCleanPolyData.<br>
But when I read CombineModels.py source code, there exist not related class, only use vtkPolyDataBooleanFilter to cut models. So, perhaps I have to add some postprocessed beftore Difference compute, to avoid empty mesh result?<br>
Expect to your reply and appreciate your help in the past.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb36e0c4bbdd0b64825bba8480e5a6f22c85cdfa.jpeg" data-download-href="/uploads/short-url/xyNMqFIDpRF5BxwfpQatfiZnAym.jpeg?dl=1" title="combine Models" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eb36e0c4bbdd0b64825bba8480e5a6f22c85cdfa_2_690x361.jpeg" alt="combine Models" data-base62-sha1="xyNMqFIDpRF5BxwfpQatfiZnAym" width="690" height="361" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eb36e0c4bbdd0b64825bba8480e5a6f22c85cdfa_2_690x361.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eb36e0c4bbdd0b64825bba8480e5a6f22c85cdfa_2_1035x541.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/eb36e0c4bbdd0b64825bba8480e5a6f22c85cdfa_2_1380x722.jpeg 2x" data-dominant-color="BDBCCB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">combine Models</span><span class="informations">1919×1006 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1CDGMM0YqLg8yk2v7YUKcpN5yFooiLTdN/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1CDGMM0YqLg8yk2v7YUKcpN5yFooiLTdN/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1CDGMM0YqLg8yk2v7YUKcpN5yFooiLTdN/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1CDGMM0YqLg8yk2v7YUKcpN5yFooiLTdN/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">surfaceCutDemo0812.zip</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
Above link is the mrml file and model files.</p>

---

## Post #2 by @lassoan (2021-08-12 17:57 UTC)

<p>You cannot subtract the Model_1 part from the original liver, as most of the points are coincident. If you want to get the other half of the liver then you can probably flip the baffle surface, or ask vtkbool developer about it.</p>
<p>You can also use Dynamic Modeler tool to partition the liver. If you just need planar cuts then you can use the fast and accurate “Plane cut” tool, but if you want to cut along an arbitrary curve then you can use “Curve cut” tool.</p>
<p>For simulating liver resection, there is a tool specifically designed for this, which is currently being refactored and improved by the Alive project (see <a href="https://github.com/ALive-research/Slicer-LiverAnalysis">Slicer extension</a> here). <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> can give you more information on the status of this.</p>

---

## Post #3 by @StephenLeePeng (2021-08-13 14:08 UTC)

<p>Thanks for your reply.<br>
As you mentioned, after intersection operation finished first time, I flip the Baffle surface, by switch to Surface Toolbox module, select the “Normals” or “Compute Normals” option in windows/linux slicer version, checked the “Flip normals” and “Splitting” checkbox, then click Apply button, a flipped surface will computed.<br>
Finally, I switch to Combine models module again, use the flipped surface to intersect the liver stl model second time, after click Apply button and wait for 4~5 seconds,  upper part of liver will be cut success by flipped surface.</p>
<p>Followed img is liver been segmented into two parts, by baffle surface and flipped baffle surface.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/147bc260a6efa0e62256726dffc99e442b07115a.png" data-download-href="/uploads/short-url/2VcHyfGdbTyZLUHW4eRmbEDSxKO.png?dl=1" title="微信图片_20210813220153" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/147bc260a6efa0e62256726dffc99e442b07115a_2_620x500.png" alt="微信图片_20210813220153" data-base62-sha1="2VcHyfGdbTyZLUHW4eRmbEDSxKO" width="620" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/147bc260a6efa0e62256726dffc99e442b07115a_2_620x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/147bc260a6efa0e62256726dffc99e442b07115a_2_930x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/147bc260a6efa0e62256726dffc99e442b07115a.png 2x" data-dominant-color="1B311E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">微信图片_20210813220153</span><span class="informations">1043×841 227 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
