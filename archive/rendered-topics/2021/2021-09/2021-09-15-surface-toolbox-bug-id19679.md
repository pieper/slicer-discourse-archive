---
topic_id: 19679
title: "Surface Toolbox Bug"
date: 2021-09-15
url: https://discourse.slicer.org/t/19679
---

# Surface Toolbox bug

**Topic ID**: 19679
**Date**: 2021-09-15
**URL**: https://discourse.slicer.org/t/surface-toolbox-bug/19679

---

## Post #1 by @smrolfe (2021-09-15 01:02 UTC)

<p>The decimate tool in the Surface Toolbox produces the same output with or without the “Boundary deletion” checkbox selected. On debugging, it looks like there’s a typo in the parameter name here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/SlicerSurfaceToolbox/blob/362684dced4d3202f3947ee47ac662110a4405b9/SurfaceToolbox/SurfaceToolbox.py#L537">
  <header class="source">

      <a href="https://github.com/Slicer/SlicerSurfaceToolbox/blob/362684dced4d3202f3947ee47ac662110a4405b9/SurfaceToolbox/SurfaceToolbox.py#L537" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/SlicerSurfaceToolbox/blob/362684dced4d3202f3947ee47ac662110a4405b9/SurfaceToolbox/SurfaceToolbox.py#L537" target="_blank" rel="noopener nofollow ugc">Slicer/SlicerSurfaceToolbox/blob/362684dced4d3202f3947ee47ac662110a4405b9/SurfaceToolbox/SurfaceToolbox.py#L537</a></h4>



  <pre class="onebox">    <code class="lang-py">
      <ol class="start lines" start="527" style="counter-reset: li-counter 526 ;">
          <li>outputModel.AddDefaultStorageNode()
</li>
          <li>
</li>
          <li>if parameterNode.GetParameter("cleaner") == "true":
</li>
          <li>  self.updateProcess("Clean...")
</li>
          <li>  SurfaceToolboxLogic.clean(outputModel, outputModel)
</li>
          <li>
</li>
          <li>if parameterNode.GetParameter("decimation") == "true":
</li>
          <li>  self.updateProcess("Decimation...")
</li>
          <li>  SurfaceToolboxLogic.decimate(outputModel, outputModel,
</li>
          <li>    reductionFactor=float(parameterNode.GetParameter("decimationReduction")),
</li>
          <li class="selected">    decimateBoundary=parameterNode.GetParameter("decimationBoundary") == "true")
</li>
          <li>
</li>
          <li>if parameterNode.GetParameter("smoothing") == "true":
</li>
          <li>  self.updateProcess("Smoothing...")
</li>
          <li>  method = parameterNode.GetParameter("smoothingMethod")
</li>
          <li>  SurfaceToolboxLogic.smooth(outputModel, outputModel,
</li>
          <li>    method=parameterNode.GetParameter("smoothingMethod"),
</li>
          <li>    iterations=int(float(parameterNode.GetParameter("smoothingLaplaceIterations" if method=='Laplace' else "smoothingTaubinIterations"))),
</li>
          <li>    laplaceRelaxationFactor=float(parameterNode.GetParameter("smoothingLaplaceRelaxation")),
</li>
          <li>    taubinPassBand=float(parameterNode.GetParameter("smoothingTaubinPassBand")),
</li>
          <li>    boundarySmoothing=parameterNode.GetParameter("smoothingBoundarySmoothing") == "true")
</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Which should be consistent with the definition here:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/SlicerSurfaceToolbox/blob/362684dced4d3202f3947ee47ac662110a4405b9/SurfaceToolbox/SurfaceToolbox.py#L331">
  <header class="source">

      <a href="https://github.com/Slicer/SlicerSurfaceToolbox/blob/362684dced4d3202f3947ee47ac662110a4405b9/SurfaceToolbox/SurfaceToolbox.py#L331" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/SlicerSurfaceToolbox/blob/362684dced4d3202f3947ee47ac662110a4405b9/SurfaceToolbox/SurfaceToolbox.py#L331" target="_blank" rel="noopener nofollow ugc">Slicer/SlicerSurfaceToolbox/blob/362684dced4d3202f3947ee47ac662110a4405b9/SurfaceToolbox/SurfaceToolbox.py#L331</a></h4>



  <pre class="onebox">    <code class="lang-py">
      <ol class="start lines" start="321" style="counter-reset: li-counter 320 ;">
          <li>  ScriptedLoadableModuleLogic.__init__(self)
</li>
          <li>  self.updateProcessCallback = None
</li>
          <li>
</li>
          <li>def setDefaultParameters(self, parameterNode):
</li>
          <li>  """
</li>
          <li>  Initialize parameter node with default settings.
</li>
          <li>  """
</li>
          <li>  defaultValues = [
</li>
          <li>    ("decimation", "false"),
</li>
          <li>    ("decimationReduction", "0.8"),
</li>
          <li class="selected">    ("decimationBoundaryDeletion", "true"),
</li>
          <li>    ("smoothing", "false"),
</li>
          <li>    ("smoothingMethod", "Taubin"),
</li>
          <li>    ("smoothingLaplaceIterations", "100"),
</li>
          <li>    ("smoothingLaplaceRelaxation", "0.5"),
</li>
          <li>    ("smoothingTaubinIterations", "30"),
</li>
          <li>    ("smoothingTaubinPassBand", "0.1"),
</li>
          <li>    ("smoothingBoundarySmoothing", "true"),
</li>
          <li>    ("normals", "false"),
</li>
          <li>    ("normalsAutoOrient", "false"),
</li>
          <li>    ("normalsFlip", "false"),
</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Changing the name on line 537 resolves the issue. I can submit a pull request with this change if this looks correct.</p>

---

## Post #2 by @lassoan (2021-09-15 01:12 UTC)

<p>Good catch. Yes, please send a pull request (keep <code>decimationBoundaryDeletion</code>). Thank you!</p>

---
