---
topic_id: 8276
title: "Remove 3D View Axis Labels In Python Script"
date: 2019-09-03
url: https://discourse.slicer.org/t/8276
---

# Remove 3D view axis labels in python script

**Topic ID**: 8276
**Date**: 2019-09-03
**URL**: https://discourse.slicer.org/t/remove-3d-view-axis-labels-in-python-script/8276

---

## Post #1 by @ezemikulan (2019-09-03 13:29 UTC)

<p>Hi, I’m trying to save images of a volume render via a python script and I would like to toggle off the axis labels but I’m unable to do so.</p>
<p>I’ve searched inside various objects, <em>layoutManager.threeDWidget(0).threeDView()</em> and <em>layoutManager.threeDWidget(0).threeDView().renderWindow().GetRenderers().GetFirstRenderer()</em>, for example but I can’t find a way.</p>
<p>Here is my code so far:</p>
<pre><code>fname_vol = 'T1.mgz'
loadedVolumeNode = slicer.util.loadVolume(fname_vol)
volumeNode = slicer.util.getNode('T1')

volRenLogic = slicer.modules.volumerendering.logic()
displayNode = volRenLogic.CreateDefaultVolumeRenderingNodes(volumeNode)

layoutManager = slicer.app.layoutManager()
threeDView = layoutManager.threeDWidget(0).threeDView()
renderWindow = threeDView.renderWindow()
renderer = renderWindow.GetRenderers().GetFirstRenderer()
renderWindow.Render()

views_names = ('Anterior', 'Left', 'Right')
views_att = (ctk.ctkAxesWidget().Anterior, ctk.ctkAxesWidget().Left, ctk.ctkAxesWidget().Right)

for v, a in zip(views_names, views_att):
    threeDView.lookFromViewAxis(a)
    renderWindow.SetAlphaBitPlanes(1)
    wti = vtk.vtkWindowToImageFilter()
    wti.SetInputBufferTypeToRGBA()
    wti.SetInput(renderWindow)
    writer = vtk.vtkPNGWriter()
    writer.SetFileName(test_%s.png" % v)
    writer.SetInputConnection(wti.GetOutputPort())
    writer.Write()
</code></pre>
<p>Any help would be very appreciated, cheers,</p>
<p>Operating system: Ubuntu 18<br>
Slicer version: 4.10.2</p>

---

## Post #2 by @aiden.zhu (2019-09-03 13:51 UTC)

<p>Does this help?</p>
<pre><code class="lang-python">v = slicer.mrmlScene.GetNodeByID('vtkMRMLViewNode1')
v.SetAxisLabelsVisible(True)
# or
v.SetAxisLabelsVisible(False)
</code></pre>

---

## Post #3 by @ezemikulan (2019-09-03 13:58 UTC)

<p>It worked perfectly. Thanks a lot!</p>

---
