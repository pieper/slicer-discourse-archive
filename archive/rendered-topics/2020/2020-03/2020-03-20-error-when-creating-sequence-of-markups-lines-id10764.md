---
topic_id: 10764
title: "Error When Creating Sequence Of Markups Lines"
date: 2020-03-20
url: https://discourse.slicer.org/t/10764
---

# Error when creating sequence of markups lines

**Topic ID**: 10764
**Date**: 2020-03-20
**URL**: https://discourse.slicer.org/t/error-when-creating-sequence-of-markups-lines/10764

---

## Post #1 by @Jainey (2020-03-20 15:17 UTC)

<p>Slicer 4.11<br>
Mac OS</p>
<p>Trying to create a sequence (using sequences module) of transform hardened marks ups with lines.<br>
Slicer crashes<br>
Works fine with angles (If I draw an angle on the volume and create multiple angles , harden them on the volume and create a sequence, it plays fine in the browser, Also ok with fidu markers. Moment I select line and do the same slicer crashes<br>
Report as follows- I m zero to programming and python</p>
<p>Thanks a lot<br>
[DEBUG][Qt] 21.03.2020 02:10:49 [] (unknown:0) - Session start time …: 2020-03-21 02:10:49<br>
[DEBUG][Qt] 21.03.2020 02:10:49 [] (unknown:0) - Slicer version …: 4.11.0-2019-12-06 (revision 28668) macosx-amd64 - installed release<br>
[DEBUG][Qt] 21.03.2020 02:10:49 [] (unknown:0) - Operating system …: Mac OS X / 10.15.1 / 19B88 - 64-bit<br>
[DEBUG][Qt] 21.03.2020 02:10:49 [] (unknown:0) - Memory …: 16384 MB physical, 17408 MB virtual<br>
[DEBUG][Qt] 21.03.2020 02:10:49 [] (unknown:0) - CPU …: GenuineIntel Intel® Core™ i9-9880H CPU @ 2.30GHz, 8 cores, 16 logical processors<br>
[DEBUG][Qt] 21.03.2020 02:10:49 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, Sequential threading<br>
[DEBUG][Qt] 21.03.2020 02:10:49 [] (unknown:0) - Qt configuration …: version 5.10.0, with SSL, requested OpenGL 3.2 (core profile)<br>
[DEBUG][Qt] 21.03.2020 02:10:49 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 21.03.2020 02:10:49 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 21.03.2020 02:10:49 [] (unknown:0) - Application path …: /Applications/Slicer 3.app/Contents/MacOS<br>
[DEBUG][Qt] 21.03.2020 02:10:49 [] (unknown:0) - Additional module paths …: /Applications/Slicer 3.app/Contents/Extensions-28668/Sequences/lib/Slicer-4.11/qt-loadable-modules, /Applications/Slicer 3.app/Contents/Extensions-28668/Sequences/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer 3.app/Contents/Extensions-28668/SlicerElastix/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer 3.app/Contents/Extensions-28668/ModelToModelDistance/lib/Slicer-4.11/cli-modules, /Applications/Slicer 3.app/Contents/Extensions-28668/Q3DC/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer 3.app/Contents/Extensions-28668/CMFreg/lib/Slicer-4.11/cli-modules, /Applications/Slicer 3.app/Contents/Extensions-28668/CMFreg/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer 3.app/Contents/Extensions-28668/ShapePopulationViewer/lib/Slicer-4.11/qt-loadable-modules, /Applications/Slicer 3.app/Contents/Extensions-28668/MarkupsToModel/lib/Slicer-4.11/qt-loadable-modules, /Applications/Slicer 3.app/Contents/Extensions-28668/DCMQI/lib/Slicer-4.11/cli-modules, /Applications/Slicer 3.app/Contents/Extensions-28668/SlicerIGT/lib/Slicer-4.11/qt-loadable-modules, /Applications/Slicer 3.app/Contents/Extensions-28668/SlicerIGT/lib/Slicer-4.11/qt-scripted-modules, /Applications/Slicer 3.app/Contents/Extensions-28668/SlicerIGSIO/lib/Slicer-4.11/qt-loadable-modules, /Applications/Slicer 3.app/Contents/Extensions-28668/SlicerOpenIGTLink/lib/Slicer-4.11/qt-loadable-modules, /Applications/Slicer 3.app/Contents/Extensions-28668/SlicerOpenIGTLink/lib/Slicer-4.11/qt-scripted-modules<br>
[DEBUG][Python] 21.03.2020 02:10:50 [Python] (/Applications/Slicer 3.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 21.03.2020 02:10:53 [Python] (/Applications/Slicer 3.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 21.03.2020 02:10:53 [Python] (/Applications/Slicer 3.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 21.03.2020 02:10:54 [] (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Python] 21.03.2020 02:11:00 [Python] (/Applications/Slicer 3.app/Contents/lib/Slicer-4.11/qt-scripted-modules/DICOMLib/DICOMProcesses.py:171) - Starting storescp process<br>
[DEBUG][Python] 21.03.2020 02:11:00 [Python] (/Applications/Slicer 3.app/Contents/lib/Slicer-4.11/qt-scripted-modules/DICOMLib/DICOMProcesses.py:68) - ('Starting /Applications/Slicer 3.app/Contents/bin/storescp with ', [‘11112’, ‘–accept-all’, ‘–output-directory’, ‘/Users/mel/Documents/sl/incoming’, ‘–exec-sync’, ‘–exec-on-reception’, ‘/Applications/Slicer 3.app/Contents/bin/dcmdump --load-short --print-short --print-filename --search PatientName “/Users/mel/Documents/sl/incoming/<span class="hashtag">#f</span>”’])<br>
[DEBUG][Python] 21.03.2020 02:11:00 [Python] (/Applications/Slicer 3.app/Contents/lib/Slicer-4.11/qt-scripted-modules/DICOMLib/DICOMProcesses.py:72) - Process /Applications/Slicer 3.app/Contents/bin/storescp now in state Starting<br>
[INFO][Python] 21.03.2020 02:11:00 [Python] (/Applications/Slicer 3.app/Contents/lib/Slicer-4.11/qt-scripted-modules/DICOM.py:166) - DICOM C-Store SCP service started at port 11112<br>
[INFO][Stream] 21.03.2020 02:11:00 [] (unknown:0) - DICOM C-Store SCP service started at port 11112<br>
[DEBUG][Python] 21.03.2020 02:11:00 [Python] (/Applications/Slicer 3.app/Contents/lib/Slicer-4.11/qt-scripted-modules/DICOMLib/DICOMProcesses.py:72) - Process /Applications/Slicer 3.app/Contents/bin/storescp now in state Running</p>

---

## Post #2 by @lassoan (2020-03-22 00:47 UTC)

<p>Thanks for reporting this. I could not reproduce the crash. Could you try on a new Slicer installation, only with Sequences extension installed? Could you give step-by-step instructions (which buttons you clicked) or a screen capture video of the crash? Thanks!</p>

---

## Post #3 by @Jainey (2020-03-22 05:15 UTC)

<p>Will do,<br>
Thanks for the reply</p>

---
