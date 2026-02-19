---
topic_id: 382
title: "Freesurfer Annotation File Crashes Model Module"
date: 2017-05-25
url: https://discourse.slicer.org/t/382
---

# Freesurfer annotation file crashes model module

**Topic ID**: 382
**Date**: 2017-05-25
**URL**: https://discourse.slicer.org/t/freesurfer-annotation-file-crashes-model-module/382

---

## Post #1 by @mrjeffs (2017-05-25 04:01 UTC)

<p>i tried to load a freesurfer surface <code>lh.pial</code> and then add the <code>lh.aparc.a2009s.annot</code> file to show parcellation which loaded and displayed well but when i touched the model scene selector to turn the model off slicer crashed. see bug report below.</p>

---

## Post #2 by @mrjeffs (2017-05-25 04:03 UTC)

<pre><code class="lang-auto">[DEBUG][Qt] 24.05.2017 20:30:19 [] (unknown:0) - Session start time .......: 2017-05-24 20:30:19
[DEBUG][Qt] 24.05.2017 20:30:19 [] (unknown:0) - Slicer version ...........: 4.7.0-2017-05-23 (revision 26032) macosx-amd64 - installed
[DEBUG][Qt] 24.05.2017 20:30:19 [] (unknown:0) - Operating system .........: Mac OS X / 10.11.6 / 15G1510 - 64-bit
[DEBUG][Qt] 24.05.2017 20:30:19 [] (unknown:0) - Memory ...................: 32768 MB physical, 11264 MB virtual
[DEBUG][Qt] 24.05.2017 20:30:19 [] (unknown:0) - CPU ......................: GenuineIntel Intel(R) Core(TM) i7-6700K CPU @ 4.00GHz, 4 cores, 8 logical processors
[DEBUG][Qt] 24.05.2017 20:30:19 [] (unknown:0) - Developer mode enabled ...: no
[DEBUG][Qt] 24.05.2017 20:30:19 [] (unknown:0) - Prefer executable CLI ....: yes
[DEBUG][Qt] 24.05.2017 20:30:19 [] (unknown:0) - Additional module paths ..: /Applications/Slicer_dev_5-24.app/Contents/Extensions-26032/DTIProcess/lib/Slicer-4.7/cli-modules, /Applications/Slicer_dev_5-24.app/Contents/Extensions-26032/UKFTractography/lib/Slicer-4.7/cli-modules, /Applications/Slicer_dev_5-24.app/Contents/Extensions-26032/SlicerDMRI/lib/Slicer-4.7/cli-modules, /Applications/Slicer_dev_5-24.app/Contents/Extensions-26032/SlicerDMRI/lib/Slicer-4.7/qt-loadable-modules, /Applications/Slicer_dev_5-24.app/Contents/Extensions-26032/SlicerDMRI/lib/Slicer-4.7/qt-scripted-modules, /Applications/Slicer_dev_5-24.app/Contents/Extensions-26032/ResampleDTIlogEuclidean/lib/Slicer-4.7/cli-modules, /Applications/Slicer_dev_5-24.app/Contents/Extensions-26032/Sequences/lib/Slicer-4.7/qt-loadable-modules, /Applications/Slicer_dev_5-24.app/Contents/Extensions-26032/SegmentEditorExtraEffects/lib/Slicer-4.7/qt-scripted-modules
[DEBUG][Python] 24.05.2017 20:30:25 [Python] (/Applications/Slicer_dev_5-24.app/Contents/lib/Slicer-4.7/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 24.05.2017 20:30:26 [Python] (/Applications/Slicer_dev_5-24.app/Contents/lib/Slicer-4.7/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 24.05.2017 20:30:26 [Python] (/Applications/Slicer_dev_5-24.app/Contents/lib/Slicer-4.7/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 24.05.2017 20:30:21 [] (unknown:0) - Number of registered modules: 169
[CRITICAL][Qt] 24.05.2017 20:30:22 [] (unknown:0) -   Error(s):
    CLI executable: /Applications/Slicer_dev_5-24.app/Contents/Extensions-26032/DTIProcess/lib/Slicer-4.7/cli-modules/polydatamerge
    dyld: Library not loaded: @rpath/lib/Slicer-4.7/libjsoncpp.0.dylib
  Referenced from: /Applications/Slicer_dev_5-24.app/Contents/Extensions-26032/DTIProcess/lib/Slicer-4.7/cli-modules/polydatamerge
  Reason: image not found

    CLI executable: /Applications/Slicer_dev_5-24.app/Contents/Extensions-26032/DTIProcess/lib/Slicer-4.7/cli-modules/polydatamerge
    Failed to retrieve Xml Description
[CRITICAL][Qt] 24.05.2017 20:30:22 [] (unknown:0) - Fail to instantiate module  "polydatamerge"
[CRITICAL][Qt] 24.05.2017 20:30:22 [] (unknown:0) -   Error(s):
    CLI executable: /Applications/Slicer_dev_5-24.app/Contents/Extensions-26032/DTIProcess/lib/Slicer-4.7/cli-modules/polydatatransform
    dyld: Library not loaded: @rpath/lib/Slicer-4.7/libjsoncpp.0.dylib
  Referenced from: /Applications/Slicer_dev_5-24.app/Contents/Extensions-26032/DTIProcess/lib/Slicer-4.7/cli-modules/polydatatransform
  Reason: image not found

    CLI executable: /Applications/Slicer_dev_5-24.app/Contents/Extensions-26032/DTIProcess/lib/Slicer-4.7/cli-modules/polydatatransform
    Failed to retrieve Xml Description
[CRITICAL][Qt] 24.05.2017 20:30:22 [] (unknown:0) - Fail to instantiate module  "polydatatransform"
[DEBUG][Qt] 24.05.2017 20:30:22 [] (unknown:0) - Number of instantiated modules: 167
[WARNING][Qt] 24.05.2017 20:30:25 [] (unknown:0) - When loading module  "CLIEventTest" , the dependency "CLI4Test" failed to be loaded.
[INFO][Stream] 24.05.2017 20:30:25 [] (unknown:0) - Initializing terminology mapping for map file /Applications/Slicer_dev_5-24.app/Contents/share/Slicer-4.7/ColorFiles/Terminology//GenericAnatomyColors-SNOMED.csv
[INFO][Stream] 24.05.2017 20:30:25 [] (unknown:0) - 288 terms were read for Slicer LUT GenericAnatomyColors
[WARNING][Qt] 24.05.2017 20:30:26 [] (unknown:0) - When loading module  "TwoCLIsInARowTest" , the dependency "CLI4Test" failed to be loaded.
[WARNING][Qt] 24.05.2017 20:30:26 [] (unknown:0) - When loading module  "TwoCLIsInParallelTest" , the dependency "CLI4Test" failed to be loaded.
[DEBUG][Qt] 24.05.2017 20:30:26 [] (unknown:0) - Number of loaded modules: 164
[DEBUG][Qt] 24.05.2017 20:30:26 [] (unknown:0) - Switch to module:  "Welcome"
[CRITICAL][FD] 24.05.2017 20:32:27 [] (unknown:0) - 2017-05-24 20:32:27.298 Slicer[4663:1738626] modalSession has been exited prematurely - check for a reentrant call to endModalSession:
[CRITICAL][FD] 24.05.2017 20:32:32 [] (unknown:0) - 2017-05-24 20:32:32.970 Slicer[4663:1738626] modalSession has been exited prematurely - check for a reentrant call to endModalSession:
[DEBUG][Qt] 24.05.2017 20:32:33 [] (unknown:0) - "Model" Reader has successfully read the file "/Users/mrjeffs/Desktop/nbwr/Slicer_scenes/Slicer_whole_br_UKF_lt-SLF-IFOF_qT1-05-24-2017_6pm/lh.pial" "[0.19s]"
[CRITICAL][FD] 24.05.2017 20:32:45 [] (unknown:0) - 2017-05-24 20:32:45.591 Slicer[4663:1738626] modalSession has been exited prematurely - check for a reentrant call to endModalSession:
[DEBUG][Qt] 24.05.2017 20:32:45 [] (unknown:0) - qSlicerScalarOverlayReader::options(): 0x11127b640
[CRITICAL][FD] 24.05.2017 20:32:51 [] (unknown:0) - 2017-05-24 20:32:51.383 Slicer[4663:1738626] modalSession has been exited prematurely - check for a reentrant call to endModalSession:
[DEBUG][Qt] 24.05.2017 20:32:51 [] (unknown:0) - "Scalar Overlay" Reader has successfully read the file "/Users/mrjeffs/Desktop/nbwr/Slicer_scenes/Slicer_whole_br_UKF_lt-SLF-IFOF_qT1-05-24-2017_6pm/lh.aparc.a2009s.annot" "[0.03s]"
[ERROR][VTK] 24.05.2017 20:32:51 [vtkLookupTable (0x131019a40)] (/Users/kitware/Dashboards/Nightly/Slicer-0-build/VTKv7/Common/Core/vtkLookupTable.cxx:144) - Bad table range: [1e+299, -1e+299]
[DEBUG][Qt] 24.05.2017 20:32:56 [] (unknown:0) - Switch to module:  "Models"
[ERROR][VTK] 24.05.2017 20:33:02 [vtkLookupTable (0x131019a40)] (/Users/kitware/Dashboards/Nightly/Slicer-0-build/VTKv7/Common/Core/vtkLookupTable.cxx:144) - Bad table range: [1e+299, -1e+299]
</code></pre>

---

## Post #3 by @mrjeffs (2017-05-25 04:05 UTC)

<p>and this log:</p>
<pre><code class="lang-auto">[DEBUG][Qt] 24.05.2017 20:23:56 [] (unknown:0) - Session start time .......: 2017-05-24 20:23:56
[DEBUG][Qt] 24.05.2017 20:23:56 [] (unknown:0) - Slicer version ...........: 4.7.0-2017-05-23 (revision 26032) macosx-amd64 - installed
[DEBUG][Qt] 24.05.2017 20:23:56 [] (unknown:0) - Operating system .........: Mac OS X / 10.11.6 / 15G1510 - 64-bit
[DEBUG][Qt] 24.05.2017 20:23:56 [] (unknown:0) - Memory ...................: 32768 MB physical, 11264 MB virtual
[DEBUG][Qt] 24.05.2017 20:23:56 [] (unknown:0) - CPU ......................: GenuineIntel Intel(R) Core(TM) i7-6700K CPU @ 4.00GHz, 4 cores, 8 logical processors
[DEBUG][Qt] 24.05.2017 20:23:56 [] (unknown:0) - Developer mode enabled ...: no
[DEBUG][Qt] 24.05.2017 20:23:56 [] (unknown:0) - Prefer executable CLI ....: yes
[DEBUG][Qt] 24.05.2017 20:23:56 [] (unknown:0) - Additional module paths ..: /Applications/Slicer_dev_5-24.app/Contents/Extensions-26032/DTIProcess/lib/Slicer-4.7/cli-modules, /Applications/Slicer_dev_5-24.app/Contents/Extensions-26032/UKFTractography/lib/Slicer-4.7/cli-modules, /Applications/Slicer_dev_5-24.app/Contents/Extensions-26032/SlicerDMRI/lib/Slicer-4.7/cli-modules, /Applications/Slicer_dev_5-24.app/Contents/Extensions-26032/SlicerDMRI/lib/Slicer-4.7/qt-loadable-modules, /Applications/Slicer_dev_5-24.app/Contents/Extensions-26032/SlicerDMRI/lib/Slicer-4.7/qt-scripted-modules, /Applications/Slicer_dev_5-24.app/Contents/Extensions-26032/ResampleDTIlogEuclidean/lib/Slicer-4.7/cli-modules, /Applications/Slicer_dev_5-24.app/Contents/Extensions-26032/Sequences/lib/Slicer-4.7/qt-loadable-modules, /Applications/Slicer_dev_5-24.app/Contents/Extensions-26032/SegmentEditorExtraEffects/lib/Slicer-4.7/qt-scripted-modules
[DEBUG][Python] 24.05.2017 20:24:02 [Python] (/Applications/Slicer_dev_5-24.app/Contents/lib/Slicer-4.7/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 24.05.2017 20:24:03 [Python] (/Applications/Slicer_dev_5-24.app/Contents/lib/Slicer-4.7/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 24.05.2017 20:24:03 [Python] (/Applications/Slicer_dev_5-24.app/Contents/lib/Slicer-4.7/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 24.05.2017 20:23:59 [] (unknown:0) - Number of registered modules: 169
[CRITICAL][Qt] 24.05.2017 20:23:59 [] (unknown:0) -   Error(s):
    CLI executable: /Applications/Slicer_dev_5-24.app/Contents/Extensions-26032/DTIProcess/lib/Slicer-4.7/cli-modules/polydatamerge
    dyld: Library not loaded: @rpath/lib/Slicer-4.7/libjsoncpp.0.dylib
  Referenced from: /Applications/Slicer_dev_5-24.app/Contents/Extensions-26032/DTIProcess/lib/Slicer-4.7/cli-modules/polydatamerge
  Reason: image not found

    CLI executable: /Applications/Slicer_dev_5-24.app/Contents/Extensions-26032/DTIProcess/lib/Slicer-4.7/cli-modules/polydatamerge
    Failed to retrieve Xml Description
[CRITICAL][Qt] 24.05.2017 20:23:59 [] (unknown:0) - Fail to instantiate module  "polydatamerge"
[CRITICAL][Qt] 24.05.2017 20:23:59 [] (unknown:0) -   Error(s):
    CLI executable: /Applications/Slicer_dev_5-24.app/Contents/Extensions-26032/DTIProcess/lib/Slicer-4.7/cli-modules/polydatatransform
    dyld: Library not loaded: @rpath/lib/Slicer-4.7/libjsoncpp.0.dylib
  Referenced from: /Applications/Slicer_dev_5-24.app/Contents/Extensions-26032/DTIProcess/lib/Slicer-4.7/cli-modules/polydatatransform
  Reason: image not found

    CLI executable: /Applications/Slicer_dev_5-24.app/Contents/Extensions-26032/DTIProcess/lib/Slicer-4.7/cli-modules/polydatatransform
    Failed to retrieve Xml Description
[CRITICAL][Qt] 24.05.2017 20:23:59 [] (unknown:0) - Fail to instantiate module  "polydatatransform"
[DEBUG][Qt] 24.05.2017 20:23:59 [] (unknown:0) - Number of instantiated modules: 167
[WARNING][Qt] 24.05.2017 20:24:02 [] (unknown:0) - When loading module  "CLIEventTest" , the dependency "CLI4Test" failed to be loaded.
[INFO][Stream] 24.05.2017 20:24:02 [] (unknown:0) - Initializing terminology mapping for map file /Applications/Slicer_dev_5-24.app/Contents/share/Slicer-4.7/ColorFiles/Terminology//GenericAnatomyColors-SNOMED.csv
[INFO][Stream] 24.05.2017 20:24:02 [] (unknown:0) - 288 terms were read for Slicer LUT GenericAnatomyColors
[WARNING][Qt] 24.05.2017 20:24:03 [] (unknown:0) - When loading module  "TwoCLIsInARowTest" , the dependency "CLI4Test" failed to be loaded.
[WARNING][Qt] 24.05.2017 20:24:03 [] (unknown:0) - When loading module  "TwoCLIsInParallelTest" , the dependency "CLI4Test" failed to be loaded.
[DEBUG][Qt] 24.05.2017 20:24:03 [] (unknown:0) - Number of loaded modules: 164
[DEBUG][Qt] 24.05.2017 20:24:03 [] (unknown:0) - Switch to module:  "Welcome"
[CRITICAL][FD] 24.05.2017 20:24:14 [] (unknown:0) - 2017-05-24 20:24:14.308 Slicer[4639:1726512] modalSession has been exited prematurely - check for a reentrant call to endModalSession:
[CRITICAL][FD] 24.05.2017 20:24:16 [] (unknown:0) - 2017-05-24 20:24:16.053 Slicer[4639:1726512] modalSession has been exited prematurely - check for a reentrant call to endModalSession:
[DEBUG][Qt] 24.05.2017 20:24:16 [] (unknown:0) - "Model" Reader has successfully read the file "/Users/mrjeffs/Desktop/nbwr/Slicer_scenes/Slicer_whole_br_UKF_lt-SLF-IFOF_qT1-05-24-2017_6pm/rh.white" "[0.19s]"
[DEBUG][Qt] 24.05.2017 20:24:18 [] (unknown:0) - Switch to module:  "Models"
[CRITICAL][FD] 24.05.2017 20:24:29 [] (unknown:0) - 2017-05-24 20:24:29.722 Slicer[4639:1726512] modalSession has been exited prematurely - check for a reentrant call to endModalSession:
[DEBUG][Qt] 24.05.2017 20:24:29 [] (unknown:0) - qSlicerScalarOverlayReader::options(): 0x11bc4b4a0
</code></pre>

---

## Post #4 by @jcfr (2017-05-25 04:11 UTC)

<p>Would be able to share the dataset causing the crash ?</p>

---

## Post #5 by @mrjeffs (2017-05-25 04:24 UTC)

<p>removed links, annot now loads fine, however edited lh.thickness fails to load.</p>

---

## Post #6 by @lassoan (2017-05-25 11:43 UTC)

<p>Thanks for reporting this. The hang is due to a recent change in Models module (in computing display precision for scalar range). I’ve prepared a fix: <a href="https://github.com/Slicer/Slicer/pull/728">https://github.com/Slicer/Slicer/pull/728</a></p>

---

## Post #7 by @lassoan (2017-05-25 22:30 UTC)

<p>The fix will be available in tomorrow’s nightly build.</p>

---

## Post #8 by @mrjeffs (2017-05-25 22:31 UTC)

<p>awesome, thanks guys, or merci. jeff</p>

---

## Post #9 by @mrjeffs (2017-06-01 23:18 UTC)

<p>tested june 1 and annotation loads but i tried loading a modified lh.thickness file and it failed to load in slicer tho freeview works fine.<br>
copy of debug:<br>
[DEBUG][Qt] 01.06.2017 16:08:48 [] (unknown:0) - Session start time …: 2017-06-01 16:08:48<br>
[DEBUG][Qt] 01.06.2017 16:08:48 [] (unknown:0) - Slicer version …: 4.7.0-2017-05-31 (revision 26062) macosx-amd64 - installed<br>
[DEBUG][Qt] 01.06.2017 16:08:48 [] (unknown:0) - Operating system …: Mac OS X / 10.11.6 / 15G1510 - 64-bit<br>
[DEBUG][Qt] 01.06.2017 16:08:48 [] (unknown:0) - Memory …: 32768 MB physical, 17408 MB virtual<br>
[DEBUG][Qt] 01.06.2017 16:08:48 [] (unknown:0) - CPU …: GenuineIntel Intel® Core™ i7-6700K CPU @ 4.00GHz, 4 cores, 8 logical processors<br>
[DEBUG][Qt] 01.06.2017 16:08:48 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 01.06.2017 16:08:48 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 01.06.2017 16:08:48 [] (unknown:0) - Additional module paths …: (none)<br>
[DEBUG][Python] 01.06.2017 16:08:53 [Python] (/Applications/Slicer_4p7p0_dev06-01-2017.app/Contents/lib/Slicer-4.7/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 01.06.2017 16:08:53 [Python] (/Applications/Slicer_4p7p0_dev06-01-2017.app/Contents/lib/Slicer-4.7/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 01.06.2017 16:08:53 [Python] (/Applications/Slicer_4p7p0_dev06-01-2017.app/Contents/lib/Slicer-4.7/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 01.06.2017 16:08:50 [] (unknown:0) - Number of registered modules: 137<br>
[DEBUG][Qt] 01.06.2017 16:08:50 [] (unknown:0) - Number of instantiated modules: 137<br>
[INFO][Stream] 01.06.2017 16:08:53 [] (unknown:0) - Initializing terminology mapping for map file /Applications/Slicer_4p7p0_dev06-01-2017.app/Contents/share/Slicer-4.7/ColorFiles/Terminology//GenericAnatomyColors-SNOMED.csv<br>
[INFO][Stream] 01.06.2017 16:08:53 [] (unknown:0) - 288 terms were read for Slicer LUT GenericAnatomyColors<br>
[DEBUG][Qt] 01.06.2017 16:08:54 [] (unknown:0) - Number of loaded modules: 137<br>
[DEBUG][Qt] 01.06.2017 16:08:54 [] (unknown:0) - Switch to module:  “Welcome”<br>
[CRITICAL][FD] 01.06.2017 16:09:30 [] (unknown:0) - 2017-06-01 16:09:30.337 Slicer[19903:8055473] modalSession has been exited prematurely - check for a reentrant call to endModalSession:<br>
[CRITICAL][FD] 01.06.2017 16:09:32 [] (unknown:0) - 2017-06-01 16:09:32.667 Slicer[19903:8055473] modalSession has been exited prematurely - check for a reentrant call to endModalSession:<br>
[DEBUG][Qt] 01.06.2017 16:09:32 [] (unknown:0) - “Model” Reader has successfully read the file “/Users/mrjeffs/Desktop/template_hires_br_freesurf_v6/surf/lh.pial” “[0.18s]”<br>
[CRITICAL][FD] 01.06.2017 16:09:44 [] (unknown:0) - 2017-06-01 16:09:44.919 Slicer[19903:8055473] modalSession has been exited prematurely - check for a reentrant call to endModalSession:<br>
[DEBUG][Qt] 01.06.2017 16:09:44 [] (unknown:0) - qSlicerScalarOverlayReader::options(): 0x11095abf0<br>
[CRITICAL][FD] 01.06.2017 16:09:56 [] (unknown:0) - 2017-06-01 16:09:56.472 Slicer[19903:8055473] modalSession has been exited prematurely - check for a reentrant call to endModalSession:<br>
[DEBUG][Qt] 01.06.2017 16:10:00 [] (unknown:0) - Switch to module:  “Models”<br>
[CRITICAL][FD] 01.06.2017 16:12:28 [] (unknown:0) - 2017-06-01 16:12:28.208 Slicer[19903:8055473] modalSession has been exited prematurely - check for a reentrant call to endModalSession:<br>
[CRITICAL][FD] 01.06.2017 16:12:48 [] (unknown:0) - 2017-06-01 16:12:48.153 Slicer[19903:8055473] modalSession has been exited prematurely - check for a reentrant call to endModalSession:<br>
[DEBUG][Qt] 01.06.2017 16:12:48 [] (unknown:0) - qSlicerScalarOverlayReader::options(): 0x11095abf0<br>
[CRITICAL][FD] 01.06.2017 16:12:51 [] (unknown:0) - 2017-06-01 16:12:51.082 Slicer[19903:8055473] modalSession has been exited prematurely - check for a reentrant call to endModalSession:<br>
[DEBUG][Qt] 01.06.2017 16:12:51 [] (unknown:0) - “Scalar Overlay” Reader has successfully read the file “/Users/mrjeffs/Desktop/template_hires_br_freesurf_v6/label/lh.aparc.a2009s.annot” “[0.06s]”</p>

---

## Post #10 by @mrjeffs (2017-06-01 23:23 UTC)

<p>here are the new files:<br>
new thickness file:<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/images/favicon-vflUeLeeY.ico" class="site-icon" width="32" height="32">
      <a href="https://www.dropbox.com/s/tw3p4gqlgztr095/lh.meanthickness_contrl?dl=0" target="_blank" rel="nofollow noopener">Dropbox</a>
  </header>
  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/images/spectrum-icons/generated/content/content-unknown-large.png" class="thumbnail onebox-avatar" width="160" height="160">

<h3><a href="https://www.dropbox.com/s/tw3p4gqlgztr095/lh.meanthickness_contrl?dl=0" target="_blank" rel="nofollow noopener">lh.meanthickness_contrl</a></h3>

<p>Shared with Dropbox</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
a pial file:<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/images/favicon-vflUeLeeY.ico" class="site-icon" width="32" height="32">
      <a href="https://www.dropbox.com/s/s0bes6mu8x2rajo/lh.pial?dl=0" target="_blank" rel="nofollow noopener">Dropbox</a>
  </header>
  <article class="onebox-body">
    <img src="https://www.dropbox.com/static/images/spectrum-icons/generated/content/content-unknown-large.png" class="thumbnail onebox-avatar" width="160" height="160">

<h3><a href="https://www.dropbox.com/s/s0bes6mu8x2rajo/lh.pial?dl=0" target="_blank" rel="nofollow noopener">lh.pial</a></h3>

<p>Shared with Dropbox</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #11 by @lassoan (2017-06-02 13:46 UTC)

<p>The current version of Slicer can only load scalar overlays from files with standard file extensions. I’ve committed a fix that will allow loading scalar overlay files with any extension - this fix will be available in tomorrow’s nightly version.</p>
<p>Till then, if you rename your file to lh.thickness then it should load fine.</p>

---

## Post #12 by @mrjeffs (2017-06-02 14:51 UTC)

<p>ah it was that simple. great. that will be helpful for our other modalities as well. thanks. jeff</p>

---

## Post #13 by @lassoan (2017-06-02 15:13 UTC)

<p>I’ve tested this a bit more and unfortunately it has some side effects if we let any file extension to be recognized as FreeSurfer scalar overlay. Would it be an issue for you to save your overlay files with file extensions that ends with a standard extension? For example instead of <code>lh.meanthickness_contrl</code> these would all work: <code>lh.contrl.mean.thickness</code>, <code>lh.mean_contrl.thickness</code>, <code>lh_mean_contrl.thickness</code>.</p>

---

## Post #14 by @mrjeffs (2017-06-02 15:21 UTC)

<p>no problem. makes sense to have it be limited. lh.some_contiguous_string.thickness works fine. it looks like there is an option for multiple scalars per model object, so may i also suggest an  lh.some_contiguous_string.dspm,<br>
and  lh.some_contiguous_string.morph as a starting list.<br>
off topic but is there a method to cycle thru an overlay in movie mode? that would be a very useful feature for<br>
multi modal meg datasets<br>
jeff</p>

---

## Post #15 by @lassoan (2017-06-02 15:51 UTC)

<p>Do files with .dspm and .morph extension have the same format as .thickness files?</p>
<p>About the movie: I’ve created a separate topic to discuss that - <a href="https://discourse.slicer.org/t/create-movie-of-changing-scalar-data-on-a-model/426">see here</a></p>

---

## Post #16 by @mrjeffs (2017-06-02 17:48 UTC)

<p>i think the better way is to deal directly with .stc files as overlays, .dspm static files would only be helpful once you have identified the critical time slice. so i ammend my feature request to .stc files and stabdard freesurfer morph files.</p>

---
