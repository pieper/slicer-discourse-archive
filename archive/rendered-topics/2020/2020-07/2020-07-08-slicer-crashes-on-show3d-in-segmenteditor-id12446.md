---
topic_id: 12446
title: "Slicer Crashes On Show3D In Segmenteditor"
date: 2020-07-08
url: https://discourse.slicer.org/t/12446
---

# Slicer crashes on Show3D in SegmentEditor

**Topic ID**: 12446
**Date**: 2020-07-08
**URL**: https://discourse.slicer.org/t/slicer-crashes-on-show3d-in-segmenteditor/12446

---

## Post #1 by @MartinHorstmann (2020-07-08 16:40 UTC)

<p>Hello,</p>
<p>I’m using Slicer to segment single slices (not all) of a biological microCT sample. Unfortunately, after a while, I guess when the segmentation has reached a certain size, Slicer crashes with the error: “slicerApp-real.exe has stopped working”. I noticed that this error only occurs, if I have the segmented slices plotted in 3D. When I do the segmentation without having activated “show 3D” in Segment editor, I do not face this issue. Furthermore, if I later on try to activate “Show 3D”, slicer crashes immediately most of the times.</p>
<p>Also when I load the segmentation without a stack, slicer crashes upon “show 3D”. I faced this issue on two machines, both with the latest slicer version installed and quite a lot of RAM (64 GB), furthermore, I have another segmentation of that size, that also elicits the same behaviour. Therefore I suspect it is independent of the machine, probably dependent on the files, but these have been fully created in Slicer. The final segmentation (XYZ.seg.nrrd) is about 11 MB. It comprises a segmentation on about 50 of 2388 slices, so on average every 40th to 50th slice is labeled with 2 Segments. If it helps, I can send or upload one of the segmentations that cause the error.<br>
In the following the log file of the session in which I loaded the segmentation and slicer crashed upon show3D in segment editor.</p>
<p>Many thanks for your work on slicer so far and thanks in advance for your help.<br>
Martin</p>
<p>[DEBUG][Qt] 08.07.2020 17:05:55 [] (unknown:0) - Session start time …: 2020-07-08 17:05:55<br>
[DEBUG][Qt] 08.07.2020 17:05:55 [] (unknown:0) - Slicer version …: 4.10.2 (revision 28257) win-amd64 - installed release<br>
[DEBUG][Qt] 08.07.2020 17:05:55 [] (unknown:0) - Operating system …: Windows /  Professional /  (Build 9200) - 64-bit<br>
[DEBUG][Qt] 08.07.2020 17:05:55 [] (unknown:0) - Memory …: 65495 MB physical, 76759 MB virtual<br>
[DEBUG][Qt] 08.07.2020 17:05:55 [] (unknown:0) - CPU …: GenuineIntel , 8 cores, 8 logical processors<br>
[DEBUG][Qt] 08.07.2020 17:05:55 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 08.07.2020 17:05:55 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 08.07.2020 17:05:55 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 08.07.2020 17:05:55 [] (unknown:0) - Additional module paths …: (none)<br>
[DEBUG][Python] 08.07.2020 17:06:00 [Python] (C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 08.07.2020 17:06:01 [Python] (C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 08.07.2020 17:06:01 [Python] (C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 08.07.2020 17:06:01 [] (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 08.07.2020 17:09:00 [] (unknown:0) - “Segmentation” Reader has successfully read the file “G:/xxxxxx/xxxxx/xxxxx/xxxx/xxxxx/200707/Segmentation_200707_1716.seg.nrrd” “[35.60s]”<br>
[DEBUG][Qt] 08.07.2020 17:09:34 [] (unknown:0) - Switch to module:  “SegmentEditor”</p>

---

## Post #2 by @lassoan (2020-07-08 16:44 UTC)

<p>Please try the latest Slicer Preview Release has errors, too. If yes, then please share the segmentation file so that we can debug.</p>

---

## Post #3 by @MartinHorstmann (2020-07-09 06:27 UTC)

<p>Installing and using the latest Preview release totally solved that issue. Thanks for your help! And sorry for bothering you with that. I could have tried that myself…</p>

---
