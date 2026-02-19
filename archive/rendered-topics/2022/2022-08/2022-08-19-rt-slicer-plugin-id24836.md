---
topic_id: 24836
title: "Rt Slicer Plugin"
date: 2022-08-19
url: https://discourse.slicer.org/t/24836
---

# RT Slicer Plugin

**Topic ID**: 24836
**Date**: 2022-08-19
**URL**: https://discourse.slicer.org/t/rt-slicer-plugin/24836

---

## Post #1 by @Vesa_Alexandru (2022-08-19 14:13 UTC)

<p>Hello !<br>
I’m running the docker version of 3D-slicer : <a href="https://github.com/Slicer/SlicerDocker" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Slicer/SlicerDocker: Build, package, test, and run 3D Slicer and Slicer Extensions in Docker.</a></p>
<p>I have a problem when i’m trying to export the RT contour . I have also installed all the plugins.</p>
<p>"Failed to export using plugin DicomRtImportExportPluginClass<br>
Traceback (most recent call last):<br>
File “”, line 3, in <br>
File “/home/sliceruser/Slicer/NA-MIC/Extensions-30822/SlicerRT/lib/Slicer-5.0/qt-scripted-modules/DicomRtImportExportPlugin.py”, line 126, in export<br>
message = slicer.modules.dicomrtimportexport.logic().ExportDicomRTStudy(exportablesCollection)<br>
AttributeError: module ‘modules’ has no attribute ‘dicomrtimportexport’ "</p>
<p>How should I approach this ?<br>
Thanks,<br>
Alex</p>

---

## Post #2 by @cpinter (2022-09-02 09:56 UTC)

<p>SlicerRT may not be properly installed. Do you get any errors on startup? Please see the log.</p>

---

## Post #3 by @alireza (2023-10-05 19:10 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a><br>
I’m getting this error suddenly. I have done clean uninstall, installed again Slicer stable and Slicer nightly again the same issue mentioned by OP.</p>
<p>I see these errors in my Error log. Any idea what is happening? I have re-installed and installed again everything no success.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/dbe1b63b800289c14486e7b1eea71c30c14f391a.png" alt="CleanShot 2023-10-05 at 15.09.56" data-base62-sha1="vna9o5fP2NaPDjBB4Ajc6Atrs2S" width="592" height="355"></p>
<p>After a fresh install these errors are not there, but as soon as I install SlicerRT they appear</p>
<p>PS: I’m using Mac M2</p>
<p>This is one of the errors</p>
<pre><code class="lang-auto">dlopen(/Applications/Slicer.app/Contents/Extensions-32207/SlicerRT/lib/Slicer-5.5/qt-loadable-modules/vtkSlicerSegmentComparisonModuleLogicPython.so, 0x0002): Library not loaded: @rpath/libomp.dylib
  Referenced from: &lt;1ED556AD-4C86-3666-8D29-E9A71CDE5CE4&gt; /Applications/Slicer.app/Contents/Extensions-32207/SlicerRT/lib/Slicer-5.5/qt-loadable-modules/libvtkSlicerSegmentComparisonModuleLogic.dylib
  Reason: tried: '/Applications/Slicer.app/Contents/bin/../bin/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/bin/../lib/Slicer-5.5/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/bin/../lib/Slicer-5.5/cli-modules/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/bin/../lib/Slicer-5.5/qt-loadable-modules/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/../lib/Slicer-5.5/qt-loadable-modules/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/bin/../lib/Python/lib/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/bin/../lib/Python/lib/python3.9/site-packages/numpy/core/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/bin/../lib/Python/lib/python3.9/site-packages/numpy/lib/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/Users/svc-dashboard/D/Support/clang+llvm-14.0.6-x86_64-apple-darwin/lib/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/Support/clang+llvm-14.0.6-x86_64-apple-darwin/lib/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/MacOS/../libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/CTK-build/CMakeExternals/Install/lib/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/CTK-build/CMakeExternals/Install/lib/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/usr/local/lib/libomp.dylib' (no such file), '/usr/lib/libomp.dylib' (no such file, not in dyld cache)
