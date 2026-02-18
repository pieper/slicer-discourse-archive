# How to make nasal cavity 3 d model in 3D slicer which can be used for simulations?

**Topic ID**: 19701
**Date**: 2021-09-16
**URL**: https://discourse.slicer.org/t/how-to-make-nasal-cavity-3-d-model-in-3d-slicer-which-can-be-used-for-simulations/19701

---

## Post #1 by @Sliceeeeee (2021-09-16 11:06 UTC)

<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:<strong>strong text</strong></p>

---

## Post #2 by @lassoan (2021-09-16 18:49 UTC)

<p>You can generate a 3D model of the nasal cavity by segmenting a CT (maybe an MRI) image. <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">This page</a> is a good starting point for learning segmentation.</p>
<p>Probably a simple thresholding (using Threshold effect) followed by median filtering (using Smoothing effect) will give you a good model. You can fix small errors using Paint effect.</p>
<p>You can check the segmented model from inside flythrough perspective using Endoscopy module:</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/5902584f9fd9a4825195c349f8778c16ef70db06.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/5902584f9fd9a4825195c349f8778c16ef70db06.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/5902584f9fd9a4825195c349f8778c16ef70db06.mp4</a>
    </source></video>
  </div><p></p>

---

## Post #3 by @slicer365 (2021-09-16 23:35 UTC)

<p>How to make the red point move as is shown in this video?</p>

---

## Post #4 by @lassoan (2021-09-17 00:00 UTC)

<p>Currently, the cursor is a small sphere. You can add a markups fiducial point at (0,0,0) position and apply the transform that the Endoscopy module creates. This is how I displayed the red sphere.</p>
<p>I’ll update the Endoscopy module so that it creates a markups fiducial node as cursor by default, because it is easier to adjust its size it has more visualization options.</p>

---

## Post #5 by @Sliceeeeee (2021-09-17 14:49 UTC)

<p>While constructing the 3D model of nasal cavity should I paint the region filled with air or the region contains bones and all ? (I am very new in this software)</p>

---

## Post #6 by @lassoan (2021-09-17 20:17 UTC)

<p>No need to fill the air (the camera will always be inside the “air” region anyway). You can segment bones and soft tissue separately, but bones will only become visible if you simulate cutting of soft tissue (otherwise soft tissue will always occlude bones, so you will not see them).</p>
<p>Pull request has been submitted that changes the endoscopy cursor to markups fiducial point:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/5872">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/5872" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/5872" target="_blank" rel="noopener">ENH: Use markups fiducial point as cursor in Endoscopy module</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>lassoan:endoscopy-markups-cursor</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-09-17" data-time="20:24:33" data-timezone="UTC">08:24PM - 17 Sep 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="1 commits changed 1 files with 32 additions and 10 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/5872/files" target="_blank" rel="noopener">
          <span class="added">+32</span>
          <span class="removed">-10</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">The user can more easily adjust size and appearance (scaling, projection, occlud<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/5872" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ed visibility, etc.) more flexibly than a model node.
In the module logic class, developers can choose between using a model or a markups fiducial.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @Sliceeeeee (2021-09-18 01:10 UTC)

<p>Actually I am not getting the point, I am trying to do it by thresholding and masking the region which contains the air only, and filling the paint there . Is the correct way of doing ?</p>

---

## Post #8 by @lassoan (2021-09-18 02:39 UTC)

<p>You only need to Threshold effect. Set the intensity range so that it includes everything but air (soft tissue, bones, etc.), then click Apply. That’s all. If you want, you can apply some Smoothing and touch up the segmentation using Paint effect.</p>
<p>You only wrote that you want to use the model for “simulations”. What kind of simulations do you want to do? What do you want to simulate, just navigation in the nasal cavity, or also drilling/cutting? Do you plan to use Slicer for visualization or you just need to create a model and use it in some other software?</p>

---

## Post #9 by @Sliceeeeee (2021-09-18 03:34 UTC)

<p>I want to do CFD simulation for air flow  inside nasal cavity,</p>

---

## Post #10 by @lassoan (2021-09-18 04:23 UTC)

<p>I see, OK, then your simulation domain is the air, so you actually need to get the air segmented.</p>
<p>The techniques described here should work:</p>
<aside class="quote" data-post="1" data-topic="15487">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/b5a626/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/need-help-for-segment-nasal-cavity-and-turbinates/15487">Need help for segment nasal cavity and turbinates</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi! I have a sinonasal CT and I need to segment the nasal cavities and turbinates in order to get the volume of them. Could someone help me? Thanks!
  </blockquote>
</aside>


---

## Post #11 by @Sliceeeeee (2021-09-30 12:43 UTC)

<p>Directly 3d model of airway will be imported to Ansys or any before processing is required?</p>

---

## Post #12 by @lassoan (2021-09-30 12:54 UTC)

<p>Can Ansys import an STL, PLY, or OBJ file and create a volumetric mesh from it for the simulation? If yes, then you can use the exported segmentation as is.</p>
<p>If Ansys cannot generate volumetric mesh then you can create that using SegmentMesher extension, then convert the resulting VTK  or VTU file to a format that Ansys can load using <code>meshio</code> Python package.</p>

---

## Post #13 by @Sliceeeeee (2021-10-01 10:52 UTC)

<p>I am able to import it to the ansys but i am not able to mesh it ,</p>

---

## Post #14 by @Sliceeeeee (2021-10-01 11:29 UTC)

<p>i used segmentmesher extension , it showed the that the model is generated but i could not see any meshing . please help me in this regard .</p>

---

## Post #15 by @lassoan (2021-10-01 14:16 UTC)

<p>If you don’t cut into the mesh then you will not see what is inside (surface or volumetric mesh). See the <a href="https://github.com/lassoan/SlicerSegmentMesher#tutorial">module’s tutorial</a> for step-by-step instructions on how to cut into a model and visualize mesh elements.</p>

---
