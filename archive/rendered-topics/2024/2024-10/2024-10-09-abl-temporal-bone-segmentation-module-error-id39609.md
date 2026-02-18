# ABL Temporal Bone Segmentation Module ERROR

**Topic ID**: 39609
**Date**: 2024-10-09
**URL**: https://discourse.slicer.org/t/abl-temporal-bone-segmentation-module-error/39609

---

## Post #1 by @BDA (2024-10-09 12:12 UTC)

<p>Operating system: windows<br>
Slicer version: 5.7.0<br>
Expected behavior: Temporal bone segmentation from CT images<br>
Actual behavior: I want to get a three-dimensional model of the temporal bone in CT images with ABL temporal bone segmentation. But every time in the second step in the rigid registration section at 14% the program gives an error. The error I get every time is <code>CalledProcessError: Command 'elastix' returned non-zero exit status 1.</code> I examined the messages written to users who used this program in the form and encountered the same error, but the solutions offered to them were also insufficient and did not help me. I would be very grateful if you can explain step by step how I can solve this error or if there is an alternative extension program that you can suggest.<br>
I am sharing with you below the part containing the whole process in the Phyton section and the screenshot containing the error.</p>
<details>
<summary>
PYTHON CONSOLE</summary>
<pre><code class="lang-auto">Python 3.9.10 (main, May 26 2024, 23:20:36) [MSC v.1939 64 bit (AMD64)] on win32

&gt;&gt;&gt;

[Qt] libpng warning: iCCP: known incorrect sRGB profile

[Qt] libpng warning: iCCP: too many profiles

[Python] Geometric issues were found with 1 of the series. Please use caution.

[ITK] WARNING: In C:\D\P\S-0-build\ITK\Modules\IO\ImageBase\include\itkImageSeriesReader.hxx, line 478

[ITK] ImageSeriesReader (00000198A95A3D50): Non uniform sampling or missing slices detected, maximum nonuniformity:0.000995263

Downloading atlas... 0%

Downloading atlas... 100%

Downloading atlas... 100%