dlopen(/Applications/Slicer.app/Contents/Extensions-32207/SlicerRT/lib/Slicer-5.5/qt-loadable-modules/vtkSlicerExternalBeamPlanningModuleLogicPython.so, 0x0002): Library not loaded: @rpath/libomp.dylib
  Referenced from: &lt;4CF5FCDE-B1B2-36B5-BC42-69335F1D965D&gt; /Applications/Slicer.app/Contents/Extensions-32207/SlicerRT/lib/Slicer-5.5/qt-loadable-modules/libvtkSlicerExternalBeamPlanningModuleLogic.dylib
  Reason: tried: '/Applications/Slicer.app/Contents/bin/../bin/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/bin/../lib/Slicer-5.5/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/bin/../lib/Slicer-5.5/cli-modules/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/bin/../lib/Slicer-5.5/qt-loadable-modules/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/../lib/Slicer-5.5/qt-loadable-modules/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/bin/../lib/Python/lib/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/bin/../lib/Python/lib/python3.9/site-packages/numpy/core/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/bin/../lib/Python/lib/python3.9/site-packages/numpy/lib/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/Users/svc-dashboard/D/Support/clang+llvm-14.0.6-x86_64-apple-darwin/lib/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/Support/clang+llvm-14.0.6-x86_64-apple-darwin/lib/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/MacOS/../libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/CTK-build/CMakeExternals/Install/lib/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/CTK-build/CMakeExternals/Install/lib/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/usr/local/lib/libomp.dylib' (no such file), '/usr/lib/libomp.dylib' (no such file, not in dyld cache)Library not loaded: @rpath/libomp.dylib
  Referenced from: &lt;1B933BBC-6B24-385C-A690-5FF21ED88845&gt; /Applications/Slicer.app/Contents/Extensions-32207/SlicerRT/lib/Slicer-5.5/qt-loadable-modules/libvtkSlicerBeamsModuleMRML.dylib
  Reason: tried: '/Applications/Slicer.app/Contents/bin/../bin/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/bin/../lib/Slicer-5.5/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/bin/../lib/Slicer-5.5/cli-modules/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/bin/../lib/Slicer-5.5/qt-loadable-modules/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/../lib/Slicer-5.5/qt-loadable-modules/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/bin/../lib/Python/lib/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/bin/../lib/Python/lib/python3.9/site-packages/numpy/core/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/bin/../lib/Python/lib/python3.9/site-packages/numpy/lib/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/Users/svc-dashboard/D/Support/clang+llvm-14.0.6-x86_64-apple-darwin/lib/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/Support/clang+llvm-14.0.6-x86_64-apple-darwin/lib/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/MacOS/../libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/CTK-build/CMakeExternals/Install/lib/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/CTK-build/CMakeExternals/Install/lib/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/usr/local/lib/libomp.dylib' (no such file), '/usr/lib/libomp.dylib' (no such file, not in dyld cache)
