# Problems with Segment Registration Module

**Topic ID**: 35951
**Date**: 2024-05-06
**URL**: https://discourse.slicer.org/t/problems-with-segment-registration-module/35951

---

## Post #1 by @Nelson_Wu (2024-05-06 17:45 UTC)

<p>Good afternoon,</p>
<p>I was trying to compute the deformation vector field between two whole brain MRI  gray-scale (with segmentations) images.  I tried to use the segment registration module to assist in that purpose. However, as I input the images and segmentations of the fixed and moving images and hit run, a watch icon appeared, and the following error messages are generated in the Python console:</p>
<p>Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/Extensions-32840/SegmentRegistration/lib/Slicer-5.7/qt-scripted-modules/SegmentRegistration.py”, line 256, in onPerformRegistration<br>
if self.logic.performRegistration():<br>
File “/Applications/Slicer.app/Contents/Extensions-32840/SegmentRegistration/lib/Slicer-5.7/qt-scripted-modules/SegmentRegistration.py”, line 371, in performRegistration<br>
self.createContourLabelmaps()<br>
File “/Applications/Slicer.app/Contents/Extensions-32840/SegmentRegistration/lib/Slicer-5.7/qt-scripted-modules/SegmentRegistration.py”, line 560, in createContourLabelmaps<br>
movingAnatomyOrientedImageData.UnRegister(None)<br>
AttributeError: ‘NoneType’ object has no attribute ‘UnRegister’<br>
[VTK] CropVolume: Invalid input volume or ROI<br>
[Python] Unable to access cropped moving volume<br>
[Python] Invalid data selection<br>
[VTK] Generic Warning: In vtkSlicerSegmentationsModuleLogic.cxx, line 408<br>
[VTK] vtkSlicerSegmentationsModuleLogic::CreateOrientedImageDataFromVolumeNode: Invalid volume node</p>
<p>I have saved both the images and segmentations in nii.gz format and loaded them as volume and segmentations respectively. Should I change the input data into DICOM as in the tutorials to make it working? Thank you for the help in advance!</p>

---
