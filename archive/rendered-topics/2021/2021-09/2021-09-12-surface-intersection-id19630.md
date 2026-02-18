# Surface Intersection

**Topic ID**: 19630
**Date**: 2021-09-12
**URL**: https://discourse.slicer.org/t/surface-intersection/19630

---

## Post #1 by @Fluvio_Lobo (2021-09-12 14:33 UTC)

<p>Hello,</p>
<p>I am trying to calculate the intersection of two surface models to design an orthognathic splint.<br>
The intersection will be used as a flag for the mandible to stop rotating and set the occlusion.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/3311794f08951d37237b2db0df44655ebb71a8a8.png" data-download-href="/uploads/short-url/7hLMTgjxqcxI5dp6mdtdyfCJ1Hy.png?dl=1" title="intermediate" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/3311794f08951d37237b2db0df44655ebb71a8a8_2_517x276.png" alt="intermediate" data-base62-sha1="7hLMTgjxqcxI5dp6mdtdyfCJ1Hy" width="517" height="276" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/3311794f08951d37237b2db0df44655ebb71a8a8_2_517x276.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/3311794f08951d37237b2db0df44655ebb71a8a8_2_775x414.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/3311794f08951d37237b2db0df44655ebb71a8a8_2_1034x552.png 2x" data-dominant-color="9897AF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">intermediate</span><span class="informations">1171×626 297 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I found <a href="https://discourse.slicer.org/t/new-experimental-feature-boolean-operations-union-intersection-difference-on-meshes/16048">this post</a> but cannot seem to find the <strong>Sandbox</strong> extension nor the <strong>Combine Models</strong> module! I am running <strong>Slicer 4.13.0-2021-07-29 r30081 / 3b37852</strong></p>
<p>If there are other clever ways of doing this, without having to create segments out of the models, I am all ears!</p>
<p>Thank you,</p>

---

## Post #2 by @lassoan (2021-09-12 14:44 UTC)

<p>If your input data set is a CT volume then creating the splint using Segment Editor is the most suitable tool (as you have relatively low accuracy due to the limited resolution of the CT volume).</p>
<p>If you also have surface scans then it may make sense to use the high-accuracy scanned surfaces directly. For this, the Combine models module can be used. You can find Sandbox extension in the very latest Slicer Preview Release (the Extensions Server is being transitioned to a new system, so it is more complicated to access extensions in older Slicer versions).</p>

---

## Post #3 by @manjula (2021-09-12 15:03 UTC)

<p>Just my thoughts on this,</p>
<p>I think it is better to use the collision detection for the application you plan to use. We have done it in Bone reconstruction planner and Prof Lasso or Mauro will be able to tell you on how to technically implement it.  The best thing about is that the user can decide how much intersection (intercuspation) is acceptable so the surgeon can decide it. Only drawback in both methods is that (intersection and collision detection ) is that it is implemented on the whole arch. If it can be implemented in a tripod fashion then it will be ideal.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/blob/a7f80c02d7be62acccd880cd6235f36d73dd76ad/BoneReconstructionPlanner/BoneReconstructionPlanner.py#L2372-L2388">
  <header class="source">

      <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/blob/a7f80c02d7be62acccd880cd6235f36d73dd76ad/BoneReconstructionPlanner/BoneReconstructionPlanner.py#L2372-L2388" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/blob/a7f80c02d7be62acccd880cd6235f36d73dd76ad/BoneReconstructionPlanner/BoneReconstructionPlanner.py#L2372-L2388" target="_blank" rel="noopener nofollow ugc">SlicerIGT/SlicerBoneReconstructionPlanner/blob/a7f80c02d7be62acccd880cd6235f36d73dd76ad/BoneReconstructionPlanner/BoneReconstructionPlanner.py#L2372-L2388</a></h4>



  <pre class="onebox">    <code class="lang-py">
      <ol class="start lines" start="2372" style="counter-reset: li-counter 2371 ;">
          <li>import vtkSlicerRtCommonPython
</li>
          <li>for i in range(0,len(duplicateFibulaBonePiecesList) -1):
</li>
          <li>  collisionDetection = vtkSlicerRtCommonPython.vtkCollisionDetectionFilter()
</li>
          <li>  #collisionDetection = vtk.vtkCollisionDetectionFilter()
</li>
          <li>  collisionDetection.SetInputData(0, duplicateFibulaBonePiecesList[i].GetPolyData())
</li>
          <li>  collisionDetection.SetInputData(1, duplicateFibulaBonePiecesList[i+1].GetPolyData())
</li>
          <li>  matrix1 = vtk.vtkMatrix4x4()
</li>
          <li>  collisionDetection.SetMatrix(0, matrix1)
</li>
          <li>  collisionDetection.SetMatrix(1, matrix1)
</li>
          <li>  collisionDetection.SetBoxTolerance(0.0)
</li>
          <li>  collisionDetection.SetCellTolerance(0.0)
</li>
          <li>  collisionDetection.SetNumberOfCellsPerNode(2)
</li>
          <li>  collisionDetection.Update()
</li>
          <li>  
</li>
          <li>  if collisionDetection.GetNumberOfContacts() &gt; 0:
</li>
          <li>    collisionDetected = True
</li>
          <li>    break
</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #4 by @Fluvio_Lobo (2021-09-12 15:49 UTC)

<blockquote>
<p>If you also have surface scans then it may make sense to use the high-accuracy scanned surfaces directly. For this, the Combine models module can be used. You can find Sandbox extension in the very latest Slicer Preview Release (the Extensions Server is being transitioned to a new system, so it is more complicated to access extensions in older Slicer versions).</p>
</blockquote>
<p>I am actually combining <strong>surface scan</strong> and CBCT data. I will update to the latest slicer version and use the module.</p>
<p>Thank you!</p>

---

## Post #5 by @Fluvio_Lobo (2021-09-12 15:51 UTC)

<p><a class="mention" href="/u/manjula">@manjula</a>,</p>
<p>I agree, this is may be more appropriate. I am also glad is already part of SlicerIGT!</p>

---

## Post #6 by @mau_igna_06 (2021-09-12 19:25 UTC)

<p>Make another post on discourse if you need help with the collisionDetectionFilter. <a class="mention" href="/u/manjula">@manjula</a> gave you a code example to get you started</p>
<p>Mauro</p>

---