Downloading atlas... 100%

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 100

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 119

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 119

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 119

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 119

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 119

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 100

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 119

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 100

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 119

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 100

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 119

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 100

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsNode.h, line 782

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsNode::RemoveMarkup method is deprecated, please use RemoveNthControlPoint instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 100

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 119

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 100

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 119

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 100

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 119

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 100

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsNode.h, line 782

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsNode::RemoveMarkup method is deprecated, please use RemoveNthControlPoint instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 100

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 119

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 100

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 119

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 100

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 119

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 100

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsNode.h, line 782

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsNode::RemoveMarkup method is deprecated, please use RemoveNthControlPoint instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 100

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 119

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 100

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 119

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 100

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 119

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 100

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsNode.h, line 782

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsNode::RemoveMarkup method is deprecated, please use RemoveNthControlPoint instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 100

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 119

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 100

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 119

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 100

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 119

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 100

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsNode.h, line 782

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsNode::RemoveMarkup method is deprecated, please use RemoveNthControlPoint instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 100

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 100

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 119

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 113

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E96FB0): vtkMRMLMarkupsFiducialNode::AddFiducialFromArray method is deprecated, please use AddControlPoint instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 100

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 119

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 113

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E96FB0): vtkMRMLMarkupsFiducialNode::AddFiducialFromArray method is deprecated, please use AddControlPoint instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 100

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 119

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 113

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E96FB0): vtkMRMLMarkupsFiducialNode::AddFiducialFromArray method is deprecated, please use AddControlPoint instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 100

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 119

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 113

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E96FB0): vtkMRMLMarkupsFiducialNode::AddFiducialFromArray method is deprecated, please use AddControlPoint instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 100

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 119

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 113

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E96FB0): vtkMRMLMarkupsFiducialNode::AddFiducialFromArray method is deprecated, please use AddControlPoint instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 100

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 119

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 113

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E96FB0): vtkMRMLMarkupsFiducialNode::AddFiducialFromArray method is deprecated, please use AddControlPoint instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 100

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 119

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 113

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E96FB0): vtkMRMLMarkupsFiducialNode::AddFiducialFromArray method is deprecated, please use AddControlPoint instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 100

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 119

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 113

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E96FB0): vtkMRMLMarkupsFiducialNode::AddFiducialFromArray method is deprecated, please use AddControlPoint instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 100

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 119

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 113

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E96FB0): vtkMRMLMarkupsFiducialNode::AddFiducialFromArray method is deprecated, please use AddControlPoint instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 100

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 119

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 173

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E91450): vtkMRMLMarkupsFiducialNode::GetNthFiducialLabel method is deprecated, please use GetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 113

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E96FB0): vtkMRMLMarkupsFiducialNode::AddFiducialFromArray method is deprecated, please use AddControlPoint instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 100

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 179

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::SetNthFiducialLabel method is deprecated, please use SetNthControlPointLabel instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 119

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E954D0): vtkMRMLMarkupsFiducialNode::GetNthFiducialPosition method is deprecated, please use GetNthControlPointPosition instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 100

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E96FB0): vtkMRMLMarkupsFiducialNode::GetNumberOfFiducials method is deprecated, please use GetNumberOfControlPoints instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 167

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E96FB0): vtkMRMLMarkupsFiducialNode::SetNthFiducialVisibility method is deprecated, please use SetNthControlPointVisibility instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 167

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E96FB0): vtkMRMLMarkupsFiducialNode::SetNthFiducialVisibility method is deprecated, please use SetNthControlPointVisibility instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 167

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E96FB0): vtkMRMLMarkupsFiducialNode::SetNthFiducialVisibility method is deprecated, please use SetNthControlPointVisibility instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 167

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E96FB0): vtkMRMLMarkupsFiducialNode::SetNthFiducialVisibility method is deprecated, please use SetNthControlPointVisibility instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 167

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E96FB0): vtkMRMLMarkupsFiducialNode::SetNthFiducialVisibility method is deprecated, please use SetNthControlPointVisibility instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 167

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E96FB0): vtkMRMLMarkupsFiducialNode::SetNthFiducialVisibility method is deprecated, please use SetNthControlPointVisibility instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 167

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E96FB0): vtkMRMLMarkupsFiducialNode::SetNthFiducialVisibility method is deprecated, please use SetNthControlPointVisibility instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 167

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E96FB0): vtkMRMLMarkupsFiducialNode::SetNthFiducialVisibility method is deprecated, please use SetNthControlPointVisibility instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 167

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E96FB0): vtkMRMLMarkupsFiducialNode::SetNthFiducialVisibility method is deprecated, please use SetNthControlPointVisibility instead

[VTK] Warning: In vtkMRMLMarkupsFiducialNode.h, line 167

[VTK] vtkMRMLMarkupsFiducialNode (00000198B1E96FB0): vtkMRMLMarkupsFiducialNode::SetNthFiducialVisibility method is deprecated, please use SetNthControlPointVisibility instead

Volume registration is started in working directory: C:/Users/betul/AppData/Local/Temp/Slicer/Elastix/20241009_150325_942

Register volumes...

elastix is started at Wed Oct 9 15:03:38 2024.

which elastix: C:\Users\betul\AppData\Local\slicer.org\Slicer 5.7.0-2024-05-24\slicer.org\Extensions-32875\SlicerElastix\lib\Slicer-5.7\elastix.exe

elastix version: 5.1.0

Git revision SHA: d652938573e5f193955908eba225a854b31ce36a

Git revision date: Thu Jan 12 14:20:18 2023 +0100

Build date: May 25 2024 04:08:21

Compiler: Visual C++ version 193933523.0

Memory address size: 64-bit

CMake version: 3.22.1

ITK version: 5.3.0

Command-line arguments:

