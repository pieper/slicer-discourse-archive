---
topic_id: 2611
title: "Problem With Saving"
date: 2018-04-17
url: https://discourse.slicer.org/t/2611
---

# Problem with saving

**Topic ID**: 2611
**Date**: 2018-04-17
**URL**: https://discourse.slicer.org/t/problem-with-saving/2611

---

## Post #1 by @rakusb (2018-04-17 16:23 UTC)

<p>Hi,<br>
I have problem with saving anything in Slicer 4.8.0. What i do wrong?</p>
<p>Here you have screen</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8c4b4ce50fb0d50ca66660a3bb0b87ab1081a0b.png" data-download-href="/uploads/short-url/uVCzDM4C99DXW1zS9LrRGMA9pI7.png?dl=1" title="Przechwytywanie" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8c4b4ce50fb0d50ca66660a3bb0b87ab1081a0b.png" alt="Przechwytywanie" data-base62-sha1="uVCzDM4C99DXW1zS9LrRGMA9pI7" width="690" height="270" data-dominant-color="EEE3E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Przechwytywanie</span><span class="informations">798×313 27 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2018-04-17 18:52 UTC)

<p>Looks like you are saving into the application directory so you may not have permission.  What if you change the directory to somewhere else?</p>

---

## Post #3 by @rakusb (2018-04-17 19:03 UTC)

<p>Same thing …  I tried almost everything, older versions too.</p>

---

## Post #4 by @pieper (2018-04-17 19:50 UTC)

<p>Need to check the error log then: <a href="https://www.slicer.org/wiki/Documentation/4.8/SlicerApplication/ErrorLog">https://www.slicer.org/wiki/Documentation/4.8/SlicerApplication/ErrorLog</a></p>

---

## Post #5 by @cpinter (2018-04-17 20:21 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> I just updated this page so that it points to the very useful ‘Report a bug’ window where the clipboard can be copied by a single button press.</p>
<p><a class="mention" href="/u/rakusb">@rakusb</a> Accessible from Help -&gt; Report a bug</p>

---

## Post #6 by @rakusb (2018-04-17 21:47 UTC)

