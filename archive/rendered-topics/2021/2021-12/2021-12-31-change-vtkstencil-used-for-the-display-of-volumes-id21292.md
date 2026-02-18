# Change vtkStencil used for the display of volumes

**Topic ID**: 21292
**Date**: 2021-12-31
**URL**: https://discourse.slicer.org/t/change-vtkstencil-used-for-the-display-of-volumes/21292

---

## Post #1 by @riep (2021-12-31 14:54 UTC)

<p>Dear everyone,<br>
I am working on a python script that overwrite the Background Image Stencil Data used in the display volume node.<br>
It is natively defined in <a href="https://github.com/Slicer/Slicer/blob/0673b1c05404b21d259cfaf85a5f89d9cf1f3771/Libs/MRML/Logic/vtkMRMLSliceLayerLogic.cxx#L797" class="inline-onebox" rel="noopener nofollow ugc">Slicer/vtkMRMLSliceLayerLogic.cxx at 0673b1c05404b21d259cfaf85a5f89d9cf1f3771 · Slicer/Slicer · GitHub</a><br>
I have basically commented all occurrences of SetBackgroundImageStencilDataConnection in the slice layer logic.</p>
<p>Instead, I have initialized my own stencil from a vtkMRMLAnnotationROINode (roiNode)</p>
<pre><code class="lang-auto"> # Create a box implicit function that will be used as a stencil
    roiBox = vtk.vtkBox()
    roiCenter = [0, 0, 0]
    roiNode.GetXYZ(roiCenter)
    roiRadius = [0, 0, 0]
    roiNode.GetRadiusXYZ(roiRadius)
    roiBox.SetBounds(roiCenter[0] - roiRadius[0], roiCenter[0] + roiRadius[0], roiCenter[1] - roiRadius[1], roiCenter[1] + roiRadius[1], roiCenter[2] - roiRadius[2], roiCenter[2] + roiRadius[2])

    rasToBox = vtk.vtkMatrix4x4()
    if roiNode.GetTransformNodeID() != None:
      roiBoxTransformNode = slicer.mrmlScene.GetNodeByID(roiNode.GetTransformNodeID())
      boxToRas = vtk.vtkMatrix4x4()
      roiBoxTransformNode.GetMatrixTransformToWorld(boxToRas)
      rasToBox.DeepCopy(boxToRas)
      rasToBox.Invert()

    ijkToRas = vtk.vtkMatrix4x4()
    volumeNode.GetIJKToRASMatrix(ijkToRas)

    ijkToBox = vtk.vtkMatrix4x4()
    vtk.vtkMatrix4x4.Multiply4x4(rasToBox, ijkToRas, ijkToBox)
    ijkToBoxTransform = vtk.vtkTransform()
    ijkToBoxTransform.SetMatrix(ijkToBox)
    roiBox.SetTransform(ijkToBoxTransform)

    # Use the stencil to fill the volume
    imageData = volumeNode.GetImageData()

    # Convert the implicit function to a stencil
    functionToStencil = vtk.vtkImplicitFunctionToImageStencil()
    functionToStencil.SetInput(roiBox)
    functionToStencil.SetOutputOrigin(imageData.GetOrigin())
    functionToStencil.SetOutputSpacing(imageData.GetSpacing())
    functionToStencil.SetOutputWholeExtent(imageData.GetExtent())
    functionToStencil.Update()
</code></pre>
<p>Then, I bound the output to the volume</p>
<pre><code class="lang-auto">volumeNode.GetScalarVolumeDisplayNode().SetBackgroundImageStencilDataConnection(functionToStencil.GetOutputPort())
</code></pre>
<p>This has no effects and I cannot figure out why.<br>
Does anyone have an idea why?</p>
<p>Thank you in advance,<br>
Pierre<br>
Pierre</p>

---
