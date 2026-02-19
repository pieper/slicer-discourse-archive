---
topic_id: 22266
title: "Slicerigt Cannot Use"
date: 2022-03-02
url: https://discourse.slicer.org/t/22266
---

# SlicerIGT cannot use

**Topic ID**: 22266
**Date**: 2022-03-02
**URL**: https://discourse.slicer.org/t/slicerigt-cannot-use/22266

---

## Post #1 by @user5 (2022-03-02 17:05 UTC)

<p>I have built a Slicer project with SlicerVR. I would like to use SlicerIGT in my project, so I directly install SlicerIGT and SlicerIGTLink in extensions-manager. Although I installed it successfully, it cannot open normally which is coming out those error,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb619581c151e1d6c0f1473f6619da95ae0ef1ba.png" data-download-href="/uploads/short-url/xAhhfV4ohZQDkhhP9mRmgMdEHiy.png?dl=1" title="233" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb619581c151e1d6c0f1473f6619da95ae0ef1ba.png" alt="233" data-base62-sha1="xAhhfV4ohZQDkhhP9mRmgMdEHiy" width="690" height="194" data-dominant-color="FDECEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">233</span><span class="informations">1356×383 10.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Why those error is coming out suddenly? I do not any problem of installing SlicerIGT in normal release version.<br>
How can I fix it?</p>

---

## Post #2 by @user5 (2022-03-03 13:10 UTC)

<p>I have already followed this link to download Visual C++ runtime to fix the problem, but it does not work.</p>
<blockquote>
<p><a href="https://github.com/Slicer/Slicer/issues/4958" class="inline-onebox" rel="noopener nofollow ugc">Slicer modules fail to load · Issue #4958 · Slicer/Slicer · GitHub</a></p>
</blockquote>
<p>It is the error in CMD.</p>
<pre><code class="lang-auto">Warning: QT_DEVICE_PIXEL_RATIO is deprecated. Instead use:
   QT_AUTO_SCREEN_SCALE_FACTOR to enable platform plugin controlled per-screen factors.
   QT_SCREEN_SCALE_FACTORS to set per-screen factors.
   QT_SCALE_FACTOR to set the application global scale factor.