dlopen(/Applications/Slicer.app/Contents/Extensions-32207/SlicerRT/lib/Slicer-5.5/qt-loadable-modules/vtkSlicerDicomRtImportExportModuleLogicPython.so, 0x0002): Library not loaded: @rpath/libomp.dylib
  Referenced from: &lt;25965AFF-EE1C-3F21-958E-5D8E35FA9E6C&gt; /Applications/Slicer.app/Contents/Extensions-32207/SlicerRT/lib/Slicer-5.5/qt-loadable-modules/libvtkSlicerDicomRtImportExportModuleLogic.dylib
  Reason: tried: '/Applications/Slicer.app/Contents/bin/../bin/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/bin/../lib/Slicer-5.5/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/bin/../lib/Slicer-5.5/cli-modules/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/bin/../lib/Slicer-5.5/qt-loadable-modules/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/../lib/Slicer-5.5/qt-loadable-modules/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/bin/../lib/Python/lib/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/bin/../lib/Python/lib/python3.9/site-packages/numpy/core/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/bin/../lib/Python/lib/python3.9/site-packages/numpy/lib/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/Users/svc-dashboard/D/Support/clang+llvm-14.0.6-x86_64-apple-darwin/lib/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/Support/clang+llvm-14.0.6-x86_64-apple-darwin/lib/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/MacOS/../libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/CTK-build/CMakeExternals/Install/lib/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/CTK-build/CMakeExternals/Install/lib/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/usr/local/lib/libomp.dylib' (no such file), '/usr/lib/libomp.dylib' (no such file, not in dyld cache)Library not loaded: @rpath/libomp.dylib
  Referenced from: &lt;1B933BBC-6B24-385C-A690-5FF21ED88845&gt; /Applications/Slicer.app/Contents/Extensions-32207/SlicerRT/lib/Slicer-5.5/qt-loadable-modules/libvtkSlicerBeamsModuleMRML.dylib
  Reason: tried: '/Applications/Slicer.app/Contents/bin/../bin/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/bin/../lib/Slicer-5.5/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/bin/../lib/Slicer-5.5/cli-modules/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/bin/../lib/Slicer-5.5/qt-loadable-modules/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/../lib/Slicer-5.5/qt-loadable-modules/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/bin/../lib/Python/lib/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/bin/../lib/Python/lib/python3.9/site-packages/numpy/core/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/bin/../lib/Python/lib/python3.9/site-packages/numpy/lib/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/Users/svc-dashboard/D/Support/clang+llvm-14.0.6-x86_64-apple-darwin/lib/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/Support/clang+llvm-14.0.6-x86_64-apple-darwin/lib/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/MacOS/../libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/CTK-build/CMakeExternals/Install/lib/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/CTK-build/CMakeExternals/Install/lib/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/usr/local/lib/libomp.dylib' (no such file), '/usr/lib/libomp.dylib' (no such file, not in dyld cache)
dlopen(/Applications/Slicer.app/Contents/Extensions-32207/SlicerRT/lib/Slicer-5.5/qt-loadable-modules/vtkSlicerPlastimatchPyModuleLogicPython.so, 0x0002): Library not loaded: @rpath/libomp.dylib
  Referenced from: &lt;7C742946-BFDC-37D9-99C6-29D03B57AF9F&gt; /Applications/Slicer.app/Contents/Extensions-32207/SlicerRT/lib/Slicer-5.5/qt-loadable-modules/libvtkSlicerPlastimatchPyModuleLogic.dylib
  Reason: tried: '/Applications/Slicer.app/Contents/bin/../bin/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/bin/../lib/Slicer-5.5/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/bin/../lib/Slicer-5.5/cli-modules/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/bin/../lib/Slicer-5.5/qt-loadable-modules/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/../lib/Slicer-5.5/qt-loadable-modules/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/bin/../lib/Python/lib/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/bin/../lib/Python/lib/python3.9/site-packages/numpy/core/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/bin/../lib/Python/lib/python3.9/site-packages/numpy/lib/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/Users/svc-dashboard/D/Support/clang+llvm-14.0.6-x86_64-apple-darwin/lib/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/Support/clang+llvm-14.0.6-x86_64-apple-darwin/lib/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/qRestAPI-build/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/MacOS/../libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/CTK-build/CMakeExternals/Install/lib/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/CTK-build/CMakeExternals/Install/lib/libomp.dylib' (no such file), '/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/Users/svc-dashboard/D/P/A/teem-build/bin/libomp.dylib' (no such file), '/usr/local/lib/libomp.dylib' (no such file), '/usr/lib/libomp.dylib' (no such file, not in dyld cache)
</code></pre>

---

## Post #4 by @pieper (2023-10-05 19:17 UTC)

