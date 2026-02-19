---
topic_id: 40154
title: "Coordinate Error When Outputting Vtk Model"
date: 2024-11-12
url: https://discourse.slicer.org/t/40154
---

# Coordinate error when outputting VTK model

**Topic ID**: 40154
**Date**: 2024-11-12
**URL**: https://discourse.slicer.org/t/coordinate-error-when-outputting-vtk-model/40154

---

## Post #1 by @yoonjh119 (2024-11-12 17:10 UTC)

<p>I am writing a code to read a nifiti file with python code, convert it to vtk format, and save it again. When I display the output result in a slicer, the location is different. Below is the output result (original in red) and the code. I would appreciate your help.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/03b580a5bee2b253ecaa658e4466b587ec17b374.png" data-download-href="/uploads/short-url/wOiAnvs20qI5Vf8ul7rGAazrx2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/03b580a5bee2b253ecaa658e4466b587ec17b374_2_592x500.png" alt="image" data-base62-sha1="wOiAnvs20qI5Vf8ul7rGAazrx2" width="592" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/03b580a5bee2b253ecaa658e4466b587ec17b374_2_592x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/03b580a5bee2b253ecaa658e4466b587ec17b374.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/03b580a5bee2b253ecaa658e4466b587ec17b374.png 2x" data-dominant-color="9691C8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">643×543 48.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<pre data-code-wrap="python"><code class="lang-python">import nibabel as nib
import numpy as np
import vtk
import vmtk.vtkvmtkMiscPython as vtkvmtkMisc
from vtk.util import numpy_support
import matplotlib.pyplot as plt

input_nifti = 'artery1_obj_1.nii.gz'
msk_name='output_test.vtk'

reader = vtk.vtkNIFTIImageReader()
reader.SetFileName(input_nifti)
reader.Update()

cast = vtk.vtkImageCast()
cast.SetInputData(reader.GetOutput())
cast.SetOutputScalarTypeToFloat()
cast.Update()

mc = vtk.vtkMarchingCubes()
mc.SetInputData(cast.GetOutput())
mc.ComputeNormalsOn()
mc.SetValue(0,0.5)
mc.Update()

transform = vtk.vtkTransform()
if reader.GetQFormMatrix():
    transform.Concatenate(reader.GetQFormMatrix())
elif reader.GetSFormMatrix():
    transform.Concatenate(reader.GetSFormMatrix())


tpd = vtk.vtkTransformPolyDataFilter()
tpd.SetInputData(mc.GetOutput())
tpd.SetTransform(transform)
tpd.Update()

writer = vtk.vtkPolyDataWriter()
writer.SetInputData(tpd.GetOutput())
writer.SetFileName(msk_name)
writer.Update()
</code></pre>

---

## Post #2 by @lassoan (2024-11-12 17:24 UTC)

<p>You have saved your mesh to file in RAS coordinate system. This is highly unusual, as DICOM standard uses LPS and all files storing DICOM-derived data is expected to use LPS coordinate system (unless another coordinate system is explicitly specified in the file).</p>
<p>The solution is to add an RAS-&gt;LPS transformation (<code>diag([-1,-1,1,1])</code> matrix) in your polydata transform.</p>
<p>Note that it is not appropriate to use vtkMarchingCubes on a label image. You either need to apply low-pass filter (e.g., Gaussian image smoothing) on the image before passing it to contour filter, or you need to apply low-pass filter (e.g., windowed sinc polydata smoothing) on the contour filter output. Also, using the classic marching cubes algorithm is not the best solution anymore. Flying edges or surface nets provide results at higher quality and/or faster.</p>

---

## Post #3 by @yoonjh119 (2024-11-24 11:40 UTC)

<p>Thank you, the problem has been solved.</p>

---