Warning: QT_DEVICE_PIXEL_RATIO is deprecated. Instead use:
   QT_AUTO_SCREEN_SCALE_FACTOR to enable platform plugin controlled per-screen factors.
   QT_SCREEN_SCALE_FACTORS to set per-screen DPI.
   QT_SCALE_FACTOR to set the application global scale factor.
  Error(s):
    Cannot load library C:\D\S4R\Slicer_build_2\Slicer-build\NA-MIC\Extensions-30625\SlicerIGT\lib\Slicer-4.13\qt-loadable-modules\qSlicerBreachWarningModule.dll: The specified module could not be found.
  Error(s):
    Cannot load library C:\D\S4R\Slicer_build_2\Slicer-build\NA-MIC\Extensions-30625\SlicerIGT\lib\Slicer-4.13\qt-loadable-modules\qSlicerCollectPointsModule.dll: The specified module could not be found.
  Error(s):
    Cannot load library C:\D\S4R\Slicer_build_2\Slicer-build\NA-MIC\Extensions-30625\SlicerIGT\lib\Slicer-4.13\qt-loadable-modules\qSlicerCreateModelsModule.dll: The specified module could not be found.
  Error(s):
    Cannot load library C:\D\S4R\Slicer_build_2\Slicer-build\NA-MIC\Extensions-30625\SlicerIGT\lib\Slicer-4.13\qt-loadable-modules\qSlicerFiducialRegistrationWizardModule.dll: The specified module could not be found.
  Error(s):
    Cannot load library C:\D\S4R\Slicer_build_2\Slicer-build\NA-MIC\Extensions-30625\SlicerIGT\lib\Slicer-4.13\qt-loadable-modules\qSlicerPathExplorerModule.dll: The specified module could not be found.
  Error(s):
    Cannot load library C:\D\S4R\Slicer_build_2\Slicer-build\NA-MIC\Extensions-30625\SlicerIGT\lib\Slicer-4.13\qt-loadable-modules\qSlicerPivotCalibrationModule.dll: The specified module could not be found.
  Error(s):
    Cannot load library C:\D\S4R\Slicer_build_2\Slicer-build\NA-MIC\Extensions-30625\SlicerIGT\lib\Slicer-4.13\qt-loadable-modules\qSlicerTransformProcessorModule.dll: The specified module could not be found.
  Error(s):
    Cannot load library C:\D\S4R\Slicer_build_2\Slicer-build\NA-MIC\Extensions-30625\SlicerIGT\lib\Slicer-4.13\qt-loadable-modules\qSlicerUltrasoundSnapshotsModule.dll: The specified module could not be found.
  Error(s):
    Cannot load library C:\D\S4R\Slicer_build_2\Slicer-build\NA-MIC\Extensions-30625\SlicerIGT\lib\Slicer-4.13\qt-loadable-modules\qSlicerVolumeResliceDriverModule.dll: The specified module could not be found.
  Error(s):
    Cannot load library C:\D\S4R\Slicer_build_2\Slicer-build\NA-MIC\Extensions-30625\SlicerIGT\lib\Slicer-4.13\qt-loadable-modules\qSlicerWatchdogModule.dll: The specified module could not be found.
  Error(s):
    Cannot load library C:\D\S4R\Slicer_build_2\Slicer-build\NA-MIC\Extensions-30625\SlicerOpenIGTLink\lib\Slicer-4.13\qt-loadable-modules\qSlicerOpenIGTLinkIFModule.dll: The specified module could not be found.
  Error(s):
    Cannot load library C:\D\S4R\Slicer_build_2\Slicer-build\NA-MIC\Extensions-30625\SlicerOpenIGTLink\lib\Slicer-4.13\qt-loadable-modules\qSlicerOpenIGTLinkRemoteModule.dll: The specified module could not be found.
  Error(s):
    Cannot load library C:\D\S4R\Slicer_build_2\Slicer-build\NA-MIC\Extensions-30625\SlicerOpenIGTLink\lib\Slicer-4.13\qt-loadable-modules\qSlicerPlusRemoteModule.dll: The specified module could not be found.
When loading module  "BreachWarningSelfTest" , the dependency "CreateModels" failed to be loaded.
DLL load failed while importing vtkSlicerBreachWarningModuleLogicPython: The specified module could not be found.
DLL load failed while importing vtkSlicerCollectPointsModuleLogicPython: The specified module could not be found.
DLL load failed while importing vtkSlicerCreateModelsModuleLogicPython: The specified module could not be found.
DLL load failed while importing vtkSlicerFiducialRegistrationWizardModuleLogicPython: The specified module could not be found.
DLL load failed while importing vtkSlicerPathExplorerModuleLogicPython: The specified module could not be found.
DLL load failed while importing vtkSlicerPivotCalibrationModuleLogicPython: The specified module could not be found.
DLL load failed while importing vtkSlicerTransformProcessorModuleLogicPython: The specified module could not be found.
DLL load failed while importing vtkSlicerUltrasoundSnapshotsModuleLogicPython: The specified module could not be found.
DLL load failed while importing vtkSlicerVolumeResliceDriverModuleLogicPython: The specified module could not be found.
DLL load failed while importing vtkSlicerWatchdogModuleLogicPython: The specified module could not be found.
DLL load failed while importing vtkSlicerBreachWarningModuleMRMLPython: The specified module could not be found.
DLL load failed while importing vtkSlicerCollectPointsModuleMRMLPython: The specified module could not be found.
DLL load failed while importing vtkSlicerFiducialRegistrationWizardModuleMRMLPython: The specified module could not be found.
DLL load failed while importing vtkSlicerPathExplorerModuleMRMLPython: The specified module could not be found.
DLL load failed while importing vtkSlicerTransformProcessorModuleMRMLPython: The specified module could not be found.
DLL load failed while importing vtkSlicerWatchdogModuleMRMLPython: The specified module could not be found.
DLL load failed while importing vtkSlicerWatchdogModuleMRMLDisplayableManagerPython: The specified module could not be found.
DLL load failed while importing qSlicerFiducialRegistrationWizardModuleWidgetsPythonQt: The specified module could not be found.
DLL load failed while importing qSlicerPathExplorerModuleWidgetsPythonQt: The specified module could not be found.
DLL load failed while importing qSlicerPathExplorerSubjectHierarchyPluginsPythonQt: The specified module could not be found.
DLL load failed while importing qSlicerVolumeResliceDriverModuleWidgetsPythonQt: The specified module could not be found.
When loading module  "UltrasoundRemoteControl" , the dependency "OpenIGTLinkRemote" failed to be loaded.
</code></pre>

