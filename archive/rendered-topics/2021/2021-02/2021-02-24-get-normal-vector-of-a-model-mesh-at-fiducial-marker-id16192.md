# Get normal vector of a model mesh at fiducial marker

**Topic ID**: 16192
**Date**: 2021-02-24
**URL**: https://discourse.slicer.org/t/get-normal-vector-of-a-model-mesh-at-fiducial-marker/16192

---

## Post #1 by @apparrilla (2021-02-24 20:55 UTC)

<p>Hi everyone!<br>
I´d like to get the normal vector of a model surface at a marked point with a fiducial.<br>
Is there any example in the script repository for this task?</p>
<p>Thanks on advance…</p>

---

## Post #2 by @mau_igna_06 (2021-02-24 23:27 UTC)

<p>Here is the code:</p>
<pre><code class="lang-auto">fiducial = getNode('F')
model = getNode('Model')

point = [0,0,0]
fiducial.GetNthFiducialPosition(0,point)

normalsOfModel = slicer.util.arrayFromModelPointData(model, 'Normals')

modelMesh = model.GetMesh()

pointID = modelMesh.FindPoint(point)

normalAtPointID = normalsOfModel[pointID]
</code></pre>
<p>It gives the normal of the nearest-model-point to the fiducial-point</p>

---

## Post #3 by @apparrilla (2021-02-27 00:36 UTC)

<p>It gives me some kind of problem <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> :</p>
<blockquote>
<p>AppData\Local\NA-MIC\Slicer 4.13.0-2021-02-16\bin\Python\slicer\util.py", line 1505, in _vtkArrayFromModelData<br>
location, arrayName, “', '”.join(availableArrayNames)))<br>
ValueError: Input modelNode does not contain point data array ‘Normals’. Available array names: ‘RegionId’</p>
</blockquote>
<p>It look like modelNode hasn´t normals info…</p>

---

## Post #4 by @lassoan (2021-02-27 01:20 UTC)

<p>You can compute normals using Surface Toolbox module.</p>

---
