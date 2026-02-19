---
topic_id: 41445
title: "Build Slicer With Slicerrt"
date: 2025-02-02
url: https://discourse.slicer.org/t/41445
---

# Build Slicer with SlicerRT

**Topic ID**: 41445
**Date**: 2025-02-02
**URL**: https://discourse.slicer.org/t/build-slicer-with-slicerrt/41445

---

## Post #1 by @SSDad (2025-02-02 00:25 UTC)

<p>I am trying to follow this website to add SlicerRT Extension to Slicer</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/SlicerRt/SlicerRT/wiki/SlicerRt-developers-page">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerRt/SlicerRT/wiki/SlicerRt-developers-page" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/02ae8fef4b304901951d52a6e07174797dca774e0a425133cbdd5c6a8c20d652/SlicerRt/SlicerRT" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/SlicerRt/SlicerRT/wiki/SlicerRt-developers-page" target="_blank" rel="noopener nofollow ugc">SlicerRt developers page</a></h3>

  <p>Open-source toolkit for radiation therapy research, an extension of 3D Slicer. Features include DICOM-RT import/export, dose volume histogram, dose accumulation, external beam planning (TPS), struc...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I have a couple questions here.</p>
<ol>
<li>
<p>What does the following sentence mean?<br>
" * When configuring the project set the Slicer_DIR to the Slicer version that you have built (e.g., c:/d/S4D/Slicer-build)"</p>
</li>
<li>
<p>Where is ‘SlicerRT.sln’?  I just cannot find it from the repo?<br>
“* Open SlicerRT.sln, select the Debug/Release configuration that matches the configuration that used for Slicer build, and build ALL_BUILD”</p>
</li>
</ol>
<p>Any help will be appreciated!</p>

---

## Post #2 by @cpinter (2025-02-03 10:10 UTC)

<p>When building SlicerRT you need to point to an existing Slicer build. The line means specifying the directory in CMake before starting the build<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b84417ec4629dc2c3ceb4a8f70bff2c81feebcb.png" data-download-href="/uploads/short-url/3VqfpmxuWn5rUfzQKrsknEphD5N.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1b84417ec4629dc2c3ceb4a8f70bff2c81feebcb.png" alt="image" data-base62-sha1="3VqfpmxuWn5rUfzQKrsknEphD5N" width="647" height="500" data-dominant-color="EF8F90"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1063×821 46.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Or if you configure in command line:<br>
<code>cmake -G "Visual Studio 17 2022" -DSlicer_DIR:PATH=c:/d/%SLICER_SUPERBUILD_DIR_NAME%/Slicer-build %3 %SRC_DIR%</code></p>
<p>SlicerRT.sln will appear after successful configuration+generation with CMake.</p>

---

## Post #3 by @SSDad (2025-02-04 05:55 UTC)

