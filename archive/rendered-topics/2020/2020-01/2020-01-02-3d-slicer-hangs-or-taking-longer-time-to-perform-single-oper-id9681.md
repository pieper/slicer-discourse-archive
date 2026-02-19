---
topic_id: 9681
title: "3D Slicer Hangs Or Taking Longer Time To Perform Single Oper"
date: 2020-01-02
url: https://discourse.slicer.org/t/9681
---

# 3D slicer hangs or taking longer time to perform single operation

**Topic ID**: 9681
**Date**: 2020-01-02
**URL**: https://discourse.slicer.org/t/3d-slicer-hangs-or-taking-longer-time-to-perform-single-operation/9681

---

## Post #1 by @Ramya_C (2020-01-02 02:17 UTC)

<p>Operating system: windows 10<br>
Slicer version: 4.8.1<br>
Expected behavior:<br>
Actual behavior:</p>
<p>I am using 3D slicer for segmentation and modelling. The slicer file takes longer time to open and to perform any operation. My file is not big and not sure if the issue caused.<br>
I have tried in latest version as well with my file but still getting this hanging issue.</p>
<p>I have updated my graphics card and Bios. Below is the log file extracted from the bug<br>
May I know if anyone can help to assit with this issue.<br>
[DEBUG][Qt] 02.01.2020 07:55:05 [] (unknown:0) - Session start time …: 2020-01-02 07:55:05<br>
[DEBUG][Qt] 02.01.2020 07:55:05 [] (unknown:0) - Slicer version …: 4.8.1 (revision 26813) win-amd64 - installed<br>
[DEBUG][Qt] 02.01.2020 07:55:05 [] (unknown:0) - Operating system …: Windows /  Professional /  (Build 9200) - 64-bit<br>
[DEBUG][Qt] 02.01.2020 07:55:05 [] (unknown:0) - Memory …: 16226 MB physical, 45922 MB virtual<br>
[DEBUG][Qt] 02.01.2020 07:55:05 [] (unknown:0) - CPU …: GenuineIntel , 12 cores, 16 logical processors<br>
[DEBUG][Qt] 02.01.2020 07:55:05 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 02.01.2020 07:55:05 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 02.01.2020 07:55:05 [] (unknown:0) - Additional module paths …: (none)<br>
[DEBUG][Python] 02.01.2020 07:55:06 [Python] (C:\Program Files\Slicer 4.8.1\lib\Python\Lib\site-packages\git\cmd.py:719) - Popen(%s, cwd=%s, universal_newlines=%s, shell=%s)<br>
[DEBUG][Python] 02.01.2020 07:55:07 [Python] (C:\Program Files\Slicer 4.8.1\lib\Python\Lib\site-packages\git\cmd.py:719) - Popen(%s, cwd=%s, universal_newlines=%s, shell=%s)<br>
[DEBUG][Python] 02.01.2020 07:55:08 [Python] (C:\Program Files\Slicer 4.8.1\lib\Slicer-4.8\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 02.01.2020 07:55:09 [Python] (C:\Program Files\Slicer 4.8.1\lib\Slicer-4.8\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 02.01.2020 07:55:09 [Python] (C:\Program Files\Slicer 4.8.1\lib\Slicer-4.8\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 02.01.2020 07:55:05 [] (unknown:0) - Number of registered modules: 135<br>
[DEBUG][Qt] 02.01.2020 07:55:07 [] (unknown:0) - Number of instantiated modules: 135<br>
[DEBUG][Qt] 02.01.2020 07:55:09 [] (unknown:0) - Number of loaded modules: 135<br>
[DEBUG][Qt] 02.01.2020 07:55:09 [] (unknown:0) - Switch to module:  “Welcome”<br>
[INFO][VTK] 02.01.2020 07:55:11 [vtkMRMLVolumeArchetypeStorageNode (000001D6923A3800)] (D:\D\P\Slicer-481\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:465) - Loaded volume from file: C:/Users/ramya.c/Desktop/models/1st Jan 2020/v2/3 HEAD SAG 1  1.0  B31s…nrrd. Dimensions: 512x512x427. Number of components: 1. Pixel type: short.<br>
[WARNING][VTK] 02.01.2020 08:00:54 [vtkObserverManager (000001D69270C3D0)] (D:\D\P\Slicer-481\Libs\MRML\Core\vtkObserverManager.cxx:131) - The same object is already observed with the same priority. The observation is kept as is.<br>
[WARNING][VTK] 02.01.2020 08:00:54 [vtkObserverManager (000001D69270CA30)] (D:\D\P\Slicer-481\Libs\MRML\Core\vtkObserverManager.cxx:131) - The same object is already observed with the same priority. The observation is kept as is.<br>
[DEBUG][Qt] 02.01.2020 08:00:55 [] (unknown:0) - “MRML Scene” Reader has successfully read the file “C:/Users/ramya.c/Desktop/models/1st Jan 2020/v2/2019-11-22-Scene.mrml” “[345.79s]”<br>
[DEBUG][Qt] 02.01.2020 08:03:03 [] (unknown:0) - Switch to module:  “VolumeRendering”<br>
[WARNING][VTK] 02.01.2020 08:03:04 [vtkObserverManager (000001D69270CA30)] (D:\D\P\Slicer-481\Libs\MRML\Core\vtkObserverManager.cxx:131) - The same object is already observed with the same priority. The observation is kept as is.<br>
[DEBUG][Qt] 02.01.2020 08:03:55 [] (unknown:0) - Switch to module:  “SegmentEditor”<br>
[WARNING][Qt] 02.01.2020 08:13:49 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile</p>

---

## Post #2 by @lassoan (2020-01-02 02:56 UTC)

<p>Slicer-4.8.1 is more than two years old! We have fixed many issues and implemented huge performance improvements since then, so please do not use this ancient version anymore.</p>
<p>If possible, create a new scene from scratch using latest Slicer Preview release. If you still experience any performance issues then let us know.</p>

---

## Post #3 by @Ramya_C (2020-01-02 03:00 UTC)

<p>Is it possible to use the file created in slicer 4.8.1 in the preview release  and do the necessary work from there ?</p>

---

## Post #4 by @lassoan (2020-01-02 03:02 UTC)

<p>You may not benefit from all the performance improvements if you load a scene that was created with a very old Slicer version.</p>
<p>The best is if you can re-create the scene from scratch - at least for testing, to see if indeed you get much better performance. Loading data files into the scene (rather than opening an old scene file) may help, too.</p>

---

## Post #5 by @Saima (2020-11-02 05:45 UTC)

<p>Hi Andras,<br>
I am accessing all voxels based on value &gt; 0 and then adding fiducial at that point. Slicer is not responding for longer arrays like I am iterating over 58000. Its haults and i need to shut it down.</p>
<p>How to make this fast and get the results.</p>
<p>i m using 4.11 version of 3d slicer<br>
thank you</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #6 by @lassoan (2020-11-02 17:23 UTC)

<p>Fiducials points are interactive widgets. You can expect performance issues if want to interact with 58000 of interactive widgets in a view.</p>
<p>If you want to just visualize points then don’t create markups. Instead, you can create a point set and generate a displayable polydata using VTK glyph filter. But of course if you really just want to visualize each voxel of an image then you can do that directly, using volume rendering module.</p>
<p>But there are issues with the approach at other levels, too. You should not iterate through more than a few hundred (or maybe a few thousand) points in Python. If you have a lot of points then you need to use vector operations: keep all coordinates in numpy array and do everything using array operations.</p>

---
