---
topic_id: 14396
title: "Mac Osx 10 15 7 Cant Load Volumes"
date: 2020-11-02
url: https://discourse.slicer.org/t/14396
---

# Mac osX 10.15.7. Can't load volumes

**Topic ID**: 14396
**Date**: 2020-11-02
**URL**: https://discourse.slicer.org/t/mac-osx-10-15-7-cant-load-volumes/14396

---

## Post #1 by @axlander (2020-11-02 22:50 UTC)

<p>I downloaded and installed  slicer 4.11 in my Applications folder.</p>
<p>Slicer starts normally but I can’t load volumes (.nii) or load dcm files. After starting, the following warnings appear.</p>
<p>When loading module  “DICOM” , the dependency “SubjectHierarchy” failed to be loaded.<br>
When loading module  “DICOM” , the dependency “SubjectHierarchy” failed to be loaded.<br>
When loading module  “DICOMPatcher” , the dependency “DICOM” failed to be loaded.<br>
When loading module  “MarkupsWidgetsSelfTest” , the dependency “Markups” failed to be loaded.<br>
When loading module  “MultiVolumeImporter” , the dependency “MultiVolumeExplorer” failed to be loaded.<br>
When loading module  “NeurosurgicalPlanningTutorialMarkupsSelfTest” , the dependency “Segmentations” failed to be loaded.<br>
When loading module  “PlotsSelfTest” , the dependency “Plots” failed to be loaded.<br>
When loading module  “SegmentEditor” , the dependency “Segmentations” failed to be loaded.<br>
When loading module  “SegmentStatistics” , the dependency “SubjectHierarchy” failed to be loaded.<br>
When loading module  “SubjectHierarchyCorePluginsSelfTest” , the dependency “SubjectHierarchy” failed to be loaded.<br>
When loading module  “SubjectHierarchyGenericSelfTest” , the dependency “SubjectHierarchy” failed to be loaded.<br>
When loading module  “TablesSelfTest” , the dependency “Tables” failed to be loaded.</p>
<p>I read the warning, “You cannot install extensions into the read-only volume so you must copy before installing extensions”. I was unsure if that meant I had to load extensions separately, and how to do that.</p>
<p>Thanks for any help!</p>

---

## Post #2 by @lassoan (2020-11-03 16:01 UTC)

<p>Are you using latest stable version (Slicer-4.11.20200930)?</p>

---

## Post #3 by @axlander (2020-11-03 17:11 UTC)

<p>Yes - 4.11.20200930. I tried the preview release as well but had similar errors.</p>

---

## Post #4 by @lassoan (2020-11-03 23:44 UTC)

<p>Could you upload the application log (menu: Help/Report a bug) somewhere (dropbox/onedrive/gdrive/…) and post the link here? Thanks.</p>

---

## Post #5 by @axlander (2020-11-04 15:35 UTC)