<p>Hi <a class="mention" href="/u/cpinter">@cpinter</a> ,</p>
<p>Thanks a lot for your help.  I was able to generate SlicerRT.sln in the folder ‘B’ by</p>
<p>‘PS D:\OA\SlicerRT\B&gt; cmake -G “Visual Studio 17 2022” -DSlicer_DIR:PATH=D:\OA\Slicer\D\Slicer-build D:\OA\SlicerRT\S’</p>
<p>and then loaded the SlicerRT.sln in Visual Studio to build the binary.</p>
<p>However, after adding the paths as the following</p>
<ul>
<li>Start Slicer and in the application settings add the following additional module paths (replace Debug by Release if you are testing in Release mode):
<ul>
<li>\inner-build\lib\Slicer-4.11\cli-modules</li>
<li>\inner-build\lib\Slicer-4.11\qt-scripted-modules</li>
<li>\inner-build\lib\Slicer-4.11\qt-loadable-modules</li>
</ul>
</li>
</ul>
<p>and restarted Slicer, I had the following in the terminal</p>
<hr>
<p>DLL load failed while importing vtkSlicerDicomRtImportExportModuleLogicPython: The specified module could not be found.<br>
DLL load failed while importing vtkSlicerDicomSroImportExportModuleLogicPython: The specified module could not be found.DLL load failed while importing vtkSlicerDicomSroImportExportModuleLogicPython: The specified module could not be found.DLL load failed while importing vtkSlicerDicomSroImportExportModuleLogicPython: The specified module could not be found.DLL load failed while importing vtkSlicerDicomSroImportExportModuleLogicPython: The specified module could not be found.DLL load failed while importing vtkSlicerDrrImageComputationModuleLogicPython: The specified module could not be found.<br>
DLL load failed while importing vtkSlicerDrrImageComputationModuleLogicPython: The specified module could not be found.<br>
DLL load failed while importing vtkSlicerDrrImageComputationModuleLogicPython: The specified module could not be found.<br>
DLL load failed while importing vtkSlicerDrrImageComputationModuleLogicPython: The specified module could not be found.<br>
Failed to load vtkSlicerExternalBeamPlanningModuleLogicPython: No module named vtkSlicerBeamsModuleLogicPython<br>
Failed to load vtkSlicerExternalBeamPlanningModuleLogicPython: No module named vtkSlicerBeamsModuleLogicPython<br>
Failed to load vtkSlicerExternalBeamPlanningModuleLogicPython: No module named vtkSlicerBeamsModuleLogicPython<br>
Failed to load vtkSlicerExternalBeamPlanningModuleLogicPython: No module named vtkSlicerBeamsModuleLogicPython<br>
DLL load failed while importing vtkSlicerRoomsEyeViewModuleLogicPython: The specified module could not be found.<br>
DLL load failed while importing vtkSlicerRoomsEyeViewModuleLogicPython: The specified module could not be found.<br>
DLL load failed while importing vtkSlicerRoomsEyeViewModuleLogicPython: The specified module could not be found.<br>
DLL load failed while importing vtkSlicerRoomsEyeViewModuleLogicPython: The specified module could not be found.<br>
DLL load failed while importing qSlicerBeamsModuleWidgetsPythonQt: The specified module could not be found.<br>
DLL load failed while importing qSlicerBeamsModuleWidgetsPythonQt: The specified module could not be found.<br>
DLL load failed while importing qSlicerBeamsModuleWidgetsPythonQt: The specified module could not be found.<br>
DLL load failed while importing qSlicerBeamsModuleWidgetsPythonQt: The specified module could not be found.<br>
DLL load failed while importing qSlicerExternalBeamPlanningModuleWidgetsPythonQt: The specified module could not be found.<br>
DLL load failed while importing qSlicerExternalBeamPlanningModuleWidgetsPythonQt: The specified module could not be found.<br>
DLL load failed while importing qSlicerExternalBeamPlanningModuleWidgetsPythonQt: The specified module could not be found.<br>
DLL load failed while importing qSlicerExternalBeamPlanningModuleWidgetsPythonQt: The specified module could not be found.<br>
DLL load failed while importing qSlicerPlmProtonDoseEngineDoseEnginesPythonQt: The specified module could not be found.<br>
DLL load failed while importing qSlicerPlmProtonDoseEngineDoseEnginesPythonQt: The specified module could not be found.<br>
DLL load failed while importing qSlicerPlmProtonDoseEngineDoseEnginesPythonQt: The specified module could not be found.<br>
DLL load failed while importing qSlicerPlmProtonDoseEngineDoseEnginesPythonQt: The specified module could not be found.<br>
When loading module  “BatchStructureSetConversion” , the dependency “DicomRtImportExport” failed to be loaded.<br>
When loading module  “DvhComparison” , the dependency “DoseVolumeHistogram” failed to be loaded.<br>
When loading module  “IGRTWorkflow_SelfTest” , the dependency “DicomRtImportExport” failed to be loaded.<br>
Switch to module:  “Welcome”</p>
<hr>
<p>The problem seems qt/python related.  Any idea how to fix?</p>

---

## Post #4 by @cpinter (2025-02-04 09:59 UTC)

<p>First of all, make sure the module paths are valid (I doubt you built 4.11).</p>
<p>The DLL loading errors are due to not all paths being explored for loading dependencies, i.e. missing paths. One workaround you can do is to copy the DLLs from <code>...\SlicerRT_R\bin\Release\*.dll</code> to <code>\SlicerRT_R\inner-build\lib\Slicer-5.7\qt-loadable-modules\Release</code>, but this is not a proper solution. It is recommended to use the <code>inner-build\SlicerWithSlicerRT.exe</code> file for starting SlicerRT, which sets up all the paths.</p>
<p>If you need this for debugging, then start VS like this<br>
<code>..\S5D\Slicer-build\Slicer.exe --VisualStudio --launcher-no-splash --launcher-additional-settings ./SlicerRT_D/inner-build/AdditionalLauncherSettings.ini c:\d\_Extensions\SlicerRT_D\inner-build\SlicerRT.sln</code></p>

---

## Post #5 by @SSDad (2025-02-04 22:43 UTC)

<p>Hi <a class="mention" href="/u/cpinter">@cpinter</a> ,</p>
<p>Thanks again!</p>
<p>You are right, my Slicer version is 5.7.</p>
<p>Now I can start SlicerRT by running ‘inner-build\SlicerWithSlicerRT.exe’.</p>
<p>But when I try ‘./Slicer.exe --VisualStudio --launcher-no-splash --launcher-additional-settings D:\OA\SlicerRT\B/inner-build/AdditionalLauncherSettings.ini D:\OA\SlicerRT\B\inner-build\SlicerRT.sln’ in VS and run debug (ALL_BUILD is set as Startup Project), I got a pop up said ‘Unable to start program ‘.\SlicerRT\inner-build\x64\Debug\All_BUILD’, access is denied’  (sorry I do know how to post images here).  Any idea?</p>

---

## Post #6 by @cpinter (2025-02-05 11:45 UTC)

<p>You need to specify the executable for your startup project (which you need to change to basically any other project). Please see in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/debugging/windowscpp.html#debugging-using-visual-studio">developer documentation</a>.</p>

---
