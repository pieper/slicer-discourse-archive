# Volume rendering does not work after reloading scene

**Topic ID**: 20136
**Date**: 2021-10-13
**URL**: https://discourse.slicer.org/t/volume-rendering-does-not-work-after-reloading-scene/20136

---

## Post #1 by @stephan13 (2021-10-13 17:32 UTC)

<p>Problem report for Slicer 4.11.20210226 win-amd64:</p>
<p>Hi there</p>
<p>I cropped a volume and saved everything into a scene. After reloading the scene, I can<br>
only see the 3D rendering of the cropped volume. The rendered original volume does not appear, even though the volume is set to visible. Also I noted that the crop bar is deactivated in the Volume Rendering module for the original volume only (usually this is activated for other volumes). Slice views are normally visible though.</p>
<p>Any suggestions? Thanks.</p>
<p>Logs do not provide much, unfortunately:</p>
<p>[DEBUG][Qt] 13.10.2021 19:28:09 [] (unknown:0) - Session start time …: 2021-10-13 19:28:09<br>
[DEBUG][Qt] 13.10.2021 19:28:09 [] (unknown:0) - Slicer version …: 4.11.20210226 (revision 29738 / 7a593c8) win-amd64 - installed release<br>
[DEBUG][Qt] 13.10.2021 19:28:09 [] (unknown:0) - Operating system …: Windows /  Professional / (Build 19042, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 13.10.2021 19:28:09 [] (unknown:0) - Memory …: 32081 MB physical, 36945 MB virtual<br>
[DEBUG][Qt] 13.10.2021 19:28:09 [] (unknown:0) - CPU …: AuthenticAMD AMD Ryzen 7 PRO 4750U with Radeon Graphics, 16 cores, 16 logical processors<br>
[DEBUG][Qt] 13.10.2021 19:28:09 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 13.10.2021 19:28:09 [] (unknown:0) - Qt configuration …: version 5.15.1, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 13.10.2021 19:28:09 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 13.10.2021 19:28:09 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 13.10.2021 19:28:09 [] (unknown:0) - Application path …: C:/ProgramData/NA-MIC/Slicer 4.11.20210226/bin<br>
[DEBUG][Qt] 13.10.2021 19:28:09 [] (unknown:0) - Additional module paths …: NA-MIC/Extensions-29738/SlicerJupyter/lib/Slicer-4.11/qt-loadable-modules, NA-MIC/Extensions-29738/SlicerJupyter/lib/Slicer-4.11/qt-scripted-modules, NA-MIC/Extensions-29738/SlicerElastix/lib/Slicer-4.11/qt-scripted-modules, NA-MIC/Extensions-29738/SlicerCochlea/lib/Slicer-4.11/qt-scripted-modules, NA-MIC/Extensions-29738/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules<br>
[WARNING][Python] 13.10.2021 19:28:11 [Python] (C:\ProgramData\NA-MIC\Slicer 4.11.20210226\bin\Python\slicer\util.py:2160) - toVTKString is deprecated! Conversion is no longer necessary.<br>
[DEBUG][Python] 13.10.2021 19:28:11 [Python] (C:\ProgramData\NA-MIC\Slicer 4.11.20210226\lib\Python\Lib\site-packages\pydicom\datadict.py:432) - Reversing DICOM dictionary so can look up tag from a keyword…<br>
[CRITICAL][Stream] 13.10.2021 19:28:11 [] (unknown:0) - toVTKString is deprecated! Conversion is no longer necessary.<br>
[DEBUG][Python] 13.10.2021 19:28:13 [Python] (C:\ProgramData\NA-MIC\Slicer 4.11.20210226\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 13.10.2021 19:28:14 [Python] (C:\ProgramData\NA-MIC\Slicer 4.11.20210226\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 13.10.2021 19:28:14 [Python] (C:\ProgramData\NA-MIC\Slicer 4.11.20210226\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[INFO][Python] 13.10.2021 19:28:15 [Python] (C:/ProgramData/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules/SegmentEditorNvidiaAIAA.py:32) - This plugin dir: C:/ProgramData/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules<br>
[DEBUG][Qt] 13.10.2021 19:28:14 [] (unknown:0) - Switch to module:  “Welcome”<br>
[INFO][Stream] 13.10.2021 19:28:15 [] (unknown:0) - This plugin dir: C:/ProgramData/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/NvidiaAIAssistedAnnotation/lib/Slicer-4.11/qt-scripted-modules<br>
[INFO][VTK] 13.10.2021 19:28:16 [vtkMRMLVolumeArchetypeStorageNode (000002C3807AB620)] (D:\D\S\Slicer-1\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:509) - Loaded volume from file: C:/Users/steph/AppData/Local/NA-MIC/Slicer/cache/SlicerIO/__BundleLoadTemp-2021-10-13_192815_714/I38-Scene-2021-10-11/Data/ITIDE_I38_preop.nrrd. Dimensions: 512x512x759. Number of components: 1. Pixel type: short.<br>
[INFO][VTK] 13.10.2021 19:28:17 [vtkMRMLVolumeArchetypeStorageNode (000002C3807AAC70)] (D:\D\S\Slicer-1\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:509) - Loaded volume from file: C:/Users/steph/AppData/Local/NA-MIC/Slicer/cache/SlicerIO/__BundleLoadTemp-2021-10-13_192815_714/I38-Scene-2021-10-11/Data/ITIDE_I38_postop.nrrd. Dimensions: 512x512x271. Number of components: 1. Pixel type: short.<br>
[INFO][VTK] 13.10.2021 19:28:17 [vtkMRMLVolumeArchetypeStorageNode (000002C3807AAE60)] (D:\D\S\Slicer-1\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:509) - Loaded volume from file: C:/Users/steph/AppData/Local/NA-MIC/Slicer/cache/SlicerIO/__BundleLoadTemp-2021-10-13_192815_714/I38-Scene-2021-10-11/Data/CroppedPostop.nrrd. Dimensions: 442x318x251. Number of components: 1. Pixel type: short.<br>
[INFO][VTK] 13.10.2021 19:28:17 [vtkMRMLVolumeArchetypeStorageNode (000002C3807AB810)] (D:\D\S\Slicer-1\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:509) - Loaded volume from file: C:/Users/steph/AppData/Local/NA-MIC/Slicer/cache/SlicerIO/__BundleLoadTemp-2021-10-13_192815_714/I38-Scene-2021-10-11/Data/CroppedPreop.nrrd. Dimensions: 374x310x503. Number of components: 1. Pixel type: short.<br>
[INFO][VTK] 13.10.2021 19:28:18 [vtkMRMLVolumeArchetypeStorageNode (000002C3807AB050)] (D:\D\S\Slicer-1\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:509) - Loaded volume from file: C:/Users/steph/AppData/Local/NA-MIC/Slicer/cache/SlicerIO/__BundleLoadTemp-2021-10-13_192815_714/I38-Scene-2021-10-11/Data/RegistrationPostop.nrrd. Dimensions: 374x310x503. Number of components: 1. Pixel type: short.<br>
[INFO][VTK] 13.10.2021 19:28:18 [vtkMRMLVolumeArchetypeStorageNode (000002C3807A9CF0)] (D:\D\S\Slicer-1\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:509) - Loaded volume from file: C:/Users/steph/AppData/Local/NA-MIC/Slicer/cache/SlicerIO/__BundleLoadTemp-2021-10-13_192815_714/I38-Scene-2021-10-11/Data/BoardPreopPost.nrrd. Dimensions: 374x310x503. Number of components: 1. Pixel type: short.<br>
[DEBUG][Qt] 13.10.2021 19:28:19 [] (unknown:0) - “MRB Slicer Data Bundle” Reader has successfully read the file “C:/project/ITIDE/03-Processing/CT/I38/I38-Scene-2021-10-11.mrb” “[4.06s]”<br>
[INFO][Stream] 13.10.2021 19:28:19 [] (unknown:0) - Loading Slicer RC file [C:/Users/steph/.slicerrc.py]<br>
[DEBUG][Qt] 13.10.2021 19:28:20 [] (unknown:0) - Switch to module:  “Data”<br>
[DEBUG][Qt] 13.10.2021 19:28:22 [] (unknown:0) - Switch to module:  “VolumeRendering”<br>
[DEBUG][Qt] 13.10.2021 19:28:49 [] (unknown:0) - Switch to module:  “Data”<br>
[DEBUG][Qt] 13.10.2021 19:29:00 [] (unknown:0) - Switch to module:  “VolumeRendering”</p>

---

## Post #2 by @lassoan (2021-10-13 18:31 UTC)

<p>This issue was fixed some time ago in the Slicer Preview Release.</p>

---
