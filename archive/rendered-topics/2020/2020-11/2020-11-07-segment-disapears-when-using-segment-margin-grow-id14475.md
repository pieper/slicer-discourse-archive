---
topic_id: 14475
title: "Segment Disapears When Using Segment Margin Grow"
date: 2020-11-07
url: https://discourse.slicer.org/t/14475
---

# Segment disapears when using segment margin-> grow

**Topic ID**: 14475
**Date**: 2020-11-07
**URL**: https://discourse.slicer.org/t/segment-disapears-when-using-segment-margin-grow/14475

---

## Post #1 by @l.znaniecki (2020-11-07 18:47 UTC)

<p>Problem report for Slicer 4.11.20200930 win-amd64: [please describe expected and actual behavior]</p>
<p>Segment disapears when using segment margin-&gt; grow. This happens repeatedly on some segmentations of some CTs. I can’t find a pattern so far, but the problem has occured &gt; 10 times.</p>
<p>Log:<br>
[DEBUG][Qt] 07.11.2020 19:39:43 [] (unknown:0) - Session start time …: 2020-11-07 19:39:43<br>
[DEBUG][Qt] 07.11.2020 19:39:43 [] (unknown:0) - Slicer version …: 4.11.20200930 (revision 29402 / 002be18) win-amd64 - installed release<br>
[DEBUG][Qt] 07.11.2020 19:39:43 [] (unknown:0) - Operating system …: Windows /  Professional / (Build 19041, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 07.11.2020 19:39:43 [] (unknown:0) - Memory …: 32711 MB physical, 37575 MB virtual<br>
[DEBUG][Qt] 07.11.2020 19:39:43 [] (unknown:0) - CPU …: AuthenticAMD AMD Ryzen 9 3900X 12-Core Processor            , 24 cores, 24 logical processors<br>
[DEBUG][Qt] 07.11.2020 19:39:43 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 07.11.2020 19:39:43 [] (unknown:0) - Qt configuration …: version 5.15.1, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 07.11.2020 19:39:43 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 07.11.2020 19:39:43 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 07.11.2020 19:39:43 [] (unknown:0) - Application path …: C:/Users/eendo/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin<br>
[DEBUG][Qt] 07.11.2020 19:39:43 [] (unknown:0) - Additional module paths …: C:/Users/eendo/AppData/Roaming/NA-MIC/Extensions-29402/SegmentEditorExtraEffects/lib/Slicer-4.11/qt-scripted-modules, C:/Users/eendo/AppData/Roaming/NA-MIC/Extensions-29402/MarkupsToModel/lib/Slicer-4.11/qt-loadable-modules, C:/Users/eendo/AppData/Roaming/NA-MIC/Extensions-29402/SlicerVMTK/lib/Slicer-4.11/qt-loadable-modules, C:/Users/eendo/AppData/Roaming/NA-MIC/Extensions-29402/SlicerVMTK/lib/Slicer-4.11/qt-scripted-modules, C:/Users/eendo/AppData/Roaming/NA-MIC/Extensions-29402/SlicerRT/lib/Slicer-4.11/cli-modules, C:/Users/eendo/AppData/Roaming/NA-MIC/Extensions-29402/SlicerRT/lib/Slicer-4.11/qt-loadable-modules, C:/Users/eendo/AppData/Roaming/NA-MIC/Extensions-29402/SlicerRT/lib/Slicer-4.11/qt-scripted-modules, C:/Users/eendo/AppData/Roaming/NA-MIC/Extensions-29402/QuantitativeReporting/lib/Slicer-4.11/qt-scripted-modules, C:/Users/eendo/AppData/Roaming/NA-MIC/Extensions-29402/DCMQI/lib/Slicer-4.11/cli-modules, C:/Users/eendo/AppData/Roaming/NA-MIC/Extensions-29402/PETDICOMExtension/lib/Slicer-4.11/cli-modules, C:/Users/eendo/AppData/Roaming/NA-MIC/Extensions-29402/PETDICOMExtension/lib/Slicer-4.11/qt-scripted-modules, C:/Users/eendo/AppData/Roaming/NA-MIC/Extensions-29402/SlicerDevelopmentToolbox/lib/Slicer-4.11/qt-scripted-modules, C:/Users/eendo/AppData/Roaming/NA-MIC/Extensions-29402/ChangeTracker/lib/Slicer-4.11/cli-modules, C:/Users/eendo/AppData/Roaming/NA-MIC/Extensions-29402/ChangeTracker/lib/Slicer-4.11/qt-scripted-modules, C:/Users/eendo/Documents/aortaai_slicer/Aorta.AI, C:/Users/eendo/AppData/Roaming/NA-MIC/Extensions-29402/SlicerElastix/lib/Slicer-4.11/qt-scripted-modules<br>
[DEBUG][Python] 07.11.2020 19:39:47 [Python] (C:\Users\eendo\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Python\Lib\site-packages\pydicom\datadict.py:432) - Reversing DICOM dictionary so can look up tag from a keyword…<br>
[CRITICAL][Stream] 07.11.2020 19:39:46 [] (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 07.11.2020 19:39:46 [] (unknown:0) -   File “”, line 1, in <br>
[CRITICAL][Stream] 07.11.2020 19:39:46 [] (unknown:0) -   File “C:\Users\eendo\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Python\Lib\imp.py”, line 170, in load_source<br>
[CRITICAL][Stream] 07.11.2020 19:39:46 [] (unknown:0) -     module = _exec(spec, sys.modules[name])<br>
[CRITICAL][Stream] 07.11.2020 19:39:46 [] (unknown:0) -   File “”, line 618, in _exec<br>
[CRITICAL][Stream] 07.11.2020 19:39:46 [] (unknown:0) -   File “”, line 678, in exec_module<br>
[CRITICAL][Stream] 07.11.2020 19:39:46 [] (unknown:0) -   File “”, line 219, in <em>call_with_frames_removed<br>
[CRITICAL][Stream] 07.11.2020 19:39:46 [] (unknown:0) -   File “C:/Users/eendo/AppData/Roaming/NA-MIC/Extensions-29402/ChangeTracker/lib/Slicer-4.11/qt-scripted-modules/ChangeTracker.py”, line 4, in <br>
[CRITICAL][Stream] 07.11.2020 19:39:46 [] (unknown:0) -     import ChangeTrackerWizard<br>
[CRITICAL][Stream] 07.11.2020 19:39:46 [] (unknown:0) -   File "C:\Users\eendo\AppData\Roaming\NA-MIC\Extensions-29402\ChangeTracker\lib\Slicer-4.11\qt-scripted-modules\ChangeTrackerWizard_<em>init</em></em>.py", line 2, in <br>
[CRITICAL][Stream] 07.11.2020 19:39:46 [] (unknown:0) -     from ChangeTrackerStep import *<br>
[CRITICAL][Stream] 07.11.2020 19:39:46 [] (unknown:0) - ModuleNotFoundError: No module named ‘ChangeTrackerStep’<br>
[CRITICAL][Qt] 07.11.2020 19:39:46 [] (unknown:0) - loadSourceAsModule - Failed to load file “C:/Users/eendo/AppData/Roaming/NA-MIC/Extensions-29402/ChangeTracker/lib/Slicer-4.11/qt-scripted-modules/ChangeTracker.py”  as module “ChangeTracker” !<br>
[CRITICAL][Qt] 07.11.2020 19:39:46 [] (unknown:0) - Fail to instantiate module  “ChangeTracker”<br>
[CRITICAL][Qt] 07.11.2020 19:39:48 [] (unknown:0) -   Error(s):<br>
CLI executable: C:/Users/eendo/AppData/Roaming/NA-MIC/Extensions-29402/SlicerVMTK/lib/Slicer-4.11/qt-loadable-modules/vtkvmtk.py<br>
The process failed to start. Either the invoked program is missing, or you may have insufficient permissions to invoke the program.<br>
[CRITICAL][Qt] 07.11.2020 19:39:48 [] (unknown:0) - Fail to instantiate module  “vtkvmtk”<br>
[CRITICAL][Qt] 07.11.2020 19:39:48 [] (unknown:0) - The following modules failed to be instantiated:<br>
[CRITICAL][Qt] 07.11.2020 19:39:48 [] (unknown:0) -    ChangeTracker<br>
[CRITICAL][Qt] 07.11.2020 19:39:48 [] (unknown:0) -    vtkvmtk<br>
[DEBUG][Python] 07.11.2020 19:39:50 [Python] (C:\Users\eendo\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[WARNING][Qt] 07.11.2020 19:39:51 [] (unknown:0) - When loading module  “ChangeTrackerSelfTest” , the dependency “ChangeTracker” failed to be loaded.<br>
[DEBUG][Python] 07.11.2020 19:39:51 [Python] (C:\Users\eendo\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 07.11.2020 19:39:51 [Python] (C:\Users\eendo\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[INFO][Python] 07.11.2020 19:39:52 [Python] (C:/Users/eendo/Documents/aortaai_slicer/Aorta.AI/SegmentEditorNvidiaAIAA.py:32) - This plugin dir: C:/Users/eendo/Documents/aortaai_slicer/Aorta.AI<br>
[DEBUG][Python] 07.11.2020 19:39:52 [Python] (C:\Users\eendo\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Slicer-4.11\qt-scripted-modules\DICOMLib\DICOMProcesses.py:171) - Starting storescp process<br>
[DEBUG][Python] 07.11.2020 19:39:52 [Python] (C:\Users\eendo\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Slicer-4.11\qt-scripted-modules\DICOMLib\DICOMProcesses.py:68) - ('Starting C:/Users/eendo/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin/…/bin\storescp.exe with ', [‘11112’, ‘–accept-all’, ‘–output-directory’, ‘C:/slicerDB/AAA/incoming’, ‘–exec-sync’, ‘–exec-on-reception’, ‘C:/Users/eendo/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin/…/bin\dcmdump.exe --load-short --print-short --print-filename --search PatientName “C:/slicerDB/AAA/incoming/<span class="hashtag">#f</span>”’])<br>
[DEBUG][Python] 07.11.2020 19:39:52 [Python] (C:\Users\eendo\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Slicer-4.11\qt-scripted-modules\DICOMLib\DICOMProcesses.py:72) - Process C:/Users/eendo/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin/…/bin\storescp.exe now in state Starting<br>
[DEBUG][Python] 07.11.2020 19:39:52 [Python] (C:\Users\eendo\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Slicer-4.11\qt-scripted-modules\DICOMLib\DICOMProcesses.py:72) - Process C:/Users/eendo/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin/…/bin\storescp.exe now in state Running<br>
[INFO][Python] 07.11.2020 19:39:52 [Python] (C:/Users/eendo/AppData/Local/NA-MIC/Slicer 4.11.20200930/bin/…/lib/Slicer-4.11/qt-scripted-modules/DICOM.py:200) - DICOM C-Store SCP service started at port 11112<br>
[DEBUG][Qt] 07.11.2020 19:39:51 [] (unknown:0) - Switch to module:  “Welcome”<br>
[INFO][Stream] 07.11.2020 19:39:52 [] (unknown:0) - This plugin dir: C:/Users/eendo/Documents/aortaai_slicer/Aorta.AI<br>
[INFO][VTK] 07.11.2020 19:39:52 [vtkMRMLScene (000001EB5294DD30)] (D:\D\S\Slicer-0\Libs\MRML\Core\vtkMRMLScene.cxx:316) - vtkMRMLScene::Clear<br>
[INFO][VTK] 07.11.2020 19:39:52 [vtkMRMLScene (000001EB5294DD30)] (D:\D\S\Slicer-0\Libs\MRML\Core\vtkMRMLScene.cxx:762) - vtkMRMLScene::Import<br>
[INFO][VTK] 07.11.2020 19:39:52 [vtkMRMLVolumeArchetypeStorageNode (000001EB52960DC0)] (D:\D\S\Slicer-0\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:473) - Loaded volume from file: C:/Users/eendo/AppData/Roaming/NA-MIC/Extensions-29402/SlicerVMTK/lib/Slicer-4.11/qt-scripted-modules/Resources/Vesselness.png. Dimensions: 65x50x1. Number of components: 3. Pixel type: unsigned char.<br>
[INFO][VTK] 07.11.2020 19:39:52 [vtkMRMLScene (000001EB52AC0080)] (D:\D\S\Slicer-0\Libs\MRML\Core\vtkMRMLScene.cxx:316) - vtkMRMLScene::Clear<br>
[INFO][VTK] 07.11.2020 19:39:52 [vtkMRMLScene (000001EB52AC0080)] (D:\D\S\Slicer-0\Libs\MRML\Core\vtkMRMLScene.cxx:762) - vtkMRMLScene::Import<br>
[INFO][VTK] 07.11.2020 19:39:52 [vtkMRMLScene (000001EB5294DD30)] (D:\D\S\Slicer-0\Libs\MRML\Core\vtkMRMLScene.cxx:316) - vtkMRMLScene::Clear<br>
[INFO][Stream] 07.11.2020 19:39:52 [] (unknown:0) - DICOM C-Store SCP service started at port 11112<br>
[INFO][VTK] 07.11.2020 19:40:23 [vtkMRMLVolumeArchetypeStorageNode (000001EB52961770)] (D:\D\S\Slicer-0\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:473) - Loaded volume from file: X:/badania/66_TODO/66.nii.gz. Dimensions: 512x512x395. Number of components: 1. Pixel type: short.<br>
[INFO][VTK] 07.11.2020 19:40:23 [vtkMRMLScene (000001EB4C8C7030)] (D:\D\S\Slicer-0\Libs\MRML\Core\vtkMRMLScene.cxx:316) - vtkMRMLScene::Clear<br>
[DEBUG][Qt] 07.11.2020 19:40:23 [] (unknown:0) - “Volume” Reader has successfully read the file “X:/badania/66_TODO/66.nii.gz” “[1.80s]”<br>
[DEBUG][Qt] 07.11.2020 19:40:25 [] (unknown:0) - “Segmentation” Reader has successfully read the file “X:/badania/66_TODO/66_AI.seg.nrrd” “[1.52s]”<br>
[DEBUG][Qt] 07.11.2020 19:40:29 [] (unknown:0) - “Segmentation” Reader has successfully read the file “X:/badania/66_TODO/66_kontrast.seg.nrrd” “[3.61s]”<br>
[DEBUG][Qt] 07.11.2020 19:41:42 [] (unknown:0) - Switch to module:  “SegmentEditor”<br>
[WARNING][Qt] 07.11.2020 19:41:43 [] (unknown:0) - QLayout::addChildLayout: layout “” already has a parent<br>
[WARNING][Qt] 07.11.2020 19:41:43 [] (unknown:0) - ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 100 1<br>
[DEBUG][Qt] 07.11.2020 19:41:48 [] (unknown:0) - Switch to module:  “Data”<br>
[DEBUG][Qt] 07.11.2020 19:42:02 [] (unknown:0) - Switch to module:  “SegmentEditor”<br>
[WARNING][Qt] 07.11.2020 19:42:08 [] (unknown:0) - ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 100 1<br>
[ERROR][VTK] 07.11.2020 19:42:18 [vtkITKImageMargin (000001EB76A2BD90)] (D:\D\S\Slicer-0\Libs\vtkITK\vtkITKImageMargin.cxx:198) - Incompatible data type for this version of ITK.<br>
[CRITICAL][Qt] 07.11.2020 19:42:24 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLSegmentationNode )  doesn’t return data of type vtkObject.<br>
The slot ( “1onDisplayNodeModified(vtkObject*, vtkObject*)” ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 07.11.2020 19:42:24 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject <em>,class vtkObject <em>) : Invalid object type calling display node modified event<br>
[CRITICAL][Qt] 07.11.2020 19:42:32 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLSegmentationNode )  doesn’t return data of type vtkObject.<br>
The slot ( "1onDisplayNodeModified(vtkObject</em>, vtkObject</em>)" ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 07.11.2020 19:42:32 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject *,class vtkObject *) : Invalid object type calling display node modified event<br>
[ERROR][VTK] 07.11.2020 19:42:45 [vtkITKImageMargin (000001EB76A31220)] (D:\D\S\Slicer-0\Libs\vtkITK\vtkITKImageMargin.cxx:198) - Incompatible data type for this version of ITK.</p>
<p>Your help will be much appreciated.</p>
<p>Regards,<br>
Lukasz</p>

---

## Post #2 by @l.znaniecki (2020-11-07 19:32 UTC)

<p>I analysed the volume type, and it appears, that Volume type is always scalar. However, for volume type:</p>
<ul>
<li>float - segments disapper</li>
<li>short - segments grow / shrink as supposed.</li>
</ul>
<p>Can I resolve it somehow? Easily convert volume types?</p>
<p>Regard<br>
Lukasz</p>

---

## Post #3 by @lassoan (2020-11-07 20:14 UTC)

<p>Thanks for reporting this. You can change scalar type of an input volume using Cast scalar volume module.</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> can you check if you can reproduce the problem of using margin effect on float/double volumes?</p>

---

## Post #4 by @l.znaniecki (2020-11-08 09:43 UTC)

<p>Hi, thanks.</p>
<p>I have changed volume type to short. In one case it resolved the problem, in case of other two volumes the problem persists.</p>
<p>Any ideas?</p>
<p>Regards,<br>
Lukasz</p>

---

## Post #5 by @l.znaniecki (2020-11-08 09:46 UTC)

<p>[DEBUG][Qt] 08.11.2020 10:44:09 [] (unknown:0) - Switch to module:  “SegmentEditor”<br>
[WARNING][Qt] 08.11.2020 10:44:16 [] (unknown:0) - ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 100 2<br>
[WARNING][Qt] 08.11.2020 10:44:23 [] (unknown:0) - ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 100 2<br>
[ERROR][VTK] 08.11.2020 10:44:45 [vtkITKImageMargin (00000260907E8CD0)] (D:\D\S\Slicer-0\Libs\vtkITK\vtkITKImageMargin.cxx:198) - Incompatible data type for this version of ITK.</p>
<p>Do I need to change ITK version somehow?</p>

---

## Post #6 by @lassoan (2020-11-08 18:46 UTC)

<p>Until the margin effect is improved in Slicer to support float volumes directly, you need to cast the master volume to integer type (using Cast scalar volume module) before you choose it as master volume.</p>

---

## Post #7 by @l.znaniecki (2020-11-08 19:45 UTC)

<p>Thank you.</p>
<p>Still, even if cast the volume to int, the problem persists, segment disappears when I grow it.</p>
<p>[DEBUG][Qt] 08.11.2020 20:38:46 [] (unknown:0) - Switch to module:  “SegmentEditor”<br>
[ERROR][VTK] 08.11.2020 20:39:03 [vtkITKImageMargin (00000237D5628940)] (D:\D\S\Slicer-0\Libs\vtkITK\vtkITKImageMargin.cxx:198) - Incompatible data type for this version of ITK.<br>
[CRITICAL][Qt] 08.11.2020 20:39:49 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLSegmentationNode )  doesn’t return data of type vtkObject.<br>
The slot ( “1onDisplayNodeModified(vtkObject*, vtkObject*)” ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 08.11.2020 20:39:49 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject <em>,class vtkObject <em>) : Invalid object type calling display node modified event<br>
[WARNING][Qt] 08.11.2020 20:40:06 [] (unknown:0) - ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 100 1<br>
[CRITICAL][Qt] 08.11.2020 20:40:20 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLSegmentationNode )  doesn’t return data of type vtkObject.<br>
The slot ( "1onDisplayNodeModified(vtkObject</em>, vtkObject</em>)" ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 08.11.2020 20:40:20 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject <em>,class vtkObject <em>) : Invalid object type calling display node modified event<br>
[WARNING][Qt] 08.11.2020 20:40:41 [] (unknown:0) - ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 100 2<br>
[INFO][Python] 08.11.2020 20:40:55 [Python] (C:\Users\eendo\AppData\Local\NA-MIC\Slicer 4.11.20200930\lib\Slicer-4.11\qt-scripted-modules\SegmentEditorEffects\SegmentEditorIslandsEffect.py:155) - 2 islands created (3 ignored)<br>
[INFO][Stream] 08.11.2020 20:40:55 [] (unknown:0) - 2 islands created (3 ignored)<br>
[ERROR][VTK] 08.11.2020 20:41:55 [vtkITKImageMargin (000002382F85B120)] (D:\D\S\Slicer-0\Libs\vtkITK\vtkITKImageMargin.cxx:198) - Incompatible data type for this version of ITK.<br>
[CRITICAL][Qt] 08.11.2020 20:42:11 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLSegmentationNode )  doesn’t return data of type vtkObject.<br>
The slot ( "1onDisplayNodeModified(vtkObject</em>, vtkObject</em>)" ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 08.11.2020 20:42:11 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject <em>,class vtkObject <em>) : Invalid object type calling display node modified event<br>
[ERROR][VTK] 08.11.2020 20:42:16 [vtkITKImageMargin (0000023831270480)] (D:\D\S\Slicer-0\Libs\vtkITK\vtkITKImageMargin.cxx:198) - Incompatible data type for this version of ITK.<br>
[CRITICAL][Qt] 08.11.2020 20:42:19 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLSegmentationNode )  doesn’t return data of type vtkObject.<br>
The slot ( "1onDisplayNodeModified(vtkObject</em>, vtkObject</em>)" ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 08.11.2020 20:42:19 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject *,class vtkObject *) : Invalid object type calling display node modified event<br>
[DEBUG][Qt] 08.11.2020 20:42:23 [] (unknown:0) - Switch to module:  “Volumes”</p>
<p>Any further suggestions?</p>
<p>regards,<br>
Lukasz</p>

---

## Post #8 by @lassoan (2020-11-08 20:32 UTC)

<p>“Short” data type should work. If you have any scene where you casted the master volume to “short” and margin effect does not work then share the scene with us (upload to dropbox/onedrive/gdrive/… and post the link) and we’ll investigate.</p>

---

## Post #9 by @l.znaniecki (2020-11-08 20:53 UTC)

<p>Still no succes. I will send you a link to the dataset.</p>
<p>Regards, and thank you for your help again!</p>
<p>Lukasz</p>
<p>Message:<br>
DEBUG][Qt] 08.11.2020 21:47:06 [] (unknown:0) - Switch to module:  “Volumes”<br>
[WARNING][Qt] 08.11.2020 21:47:10 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  D:\D\S\Slicer-0-build\CTK\Libs\Widgets\ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 08.11.2020 21:47:10 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  D:\D\S\Slicer-0-build\CTK\Libs\Widgets\ctkMatrixWidget.cpp  line  253<br>
[WARNING][Qt] 08.11.2020 21:47:10 [] (unknown:0) - Assertion <code>this-&gt;Table-&gt;rowHeight(i) == newHeight</code> failed in  D:\D\S\Slicer-0-build\CTK\Libs\Widgets\ctkMatrixWidget.cpp  line  253<br>
[DEBUG][Qt] 08.11.2020 21:47:14 [] (unknown:0) - Switch to module:  “Data”<br>
[DEBUG][Qt] 08.11.2020 21:47:23 [] (unknown:0) - Switch to module:  “SegmentEditor”<br>
[WARNING][Qt] 08.11.2020 21:47:23 [] (unknown:0) - ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 100 2<br>
[DEBUG][Qt] 08.11.2020 21:47:37 [] (unknown:0) - Switch to module:  “Volumes”<br>
[DEBUG][Qt] 08.11.2020 21:47:41 [] (unknown:0) - Switch to module:  “SegmentEditor”<br>
[ERROR][VTK] 08.11.2020 21:47:47 [vtkITKImageMargin (00000237CEE01260)] (D:\D\S\Slicer-0\Libs\vtkITK\vtkITKImageMargin.cxx:198) - Incompatible data type for this version of ITK.<br>
[CRITICAL][Qt] 08.11.2020 21:47:54 [] (unknown:0) - The VTKEvent( 17000 ) triggered by vtkObject( vtkMRMLSegmentationNode )  doesn’t return data of type vtkObject.<br>
The slot ( “1onDisplayNodeModified(vtkObject*, vtkObject*)” ) owned by  QObject( “” )  may be incorrect.<br>
[CRITICAL][Qt] 08.11.2020 21:47:54 [] (unknown:0) - void __cdecl qSlicerSubjectHierarchyPluginLogic::onDisplayNodeModified(class vtkObject *,class vtkObject *) : Invalid object type calling display node modified event<br>
[WARNING][Qt] 08.11.2020 21:49:44 [] (unknown:0) - ctkSliderWidget::setSingleStep() 0 is out of bounds. 0 100 2<br>
[WARNING][Qt] 08.11.2020 21:50:24 [] (unknown:0) - QGestureManager::deliverEvent: could not find the target for gesture<br>
[ERROR][VTK] 08.11.2020 21:50:32 [vtkITKImageMargin (00000237CF29CC20)] (D:\D\S\Slicer-0\Libs\vtkITK\vtkITKImageMargin.cxx:198) - Incompatible data type for this version of ITK.</p>

---
