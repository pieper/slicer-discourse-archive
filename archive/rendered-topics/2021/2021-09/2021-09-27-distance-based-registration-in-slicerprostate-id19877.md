# Distance Based Registration in SlicerProstate

**Topic ID**: 19877
**Date**: 2021-09-27
**URL**: https://discourse.slicer.org/t/distance-based-registration-in-slicerprostate/19877

---

## Post #1 by @finetjul (2021-09-27 11:06 UTC)

<p>Hi there,</p>
<p>I’ve been playing with the Distance Based Registration in the SlicerProstate extension, but I failed to make it work.</p>
<p>Here is the error I got:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "C:/Users/julien/AppData/Local/NA-MIC/Slicer 4.13.0-2021-09-26/NA-MIC/Extensions-30261/SlicerProstate/lib/Slicer-4.13/qt-scripted-modules/DistanceMapBasedRegistration.py", line 249, in onApplyButton
    logic.run(self.parameterNode)
  File "C:/Users/julien/AppData/Local/NA-MIC/Slicer 4.13.0-2021-09-26/NA-MIC/Extensions-30261/SlicerProstate/lib/Slicer-4.13/qt-scripted-modules/DistanceMapBasedRegistration.py", line 356, in run
    (bbMin,bbMax) = self.getBoundingBox(fixedLabelNodeID, movingLabelNodeID)
  File "C:/Users/julien/AppData/Local/NA-MIC/Slicer 4.13.0-2021-09-26/NA-MIC/Extensions-30261/SlicerProstate/lib/Slicer-4.13/qt-scripted-modules/DistanceMapBasedRegistration.py", line 501, in getBoundingBox
    unionLabelImage = (cast.Execute(fixedLabelImage) + cast.Execute(movingLabelImage)) &gt; 0
  File "C:\Users\julien\AppData\Local\NA-MIC\Slicer 4.13.0-2021-09-26\lib\Python\lib\site-packages\simpleitk-2.1.0-py3.6-win-amd64.egg\SimpleITK\SimpleITK.py", line 3815, in __add__
    return Add( self, other )
  File "C:\Users\julien\AppData\Local\NA-MIC\Slicer 4.13.0-2021-09-26\lib\Python\lib\site-packages\simpleitk-2.1.0-py3.6-win-amd64.egg\SimpleITK\SimpleITK.py", line 11049, in Add
    return _SimpleITK.Add(*args)
RuntimeError: Exception thrown in SimpleITK Add: D:\D\P\Slicer-0-build\ITK\Modules\Core\Common\include\itkImageToImageFilter.hxx:220:
ITK ERROR: AddImageFilter(000001D14ABEC510): Inputs do not occupy the same physical space! 
InputImage Origin: [0.0000000e+00, 0.0000000e+00, 0.0000000e+00], InputImage_1 Origin: [-7.3025000e+01, -5.4518000e+01, -2.5613000e+00]
	Tolerance: 1.5264600e-07
InputImage Spacing: [1.5264600e-01, 1.5266600e-01, 2.5629900e-01], InputImage_1 Spacing: [4.2970000e-01, 4.2970000e-01, 2.9999500e+00]
	Tolerance: 1.5264600e-07
</code></pre>
<p>The prostate labelmaps are imported contours that have been converted to labelmap (0=air, 1=prostate) in the Segmentations module using a reference image(US + MRI). (I also tried without using a reference image).<br>
I also tried to pre-align (hardened transform) the moving labelmap to share some extent with the fix labelmap.</p>
<p>I typically do not understand the error that stipulates the fix and moving origins and spacing are different. This difference is, to me, expected because we are trying to register.</p>
<p>Thanks,<br>
Julien.</p>

---

## Post #2 by @lassoan (2021-09-28 13:51 UTC)

<p>I’m investigating this and will report what I find.</p>

---
