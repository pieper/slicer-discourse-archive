---
topic_id: 20277
title: "Cant Display Model From C"
date: 2021-10-21
url: https://discourse.slicer.org/t/20277
---

# Can't display model from C++

**Topic ID**: 20277
**Date**: 2021-10-21
**URL**: https://discourse.slicer.org/t/cant-display-model-from-c/20277

---

## Post #1 by @keri (2021-10-21 03:14 UTC)

<p>Hi,</p>
<p>Here is my first attempt to add a model but I can’t display scalars on 3D view:</p>
<pre><code class="lang-cpp">  vtkNew&lt;vtkPoints&gt; pts;
  vtkNew&lt;vtkDoubleArray&gt; derivs;
  ...
  vtkNew&lt;vtkPolyData&gt; polyData;
  polyData-&gt;SetPoints(pts);
  polyData-&gt;GetPointData()-&gt;SetScalars(derivs);

  vtkNew&lt;vtkMRMLModelNode&gt; modelNode;
  modelNode-&gt;SetAndObservePolyData(polyData);

  GetMRMLScene()-&gt;AddNode(modelNode.GetPointer());
  modelNode-&gt;CreateDefaultDisplayNodes();
</code></pre>
<p>I can see that the node is added to the scene and the scalars present but I can’t find a node on the view:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62440da497df9d42d611e17bb98e2a89e2f4249c.jpeg" data-download-href="/uploads/short-url/e1iAVwQhwKi9kgqBGC4svolb2Ve.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/62440da497df9d42d611e17bb98e2a89e2f4249c_2_413x500.jpeg" alt="image" data-base62-sha1="e1iAVwQhwKi9kgqBGC4svolb2Ve" width="413" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/62440da497df9d42d611e17bb98e2a89e2f4249c_2_413x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62440da497df9d42d611e17bb98e2a89e2f4249c.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62440da497df9d42d611e17bb98e2a89e2f4249c.jpeg 2x" data-dominant-color="E4E7E8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">465×562 56.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-10-21 04:25 UTC)

<p>You can use the Models module logic’s convenience method for this:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/5317e68bf9768c249f34089011440d93e8c83096/Modules/Loadable/Models/Logic/vtkSlicerModelsLogic.cxx#L174-L188">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/5317e68bf9768c249f34089011440d93e8c83096/Modules/Loadable/Models/Logic/vtkSlicerModelsLogic.cxx#L174-L188" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/5317e68bf9768c249f34089011440d93e8c83096/Modules/Loadable/Models/Logic/vtkSlicerModelsLogic.cxx#L174-L188" target="_blank" rel="noopener">Slicer/Slicer/blob/5317e68bf9768c249f34089011440d93e8c83096/Modules/Loadable/Models/Logic/vtkSlicerModelsLogic.cxx#L174-L188</a></h4>



  <pre class="onebox">    <code class="lang-cxx">
      <ol class="start lines" start="174" style="counter-reset: li-counter 173 ;">
          <li>vtkMRMLModelNode* vtkSlicerModelsLogic::AddModel(vtkPolyData* polyData)</li>
          <li>{</li>
          <li>  if (this-&gt;GetMRMLScene() == nullptr)</li>
          <li>    {</li>
          <li>    return nullptr;</li>
          <li>    }</li>
          <li>  vtkMRMLModelNode* model = vtkMRMLModelNode::SafeDownCast(this-&gt;GetMRMLScene()-&gt;AddNewNodeByClass("vtkMRMLModelNode"));</li>
          <li>  if (!model)</li>
          <li>    {</li>
          <li>    return nullptr;</li>
          <li>    }</li>
          <li>  model-&gt;SetAndObservePolyData(polyData);</li>
          <li>  model-&gt;CreateDefaultDisplayNodes();</li>
          <li>  return model;</li>
          <li>}</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @keri (2021-10-21 18:24 UTC)