-f C:/Users/betul/AppData/Local/Temp/Slicer/Elastix/20241009_150325_942\input\fixed.mha -m C:/Users/betul/AppData/Local/Temp/Slicer/Elastix/20241009_150325_942\input\moving.mha -fMask C:/Users/betul/AppData/Local/Temp/Slicer/Elastix/20241009_150325_942\input\fixedMask.mha -mMask C:/Users/betul/AppData/Local/Temp/Slicer/Elastix/20241009_150325_942\input\movingMask.mha -p "C:\Users\betul\AppData\Local\slicer.org\Slicer 5.7.0-2024-05-24\slicer.org\Extensions-32875\ABLTemporalBoneSegmentation\lib\Slicer-5.7\qt-scripted-modules\Resources\Parameters\Parameters_Rigid.txt" -out C:/Users/betul/AppData/Local/Temp/Slicer/Elastix/20241009_150325_942\result-transform

elastix runs at: MSI

Windows Personal (x64), (Build 9200)

with 16230 MB memory, and 6 cores @ 2592 MHz.

-------------------------------------------------------------------------

Running elastix with parameter file 0: "C:\Users\betul\AppData\Local\slicer.org\Slicer 5.7.0-2024-05-24\slicer.org\Extensions-32875\ABLTemporalBoneSegmentation\lib\Slicer-5.7\qt-scripted-modules\Resources\Parameters\Parameters_Rigid.txt".

Current time: Wed Oct 9 15:03:38 2024.

Reading the elastix parameters from file ...

Installing all components.

InstallingComponents was successful.

ELASTIX version: 5.1.0

Command line options from ElastixBase:

-f C:/Users/betul/AppData/Local/Temp/Slicer/Elastix/20241009_150325_942\input\fixed.mha

-m C:/Users/betul/AppData/Local/Temp/Slicer/Elastix/20241009_150325_942\input\moving.mha

-fMask C:/Users/betul/AppData/Local/Temp/Slicer/Elastix/20241009_150325_942\input\fixedMask.mha

-mMask C:/Users/betul/AppData/Local/Temp/Slicer/Elastix/20241009_150325_942\input\movingMask.mha

-out C:\Users\betul\AppData\Local\Temp\Slicer\Elastix\20241009_150325_942\result-transform\

-p C:\Users\betul\AppData\Local\slicer.org\Slicer 5.7.0-2024-05-24\slicer.org\Extensions-32875\ABLTemporalBoneSegmentation\lib\Slicer-5.7\qt-scripted-modules\Resources\Parameters\Parameters_Rigid.txt

-priority unspecified, so NORMAL process priority

-threads unspecified, so all available threads are used

WARNING: The parameter "UseDirectionCosines", requested at entry number 0, does not exist at all.

The default value "true" is used instead.

WARNING: The option "UseDirectionCosines" was not found in your parameter file.

From elastix 4.8 it defaults to true!

This may change the behavior of your registrations considerably.

Command line options from TransformBase:

-t0 unspecified, so no initial transform used

Reading images...

Reading images took 2755 ms.

WARNING: the fixed pyramid schedule is not fully specified!

A default pyramid schedule is used.

WARNING: the moving pyramid schedule is not fully specified!

A default pyramid schedule is used.

WARNING: The parameter "AutomaticTransformInitializationMethod", requested at entry number 0, does not exist at all.

The default value "GeometricalCenter" is used instead.

Transform parameters are initialized as: [0, 0, 0, -8.409050160942527, -149.67364680019364, -539.3851643195211]

Scales are estimated automatically.

Scales for transform parameters are: [3478.2728631552554, 3139.864046504555, 2777.083053093664, 1, 1, 1]

Initialization of all components (before registration) took: 22 ms.

Preparation of the image pyramids took: 3592 ms.

Resolution: 0

WARNING: The parameter "ShowExactMetricValue", requested at entry number 0, does not exist at all.

The default value "false" is used instead.

WARNING: The parameter "CheckNumberOfSamples", requested at entry number 0, does not exist at all.

The default value "true" is used instead.

WARNING: The parameter "UseMultiThreadingForMetrics", requested at entry number 0, does not exist at all.

