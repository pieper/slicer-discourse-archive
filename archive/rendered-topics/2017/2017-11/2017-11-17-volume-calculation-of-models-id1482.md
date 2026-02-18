# Volume calculation of Models

**Topic ID**: 1482
**Date**: 2017-11-17
**URL**: https://discourse.slicer.org/t/volume-calculation-of-models/1482

---

## Post #1 by @Remco (2017-11-17 14:17 UTC)

<p>Operating system: Win7<br>
Slicer version: 4.9.0-2017-11-16</p>
<p>I have loaded a uMRI dataset and created some surface meshes using the segment editor. I would like to interrogate the volume of the surface meshes using the Models Module, however the units are in mm^3 (See screenshot). Since my volumes are very small this is somewhat unfortunate. Can I adjust the units or significant digits somewhere? the general setting for length under Preferences does not appear to affect the volume calculation. Is there perhaps a different module I could use?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dcc3e91e502ac86bd64c8926db6c82a728a95e44.png" alt="20171117_Model-volume-information" data-base62-sha1="vuYMmz23J9qzXz2yjYzUfmnTEkk" width="650" height="318"> .</p>

---

## Post #2 by @lassoan (2017-11-17 14:20 UTC)

<p>You might consider changing volume spacing in Volumes module, for example multiplying it by 1000 (so the unit would be micrometer instead of millimeter). Of course that would mean you would need to interpret values that are shown in mm as um. You can also change displayed length unit from mm to um in Edit/Application settings/Units, but there may be some places where “mm” is hardcoded, so you would still see mm.</p>

---

## Post #3 by @Remco (2017-11-17 15:23 UTC)

<p>Thanks for the advice, I see that I can indeed change the volume spacing in the Volume module. However, the existing volume meshes are not updated, only new models have the new volume spacing applied.</p>
<p>I assume I would have to recreate the models?</p>

---

## Post #4 by @lassoan (2017-11-17 21:57 UTC)

<p>You can scale models by applying a transformation matrix that has the scaling factor in the first 3 values in the diagonal (using Transforms module).</p>

---

## Post #5 by @brhoom (2018-05-10 22:08 UTC)

<p>A related question. I tried to scale to 0.001 but it does not work. The Transforms module does not accept more than 2 places after the decimal point.  I tried this code but also does not work:</p>
<pre><code>nd=getNode('img')
vTransform = vtk.vtkTransform()
vTransform.Scale(0.001,0.001,0.001)
transform = slicer.vtkMRMLLinearTransformNode()
slicer.mrmlScene.AddNode(transform) 
logic = slicer.vtkSlicerTransformLogic()
logic.hardenTransform(nd)</code></pre>

---

## Post #6 by @lassoan (2018-05-10 22:39 UTC)

<p>You can press <code>Ctrl</code> - <code>+</code> to increase the number of displayed decimal digits.</p>

---

## Post #7 by @brhoom (2018-05-11 06:30 UTC)

<p>This works, thanks Andras.</p>

---
