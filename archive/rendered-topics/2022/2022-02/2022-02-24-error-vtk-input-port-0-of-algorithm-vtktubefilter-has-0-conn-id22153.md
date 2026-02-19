---
topic_id: 22153
title: "Error Vtk Input Port 0 Of Algorithm Vtktubefilter Has 0 Conn"
date: 2022-02-24
url: https://discourse.slicer.org/t/22153
---

# Error VTK Input port 0 of algorithm vtkTubeFilter has 0 connections but is not optional

**Topic ID**: 22153
**Date**: 2022-02-24
**URL**: https://discourse.slicer.org/t/error-vtk-input-port-0-of-algorithm-vtktubefilter-has-0-connections-but-is-not-optional/22153

---

## Post #1 by @steffen-o (2022-02-24 10:00 UTC)

<p>Hi,</p>
<p>Slicer version: 4.13.0</p>
<p>I’m using 3D Slicer for segmentation and landmarking of micro CT data for quite a while now and I like it very much!<br>
The new Markup functionality (Landmark templates,skipping Landmarks, editing misplaced landmarks, …) in v4.13 is helping me a lot. I use some Python code snippets to create markup planes and set views.<br>
But i am getting a lot of errors in the log.</p>
<blockquote>
<p>Input port 0 of algorithm vtkTubeFilter(000002A9C3419DF0) has 0 connections but is not optional.</p>
</blockquote>
<p>The error doesn’t seem to do much (except flooding the error log).<br>
Has anybody encountered this error before? What did I do wrong?</p>
<p>I hope you can help me, thank you in advance!</p>
<p>Here is my Log:</p>
<blockquote>
<p>[DEBUG][Qt] 24.02.2022 09:46:31 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: 2022-02-24 09:46:31<br>
[DEBUG][Qt] 24.02.2022 09:46:31 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 4.13.0-2022-02-23 (revision 30641 / 7da0024) win-amd64 - installed release<br>
[DEBUG][Qt] 24.02.2022 09:46:31 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Operating system …: Windows /  Professional / (Build 17763, Code Page 1252) - 64-bit<br>
[DEBUG][Qt] 24.02.2022 09:46:31 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Memory …: 130982 MB physical, 150438 MB virtual<br>
[DEBUG][Qt] 24.02.2022 09:46:31 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CPU …: GenuineIntel , 12 cores, 12 logical processors<br>
[DEBUG][Qt] 24.02.2022 09:46:31 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 24.02.2022 09:46:31 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Qt configuration …: version 5.15.2, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 24.02.2022 09:46:31 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Internationalization …: disabled, language=<br>
[DEBUG][Qt] 24.02.2022 09:46:31 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Developer mode …: enabled<br>
[DEBUG][Qt] 24.02.2022 09:46:31 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Application path …: C:/ProgramData/NA-MIC/Slicer 4.13.0-2022-02-23/bin<br>
[DEBUG][Qt] 24.02.2022 09:46:31 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths …: (none)<br>
[DEBUG][Python] 24.02.2022 09:46:36 [Python] (C:\ProgramData\NA-MIC\Slicer 4.13.0-2022-02-23\lib\Slicer-4.13\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 24.02.2022 09:46:37 [Python] (C:\ProgramData\NA-MIC\Slicer 4.13.0-2022-02-23\lib\Slicer-4.13\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 24.02.2022 09:46:37 [Python] (C:\ProgramData\NA-MIC\Slicer 4.13.0-2022-02-23\lib\Slicer-4.13\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 24.02.2022 09:46:37 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Welcome”<br>
[INFO][Stream] 24.02.2022 09:46:38 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Loading Slicer RC file [C:/Users/User1/.slicerrc.py]<br>
[INFO][VTK] 24.02.2022 09:47:14 [vtkMRMLVolumeArchetypeStorageNode (000002A7B62A1E70)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:513) - Loaded volume from file: G:/student/Prep1/Prep1_8bit_3px3dmed.nrrd. Dimensions: 2048x2048x1484. Number of components: 1. Pixel type: unsigned char.<br>
[INFO][VTK] 24.02.2022 09:47:17 [vtkMRMLVolumeArchetypeStorageNode (000002A7B62A1A70)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:513) - Loaded volume from file: G:/student/Prep1/Prep1_8bit_3px3dmed cropped.nrrd. Dimensions: 785x869x670. Number of components: 1. Pixel type: unsigned char.<br>
[INFO][VTK] 24.02.2022 09:47:28 [vtkMRMLVolumeArchetypeStorageNode (000002A7B62A0670)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:513) - Loaded volume from file: G:/student/Prep1/Prep1_8bit_3px3dmed_bin2.nrrd. Dimensions: 1024x1024x742. Number of components: 1. Pixel type: unsigned char.<br>
[INFO][VTK] 24.02.2022 09:47:51 [vtkMRMLVolumeArchetypeStorageNode (000002A7B62A0870)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:513) - Loaded volume from file: G:/student/Prep1/Cropped volume_ss2.nrrd. Dimensions: 1573x1740x1342. Number of components: 1. Pixel type: unsigned char.<br>
[ERROR][VTK] 24.02.2022 09:48:07 [vtkMRMLMarkupsDisplayableManagerHelper (000002A7B6D22710)] (D:\D\P\Slicer-0\Modules\Loadable\Markups\MRMLDM\vtkMRMLMarkupsDisplayableManagerHelper.cxx:297) - vtkMRMLMarkupsDisplayableManager2D: Failed to create widget<br>
[ERROR][VTK] 24.02.2022 09:48:07 [vtkMRMLMarkupsDisplayableManagerHelper (000002A7B6D22710)] (D:\D\P\Slicer-0\Modules\Loadable\Markups\MRMLDM\vtkMRMLMarkupsDisplayableManagerHelper.cxx:297) - vtkMRMLMarkupsDisplayableManager2D: Failed to create widget<br>
[ERROR][VTK] 24.02.2022 09:48:07 [vtkMRMLMarkupsDisplayableManagerHelper (000002A7B6D21D10)] (D:\D\P\Slicer-0\Modules\Loadable\Markups\MRMLDM\vtkMRMLMarkupsDisplayableManagerHelper.cxx:297) - vtkMRMLMarkupsDisplayableManager2D: Failed to create widget<br>
[ERROR][VTK] 24.02.2022 09:48:07 [vtkMRMLMarkupsDisplayableManagerHelper (000002A7B6D21D10)] (D:\D\P\Slicer-0\Modules\Loadable\Markups\MRMLDM\vtkMRMLMarkupsDisplayableManagerHelper.cxx:297) - vtkMRMLMarkupsDisplayableManager2D: Failed to create widget<br>
[ERROR][VTK] 24.02.2022 09:48:07 [vtkMRMLMarkupsDisplayableManagerHelper (000002A7B6D52550)] (D:\D\P\Slicer-0\Modules\Loadable\Markups\MRMLDM\vtkMRMLMarkupsDisplayableManagerHelper.cxx:297) - vtkMRMLMarkupsDisplayableManager2D: Failed to create widget<br>
[ERROR][VTK] 24.02.2022 09:48:07 [vtkMRMLMarkupsDisplayableManagerHelper (000002A7B6D52550)] (D:\D\P\Slicer-0\Modules\Loadable\Markups\MRMLDM\vtkMRMLMarkupsDisplayableManagerHelper.cxx:297) - vtkMRMLMarkupsDisplayableManager2D: Failed to create widget<br>
[ERROR][VTK] 24.02.2022 09:48:07 [vtkMRMLMarkupsDisplayableManagerHelper (000002A7B6D12B30)] (D:\D\P\Slicer-0\Modules\Loadable\Markups\MRMLDM\vtkMRMLMarkupsDisplayableManagerHelper.cxx:297) - vtkMRMLMarkupsDisplayableManager2D: Failed to create widget<br>
[ERROR][VTK] 24.02.2022 09:48:07 [vtkMRMLMarkupsDisplayableManagerHelper (000002A7B6D12B30)] (D:\D\P\Slicer-0\Modules\Loadable\Markups\MRMLDM\vtkMRMLMarkupsDisplayableManagerHelper.cxx:297) - vtkMRMLMarkupsDisplayableManager2D: Failed to create widget<br>
[ERROR][VTK] 24.02.2022 09:48:07 [vtkMRMLMarkupsDisplayableManagerHelper (000002A7B6D22710)] (D:\D\P\Slicer-0\Modules\Loadable\Markups\MRMLDM\vtkMRMLMarkupsDisplayableManagerHelper.cxx:297) - vtkMRMLMarkupsDisplayableManager2D: Failed to create widget<br>
[ERROR][VTK] 24.02.2022 09:48:07 [vtkMRMLMarkupsDisplayableManagerHelper (000002A7B6D22710)] (D:\D\P\Slicer-0\Modules\Loadable\Markups\MRMLDM\vtkMRMLMarkupsDisplayableManagerHelper.cxx:297) - vtkMRMLMarkupsDisplayableManager2D: Failed to create widget<br>
[ERROR][VTK] 24.02.2022 09:48:07 [vtkMRMLMarkupsDisplayableManagerHelper (000002A7B6D21D10)] (D:\D\P\Slicer-0\Modules\Loadable\Markups\MRMLDM\vtkMRMLMarkupsDisplayableManagerHelper.cxx:297) - vtkMRMLMarkupsDisplayableManager2D: Failed to create widget<br>
[ERROR][VTK] 24.02.2022 09:48:07 [vtkMRMLMarkupsDisplayableManagerHelper (000002A7B6D21D10)] (D:\D\P\Slicer-0\Modules\Loadable\Markups\MRMLDM\vtkMRMLMarkupsDisplayableManagerHelper.cxx:297) - vtkMRMLMarkupsDisplayableManager2D: Failed to create widget<br>
[ERROR][VTK] 24.02.2022 09:48:07 [vtkMRMLMarkupsDisplayableManagerHelper (000002A7B6D52550)] (D:\D\P\Slicer-0\Modules\Loadable\Markups\MRMLDM\vtkMRMLMarkupsDisplayableManagerHelper.cxx:297) - vtkMRMLMarkupsDisplayableManager2D: Failed to create widget<br>
[ERROR][VTK] 24.02.2022 09:48:07 [vtkMRMLMarkupsDisplayableManagerHelper (000002A7B6D52550)] (D:\D\P\Slicer-0\Modules\Loadable\Markups\MRMLDM\vtkMRMLMarkupsDisplayableManagerHelper.cxx:297) - vtkMRMLMarkupsDisplayableManager2D: Failed to create widget<br>
[ERROR][VTK] 24.02.2022 09:48:07 [vtkMRMLMarkupsDisplayableManagerHelper (000002A7B6D12B30)] (D:\D\P\Slicer-0\Modules\Loadable\Markups\MRMLDM\vtkMRMLMarkupsDisplayableManagerHelper.cxx:297) - vtkMRMLMarkupsDisplayableManager2D: Failed to create widget<br>
[ERROR][VTK] 24.02.2022 09:48:07 [vtkMRMLMarkupsDisplayableManagerHelper (000002A7B6D12B30)] (D:\D\P\Slicer-0\Modules\Loadable\Markups\MRMLDM\vtkMRMLMarkupsDisplayableManagerHelper.cxx:297) - vtkMRMLMarkupsDisplayableManager2D: Failed to create widget<br>
[DEBUG][Qt] 24.02.2022 09:48:07 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “MRML Scene” Reader has successfully read the file “G:/student/Prep1/2019-11-05-Scene.mrml” “[57.97s]”<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F11FF0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F134F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F1AEF0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F1BBF0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F261F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F24BF0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C3418AF0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C3419DF0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C34353F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C34352F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F0B5F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F047F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F377F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F36BF0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C342D9F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C342D7F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F2F5F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F2C2F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C343B4F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C343B2F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F11FF0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F134F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F1AEF0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F1BBF0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F261F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F24BF0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C3418AF0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C3419DF0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C34353F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C34352F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F0B5F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F047F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F377F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F36BF0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C342D9F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C342D7F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F2F5F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F2C2F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C343B4F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C343B2F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F11FF0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F134F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F1AEF0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F1BBF0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F261F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F24BF0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C3418AF0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C3419DF0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C34353F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C34352F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F0B5F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F047F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F377F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F36BF0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C342D9F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C342D7F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F2F5F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F2C2F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C343B4F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C343B2F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F11FF0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F134F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F1AEF0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F1BBF0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F261F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F24BF0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C3418AF0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C3419DF0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C34353F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C34352F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F0B5F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F047F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F377F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F36BF0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C342D9F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C342D7F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F2F5F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F2C2F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C343B4F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C343B2F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F11FF0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F134F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F1AEF0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F1BBF0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F261F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F24BF0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C3418AF0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C3419DF0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C34353F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C34352F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F0B5F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F047F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F377F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F36BF0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C342D9F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C342D7F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F2F5F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F2C2F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C343B4F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C343B2F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F11FF0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F134F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F1AEF0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F1BBF0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F261F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F24BF0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C3418AF0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C3419DF0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C34353F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C34352F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F0B5F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F047F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F377F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F36BF0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C342D9F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C342D7F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F2F5F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F2C2F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C343B4F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C343B2F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F11FF0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F134F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F1AEF0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F1BBF0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F261F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F24BF0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C3418AF0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C3419DF0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C34353F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C34352F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F0B5F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F047F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F377F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F36BF0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C342D9F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C342D7F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F2F5F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F2C2F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C343B4F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C343B2F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F11FF0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F134F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F1AEF0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F1BBF0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F261F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F24BF0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C3418AF0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C3419DF0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C34353F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C34352F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F0B5F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F047F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F377F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F36BF0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C342D9F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C342D7F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C1F2F5F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C1F2C2F0) has 0 connections but is not optional.<br>
[ERROR][VTK] 24.02.2022 09:48:09 [vtkCompositeDataPipeline (000002A9C343B4F0)] (D:\D\P\Slicer-0-build\VTK\Common\ExecutionModel\vtkDemandDrivenPipeline.cxx:668) - Input port 0 of algorithm vtkTubeFilter(000002A9C343B2F0) has 0 connections but is not optional.</p>
</blockquote>

---

## Post #2 by @ebrahim (2022-02-24 12:04 UTC)

<p>I wonder if it’s connected to this: <a href="https://github.com/Slicer/Slicer/issues/6098" class="inline-onebox" rel="noopener nofollow ugc">Adding volume by class name produces warnings · Issue #6098 · Slicer/Slicer · GitHub</a></p>

---

## Post #3 by @steffen-o (2022-03-02 09:33 UTC)

<p>The strange part of this error is: it only appears after reloading the saved scene.<br>
I could narrow the error down to this part of my Python code:</p>
<pre><code class="lang-auto">segmentationNodes= list(slicer.mrmlScene.GetNodesByClass("vtkMRMLSegmentationNode"))

# segmentationNode = getNode("Segmentation")
for segNode in segmentationNodes:
  shNode = slicer.mrmlScene.GetSubjectHierarchyNode()
  exportFolderItemId = shNode.CreateFolderItem(shNode.GetSceneItemID(), segNode.GetName()+"_models")
  slicer.modules.segmentations.logic().ExportAllSegmentsToModels(segNode, exportFolderItemId)

</code></pre>
<p>This part should make models of all the segmentations and put them in a folder for easier handling of the visibility.<br>
If i only have one Segmentation there is no error…</p>
<p>I hope someone could help me to correct this code snippet</p>

---

## Post #4 by @steffen-o (2022-03-02 10:22 UTC)

<p>I think i found my mistake <img src="https://emoji.discourse-cdn.com/twitter/man_facepalming.png?v=12" title=":man_facepalming:" class="emoji" alt=":man_facepalming:" loading="lazy" width="20" height="20"></p>
<p>I forgot to include these two lines (<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-model-nodes-from-segmentation-node" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a>):</p>
<pre><code class="lang-auto">segmentModels = vtk.vtkCollection()
shNode.GetDataNodesInBranch(exportFolderItemId, segmentModels)
</code></pre>

---