<p>Andras - Thanks for your help. The log file is pretty short so I hope you don’t mind that I post it here (below).</p>
<p>[DEBUG][Qt] 04.11.2020 07:08:03 [] (unknown:0) - Session start time …: 2020-11-04 07:08:03<br>
[DEBUG][Qt] 04.11.2020 07:08:03 [] (unknown:0) - Slicer version …: 4.11.20200930 (revision 29402 / 002be18) macosx-amd64 - installed release<br>
[DEBUG][Qt] 04.11.2020 07:08:03 [] (unknown:0) - Operating system …: Mac OS X / 10.15.7 / 19H2 - 64-bit<br>
[DEBUG][Qt] 04.11.2020 07:08:03 [] (unknown:0) - Memory …: 16384 MB physical, 1024 MB virtual<br>
[DEBUG][Qt] 04.11.2020 07:08:03 [] (unknown:0) - CPU …: GenuineIntel Intel® Core™ i5-9600K CPU @ 3.70GHz, 6 cores, 6 logical processors<br>
[DEBUG][Qt] 04.11.2020 07:08:03 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, Sequential threading<br>
[DEBUG][Qt] 04.11.2020 07:08:03 [] (unknown:0) - Qt configuration …: version 5.15.1, with SSL, requested OpenGL 3.2 (core profile)<br>
[DEBUG][Qt] 04.11.2020 07:08:03 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 04.11.2020 07:08:03 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 04.11.2020 07:08:03 [] (unknown:0) - Application path …: /Applications/Slicer.app/Contents/MacOS<br>
[DEBUG][Qt] 04.11.2020 07:08:03 [] (unknown:0) - Additional module paths …: /Applications/Slicer.app/Contents/Extensions-29402/DCMQI/lib/Slicer-4.11/cli-modules<br>
[DEBUG][Python] 04.11.2020 07:08:03 [Python] (/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/pydicom/datadict.py:432) - Reversing DICOM dictionary so can look up tag from a keyword…<br>
[WARNING][Qt] 04.11.2020 07:08:04 [] (unknown:0) - When loading module  “DICOM” , the dependency “SubjectHierarchy” failed to be loaded.<br>
[WARNING][Qt] 04.11.2020 07:08:04 [] (unknown:0) - When loading module  “DICOM” , the dependency “SubjectHierarchy” failed to be loaded.<br>
[WARNING][Qt] 04.11.2020 07:08:04 [] (unknown:0) - When loading module  “DICOMPatcher” , the dependency “DICOM” failed to be loaded.<br>
[WARNING][Qt] 04.11.2020 07:08:04 [] (unknown:0) - When loading module  “MarkupsWidgetsSelfTest” , the dependency “Markups” failed to be loaded.<br>
[WARNING][Qt] 04.11.2020 07:08:04 [] (unknown:0) - When loading module  “MultiVolumeImporter” , the dependency “MultiVolumeExplorer” failed to be loaded.<br>
[WARNING][Qt] 04.11.2020 07:08:04 [] (unknown:0) - When loading module  “NeurosurgicalPlanningTutorialMarkupsSelfTest” , the dependency “Segmentations” failed to be loaded.<br>
[WARNING][Qt] 04.11.2020 07:08:04 [] (unknown:0) - When loading module  “PlotsSelfTest” , the dependency “Plots” failed to be loaded.<br>
[WARNING][Qt] 04.11.2020 07:08:04 [] (unknown:0) - When loading module  “SegmentEditor” , the dependency “Segmentations” failed to be loaded.<br>
[WARNING][Qt] 04.11.2020 07:08:04 [] (unknown:0) - When loading module  “SegmentStatistics” , the dependency “SubjectHierarchy” failed to be loaded.<br>
[WARNING][Qt] 04.11.2020 07:08:04 [] (unknown:0) - When loading module  “SubjectHierarchyCorePluginsSelfTest” , the dependency “SubjectHierarchy” failed to be loaded.<br>
[WARNING][Qt] 04.11.2020 07:08:04 [] (unknown:0) - When loading module  “SubjectHierarchyGenericSelfTest” , the dependency “SubjectHierarchy” failed to be loaded.<br>
[WARNING][Qt] 04.11.2020 07:08:04 [] (unknown:0) - When loading module  “TablesSelfTest” , the dependency “Tables” failed to be loaded.<br>
[WARNING][Python] 04.11.2020 07:08:04 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/DataProbeLib/SliceViewAnnotations.py:26) - SliceAnnotations: Disable features relying on vtkPVScalarBarActor<br>
[CRITICAL][Stream] 04.11.2020 07:08:04 [] (unknown:0) - SliceAnnotations: Disable features relying on vtkPVScalarBarActor</p>

---

## Post #6 by @lassoan (2020-11-04 19:35 UTC)

<p>Could you please try deleting Slicer completely, then reinstalling it, without installing any extensions?</p>

---

## Post #7 by @axlander (2020-11-04 22:36 UTC)

<p>Hi Andras. Your comment made me realize that the .ini files weren’t deleted with the new install. Once I deleted them, it solved the problem. Thanks for your help!</p>

---

## Post #8 by @lassoan (2020-11-04 22:51 UTC)

<p>Great! Thanks for the update.</p>

---
