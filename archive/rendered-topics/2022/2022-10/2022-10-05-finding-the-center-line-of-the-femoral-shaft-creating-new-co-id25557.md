---
topic_id: 25557
title: "Finding The Center Line Of The Femoral Shaft Creating New Co"
date: 2022-10-05
url: https://discourse.slicer.org/t/25557
---

# Finding the center line of the femoral shaft (creating new coordinate system)

**Topic ID**: 25557
**Date**: 2022-10-05
**URL**: https://discourse.slicer.org/t/finding-the-center-line-of-the-femoral-shaft-creating-new-coordinate-system/25557

---

## Post #1 by @jegberink (2022-10-05 09:47 UTC)

<p>Hello everyone,</p>
<p>I was wondering if anyone has had a similar problem and could help me figure this out.</p>
<p>In short: I have a preoperative and postoperative CT of a femur. Postoperative the proximal femur above the trochanter minor has been repositioned. We want to measure this reposition.</p>
<p>Because we have multiple patients we would like to create a local coordinate system for consistent measurement. For this i figured we could appoint the femoral shaft axis as the Z-axis and pick another landmark to create a coordinate system.</p>
<p>I’ve tried the vascular modeling toolkit, however the medullary cavity seems to disrupt the algorithm.</p>
<p>Is there a possibility to get the center point of multiple axial slices of the femoral shaft segmentation and creating a trendline through these points to create the femoral shaft axis?</p>
<p>Thank you in advance</p>

---

## Post #2 by @mau_igna_06 (2022-10-05 12:05 UTC)

<p>Hi. Have you tried the vmtk extension centerline extraction algoririthm? If so, what is your feedback?</p>

---

## Post #3 by @jegberink (2022-10-06 06:25 UTC)

<p>I did, unfortunately the CT is only of the proximal part of the femur. The medullary cavity seems to give VMTK some problems in calculating the centerline correctly as shown here:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/245774c3814a9d9db597c1e27b121378ac0e5c2c.png" data-download-href="/uploads/short-url/5buyTl7Xr4qX733IVfaVJhfFkPW.png?dl=1" title="vmtk" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/245774c3814a9d9db597c1e27b121378ac0e5c2c_2_464x500.png" alt="vmtk" data-base62-sha1="5buyTl7Xr4qX733IVfaVJhfFkPW" width="464" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/245774c3814a9d9db597c1e27b121378ac0e5c2c_2_464x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/245774c3814a9d9db597c1e27b121378ac0e5c2c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/245774c3814a9d9db597c1e27b121378ac0e5c2c.png 2x" data-dominant-color="9D9BC2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">vmtk</span><span class="informations">606×653 83.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If i were to fill in the medullary cavity and it would create the centerline, would i then be able to construct a line averaging this one? (so a straight line i could use as my z axis?).</p>
<p>Thank you for reaching out.</p>

---

## Post #4 by @mau_igna_06 (2022-10-06 12:53 UTC)

<aside class="quote no-group" data-username="jegberink" data-post="3" data-topic="25557">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jegberink/48/16031_2.png" class="avatar"> jegberink:</div>
<blockquote>
<p>If i were to fill in the medullary cavity and it would create the centerline, would i then be able to construct a line averaging this one? (so a straight line i could use as my z axis?).</p>
</blockquote>
</aside>
<p>Bones are not perfectly straight so you still obtain a centerline curve but then you would just select two points of it that delineate your region of interest, that would be the two points to create the axis line you want.</p>
<p>You can solve the cavity with the WrapSolidify effect of the extensions manager. You should apply it using the segment editor over the current femur segmentation you have. Then use vmtk centerline extraction.</p>
<p>If you have a almost-straight bone model exported from your segmentation you may also have a look at this algorithm:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/blob/ed9c145476125123e9772d526635a030e2675596/BoneReconstructionPlanner/BoneReconstructionPlanner.py#L3107-L3143">
  <header class="source">

      <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/blob/ed9c145476125123e9772d526635a030e2675596/BoneReconstructionPlanner/BoneReconstructionPlanner.py#L3107-L3143" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/blob/ed9c145476125123e9772d526635a030e2675596/BoneReconstructionPlanner/BoneReconstructionPlanner.py#L3107-L3143" target="_blank" rel="noopener nofollow ugc">SlicerIGT/SlicerBoneReconstructionPlanner/blob/ed9c145476125123e9772d526635a030e2675596/BoneReconstructionPlanner/BoneReconstructionPlanner.py#L3107-L3143</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="3107" style="counter-reset: li-counter 3106 ;">
          <li>def centerFibulaLine(self):
</li>
          <li>  parameterNode = self.getParameterNode()
</li>
          <li>  fibulaLine = parameterNode.GetNodeReference("fibulaLine")
</li>
          <li>  fibulaModelNode = parameterNode.GetNodeReference("fibulaModelNode")
</li>
          <li>
</li>
          <li>  shNode = slicer.mrmlScene.GetSubjectHierarchyNode()
</li>
          <li>  intersectionsFolder = shNode.CreateFolderItem(self.getParentFolderItemID(),"Intersections")
</li>
          <li>
</li>
          <li>  lineStartPos = np.zeros(3)
</li>
          <li>  lineEndPos = np.zeros(3)
</li>
          <li>  fibulaLine.GetNthControlPointPositionWorld(0, lineStartPos)
</li>
          <li>  fibulaLine.GetNthControlPointPositionWorld(1, lineEndPos)
</li>
          <li>
</li>
          <li>  numberOfRepetitionsOfPositioningAlgorithm = 5
</li>
          <li>  for i in range(numberOfRepetitionsOfPositioningAlgorithm):
</li>
          <li>    fibulaLineNorm = np.linalg.norm(lineEndPos-lineStartPos)
</li>
          <li>    fibulaLineDirection = (lineEndPos-lineStartPos)/fibulaLineNorm
</li>
          <li>
</li>
          <li>    fibulaStartIntersectionModel = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLModelNode','FibulaStartIntersection %d' % i)
</li>
          <li>    fibulaEndIntersectionModel = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLModelNode','FibulaEndIntersection %d' % i)
</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner/blob/ed9c145476125123e9772d526635a030e2675596/BoneReconstructionPlanner/BoneReconstructionPlanner.py#L3107-L3143" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Hope it helps</p>

---
