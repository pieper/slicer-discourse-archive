---
topic_id: 38041
title: "Converting Vtk To Dicom"
date: 2024-08-26
url: https://discourse.slicer.org/t/38041
---

# Converting vtk to DICOM

**Topic ID**: 38041
**Date**: 2024-08-26
**URL**: https://discourse.slicer.org/t/converting-vtk-to-dicom/38041

---

## Post #1 by @dbak (2024-08-26 21:22 UTC)

<p>Hi! I have a VTK file (UnstructuredGrid) that I want to convert to a DICOM to share with my colleagues in medicine. I am familiar with VTKs but it is my first time doing anything with DICOM, so I would appreciate any help!</p>
<p>The VTK is of a 3D geometry and has a point data field (let’s call it P) that I want to project/show in the DICOM image.</p>
<p>I can import the VTK to Slicer as a Model and color it through “Scalars” by selecting the field P (see the top part of attached screenshot), but when I want to segment and turn it into a volume to later export as DICOM, I lose the coloring, and only the domain itself is colored by a single color (see lower part of screenshot)… I want to have the same coloring on the “slices” so I can have that as the DICOM…</p>
<p>Can anyone help me with this? Thank you very much!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5bb1a74517e5b83534702079d1f375b27d5dd42.png" data-download-href="/uploads/short-url/wMicSIPSjzIr5nhiLfMcfrc2pIC.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e5bb1a74517e5b83534702079d1f375b27d5dd42_2_690x344.png" alt="image" data-base62-sha1="wMicSIPSjzIr5nhiLfMcfrc2pIC" width="690" height="344" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e5bb1a74517e5b83534702079d1f375b27d5dd42_2_690x344.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e5bb1a74517e5b83534702079d1f375b27d5dd42_2_1035x516.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e5bb1a74517e5b83534702079d1f375b27d5dd42_2_1380x688.png 2x" data-dominant-color="A6A6B6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1912×955 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2024-08-27 09:19 UTC)

<p>I’m not aware of a really fitting format for this in DICOM. What I could imagine is to convert this “colored” mesh into a volume and export it as a conventional CT (or other image) modality. There is no module in Slicer to probe model into volume (only the other way around), but this function does this:</p>
<pre><code class="lang-auto">def probeMeshIntoVolume(self, inputMeshModel, currentMeshArrayName, inputVolume, outputVolume):
  """
  Probe values of a certain array at voxels of a reference volume and copy the probed values to an output volume.
  """
  # Get RAS to IJK transform of the input volume
  ras2IjkMatrix = vtk.vtkMatrix4x4()
  inputVolume.GetRASToIJKMatrix(ras2IjkMatrix)
  ras2IjkTransform = vtk.vtkTransform()
  ras2IjkTransform.SetMatrix(ras2IjkMatrix)
  # Apply the transformation to the grid
  transformFilter = vtk.vtkTransformFilter()
  transformFilter.SetInputData(inputMeshModel.GetUnstructuredGrid())
  transformFilter.SetTransform(ras2IjkTransform)
  transformFilter.Update()

  # Probe mesh with volume
  probeFilter = vtk.vtkProbeFilter()
  probeFilter.SetInputData(inputVolume.GetImageData())
  probeFilter.SetSourceData(transformFilter.GetOutputDataObject(0))  # The mesh grid transformed to IJK
  probeFilter.SetPassPointArrays(True)  # Keep image points as scalars
  probeFilter.Update()

  # Create output volume from comparison
  outputVolume.SetRASToIJKMatrix(ras2IjkMatrix)
  outputVolume.SetName(f'Probed {inputMeshModel.GetName()} ({currentMeshArrayName}) with {inputVolume.GetName()}')
  outputShape = tuple(reversed(probeFilter.GetOutput().GetDimensions()))
  probeArray = vtk.util.numpy_support.vtk_to_numpy(probeFilter.GetOutput().GetPointData().GetArray(currentMeshArrayName))
  outputArray = probeArray.reshape(outputShape)
  slicer.util.updateVolumeFromArray(outputVolume, outputArray)
</code></pre>
<p>The only thing you need but don’t have is a reference volume. You can decide what resolution you need and either create a volume from scratch or load a sample volume and use it (after setting a different spacing if you want).</p>
<p>Then you can export the output volume into DICOM.<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-a-volume-to-dicom-file-format" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-a-volume-to-dicom-file-format</a></p>

---