<aside class="quote no-group" data-username="alireza" data-post="3" data-topic="24836">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alireza/48/67173_2.png" class="avatar"> alireza:</div>
<blockquote>
<p><code>libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/bin/../lib/Python/lib/libomp.dylib' (no such file), '/Applications/Slicer.app/Contents/bin/../lib/Python/lib/python3.9/site-packag</code></p>
</blockquote>
</aside>
<p>Thanks for reporting - I have seen similar errors when trying to use the Extension manager on 5.4.0 on mac (intel mac pro) but haven’t had time to report or investigate.</p>
<p>I suspect there’s something getting corrupted in the installation paths because I had already installed some extensions and the errors started when I tried to install more.</p>
<p>Try running:</p>
<pre><code class="lang-auto">/Applications/Slicer.app/Contents/MacOS/Slicer --settings-path
</code></pre>
<p>And deleting the extensions folders from the indicated directory.</p>

---

## Post #5 by @alireza (2023-10-05 19:22 UTC)

<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="24836">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<pre><code class="lang-auto">/Applications/Slicer.app/Contents/MacOS/Slicer --settings-path
</code></pre>
</blockquote>
</aside>
<p>Tried this but no luck so far.</p>

---

## Post #6 by @alireza (2023-10-05 19:26 UTC)

<p>I can confirm that 5.2.2 works fine</p>

---

## Post #7 by @pieper (2023-10-05 19:38 UTC)

<p>For me, the message from 5.4.0 is pasted below.  I deleted the .app folder and re-installed a fresh download and still get the same message.  It seems different from what <a class="mention" href="/u/alireza">@alireza</a> is reporting.</p>
<pre><code class="lang-auto">Reason: tried: '/Applications/Slicer-5.4.0.app/Contents/Frameworks/QtWebEngineCore.framework/Helpers/QtWebEngineProcess.app/Contents/Frameworks/Frameworks/QtGui.framework/Versions/5/QtGui' (no such file), '/Applications/Slicer-5.4.0.app/Contents/Frameworks/QtWebEngineCore.framework/Helpers/QtWebEngineProcess.app/Contents/MacOS/../../../../../../../../Frameworks/QtGui.framework/Versions/5/QtGui' (no such file), '/Applications/Slicer-5.4.0.app/Contents/Frameworks/QtWebEngineCore.framework/Helpers/QtWebEngineProcess.app/Contents/Frameworks/Frameworks/QtGui.framework/Versions/5/QtGui' (no such file), '/Applications/Slicer-5.4.0.app/Contents/Frameworks/QtWebEngineCore.framework/Helpers/QtWebEngineProcess.app/Contents/MacOS/../../../../../../../../Frameworks/QtGui.framework/Versions/5/QtGui' (no such file), '/System/Library/Frameworks/QtGui.framework/Versions/5/QtGui' (no such file, not in dyld cache)
dyld[44464]: Library not loaded: @rpath/Frameworks/QtGui.framework/Versions/5/QtGui
  Referenced from: &lt;70B6F0CE-47D4-3D19-8AD6-EACF9B64D3ED&gt; /Applications/Slicer-5.4.0.app/Contents/Frameworks/QtWebEngineCore.framework/Helpers/QtWebEngineProcess.app/Contents/MacOS/QtWebEngineProcess
</code></pre>

---

## Post #8 by @Soumen_Mohanty (2023-11-01 04:50 UTC)

<p>Hi just checking in on this. I reverted back to a previous version, but I installed 5.5.0 today and I believe the issue hasn’t been fixed yet?</p>

---

## Post #9 by @lassoan (2023-11-02 00:38 UTC)

<p>The issue has been fixed both in Slicer-5.4 and recent Slicer-5.5 releases. If you still experience any issues then let us know.</p>

---

## Post #10 by @brandus1 (2023-11-28 15:16 UTC)

<p>same error happens to me in Slicer 5.6</p>

---