<p>Thank you for the answer</p>
<p>I noticed that my data has <code>nan</code> values and thus the scalar range is useless. Did you have an experience of displaying models with <code>nan</code>?</p>

---

## Post #4 by @lassoan (2021-10-21 18:37 UTC)

<p>It is practically impossible to prepare a software to properly deal with nan values everywhere. It would have enormous performance impact and would complicate algorithms and display pipelines at an unreasonable level. Also, meaning of  “properly deal with nan” depends on the use case. Points/cells with nan values could be removed, skipped (interpolated using nearby valid values), displayed with a transparent value or special color, …?</p>
<p>I would recommend to get rid of the nan values as soon as you can (right after importing the mesh). For example by converting them to a value that makes sense for your application and maybe by applying further processing (e.g., remove regions with nan valued scalar by using threshold filter).</p>

---

## Post #5 by @keri (2021-10-21 18:56 UTC)

<p>I still can’t make scalar visualization work.</p>
<p>For example what is wrong with this pretty simple snippet of code:</p>
<pre><code class="lang-c++">// preparing rectangular grid
  ptrdiff_t nX = 10;
  ptrdiff_t nY = 10;

  vtkNew&lt;vtkPoints&gt; pts;
  pts-&gt;SetNumberOfPoints(nX*nY);

  vtkNew&lt;vtkDoubleArray&gt; scalars;
  scalars-&gt;SetName("my_scalars");
  scalars-&gt;SetNumberOfTuples(nX*nY);

  double vals[3];
  for (ptrdiff_t y = 0; y &lt; nY; y++){
    for (ptrdiff_t x = 0; x &lt; nX; x++){
      vals[0] = x;
      vals[1] = y;
      vals[2] = 0;
      pts-&gt;SetPoint(x + y*nX, vals);
      scalars-&gt;SetValue(x + y*nX, x+y);
    }
  }

// creating polydata and adding it to the scene
  vtkNew&lt;vtkPolyData&gt; polyData;
  polyData-&gt;SetPoints(pts);
  polyData-&gt;GetPointData()-&gt;SetScalars(scalars);

  qSlicerApplication* app = qSlicerApplication::application();
  vtkSlicerModelsLogic* modelsLogic =
    vtkSlicerModelsLogic::SafeDownCast(app-&gt;moduleLogic("Models"));
  vtkMRMLModelNode* modelNode =
    modelsLogic-&gt;AddModel(polyData);
</code></pre>
<p>I’m trying to represent rectangular grid and set scalars to points.<br>
After running the app I can see that the model is added but no any coloring applied<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/0091327edaa3a36765888acce0405f69ec77bb7e.jpeg" data-download-href="/uploads/short-url/515bCLHo6TOddp45BDZ3FmvT8G.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0091327edaa3a36765888acce0405f69ec77bb7e_2_690x383.jpeg" alt="image" data-base62-sha1="515bCLHo6TOddp45BDZ3FmvT8G" width="690" height="383" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0091327edaa3a36765888acce0405f69ec77bb7e_2_690x383.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/0091327edaa3a36765888acce0405f69ec77bb7e.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/0091327edaa3a36765888acce0405f69ec77bb7e.jpeg 2x" data-dominant-color="C7C9E0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">897×498 74.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @lassoan (2021-10-21 19:31 UTC)

<p>Could you please share Python code that generates the mesh or upload the generated mesh somewhere  and post the link here?</p>

---

## Post #7 by @keri (2021-10-21 19:44 UTC)

<p>Here is the code I use to test it in python.<br>
The mesh (mesh and points I guess share the same meaning) is named <code>vpoints</code> and <code>varray</code> is scalars (any random numbers):</p>
<pre><code class="lang-python"># variable prefixed with `v` is treated as `vtk` object

import numpy as np

nx = 10
ny = 10

rng = np.random.default_rng(12345)
array = rng.random((nx*ny))

