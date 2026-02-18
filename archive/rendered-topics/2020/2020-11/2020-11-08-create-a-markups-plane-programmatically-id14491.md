# Create a markups plane programmatically

**Topic ID**: 14491
**Date**: 2020-11-08
**URL**: https://discourse.slicer.org/t/create-a-markups-plane-programmatically/14491

---

## Post #1 by @mau_igna_06 (2020-11-08 16:12 UTC)

<p>I don’t know how to create a markups plane through code. I tried the following with no success:</p>
<blockquote>
<p>A = slicer.vtkMRMLMarkupsPlaneNode()<br>
A.SetOrigin([0,0,0])<br>
A.SetNormal([0,0,1])<br>
A.SetAxes([1,0,0],[0,1,0],[0,0,1])<br>
A.UpdateScene(slicer.mrmlScene)</p>
</blockquote>
<p>Expected behaviour: A new plane is shown on the 3D view and on the Markups Node list.</p>

---

## Post #2 by @Sunderlandkyl (2020-11-08 16:27 UTC)

<p>You need to add the node to the scene first. Try:</p>
<pre><code class="lang-auto">A = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsPlaneNode")
A.SetOrigin([0,0,0])
A.SetNormal([0,0,1])
A.SetAxes([1,0,0],[0,1,0],[0,0,1])
</code></pre>

---

## Post #3 by @mau_igna_06 (2020-11-09 02:06 UTC)

<p>In math only with an point and a normal vector it is possible to define a plane. So why do we use SetAxes function and what does it does?<br>
Then, I have a transform linked to the PlaneToWorldMatrix of the plane and it’s applied to a model. Why when I execute these lines the position of the model changes for the same normal vector?:</p>
<blockquote>
<p>plane.SetNormal([0,0,1])#<br>
plane.SetNormal([0,1,0])<br>
plane.SetNormal([1,0,0])<br>
plane.SetNormal([0,0,1])#<br>
plane.SetNormal([0,1,0])<br>
plane.SetNormal([1,0,0])</p>
</blockquote>
<p>How does the SetNormal function works?</p>

---
