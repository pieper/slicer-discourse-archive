---
topic_id: 20816
title: "Freesurfer Import Module Not Loading"
date: 2021-11-28
url: https://discourse.slicer.org/t/20816
---

# Freesurfer import module not loading

**Topic ID**: 20816
**Date**: 2021-11-28
**URL**: https://discourse.slicer.org/t/freesurfer-import-module-not-loading/20816

---

## Post #1 by @Vinny (2021-11-28 13:16 UTC)

<p>Hi,</p>
<p>When the Freesurfer import module is installed, I can use it immediately.  However, when Slicer is opened subsequently, I get the following message that it cannot be loaded:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6e7fc36123b907e2eb728473006e2dfc6582464.png" alt="image" data-base62-sha1="wWGQl70GpLXlhGGEJOShgY0elmI" width="689" height="462"></p>
<p>How can this module be loaded?</p>
<p>OS: Ubuntu 20.04<br>
3d Slicer version: 4.13.0-2021-10-10</p>
<p>Thanks,</p>
<p>Vinny</p>

---

## Post #2 by @pieper (2021-11-28 13:28 UTC)

<p>Please post the <a href="https://www.slicer.org/wiki/Documentation/4.10/SlicerApplication/ErrorLog">error log</a>.</p>

---

## Post #3 by @Vinny (2021-11-28 13:41 UTC)

