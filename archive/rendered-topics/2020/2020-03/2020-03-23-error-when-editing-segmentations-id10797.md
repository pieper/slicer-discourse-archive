---
topic_id: 10797
title: "Error When Editing Segmentations"
date: 2020-03-23
url: https://discourse.slicer.org/t/10797
---

# Error when editing segmentations

**Topic ID**: 10797
**Date**: 2020-03-23
**URL**: https://discourse.slicer.org/t/error-when-editing-segmentations/10797

---

## Post #1 by @KassandraFord (2020-03-23 17:25 UTC)

<p>Problem report for Slicer 4.11.0-2020-03-15 win-amd64: [please describe expected and actual behavior]</p>
<p>This error has happened several times in the last week. I have tried downloading the new preview versions of Slicer, but I am still getting this error. First, I can no longer read in a .nrrd file as a Volume Sequence, only a Volume. The preview options for editing the segment (grow from seeds,etc.) are no longer available. After I read in a .nrrd file, I went to Segmentations&gt;Create New Segment&gt;Edit Selected. Each time there is an error, I am either using the Scissors tool or the Islands tool to remove sections of the scan I do not need. The program starts to work, then puts out this error. If I accept the error and continue, it will not allow me to save any of the work done. Once I close the program, a second window pops up with several phrases like “vtkDebugLeaks has detected LEAKS!” I have a screenshot of both errors.</p>
<p>Log file:<br>
[DEBUG][Qt] 23.03.2020 11:18:41 [] (unknown:0) - Session start time …: 2020-03-23 11:18:41<br>
[DEBUG][Qt] 23.03.2020 11:18:41 [] (unknown:0) - Slicer version …: 4.11.0-2020-03-15 (revision 5266433) win-amd64 - installed release<br>
[DEBUG][Qt] 23.03.2020 11:18:41 [] (unknown:0) - Operating system …: Windows /  Personal / (Build 18362, Code Page 65001) - 64-bit<br>
[DEBUG][Qt] 23.03.2020 11:18:41 [] (unknown:0) - Memory …: 16210 MB physical, 23330 MB virtual<br>
[DEBUG][Qt] 23.03.2020 11:18:41 [] (unknown:0) - CPU …: GenuineIntel , 12 cores, 12 logical processors<br>
[DEBUG][Qt] 23.03.2020 11:18:41 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 23.03.2020 11:18:41 [] (unknown:0) - Qt configuration …: version 5.10.1, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 23.03.2020 11:18:41 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 23.03.2020 11:18:41 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 23.03.2020 11:18:41 [] (unknown:0) - Application path …: C:/Users/kassy/AppData/Local/NA-MIC/Slicer 4.11.0-2020-03-15/bin<br>
[DEBUG][Qt] 23.03.2020 11:18:41 [] (unknown:0) - Additional module paths …: (none)<br>
[DEBUG][Python] 23.03.2020 11:18:45 [Python] (C:\Users\kassy\AppData\Local\NA-MIC\Slicer 4.11.0-2020-03-15\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 23.03.2020 11:18:45 [Python] (C:\Users\kassy\AppData\Local\NA-MIC\Slicer 4.11.0-2020-03-15\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 23.03.2020 11:18:45 [Python] (C:\Users\kassy\AppData\Local\NA-MIC\Slicer 4.11.0-2020-03-15\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 23.03.2020 11:18:46 [] (unknown:0) - Switch to module:  “Welcome”<br>
[INFO][VTK] 23.03.2020 11:19:10 [vtkMRMLVolumeArchetypeStorageNode (000001DB2D80D7E0)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:471) - Loaded volume from file: D:/Dropbox/Dissertation GMM work/NRRD FILES/GMCan13_7-3.nrrd. Dimensions: 848x496x1642. Number of components: 1. Pixel type: unsigned char.<br>
[DEBUG][Qt] 23.03.2020 11:19:10 [] (unknown:0) - “Volume” Reader has successfully read the file “D:/Dropbox/Dissertation GMM work/NRRD FILES/GMCan13_7-3.nrrd” “[4.23s]”<br>
[DEBUG][Qt] 23.03.2020 11:19:26 [] (unknown:0) - Switch to module:  “Segmentations”<br>
[DEBUG][Qt] 23.03.2020 11:19:31 [] (unknown:0) - Switch to module:  “SegmentEditor”<br>
[DEBUG][Qt] 23.03.2020 11:22:42 [] (unknown:0) - Switch to module:  “Segmentations”<br>
[CRITICAL][Qt] 23.03.2020 11:22:44 [] (unknown:0) - double __cdecl qSlicerSubjectHierarchyFolderPlugin::canOwnSubjectHierarchyItem(__int64) const : Input item is invalid<br>
[ERROR][VTK] 23.03.2020 11:22:44 [vtkMRMLSubjectHierarchyNode (000001DB135468C0)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLSubjectHierarchyNode.cxx:2057) - GetItemDataNode: Failed to find subject hierarchy item by ID 0<br>
[CRITICAL][Qt] 23.03.2020 11:22:46 [] (unknown:0) - double __cdecl qSlicerSubjectHierarchyFolderPlugin::canOwnSubjectHierarchyItem(__int64) const : Input item is invalid<br>
[ERROR][VTK] 23.03.2020 11:22:46 [vtkMRMLSubjectHierarchyNode (000001DB135468C0)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLSubjectHierarchyNode.cxx:2057) - GetItemDataNode: Failed to find subject hierarchy item by ID 0<br>
[INFO][VTK] 23.03.2020 11:24:46 [vtkMRMLVolumeArchetypeStorageNode (000001DCA2E4E980)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:471) - Loaded volume from file: D:/Dropbox/Dissertation GMM work/NRRD FILES/GMCan14_1-3.nrrd. Dimensions: 520x932x1490. Number of components: 1. Pixel type: unsigned char.<br>
[DEBUG][Qt] 23.03.2020 11:24:46 [] (unknown:0) - “Volume” Reader has successfully read the file “D:/Dropbox/Dissertation GMM work/NRRD FILES/GMCan14_1-3.nrrd” “[4.49s]”<br>
[DEBUG][Qt] 23.03.2020 11:24:53 [] (unknown:0) - Switch to module:  “SegmentEditor”<br>
[DEBUG][Qt] 23.03.2020 11:30:49 [] (unknown:0) - Switch to module:  “Segmentations”<br>
[CRITICAL][Qt] 23.03.2020 11:30:51 [] (unknown:0) - double __cdecl qSlicerSubjectHierarchyFolderPlugin::canOwnSubjectHierarchyItem(__int64) const : Input item is invalid<br>
[ERROR][VTK] 23.03.2020 11:30:51 [vtkMRMLSubjectHierarchyNode (000001DB2E31D640)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLSubjectHierarchyNode.cxx:2057) - GetItemDataNode: Failed to find subject hierarchy item by ID 0<br>
[INFO][VTK] 23.03.2020 11:33:11 [vtkMRMLVolumeArchetypeStorageNode (000001DC933759D0)] (D:\D\P\Slicer-0\Libs\MRML\Core\vtkMRMLVolumeArchetypeStorageNode.cxx:471) - Loaded volume from file: D:/Dropbox/Dissertation GMM work/NRRD FILES/GMCan14_2-D.nrrd. Dimensions: 680x1040x1700. Number of components: 1. Pixel type: unsigned char.<br>
[DEBUG][Qt] 23.03.2020 11:33:11 [] (unknown:0) - “Volume” Reader has successfully read the file “D:/Dropbox/Dissertation GMM work/NRRD FILES/GMCan14_2-D.nrrd” “[7.41s]”<br>
[DEBUG][Qt] 23.03.2020 11:33:44 [] (unknown:0) - Switch to module:  “SegmentEditor”<br>
[CRITICAL][Qt] 23.03.2020 11:37:14 [] (unknown:0) - “Slicer has caught an internal error.\n\nYou may be able to continue from this point, but results are undefined.\n\nSuggested action is to save your work and restart.\n\nIf you have a repeatable sequence of steps that causes this message, please report the issue following instructions available at <a href="http://slicer.org" rel="nofollow noopener">http://slicer.org</a>\n\n\nThe message detail is:\n\nException thrown in event: bad allocation”<br>
[DEBUG][Qt] 23.03.2020 11:37:58 [] (unknown:0) - Switch to module:  “”</p>

---

## Post #2 by @pieper (2020-03-23 17:50 UTC)

<aside class="quote no-group" data-username="KassandraFord" data-post="1" data-topic="10797">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/977dab/48.png" class="avatar"> KassandraFord:</div>
<blockquote>
<p>Exception thrown in event: bad allocation</p>
</blockquote>
</aside>
<p>This message means you have run out of memory.  Maybe you are working on particularly large data?<br>
You can either add memory to your computer or downsample the data.</p>

---

## Post #3 by @lassoan (2020-03-23 18:03 UTC)

<aside class="quote no-group" data-username="KassandraFord" data-post="1" data-topic="10797">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/977dab/48.png" class="avatar"> KassandraFord:</div>
<blockquote>
<p>I can no longer read in a .nrrd file as a Volume Sequence, only a Volume</p>
</blockquote>
</aside>
<p>You need to install Sequences extension to be able to load a volume sequence.</p>
<aside class="quote no-group" data-username="KassandraFord" data-post="1" data-topic="10797">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/977dab/48.png" class="avatar"> KassandraFord:</div>
<blockquote>
<p>Exception thrown in event: bad allocation”</p>
</blockquote>
</aside>
<p>This means that you have ran out of memory.</p>
<p>You either have to load less data at a time, decrease their size by cropping and/or resampling (using Crop volume module), or increase virtual memory size in your system settings (e.g., try setting it to 50GB; but this may slow down the application significantly if you load a lot of data).</p>

---
