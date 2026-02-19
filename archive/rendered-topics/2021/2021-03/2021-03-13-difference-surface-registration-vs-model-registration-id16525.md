---
topic_id: 16525
title: "Difference Surface Registration Vs Model Registration"
date: 2021-03-13
url: https://discourse.slicer.org/t/16525
---

# Difference Surface Registration vs Model Registration

**Topic ID**: 16525
**Date**: 2021-03-13
**URL**: https://discourse.slicer.org/t/difference-surface-registration-vs-model-registration/16525

---

## Post #1 by @sfglio (2021-03-13 22:15 UTC)

<p>I am wondering where exactly is the difference between surface registration modul and the model registration (of SlicersIGT)</p>
<p>Model registration states it: iterative closest point</p>
<p>Surface Registration: which method is used here???</p>
<p>BTW: I noticed that if you want to register a transformed STL using model registration it does <strong>not</strong> take the transformation into account<br>
however<br>
surface registration does what it should: it registers the transformed STL</p>
<p>So can I conclude that the results won’t differ beside the above mentioned fact?</p>

---

## Post #2 by @lassoan (2021-03-14 04:11 UTC)

<p>They both use the same ICP algorithm implementation (vtkIterativeClosestPointTransform):</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/DCBIA-OrthoLab/CMFreg/blob/master/SurfaceRegistration/SurfaceRegistration.py#L722" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/DCBIA-OrthoLab/CMFreg/blob/master/SurfaceRegistration/SurfaceRegistration.py#L722" target="_blank" rel="noopener">DCBIA-OrthoLab/CMFreg/blob/master/SurfaceRegistration/SurfaceRegistration.py#L722</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="712" style="counter-reset: li-counter 711 ;">
<li>    parameters["movingLandmarks"] = movingLandmarks
</li>
<li>    parameters["saveTransform"] = saveTransform
</li>
<li>    parameters["transformType"] = tranformType
</li>
<li>    fiducialRegistration = slicer.modules.fiducialregistration
</li>
<li>    slicer.cli.run(fiducialRegistration, None, parameters, wait_for_completion=True)
</li>
<li>
</li>
<li>def runICP(self, fixed, moving, outputTrans, meanDistanceType,
</li>
<li>           landmarkTransformType, numberOfLandmarks, maxDistance,
</li>
<li>           numberOfIterations, matchCentroids, checkMeanDistance):
</li>
<li>    """Run the actual algorithm"""
</li>
<li class="selected">    icp = vtk.vtkIterativeClosestPointTransform()
</li>
<li>    icp.SetSource(moving)
</li>
<li>    icp.SetTarget(fixed)
</li>
<li>    if landmarkTransformType == "RigidBody":
</li>
<li>        icp.GetLandmarkTransform().SetModeToRigidBody()
</li>
<li>    elif landmarkTransformType == "Similarity":
</li>
<li>        icp.GetLandmarkTransform().SetModeToSimilarity()
</li>
<li>    elif landmarkTransformType == "Affine":
</li>
<li>        icp.GetLandmarkTransform().SetModeToAffine()
</li>
<li>    if meanDistanceType == "Root Mean Square":
</li>
<li>        icp.SetMeanDistanceModeToRMS()
</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerIGT/SlicerIGT/blob/master/ModelRegistration/ModelRegistration.py#L187" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerIGT/SlicerIGT/blob/master/ModelRegistration/ModelRegistration.py#L187" target="_blank" rel="noopener">SlicerIGT/SlicerIGT/blob/master/ModelRegistration/ModelRegistration.py#L187</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="177" style="counter-reset: li-counter 176 ;">
<li>computation done by your module.  The interface</li>
<li>should be such that other python code can import</li>
<li>this class and make use of the functionality without</li>
<li>requiring an instance of the Widget</li>
<li>"""</li>
<li>
<li>def run(self, inputSourceModel, inputTargetModel, outputSourceToTargetTransform, transformType=0, numIterations=100 ):</li>
<li>
<li>  self.delayDisplay('Running iterative closest point registration')</li>
<li>
<li class="selected">  icpTransform = vtk.vtkIterativeClosestPointTransform()</li>
<li>  icpTransform.SetSource( inputSourceModel.GetPolyData() )</li>
<li>  icpTransform.SetTarget( inputTargetModel.GetPolyData() )</li>
<li>  icpTransform.GetLandmarkTransform().SetModeToRigidBody()</li>
<li>  if transformType == 1:</li>
<li>    icpTransform.GetLandmarkTransform().SetModeToSimilarity()</li>
<li>  if transformType == 2:</li>
<li>    icpTransform.GetLandmarkTransform().SetModeToAffine()</li>
<li>  icpTransform.SetMaximumNumberOfIterations( numIterations )</li>
<li>  icpTransform.Modified()</li>
<li>  icpTransform.Update()</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>The difference is in GUI and workflow. SurfaceRegistration includes both landmark registration and ICP; while SlicerIGT implements this in two modules (Fiducial Registration Wizard and Model Registration).</p>

---
