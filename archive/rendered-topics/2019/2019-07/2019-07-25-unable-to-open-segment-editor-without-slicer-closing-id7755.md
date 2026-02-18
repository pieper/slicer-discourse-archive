# Unable to open segment editor without slicer closing

**Topic ID**: 7755
**Date**: 2019-07-25
**URL**: https://discourse.slicer.org/t/unable-to-open-segment-editor-without-slicer-closing/7755

---

## Post #1 by @Andrew_Kanawati (2019-07-25 14:27 UTC)

<p>Problem report for Slicer 4.10.2 win-amd64:  Slicer keeps closing when I try to edit segment editor.</p>
<p>[DEBUG][Qt] 25.07.2019 10:17:00 [] (unknown:0) - Session start time …: 2019-07-25 10:17:00<br>
[DEBUG][Qt] 25.07.2019 10:17:00 [] (unknown:0) - Slicer version …: 4.10.2 (revision 28257) win-amd64 - installed release<br>
[DEBUG][Qt] 25.07.2019 10:17:00 [] (unknown:0) - Operating system …: Windows /  Personal /  (Build 9200) - 64-bit<br>
[DEBUG][Qt] 25.07.2019 10:17:00 [] (unknown:0) - Memory …: 16276 MB physical, 18708 MB virtual<br>
[DEBUG][Qt] 25.07.2019 10:17:00 [] (unknown:0) - CPU …: GenuineIntel , 12 cores, 12 logical processors<br>
[DEBUG][Qt] 25.07.2019 10:17:00 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 25.07.2019 10:17:00 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 25.07.2019 10:17:00 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 25.07.2019 10:17:00 [] (unknown:0) - Additional module paths …: C:/Users/andre/AppData/Roaming/NA-MIC/Extensions-28257/SegmentEditorExtraEffects/lib/Slicer-4.10/qt-scripted-modules, C:/Users/andre/AppData/Roaming/NA-MIC/Extensions-28257/MarkupsToModel/lib/Slicer-4.10/qt-loadable-modules, C:/Users/andre/AppData/Roaming/NA-MIC/Extensions-28257/AnomalousFiltersExtension/lib/Slicer-4.10/cli-modules, C:/Users/andre/AppData/Roaming/NA-MIC/Extensions-28257/PedicleScrewSimulator/lib/Slicer-4.10/qt-scripted-modules, C:/Users/andre/AppData/Roaming/NA-MIC/Extensions-28257/SegmentRegistration/lib/Slicer-4.10/qt-scripted-modules, C:/Users/andre/AppData/Roaming/NA-MIC/Extensions-28257/SlicerProstate/lib/Slicer-4.10/cli-modules, C:/Users/andre/AppData/Roaming/NA-MIC/Extensions-28257/SlicerProstate/lib/Slicer-4.10/qt-scripted-modules, C:/Users/andre/AppData/Roaming/NA-MIC/Extensions-28257/SlicerRT/lib/Slicer-4.10/cli-modules, C:/Users/andre/AppData/Roaming/NA-MIC/Extensions-28257/SlicerRT/lib/Slicer-4.10/qt-loadable-modules, C:/Users/andre/AppData/Roaming/NA-MIC/Extensions-28257/SlicerRT/lib/Slicer-4.10/qt-scripted-modules, C:/Users/andre/AppData/Roaming/NA-MIC/Extensions-28257/ModelToModelDistance/lib/Slicer-4.10/cli-modules<br>
[DEBUG][Python] 25.07.2019 10:17:02 [Python] (C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 25.07.2019 10:17:03 [Python] (C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 25.07.2019 10:17:03 [Python] (C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 25.07.2019 10:17:03 [] (unknown:0) - Switch to module:  “Welcome”</p>

---

## Post #2 by @cpinter (2019-07-25 14:29 UTC)

<p>Hi! Thanks for the report and the log. Unfortunately the log does not contain any clues. Does this occur even if you try to open Segment Editor immediately after starting Slicer? Do you have any extensions installed? What happens if you delete Slicer.ini and try again?</p>

---

## Post #3 by @Andrew_Kanawati (2019-07-29 22:42 UTC)

<p>Everything actually works fine when I open segment editor first before loading data. Thank you very much</p>

---

## Post #4 by @cpinter (2019-07-30 12:02 UTC)

<p>This shouldn’t be a limiting factor. Could you help us get to the bottom of this?</p>
<p>What did you try to do?<br>
What happened instead?</p>

---

## Post #5 by @Andrew_Kanawati (2019-09-11 23:33 UTC)

<p>Hi<br>
This problem is occurring again for me<br>
Slicer is actually closing whenever I try opening a file now</p>
<p>[DEBUG][Qt] 11.09.2019 19:22:34 [] (unknown:0) - Session start time …: 2019-09-11 19:22:34<br>
[DEBUG][Qt] 11.09.2019 19:22:34 [] (unknown:0) - Slicer version …: 4.10.2 (revision 28257) macosx-amd64 - installed release<br>
[DEBUG][Qt] 11.09.2019 19:22:34 [] (unknown:0) - Operating system …: Mac OS X / 10.14.4 / 18E224 - 64-bit<br>
[DEBUG][Qt] 11.09.2019 19:22:34 [] (unknown:0) - Memory …: 32768 MB physical, 0 MB virtual<br>
[DEBUG][Qt] 11.09.2019 19:22:34 [] (unknown:0) - CPU …: GenuineIntel Intel® Xeon® W-2140B CPU @ 3.20GHz, 8 cores, 16 logical processors<br>
[DEBUG][Qt] 11.09.2019 19:22:34 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, Sequential threading<br>
[DEBUG][Qt] 11.09.2019 19:22:34 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 11.09.2019 19:22:34 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 11.09.2019 19:22:34 [] (unknown:0) - Additional module paths …: /Applications/Slicer.app/Contents/Extensions-28257/VolumeClip/lib/Slicer-4.10/qt-scripted-modules, /Applications/Slicer.app/Contents/Extensions-28257/SegmentEditorExtraEffects/lib/Slicer-4.10/qt-scripted-modules, /Applications/Slicer.app/Contents/Extensions-28257/MarkupsToModel/lib/Slicer-4.10/qt-loadable-modules, /Applications/Slicer.app/Contents/Extensions-28257/AnomalousFiltersExtension/lib/Slicer-4.10/cli-modules, /Applications/Slicer.app/Contents/Extensions-28257/ModelToModelDistance/lib/Slicer-4.10/cli-modules, /Applications/Slicer.app/Contents/Extensions-28257/SlicerProstate/lib/Slicer-4.10/cli-modules, /Applications/Slicer.app/Contents/Extensions-28257/SlicerProstate/lib/Slicer-4.10/qt-scripted-modules, /Applications/Slicer.app/Contents/Extensions-28257/SlicerRT/lib/Slicer-4.10/cli-modules, /Applications/Slicer.app/Contents/Extensions-28257/SlicerRT/lib/Slicer-4.10/qt-loadable-modules, /Applications/Slicer.app/Contents/Extensions-28257/SlicerRT/lib/Slicer-4.10/qt-scripted-modules, /Applications/Slicer.app/Contents/Extensions-28257/PedicleScrewSimulator/lib/Slicer-4.10/qt-scripted-modules<br>
[DEBUG][Python] 11.09.2019 19:22:38 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.10/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 11.09.2019 19:22:41 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.10/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 11.09.2019 19:22:41 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.10/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 11.09.2019 19:22:41 [] (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 11.09.2019 19:22:46 [] (unknown:0) - Switch to module:  “SegmentEditor”<br>
[DEBUG][Qt] 11.09.2019 19:26:39 [] (unknown:0) - Switch to module:  “Welcome”</p>

---

## Post #6 by @jamesobutler (2019-09-11 23:43 UTC)

<p><a class="mention" href="/u/andrew_kanawati">@Andrew_Kanawati</a> It appears that you have several extensions installed. One option of debugging is to see if uninstalling extensions changes the current behavior. Try uninstalling all extensions and retry your action. It it solves the issue than you will want to narrow it down to the problem extension.</p>
<p>If not an extension issue, second option could be attempting to load the same volume using the latest Slicer Preview instead of Slicer 4.10.2 which you are currently using.</p>

---

## Post #7 by @Andrew_Kanawati (2019-09-11 23:44 UTC)

<p>I’ll try to uninstall the extensions, but I’ve had all of this installed on another computer without any trouble in the past</p>

---

## Post #8 by @jamesobutler (2019-09-11 23:50 UTC)

<p>If you used the same exact version of Slicer and the same exact versions of the extensions in the past then it could be a problem specific to the file, but try these debugging actions too.</p>

---

## Post #9 by @Andrew_Kanawati (2019-09-12 01:44 UTC)

<p>Thanks so much<br>
It must be the files</p>

---
