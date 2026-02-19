---
topic_id: 15593
title: "Python Code Model To Model Distance"
date: 2021-01-19
url: https://discourse.slicer.org/t/15593
---

# Python code model-to-model distance

**Topic ID**: 15593
**Date**: 2021-01-19
**URL**: https://discourse.slicer.org/t/python-code-model-to-model-distance/15593

---

## Post #1 by @Judith (2021-01-19 16:09 UTC)

<p>Hello everyone,<br>
Does anyone know where to find the underlying python code of the model-to-model distance module? I want to automate these parameters:</p>
<p>’ Source model: prostate<br>
Target model: tumor<br>
Vtkoutputfile: create new model as ‘whole_dist_pt’<br>
Distance: signed_closest_point<br>
Apply’</p>
<p>I have to do this for 6 models, so it would be really convenient if I can just copy the python script instead of manually clicking every time.</p>
<p>Many thanks in advance,</p>
<p>Kind regards,<br>
Judith</p>

---

## Post #2 by @smrolfe (2021-01-19 23:40 UTC)

<p>The C++ source code for the model-to-model distance module is <a href="https://github.com/NIRALUser/3DMetricTools/tree/master/ModelToModelDistance" rel="noopener nofollow ugc">here</a>.</p>
<p>It uses the vtkDistancePolyDataFilter which also has a Python wrapper. I have a Python module that uses this filter <a href="https://github.com/SlicerMorph/SlicerMorph/blob/4e7fcdf0a9e035cb66539ba140b8ba32a7413da8/MeshDistanceMeasurement/MeshDistanceMeasurement.py#L281" rel="noopener nofollow ugc">here</a> which may help as an example.</p>

---

## Post #3 by @BraveDistribution (2022-07-13 16:40 UTC)

<p>Hi <a class="mention" href="/u/smrolfe">@smrolfe</a>:</p>
<p>thanks for the script.</p>
<p>I am wondering why is rmse used instead of mean in the code?</p>
<pre><code class="lang-auto">#meanDistance = np.average(distanceArray)
meanDistance = self.rmse(distanceArray)
</code></pre>
<p>Do the indices of the meshes nodes have to correspond, when calculating distance?</p>
<p>Thanks.</p>

---

## Post #4 by @smrolfe (2022-07-13 18:30 UTC)

<p><a class="mention" href="/u/bravedistribution">@BraveDistribution</a> The mean error should not be used here since the script is using the signed distance option of the vtkDistancePolyDataFilter. The commented line is from a previous version, I will remove to avoid confusion.</p>
<p>In this implementation, the distance to the second model is computed for every point on the first model, so the mesh nodes are not required to correspond.</p>

---

## Post #5 by @BraveDistribution (2022-07-14 12:55 UTC)

<p>Thanks.</p>
<p>What’s interesting is when using this code, I receive segfault:</p>
<pre><code class="lang-auto">    distanceFilter = vtk.vtkDistancePolyDataFilter()
    distanceFilter.SetInputData(0, input1)
    distanceFilter.SetInputData(1, input2)
    distanceFilter.SignedDistanceOff()
    distanceFilter.Update()  # Calculate distance
</code></pre>
<p>at distanceFilter.Update() I receive:<br>
<code>Process finished with exit code 139 (interrupted by signal 11: SIGSEGV)</code></p>
<p>I know that’s probably out of scope of slicer, just wanted to mention it, since its closely related.</p>

---

## Post #6 by @pieper (2022-07-14 18:37 UTC)

<p><a class="mention" href="/u/bravedistribution">@BraveDistribution</a> the thing to do is to create a small complete script in pure VTK and submit it along with the data that replicates the issue to the <a href="https://gitlab.kitware.com/vtk/vtk/-/issues">VTK issue tracker</a>.</p>

---

## Post #7 by @griffinfi (2024-07-16 19:29 UTC)

<p>Hi there,</p>
<p>I wanted to follow up on this as I do not know how to use C++ – do I copy and paste that code into Slicer? Or use the “wrapper” ?<br>
Thanks in advance.</p>

---
