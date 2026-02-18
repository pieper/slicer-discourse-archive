# Retrieve Volume and Surface Area of a ModelNode (Surface Mesh (vtkPolyData)) - Python

**Topic ID**: 21556
**Date**: 2022-01-21
**URL**: https://discourse.slicer.org/t/retrieve-volume-and-surface-area-of-a-modelnode-surface-mesh-vtkpolydata-python/21556

---

## Post #1 by @l.geronzi (2022-01-21 11:04 UTC)

<p>Hi all,<br>
I am a beginner and I don’t have much experience with the 3DSlicer environment and vtk libraries. I have already followed the various tutorials to get started.<br>
My problem is the following.<br>
I am trying to use python to retrieve model information, particularly Surface Area and Volume.<br>
The ModelNode in my case is a Surface Mesh (vtkPolyData).<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/369e38ea8c835223fb1e0604eb5678e1bc16e3af.png" alt="problem" data-base62-sha1="7NaLW6A3BggiT9LYUn9y6A8AqJ1" width="548" height="219"><br>
I’m using:<br>
modelnode=slicer.util.getNode(“Model_3”)<br>
meshpolydata=modelnode.GetMesh()</p>
<p>From here, how do I get easily Surface Area and Volume?</p>
<p>Thank you,</p>
<p>Leonardo</p>

---

## Post #2 by @l.geronzi (2022-01-21 14:14 UTC)

<p>I don’t know if this is the best approach but I found the solution for my problem using the vtkMassProperties<br>
Mass = vtk.vtkMassProperties()<br>
Mass.SetInputData(mesh)<br>
Mass.Update()<br>
Surface_Area=Mass.GetSurfaceArea()<br>
Volume=Mass.GetVolume()</p>
<p>I hope this can be of help to someone.</p>

---

## Post #3 by @chir.set (2022-01-21 14:15 UTC)

<aside class="quote no-group" data-username="l.geronzi" data-post="1" data-topic="21556">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/97f17d/48.png" class="avatar"> l.geronzi:</div>
<blockquote>
<p>From here, how do I get easily Surface Area and Volume?</p>
</blockquote>
</aside>
<p>Pass the polydata to vtkMassProperties, and the rest is quite straightforward.</p>

---

## Post #4 by @mau_igna_06 (2022-01-21 14:46 UTC)

<p>If you check Slicer’s code they pass the polydata by a triangleFilter with a specific option before using massProperties. I don’t know why they do it but when I have to calculate a surfaceArea or volume I do it too</p>
<p>Hope it helps</p>

---

## Post #5 by @jumbojing (2022-08-02 02:57 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="4" data-topic="21556">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>triangleFilter</p>
</blockquote>
</aside>
<pre data-code-wrap="python"><code class="lang-python">.....
        tri_converter = vtk.vtkTriangleFilter()
        tri_converter.SetInputDataObject(model.GetMesh())
        tri_converter.Update()
        Mass = vtk.vtkMassProperties() 
        Mass.SetInputData(tri_converter.GetOutput()) 
        Mass.Update() 
        return Mass.GetSurfaceArea(),Mass.GetVolume()
</code></pre>

---
