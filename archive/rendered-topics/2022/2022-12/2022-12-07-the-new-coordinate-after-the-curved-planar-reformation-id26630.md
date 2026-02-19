---
topic_id: 26630
title: "The New Coordinate After The Curved Planar Reformation"
date: 2022-12-07
url: https://discourse.slicer.org/t/26630
---

# the new coordinate after the curved planar reformation

**Topic ID**: 26630
**Date**: 2022-12-07
**URL**: https://discourse.slicer.org/t/the-new-coordinate-after-the-curved-planar-reformation/26630

---

## Post #1 by @bulalala (2022-12-07 15:04 UTC)

<p>how does it determine the new coordinate frame after the curved planar reformation?  like the determination of origin and the determination of three new axes</p>

---

## Post #2 by @lassoan (2022-12-07 15:14 UTC)

<p>You can transform point positions from world (RAS) space to the straightened space using the “Output transform”. For example, you can define point positions in the original image and apply the output transform to get the point positions in the straightened image.</p>
<p>You can invert the transform in the Transforms module if you want to convert point coordinates from the straightened space to the world space.</p>

---

## Post #3 by @bulalala (2022-12-08 09:26 UTC)

<p>Thank you for your answer. I don’t understand about one point. The straightened space might have axis like XYZ or RAS when the reconstruction results of CPR are presented in 3D space like the image below. In the space of CPR results, it’s like having three axes that are perpendicular to each other by default. How are these three perpendicular axes determined? In other words, what is the basis for choosing these three directions as the new axes?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f3166965db5ba4617672ea20c8befbde4082a4c0.png" data-download-href="/uploads/short-url/yGs2CaqdYyYTnjhxGQI25AxQh5m.png?dl=1" title="sample" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f3166965db5ba4617672ea20c8befbde4082a4c0_2_690x443.png" alt="sample" data-base62-sha1="yGs2CaqdYyYTnjhxGQI25AxQh5m" width="690" height="443" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f3166965db5ba4617672ea20c8befbde4082a4c0_2_690x443.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f3166965db5ba4617672ea20c8befbde4082a4c0.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f3166965db5ba4617672ea20c8befbde4082a4c0.png 2x" data-dominant-color="3E3E47"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">sample</span><span class="informations">1005×646 113 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2022-12-08 14:10 UTC)

<p>The axes are computed so that the straightened space is positioned and oriented similarly to the the original space. See exact algorithm here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/PerkLab/SlicerSandbox/blob/d4a0d5cb491da5d6c9a721fd21c6ab38d43c9528/CurvedPlanarReformat/CurvedPlanarReformat.py#L218">
  <header class="source">

      <a href="https://github.com/PerkLab/SlicerSandbox/blob/d4a0d5cb491da5d6c9a721fd21c6ab38d43c9528/CurvedPlanarReformat/CurvedPlanarReformat.py#L218" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/PerkLab/SlicerSandbox/blob/d4a0d5cb491da5d6c9a721fd21c6ab38d43c9528/CurvedPlanarReformat/CurvedPlanarReformat.py#L218" target="_blank" rel="noopener">PerkLab/SlicerSandbox/blob/d4a0d5cb491da5d6c9a721fd21c6ab38d43c9528/CurvedPlanarReformat/CurvedPlanarReformat.py#L218</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="208" style="counter-reset: li-counter 207 ;">
          <li>if not slicer.vtkMRMLMarkupsCurveNode.ResamplePoints(originalCurvePoints, sampledPoints, resamplingCurveSpacing, False):</li>
          <li>  raise ValueError("Resampling curve failed")</li>
          <li>resampledCurveNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsCurveNode", "CurvedPlanarReformat_resampled_curve_temp")</li>
          <li>resampledCurveNode.SetNumberOfPointsPerInterpolatingSegment(1)</li>
          <li>resampledCurveNode.SetCurveTypeToLinear()</li>
          <li>resampledCurveNode.SetControlPointPositionsWorld(sampledPoints)</li>
          <li>
          <li>curveNodePlane = vtk.vtkPlane()</li>
          <li>slicer.modules.markups.logic().GetBestFitPlane(resampledCurveNode, curveNodePlane)</li>
          <li>
          <li class="selected"># Z axis (from first curve point to last, this will be the straightened curve long axis)</li>
          <li>curveStartPoint = np.zeros(3)</li>
          <li>curveEndPoint = np.zeros(3)</li>
          <li>resampledCurveNode.GetNthControlPointPositionWorld(0, curveStartPoint)</li>
          <li>resampledCurveNode.GetNthControlPointPositionWorld(resampledCurveNode.GetNumberOfControlPoints()-1, curveEndPoint)</li>
          <li>transformGridAxisZ = (curveEndPoint-curveStartPoint)/np.linalg.norm(curveEndPoint-curveStartPoint)</li>
          <li>
          <li>if stretching:</li>
          <li>  # Y axis = best fit plane normal</li>
          <li>  transformGridAxisY = np.copy(curveNodePlane.GetNormal())</li>
          <li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