---

## Post #3 by @user5 (2022-03-03 19:25 UTC)

<p>I have built a Slicer project with SlicerVR. I would like to use SlicerIGT in my project, so I directly install SlicerIGT and SlicerIGTLink in extensions-manager. Although I installed it successfully, it cannot open normally which is coming out those error,</p>
<pre><code class="lang-auto">Warning: QT_DEVICE_PIXEL_RATIO is deprecated. Instead use:
   QT_AUTO_SCREEN_SCALE_FACTOR to enable platform plugin controlled per-screen factors.
   QT_SCREEN_SCALE_FACTORS to set per-screen factors.
   QT_SCALE_FACTOR to set the application global scale factor.
Warning: QT_DEVICE_PIXEL_RATIO is deprecated. Instead use:
   QT_AUTO_SCREEN_SCALE_FACTOR to enable platform plugin controlled per-screen factors.
   QT_SCREEN_SCALE_FACTORS to set per-screen DPI.
   QT_SCALE_FACTOR to set the application global scale factor.
  Error(s):
    Cannot load library C:\D\S4R\Slicer_build_2\Slicer-build\NA-MIC\Extensions-30625\SlicerIGT\lib\Slicer-4.13\qt-loadable-modules\qSlicerBreachWarningModule.dll: The specified module could not be found.
  Error(s):
    Cannot load library C:\D\S4R\Slicer_build_2\Slicer-build\NA-MIC\Extensions-30625\SlicerIGT\lib\Slicer-4.13\qt-loadable-modules\qSlicerCollectPointsModule.dll: The specified module could not be found.
  Error(s):
    Cannot load library C:\D\S4R\Slicer_build_2\Slicer-build\NA-MIC\Extensions-30625\SlicerIGT\lib\Slicer-4.13\qt-loadable-modules\qSlicerCreateModelsModule.dll: The specified module could not be found.
  Error(s):
    Cannot load library C:\D\S4R\Slicer_build_2\Slicer-build\NA-MIC\Extensions-30625\SlicerIGT\lib\Slicer-4.13\qt-loadable-modules\qSlicerFiducialRegistrationWizardModule.dll: The specified module could not be found.
  Error(s):
    Cannot load library C:\D\S4R\Slicer_build_2\Slicer-build\NA-MIC\Extensions-30625\SlicerIGT\lib\Slicer-4.13\qt-loadable-modules\qSlicerPathExplorerModule.dll: The specified module could not be found.
  Error(s):
    Cannot load library C:\D\S4R\Slicer_build_2\Slicer-build\NA-MIC\Extensions-30625\SlicerIGT\lib\Slicer-4.13\qt-loadable-modules\qSlicerPivotCalibrationModule.dll: The specified module could not be found.
  Error(s):
    Cannot load library C:\D\S4R\Slicer_build_2\Slicer-build\NA-MIC\Extensions-30625\SlicerIGT\lib\Slicer-4.13\qt-loadable-modules\qSlicerTransformProcessorModule.dll: The specified module could not be found.
  Error(s):
    Cannot load library C:\D\S4R\Slicer_build_2\Slicer-build\NA-MIC\Extensions-30625\SlicerIGT\lib\Slicer-4.13\qt-loadable-modules\qSlicerUltrasoundSnapshotsModule.dll: The specified module could not be found.
  Error(s):
    Cannot load library C:\D\S4R\Slicer_build_2\Slicer-build\NA-MIC\Extensions-30625\SlicerIGT\lib\Slicer-4.13\qt-loadable-modules\qSlicerVolumeResliceDriverModule.dll: The specified module could not be found.
  Error(s):
    Cannot load library C:\D\S4R\Slicer_build_2\Slicer-build\NA-MIC\Extensions-30625\SlicerIGT\lib\Slicer-4.13\qt-loadable-modules\qSlicerWatchdogModule.dll: The specified module could not be found.
  Error(s):
    Cannot load library C:\D\S4R\Slicer_build_2\Slicer-build\NA-MIC\Extensions-30625\SlicerOpenIGTLink\lib\Slicer-4.13\qt-loadable-modules\qSlicerOpenIGTLinkIFModule.dll: The specified module could not be found.
  Error(s):
    Cannot load library C:\D\S4R\Slicer_build_2\Slicer-build\NA-MIC\Extensions-30625\SlicerOpenIGTLink\lib\Slicer-4.13\qt-loadable-modules\qSlicerOpenIGTLinkRemoteModule.dll: The specified module could not be found.
  Error(s):
    Cannot load library C:\D\S4R\Slicer_build_2\Slicer-build\NA-MIC\Extensions-30625\SlicerOpenIGTLink\lib\Slicer-4.13\qt-loadable-modules\qSlicerPlusRemoteModule.dll: The specified module could not be found.
