---
topic_id: 38003
title: "Segment Misalignment"
date: 2024-08-22
url: https://discourse.slicer.org/t/38003
---

# Segment misalignment

**Topic ID**: 38003
**Date**: 2024-08-22
**URL**: https://discourse.slicer.org/t/segment-misalignment/38003

---

## Post #1 by @Arash1 (2024-08-22 15:25 UTC)

<p>Hi all<br>
Hope you are doing great.<br>
I am working on nasal cavity segmentation. One issue that I have is that the segment doesn’t overlap with the DICOM (picture attached).<br>
A few technical details to mention are that I did crop the volume and used masking.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1aee64b7055e7e4add8fd5a4fec9a823404a98d1.png" alt="Untitled" data-base62-sha1="3QfawBLRO4QbKM0HdrbLHEgKdQR" width="675" height="409"></p>

---

## Post #2 by @muratmaga (2024-08-22 20:07 UTC)

<p>Where is the segmentation coming from? This should not happen if you are running the segmentation in Slicer.</p>

---

## Post #3 by @Arash1 (2024-08-22 20:09 UTC)

<p>Hi<br>
Thank you very much for your response. Segmentation was created in 3D Slicer.</p>

---

## Post #4 by @pieper (2024-08-22 20:11 UTC)

<p>You’ll need to describe your exact steps that led to this result.</p>

---

## Post #5 by @Arash1 (2024-08-22 20:12 UTC)

<p>Hi<br>
I used the crop volume to increase the resolution. Then, I used the SimpleLungMask to create a segment.</p>

---

## Post #6 by @pieper (2024-08-22 20:16 UTC)

<aside class="quote no-group" data-username="Arash1" data-post="5" data-topic="38003">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/arash1/48/78865_2.png" class="avatar"> Arash1:</div>
<blockquote>
<p>SimpleLungMask</p>
</blockquote>
</aside>
<p>I don’t recognize that - is it part of an extension?</p>

---

## Post #7 by @Arash1 (2024-08-22 20:18 UTC)

<p>It belongs to:<br>
Chest Imaging Platform-&gt;Toolkit-&gt;Segmentation-&gt;Generate Simple Lung Mask</p>

---

## Post #8 by @pieper (2024-08-22 20:31 UTC)

<p>That extension may not be fully maintained.  You should try running it on the sample data or tutorial data and if the same issue occurs file an issue with the Chest Imaging Platform group.  It’s possible that the issue is with some tool that’s not correctly accounting for LPS/RAS coordinates.  It would be great if you could help them fix it.</p>

---

## Post #9 by @Arash1 (2024-08-22 20:36 UTC)

<p>Thank you very much.<br>
I will rerun this with all the steps and share the progress.</p>

---

## Post #10 by @Arash1 (2024-08-30 17:45 UTC)