vpoints = vtk.vtkPoints()
vpoints.SetNumberOfPoints(nx*ny)

varray = vtk.vtkDoubleArray()
varray.SetNumberOfComponents(1)
varray.SetName("my_scalar")
varray.SetNumberOfTuples(nx*ny)

for y in range(0, ny):
    for x in range(0, nx):
        ind = x + y*nx
        vpoints.SetPoint(ind, [x,y,0])
        varray.SetValue(ind, array[ind])

vpoly = vtk.vtkPolyData()
vpoly.SetPoints(vpoints)
vpoly.GetPointData().SetScalars(varray) # this returns 0 - is it ok?

modelNode = slicer.modules.models.logic().AddModel(vpoly)
</code></pre>

---

## Post #8 by @lassoan (2021-10-21 20:01 UTC)

<p>This code generates a pointset and puts it into a polydata object, but there is nothing displayable here (there are no cells, just points). If you want to display some shape at each point position then you can use <code>vpoly</code> as input to a vtkGlyph3D filter (along with some glyph source, source as a sphere source). The output of that filter will be displayable.</p>

---

## Post #9 by @keri (2021-10-21 22:33 UTC)

<p>Thank you very much!</p>
<p>Just in case here is the <a href="https://kitware.github.io/vtk-examples/site/Cxx/VisualizationAlgorithms/ExponentialCosine/" rel="noopener nofollow ugc">Exponential Cosine VTK example</a> converted to Slicer API:</p>
<pre><code class="lang-python">import math

plane = vtk.vtkPlaneSource()
plane.SetResolution(300, 300)

transform = vtk.vtkTransform()
transform.Scale(10.0, 10.0, 1.0)

transF = vtk.vtkTransformPolyDataFilter()
transF.SetInputConnection(plane.GetOutputPort())
transF.SetTransform(transform)
transF.Update()

input = transF.GetOutput()
numPts = input.GetNumberOfPoints()

newPts = vtk.vtkPoints()
newPts.SetNumberOfPoints(numPts)

derivs = vtk.vtkDoubleArray()
derivs.SetName("my_scalar")
derivs.SetNumberOfTuples(numPts)

bessel = vtk.vtkPolyData()
bessel.CopyStructure(input)
bessel.SetPoints(newPts)
bessel.GetPointData().SetScalars(derivs)

x = [0,0,0]

for i in range(0, numPts):
    input.GetPoint(i, x)
    r = math.sqrt(x[0] * x[0] + x[1] * x[1])
    x[2] = math.exp(-r) * math.cos(10.0 * r)
    newPts.SetPoint(i, x)
    deriv = -math.exp(-r) * (math.cos(10.0 * r) + 10.0 * math.sin(10.0 * r))
    derivs.SetValue(i, deriv)

warp = vtk.vtkWarpScalar()
warp.SetInputData(bessel)
warp.XYPlaneOn()
warp.SetScaleFactor(0.5)

modelNode = slicer.modules.models.logic().AddModel(warp.GetOutputPort())
</code></pre>

---

## Post #10 by @lassoan (2021-10-22 00:22 UTC)

<p>Thank you for the example, looks nice!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/37f5bc714fd5446f97f9c3485228a7955998fa0e.jpeg" data-download-href="/uploads/short-url/7Z2Knv76M4te9TsAMbiCbMMyzZc.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/37f5bc714fd5446f97f9c3485228a7955998fa0e_2_690x419.jpeg" alt="image" data-base62-sha1="7Z2Knv76M4te9TsAMbiCbMMyzZc" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/37f5bc714fd5446f97f9c3485228a7955998fa0e_2_690x419.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/37f5bc714fd5446f97f9c3485228a7955998fa0e_2_1035x628.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/37f5bc714fd5446f97f9c3485228a7955998fa0e_2_1380x838.jpeg 2x" data-dominant-color="BBC7D6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1166 134 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