When loading module  "BreachWarningSelfTest" , the dependency "CreateModels" failed to be loaded.
DLL load failed while importing vtkSlicerBreachWarningModuleLogicPython: The specified module could not be found.
DLL load failed while importing vtkSlicerCollectPointsModuleLogicPython: The specified module could not be found.
DLL load failed while importing vtkSlicerCreateModelsModuleLogicPython: The specified module could not be found.
DLL load failed while importing vtkSlicerFiducialRegistrationWizardModuleLogicPython: The specified module could not be found.
DLL load failed while importing vtkSlicerPathExplorerModuleLogicPython: The specified module could not be found.
DLL load failed while importing vtkSlicerPivotCalibrationModuleLogicPython: The specified module could not be found.
DLL load failed while importing vtkSlicerTransformProcessorModuleLogicPython: The specified module could not be found.
DLL load failed while importing vtkSlicerUltrasoundSnapshotsModuleLogicPython: The specified module could not be found.
DLL load failed while importing vtkSlicerVolumeResliceDriverModuleLogicPython: The specified module could not be found.
DLL load failed while importing vtkSlicerWatchdogModuleLogicPython: The specified module could not be found.
DLL load failed while importing vtkSlicerBreachWarningModuleMRMLPython: The specified module could not be found.
DLL load failed while importing vtkSlicerCollectPointsModuleMRMLPython: The specified module could not be found.
DLL load failed while importing vtkSlicerFiducialRegistrationWizardModuleMRMLPython: The specified module could not be found.
DLL load failed while importing vtkSlicerPathExplorerModuleMRMLPython: The specified module could not be found.
DLL load failed while importing vtkSlicerTransformProcessorModuleMRMLPython: The specified module could not be found.
DLL load failed while importing vtkSlicerWatchdogModuleMRMLPython: The specified module could not be found.
DLL load failed while importing vtkSlicerWatchdogModuleMRMLDisplayableManagerPython: The specified module could not be found.
DLL load failed while importing qSlicerFiducialRegistrationWizardModuleWidgetsPythonQt: The specified module could not be found.
DLL load failed while importing qSlicerPathExplorerModuleWidgetsPythonQt: The specified module could not be found.
DLL load failed while importing qSlicerPathExplorerSubjectHierarchyPluginsPythonQt: The specified module could not be found.
DLL load failed while importing qSlicerVolumeResliceDriverModuleWidgetsPythonQt: The specified module could not be found.
When loading module  "UltrasoundRemoteControl" , the dependency "OpenIGTLinkRemote" failed to be loaded.
</code></pre>
<p>I have already followed this link to download Visual C++ runtime to fix the problem, but it does not work.</p>
<blockquote>
<p><a href="https://github.com/Slicer/Slicer/issues/4958" class="inline-onebox" rel="noopener nofollow ugc">Slicer modules fail to load · Issue #4958 · Slicer/Slicer · GitHub</a></p>
</blockquote>
<p>Why those error is coming out? How can I fix it?</p>