<p>Hello. The problem seems to be the coordinates. Using the “Transforms”, it was solved, but the nature of the challenge remains in place.</p>
<p>One error that I receive the moment I open the app, is the <strong>“ParticlesDisplay” , the dependency “TractographyDisplay” failed to be loaded.</strong> I am not sure how to fix it. I have checked the internet and proxy settings.</p>
<p>Here is the log. I used the sample data.</p>
<p>[DEBUG][Qt] 30.08.2024 11:15:59 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: 20240830_111559<br>
[DEBUG][Qt] 30.08.2024 11:15:59 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 5.6.2 (revision 32448 / f10cd8c) win-amd64 - installed release<br>
[DEBUG][Qt] 30.08.2024 11:15:59 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Operating system …: Windows /  Professional / (Build 22631, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 30.08.2024 11:15:59 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Memory …: 32501 MB physical, 37621 MB virtual<br>
[DEBUG][Qt] 30.08.2024 11:15:59 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CPU …: GenuineIntel , 12 cores, 12 logical processors<br>
[DEBUG][Qt] 30.08.2024 11:15:59 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 30.08.2024 11:15:59 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Qt configuration …: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 30.08.2024 11:15:59 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Internationalization …: disabled, language=<br>
[DEBUG][Qt] 30.08.2024 11:15:59 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Developer mode …: disabled<br>
[DEBUG][Qt] 30.08.2024 11:15:59 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Application path …: C:/Slicer 5.6.2/bin<br>
[DEBUG][Qt] 30.08.2024 11:15:59 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths …: <a href="http://slicer.org/Extensions-32448/Chest_Imaging_Platform/lib/Slicer-5.6/cli-modules" rel="noopener nofollow ugc">slicer.org/Extensions-32448/Chest_Imaging_Platform/lib/Slicer-5.6/cli-modules</a>, <a href="http://slicer.org/Extensions-32448/Chest_Imaging_Platform/lib/Slicer-5.6/qt-loadable-modules" rel="noopener nofollow ugc">slicer.org/Extensions-32448/Chest_Imaging_Platform/lib/Slicer-5.6/qt-loadable-modules</a>, <a href="http://slicer.org/Extensions-32448/Chest_Imaging_Platform/lib/Slicer-5.6/qt-scripted-modules" rel="noopener nofollow ugc">slicer.org/Extensions-32448/Chest_Imaging_Platform/lib/Slicer-5.6/qt-scripted-modules</a><br>
[WARNING][Qt] 30.08.2024 11:16:11 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - When loading module  “ParticlesDisplay” , the dependency “TractographyDisplay” failed to be loaded.<br>
[DEBUG][Python] 30.08.2024 11:16:11 [Python] (C:\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 30.08.2024 11:16:11 [Python] (C:\Slicer 5.6.2\lib\Slicer-5.6\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:39) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 30.08.2024 11:16:11 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 30.08.2024 11:16:57 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “SampleData”<br>
[DEBUG][Python] 30.08.2024 11:17:05 [Python] (C:/Slicer 5.6.2/bin/…/lib/Slicer-5.6/qt-scripted-modules/SampleData.py:384) - Verifying checksum<br>
[DEBUG][Python] 30.08.2024 11:17:05 [Python] (C:/Slicer 5.6.2/bin/…/lib/Slicer-5.6/qt-scripted-modules/SampleData.py:384) - File already exists and checksum is OK - reusing it.<br>
[DEBUG][Python] 30.08.2024 11:17:05 [Python] (C:/Slicer 5.6.2/bin/…/lib/Slicer-5.6/qt-scripted-modules/SampleData.py:384) - Requesting load PreDentalSurgery from C:/Users/amanl/AppData/Local/slicer.org/Slicer/cache/SlicerIO/PreDentalSurgery.gipl.gz …<br>
[DEBUG][Qt] 30.08.2024 11:17:06 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “Volume” Reader has successfully read the file “C:/Users/amanl/AppData/Local/slicer.org/Slicer/cache/SlicerIO/PreDentalSurgery.gipl.gz” “[0.42s]”<br>
[DEBUG][Python] 30.08.2024 11:17:06 [Python] (C:/Slicer 5.6.2/bin/…/lib/Slicer-5.6/qt-scripted-modules/SampleData.py:384) - Load finished<br>
[DEBUG][Python] 30.08.2024 11:17:06 [Python] (C:/Slicer 5.6.2/bin/…/lib/Slicer-5.6/qt-scripted-modules/SampleData.py:384) - Verifying checksum<br>
[DEBUG][Python] 30.08.2024 11:17:06 [Python] (C:/Slicer 5.6.2/bin/…/lib/Slicer-5.6/qt-scripted-modules/SampleData.py:384) - File already exists and checksum is OK - reusing it.<br>
[DEBUG][Python] 30.08.2024 11:17:06 [Python] (C:/Slicer 5.6.2/bin/…/lib/Slicer-5.6/qt-scripted-modules/SampleData.py:384) - Requesting load PostDentalSurgery from C:/Users/amanl/AppData/Local/slicer.org/Slicer/cache/SlicerIO/PostDentalSurgery.gipl.gz …<br>
[DEBUG][Qt] 30.08.2024 11:17:06 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “Volume” Reader has successfully read the file “C:/Users/amanl/AppData/Local/slicer.org/Slicer/cache/SlicerIO/PostDentalSurgery.gipl.gz” “[0.43s]”<br>
[DEBUG][Python] 30.08.2024 11:17:06 [Python] (C:/Slicer 5.6.2/bin/…/lib/Slicer-5.6/qt-scripted-modules/SampleData.py:384) - Load finished<br>
[DEBUG][Qt] 30.08.2024 11:17:10 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “SegmentEditor”<br>
[DEBUG][Qt] 30.08.2024 11:17:18 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “CropVolume”<br>
[INFO][VTK] 30.08.2024 11:17:54 [vtkSlicerCLIModuleLogic (0000022AE29C3100)] (D:\D\S\S-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:870) - Found CommandLine Module, target is C:/Slicer 5.6.2/bin/…/lib/Slicer-5.6/cli-modules/ResampleScalarVectorDWIVolume.exe<br>
[INFO][VTK] 30.08.2024 11:17:54 [vtkSlicerCLIModuleLogic (0000022AE29C3100)] (D:\D\S\S-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:888) - ModuleType: CommandLineModule<br>
[INFO][VTK] 30.08.2024 11:17:54 [vtkSlicerCLIModuleLogic (0000022AE29C3100)] (D:\D\S\S-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:1729) - Resample Scalar/Vector/DWI Volume command line:</p>
<p>C:/Slicer 5.6.2/bin/…/lib/Slicer-5.6/cli-modules/ResampleScalarVectorDWIVolume.exe --hfieldtype h-Field --interpolation nn --transform_order output-to-input --image_center input --spacing 0.0500000000000001,0.0500000000000001,0.0500000000000001 --size 2481,2937,2181 --origin 153.65,146.596,55.7024 --direction_matrix -1,0,0,0,-1,0,0,0,1 --number_of_thread 0 --default_pixel_value 0 --window_function c --spline_order 3 --transform_matrix 1,0,0,0,1,0,0,0,1,0,0,0 --transform a C:/Users/amanl/AppData/Local/Temp/Slicer/HDGE_vtkMRMLScalarVolumeNodeB.nrrd C:/Users/amanl/AppData/Local/Temp/Slicer/HDGE_vtkMRMLScalarVolumeNodeD.nrrd<br>
[INFO][VTK] 30.08.2024 11:23:05 [vtkSlicerCLIModuleLogic (0000022AE29C3100)] (D:\D\S\S-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:1943) - Resample Scalar/Vector/DWI Volume completed without errors<br>
[DEBUG][Qt] 30.08.2024 11:28:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “GenerateSimpleLungMask”<br>
[INFO][VTK] 30.08.2024 11:28:24 [vtkSlicerCLIModuleLogic (0000022AE377AB00)] (D:\D\S\S-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:870) - Found CommandLine Module, target is C:/Slicer 5.6.2/slicer.org/Extensions-32448/Chest_Imaging_Platform/lib/Slicer-5.6/cli-modules/GenerateSimpleLungMask.exe<br>
[INFO][VTK] 30.08.2024 11:28:24 [vtkSlicerCLIModuleLogic (0000022AE377AB00)] (D:\D\S\S-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:888) - ModuleType: CommandLineModule<br>
[INFO][VTK] 30.08.2024 11:29:21 [vtkSlicerCLIModuleLogic (0000022AE377AB00)] (D:\D\S\S-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:1729) - Generate Simple Lung Mask command line:</p>
<p>C:/Slicer 5.6.2/slicer.org/Extensions-32448/Chest_Imaging_Platform/lib/Slicer-5.6/cli-modules/GenerateSimpleLungMask.exe --input C:/Users/amanl/AppData/Local/Temp/Slicer/HDGE_vtkMRMLScalarVolumeNodeD.nrrd --output C:/Users/amanl/AppData/Local/Temp/Slicer/HDGE_vtkMRMLSegmentationNodeC.nrrd --lowDose<br>
[INFO][VTK] 30.08.2024 11:30:27 [vtkSlicerCLIModuleLogic (0000022AE377AB00)] (D:\D\S\S-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:1917) - Generate Simple Lung Mask standard output:</p>
<p>Reading image…<br>
Median filtering…<br>
[ERROR][VTK] 30.08.2024 11:30:27 [vtkSlicerCLIModuleLogic (0000022AE377AB00): Generate Simple Lung Mask standard error:</p>
<p>2024-08-30 11:30:21.820 (  58.746s) [                ]vtkGenericDataArray.txx:390    ERR| vtkTypeInt16Array (000002256F06EA90)] (vtkSlicerCLIModuleLogic.cxx:1923) - Unable to allocate 15892286157 elements of size 2 bytes.<br>
[ERROR][VTK] 30.08.2024 11:30:27 [vtkSlicerCLIModuleLogic (0000022AE377AB00)] (vtkSlicerCLIModuleLogic.cxx:1996) - Generate Simple Lung Mask terminated with an unknown exception<br>
[INFO][VTK] 30.08.2024 11:34:08 [vtkSlicerCLIModuleLogic (0000022AE377AB00)] (D:\D\S\S-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:870) - Found CommandLine Module, target is C:/Slicer 5.6.2/slicer.org/Extensions-32448/Chest_Imaging_Platform/lib/Slicer-5.6/cli-modules/GenerateSimpleLungMask.exe<br>
[INFO][VTK] 30.08.2024 11:34:08 [vtkSlicerCLIModuleLogic (0000022AE377AB00)] (D:\D\S\S-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:888) - ModuleType: CommandLineModule<br>
[INFO][VTK] 30.08.2024 11:36:01 [vtkSlicerCLIModuleLogic (0000022AE377AB00)] (D:\D\S\S-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:1729) - Generate Simple Lung Mask command line:</p>
<p>C:/Slicer 5.6.2/slicer.org/Extensions-32448/Chest_Imaging_Platform/lib/Slicer-5.6/cli-modules/GenerateSimpleLungMask.exe --input C:/Users/amanl/AppData/Local/Temp/Slicer/HDGE_vtkMRMLScalarVolumeNodeD.nrrd --output C:/Users/amanl/AppData/Local/Temp/Slicer/HDGE_vtkMRMLSegmentationNodeD.nrrd<br>
[INFO][VTK] 30.08.2024 11:37:08 [vtkSlicerCLIModuleLogic (0000022AE377AB00)] (D:\D\S\S-0\Base\QTCLI\vtkSlicerCLIModuleLogic.cxx:1917) - Generate Simple Lung Mask standard output:</p>
<p>Reading image…<br>
Lung mask extraction…<br>
[ERROR][VTK] 30.08.2024 11:37:08 [vtkSlicerCLIModuleLogic (0000022AE377AB00): Generate Simple Lung Mask standard error:</p>
<p>2024-08-30 11:37:03.389 (  62.119s) [                ]vtkGenericDataArray.txx:390    ERR| vtkTypeInt16Array (000001C3525910A0)] (vtkSlicerCLIModuleLogic.cxx:1923) - Unable to allocate 15892286157 elements of size 2 bytes.<br>
[ERROR][VTK] 30.08.2024 11:37:08 [vtkSlicerCLIModuleLogic (0000022AE377AB00)] (vtkSlicerCLIModuleLogic.cxx:1996) - Generate Simple Lung Mask terminated with an unknown exception</p>

---

## Post #11 by @pieper (2024-08-30 18:05 UTC)

<p>Again, it’s very likely that the Chest Imaging Platform needs maintenance and you shouldn’t expect to be able to use it without investing time to understand and fix it.</p>
<p>If the issue is the missing Tractography Display module you can try installing the SlicerDMRI extension and that may help.</p>

---
