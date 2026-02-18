# How to access coronal image data array from a Diffusion Weighted Volume Node

**Topic ID**: 6054
**Date**: 2019-03-07
**URL**: https://discourse.slicer.org/t/how-to-access-coronal-image-data-array-from-a-diffusion-weighted-volume-node/6054

---

## Post #1 by @John_DiMatteo (2019-03-07 00:05 UTC)

<p>How can I access coronal pixel data from a MRMLCorePython.vtkMRMLDiffusionWeightedVolumeNode object in a python slicer extension module?</p>
<p>I’m creating a numpy array based on axial diffusion dicom pixel data, e.g.</p>
<p>{code}<br>
np_dwi_array, flip_angles = dicom_util.read_dicomdir(inputDirectory)<br>
outputDWIVolume.SetIJKToRASMatrix(vtk.vtkMatrix4x4())<br>
slicer.util.updateVolumeFromArray(outputDWIVolume, np_dwi_array)<br>
{code}</p>
<p>I’d like to access the coronal pixel data arrays to do region of interest finding analysis on.  It is easier to do this analysis on the coronal orientation, even though the original scan data is in the axial orientation.  The coronal images are displayed in slicer so I figure it should be programmatically accessible as well.</p>
<p>Thanks</p>

---

## Post #2 by @pieper (2019-03-07 20:53 UTC)

<p>Slicer reformats the data on the fly for visualization so you can’t just get the DWI coronal.  But you can use numpy commands or vtk classes to reformat any of the image data.</p>

---

## Post #3 by @John_DiMatteo (2019-03-11 16:50 UTC)

<p>thanks, a numpy transpose was all that was needed and I was over complicating things</p>

---