---

## Post #4 by @user5 (2022-03-04 10:21 UTC)

<p>I afraid that the problem is occurred by too long extension path, so I put the file into C drive to make the path being shorter. Unfortunately, it seem like not useful.</p>
<pre><code class="lang-auto">Warning: QT_DEVICE_PIXEL_RATIO is deprecated. Instead use:
   QT_AUTO_SCREEN_SCALE_FACTOR to enable platform plugin controlled per-screen factors.
   QT_SCREEN_SCALE_FACTORS to set per-screen factors.
   QT_SCALE_FACTOR to set the application global scale factor.
Warning: QT_DEVICE_PIXEL_RATIO is deprecated. Instead use:
   QT_AUTO_SCREEN_SCALE_FACTOR to enable platform plugin controlled per-screen factors.
   QT_SCREEN_SCALE_FACTORS to set per-screen DPI.
   QT_SCALE_FACTOR to set the application global scale factor.
  Error(s):
    Cannot load library C:\NA-MIC\SlicerIGT\lib\Slicer-4.13\qt-loadable-modules\qSlicerBreachWarningModule.dll: The specified module could not be found.
  Error(s):
    Cannot load library C:\NA-MIC\SlicerIGT\lib\Slicer-4.13\qt-loadable-modules\qSlicerCollectPointsModule.dll: The specified module could not be found.
  Error(s):
    Cannot load library C:\NA-MIC\SlicerIGT\lib\Slicer-4.13\qt-loadable-modules\qSlicerCreateModelsModule.dll: The specified module could not be found.
  Error(s):
    Cannot load library C:\NA-MIC\SlicerIGT\lib\Slicer-4.13\qt-loadable-modules\qSlicerFiducialRegistrationWizardModule.dll: The specified module could not be found.
  Error(s):
    Cannot load library C:\NA-MIC\SlicerIGT\lib\Slicer-4.13\qt-loadable-modules\qSlicerPathExplorerModule.dll: The specified module could not be found.
  Error(s):
    Cannot load library C:\NA-MIC\SlicerIGT\lib\Slicer-4.13\qt-loadable-modules\qSlicerPivotCalibrationModule.dll: The specified module could not be found.
  Error(s):
    Cannot load library C:\NA-MIC\SlicerIGT\lib\Slicer-4.13\qt-loadable-modules\qSlicerTransformProcessorModule.dll: The specified module could not be found.
  Error(s):
    Cannot load library C:\NA-MIC\SlicerIGT\lib\Slicer-4.13\qt-loadable-modules\qSlicerUltrasoundSnapshotsModule.dll: The specified module could not be found.
  Error(s):
    Cannot load library C:\NA-MIC\SlicerIGT\lib\Slicer-4.13\qt-loadable-modules\qSlicerVolumeResliceDriverModule.dll: The specified module could not be found.
  Error(s):
    Cannot load library C:\NA-MIC\SlicerIGT\lib\Slicer-4.13\qt-loadable-modules\qSlicerWatchdogModule.dll: The specified module could not be found.
  Error(s):
    Cannot load library C:\NA-MIC\SlicerOpenIGTLink\lib\Slicer-4.13\qt-loadable-modules\qSlicerOpenIGTLinkIFModule.dll: The specified module could not be found.
  Error(s):
    Cannot load library C:\NA-MIC\SlicerOpenIGTLink\lib\Slicer-4.13\qt-loadable-modules\qSlicerOpenIGTLinkRemoteModule.dll: The specified module could not be found.
  Error(s):
    Cannot load library C:\NA-MIC\SlicerOpenIGTLink\lib\Slicer-4.13\qt-loadable-modules\qSlicerPlusRemoteModule.dll: The specified module could not be found.
