# Colorbar of volume rendering on 3D view

**Topic ID**: 25336
**Date**: 2022-09-19
**URL**: https://discourse.slicer.org/t/colorbar-of-volume-rendering-on-3d-view/25336

---

## Post #1 by @park (2022-09-19 11:10 UTC)

<p>Hellow all,</p>
<p>I would like to make color bar of volume rendering plot on 3D view<br>
The volume rendering function is costum maded for scientific data<br>
(The code indicated below)</p>
<p>Is there any way to make this ?</p>
<pre><code class="lang-auto">def showVolumeRendering(volumeNode):

    volRenLogic = slicer.modules.volumerendering.logic()
    displayNode = volRenLogic.CreateDefaultVolumeRenderingNodes(volumeNode)

    propertyNode = displayNode.GetVolumePropertyNode()

    VolumeProperty = propertyNode.GetVolumeProperty()
    VolumeProperty.SetAmbient(0.95)
    VolumeProperty.SetDiffuse(0.15)
    VolumeProperty.SetSpecular(0.0)
    VolumeProperty.SetSpecularPower(1.0)

    array = slicer.util.arrayFromVolume(volumeNode)
    array_max = np.max(array)

    opacityTransfer = vtk.vtkPiecewiseFunction()
    opacityTransfer.AddPoint(0,0)
    opacityTransfer.AddPoint(array_max*0.15, 0.)
    opacityTransfer.AddPoint(array_max*0.3,0.07)
    opacityTransfer.AddPoint(array_max*0.5,0.07)
    opacityTransfer.AddPoint(array_max*0.6,0.07)
    opacityTransfer.AddPoint(array_max*0.7,0.1)
    opacityTransfer.AddPoint(array_max*0.85,0.35)
    opacityTransfer.AddPoint(array_max*0.99,1)
    opacityTransfer.AddPoint(array_max*1,0.01)

    ctf = vtk.vtkColorTransferFunction()
    ctf.AddRGBPoint(array_max*0.25, 0.1,0.1,1.0)
    ctf.AddRGBPoint(array_max*0.5, 0.2,1.0,0.2)
    ctf.AddRGBPoint(array_max*0.75, 1.0,0.5,0.0)
    ctf.AddRGBPoint(array_max*0.95, 1.0,0.0,0.0)

    propertyNode.SetColor(ctf)
    propertyNode.SetScalarOpacity(opacityTransfer)
</code></pre>

---

## Post #2 by @lassoan (2022-09-19 13:59 UTC)

<p>See how to do this in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#create-custom-color-map-and-display-color-legend">examples in the script repository</a>.</p>

---
