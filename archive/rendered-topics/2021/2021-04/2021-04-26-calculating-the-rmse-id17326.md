# Calculating the RMSE

**Topic ID**: 17326
**Date**: 2021-04-26
**URL**: https://discourse.slicer.org/t/calculating-the-rmse/17326

---

## Post #1 by @toyama (2021-04-26 08:01 UTC)

<p>I would like to get the RMSE, which is the evaluation criteria for DIR.<br>
I looked at the Slicer community and found the Fiducials To Model Distance modelu and the Fiducials To Model Registration module to be useful.<br>
I want to use the Fiducials To Model Distance modelu to calculate the RMSE. I know that RMSE is a point-to-point measure, but if I specify a segment in the “Input reference points or surface” field as shown in the figure, what will the RMSE be based on in the “Input reference points”  and the segment?<br>
I would appreciate your answer.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e64f765fc7a2822922ccc875e754d3e2e286f86c.png" alt="image" data-base62-sha1="wRq44ccRuBuHbewAiJE728464yg" width="567" height="237"></p>

---

## Post #2 by @lassoan (2021-05-07 14:07 UTC)

<p>It seems that the developer of this extension does not monitor this forum. As always, you can:</p>
<ol>
<li>ask the developer directly by creating an issue or discussion topic in the extension’s repository</li>
<li>have a look at the source code yourself</li>
</ol>
<p>The relevant part of the source code of the repository is here:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/ReynoldsJ20/SlicerFiducialsToModelDistance/blob/9ba774a39460fac85da215c5cfbbb19881094d6b/FiducialsToModelDistance/FiducialsToModelDistance.py#L212-L224" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/ReynoldsJ20/SlicerFiducialsToModelDistance/blob/9ba774a39460fac85da215c5cfbbb19881094d6b/FiducialsToModelDistance/FiducialsToModelDistance.py#L212-L224" target="_blank" rel="noopener">ReynoldsJ20/SlicerFiducialsToModelDistance/blob/9ba774a39460fac85da215c5cfbbb19881094d6b/FiducialsToModelDistance/FiducialsToModelDistance.py#L212-L224</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="212" style="counter-reset: li-counter 211 ;">
<li>distanceFilter = vtk.vtkImplicitPolyDataDistance()</li>
<li>distanceFilter.SetInput(surface_World)</li>
<li>nOfFiducialPoints = inputPoints.GetNumberOfFiducials()</li>
<li>import numpy as np</li>
<li>distances = np.zeros(nOfFiducialPoints)</li>
<li>labels = [""] * nOfFiducialPoints</li>
<li>for i in range(nOfFiducialPoints):</li>
<li>  point_World = np.zeros(3)</li>
<li>  inputPoints.GetNthControlPointPositionWorld(i, point_World)</li>
<li>  closestPointOnSurface_World = np.zeros(3)</li>
<li>  closestPointDistance = distanceFilter.EvaluateFunctionAndGetClosestPoint(point_World, closestPointOnSurface_World)</li>
<li>  labels[i] = inputPoints.GetNthControlPointLabel(i)</li>
<li>  distances[i] = closestPointDistance</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>So, it compares point position to the position of the closest point on the surface.</p>

---

## Post #4 by @toyama (2021-06-09 05:33 UTC)

<p>Thank you for your response.<br>
I was late in checking the notification.<br>
I would like to ask an additional question now.<br>
So, when you say “So, it compares the point position to the position of the closest point on the surface.”, does 3DSlicer recognize the segment surface as a point, or does it recognize the CT image as a point?<br>
If you know, please let me know.</p>

---

## Post #5 by @lassoan (2021-06-09 21:48 UTC)

<p>It does not recognize the CT image as point. How would you recognize a point in the CT image?</p>
<p>You register a surface (typically extracted from an image using segmentation, such as simple thresholding) and a set of points.</p>

---

## Post #6 by @toyama (2021-06-11 08:51 UTC)

<p>Thank you for your answer .<br>
If I have any more questions, I would like to ask you.<br>
Thank you very much.</p>

---
