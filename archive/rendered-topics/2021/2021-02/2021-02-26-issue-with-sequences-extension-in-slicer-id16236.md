# Issue with Sequences extension in Slicer

**Topic ID**: 16236
**Date**: 2021-02-26
**URL**: https://discourse.slicer.org/t/issue-with-sequences-extension-in-slicer/16236

---

## Post #1 by @IGT_User_UC3M (2021-02-26 12:44 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11.20200930</p>
<p>I want to use the 3D Slicer version 4.11.20200930 and the Sequences Extension and Module to record a sequence. The sequence is a video captured with an IntelRealSense camera that is sent to 3D Slicer through Plus Toolkit. I can acquire the images either in black and white (BW) or in RGB. If I do the first option, the corresponding node in 3D Slicer is a vtkMRMLScalarVolumeNode and I can record and save it without any problem. However, if I do acquire the images in RGB, the corresponding node in 3D Slicer is a vtkMRMLVectorVolumeNode. For some reason, it is not recognized as a Proxy Node in the Sequences module. As a result, I cannot record the sequence nor save it.</p>
<p>I attempted to do the same with the 4.10.2 Slicer version and I could record both types of sequences (with the BW and the RGB images) without problems. So, I was wondering if anything has been modified in this new version regarding the vtkMRMLVectorVolumeNodes.</p>
<p>Thank you.</p>

---