When loading module  "BreachWarningSelfTest" , the dependency "CreateModels" failed to be loaded.
DLL load failed while importing vtkSlicerBreachWarningModuleLogicPython: The specified module could not be found.
DLL load failed while importing vtkSlicerCollectPointsModuleLogicPython: The specified module could not be found.
DLL load failed while importing vtkSlicerCreateModelsModuleLogicPython: The specified module could not be found.
DLL load failed while importing vtkSlicerFiducialRegistrationWizardModuleLogicPython: The specified module could not be found.
DLL load failed while importing vtkSlicerPathExplorerModuleLogicPython: The specified module could not be found.
DLL load failed while importing vtkSlicerPivotCalibrationModuleLogicPython: The specified module could not be found.
DLL load failed while importing vtkSlicerTransformProcessorModuleLogicPython: The specified module could not be found.
DLL load failed while importing vtkSlicerUltrasoundSnapshotsModuleLogicPython: The specified module could not be found.
DLL load failed while importing vtkSlicerVolumeResliceDriverModuleLogicPython: The specified module could not be found.
DLL load failed while importing vtkSlicerWatchdogModuleLogicPython: The specified module could not be found.
DLL load failed while importing vtkSlicerBreachWarningModuleMRMLPython: The specified module could not be found.
DLL load failed while importing vtkSlicerCollectPointsModuleMRMLPython: The specified module could not be found.
DLL load failed while importing vtkSlicerFiducialRegistrationWizardModuleMRMLPython: The specified module could not be found.
DLL load failed while importing vtkSlicerPathExplorerModuleMRMLPython: The specified module could not be found.
DLL load failed while importing vtkSlicerTransformProcessorModuleMRMLPython: The specified module could not be found.
DLL load failed while importing vtkSlicerWatchdogModuleMRMLPython: The specified module could not be found.
DLL load failed while importing vtkSlicerWatchdogModuleMRMLDisplayableManagerPython: The specified module could not be found.
DLL load failed while importing qSlicerFiducialRegistrationWizardModuleWidgetsPythonQt: The specified module could not be found.
DLL load failed while importing qSlicerPathExplorerModuleWidgetsPythonQt: The specified module could not be found.
DLL load failed while importing qSlicerPathExplorerSubjectHierarchyPluginsPythonQt: The specified module could not be found.
DLL load failed while importing qSlicerVolumeResliceDriverModuleWidgetsPythonQt: The specified module could not be found.
</code></pre>
<p>I would like to ask that do everybody have any idea to fix it?</p>
<p>Thank you</p>

---

## Post #5 by @cpinter (2022-03-04 10:32 UTC)

<p>If you build Slicer, you will need to build all the extensions you want to use.</p>

---

## Post #6 by @user5 (2022-03-04 11:47 UTC)

<p>Thank you for your reply.<br>
So I need to add a new entry for each extension source file in CMake of Slicer master build. Am I right?</p>

---

## Post #7 by @cpinter (2022-03-04 14:21 UTC)

<aside class="quote no-group" data-username="user5" data-post="1" data-topic="22266">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/user5/48/13217_2.png" class="avatar"> user5:</div>
<blockquote>
<p>I have built a Slicer project with SlicerVR</p>
</blockquote>
</aside>
<p>You said you built SlicerVR for your Slicer. You need to do the same for all the other extensions too.</p>

---
