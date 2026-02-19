---
topic_id: 26605
title: "Dicom Not Loading"
date: 2022-12-06
url: https://discourse.slicer.org/t/26605
---

# DICOM not loading 

**Topic ID**: 26605
**Date**: 2022-12-06
**URL**: https://discourse.slicer.org/t/dicom-not-loading/26605

---

## Post #1 by @Rox_24 (2022-12-06 15:15 UTC)

<p>Hi, Slicer will not let us load new dicom and if it does nothing shows on the dicom information side! The below debug message was brought up! Please can you advise on how we can reset the slicer to get it working again!</p>
<pre><code class="lang-auto">[DEBUG][Qt] 06.12.2022 10:21:33 [] (unknown:0) - Session start time .......: 2022-12-06 10:21:33
[DEBUG][Qt] 06.12.2022 10:21:33 [] (unknown:0) - Slicer version ...........: 4.8.1 (revision 26813) win-amd64 - installed
[DEBUG][Qt] 06.12.2022 10:21:33 [] (unknown:0) - Operating system .........: Windows /  Professional /  (Build 9200) - 64-bit
[DEBUG][Qt] 06.12.2022 10:21:33 [] (unknown:0) - Memory ...................: 65370 MB physical, 80370 MB virtual
[DEBUG][Qt] 06.12.2022 10:21:33 [] (unknown:0) - CPU ......................: GenuineIntel , 12 cores, 16 logical processors
[DEBUG][Qt] 06.12.2022 10:21:33 [] (unknown:0) - Developer mode enabled ...: no
[DEBUG][Qt] 06.12.2022 10:21:33 [] (unknown:0) - Prefer executable CLI ....: yes
[DEBUG][Qt] 06.12.2022 10:21:33 [] (unknown:0) - Additional module paths ..: (none)
[DEBUG][Python] 06.12.2022 10:21:49 [Python] (T:\Selective Documents\Common Documents\AA PRECISE\SOFTWARE\Slicer-4.8.1-win-amd64\lib\Python\Lib\site-packages\git\cmd.py:719) - Popen(%s, cwd=%s, universal_newlines=%s, shell=%s)
[DEBUG][Python] 06.12.2022 10:21:51 [Python] (T:\Selective Documents\Common Documents\AA PRECISE\SOFTWARE\Slicer-4.8.1-win-amd64\lib\Python\Lib\site-packages\git\cmd.py:719) - Popen(%s, cwd=%s, universal_newlines=%s, shell=%s)
[DEBUG][Python] 06.12.2022 10:22:04 [Python] (T:\Selective Documents\Common Documents\AA PRECISE\SOFTWARE\Slicer-4.8.1-win-amd64\lib\Slicer-4.8\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 06.12.2022 10:22:07 [Python] (T:\Selective Documents\Common Documents\AA PRECISE\SOFTWARE\Slicer-4.8.1-win-amd64\lib\Slicer-4.8\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 06.12.2022 10:22:07 [Python] (T:\Selective Documents\Common Documents\AA PRECISE\SOFTWARE\Slicer-4.8.1-win-amd64\lib\Slicer-4.8\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 06.12.2022 10:21:34 [] (unknown:0) - Number of registered modules: 135
[DEBUG][Qt] 06.12.2022 10:21:56 [] (unknown:0) - Number of instantiated modules: 135
[DEBUG][Qt] 06.12.2022 10:22:07 [] (unknown:0) - Number of loaded modules: 135
[DEBUG][Qt] 06.12.2022 10:22:07 [] (unknown:0) - Switch to module:  "Welcome"
[DEBUG][Qt] 06.12.2022 10:22:16 [] (unknown:0) - Switch to module:  "DICOM"
[INFO][Stream] 06.12.2022 10:22:21 [] (unknown:0) - selected row 0
[INFO][Stream] 06.12.2022 10:22:21 [] (unknown:0) - Past Week: NON CONTRAST for (patient-name-0-redacted)
[INFO][Stream] 06.12.2022 10:22:22 [] (unknown:0) - selected row 0
[INFO][Stream] 06.12.2022 10:22:22 [] (unknown:0) - Past Week: NON CONTRAST for (patient-name-0-redacted)
[INFO][Stream] 06.12.2022 10:22:23 [] (unknown:0) - selected row 0
[INFO][Stream] 06.12.2022 10:22:23 [] (unknown:0) - Past Week: NON CONTRAST for (patient-name-0-redacted)
[INFO][Stream] 06.12.2022 10:22:23 [] (unknown:0) - selected row 0
[INFO][Stream] 06.12.2022 10:22:23 [] (unknown:0) - Past Week: NON CONTRAST for (patient-name-0-redacted)
[INFO][Stream] 06.12.2022 10:22:23 [] (unknown:0) - selected row 0
[INFO][Stream] 06.12.2022 10:22:23 [] (unknown:0) - Past Week: NON CONTRAST for (patient-name-0-redacted)
[INFO][Stream] 06.12.2022 10:22:24 [] (unknown:0) - selected row 0
[INFO][Stream] 06.12.2022 10:22:24 [] (unknown:0) - Past Week: NON CONTRAST for (patient-name-0-redacted)
[INFO][Stream] 06.12.2022 10:22:27 [] (unknown:0) - selected row 0
[INFO][Stream] 06.12.2022 10:22:27 [] (unknown:0) - Past Week: NON CONTRAST for (patient-name-0-redacted)
[INFO][Stream] 06.12.2022 10:22:35 [] (unknown:0) - selected row 4
[INFO][Stream] 06.12.2022 10:22:35 [] (unknown:0) - Past Month: Facial Bones 1mm Bone 3D for (patient-name-1-redacted)
[INFO][Stream] 06.12.2022 10:22:37 [] (unknown:0) - selected row 2
[INFO][Stream] 06.12.2022 10:22:37 [] (unknown:0) - Past Week: AXIAL for (patient-name-2-redacted)
[INFO][Stream] 06.12.2022 10:22:38 [] (unknown:0) - selected row 1
[INFO][Stream] 06.12.2022 10:22:38 [] (unknown:0) - Past Week: Bone 0.5 for (patient-name-3-redacted)
[INFO][Stream] 06.12.2022 10:22:39 [] (unknown:0) - selected row 0
[INFO][Stream] 06.12.2022 10:22:39 [] (unknown:0) - Past Week: NON CONTRAST for (patient-name-0-redacted)
[INFO][Stream] 06.12.2022 10:22:41 [] (unknown:0) - selected row 4
[INFO][Stream] 06.12.2022 10:22:41 [] (unknown:0) - Past Month: Facial Bones 1mm Bone 3D for (patient-name-1-redacted)
[INFO][Stream] 06.12.2022 10:22:42 [] (unknown:0) - selected row 3
[INFO][Stream] 06.12.2022 10:22:42 [] (unknown:0) - Past Week: 0.5 x 0.5 MAC for (patient-name-4-redacted)
[INFO][Stream] 06.12.2022 10:29:02 [] (unknown:0) - starting storescp process
[INFO][Stream] 06.12.2022 10:29:02 [] (unknown:0) - (u'Starting T:/Selective Documents/Common Documents/AA PRECISE/SOFTWARE/Slicer-4.8.1-win-amd64/bin\\storescp.exe with ', ['11112', '--accept-all', '--output-directory', u'\\\\sspdc.ssjhb.local\\redirected folders$\\roxanne\\Documents\\SlicerDICOMDatabase/incoming', '--exec-sync', '--exec-on-reception', u'T:/Selective Documents/Common Documents/AA PRECISE/SOFTWARE/Slicer-4.8.1-win-amd64/bin\\dcmdump.exe --load-short --print-short --print-filename --search PatientName "\\\\sspdc.ssjhb.local\\redirected folders$\\roxanne\\Documents\\SlicerDICOMDatabase/incoming/#f"'])
[INFO][Stream] 06.12.2022 10:29:02 [] (unknown:0) - process T:/Selective Documents/Common Documents/AA PRECISE/SOFTWARE/Slicer-4.8.1-win-amd64/bin\storescp.exe now in state Starting
[INFO][Stream] 06.12.2022 10:29:02 [] (unknown:0) - process T:/Selective Documents/Common Documents/AA PRECISE/SOFTWARE/Slicer-4.8.1-win-amd64/bin\storescp.exe now in state Running
[INFO][Stream] 06.12.2022 10:29:48 [] (unknown:0) - selected row 0
[INFO][Stream] 06.12.2022 10:29:48 [] (unknown:0) - Past Week: NON CONTRAST for (patient-name-0-redacted)
[INFO][Stream] 06.12.2022 10:29:50 [] (unknown:0) - selected row 0
[INFO][Stream] 06.12.2022 10:29:50 [] (unknown:0) - Past Week: NON CONTRAST for (patient-name-0-redacted)
[INFO][Stream] 06.12.2022 10:29:51 [] (unknown:0) - selected row 0
[INFO][Stream] 06.12.2022 10:29:51 [] (unknown:0) - Past Week: NON CONTRAST for (patient-name-0-redacted)
[INFO][Stream] 06.12.2022 10:29:51 [] (unknown:0) - selected row 0
[INFO][Stream] 06.12.2022 10:29:51 [] (unknown:0) - Past Week: NON CONTRAST for (patient-name-0-redacted)
[INFO][Stream] 06.12.2022 10:30:01 [] (unknown:0) - selected row 1
[INFO][Stream] 06.12.2022 10:30:01 [] (unknown:0) - Past Week: Bone 0.5 for (patient-name-3-redacted)
[INFO][Stream] 06.12.2022 10:30:04 [] (unknown:0) - stopping DICOM process
[WARNING][Qt] 06.12.2022 10:30:04 [] (unknown:0) - QProcess: Destroyed while process is still running.
[INFO][Stream] 06.12.2022 10:30:04 [] (unknown:0) - process T:/Selective Documents/Common Documents/AA PRECISE/SOFTWARE/Slicer-4.8.1-win-amd64/bin\storescp.exe now in state NotRunning
[CRITICAL][Stream] 06.12.2022 10:30:04 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 06.12.2022 10:30:04 [] (unknown:0) -   File "T:/Selective Documents/Common Documents/AA PRECISE/SOFTWARE/Slicer-4.8.1-win-amd64/lib/Slicer-4.8/qt-scripted-modules/DICOM.py", line 395, in onToggleListener
[CRITICAL][Stream] 06.12.2022 10:30:04 [] (unknown:0) -     del slicer.dicomListener
[CRITICAL][Stream] 06.12.2022 10:30:04 [] (unknown:0) - AttributeError: dicomListener
[INFO][Stream] 06.12.2022 10:30:22 [] (unknown:0) - selected row 4
[INFO][Stream] 06.12.2022 10:30:22 [] (unknown:0) - Past Month: Facial Bones 1mm Bone 3D for (patient-name-1-redacted)
[INFO][Stream] 06.12.2022 10:30:22 [] (unknown:0) - selected row 4
[INFO][Stream] 06.12.2022 10:30:22 [] (unknown:0) - Past Month: Facial Bones 1mm Bone 3D for (patient-name-1-redacted)
[DEBUG][Qt] 06.12.2022 10:30:27 [] (unknown:0) - Switch to module:  "SampleData"
[DEBUG][Qt] 06.12.2022 10:30:35 [] (unknown:0) - Switch to module:  "DICOM"
[INFO][Stream] 06.12.2022 10:30:41 [] (unknown:0) - selected row 0
[INFO][Stream] 06.12.2022 10:30:41 [] (unknown:0) - Past Week: NON CONTRAST for (patient-name-0-redacted)
[INFO][Stream] 06.12.2022 10:30:42 [] (unknown:0) - selected row 0
[INFO][Stream] 06.12.2022 10:30:42 [] (unknown:0) - Past Week: NON CONTRAST for (patient-name-0-redacted)
[INFO][Stream] 06.12.2022 10:30:43 [] (unknown:0) - selected row 4
[INFO][Stream] 06.12.2022 10:30:43 [] (unknown:0) - Past Month: Facial Bones 1mm Bone 3D for (patient-name-1-redacted)
[INFO][Stream] 06.12.2022 10:30:43 [] (unknown:0) - selected row 3
[INFO][Stream] 06.12.2022 10:30:43 [] (unknown:0) - Past Week: 0.5 x 0.5 MAC for (patient-name-4-redacted)
[INFO][Stream] 06.12.2022 10:30:45 [] (unknown:0) - selected row 3
[INFO][Stream] 06.12.2022 10:30:45 [] (unknown:0) - Past Week: 0.5 x 0.5 MAC for (patient-name-4-redacted)
[INFO][Stream] 06.12.2022 10:30:59 [] (unknown:0) - selected row 1
[INFO][Stream] 06.12.2022 10:30:59 [] (unknown:0) - Past Week: Bone 0.5 for (patient-name-3-redacted)
[WARNING][Qt] 06.12.2022 10:31:14 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile
[INFO][Stream] 06.12.2022 10:56:21 [] (unknown:0) - selected row 0
[INFO][Stream] 06.12.2022 10:56:21 [] (unknown:0) - Past Week: NON CONTRAST for (patient-name-0-redacted)
[INFO][Stream] 06.12.2022 10:56:22 [] (unknown:0) - selected row 0
[INFO][Stream] 06.12.2022 10:56:22 [] (unknown:0) - Past Week: NON CONTRAST for (patient-name-0-redacted)
[INFO][Stream] 06.12.2022 10:56:23 [] (unknown:0) - selected row 0
[INFO][Stream] 06.12.2022 10:56:23 [] (unknown:0) - Past Week: NON CONTRAST for (patient-name-0-redacted)
[INFO][Stream] 06.12.2022 10:56:23 [] (unknown:0) - selected row 0
[INFO][Stream] 06.12.2022 10:56:23 [] (unknown:0) - Past Week: NON CONTRAST for (patient-name-0-redacted)
[INFO][Stream] 06.12.2022 10:56:23 [] (unknown:0) - selected row 0
[INFO][Stream] 06.12.2022 10:56:23 [] (unknown:0) - Past Week: NON CONTRAST for (patient-name-0-redacted)
[INFO][Stream] 06.12.2022 10:56:24 [] (unknown:0) - selected row 0
[INFO][Stream] 06.12.2022 10:56:24 [] (unknown:0) - Past Week: NON CONTRAST for (patient-name-0-redacted)
[INFO][Stream] 06.12.2022 10:56:24 [] (unknown:0) - selected row 0
[INFO][Stream] 06.12.2022 10:56:24 [] (unknown:0) - Past Week: NON CONTRAST for (patient-name-0-redacted)
[INFO][Stream] 06.12.2022 10:57:17 [] (unknown:0) - selected row 2
[INFO][Stream] 06.12.2022 10:57:17 [] (unknown:0) - Past Week: AXIAL for (patient-name-2-redacted)
[INFO][Stream] 06.12.2022 10:57:17 [] (unknown:0) - selected row 2
[INFO][Stream] 06.12.2022 10:57:17 [] (unknown:0) - Past Week: AXIAL for (patient-name-2-redacted)
[INFO][Stream] 06.12.2022 10:57:18 [] (unknown:0) - selected row 2
[INFO][Stream] 06.12.2022 10:57:18 [] (unknown:0) - Past Week: AXIAL for (patient-name-2-redacted)
[INFO][Stream] 06.12.2022 10:57:18 [] (unknown:0) - selected row 2
[INFO][Stream] 06.12.2022 10:57:18 [] (unknown:0) - Past Week: AXIAL for (patient-name-2-redacted)
[INFO][Stream] 06.12.2022 10:57:18 [] (unknown:0) - selected row 2
[INFO][Stream] 06.12.2022 10:57:18 [] (unknown:0) - Past Week: AXIAL for (patient-name-2-redacted)
[INFO][Stream] 06.12.2022 10:57:19 [] (unknown:0) - selected row 2
[INFO][Stream] 06.12.2022 10:57:19 [] (unknown:0) - Past Week: AXIAL for (patient-name-2-redacted)
[INFO][Stream] 06.12.2022 10:57:19 [] (unknown:0) - selected row 2
[INFO][Stream] 06.12.2022 10:57:19 [] (unknown:0) - Past Week: AXIAL for (patient-name-2-redacted)
[INFO][Stream] 06.12.2022 10:57:19 [] (unknown:0) - selected row 2
[INFO][Stream] 06.12.2022 10:57:19 [] (unknown:0) - Past Week: AXIAL for (patient-name-2-redacted)
[INFO][Stream] 06.12.2022 10:57:30 [] (unknown:0) - selected row 0
[INFO][Stream] 06.12.2022 10:57:30 [] (unknown:0) - Past Week: NON CONTRAST for (patient-name-0-redacted)
</code></pre>

---

## Post #2 by @lassoan (2022-12-06 16:19 UTC)

<p>Please try with the current version of Slicer. If you run into problems then you can follow <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#troubleshooting">these instructions</a>.</p>

---