The default value "true" is used instead.

WARNING: The parameter "ErodeFixedMask", requested at entry number 0, does not exist at all.

The default value "false" is used instead.

WARNING: The parameter "ErodeMovingMask", requested at entry number 0, does not exist at all.

The default value "false" is used instead.

Setting the fixed masks took: 1 ms.

Setting the moving masks took: 0 ms.

WARNING: The parameter "NumberOfFixedHistogramBins", requested at entry number 0, does not exist at all.

The default value "32" is used instead.

WARNING: The parameter "NumberOfMovingHistogramBins", requested at entry number 0, does not exist at all.

The default value "32" is used instead.

WARNING: The parameter "FixedLimitRangeRatio", requested at entry number 0, does not exist at all.

The default value "0.01" is used instead.

WARNING: The parameter "MovingLimitRangeRatio", requested at entry number 0, does not exist at all.

The default value "0.01" is used instead.

WARNING: The parameter "FixedKernelBSplineOrder", requested at entry number 0, does not exist at all.

The default value "0" is used instead.

WARNING: The parameter "MovingKernelBSplineOrder", requested at entry number 0, does not exist at all.

The default value "3" is used instead.

WARNING: The parameter "UseFastAndLowMemoryVersion", requested at entry number 0, does not exist at all.

The default value "true" is used instead.

WARNING: The parameter "UseJacobianPreconditioning", requested at entry number 0, does not exist at all.

The default value "false" is used instead.

WARNING: The parameter "FiniteDifferenceDerivative", requested at entry number 0, does not exist at all.

The default value "false" is used instead.

WARNING: The parameter "SP_A", requested at entry number 0, does not exist at all.

The default value "20" is used instead.

WARNING: The parameter "MaximumNumberOfSamplingAttempts", requested at entry number 0, does not exist at all.

The default value "0" is used instead.

WARNING: The parameter "SigmoidInitialTime", requested at entry number 0, does not exist at all.

The default value "0" is used instead.

WARNING: The parameter "MaxBandCovSize", requested at entry number 0, does not exist at all.

The default value "192" is used instead.

WARNING: The parameter "NumberOfBandStructureSamples", requested at entry number 0, does not exist at all.

The default value "10" is used instead.

WARNING: The parameter "UseAdaptiveStepSizes", requested at entry number 0, does not exist at all.

The default value "true" is used instead.

WARNING: The parameter "AutomaticParameterEstimation", requested at entry number 0, does not exist at all.

The default value "true" is used instead.

WARNING: The parameter "UseConstantStep", requested at entry number 0, does not exist at all.

The default value "false" is used instead.

WARNING: The parameter "MaximumStepLengthRatio", requested at entry number 0, does not exist at all.

The default value "1" is used instead.

WARNING: The parameter "MaximumStepLength", requested at entry number 0, does not exist at all.

The default value "0.236356" is used instead.

WARNING: The parameter "NumberOfGradientMeasurements", requested at entry number 0, does not exist at all.

The default value "0" is used instead.

WARNING: The parameter "NumberOfJacobianMeasurements", requested at entry number 0, does not exist at all.

The default value "1000" is used instead.

WARNING: The parameter "NumberOfSamplesForExactGradient", requested at entry number 0, does not exist at all.

The default value "100000" is used instead.

WARNING: The parameter "SigmoidScaleFactor", requested at entry number 0, does not exist at all.

The default value "0.1" is used instead.

Elastix initialization of all components (for this resolution) took: 2 ms.

Computing the fixed image extrema took 3 ms.

Computing the moving image extrema took 3 ms.

Initialization of AdvancedMattesMutualInformation metric took: 57 ms.

Starting automatic parameter estimation for AdaptiveStochasticGradientDescent ...

WARNING: The parameter "ASGDParameterEstimationMethod", requested at entry number 0, does not exist at all.

The default value "Original" is used instead.

Computing JacobianTerms ...

Computing the Jacobian terms took 0.000634s

