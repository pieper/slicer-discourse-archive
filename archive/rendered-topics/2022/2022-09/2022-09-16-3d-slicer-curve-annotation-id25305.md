---
topic_id: 25305
title: "3D Slicer Curve Annotation"
date: 2022-09-16
url: https://discourse.slicer.org/t/25305
---

# 3D Slicer Curve Annotation

**Topic ID**: 25305
**Date**: 2022-09-16
**URL**: https://discourse.slicer.org/t/3d-slicer-curve-annotation/25305

---

## Post #1 by @stevenagl12 (2022-09-16 13:35 UTC)

<p>Can anyone tell me what the equation that is used for the curve annotation tool is to calculate the curvature for the mean and max curvature metrics?</p>

---

## Post #2 by @lassoan (2022-09-16 14:05 UTC)

<p>You can find the computation in the vtkCurveMeasurementsCalculator filter source code:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/2551f9f58637de6baf714d48543a717da3ee7197/Modules/Loadable/Markups/MRML/vtkCurveMeasurementsCalculator.cxx#L226-L239">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/2551f9f58637de6baf714d48543a717da3ee7197/Modules/Loadable/Markups/MRML/vtkCurveMeasurementsCalculator.cxx#L226-L239" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/2551f9f58637de6baf714d48543a717da3ee7197/Modules/Loadable/Markups/MRML/vtkCurveMeasurementsCalculator.cxx#L226-L239" target="_blank" rel="noopener">Slicer/Slicer/blob/2551f9f58637de6baf714d48543a717da3ee7197/Modules/Loadable/Markups/MRML/vtkCurveMeasurementsCalculator.cxx#L226-L239</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="226" style="counter-reset: li-counter 225 ;">
          <li>diffVector[0] = currPoint[0]-prevPoint[0];</li>
          <li>diffVector[1] = currPoint[1]-prevPoint[1];</li>
          <li>diffVector[2] = currPoint[2]-prevPoint[2];</li>
          <li>diffNorm = sqrt(diffVector[0]*diffVector[0] + diffVector[1]*diffVector[1] + diffVector[2]*diffVector[2]);</li>
          <li>
          </li>
<li>normDiffVector[0] = diffVector[0] / diffNorm;</li>
          <li>normDiffVector[1] = diffVector[1] / diffNorm;</li>
          <li>normDiffVector[2] = diffVector[2] / diffNorm;</li>
          <li>
          </li>
<li>// Local curvature</li>
          <li>kappa = sqrt( (normDiffVector[0]-prevNormDiffVector[0])*(normDiffVector[0]-prevNormDiffVector[0])</li>
          <li>            + (normDiffVector[1]-prevNormDiffVector[1])*(normDiffVector[1]-prevNormDiffVector[1])</li>
          <li>            + (normDiffVector[2]-prevNormDiffVector[2])*(normDiffVector[2]-prevNormDiffVector[2]) )</li>
          <li>        / diffNorm;</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
