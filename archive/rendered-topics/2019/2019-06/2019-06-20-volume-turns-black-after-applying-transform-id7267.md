---
topic_id: 7267
title: "Volume Turns Black After Applying Transform"
date: 2019-06-20
url: https://discourse.slicer.org/t/7267
---

# Volume turns black after applying transform

**Topic ID**: 7267
**Date**: 2019-06-20
**URL**: https://discourse.slicer.org/t/volume-turns-black-after-applying-transform/7267

---

## Post #1 by @blackfish (2019-06-20 21:36 UTC)

<p>Version: 4.11<br>
Operating system: win 10</p>
<p>I am trying to transform a 3D volume that I made using the grayscale model maker. However, after I apply a linear transform, the model turns black.</p>
<p>Before:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b97b5515742db478bac23e4fac723088471ca7c6.png" alt="image" data-base62-sha1="qsQzmAyNexxUobAt0XEUD19oHrw" width="310" height="210"><br>
After:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f07eb2fd5f16cd08cc5cee60df7b7c3e71790cfd.png" alt="image" data-base62-sha1="yjw2LCpCKmRHXzSVLWV7M2GtAXH" width="354" height="242"></p>
<p>What could cause this to happen?</p>
<p>Thank you in advance.</p>

---

## Post #2 by @lassoan (2019-06-20 21:57 UTC)

<p>You applied a transform that turned the model inside out (determinant of the matrix is negative). If you are sure that you want to apply this transform then you can use Surface Toolbox module to reorient the cells in the model (Normals / Flip normals).</p>

---

## Post #3 by @eliagre (2024-01-10 16:06 UTC)

<p>Version: 5.4.0<br>
Operating system: win 11</p>
<p>Hi, I encountered the same issue for a surface model and I was able to fix it by applying the suggested solution. However, I want to automate my workflow using the python console and include this step in the process. I have not been able to find a way to do it. I have looked online for how to access the Surface Toolbox module and I found this as an example: <a href="https://github.com/jzeyl/3D-Slicer-Scripts/blob/master/mirror.py" class="inline-onebox" rel="noopener nofollow ugc">3D-Slicer-Scripts/mirror.py at master · jzeyl/3D-Slicer-Scripts · GitHub</a> . This script uses the “Mirror” function of the Surface Toolbox. Similarly, I tried this for the “Compute Surface normals” function, but I get an error message. This is the code I used:</p>
<pre><code class="lang-auto"># Get the model node by name
model = slicer.util.getNode("model")

#create new empty model
modelnormals = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLModelNode','modelnormals')
modelnormals.CreateDefaultDisplayNodes()
modelnormals.GetDisplayNode().SetVisibility2D(True)

logic = slicer.util.getModuleLogic('SurfaceToolbox')
logic.computeSurfaceNormals.flipNormals(model, modelnormals)

</code></pre>
<p>And this is the error message that I got:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "&lt;string&gt;", line 10, in &lt;module&gt;
AttributeError: 'SurfaceToolboxLogic' object has no attribute 'computeSurfaceNormals'

</code></pre>
<p>I am new to this programming language and I am not sure how to solve a problem I encountered. I appreciate any guidance or feedback from more experienced coders. Would someone be able to help me or point me in the right direction? Thank you in advance</p>

---

## Post #4 by @eliagre (2024-01-10 17:53 UTC)

<p>I managed to solve my own problem! Here is the code I used:</p>
<pre><code class="lang-auto"># Get the model node by name
model = slicer.util.getNode("model")

#create new empty model
modelNormals = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLModelNode','modelNormals')
modelNormals.CreateDefaultDisplayNodes()
modelNormals.GetDisplayNode().SetVisibility2D(True)

#perform operation flipping normals on second model, using surface toolbox
logic = slicer.util.getModuleLogic('SurfaceToolbox')
logic.computeNormals(model,modelNormals,flip=True)
</code></pre>

---
