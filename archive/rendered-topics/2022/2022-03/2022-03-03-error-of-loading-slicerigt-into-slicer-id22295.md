# Error of loading SlicerIGT into Slicer

**Topic ID**: 22295
**Date**: 2022-03-03
**URL**: https://discourse.slicer.org/t/error-of-loading-slicerigt-into-slicer/22295

---

## Post #1 by @user5 (2022-03-03 19:25 UTC)

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

## Post #2 by @cpinter (2022-03-04 10:31 UTC)

<p>2 posts were merged into an existing topic: <a href="/t/slicerigt-cannot-use/22266">SlicerIGT cannot use</a></p>

---

## Post #3 by @cpinter (2022-03-04 10:31 UTC)



---
