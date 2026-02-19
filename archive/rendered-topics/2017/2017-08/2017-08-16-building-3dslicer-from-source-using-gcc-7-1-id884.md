---
topic_id: 884
title: "Building 3Dslicer From Source Using Gcc 7 1"
date: 2017-08-16
url: https://discourse.slicer.org/t/884
---

# Building 3DSlicer from source using gcc 7.1

**Topic ID**: 884
**Date**: 2017-08-16
**URL**: https://discourse.slicer.org/t/building-3dslicer-from-source-using-gcc-7-1/884

---

## Post #1 by @thaenel (2017-08-16 19:34 UTC)

<p>Hello everyone,</p>
<p>I am currently getting started on creating an extension for 3DSlicer.<br>
As <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Module" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Module</a> suggests, I have to build 3DSlicer from source to use C++ modules.</p>
<p>I am running Archlinux and I was following <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions</a> for instructions on the build process.</p>
<p>All prerequisites are installed with the following versions:<br>
<em>cmake</em> 3.8.2,<br>
<em>git</em> 2.14.1<br>
<em>svn</em> 1.9.7<br>
<em>Qt</em> 4.8.7 (including Qt Webkit)<br>
<em>gcc</em> 7.1.1</p>
<p>After downloading the 3DSlicer sources (stable 4.6.2) and creating the super build directory,<br>
<em>cmake</em> worked without errors using the argument <code>-DCMAKE_BUILD_TYPE:STRING=Debug</code><br>
When I run make (with multiple jobs) in the super build directory I get various compile errors and the build process fails. Using <em>gcc</em> 5.4 the build process ran longer, but stopped with compilation errors as well.</p>
<p>Am I missing something important here? Or is any <em>gcc</em> version &gt; 4.4 simply not tested/supported. The dashboard seems to use this ancient version of <em>gcc</em> from 2010. Should I maybe use <em>clang</em> instead?</p>
<p>Thanks in advance,<br>
Tobias</p>

---

## Post #2 by @fedorov (2017-08-16 19:58 UTC)

