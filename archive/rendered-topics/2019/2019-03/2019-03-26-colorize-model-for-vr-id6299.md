---
topic_id: 6299
title: "Colorize Model For Vr"
date: 2019-03-26
url: https://discourse.slicer.org/t/6299
---

# Colorize Model for VR

**Topic ID**: 6299
**Date**: 2019-03-26
**URL**: https://discourse.slicer.org/t/colorize-model-for-vr/6299

---

## Post #1 by @gptruncus (2019-03-26 20:15 UTC)

<p>Hello, is it possible to colorize different parts of an imported STL model(heart) for VR viewing? is this only possible by taking apart or creating two segments of heart and putting them together as different colors?<br>
system: Mac or Windows 10 latest</p>

---

## Post #2 by @cpinter (2019-03-26 22:26 UTC)

<p>You can select the vertices you want to be the same color in ParaView, export the indices, then assign scalars to those vertices with a simple python script. Do this for every color. Then you can use a color table to assign colors to the scalars. Although I only recommend this if you have a low numbre of colors and you need to do it only once (and not for every patient for example).</p>
<p>Here’s a pretty ugly and unorganized but working snippet that I used for this in the past:</p>
<pre><code>m=getNode('model')
d=m.GetDisplayNode()
d.SetBackfaceCulling(False)
c=getNode('modelColorTable')
d.SetAndObserveColorNodeID(c.GetID())
p=m.GetPolyData()
pp=p.GetPointData()
ca=vtk.vtkDoubleArray()
ca.SetName('ColorIndex')
ca.SetNumberOfTuples(p.GetNumberOfPoints())
d.SetActiveScalarName('ColorIndex')
t=getNode('vtkMRMLTableNode1')
tt=t.GetTable()
for i in xrange(ca.GetNumberOfTuples()):
  ca.SetValue(i, 0)
for r in xrange(tt.GetNumberOfRows()):
  i = tt.GetValue(r,0).ToInt()
  ca.SetValue(i, 1)
pp.AddArray(ca)
d.SetActiveScalarName('ColorIndex')
d.SetScalarVisibility(1)</code></pre>

---

## Post #3 by @lassoan (2019-03-27 13:02 UTC)

<p>How do you generate the heart model?</p>
<p>If you have downloaded the model from a 3D model database then usually they come with textures that you can apply (using SlicerIGT extension’s “Texture model” module). If the model did not come with a texture or you don’t like it then you can paint texture using Blender or MeshMixer. If you don’t paint to texture but save the color data as point or cell scalars then you can use the code snippets provided by <a class="mention" href="/u/cpinter">@cpinter</a> above to colorize the model.</p>
<p>If you want to show/hide or change the color of pieces independently, then probably the best is to split the mesh into multiple pieces (e.g., in MeshMixer or ParaView) and load each piece as a separate model. You can place the pieces in a hierarchy (in Data module) and show/hide groups of pieces at once.</p>
<p>If you have a cardiac CT or MRI image then you can create a colored model using Segment Editor module as shown in this video:</p>
<div class="lazyYT" data-youtube-id="BJoIexIvtGo" data-youtube-title="Whole heart segmentation from cardiac CT in 10 minutes" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>

---
