---
topic_id: 1774
title: "Cannot Close Contour In Segment Editor Drawing Effect"
date: 2018-01-06
url: https://discourse.slicer.org/t/1774
---

# Cannot close contour in Segment editor drawing effect

**Topic ID**: 1774
**Date**: 2018-01-06
**URL**: https://discourse.slicer.org/t/cannot-close-contour-in-segment-editor-drawing-effect/1774

---

## Post #1 by @MimiPoon (2018-01-06 16:03 UTC)

<p>Problem report for Slicer 4.8.1 macosx-amd64: [please describe expected and actual behavior]<br>
Try to segment a tumor with draw but unable to do it with Enter key and ‘a’ key.</p>
<p>log message as follows:</p>
<p>[DEBUG][Qt] 06.01.2018 07:49:25 [] (unknown:0) - Session start time …: 2018-01-06 07:49:25<br>
[DEBUG][Qt] 06.01.2018 07:49:25 [] (unknown:0) - Slicer version …: 4.8.1 (revision 26813) macosx-amd64 - installed<br>
[DEBUG][Qt] 06.01.2018 07:49:25 [] (unknown:0) - Operating system …: Mac OS X / 10.12.6 / 16G1114 - 64-bit<br>
[DEBUG][Qt] 06.01.2018 07:49:25 [] (unknown:0) - Memory …: 16384 MB physical, 0 MB virtual<br>
[DEBUG][Qt] 06.01.2018 07:49:25 [] (unknown:0) - CPU …: GenuineIntel Intel® Core™ i7-4750HQ CPU @ 2.00GHz, 4 cores, 8 logical processors<br>
[DEBUG][Qt] 06.01.2018 07:49:25 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 06.01.2018 07:49:25 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 06.01.2018 07:49:25 [] (unknown:0) - Additional module paths …: /Applications/Slicer 2.app/Contents/Extensions-26813/SlicerRadiomics/lib/Slicer-4.8/qt-scripted-modules<br>
[DEBUG][Python] 06.01.2018 07:49:29 [Python] (/Applications/Slicer 2.app/Contents/lib/Python/lib/python2.7/site-packages/git/cmd.py:719) - Popen(%s, cwd=%s, universal_newlines=%s, shell=%s)<br>
[DEBUG][Python] 06.01.2018 07:49:29 [Python] (/Applications/Slicer 2.app/Contents/lib/Python/lib/python2.7/site-packages/git/cmd.py:719) - Popen(%s, cwd=%s, universal_newlines=%s, shell=%s)<br>
[INFO][Python] 06.01.2018 07:49:30 [Python] (/Applications/Slicer 2.app/Contents/Extensions-26813/SlicerRadiomics/lib/python2.7/site-packages/radiomics/<strong>init</strong>.py:85) - Enabling C extensions<br>
[DEBUG][Python] 06.01.2018 07:49:30 [Python] (/Applications/Slicer 2.app/Contents/Extensions-26813/SlicerRadiomics/lib/python2.7/site-packages/pykwalify/compat.py:20) - Using yaml library: /Applications/Slicer 2.app/Contents/Extensions-26813/SlicerRadiomics/lib/python2.7/site-packages/yaml/<strong>init</strong>.pyc<br>
[DEBUG][Python] 06.01.2018 07:49:37 [Python] (/Applications/Slicer 2.app/Contents/lib/Slicer-4.8/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 06.01.2018 07:49:38 [Python] (/Applications/Slicer 2.app/Contents/lib/Slicer-4.8/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 06.01.2018 07:49:38 [Python] (/Applications/Slicer 2.app/Contents/lib/Slicer-4.8/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 06.01.2018 07:49:28 [] (unknown:0) - Number of registered modules: 136<br>
[INFO][Stream] 06.01.2018 07:49:30 [] (unknown:0) - Enabling C extensions<br>
[DEBUG][Qt] 06.01.2018 07:49:30 [] (unknown:0) - Number of instantiated modules: 136<br>
[DEBUG][Qt] 06.01.2018 07:49:38 [] (unknown:0) - Number of loaded modules: 136<br>
[DEBUG][Qt] 06.01.2018 07:49:38 [] (unknown:0) - Switch to module:  “Welcome”<br>
[CRITICAL][FD] 06.01.2018 07:50:19 [] (unknown:0) - 2018-01-06 07:50:19.350 Slicer[3045:24445] modalSession has been exited prematurely - check for a reentrant call to endModalSession:<br>
[CRITICAL][FD] 06.01.2018 07:50:20 [] (unknown:0) - 2018-01-06 07:50:20.384 Slicer[3045:24445] modalSession has been exited prematurely - check for a reentrant call to endModalSession:<br>
[INFO][VTK] 06.01.2018 07:50:20 [vtkMRMLVolumeArchetypeStorageNode (0x137488960)] (/Users/kitware/Dashboards/Package/Slicer-481/Libs/MRML/Core/vtkMRMLVolumeArchetypeStorageNode.cxx:465) - Loaded volume from file: /Users/mimipoon/Documents/Images/MB49/Combo/ComboNrrd/Day10_18F_ARaG_Group2_Combo_CST_PET 18F_Static_600s Acquisitio.nrrd. Dimensions: 128x128x159. Number of components: 1. Pixel type: double.<br>
[DEBUG][Qt] 06.01.2018 07:50:20 [] (unknown:0) - “Volume” Reader has successfully read the file “/Users/mimipoon/Documents/Images/MB49/Combo/ComboNrrd/Day10_18F_ARaG_Group2_Combo_CST_PET 18F_Static_600s Acquisitio.nrrd” “[0.18s]”<br>
[INFO][VTK] 06.01.2018 07:50:27 [vtkMRMLVolumeArchetypeStorageNode (0x13bc7b500)] (/Users/kitware/Dashboards/Package/Slicer-481/Libs/MRML/Core/vtkMRMLVolumeArchetypeStorageNode.cxx:465) - Loaded volume from file: /Users/mimipoon/Documents/Images/MB49/Combo/ComboNrrd/Day10_18F_ARaG_Group2_Combo_CST_v1.ct modified.nrrd. Dimensions: 512x512x700. Number of components: 1. Pixel type: double.<br>
[DEBUG][Qt] 06.01.2018 07:50:27 [] (unknown:0) - “Volume” Reader has successfully read the file “/Users/mimipoon/Documents/Images/MB49/Combo/ComboNrrd/Day10_18F_ARaG_Group2_Combo_CST_v1.ct modified.nrrd” “[6.80s]”<br>
[DEBUG][Qt] 06.01.2018 07:50:30 [] (unknown:0) - Switch to module:  “Data”<br>
[DEBUG][Qt] 06.01.2018 07:52:43 [] (unknown:0) - Switch to module:  “SegmentEditor”<br>
[CRITICAL][FD] 06.01.2018 07:52:50 [] (unknown:0) - 2018-01-06 07:52:50.636 Slicer[3045:24445] modalSession has been exited prematurely - check for a reentrant call to endModalSession:<br>
[CRITICAL][FD] 06.01.2018 07:52:56 [] (unknown:0) - 2018-01-06 07:52:56.969 Slicer[3045:24445] modalSession has been exited prematurely - check for a reentrant call to endModalSession:</p>

---

## Post #2 by @cpinter (2018-01-06 16:34 UTC)

<p>Thanks for the report! Unfortunately the log does not contain meaningful information so we need to reproduce. I tried on Windows and both ‘a’ and Enter keys work for me with the Draw effect using the latert trunk. Need to try on Mac.</p>

---

## Post #3 by @pieper (2018-01-06 17:08 UTC)

<p>Enter and ‘a’ both work for me with 4.8 Draw effect in Segment Editor on mac.</p>

---

## Post #4 by @MimiPoon (2018-01-06 22:09 UTC)

<p>Draw effect in segment editor works well in 4.8 but not successful every<br>
time in 4.8.1.</p>

---

## Post #5 by @pieper (2018-01-06 22:27 UTC)

<p>I tried 4.8.1 on mac and still had no problems.  Any idea how to reproduce the issue?</p>

---