<p>C++14 is default for gcc 6 (see <a href="https://gcc.gnu.org/gcc-6/changes.html">https://gcc.gnu.org/gcc-6/changes.html</a>) and I think Slicer is not expected/tested to compile with even C++11.</p>

---

## Post #3 by @chir.set (2017-08-16 20:18 UTC)

<p>Eight months ago, I could build Slicer on ArchLinux with gcc6 using c++98 throughout.<br>
I tried again a few weeks ago with gcc7. Using c++98, build fails in DCMTK. Using c++11, DCMTK builds, but then it will fail again in BRAINSCommonLib. The latter seems to require c++98 however. I gave up after a few dirty trials.</p>
<p>The problem is not the version of gcc. Resources downloaded automatically require conflicting c++ standards. The bottleneck is BRAINSCommonLib, so it seems to me. I don’t know who maintains that library, but it really needs some fresh blood.</p>

---

## Post #4 by @fedorov (2017-08-16 21:08 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="3" data-topic="884">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>I tried again a few weeks ago with gcc7. Using c++98, build fails in DCMTK.</p>
</blockquote>
</aside>
<p>How did you make sure that your flags prescribing c++98 were propagated throughout the superbuild process? I am not sure that works.</p>
<aside class="quote no-group" data-username="chir.set" data-post="3" data-topic="884">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>BRAINSCommonLib</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/hjmjohnson">@hjmjohnson</a> maintains that library</p>

---

## Post #5 by @lassoan (2017-08-16 21:12 UTC)

<p>We’ll release a new stable version (based on the latest nightly) within a few weeks. So, probably it is not worth spending time with the old stable release, just try to build the latest nightly and let us know if you still have issues.</p>

---

## Post #6 by @chir.set (2017-08-16 21:32 UTC)

<p>I used :</p>
<p>export CXXFLAGS="-std=c++98 -Wno-error -fpermissive"<br>
export CFLAGS="-Wno-error"</p>
<p>before configuring with ccmake. The latter allows to switch to advanced options, where the CXXFLAGS declared to ccmake can be checked.</p>
<p>Concerning BRAINSCommonLib, it seems to ignore environment variables totally, and always forces a compilation with c++98. Then VNL, which has been built with c++11 (if not, we won’t get beyond DCMTK), complains that VNL was built with a newer C++ standard. It’s that last message that hints towards BRAINSCommonLib ignoring environment variables.</p>
<p>I may try a new build this week end (will try to find some time) and post a link to full error output.</p>

---

## Post #7 by @chir.set (2017-08-16 21:33 UTC)

<p>Of course I always ‘git pull’ before building.</p>

---

## Post #8 by @fedorov (2017-08-16 21:46 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="6" data-topic="884">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>VNL, which has been built with c++11 (if not, we won’t get beyond DCMTK)</p>
</blockquote>
</aside>
<p>I don’t understand this part. You seem to imply DCMTK requires c++11, but this is not the case.</p>

---

## Post #9 by @thaenel (2017-08-16 22:20 UTC)

<p>Ok, so I tried to built the current nightly (master-branch). I still used gcc 7.1 and tried both C++11 and C++98 (using export CXXFLAGS) with -DCMAKE_BUILD_TYPE:STRING=Release. I always get compile errors in DCMTK about char16_t not being available.</p>
<p>I’m kind of clueless at the moment. I am always doing clean builds. Should the build process work with gcc and C++11? Or is the current nightly still using C++98?</p>
<pre><code>In file included from /usr/include/unicode/utypes.h:38:0,
                 from /usr/include/unicode/ucnv_err.h:88,
                 from /usr/include/unicode/ucnv.h:52,
                 from [...]/Slicer-SuperBuild-Debug/DCMTK/ofstd/libsrc/ofchrenc.cc:58:
/usr/include/unicode/umachine.h:347:13: error: 'char16_t' does not name a type; did you mean 'wchar_t'?
     typedef char16_t UChar;
             ^~~~~~~~
             wchar_t
In file included from /usr/include/unicode/utypes.h:39:0,
                 from /usr/include/unicode/ucnv_err.h:88,
                 from /usr/include/unicode/ucnv.h:52,
                 from [...]/Slicer-SuperBuild-Debug/DCMTK/ofstd/libsrc/ofchrenc.cc:58:
/usr/include/unicode/uversion.h:167:55: error: 'UChar' does not name a type; did you mean 'UChar32'?
 u_versionFromUString(UVersionInfo versionArray, const UChar *versionString);
</code></pre>
<p>Does this mean that my system header files requires C++11?<br>
Or does this mean that DCMTK requires a C++11 header?<br>
(char16_t is only available since C++11 <a href="http://en.cppreference.com/w/cpp/keyword/char16_t" rel="nofollow noopener">http://en.cppreference.com/w/cpp/keyword/char16_t</a>)</p>
<p>A verbose make output indicates that DCMTK is compiled with -std=c++98. This seems to be the problem, maybe <a class="mention" href="/u/chir.set">@chir.set</a> had the same issue?</p>

---

## Post #10 by @lassoan (2017-08-17 02:19 UTC)

<aside class="quote no-group" data-username="thaenel" data-post="9" data-topic="884">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/9fc348/48.png" class="avatar"> thaenel:</div>
<blockquote>
<p>tried both C++11 and C++98 (using export CXXFLAGS)</p>
</blockquote>
</aside>
<p>I think all CXX flags have to be set in CMake (what you set in Slicer are propagated to all libraries). Environment variables should not have any effect.</p>

---

## Post #11 by @fedorov (2017-08-17 02:35 UTC)

<aside class="quote no-group" data-username="thaenel" data-post="9" data-topic="884">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/9fc348/48.png" class="avatar"> thaenel:</div>
<blockquote>
<p>Or is the current nightly still using C++98?</p>
</blockquote>
</aside>
<p>I believe this is the case.</p>
<aside class="quote no-group" data-username="thaenel" data-post="9" data-topic="884">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/9fc348/48.png" class="avatar"> thaenel:</div>
<blockquote>
<p>Does this mean that my system header files requires C++11?</p>
</blockquote>
</aside>
<p>Probably not. You can look into that header file. It probably has a series of checks to include certain line of code depending on <code>#define</code>d things, and the heuristic doesn’t work probably.</p>
<p>I can’t debug this, since I don’t have a system with a gcc7 compiler. When I tried to debug a similar issue earlier (see notes here: <a href="https://github.com/QIICR/dcmqi/issues/235" class="inline-onebox">C++11 build errors · Issue #235 · QIICR/dcmqi · GitHub</a>), my experience was that even with <code>CXXFLAGS</code> the options were not propagated properly. There is also a specific comment about a problem in CMake propagating the flags through sub-projects. Can you try to compile just DCMTK, independently from Slicer? Taking one project at a time may be more manageable. Can you also make sure you use the latest CMake?</p>
<p>I also wonder if there is difference between using a compiler that by default uses C++11/14, and a flag needs to be used to override that behavior to use C++98 vs using a C++98 compiler that can be made to use C++11 with extra flags. I think it is the latter that usually is tested/described in the documentation (such as DCMTK instructions for enabling C++11: <a href="http://support.dcmtk.org/docs-snapshot/cxx11_support.html" class="inline-onebox">DCMTK: C++11 support in DCMTK</a>).</p>
<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="884">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I think all CXX flags have to be set in CMake</p>
</blockquote>
</aside>
<p>Based on the comment from <a class="mention" href="/u/thewtex">@thewtex</a> <a href="https://github.com/QIICR/dcmqi/issues/235#issuecomment-298037603">here</a>, <code>CXXFLAGS</code> approach is recommended.</p>

---

## Post #12 by @lassoan (2017-08-17 03:10 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="11" data-topic="884">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>Based on the comment from <a class="mention" href="/u/thewtex">@thewtex</a> here, CXXFLAGS approach is recommended</p>
</blockquote>
</aside>
<p>I meant that instead of setting CXXFLAGS directly as an env var, passing CXXFLAGS to CMake should work better, because the setting is cached, consistency can be checked, value can be written to env vars as needed, and it works on all platforms. Note that I have minimal experience with these issues (there are no such problems with Visual Studio), so these are just general comments.</p>

---

## Post #13 by @thaenel (2017-08-17 16:05 UTC)

<p>The hints you gave me were very useful, thank you!. I could get the application to build using the following script and gcc 7.1 and cmake 3.9</p>
<pre><code>#!/usr/bin/sh

BUILD=Debug

rm -rf [...]/Slicer-SuperBuild-${BUILD}
mkdir [...]/Slicer-SuperBuild-${BUILD}
cd [...]/Slicer-SuperBuild-${BUILD}
CXXFLAGS="-std=c++98 -Wno-error -fpermissive -DUCHAR_TYPE=uint16_t" CFLAGS="-Wno-error" cmake\
          -DCMAKE_BUILD_TYPE:STRING=Release\ # &lt; Bug see revised script below
          -DCMAKE_CXX_COMPILER:STRING="g++"\
          -DCMAKE_C_COMPILER:STRING="gcc"\
          -DSlicer_USE_SYSTEM_QT:BOOL=1\
          ~/Programme/Slicer
make -j 9
</code></pre>
<p>The key changes are the following:</p>
<ul>
<li>using <code>CXXFLAGS cmake [...]</code> instead of <code>export CXXFLAGS</code> and then running <code>cmake</code>
</li>
<li>using <code>-DCMAKE_CXX_FLAGS</code> doesn’t work, instead <code>-DCMAKE_CXX_FLAGS_INIT</code> has to be used (seems like an error in the definition of the external project compiler flags)</li>
<li>compiling with <code>-DUCHAR_TYPE=uint16_t</code>
</li>
</ul>
<p>The latter is necessary, because I have ICU v59 (unicode library) installed and it makes use of <code>char16_t</code> per default for defing <code>UChar</code>. By providing a different type this problem can be omitted, hence the preprocessor flag. Versions before ICU v59 didn’t use <code>char16_t</code> per default.</p>
<hr>
<p>Now to the next problem, the application builds, but when I run Slicer the loading screen starts and the application <strong>crashes</strong> with the following error message:</p>
<p><code>error: [[...]/Slicer-SuperBuild-Debug/Slicer-build/bin/./SlicerApp-real] exit abnormally - Report the problem.</code></p>
<p>That’s it, no further output <img src="https://emoji.discourse-cdn.com/twitter/confused.png?v=5" title=":confused:" class="emoji" alt=":confused:">. Is there any way to increase the amount of debug output?<br>
The test results may give further information:</p>
<details>
<summary>
Results of ctest</summary>
<pre><code>Total Test time (real) = 313.42 sec

The following tests FAILED:
	  7 - py_cmake_slicer_extensions_index_build_without_upload (Failed)
	  8 - py_cmake_slicer_extensions_index_build_with_upload (Failed)
	  9 - py_cmake_slicer_extensions_index_build_with_upload_using_ctest (Failed)
	 10 - py_cmake_slicer_extensions_index_build_without_upload_using_ctest (Failed)
	 16 - py_vtkITKArchetypeDiffusionTensorReaderFile (Failed)
	 17 - py_vtkITKArchetypeScalarReaderFile (Failed)
	258 - qSlicerCoreApplicationTest1 (Failed)
	259 - qSlicerCoreIOManagerTest1 (Failed)
	263 - qSlicerExtensionsManagerModelTest (Failed)
	267 - qSlicerSslTest (Failed)
	268 - qSlicerApplicationTest1 (Failed)
	271 - qSlicerDataDialogTest1 (Failed)
	274 - qSlicerModulePanelTest1 (Failed)
	275 - qSlicerMouseModeToolBarTest1 (Failed)
	276 - qSlicerSaveDataDialogCustomFileWriterTest (Failed)
	278 - qSlicerWidgetTest2 (Failed)
	285 - qSlicerCLIModuleTest1 (Failed)
	286 - qSlicerEventBrokerModuleGenericTest (Failed)
	287 - qSlicerEventBrokerModuleWidgetGenericTest (Failed)
	288 - qSlicerROIModuleGenericTest (Failed)
	289 - qSlicerROIModuleWidgetGenericTest (Failed)
	292 - qSlicerModulePanelTest2 (Failed)
	293 - qSlicerCamerasModuleGenericTest (Failed)
	294 - qSlicerCamerasModuleWidgetGenericTest (Failed)
	295 - qSlicerCamerasModuleWidgetTest1 (Failed)
	297 - qSlicerUnitsModuleGenericTest (Failed)
	298 - qSlicerUnitsModuleWidgetGenericTest (Failed)
	300 - qSlicerTerminologiesModuleGenericTest (Failed)
	301 - qSlicerTerminologiesModuleWidgetGenericTest (Failed)
	302 - qSlicerColorsModuleGenericTest (Failed)
	303 - qSlicerColorsModuleWidgetGenericTest (Failed)
	305 - qSlicerColorsModuleWidgetTest1 (Failed)
	306 - py_ColorsScalarBarSelfTest (Failed)
	307 - py_CustomColorTableSceneViewRestoreTestBug3992 (Failed)
	308 - qSlicerSubjectHierarchyModuleGenericTest (Failed)
	309 - qSlicerSubjectHierarchyModuleWidgetGenericTest (Failed)
	311 - qSlicerAnnotationsModuleGenericTest (Failed)
	312 - qSlicerAnnotationsModuleWidgetGenericTest (Failed)
	337 - py_AnnotationsTestingAddManyFiducials (Failed)
	338 - py_AnnotationsTestingAddManyRulers (Failed)
	339 - py_AnnotationsTestingAddManyROIs (Failed)
	340 - py_RemoveAnnotationsIDFromSelectionNode (Failed)
	341 - py_LoadAnnotationRulerScene (Failed)
	342 - py_AnnotationsTestingFiducialWithSceneViewRestore (Failed)
	343 - qSlicerMarkupsModuleGenericTest (Failed)
	344 - qSlicerMarkupsModuleWidgetGenericTest (Failed)
	345 - qSlicerSimpleMarkupsWidgetTest1 (Failed)
	346 - py_MarkupsWidgetsSelfTest (Failed)
	359 - py_AddManyMarkupsFiducialTest (Failed)
	360 - py_MarkupsSceneViewRestoreTestSimple (Failed)
	361 - py_MarkupsSceneViewRestoreTestManyLists (Failed)
	362 - py_NeurosurgicalPlanningTutorialMarkupsSelfTest (Failed)
	363 - py_MarkupsInCompareViewersSelfTest (Failed)
	364 - py_MarkupsInViewsSelfTest (Failed)
	365 - qSlicerTransformsModuleGenericTest (Failed)
	366 - qSlicerTransformsModuleWidgetGenericTest (Failed)
	373 - qSlicerDataModuleGenericTest (Failed)
	374 - qSlicerDataModuleWidgetGenericTest (Failed)
	376 - qSlicerDoubleArraysModuleGenericTest (Failed)
	377 - qSlicerDoubleArraysModuleWidgetGenericTest (Failed)
	379 - qSlicerModelsModuleGenericTest (Failed)
	380 - qSlicerModelsModuleWidgetGenericTest (Failed)
	383 - qSlicerModelsModuleWidgetTest1 (Failed)
	384 - qSlicerModelsModuleWidgetTestScene (Failed)
	387 - qSlicerSceneViewsModuleGenericTest (Failed)
	388 - qSlicerSceneViewsModuleWidgetGenericTest (Failed)
	390 - py_mainwindow_RestoreSceneViewWithoutCamera (Failed)
	391 - py_AddStorableDataAfterSceneViewTest (Failed)
	392 - qSlicerSegmentationsModuleGenericTest (Failed)
	393 - qSlicerSegmentationsModuleWidgetGenericTest (Failed)
	394 - py_nomainwindow_SegmentationsModuleTest1 (Failed)
	395 - py_nomainwindow_SegmentationWidgetsTest1 (Failed)
	396 - qSlicerWelcomeModuleGenericTest (Failed)
	397 - qSlicerWelcomeModuleWidgetGenericTest (Failed)
	398 - qSlicerTablesModuleGenericTest (Failed)
	399 - qSlicerTablesModuleWidgetGenericTest (Failed)
	401 - py_TablesSelfTest (Failed)
	402 - qSlicerReformatModuleGenericTest (Failed)
	403 - qSlicerReformatModuleWidgetGenericTest (Failed)
	404 - qSlicerViewControllersModuleGenericTest (Failed)
	405 - qSlicerViewControllersModuleWidgetGenericTest (Failed)
	406 - qSlicerVolumesModuleGenericTest (Failed)
	407 - qSlicerVolumesModuleWidgetGenericTest (Failed)
	411 - qSlicerVolumesIOOptionsWidgetTest1 (Failed)
	412 - qSlicerVolumesModuleWidgetTest1 (Failed)
	416 - py_LoadVolumeDisplaybleSceneModelClose (Failed)
	417 - py_VolumesLogicCompareVolumeGeometry (Failed)
	418 - qSlicerVolumeRenderingModuleGenericTest (Failed)
	419 - qSlicerVolumeRenderingModuleWidgetGenericTest (Failed)
	424 - qSlicerVolumeRenderingModuleWidgetTest1 (Failed)
	425 - qSlicerVolumeRenderingModuleWidgetTest2 (Failed)
	430 - py_VolumeRenderingSceneClose (Failed)
	431 - py_VolumeRenderingThreeDOnlyLayout (Failed)
	432 - qSlicerCropVolumeModuleGenericTest (Failed)
	433 - qSlicerCropVolumeModuleWidgetGenericTest (Failed)
	435 - py_CropVolumeSelfTest (Failed)
	436 - py_nomainwindow_qSlicerDataProbeModuleGenericTest (Failed)
	437 - py_nomainwindow_qSlicerDMRIInstallModuleGenericTest (Failed)
	438 - py_nomainwindow_qSlicerEditorModuleGenericTest (Failed)
	439 - py_ThresholdThreadingTest (Failed)
	440 - py_StandaloneEditorWidgetTest (Failed)
	441 - py_nomainwindow_qSlicerLabelStatisticsModuleGenericTest (Failed)
	442 - py_LabelStatistics (Failed)
	443 - py_nomainwindow_qSlicerPerformanceTestsModuleGenericTest (Failed)
	444 - py_nomainwindow_qSlicerSampleDataModuleGenericTest (Failed)
	445 - py_nomainwindow_qSlicerScreenCaptureModuleGenericTest (Failed)
	446 - py_ScreenCapture (Failed)
	447 - py_SegmentEditor (Failed)
	448 - py_nomainwindow_qSlicerSegmentStatisticsModuleGenericTest (Failed)
	449 - py_SegmentStatistics (Failed)
	450 - py_nomainwindow_qSlicerSelfTestsModuleGenericTest (Failed)
	451 - py_nomainwindow_qSlicerSurfaceToolboxModuleGenericTest (Failed)
	452 - py_nomainwindow_qSlicerVectorToScalarVolumeModuleGenericTest (Failed)
	453 - py_nomainwindow_qSlicerExtensionWizardModuleGenericTest (Failed)
	454 - py_nomainwindow_qSlicerEndoscopyModuleGenericTest (Failed)
	455 - py_nomainwindow_qSlicerDICOMModuleGenericTest (Failed)
	456 - py_nomainwindow_qSlicerDICOMPatcherModuleGenericTest (Failed)
	457 - py_DICOMPatcher (Failed)
	540 - qSlicerAppAboutDialogTest1 (Failed)
	541 - qSlicerApplicationTpyclTest1 (Failed)
	542 - qSlicerApplicationTpyclEMSegmentIntegrationTest (Failed)
	543 - qSlicerAppMainWindowTest1 (Failed)
	544 - qSlicerModuleFactoryManagerTest1 (Failed)
	545 - slicer_nomainwindow_DisableModulesCommandLineOptionsTest (Failed)
	546 - slicer_nomainwindow_DisableModulesCommandLineOptionsTest2 (Failed)
	547 - slicer_nomainwindow_NoApplicationInformationOptionTest (Failed)
	548 - slicer_nomainwindow_ApplicationInformationOptionTest (Failed)
	549 - py_nomainwindow_SlicerPythonCodeExitSuccessTest (Failed)
	550 - py_nomainwindow_testing_SlicerPythonCodeExitSuccessTest (Failed)
	553 - py_nomainwindow_SlicerPythonCodeTest3 (Failed)
	556 - py_nomainwindow_SlicerTestingExitSuccessTest (Failed)
	558 - py_SlicerTestingExitSuccessTest (Failed)
	560 - py_nomainwindow_SlicerUnitTestTest (Failed)
	562 - py_nowarning_mainwindowTest (Failed)
	563 - py_nowarning_mainwindow_application_infoTest (Failed)
	564 - py_nowarning_mainwindow_python_interactorTest (Failed)
	565 - py_nowarning_mainwindow_nocliTest (Failed)
	566 - py_nowarning_mainwindow_noloadableTest (Failed)
	567 - py_nowarning_mainwindow_noscriptedTest (Failed)
	568 - py_nowarning_mainwindow_nocli_noloadableTest (Failed)
	569 - py_nowarning_mainwindow_nocli_noscriptedTest (Failed)
	570 - py_nowarning_mainwindow_noloadable_noscriptedTest (Failed)
	571 - py_nowarning_mainwindow_nocli_noloadable_noscriptedTest (Failed)
	572 - py_nowarning_mainwindow_nomodulesTest (Failed)
	573 - py_nowarning_nomainwindowTest (Failed)
	574 - py_nowarning_nomainwindow_application_infoTest (Failed)
	575 - py_nowarning_nomainwindow_python_interactorTest (Failed)
	576 - py_nowarning_nomainwindow_nocliTest (Failed)
	577 - py_nowarning_nomainwindow_noloadableTest (Failed)
	578 - py_nowarning_nomainwindow_noscriptedTest (Failed)
	579 - py_nowarning_nomainwindow_nocli_noloadableTest (Failed)
	580 - py_nowarning_nomainwindow_nocli_noscriptedTest (Failed)
	581 - py_nowarning_nomainwindow_noloadable_noscriptedTest (Failed)
	582 - py_nowarning_nomainwindow_nocli_noloadable_noscriptedTest (Failed)
	583 - py_nowarning_nomainwindow_nomodulesTest (Failed)
	584 - py_nowarning_nomainwindow_ignoreslicerrcTest (Failed)
	585 - py_nomainwindow_SlicerOptionDisableSettingsTest (Failed)
	586 - py_nomainwindow_SlicerOptionIgnoreSlicerRCTest (Failed)
	587 - py_nomainwindow_SlicerOptionModulesToIgnoreTest (Failed)
	589 - py_nomainwindow_ScriptedModuleDiscoveryTest (Failed)
	590 - py_nomainwindow_SlicerSceneObserverTest (Failed)
	591 - py_nomainwindow_MRMLCreateNodeByClassWithoutSetReferenceCount (Failed)
	592 - py_nomainwindow_MRMLCreateNodeByClassWithSetReferenceCountMinusOne (Failed)
	593 - py_mainwindow_MRMLSceneImportAndExport (Failed)
	594 - py_nomainwindow_test_sitkUtils (Failed)
	595 - py_nomainwindow_test_saferef (Failed)
	596 - py_nomainwindow_test_slicer_util_save (Failed)
	597 - py_nomainwindow_test_slicer_util_getNodes (Failed)
	598 - py_nomainwindow_test_slicer_mgh (Failed)
	599 - py_nomainwindow_test_slicer_minc (Failed)
	600 - py_nomainwindow_test_slicer_util_VTKObservationMixin (Failed)
	601 - py_nomainwindow_DCMTKPrivateDictTest (Failed)
	602 - py_SlicerSslTest (Failed)
	604 - py_test_stdlib_import_bz2_using_slicer (Failed)
	606 - py_startupcompleted_signal_emitted_with_mainwindow_test (Failed)
	607 - py_startupcompleted_signal_emitted_without_mainwindow_test (Failed)
	608 - py_AtlasTests (Failed)
	609 - py_AbdominalAtlasTest (Failed)
	610 - py_DICOMReaders (Failed)
	611 - py_KneeAtlasTest (Failed)
	612 - py_sceneImport2428 (Failed)
	613 - py_SlicerMRBMultipleSaveRestoreLoopTest (Failed)
	614 - py_SlicerMRBMultipleSaveRestoreTest (Failed)
	615 - py_SlicerMRBSaveRestoreCheckPathsTest (Failed)
	616 - py_Slicer4Minute (Failed)
	617 - py_SlicerBoundsTest (Failed)
	618 - py_Charting (Failed)
	619 - py_SliceLinkLogic (Failed)
	620 - py_ScenePerformance (Failed)
	621 - py_SlicerCreateRulerCrashIssue4199 (Failed)
	622 - py_SlicerRestoreSceneViewCrashIssue3445 (Failed)
	623 - py_RSNAVisTutorial (Failed)
	624 - py_RSNAQuantTutorial (Failed)
	625 - py_slicerCloseCrashBug2590 (Failed)
	626 - py_SlicerOrientationSelectorTest (Failed)
	627 - py_SlicerTransformInteractionTest1 (Failed)
	628 - py_UtilTest (Failed)
	629 - py_ViewControllersSliceInterpolationBug1926 (Failed)
	630 - py_RSNA2012ProstateDemo (Failed)
	631 - py_JRC2013Vis (Failed)
	632 - py_FiducialLayoutSwitchBug1914 (Failed)
	633 - py_SubjectHierarchyGenericSelfTest (Failed)
	634 - py_SubjectHierarchyCorePluginsSelfTest (Failed)
	635 - py_CLIEventTest (Failed)
	636 - py_TwoCLIsInARowTest (Failed)
	637 - py_TwoCLIsInParallelTest (Failed)
	638 - py_BRAINSFitRigidRegistrationCrashIssue4139 (Failed)
	639 - py_nomainwindow_qSlicerMultiVolumeImporterModuleGenericTest (Failed)
	640 - py_nomainwindow_qSlicerSimpleFiltersModuleGenericTest (Failed)
	641 - py_SimpleFiltersModuleTest (Failed)
	645 - EMSeg_SlicerCommonInterfaceTestGeneral (Failed)
	649 - EMSegCL_RunDefaultNodes (Failed)
	650 - EMSegCL_RunSetEverything (Failed)
	651 - EMSegCL_DisableMultithreading (Failed)
	652 - EMSegCL_EFBogusParameterNode (Failed)
	655 - EMSegCL_EFTooManyImages (Failed)
	656 - EMSegCL_EFTooFewImages (Failed)
	657 - EMSegCL_IntermediateResults (Failed)
	660 - EMSegCL_Task_BRAINS_MRIHumanBrain_scalartype_float_very_small (Failed)
	662 - EMSegCL_Task_BRAINS_MRIHumanBrain_scalartype_uint_very_small (Failed)
	663 - EMSegCL_Task_MRIHumanBrain_2CH (Failed)
	664 - EMSegCL_Task_MRIHumanBrain_BRAINS_small (Failed)
	665 - EMSegCL_Task_HumanEye_BRAINS_small (Failed)
	666 - EMSegCL_Task_MRIHumanBrainExp_BRAINS_small (Failed)
	667 - EMSegCL_Task_MRIHumanBrainParcellation_BRAINS_small (Failed)
	668 - EMSegCL_Task_MRIHumanBrainFullParcellation_BRAINS_small (Failed)
	669 - EMSegCL_Task_NonHumanPrimate_BRAINS_small (Failed)
	671 - qSlicerDataStoreModuleGenericTest (Failed)
	672 - qSlicerDataStoreModuleWidgetGenericTest (Failed)
	673 - vtkSlicerDataStoreLogicTest (Failed)
	674 - qSlicerDataStoreModuleTest (Failed)
	675 - py_CompareVolumes (Failed)
	676 - py_nomainwindow_qSlicerLandmarkRegistrationModuleGenericTest (Failed)
	677 - py_LandmarkRegistration (Failed)
Errors while running CTest
</code></pre>
</details>
<p>Maybe there is something wrong with Python, Qt and/or OpenSSL? Most of the tests work and windows seem to show up.</p>

---

## Post #14 by @fedorov (2017-08-17 18:01 UTC)

<p>Thanks for the update, this is encouraging, and your recipe can be helpful in the future.</p>
<p>About the runtime crash, I don’t have a better suggestion than using gdb :-/</p>

---

## Post #15 by @gcsharp (2017-08-17 18:41 UTC)

<p>Since you mention OpenSSL, is your problem the following?</p>
<p><a href="https://issues.slicer.org/view.php?id=4125" class="onebox" target="_blank" rel="nofollow noopener">https://issues.slicer.org/view.php?id=4125</a></p>

---

## Post #16 by @thaenel (2017-08-17 22:26 UTC)

<p>I finally got it to build and run. Allthough I had to disable PythonQt with OpenSSL, as I am probably being affected by the same bug that <a class="mention" href="/u/gcsharp">@gcsharp</a> reported. Slicer crashes in the self-compiled OpenSSL library at startup otherwise. Maybe this has something to do with mismatching OpenSSL versions (Qt could be linked against newer versions).</p>
<p>Here is the final working build script that I used:</p>
<details>
<summary>
Build script</summary>
<pre><code>#!/usr/bin/sh

BUILD=Debug
SLICERBUILDPATH=~/Programme/Slicer-SuperBuild-${BUILD}
SLICERSRCPATH=~/Programme/Slicer
CXXCOMPILER=clang++
CCOMPILER=clang

rm -rf ${SLICERBUILDPATH}
mkdir ${SLICERBUILDPATH}
cd ${SLICERBUILDPATH}
echo
echo ========== Running cmake ==========
echo
CXXFLAGS="-std=c++98 -Wno-error -fpermissive -DUCHAR_TYPE=uint16_t" CFLAGS="-Wno-error" cmake\
          -DCMAKE_BUILD_TYPE:STRING=${BUILD}\
          -DCMAKE_CXX_COMPILER:STRING="${CXXCOMPILER}"\
          -DCMAKE_C_COMPILER:STRING="${CCOMPILER}"\
          -DSlicer_USE_SYSTEM_QT:BOOL=1\
          -DSlicer_USE_PYTHONQT_WITH_OPENSSL:BOOL=0\
          ${SLICERSRCPATH}
echo
echo ========== Running make ==========
echo
make -j 9
</code></pre>
</details>
<p>The initial script didn’t use the BUILD variable and always built in Release mode. Unfortunately gcc 7.1 can’t be used for building in Debug mode, because LibArchive enforces <code>-Werror</code> (can’t be overwritten from global CMake) and it creates warnings during the build. clang 4.0.1 can be used as a replacement.</p>
<p>Summary of the problems that I encountered:</p>
<ul>
<li>Usage of C++98 has to be enforced with newer gcc verions, as they use C++11/14 as a default</li>
<li>Warning =&gt; Error behavior may need to be disabled, if newer compiler versions are used</li>
<li>ICU v59 needs a replacement for the <code>char16_t</code> based <code>UChar</code> definition</li>
<li>LibArchive can’t be build in Debug mode using gcc v7.1 (non overridable <code>-Werror</code> and warnings during build), clang 4.0.1 works, Release mode works with both compilers</li>
<li>OpenSSL support has to be disabled for Python Qt (Slicer crashes at startup otherwise)</li>
</ul>
<p>Finally I can get to develop my own module. Thanks for all the helpful responses, this is a very welcoming community.</p>

---

## Post #17 by @chir.set (2017-08-20 09:07 UTC)

<h2><a name="p-3680-slicer-built-in-one-single-step-with-the-following-1" class="anchor" href="#p-3680-slicer-built-in-one-single-step-with-the-following-1" aria-label="Heading link"></a>Slicer built in one single step with the following :</h2>
<p>cmake -DQt5_DIR:STRING=/usr/lib64/cmake/Qt5 -DSlicer_USE_PYTHONQT_WITH_OPENSSL:BOOL=0 -DBUILD_TESTING:BOOL=0 -DCMAKE_BUILD_TYPE:STRING=Release ../Slicer</p>
<p>It uses Qt5, disables SSL with PythonQt and testing. C++11 is automatically used throughout, and VTK8 gets preferred.<br>
Host tools : gcc 7.1.1, cmake 3.8.2, qt5 5.9.1.</p>
<h2><a name="p-3680-packaging-is-more-problematic-2" class="anchor" href="#p-3680-packaging-is-more-problematic-2" aria-label="Heading link"></a>Packaging is more problematic :</h2>
<p>CPack: - Install project: Slicer<br>
CMake Error at /home/arc/src/Slicer-SuperBuild/Slicer-build/CMake/LastConfigureStep/cmake_install.cmake:156 (file):<br>
file INSTALL cannot find “/usr/lib/../libexec/QtWebEngineProcess”.<br>
Call Stack (most recent call first):<br>
/home/arc/src/Slicer-SuperBuild/Slicer-build/cmake_install.cmake:50 (include)</p>
<p>CMake Error at /home/arc/src/Slicer-SuperBuild/Slicer-build/CMake/LastConfigureStep/cmake_install.cmake:244 (file):<br>
file INSTALL cannot find “/usr/lib/../resources”.<br>
Call Stack (most recent call first):<br>
/home/arc/src/Slicer-SuperBuild/Slicer-build/cmake_install.cmake:50 (include)</p>
<p>CMake Error at /home/arc/src/Slicer-SuperBuild/Slicer-build/CMake/LastConfigureStep/cmake_install.cmake:248 (file):<br>
file INSTALL cannot find “/usr/lib/../translations/qtwebengine_locales”.<br>
Call Stack (most recent call first):<br>
/home/arc/src/Slicer-SuperBuild/Slicer-build/cmake_install.cmake:50 (include)</p>
<p>LastConfigureStep/cmake_install.cmake was edited and respective paths hard coded. A usable package was built.</p>
<h2><a name="p-3680-running-was-also-problematic-3" class="anchor" href="#p-3680-running-was-also-problematic-3" aria-label="Heading link"></a>Running was also problematic.</h2>
<p>It complains of missing xcb Qt plugin in “”. After deleting bin/qt.conf, it ran and preliminary minimal usage was OK.</p>
<h2><a name="p-3680-one-display-problem-4" class="anchor" href="#p-3680-one-display-problem-4" aria-label="Heading link"></a>One display problem :</h2>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/3999ed99d39f6c40bc8acaf883397f0d1c018304.png" alt="Screenshot_20170820_105009" data-base62-sha1="8dz0kpu3FB4bdF50FqNZOCTWYhm" width="229" height="46"><br>
This image show inappropriate display of accelerators. Not a real problem.</p>
<p>Volume rendering is definitely better when moving the model, most probably due to a better VTK8 performance.</p>
<p>I will use it routinely and report further problems if found, and if you don’t mind.</p>
<p>Regards.</p>

---

## Post #18 by @lassoan (2018-06-25 12:26 UTC)

<p>A post was merged into an existing topic: <a href="/t/slicer-build-error-on-macosx-and-linux-in-dcmtk/3277/3">Slicer build error on MacOSX and Linux in DCMTK</a></p>

---

## Post #19 by @lassoan (2018-06-25 12:24 UTC)

<p>A post was merged into an existing topic: <a href="/t/slicer-build-error-on-macosx-and-linux-in-dcmtk/3277">Slicer build error on MacOSX and Linux in DCMTK</a></p>

---

## Post #20 by @thaenel (2017-08-16 19:34 UTC)

<p>Hello everyone,</p>
<p>I am currently getting started on creating an extension for 3DSlicer.<br>
As <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Module" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Module</a> suggests, I have to build 3DSlicer from source to use C++ modules.</p>
<p>I am running Archlinux and I was following <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions</a> for instructions on the build process.</p>
<p>All prerequisites are installed with the following versions:<br>
<em>cmake</em> 3.8.2,<br>
<em>git</em> 2.14.1<br>
<em>svn</em> 1.9.7<br>
<em>Qt</em> 4.8.7 (including Qt Webkit)<br>
<em>gcc</em> 7.1.1</p>
<p>After downloading the 3DSlicer sources (stable 4.6.2) and creating the super build directory,<br>
<em>cmake</em> worked without errors using the argument <code>-DCMAKE_BUILD_TYPE:STRING=Debug</code><br>
When I run make (with multiple jobs) in the super build directory I get various compile errors and the build process fails. Using <em>gcc</em> 5.4 the build process ran longer, but stopped with compilation errors as well.</p>
<p>Am I missing something important here? Or is any <em>gcc</em> version &gt; 4.4 simply not tested/supported. The dashboard seems to use this ancient version of <em>gcc</em> from 2010. Should I maybe use <em>clang</em> instead?</p>
<p>Thanks in advance,<br>
Tobias</p>

---