<p>[DEBUG][Qt] 17.04.2018 23:44:36 [] (unknown:0) - Session start time …: 2018-04-17 23:44:36<br>
[DEBUG][Qt] 17.04.2018 23:44:36 [] (unknown:0) - Slicer version …: 4.8.1 (revision 26813) win-amd64 - installed<br>
[DEBUG][Qt] 17.04.2018 23:44:36 [] (unknown:0) - Operating system …: Windows /  Personal /  (Build 9200) - 64-bit<br>
[DEBUG][Qt] 17.04.2018 23:44:36 [] (unknown:0) - Memory …: 11200 MB physical, 12928 MB virtual<br>
[DEBUG][Qt] 17.04.2018 23:44:36 [] (unknown:0) - CPU …: AuthenticAMD AMD A8-7410 APU with AMD Radeon R5 Graphics    , 4 cores, 1 logical processors<br>
[DEBUG][Qt] 17.04.2018 23:44:36 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 17.04.2018 23:44:36 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 17.04.2018 23:44:36 [] (unknown:0) - Additional module paths …: (none)<br>
[DEBUG][Python] 17.04.2018 23:44:38 [Python] (C:\Program Files\Slicer 4.8.1\lib\Python\Lib\site-packages\git\cmd.py:719) - Popen(%s, cwd=%s, universal_newlines=%s, shell=%s)<br>
[DEBUG][Python] 17.04.2018 23:44:39 [Python] (C:\Program Files\Slicer 4.8.1\lib\Python\Lib\site-packages\git\cmd.py:719) - Popen(%s, cwd=%s, universal_newlines=%s, shell=%s)<br>
[DEBUG][Python] 17.04.2018 23:44:40 [Python] (C:\Program Files\Slicer 4.8.1\lib\Slicer-4.8\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 17.04.2018 23:44:42 [Python] (C:\Program Files\Slicer 4.8.1\lib\Slicer-4.8\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 17.04.2018 23:44:42 [Python] (C:\Program Files\Slicer 4.8.1\lib\Slicer-4.8\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 17.04.2018 23:44:37 [] (unknown:0) - Number of registered modules: 135<br>
[DEBUG][Qt] 17.04.2018 23:44:39 [] (unknown:0) - Number of instantiated modules: 135<br>
[DEBUG][Qt] 17.04.2018 23:44:42 [] (unknown:0) - Number of loaded modules: 135<br>
[DEBUG][Qt] 17.04.2018 23:44:42 [] (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 17.04.2018 23:44:48 [] (unknown:0) - Switch to module:  “SampleData”<br>
[INFO][VTK] 17.04.2018 23:44:52 [vtkMRMLVolumeArchetypeStorageNode (000000B0A528A600)] (D:\D\P\Slicer-481\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:465) - Loaded volume from file: C:/Users/BARTOM~1/AppData/Local/Temp/Slicer/RemoteIO/Panoramix-cropped.nrrd. Dimensions: 441x321x215. Number of components: 1. Pixel type: short.<br>
[DEBUG][Qt] 17.04.2018 23:44:52 [] (unknown:0) - “Volume” Reader has successfully read the file “C:/Users/BARTOM~1/AppData/Local/Temp/Slicer/RemoteIO/Panoramix-cropped.nrrd” “[2.22s]”<br>
[DEBUG][Qt] 17.04.2018 23:44:56 [] (unknown:0) - Switch to module:  “Editor”<br>
[DEBUG][Qt] 17.04.2018 23:45:04 [] (unknown:0) - Found CommandLine Module, target is  C:/Program Files/Slicer 4.8.1/lib/Slicer-4.8/cli-modules/ModelMaker.exe<br>
[DEBUG][Qt] 17.04.2018 23:45:04 [] (unknown:0) - ModuleType: CommandLineModule<br>
[DEBUG][Qt] 17.04.2018 23:45:04 [] (unknown:0) - Model Maker command line:</p>
<p>C:/Program Files/Slicer 4.8.1/lib/Slicer-4.8/cli-modules/ModelMaker.exe --color C:/Users/BARTOM~1/AppData/Local/Temp/Slicer/CJCA_vtkMRMLColorTableNodeFileGenericAnatomyColors.txt.ctbl --modelSceneFile C:/Users/BARTOM~1/AppData/Local/Temp/Slicer/CJCA_AAAAAABAAFCGFBIA.mrml#vtkMRMLModelHierarchyNode1 --name tissue --labels 1 --start -1 --end -1 --skipUnNamed --smooth 10 --filtertype Sinc --decimate 0.25 --splitnormals --pointnormals --pad C:/Users/BARTOM~1/AppData/Local/Temp/Slicer/CJCA_vtkMRMLLabelMapVolumeNodeB.nrrd<br>
[DEBUG][Qt] 17.04.2018 23:45:07 [] (unknown:0) - Model Maker standard output:</p>
<p>Adding 1 pixel padding around the image, shifting origin.<br>
Models saved to scene file C:/Users/BARTOM~1/AppData/Local/Temp/Slicer/CJCA_AAAAAABAAFCGFBIA.mrml<br>
[DEBUG][Qt] 17.04.2018 23:45:07 [] (unknown:0) - Model Maker completed without errors<br>
[ERROR][VTK] 17.04.2018 23:45:14 [vtkMRMLVolumeArchetypeStorageNode (000000B0A528A460)] (D:\D\P\Slicer-481\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:696) - UpdateFileList: Failed to create directoryC:/Program Files/Slicer 4.8.1/TempWritePanoramix-cropped<br>
[CRITICAL][Stream] 17.04.2018 23:45:14 [] (unknown:0) -<br>
[CRITICAL][Stream] 17.04.2018 23:45:14 [] (unknown:0) - itk::ExceptionObject (000000B096BF5898)<br>
[CRITICAL][Stream] 17.04.2018 23:45:14 [] (unknown:0) - Location: “unknown”<br>
[CRITICAL][Stream] 17.04.2018 23:45:14 [] (unknown:0) - File: D:\D\P\Slicer-481-package\ITKv4\Modules\IO\NRRD\src\itkNrrdImageIO.cxx<br>
[CRITICAL][Stream] 17.04.2018 23:45:14 [] (unknown:0) - Line: 1120<br>
[CRITICAL][Stream] 17.04.2018 23:45:14 [] (unknown:0) - Description: itk::ERROR: NrrdImageIO(000000B0A477BF00): Write: Error writing C:/Program Files/Slicer 4.8.1/Panoramix-cropped.nrrd:<br>
[CRITICAL][Stream] 17.04.2018 23:45:14 [] (unknown:0) - [nrrd] nrrdSave: couldn’t fopen(“C:/Program Files/Slicer 4.8.1/Panoramix-cropped.nrrd”,“wb”): Permission denied<br>
[CRITICAL][Stream] 17.04.2018 23:45:14 [] (unknown:0) -<br>
[CRITICAL][Stream] 17.04.2018 23:45:14 [] (unknown:0) -<br>
[ERROR][VTK] 17.04.2018 23:45:23 [vtkMRMLVolumeArchetypeStorageNode (000000B0A52883E0)] (D:\D\P\Slicer-481\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:696) - UpdateFileList: Failed to create directoryC:/Program Files/Slicer 4.8.1/TempWritePanoramix-cropped-label<br>
[CRITICAL][Stream] 17.04.2018 23:45:23 [] (unknown:0) -<br>
[CRITICAL][Stream] 17.04.2018 23:45:23 [] (unknown:0) - itk::ExceptionObject (000000B096BF5898)<br>
[CRITICAL][Stream] 17.04.2018 23:45:23 [] (unknown:0) - Location: “unknown”<br>
[CRITICAL][Stream] 17.04.2018 23:45:23 [] (unknown:0) - File: D:\D\P\Slicer-481-package\ITKv4\Modules\IO\NRRD\src\itkNrrdImageIO.cxx<br>
[CRITICAL][Stream] 17.04.2018 23:45:23 [] (unknown:0) - Line: 1120<br>
[CRITICAL][Stream] 17.04.2018 23:45:23 [] (unknown:0) - Description: itk::ERROR: NrrdImageIO(000000B0A477BF00): Write: Error writing C:/Program Files/Slicer 4.8.1/Panoramix-cropped-label.nrrd:<br>
[CRITICAL][Stream] 17.04.2018 23:45:23 [] (unknown:0) - [nrrd] nrrdSave: couldn’t fopen(“C:/Program Files/Slicer 4.8.1/Panoramix-cropped-label.nrrd”,“wb”): Permission denied<br>
[CRITICAL][Stream] 17.04.2018 23:45:23 [] (unknown:0) -<br>
[CRITICAL][Stream] 17.04.2018 23:45:23 [] (unknown:0) -<br>
[ERROR][VTK] 17.04.2018 23:45:25 [vtkPolyDataWriter (000000B0A365D550)] (D:\D\P\Slicer-481-package\VTKv9\IO\Legacy\vtkDataWriter.cxx:184) - Unable to open file: C:/Program Files/Slicer 4.8.1/tissue.vtk<br>
[WARNING][Qt] 17.04.2018 23:45:25 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile<br>
[WARNING][VTK] 17.04.2018 23:45:26 [vtkMRMLLabelMapVolumeDisplayNode (000000B0A4C9C3D0)] (D:\D\P\Slicer-481\Libs\MRML\Core\vtkMRMLLabelMapVolumeDisplayNode.cxx:123) - vtkMRMLLabelMapVolumeDisplayNode: Warning, the color table node: vtkMRMLColorTableNodeFileGenericAnatomyColors.txt can’t be found<br>
[WARNING][VTK] 17.04.2018 23:45:26 [vtkMRMLLabelMapVolumeDisplayNode (000000B0A4C9C3D0)] (D:\D\P\Slicer-481\Libs\MRML\Core\vtkMRMLLabelMapVolumeDisplayNode.cxx:123) - vtkMRMLLabelMapVolumeDisplayNode: Warning, the color table node: vtkMRMLColorTableNodeFileGenericAnatomyColors.txt can’t be found<br>
[WARNING][VTK] 17.04.2018 23:45:26 [vtkMRMLLabelMapVolumeDisplayNode (000000B0A4C9C3D0)] (D:\D\P\Slicer-481\Libs\MRML\Core\vtkMRMLLabelMapVolumeDisplayNode.cxx:123) - vtkMRMLLabelMapVolumeDisplayNode: Warning, the color table node: vtkMRMLColorTableNodeFileGenericAnatomyColors.txt can’t be found<br>
[ERROR][VTK] 17.04.2018 23:45:26 [vtkPNGWriter (000000B0A33D0CB0)] (D:\D\P\Slicer-481-package\VTKv9\IO\Image\vtkPNGWriter.cxx:276) - Unable to open file C:/Program Files/Slicer 4.8.1/Master Scene View.png<br>
[ERROR][VTK] 17.04.2018 23:45:26 [vtkPNGWriter (000000B0A33D0CB0)] (D:\D\P\Slicer-481-package\VTKv9\IO\Image\vtkImageWriter.cxx:504) - Ran out of disk space; deleting file(s) already written<br>
[ERROR][VTK] 17.04.2018 23:45:26 [vtkMRMLScene (000000B09967ED10)] (D:\D\P\Slicer-481\Libs\MRML\Core\vtkMRMLScene.cxx:984) - Write: Could not open file C:/Program Files/Slicer 4.8.1/2018-04-17-Scene.mrml</p>

---

## Post #7 by @pieper (2018-04-17 22:13 UTC)

<p>You are still trying to save into the Slicer program directory.</p>
<aside class="quote no-group quote-modified" data-username="rakusb" data-post="6" data-topic="2611">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/ecae2f/48.png" class="avatar"> rakusb:</div>
<blockquote>
<p>[CRITICAL][Stream] 17.04.2018 23:45:23 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Description: itk::ERROR: NrrdImageIO(000000B0A477BF00): Write: Error writing C:/Program Files/Slicer 4.8.1/Panoramix-cropped-label.nrrd:</p>
<p>[CRITICAL][Stream] 17.04.2018 23:45:23 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - [nrrd] nrrdSave: couldn’t fopen(“C:/Program Files/Slicer 4.8.1/Panoramix-cropped-label.nrrd”,“wb”): Permission denied</p>
</blockquote>
</aside>
<p>You can change it with the dialog as described here:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.8/SlicerApplication/SavingData" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/4.8/SlicerApplication/SavingData</a></p>
<aside class="quote no-group" data-username="cpinter" data-post="5" data-topic="2611">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p><a class="mention" href="/u/pieper">@pieper</a> I just updated this page so that it points to the very useful ‘Report a bug’ window where the clipboard can be copied by a single button press.</p>
</blockquote>
</aside>
<p>Good catch - Thanks!</p>

---

## Post #8 by @rakusb (2018-04-18 11:14 UTC)

<p>Same thing</p>
<p>[DEBUG][Qt] 18.04.2018 13:11:42 [] (unknown:0) - Session start time …: 2018-04-18 13:11:42<br>
[DEBUG][Qt] 18.04.2018 13:11:42 [] (unknown:0) - Slicer version …: 4.8.1 (revision 26813) win-amd64 - installed<br>
[DEBUG][Qt] 18.04.2018 13:11:42 [] (unknown:0) - Operating system …: Windows /  Personal /  (Build 9200) - 64-bit<br>
[DEBUG][Qt] 18.04.2018 13:11:42 [] (unknown:0) - Memory …: 11200 MB physical, 12928 MB virtual<br>
[DEBUG][Qt] 18.04.2018 13:11:42 [] (unknown:0) - CPU …: AuthenticAMD AMD A8-7410 APU with AMD Radeon R5 Graphics    , 4 cores, 1 logical processors<br>
[DEBUG][Qt] 18.04.2018 13:11:42 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 18.04.2018 13:11:42 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 18.04.2018 13:11:42 [] (unknown:0) - Additional module paths …: (none)<br>
[DEBUG][Qt] 18.04.2018 13:11:42 [] (unknown:0) - Session start time …: 2018-04-18 13:11:42<br>
[DEBUG][Qt] 18.04.2018 13:11:42 [] (unknown:0) - Session start time …: 2018-04-18 13:11:42<br>
[DEBUG][Qt] 18.04.2018 13:11:42 [] (unknown:0) - Slicer version …: 4.8.1 (revision 26813) win-amd64 - installed<br>
[DEBUG][Qt] 18.04.2018 13:11:42 [] (unknown:0) - Operating system …: Windows /  Personal /  (Build 9200) - 64-bit<br>
[DEBUG][Qt] 18.04.2018 13:11:42 [] (unknown:0) - Memory …: 11200 MB physical, 12928 MB virtual<br>
[DEBUG][Qt] 18.04.2018 13:11:42 [] (unknown:0) - CPU …: AuthenticAMD AMD A8-7410 APU with AMD Radeon R5 Graphics    , 4 cores, 1 logical processors<br>
[DEBUG][Qt] 18.04.2018 13:11:42 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 18.04.2018 13:11:42 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 18.04.2018 13:11:42 [] (unknown:0) - Additional module paths …: (none)<br>
[DEBUG][Python] 18.04.2018 13:12:09 [Python] (C:\Program Files\Slicer 4.8.1\lib\Python\Lib\site-packages\git\cmd.py:719) - Popen(%s, cwd=%s, universal_newlines=%s, shell=%s)<br>
[DEBUG][Python] 18.04.2018 13:12:10 [Python] (C:\Program Files\Slicer 4.8.1\lib\Python\Lib\site-packages\git\cmd.py:719) - Popen(%s, cwd=%s, universal_newlines=%s, shell=%s)<br>
[DEBUG][Python] 18.04.2018 13:12:21 [Python] (C:\Program Files\Slicer 4.8.1\lib\Slicer-4.8\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 18.04.2018 13:12:24 [Python] (C:\Program Files\Slicer 4.8.1\lib\Slicer-4.8\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 18.04.2018 13:12:24 [Python] (C:\Program Files\Slicer 4.8.1\lib\Slicer-4.8\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 18.04.2018 13:11:51 [] (unknown:0) - Number of registered modules: 135<br>
[DEBUG][Qt] 18.04.2018 13:11:51 [] (unknown:0) - Number of registered modules: 135<br>
[DEBUG][Qt] 18.04.2018 13:12:14 [] (unknown:0) - Number of instantiated modules: 135<br>
[DEBUG][Qt] 18.04.2018 13:12:24 [] (unknown:0) - Number of loaded modules: 135<br>
[DEBUG][Qt] 18.04.2018 13:12:24 [] (unknown:0) - Number of loaded modules: 135<br>
[DEBUG][Qt] 18.04.2018 13:12:24 [] (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 18.04.2018 13:12:24 [] (unknown:0) - Number of loaded modules: 135<br>
[DEBUG][Qt] 18.04.2018 13:12:24 [] (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 18.04.2018 13:12:33 [] (unknown:0) - Switch to module:  “SampleData”<br>
[INFO][VTK] 18.04.2018 13:12:43 [vtkMRMLVolumeArchetypeStorageNode (000000868DE6AA70)] (D:\D\P\Slicer-481\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:465) - Loaded volume from file: C:/Users/BARTOM~1/AppData/Local/Temp/Slicer/RemoteIO/Panoramix-cropped.nrrd. Dimensions: 441x321x215. Number of components: 1. Pixel type: short.<br>
[DEBUG][Qt] 18.04.2018 13:12:43 [] (unknown:0) - “Volume” Reader has successfully read the file “C:/Users/BARTOM~1/AppData/Local/Temp/Slicer/RemoteIO/Panoramix-cropped.nrrd” “[9.29s]”<br>
[DEBUG][Qt] 18.04.2018 13:12:47 [] (unknown:0) - Switch to module:  “Editor”<br>
[DEBUG][Qt] 18.04.2018 13:13:00 [] (unknown:0) - Found CommandLine Module, target is  C:/Program Files/Slicer 4.8.1/lib/Slicer-4.8/cli-modules/ModelMaker.exe<br>
[DEBUG][Qt] 18.04.2018 13:13:00 [] (unknown:0) - ModuleType: CommandLineModule<br>
[DEBUG][Qt] 18.04.2018 13:13:02 [] (unknown:0) - Model Maker command line:</p>
<p>C:/Program Files/Slicer 4.8.1/lib/Slicer-4.8/cli-modules/ModelMaker.exe --color C:/Users/BARTOM~1/AppData/Local/Temp/Slicer/FJJG_vtkMRMLColorTableNodeFileGenericAnatomyColors.txt.ctbl --modelSceneFile C:/Users/BARTOM~1/AppData/Local/Temp/Slicer/FJJG_AAAAAAIGIFGDJAEA.mrml#vtkMRMLModelHierarchyNode1 --name tissue --labels 1 --start -1 --end -1 --skipUnNamed --smooth 10 --filtertype Sinc --decimate 0.25 --splitnormals --pointnormals --pad C:/Users/BARTOM~1/AppData/Local/Temp/Slicer/FJJG_vtkMRMLLabelMapVolumeNodeB.nrrd<br>
[DEBUG][Qt] 18.04.2018 13:13:06 [] (unknown:0) - Model Maker standard output:</p>
<p>Adding 1 pixel padding around the image, shifting origin.<br>
Models saved to scene file C:/Users/BARTOM~1/AppData/Local/Temp/Slicer/FJJG_AAAAAAIGIFGDJAEA.mrml<br>
[DEBUG][Qt] 18.04.2018 13:13:06 [] (unknown:0) - Model Maker completed without errors<br>
[ERROR][VTK] 18.04.2018 13:13:34 [vtkMRMLVolumeArchetypeStorageNode (000000868DE6D990)] (D:\D\P\Slicer-481\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:696) - UpdateFileList: Failed to create directoryC:/Users/Bart?omiej Rakus/Documents/TempWritePanoramix-cropped<br>
[CRITICAL][Stream] 18.04.2018 13:13:34 [] (unknown:0) -<br>
[CRITICAL][Stream] 18.04.2018 13:13:34 [] (unknown:0) - itk::ExceptionObject (0000008681045A08)<br>
[CRITICAL][Stream] 18.04.2018 13:13:34 [] (unknown:0) - Location: “unknown”<br>
[CRITICAL][Stream] 18.04.2018 13:13:34 [] (unknown:0) - File: D:\D\P\Slicer-481-package\ITKv4\Modules\IO\NRRD\src\itkNrrdImageIO.cxx<br>
[CRITICAL][Stream] 18.04.2018 13:13:34 [] (unknown:0) - Line: 1120<br>
[CRITICAL][Stream] 18.04.2018 13:13:34 [] (unknown:0) - Description: itk::ERROR: NrrdImageIO(000000868EF77BE0): Write: Error writing C:/Users/Bart?omiej Rakus/Documents/Panoramix-cropped.nrrd:<br>
[CRITICAL][Stream] 18.04.2018 13:13:34 [] (unknown:0) - [nrrd] nrrdSave: couldn’t fopen(“C:/Users/Bart?omiej Rakus/Documents/Panoramix-cropped.nrrd”,“wb”): Invalid argument<br>
[CRITICAL][Stream] 18.04.2018 13:13:34 [] (unknown:0) -<br>
[CRITICAL][Stream] 18.04.2018 13:13:34 [] (unknown:0) -<br>
[ERROR][VTK] 18.04.2018 13:13:37 [vtkMRMLVolumeArchetypeStorageNode (000000868DE6D310)] (D:\D\P\Slicer-481\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:696) - UpdateFileList: Failed to create directoryC:/Users/Bart?omiej Rakus/Documents/TempWritePanoramix-cropped-label<br>
[CRITICAL][Stream] 18.04.2018 13:13:37 [] (unknown:0) -<br>
[CRITICAL][Stream] 18.04.2018 13:13:37 [] (unknown:0) - itk::ExceptionObject (0000008681045A08)<br>
[CRITICAL][Stream] 18.04.2018 13:13:37 [] (unknown:0) - Location: “unknown”<br>
[CRITICAL][Stream] 18.04.2018 13:13:37 [] (unknown:0) - File: D:\D\P\Slicer-481-package\ITKv4\Modules\IO\NRRD\src\itkNrrdImageIO.cxx<br>
[CRITICAL][Stream] 18.04.2018 13:13:37 [] (unknown:0) - Line: 1120<br>
[CRITICAL][Stream] 18.04.2018 13:13:37 [] (unknown:0) - Description: itk::ERROR: NrrdImageIO(000000868EF79350): Write: Error writing C:/Users/Bart?omiej Rakus/Documents/Panoramix-cropped-label.nrrd:<br>
[CRITICAL][Stream] 18.04.2018 13:13:37 [] (unknown:0) - [nrrd] nrrdSave: couldn’t fopen(“C:/Users/Bart?omiej Rakus/Documents/Panoramix-cropped-label.nrrd”,“wb”): Invalid argument<br>
[CRITICAL][Stream] 18.04.2018 13:13:37 [] (unknown:0) -<br>
[CRITICAL][Stream] 18.04.2018 13:13:37 [] (unknown:0) -<br>
[ERROR][VTK] 18.04.2018 13:13:38 [vtkPolyDataWriter (000000868F112E40)] (D:\D\P\Slicer-481-package\VTKv9\IO\Legacy\vtkDataWriter.cxx:184) - Unable to open file: C:/Users/Bart?omiej Rakus/Documents/tissue.vtk<br>
[WARNING][Qt] 18.04.2018 13:13:38 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile<br>
[WARNING][VTK] 18.04.2018 13:13:39 [vtkMRMLLabelMapVolumeDisplayNode (000000868F150CC0)] (D:\D\P\Slicer-481\Libs\MRML\Core\vtkMRMLLabelMapVolumeDisplayNode.cxx:123) - vtkMRMLLabelMapVolumeDisplayNode: Warning, the color table node: vtkMRMLColorTableNodeFileGenericAnatomyColors.txt can’t be found<br>
[WARNING][VTK] 18.04.2018 13:13:39 [vtkMRMLLabelMapVolumeDisplayNode (000000868F150CC0)] (D:\D\P\Slicer-481\Libs\MRML\Core\vtkMRMLLabelMapVolumeDisplayNode.cxx:123) - vtkMRMLLabelMapVolumeDisplayNode: Warning, the color table node: vtkMRMLColorTableNodeFileGenericAnatomyColors.txt can’t be found<br>
[WARNING][VTK] 18.04.2018 13:13:39 [vtkMRMLLabelMapVolumeDisplayNode (000000868F150CC0)] (D:\D\P\Slicer-481\Libs\MRML\Core\vtkMRMLLabelMapVolumeDisplayNode.cxx:123) - vtkMRMLLabelMapVolumeDisplayNode: Warning, the color table node: vtkMRMLColorTableNodeFileGenericAnatomyColors.txt can’t be found<br>
[ERROR][VTK] 18.04.2018 13:13:39 [vtkPNGWriter (000000869B4D4D30)] (D:\D\P\Slicer-481-package\VTKv9\IO\Image\vtkPNGWriter.cxx:276) - Unable to open file C:/Users/Bart?omiej Rakus/Documents/Master Scene View.png<br>
[ERROR][VTK] 18.04.2018 13:13:39 [vtkPNGWriter (000000869B4D4D30)] (D:\D\P\Slicer-481-package\VTKv9\IO\Image\vtkImageWriter.cxx:504) - Ran out of disk space; deleting file(s) already written<br>
[ERROR][VTK] 18.04.2018 13:13:39 [vtkMRMLScene (0000008683DA4B40)] (D:\D\P\Slicer-481\Libs\MRML\Core\vtkMRMLScene.cxx:984) - Write: Could not open file C:/Users/Bart?omiej Rakus/Documents/2018-04-18-Scene.mrml</p>

---

## Post #9 by @lassoan (2018-04-18 11:31 UTC)

<p>The problem is that your save path contains special characters. The path can only contain ASCII or latin1 characters (<a href="https://en.m.wikipedia.org/wiki/ISO/IEC_8859-1">https://en.m.wikipedia.org/wiki/ISO/IEC_8859-1</a>).</p>

---

## Post #10 by @pieper (2018-04-18 11:34 UTC)

<p>This time there’s a non-ascii character in the directory path.</p>
<aside class="quote no-group quote-modified" data-username="rakusb" data-post="8" data-topic="2611">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/ecae2f/48.png" class="avatar"> rakusb:</div>
<blockquote>
<p>[CRITICAL][Stream] 18.04.2018 13:13:34 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Description: itk::ERROR: NrrdImageIO(000000868EF77BE0): Write: Error writing C:/Users/Bart?omiej Rakus/Documents/Panoramix-cropped.nrrd:</p>
<p>[CRITICAL][Stream] 18.04.2018 13:13:34 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - [nrrd] nrrdSave: couldn’t fopen(“C:/Users/Bart?omiej Rakus/Documents/Panoramix-cropped.nrrd”,“wb”): Invalid argument</p>
</blockquote>
</aside>

---

## Post #11 by @rakusb (2018-04-18 12:03 UTC)

<p>…, thank you, it works <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=5" title=":smiley:" class="emoji" alt=":smiley:"></p>

---

## Post #12 by @ewa (2018-04-18 13:04 UTC)

<p>Dear Bartholomew,<br>
Why do you send me some files? And what are the projects<br>
Respectfully,<br>
Ewa Tomaszewska <img src="https://emoji.discourse-cdn.com/twitter/joy.png?v=5" title=":joy:" class="emoji" alt=":joy:"><img src="https://emoji.discourse-cdn.com/twitter/joy.png?v=5" title=":joy:" class="emoji" alt=":joy:"><img src="https://emoji.discourse-cdn.com/twitter/joy.png?v=5" title=":joy:" class="emoji" alt=":joy:"><img src="https://emoji.discourse-cdn.com/twitter/joy.png?v=5" title=":joy:" class="emoji" alt=":joy:"><img src="https://emoji.discourse-cdn.com/twitter/joy.png?v=5" title=":joy:" class="emoji" alt=":joy:"><img src="https://emoji.discourse-cdn.com/twitter/joy.png?v=5" title=":joy:" class="emoji" alt=":joy:"><img src="https://emoji.discourse-cdn.com/twitter/joy.png?v=5" title=":joy:" class="emoji" alt=":joy:"><img src="https://emoji.discourse-cdn.com/twitter/joy.png?v=5" title=":joy:" class="emoji" alt=":joy:"></p>
<details>
<summary>
Original</summary>
<p>Szanowny Panie Bartłomieju,</p>
<p>Czemu Pan wysyła mi jakieś pliki ? A co to za projekty</p>
<p>Z wyrazami szacunku,</p>
<p>Ewa Tomaszewska <img src="https://emoji.discourse-cdn.com/twitter/joy.png?v=5" title=":joy:" class="emoji" alt=":joy:"><img src="https://emoji.discourse-cdn.com/twitter/joy.png?v=5" title=":joy:" class="emoji" alt=":joy:"><img src="https://emoji.discourse-cdn.com/twitter/joy.png?v=5" title=":joy:" class="emoji" alt=":joy:"><img src="https://emoji.discourse-cdn.com/twitter/joy.png?v=5" title=":joy:" class="emoji" alt=":joy:"><img src="https://emoji.discourse-cdn.com/twitter/joy.png?v=5" title=":joy:" class="emoji" alt=":joy:"><img src="https://emoji.discourse-cdn.com/twitter/joy.png?v=5" title=":joy:" class="emoji" alt=":joy:"><img src="https://emoji.discourse-cdn.com/twitter/joy.png?v=5" title=":joy:" class="emoji" alt=":joy:"><img src="https://emoji.discourse-cdn.com/twitter/joy.png?v=5" title=":joy:" class="emoji" alt=":joy:"></p>
</details>

---