<p>Here is a screenshot error log:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/659f871c140b6d73db211b7a79391d877f465a6c.png" data-download-href="/uploads/short-url/ev00H17x2i6wqhe31IoxxsA3lfe.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/659f871c140b6d73db211b7a79391d877f465a6c_2_690x393.png" alt="image" data-base62-sha1="ev00H17x2i6wqhe31IoxxsA3lfe" width="690" height="393" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/659f871c140b6d73db211b7a79391d877f465a6c_2_690x393.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/659f871c140b6d73db211b7a79391d877f465a6c_2_1035x589.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/659f871c140b6d73db211b7a79391d877f465a6c_2_1380x786.png 2x" data-dominant-color="CDCCCD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1851×1055 166 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Also, below is the entire error log:</p>
<p>[DEBUG][Qt] 28.11.2021 08:36:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Session start time …: 2021-11-28 08:36:04<br>
[DEBUG][Qt] 28.11.2021 08:36:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Slicer version …: 4.13.0-2021-10-10 (revision 30309 / 03e9135) linux-amd64 - installed release<br>
[DEBUG][Qt] 28.11.2021 08:36:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Operating system …: Linux / 5.4.0-90-generic / <span class="hashtag-raw">#101-Ubuntu</span> SMP Fri Oct 15 20:00:55 UTC 2021 / UTF-8 - 64-bit<br>
[DEBUG][Qt] 28.11.2021 08:36:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Memory …: 15870 MB physical, 30719 MB virtual<br>
[DEBUG][Qt] 28.11.2021 08:36:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - CPU …: GenuineIntel Intel(R) Core™ i7-8750H CPU @ 2.20GHz, 6 cores, 12 logical processors<br>
[DEBUG][Qt] 28.11.2021 08:36:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - VTK configuration …: OpenGL2 rendering, Sequential threading<br>
[DEBUG][Qt] 28.11.2021 08:36:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Qt configuration …: version 5.15.2, with SSL, requested OpenGL 3.2 (core profile)<br>
[DEBUG][Qt] 28.11.2021 08:36:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 28.11.2021 08:36:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Application path …: /home/vinny/Downloads/Slicer-4.13.0-2021-10-10-linux-amd64/bin<br>
[DEBUG][Qt] 28.11.2021 08:36:04 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Additional module paths …: NA-MIC/Extensions-30309/SlicerRT/lib/Slicer-4.13/cli-modules, NA-MIC/Extensions-30309/SlicerRT/lib/Slicer-4.13/qt-loadable-modules, NA-MIC/Extensions-30309/SlicerRT/lib/Slicer-4.13/qt-scripted-modules, NA-MIC/Extensions-30309/SlicerFreeSurfer/lib/Slicer-4.13/qt-loadable-modules<br>
[CRITICAL][Qt] 28.11.2021 08:36:05 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Error(s):<br>
Cannot load library /home/vinny/Downloads/Slicer-4.13.0-2021-10-10-linux-amd64/NA-MIC/Extensions-30309/SlicerRT/lib/Slicer-4.13/qt-loadable-modules/libqSlicerBeamsModule.so: (libqSlicerBeamsModuleWidgets.so: cannot open shared object file: No such file or directory)<br>
[CRITICAL][Qt] 28.11.2021 08:36:05 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Error(s):<br>
Cannot load library /home/vinny/Downloads/Slicer-4.13.0-2021-10-10-linux-amd64/NA-MIC/Extensions-30309/SlicerRT/lib/Slicer-4.13/qt-loadable-modules/libqSlicerDicomRtImportExportModule.so: (libvtkSlicerDicomRtImportExportModuleLogic.so: cannot open shared object file: No such file or directory)<br>
[CRITICAL][Qt] 28.11.2021 08:36:05 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Error(s):<br>
Cannot load library /home/vinny/Downloads/Slicer-4.13.0-2021-10-10-linux-amd64/NA-MIC/Extensions-30309/SlicerRT/lib/Slicer-4.13/qt-loadable-modules/libqSlicerDicomSroImportExportModule.so: (libvtkSlicerDicomSroImportExportModuleLogic.so: cannot open shared object file: No such file or directory)<br>
[CRITICAL][Qt] 28.11.2021 08:36:05 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Error(s):<br>
Cannot load library /home/vinny/Downloads/Slicer-4.13.0-2021-10-10-linux-amd64/NA-MIC/Extensions-30309/SlicerRT/lib/Slicer-4.13/qt-loadable-modules/libqSlicerDoseAccumulationModule.so: (libvtkSlicerDoseAccumulationModuleLogic.so: cannot open shared object file: No such file or directory)<br>
[CRITICAL][Qt] 28.11.2021 08:36:05 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Error(s):<br>
Cannot load library /home/vinny/Downloads/Slicer-4.13.0-2021-10-10-linux-amd64/NA-MIC/Extensions-30309/SlicerRT/lib/Slicer-4.13/qt-loadable-modules/libqSlicerDoseComparisonModule.so: (libqSlicerDoseComparisonSubjectHierarchyPlugins.so: cannot open shared object file: No such file or directory)<br>
[CRITICAL][Qt] 28.11.2021 08:36:05 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Error(s):<br>
Cannot load library /home/vinny/Downloads/Slicer-4.13.0-2021-10-10-linux-amd64/NA-MIC/Extensions-30309/SlicerRT/lib/Slicer-4.13/qt-loadable-modules/libqSlicerDoseVolumeHistogramModule.so: (libqSlicerDoseVolumeHistogramSubjectHierarchyPlugins.so: cannot open shared object file: No such file or directory)<br>
[CRITICAL][Qt] 28.11.2021 08:36:05 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Error(s):<br>
Cannot load library /home/vinny/Downloads/Slicer-4.13.0-2021-10-10-linux-amd64/NA-MIC/Extensions-30309/SlicerRT/lib/Slicer-4.13/qt-loadable-modules/libqSlicerDosxyzNrc3dDoseFileReaderModule.so: (libvtkSlicerRtCommon.so: cannot open shared object file: No such file or directory)<br>
[CRITICAL][Qt] 28.11.2021 08:36:05 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Error(s):<br>
Cannot load library /home/vinny/Downloads/Slicer-4.13.0-2021-10-10-linux-amd64/NA-MIC/Extensions-30309/SlicerRT/lib/Slicer-4.13/qt-loadable-modules/libqSlicerDrrImageComputationModule.so: (libqSlicerDrrImageComputationModuleWidgets.so: cannot open shared object file: No such file or directory)<br>
[CRITICAL][Qt] 28.11.2021 08:36:05 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Error(s):<br>
Cannot load library /home/vinny/Downloads/Slicer-4.13.0-2021-10-10-linux-amd64/NA-MIC/Extensions-30309/SlicerRT/lib/Slicer-4.13/qt-loadable-modules/libqSlicerExternalBeamPlanningModule.so: (libqSlicerBeamsSubjectHierarchyPlugins.so: cannot open shared object file: No such file or directory)<br>
[CRITICAL][Qt] 28.11.2021 08:36:05 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Error(s):<br>
Cannot load library /home/vinny/Downloads/Slicer-4.13.0-2021-10-10-linux-amd64/NA-MIC/Extensions-30309/SlicerRT/lib/Slicer-4.13/qt-loadable-modules/libqSlicerIsodoseModule.so: (libvtkSlicerIsodoseModuleWidgets.so: cannot open shared object file: No such file or directory)<br>
[CRITICAL][Qt] 28.11.2021 08:36:05 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Error(s):<br>
Cannot load library /home/vinny/Downloads/Slicer-4.13.0-2021-10-10-linux-amd64/NA-MIC/Extensions-30309/SlicerRT/lib/Slicer-4.13/qt-loadable-modules/libqSlicerPlanarImageModule.so: (libvtkSlicerPlanarImageModuleLogic.so: cannot open shared object file: No such file or directory)<br>
[CRITICAL][Qt] 28.11.2021 08:36:05 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Error(s):<br>
Cannot load library /home/vinny/Downloads/Slicer-4.13.0-2021-10-10-linux-amd64/NA-MIC/Extensions-30309/SlicerRT/lib/Slicer-4.13/qt-loadable-modules/libqSlicerPlastimatchPyModule.so: (libvtkSlicerPlastimatchPyModuleLogic.so: cannot open shared object file: No such file or directory)<br>
[CRITICAL][Qt] 28.11.2021 08:36:05 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Error(s):<br>
Cannot load library /home/vinny/Downloads/Slicer-4.13.0-2021-10-10-linux-amd64/NA-MIC/Extensions-30309/SlicerRT/lib/Slicer-4.13/qt-loadable-modules/libqSlicerPlmProtonDoseEngineModule.so: (libvtkSlicerPlmProtonDoseEngineModuleLogic.so: cannot open shared object file: No such file or directory)<br>
[CRITICAL][Qt] 28.11.2021 08:36:05 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Error(s):<br>
Cannot load library /home/vinny/Downloads/Slicer-4.13.0-2021-10-10-linux-amd64/NA-MIC/Extensions-30309/SlicerRT/lib/Slicer-4.13/qt-loadable-modules/libqSlicerRoomsEyeViewModule.so: (libvtkSlicerRoomsEyeViewModuleLogic.so: cannot open shared object file: No such file or directory)<br>
[CRITICAL][Qt] 28.11.2021 08:36:05 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Error(s):<br>
Cannot load library /home/vinny/Downloads/Slicer-4.13.0-2021-10-10-linux-amd64/NA-MIC/Extensions-30309/SlicerRT/lib/Slicer-4.13/qt-loadable-modules/libqSlicerSegmentComparisonModule.so: (libvtkSlicerSegmentComparisonModuleLogic.so: cannot open shared object file: No such file or directory)<br>
[CRITICAL][Qt] 28.11.2021 08:36:05 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Error(s):<br>
Cannot load library /home/vinny/Downloads/Slicer-4.13.0-2021-10-10-linux-amd64/NA-MIC/Extensions-30309/SlicerRT/lib/Slicer-4.13/qt-loadable-modules/libqSlicerVffFileReaderModule.so: (libvtkSlicerVffFileReaderLogic.so: cannot open shared object file: No such file or directory)<br>
[CRITICAL][Qt] 28.11.2021 08:36:05 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Error(s):<br>
Cannot load library /home/vinny/Downloads/Slicer-4.13.0-2021-10-10-linux-amd64/NA-MIC/Extensions-30309/SlicerFreeSurfer/lib/Slicer-4.13/qt-loadable-modules/libqSlicerFreeSurferImporterModule.so: (libvtkSlicerFreeSurferImporterModuleLogic.so: cannot open shared object file: No such file or directory)<br>
[CRITICAL][Qt] 28.11.2021 08:36:05 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   Error(s):<br>
Cannot load library /home/vinny/Downloads/Slicer-4.13.0-2021-10-10-linux-amd64/NA-MIC/Extensions-30309/SlicerFreeSurfer/lib/Slicer-4.13/qt-loadable-modules/libqSlicerFreeSurferMarkupsModule.so: (libvtkSlicerFreeSurferMarkupsModuleLogic.so: cannot open shared object file: No such file or directory)<br>
[DEBUG][Python] 28.11.2021 08:36:08 [Python] (/home/vinny/Downloads/Slicer-4.13.0-2021-10-10-linux-amd64/lib/Slicer-4.13/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[WARNING][Qt] 28.11.2021 08:36:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - When loading module  “BatchStructureSetConversion” , the dependency “DicomRtImportExport” failed to be loaded.<br>
[CRITICAL][Stream] 28.11.2021 08:36:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - libvtkSlicerDoseComparisonModuleLogic.so: cannot open shared object file: No such file or directory<br>
[CRITICAL][Stream] 28.11.2021 08:36:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - libvtkSlicerPlastimatchPyModuleLogic.so: cannot open shared object file: No such file or directory<br>
[CRITICAL][Stream] 28.11.2021 08:36:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - libvtkSlicerBeamsModuleLogic.so: cannot open shared object file: No such file or directory<br>
[CRITICAL][Stream] 28.11.2021 08:36:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - libvtkSlicerPlanarImageModuleLogic.so: cannot open shared object file: No such file or directory<br>
[CRITICAL][Stream] 28.11.2021 08:36:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - libvtkSlicerDoseVolumeHistogramModuleLogic.so: cannot open shared object file: No such file or directory<br>
[CRITICAL][Stream] 28.11.2021 08:36:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - libvtkSlicerDoseAccumulationModuleLogic.so: cannot open shared object file: No such file or directory<br>
[CRITICAL][Stream] 28.11.2021 08:36:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - libvtkSlicerDrrImageComputationModuleLogic.so: cannot open shared object file: No such file or directory<br>
[CRITICAL][Stream] 28.11.2021 08:36:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - libvtkSlicerExternalBeamPlanningModuleLogic.so: cannot open shared object file: No such file or directory<br>
[CRITICAL][Stream] 28.11.2021 08:36:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - libvtkSlicerDicomRtImportExportModuleLogic.so: cannot open shared object file: No such file or directory<br>
[CRITICAL][Stream] 28.11.2021 08:36:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - libvtkSlicerSegmentComparisonModuleLogic.so: cannot open shared object file: No such file or directory<br>
[CRITICAL][Stream] 28.11.2021 08:36:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - libvtkSlicerIsodoseModuleLogic.so: cannot open shared object file: No such file or directory<br>
[CRITICAL][Stream] 28.11.2021 08:36:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - libvtkSlicerDicomSroImportExportModuleLogic.so: cannot open shared object file: No such file or directory<br>
[CRITICAL][Stream] 28.11.2021 08:36:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - libvtkSlicerRoomsEyeViewModuleLogic.so: cannot open shared object file: No such file or directory<br>
[CRITICAL][Stream] 28.11.2021 08:36:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - libvtkSlicerPlmProtonDoseEngineModuleLogic.so: cannot open shared object file: No such file or directory<br>
[CRITICAL][Stream] 28.11.2021 08:36:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - libvtkSlicerDoseVolumeHistogramModuleMRML.so: cannot open shared object file: No such file or directory<br>
[CRITICAL][Stream] 28.11.2021 08:36:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - libvtkSlicerBeamsModuleMRML.so: cannot open shared object file: No such file or directory<br>
[CRITICAL][Stream] 28.11.2021 08:36:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - libvtkSlicerDrrImageComputationModuleMRML.so: cannot open shared object file: No such file or directory<br>
[CRITICAL][Stream] 28.11.2021 08:36:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - libqSlicerBeamsSubjectHierarchyPlugins.so: cannot open shared object file: No such file or directory<br>
[CRITICAL][Stream] 28.11.2021 08:36:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - libqSlicerDrrImageComputationModuleWidgets.so: cannot open shared object file: No such file or directory<br>
[CRITICAL][Stream] 28.11.2021 08:36:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - libqSlicerBeamsModuleWidgets.so: cannot open shared object file: No such file or directory<br>
[CRITICAL][Stream] 28.11.2021 08:36:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - libqSlicerExternalBeamPlanningModuleWidgets.so: cannot open shared object file: No such file or directory<br>
[CRITICAL][Stream] 28.11.2021 08:36:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - libqSlicerDoseComparisonSubjectHierarchyPlugins.so: cannot open shared object file: No such file or directory<br>
[CRITICAL][Stream] 28.11.2021 08:36:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - libqSlicerDoseVolumeHistogramSubjectHierarchyPlugins.so: cannot open shared object file: No such file or directory<br>
[CRITICAL][Stream] 28.11.2021 08:36:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - libqSlicerPlmProtonDoseEngineDoseEngines.so: cannot open shared object file: No such file or directory<br>
[CRITICAL][Stream] 28.11.2021 08:36:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - libqSlicerIsodoseSubjectHierarchyPlugins.so: cannot open shared object file: No such file or directory<br>
[CRITICAL][Stream] 28.11.2021 08:36:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - libqSlicerDicomRtImportExportSubjectHierarchyPlugins.so: cannot open shared object file: No such file or directory<br>
[WARNING][Qt] 28.11.2021 08:36:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - When loading module  “DvhComparison” , the dependency “DoseVolumeHistogram” failed to be loaded.<br>
[WARNING][Qt] 28.11.2021 08:36:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - When loading module  “IGRTWorkflow_SelfTest” , the dependency “DicomRtImportExport” failed to be loaded.<br>
[DEBUG][Python] 28.11.2021 08:36:08 [Python] (/home/vinny/Downloads/Slicer-4.13.0-2021-10-10-linux-amd64/lib/Slicer-4.13/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 28.11.2021 08:36:08 [Python] (/home/vinny/Downloads/Slicer-4.13.0-2021-10-10-linux-amd64/lib/Slicer-4.13/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 28.11.2021 08:36:08 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Switch to module:  “Welcome”<br>
[INFO][Stream] 28.11.2021 08:36:09 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Loading Slicer RC file [/home/vinny/.slicerrc.py]</p>

---

## Post #4 by @pieper (2021-11-28 13:51 UTC)

<aside class="quote no-group" data-username="Vinny" data-post="3" data-topic="20816">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vinny/48/7052_2.png" class="avatar"> Vinny:</div>
<blockquote>
<p>Cannot load library /home/vinny/Downloads/Slicer-4.13.0-2021-10-10-linux-amd64/NA-MIC/Extensions-30309/SlicerFreeSurfer/lib/Slicer-4.13/qt-loadable-modules/libqSlicerFreeSurferImporterModule.so: (libvtkSlicerFreeSurferImporterModuleLogic.so: cannot open shared object file: No such file or directory)<br>
[CRITICAL][Qt] 28.11.2021 08:36:05 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - Error(s):<br>
Cannot load library /home/vinny/Downloads/Slicer-4.13.0-2021-10-10-linux-amd64/NA-MIC/Extensions-30309/SlicerFreeSurfer/lib/Slicer-4.13/qt-loadable-modules/libqSlicerFreeSurferMarkupsModule.so: (libvtkSlicerFreeSurferMarkupsModuleLogic.so: cannot open shared object file: No such file or directory)</p>
</blockquote>
</aside>
<p>Looks like this path is either deleted or corrupted somehow.  You can investigate if those files or missing or just reinstall using the current preview version.</p>

---

## Post #5 by @Vinny (2021-11-28 14:24 UTC)

<p>Thanks <a class="mention" href="/u/pieper">@pieper</a>.  Actually, I think I figured out my problem.  When I cd into the Slicer directory and execute Slicer from terminal by typing ‘Slicer’, Slicer is launched but some of those paths are corrupted as you had mentioned.  But when I launch Slicer with ‘./Slicer’, I get no such error message, and everything loads fine.</p>

---

## Post #6 by @pieper (2021-11-28 14:46 UTC)

<p>Ah, interesting.  Probably this means you have “.” in your PATH variable.  Usually this is discouraged for security reasons (e.g. any directory with an executable named ‘ls’ be executed by mistake).  In any case it seems running Slicer that way messes up the directory calculations.</p>

---

## Post #7 by @hherhold (2021-11-28 15:06 UTC)

<p>Or his PATH could include a dir that points to another Slicer executable, and when he runs ./Slicer it’s running the correct one?</p>
<p>But yes, you should make sure . is not in your PATH by running <code>echo $PATH</code>.</p>

---

## Post #8 by @hherhold (2021-11-28 15:07 UTC)

<p>(this would only be the case, of course, if he has multiple slicer executables.)</p>

---

## Post #9 by @Vinny (2021-11-28 16:18 UTC)

<p><a class="mention" href="/u/hherhold">@hherhold</a>: that’s right I more than one Slicer version installed.  When I ran echo $PATH, the stable release was on the path.  I’ll have to edit my bashrc file to point to the correct Slicer version.  Or just execute the Slicer executable from that specific directory using ‘./Slicer’.</p>
<p>Thanks!</p>

---

## Post #10 by @hherhold (2021-11-28 16:43 UTC)

<p>You can use <code>which</code> to tell you where in your <code>PATH</code> your shell is finding executables. For example:</p>
<pre><code>&gt; which ps
/bin/ps</code></pre>

---

## Post #11 by @Vinny (2021-11-28 16:58 UTC)

<p>so I ran <code>which Slicer</code> and the path points to the stable release as in the .bashrc file.  If I cd into the Slicer preview release folder and launch Slicer with ‘Slicer’, the preview release is launched, not the stable version.</p>

---

## Post #12 by @hherhold (2021-11-28 17:03 UTC)

<p>Then you might have <code>.</code> in your path. What does <code>echo $PATH</code> say?</p>

---

## Post #13 by @Vinny (2021-11-28 17:14 UTC)

<p>Here is what I get when I run echo $PATH…<br>
echo $PATH<br>
/home/vinny/Tools/dtk:/home/vinny/Tools/camino/bin:/usr/lib/jvm/java-11-oracle/bin:/home/vinny/Tools/rstudio-1.2.5019/bin:/home/vinny/Tools/Slicer-4.11.20200930-linux-amd64:/home/vinny/Tools/leaddbs/application:/home/vinny/Tools/dramms/bin:/home/vinny/Tools/freesurferv7.1.1/bin:/home/vinny/Tools/freesurferv7.1.1/fsfast/bin:/home/vinny/Tools/freesurferv7.1.1/tktools:/home/vinny/Tools/fsl/bin:/home/vinny/Tools/freesurferv7.1.1/mni/bin:/home/vinny/Tools/ants/bin:/home/vinny/Tools/fsl/bin:/home/vinny/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/vinny/Tools/niftyreg_install/bin:/home/vinny/Tools/julia/JuliaPro-1.4.1-1</p>
<p>Another thing, if I point the bashrc to the stable release Slicer 4.11.20210226 (latest stable linux release), then there is no path errors and failed import modules if I run the ‘Slicer’ command from the preview release folder (which launches the preview release version).<br>
However, if the older stable release Slicer 4.11.20200930 is on the path, this is where the errors occurred.  Note no errors occurred for the older stable release was executed from its own folder, only when instantiating for a different Slicer version.</p>

---

## Post #14 by @hherhold (2021-11-28 17:21 UTC)

<p>OK, that’s kind of odd - not sure what’s happening with that, but at least you don’t have <code>.</code> in your path (which is a good thing).</p>
<p>It’s often a good idea to give the full path when running an executable from the command line. You can set up an alias to it to make it a little easier.</p>

---

## Post #15 by @Vinny (2021-11-28 17:25 UTC)

<p>Thanks <a class="mention" href="/u/hherhold">@hherhold</a>.  Setting up an alias is a good idea for this.</p>

---
