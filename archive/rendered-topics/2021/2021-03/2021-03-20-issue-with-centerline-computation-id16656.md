# Issue with centerline computation

**Topic ID**: 16656
**Date**: 2021-03-20
**URL**: https://discourse.slicer.org/t/issue-with-centerline-computation/16656

---

## Post #1 by @PANC (2021-03-20 13:03 UTC)

<p>Operating system: Win10<br>
Slicer version: 4.11<br>
Expected behavior: Centerline computation<br>
Actual behavior: Centerline computation is not in Vascular Modeling Toolkit modular<br>
Hi, I am using 3D_Slicer 4.11 to extract the centerline and reconstruct 3D model of blood vessel. I have installed the  SlicerVMTK, SegmentEditorExtraEffects. But I have a problem, that is, there is no “centerline conputation” in Vascular Modeling Toolkit modular. Please help me, thank you.</p>

---

## Post #2 by @lassoan (2021-03-20 13:04 UTC)

<p>Could you copy here the application log (menu: Help / Report a bug)?</p>

---

## Post #3 by @PANC (2021-03-21 01:45 UTC)

<p>ok, i have pasted the log.<br>
[DEBUG][Qt] 21.03.2021 09:25:41 [] (unknown:0) - Session start time …: 2021-03-21 09:25:41<br>
[DEBUG][Qt] 21.03.2021 09:25:41 [] (unknown:0) - Slicer version …: 4.11.20200930 (revision 29402 / 002be18) win-amd64 - installed release<br>
[DEBUG][Qt] 21.03.2021 09:25:41 [] (unknown:0) - Operating system …: Windows /  Professional / (Build 19042, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 21.03.2021 09:25:41 [] (unknown:0) - Memory …: 8078 MB physical, 9358 MB virtual<br>
[DEBUG][Qt] 21.03.2021 09:25:41 [] (unknown:0) - CPU …: GenuineIntel , 4 cores, 4 logical processors<br>
[DEBUG][Qt] 21.03.2021 09:25:41 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 21.03.2021 09:25:41 [] (unknown:0) - Qt configuration …: version 5.15.1, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 21.03.2021 09:25:41 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 21.03.2021 09:25:41 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 21.03.2021 09:25:41 [] (unknown:0) - Application path …: D:/ProgramData/NA-MIC/Slicer 4.11.20200930/bin<br>
[DEBUG][Qt] 21.03.2021 09:25:41 [] (unknown:0) - Additional module paths …: C:/Users/pc/AppData/Roaming/NA-MIC/Extensions-29402/DCMQI/lib/Slicer-4.11/cli-modules, C:/Users/pc/AppData/Roaming/NA-MIC/Extensions-29402/DebuggingTools/lib/Slicer-4.11/qt-scripted-modules, C:/Users/pc/AppData/Roaming/NA-MIC/Extensions-29402/MatlabBridge/lib/Slicer-4.11/cli-modules, C:/Users/pc/AppData/Roaming/NA-MIC/Extensions-29402/MatlabBridge/lib/Slicer-4.11/qt-loadable-modules, C:/Users/pc/AppData/Roaming/NA-MIC/Extensions-29402/SlicerOpenIGTLink/lib/Slicer-4.11/qt-loadable-modules, C:/Users/pc/AppData/Roaming/NA-MIC/Extensions-29402/SlicerOpenIGTLink/lib/Slicer-4.11/qt-scripted-modules, C:/Users/pc/AppData/Roaming/NA-MIC/Extensions-29402/SegmentEditorExtraEffects/lib/Slicer-4.11/qt-scripted-modules, C:/Users/pc/AppData/Roaming/NA-MIC/Extensions-29402/MarkupsToModel/lib/Slicer-4.11/qt-loadable-modules, C:/Users/pc/AppData/Roaming/NA-MIC/Extensions-29402/SlicerVMTK/lib/Slicer-4.11/qt-loadable-modules, C:/Users/pc/AppData/Roaming/NA-MIC/Extensions-29402/SlicerVMTK/lib/Slicer-4.11/qt-scripted-modules, C:/Users/pc/AppData/Roaming/NA-MIC/Extensions-29402/MatlabModules<br>
[DEBUG][Python] 21.03.2021 09:25:48 [Python] (D:\ProgramData\NA-MIC\Slicer 4.11.20200930\lib\Python\Lib\site-packages\pydicom\datadict.py:432) - Reversing DICOM dictionary so can look up tag from a keyword…<br>
[CRITICAL][Qt] 21.03.2021 09:25:50 [] (unknown:0) -   Error(s):<br>
CLI executable: C:/Users/pc/AppData/Roaming/NA-MIC/Extensions-29402/SlicerVMTK/lib/Slicer-4.11/qt-loadable-modules/vtkvmtk.py<br>
The process failed to start. Either the invoked program is missing, or you may have insufficient permissions to invoke the program.<br>
[CRITICAL][Qt] 21.03.2021 09:25:50 [] (unknown:0) - Fail to instantiate module  “vtkvmtk”<br>
[CRITICAL][Qt] 21.03.2021 09:25:50 [] (unknown:0) - The following modules failed to be instantiated:<br>
[CRITICAL][Qt] 21.03.2021 09:25:50 [] (unknown:0) -    vtkvmtk<br>
[DEBUG][Python] 21.03.2021 09:25:51 [Python] (D:\ProgramData\NA-MIC\Slicer 4.11.20200930\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Qt] 21.03.2021 09:25:52 [] (unknown:0) - Matlab executable found on system at 0<br>
[DEBUG][Python] 21.03.2021 09:25:53 [Python] (D:\ProgramData\NA-MIC\Slicer 4.11.20200930\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 21.03.2021 09:25:53 [Python] (D:\ProgramData\NA-MIC\Slicer 4.11.20200930\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 21.03.2021 09:25:54 [] (unknown:0) - Switch to module:  “Welcome”<br>
[INFO][VTK] 21.03.2021 09:25:59 [vtkMRMLScene (000002419E6C61D0)] (D:\D\S\Slicer-0\Libs\MRML\Core\vtkMRMLScene.cxx:316) - vtkMRMLScene::Clear<br>
[INFO][VTK] 21.03.2021 09:25:59 [vtkMRMLScene (000002419E6C61D0)] (D:\D\S\Slicer-0\Libs\MRML\Core\vtkMRMLScene.cxx:762) - vtkMRMLScene::Import<br>
[INFO][VTK] 21.03.2021 09:25:59 [vtkMRMLVolumeArchetypeStorageNode (00000241AE6F1150)] (D:\D\S\Slicer-0\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:473) - Loaded volume from file: C:/Users/pc/AppData/Roaming/NA-MIC/Extensions-29402/SlicerVMTK/lib/Slicer-4.11/qt-scripted-modules/Resources/Vesselness.png. Dimensions: 65x50x1. Number of components: 3. Pixel type: unsigned char.<br>
[INFO][VTK] 21.03.2021 09:25:59 [vtkMRMLScene (00000241AE25A020)] (D:\D\S\Slicer-0\Libs\MRML\Core\vtkMRMLScene.cxx:316) - vtkMRMLScene::Clear<br>
[INFO][VTK] 21.03.2021 09:25:59 [vtkMRMLScene (00000241AE25A020)] (D:\D\S\Slicer-0\Libs\MRML\Core\vtkMRMLScene.cxx:762) - vtkMRMLScene::Import<br>
[INFO][VTK] 21.03.2021 09:25:59 [vtkMRMLScene (000002419E6C61D0)] (D:\D\S\Slicer-0\Libs\MRML\Core\vtkMRMLScene.cxx:316) - vtkMRMLScene::Clear<br>
[INFO][Stream] 21.03.2021 09:25:59 [] (unknown:0) - Loading Slicer RC file [C:/Users/pc/.slicerrc.py]<br>
[DEBUG][Python] 21.03.2021 09:28:33 [Python] (D:/ProgramData/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/SampleData.py:373) - </p><p>Status: <i>Idle</i></p><br>
[DEBUG][Qt] 21.03.2021 09:28:33 [] (unknown:0) - Switch to module:  “SampleData”<br>
[DEBUG][Python] 21.03.2021 09:28:36 [Python] (D:/ProgramData/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/SampleData.py:373) - <b>Requesting download</b> <i>Panoramix-cropped.nrrd</i> from <a href="https://github.com/Slicer/SlicerTestingData/releases/download/SHA256/146af87511520c500a3706b7b2bfb545f40d5d04dd180be3a7a2c6940e447433" rel="noopener nofollow ugc">https://github.com/Slicer/SlicerTestingData/releases/download/SHA256/146af87511520c500a3706b7b2bfb545f40d5d04dd180be3a7a2c6940e447433</a> …<br>
[DEBUG][Python] 21.03.2021 09:28:40 [Python] (D:/ProgramData/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/SampleData.py:373) - <i>Downloaded 3.5 MB (10% of 35.4 MB)…</i><br>
[DEBUG][Python] 21.03.2021 09:28:50 [Python] (D:/ProgramData/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/SampleData.py:373) - <i>Downloaded 7.1 MB (20% of 35.4 MB)…</i><br>
[DEBUG][Python] 21.03.2021 09:28:59 [Python] (D:/ProgramData/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/SampleData.py:373) - <i>Downloaded 10.6 MB (30% of 35.4 MB)…</i><br>
[DEBUG][Python] 21.03.2021 09:29:09 [Python] (D:/ProgramData/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/SampleData.py:373) - <i>Downloaded 14.2 MB (40% of 35.4 MB)…</i><br>
[DEBUG][Python] 21.03.2021 09:29:20 [Python] (D:/ProgramData/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/SampleData.py:373) - <i>Downloaded 17.7 MB (50% of 35.4 MB)…</i><br>
[DEBUG][Python] 21.03.2021 09:29:32 [Python] (D:/ProgramData/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/SampleData.py:373) - <i>Downloaded 21.2 MB (60% of 35.4 MB)…</i><br>
[DEBUG][Python] 21.03.2021 09:29:39 [Python] (D:/ProgramData/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/SampleData.py:373) - <i>Downloaded 24.8 MB (70% of 35.4 MB)…</i><br>
[DEBUG][Python] 21.03.2021 09:29:46 [Python] (D:/ProgramData/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/SampleData.py:373) - <i>Downloaded 28.3 MB (80% of 35.4 MB)…</i><br>
[DEBUG][Python] 21.03.2021 09:29:57 [Python] (D:/ProgramData/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/SampleData.py:373) - <i>Downloaded 31.8 MB (90% of 35.4 MB)…</i><br>
[DEBUG][Python] 21.03.2021 09:30:07 [Python] (D:/ProgramData/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/SampleData.py:373) - <i>Downloaded 35.4 MB (100% of 35.4 MB)…</i><br>
[DEBUG][Python] 21.03.2021 09:30:07 [Python] (D:/ProgramData/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/SampleData.py:373) - <b>Download finished</b><br>
[DEBUG][Python] 21.03.2021 09:30:07 [Python] (D:/ProgramData/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/SampleData.py:373) - <b>Verifying checksum</b><br>
[DEBUG][Python] 21.03.2021 09:30:07 [Python] (D:/ProgramData/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/SampleData.py:373) - <b>Checksum OK</b><br>
[DEBUG][Python] 21.03.2021 09:30:07 [Python] (D:/ProgramData/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/SampleData.py:373) - <b>Requesting load</b> <i>Panoramix-cropped</i> from C:/Users/pc/AppData/Local/Temp/Slicer/RemoteIO/Panoramix-cropped.nrrd …<br>
[INFO][VTK] 21.03.2021 09:30:08 [vtkMRMLVolumeArchetypeStorageNode (00000241AE6F1910)] (D:\D\S\Slicer-0\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:473) - Loaded volume from file: C:/Users/pc/AppData/Local/Temp/Slicer/RemoteIO/Panoramix-cropped.nrrd. Dimensions: 441x321x215. Number of components: 1. Pixel type: short.<br>
[INFO][VTK] 21.03.2021 09:30:08 [vtkMRMLScene (00000241B0578260)] (D:\D\S\Slicer-0\Libs\MRML\Core\vtkMRMLScene.cxx:316) - vtkMRMLScene::Clear<br>
[DEBUG][Qt] 21.03.2021 09:30:08 [] (unknown:0) - “Volume” Reader has successfully read the file “C:/Users/pc/AppData/Local/Temp/Slicer/RemoteIO/Panoramix-cropped.nrrd” “[1.00s]”<br>
[DEBUG][Python] 21.03.2021 09:30:09 [Python] (D:/ProgramData/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/SampleData.py:373) - <b>Load finished</b><br>
[DEBUG][Qt] 21.03.2021 09:31:47 [] (unknown:0) - Switch to module:  “SegmentEditor”<br>
[WARNING][Qt] 21.03.2021 09:31:48 [] (unknown:0) - QLayout::addChildLayout: layout “” already has a parent<br>
[WARNING][Qt] 21.03.2021 09:31:48 [] (unknown:0) - ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 100 1<br>
[INFO][Python] 21.03.2021 09:36:32 [Python] (D:\ProgramData\NA-MIC\Slicer 4.11.20200930\lib\Slicer-4.11\qt-scripted-modules\SegmentEditorEffects\SegmentEditorIslandsEffect.py:155) - 1 islands created (3 ignored)<br>
[INFO][Stream] 21.03.2021 09:36:32 [] (unknown:0) - 1 islands created (3 ignored)<br>
[DEBUG][Qt] 21.03.2021 09:36:47 [] (unknown:0) - Switch to module:  “Data”<br>
[DEBUG][Qt] 21.03.2021 09:37:18 [] (unknown:0) - Switch to module:  “SurfaceToolbox”<br>
[INFO][Python] 21.03.2021 09:38:07 [Python] (D:/ProgramData/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/SurfaceToolbox.py:378) - Processing started<br>
[INFO][Python] 21.03.2021 09:38:07 [Python] (D:/ProgramData/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/SurfaceToolbox.py:519) - Processing completed in 0.02 seconds<br>
[INFO][Stream] 21.03.2021 09:38:07 [] (unknown:0) - Processing started<br>
[INFO][Stream] 21.03.2021 09:38:07 [] (unknown:0) - Processing completed in 0.02 seconds<br>
[DEBUG][Qt] 21.03.2021 09:38:24 [] (unknown:0) - Switch to module:  “Data”<br>
[DEBUG][Qt] 21.03.2021 09:39:18 [] (unknown:0) - Switch to module:  “CenterlineMetrics”<p></p>

---