NumberOfGradientMeasurements to estimate sigma_i: 11

Sampling gradients ...

Time spent in resolution 0 (ITK initialization and iterating): 0.061 s.

Stopping condition: Error in metric.

Settings of AdaptiveStochasticGradientDescent in resolution 0:

( SP_a 1.000000 )

( SP_A 20.000000 )

( SP_alpha 0.602000 )

( SigmoidMax 1.000000 )

( SigmoidMin -0.800000 )

( SigmoidScale 0.000000 )

itk::ExceptionObject (0000007393CFDE80)

Location: "ElastixTemplate - Run()"

File: C:\D\P\S-0-E-b\SlicerElastix-build\elastix\Common\CostFunctions\itkAdvancedImageToImageMetric.hxx

Line: 916

Description: ITK ERROR: AdvancedMattesMutualInformationMetric(000002323CDC0C10): Too many samples map outside moving image buffer: 0 / 1117

Error occurred during actual registration.

Errors occurred!

Error: Command 'elastix' returned non-zero exit status 1.

Traceback (most recent call last):

File "C:/Users/betul/AppData/Local/slicer.org/Slicer 5.7.0-2024-05-24/slicer.org/Extensions-32875/ABLTemporalBoneSegmentation/lib/Slicer-5.7/qt-scripted-modules/ABLTemporalBoneSegmentationModule.py", line 635, in process_transform

output = function()

File "C:/Users/betul/AppData/Local/slicer.org/Slicer 5.7.0-2024-05-24/slicer.org/Extensions-32875/ABLTemporalBoneSegmentation/lib/Slicer-5.7/qt-scripted-modules/ABLTemporalBoneSegmentationModule.py", line 808, in transform

return ABLTemporalBoneSegmentationModuleLogic().apply_elastix_rigid_registration(elastix=self.elastixLogic,

File "C:/Users/betul/AppData/Local/slicer.org/Slicer 5.7.0-2024-05-24/slicer.org/Extensions-32875/ABLTemporalBoneSegmentation/lib/Slicer-5.7/qt-scripted-modules/ABLTemporalBoneSegmentationModule.py", line 1311, in apply_elastix_rigid_registration

elastix.registerVolumes(

File "C:\Users\betul\AppData\Local\slicer.org\Slicer 5.7.0-2024-05-24\slicer.org\Extensions-32875\SlicerElastix\lib\Slicer-5.7\qt-scripted-modules\Elastix.py", line 637, in registerVolumes

self.logProcessOutput(elastixProcess)

File "C:\Users\betul\AppData\Local\slicer.org\Slicer 5.7.0-2024-05-24\slicer.org\Extensions-32875\SlicerElastix\lib\Slicer-5.7\qt-scripted-modules\Elastix.py", line 572, in logProcessOutput

raise subprocess.CalledProcessError(return_code, "elastix")

subprocess.CalledProcessError: Command 'elastix' returned non-zero exit status 1.
![1|690x358](upload://hlzVbbzNx2HvPvNRrmifgYqTwxm.jpeg)
</code></pre>
</details>

---

## Post #2 by @lassoan (2024-10-10 04:33 UTC)

<aside class="quote no-group" data-username="BDA" data-post="1" data-topic="39609">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/b/5e9695/48.png" class="avatar"> BDA:</div>
<blockquote>
<pre><code class="lang-auto">Description: ITK ERROR: AdvancedMattesMutualInformationMetric(000002323CDC0C10): Too many samples map outside moving image buffer: 0 / 1117
</code></pre>
</blockquote>
</aside>
<p>This means the fixed and moving images are too far from each other. Most likely the issue is that you do not register your image to the atlas correctly. A few people has struggled with this, too - see <a href="https://github.com/Auditory-Biophysics-Lab/Slicer-ABLTemporalBoneSegmentation/issues/9">here</a>. You may work with these people to figure out how to do this registration. You may try to contact the developers of this extension, but there have not been any updates in the repository for several years, so you may need to do some digging to find someone.</p>

---
