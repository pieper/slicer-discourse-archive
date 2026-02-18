# Bone thickness mapping module was not working. what's the wrong?

**Topic ID**: 29567
**Date**: 2023-05-21
**URL**: https://discourse.slicer.org/t/bone-thickness-mapping-module-was-not-working-whats-the-wrong/29567

---

## Post #1 by @jhchoi (2023-05-21 23:28 UTC)

<p>Python 3.9.10 (main, Feb 22 2023, 01:07:37) [MSC v.1930 64 bit (AMD64)] on win32</p>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<p>TODO: implement cloud fingerprint store<br>
[Qt] libpng warning: iCCP: profile ‘ICC Profile’: ‘CMYK’: invalid ICC profile color space<br>
[Qt] libpng warning: iCCP: known incorrect sRGB profile<br>
[Qt]   Error(s):<br>
[Qt]     CLI executable: C:/Users/User/AppData/Local/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/SlicerVMTK/lib/Slicer-5.2/qt-loadable-modules/vtkvmtk.py<br>
[Qt]     The process failed to start. Either the invoked program is missing, or you may have insufficient permissions to invoke the program.<br>
[Qt] Fail to instantiate module  “vtkvmtk”<br>
[Qt] The following modules failed to be instantiated:<br>
[Qt]    vtkvmtk<br>
Failed to load vtkSlicerStenosisMeasurement3DModuleLogicPython: No module named vtkSlicerShapeModuleMRMLPython<br>
[Qt] QLayout::addChildLayout: layout “” already has a parent<br>
[Qt] This function is deprecated. Use lookFromAxis(const ctkAxesWidget::Axis&amp; axis) instead.<br>
[Qt] ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 100 1<br>
Initializing execution…<br>
Traceback (most recent call last):<br>
File “C:/Users/User/AppData/Local/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/BoneThicknessMapping/lib/Slicer-5.2/qt-scripted-modules/BoneThicknessMapping.py”, line 521, in click_execute<br>
BoneThicknessMappingLogic.set_scalar_colour_bar_state(0)<br>
File “C:/Users/User/AppData/Local/NA-MIC/Slicer 5.2.2/NA-MIC/Extensions-31382/BoneThicknessMapping/lib/Slicer-5.2/qt-scripted-modules/BoneThicknessMapping.py”, line 936, in set_scalar_colour_bar_state<br>
ctkBar = slicer.util.findChildren(colorWidget, name=‘VTKScalarBar’)[0]<br>
IndexError: list index out of range<br>
[Qt] This function is deprecated. Use lookFromAxis(const ctkAxesWidget::Axis&amp; axis) instead.</p>
<p>this module was not working.<br>
what am i do?</p>

---

## Post #2 by @mmonteiro (2023-06-21 11:27 UTC)

<p>I am having the same problem with the SlicerVMTK extension. Whenever I try to run the python console from slicer or run slicer --python-script, I get the following error:<br>
<code>Failed to load vtkSlicerStenosisMeasurement3DModuleLogicPython: No module named vtkSlicerShapeModuleMRMLPython</code></p>

---
