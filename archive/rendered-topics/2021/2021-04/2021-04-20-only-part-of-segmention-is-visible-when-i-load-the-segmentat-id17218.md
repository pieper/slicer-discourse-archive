---
topic_id: 17218
title: "Only Part Of Segmention Is Visible When I Load The Segmentat"
date: 2021-04-20
url: https://discourse.slicer.org/t/17218
---

# Only part of segmention is visible when I load the segmentation first time

**Topic ID**: 17218
**Date**: 2021-04-20
**URL**: https://discourse.slicer.org/t/only-part-of-segmention-is-visible-when-i-load-the-segmentation-first-time/17218

---

## Post #1 by @Ge_Tang (2021-04-20 20:53 UTC)

<p>Operating system:Windows 10<br>
Slicer version:4.11<br>
Expected behavior: All the segmentation should be visible</p>
<p>Hi, all,</p>
<p>I changed my script to have some logging information during looping over all the subjects. After this change, each time when I using loadsegmentation, the segmentations are not visible. I need to select each of them manually. I do not know what happens.</p>
<p>I also check the slicer.ini and the log files. Could you help me with this?</p>
<blockquote>
<p>[DEBUG][Qt] 20.04.2021 22:41:40 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: 2021-04-20 22:41:40<br>
[DEBUG][Qt] 20.04.2021 22:41:40 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 4.11.20210226 (revision 29738 / 7a593c8) win-amd64 - installed release<br>
[DEBUG][Qt] 20.04.2021 22:41:40 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Operating system …: Windows /  Professional / (Build 19042, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 20.04.2021 22:41:40 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Memory …: 130939 MB physical, 217805 MB virtual<br>
[DEBUG][Qt] 20.04.2021 22:41:40 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CPU …: GenuineIntel , 24 cores, 24 logical processors<br>
[DEBUG][Qt] 20.04.2021 22:41:40 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 20.04.2021 22:41:40 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Qt configuration …: version 5.15.1, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 20.04.2021 22:41:40 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 20.04.2021 22:41:40 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 20.04.2021 22:41:40 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Application path …: D:/GeTang/Slicer 4.11.20210226/bin<br>
[DEBUG][Qt] 20.04.2021 22:41:40 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths …: NA-MIC/Extensions-29738/SlicerVMTK/lib/Slicer-4.11/qt-loadable-modules, NA-MIC/Extensions-29738/SlicerVMTK/lib/Slicer-4.11/qt-scripted-modules<br>
[DEBUG][Python] 20.04.2021 22:41:42 [Python] (D:\GeTang\Slicer 4.11.20210226\lib\Python\Lib\site-packages\pydicom\datadict.py:432) - Reversing DICOM dictionary so can look up tag from a keyword…<br>
[CRITICAL][Qt] 20.04.2021 22:41:42 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Error(s):<br>
CLI executable: D:/GeTang/Slicer 4.11.20210226/NA-MIC/Extensions-29738/SlicerVMTK/lib/Slicer-4.11/qt-loadable-modules/vtkvmtk.py<br>
The process failed to start. Either the invoked program is missing, or you may have insufficient permissions to invoke the program.<br>
[CRITICAL][Qt] 20.04.2021 22:41:42 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Fail to instantiate module  “vtkvmtk”<br>
[CRITICAL][Qt] 20.04.2021 22:41:42 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - The following modules failed to be instantiated:<br>
[CRITICAL][Qt] 20.04.2021 22:41:42 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -    vtkvmtk<br>
[DEBUG][Python] 20.04.2021 22:41:42 [Python] (D:\GeTang\Slicer 4.11.20210226\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 20.04.2021 22:41:43 [Python] (D:\GeTang\Slicer 4.11.20210226\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 20.04.2021 22:41:43 [Python] (D:\GeTang\Slicer 4.11.20210226\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 20.04.2021 22:41:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Welcome”<br>
[INFO][VTK] 20.04.2021 22:41:43 [vtkMRMLVolumeArchetypeStorageNode (00000230BE9D09A0)] (D:\D\S\Slicer-1\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:509) - Loaded volume from file: D:/GeTang/Slicer 4.11.20210226/NA-MIC/Extensions-29738/SlicerVMTK/lib/Slicer-4.11/qt-scripted-modules/Resources/Vesselness.png. Dimensions: 65x50x1. Number of components: 3. Pixel type: unsigned char.<br>
[INFO][Stream] 20.04.2021 22:41:44 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Loading Slicer RC file [C:/Users/Ge Tang/.slicerrc.py]<br>
[DEBUG][Qt] 20.04.2021 22:42:07 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Python console user input: loadNodeFromFile(‘D:/GeTang/SANS/Segmented_data/Seg_Cosmo02mm.seg.nrrd’, ‘SegmentationFile’, {}, returnNode=False)<br>
[ERROR][VTK] 20.04.2021 22:42:14 [vtkSegmentationConverter (00000230BE389920)] (D:\D\S\Slicer-1\Libs\vtkSegmentationCore\vtkSegmentationConverter.cxx:267) - SetConversionParameter: Conversion parameter ‘Default slice thickness’ not found in converter rules!<br>
[ERROR][VTK] 20.04.2021 22:42:14 [vtkSegmentationConverter (00000230BE389920)] (D:\D\S\Slicer-1\Libs\vtkSegmentationCore\vtkSegmentationConverter.cxx:267) - SetConversionParameter: Conversion parameter ‘End capping’ not found in converter rules!<br>
[DEBUG][Qt] 20.04.2021 22:42:15 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “Segmentation” Reader has successfully read the file “D:/GeTang/SANS/Segmented_data/Seg_Cosmo02mm.seg.nrrd” “[8.77s]”<br>
[INFO][Stream] 20.04.2021 22:42:16 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - (MRMLCorePython.vtkMRMLSegmentationNode)00000230C3023648</p>
</blockquote>

---

## Post #2 by @Ge_Tang (2021-04-21 10:36 UTC)

<p>Is it the problem with vtk configuration? where could I find this configuration and how could I change it? thank you! <img src="https://emoji.discourse-cdn.com/twitter/slightly_smiling_face.png?v=9" title=":slightly_smiling_face:" class="emoji" alt=":slightly_smiling_face:"></p>

---
