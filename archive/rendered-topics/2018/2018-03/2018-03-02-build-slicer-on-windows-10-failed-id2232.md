---
topic_id: 2232
title: "Build Slicer On Windows 10 Failed"
date: 2018-03-02
url: https://discourse.slicer.org/t/2232
---

# Build Slicer on Windows 10 Failed

**Topic ID**: 2232
**Date**: 2018-03-02
**URL**: https://discourse.slicer.org/t/build-slicer-on-windows-10-failed/2232

---

## Post #1 by @leochan2009 (2018-03-02 21:29 UTC)

<p>Hi,</p>
<p>Did anyone have succesfully built the latest Slicer on Windows 10 machine.<br>
I am building slicer on my Windows 10 machine, and the compiler is “Visual studio 14 2015”.<br>
The error message came from the qSlicerApplicationHelper.cxx file at line 125<br>
"SetProcessDPIAware() identifier not found"</p>

---

## Post #2 by @lassoan (2018-03-02 22:02 UTC)

<p>I’ve built Slicer successfully this morning on Win10. Have you built from scratch?</p>

---

## Post #3 by @brhoom (2018-03-02 22:32 UTC)

<p>I did, I used VS2013 community edition (the free edition).  Try this:</p>
<ul>
<li>Considere all points mentioned in the slicer website.</li>
<li>Use qt-easy-build the way the README tells you. Run this command in VS2013 x64 Native Tools Command Prompt:<br>
<span class="mention">@powershell</span> -Command “$destDir=‘C:\sw\Qt4’;$buildType=‘Release’;$qtPlatform=‘win32-msvc2013’;$bits=‘64’;iex ((new-object net.webclient).DownloadString(‘<a href="https://raw.githubusercontent.com/jcfr/qt-easy-build/4.8.7/windows_build_qt.ps1" rel="nofollow noopener">https://raw.githubusercontent.com/jcfr/qt-easy-build/4.8.7/windows_build_qt.ps1</a>’))”</li>
<li>Use short names without special characters for your slicer source and build e.g.  c:\sw\ssrc and c:\sw\sbd</li>
<li>Use superbuild in cmake options as this solves many versions conflicts.</li>
</ul>
<p>Best!<br>
Ibraheem</p>

---

## Post #4 by @lassoan (2018-03-02 23:45 UTC)

<p>You need Qt5 to build nightly version of Slicer.</p>

---

## Post #5 by @jcfr (2018-03-03 00:44 UTC)

<p>As detailed in <a href="https://discourse.slicer.org/t/are-qt4-and-qt5-still-supported/2233" class="inline-onebox">Are Qt4 and Qt5 still supported?</a> , it is still possible to build with Qt4. That is why, <a class="mention" href="/u/brhoom">@brhoom</a> was able to build against Qt 4.8.7.</p>
<blockquote>
<p><code>SetProcessDPIAware() identifier not found</code></p>
</blockquote>
<p>This seems to be a legitimate error, as recommended in the associated <a href="https://msdn.microsoft.com/en-us/library/windows/desktop/ms633543%28v=vs.85%29.aspx?f=255&amp;MSPPError=-2147217396">documentation</a>, we will look into switching to use <code>SetProcessDpiAwareness</code>.</p>

---

## Post #6 by @leochan2009 (2018-03-03 01:03 UTC)

<p>I installed QT5.10, but it seems like QWebEngineer was not installed correctly. Will reinstall Qt5 and rebuild again.</p>

---

## Post #7 by @wpgao (2018-05-07 01:53 UTC)

<p><a class="mention" href="/u/leochan2009">@leochan2009</a> Have you resolved the problem! I had also encountered the same issue under win 10 using VS 2015+QT5.10! I had commented this line and built Slicer successfully? I’m not sure whether this will influence Slicer’s GUI!</p>

---

## Post #8 by @leochan2009 (2018-05-07 02:08 UTC)

<p>hi, I resolved the problem by reinstalling Qt5 with web engine and script support.</p>

---

## Post #9 by @wpgao (2018-05-08 07:42 UTC)

<p><a class="mention" href="/u/leochan2009">@leochan2009</a>, Thanks! I will try!</p>

---

## Post #10 by @Lucas (2018-05-24 09:40 UTC)

<p>hi，do you use the Qt5 x64？ could you tell me how to build Qt5 x64 from source?</p>

---

## Post #11 by @lassoan (2018-05-24 18:29 UTC)

<p>On Windows, you don’t have to build Qt5, you can just download from Qt’s website. I don’t know how is it now on Linux and Mac.</p>

---

## Post #12 by @ihnorton (2018-05-24 19:21 UTC)

<p>I am using the official Qt5 downloads on Mac, and I know a few others are as well.</p>
<p>I haven’t used the official Linux downloads, but if they are not compatible with your distribution then the recommended way to build from source is <a href="https://github.com/jcfr/qt-easy-build">qt-easy-build</a>.</p>

---

## Post #13 by @leochan2009 (2018-05-24 19:53 UTC)

<p><a class="mention" href="/u/lucas">@Lucas</a>,</p>
<p>yes, Andras is correct.</p>

---

## Post #14 by @pieper (2018-05-24 22:40 UTC)

<p>I’ve used the official Qt5 downloads on ubuntu and they worked fine.  Not sure about other distros.</p>

---

## Post #15 by @Lucas (2018-05-24 23:17 UTC)

<p>oh， thanks ！i will try！</p>

---

## Post #16 by @Saima (2018-06-19 04:13 UTC)

<aside class="quote no-group" data-username="brhoom" data-post="3" data-topic="2232">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/brhoom/48/1228_2.png" class="avatar"> brhoom:</div>
<blockquote>
<p>2013 community edition (the free edition). Try this:</p>
</blockquote>
</aside>
<p>I am trying to build slicer on window 10 but ran across too many errors. The one that is repeatedly coming is below:<br>
Severity	Code	Description	Project	File	Line	Suppression State<br>
Error	C1083	Cannot open include file: ‘Python.h’: No such file or directory [C:\Slicer4\Slicer4-superbuild\CTK-build\PythonQt-build\PythonQt.vcxproj] [C:\Slicer4\Slicer4-superbuild\CTK-build\PythonQt.vcxproj]	CTK	c:\slicer4\slicer4-superbuild\ctk-build\pythonqt\src\pythonqtpythoninclude.h	90</p>
<p>Window 10<br>
visual studio 15 2017<br>
qt 4.7.4 before this I installed qt 4.8.6 but it failed with that saying qt 4.7.4 is required.</p>
<p>Please reply</p>
<p>At the end of build it says:</p>
<p>error : VTK was not configured to use QT, you probably need to recompile it<br>
52&gt;  with VTK_USE_GUISUPPORT ON, VTK_Group_Qt ON, DESIRED_QT_VERSION 4 and<br>
52&gt;  QT_QMAKE_EXECUTABLE set appropriatly.  Note that Qt &gt;= 4.7.4 is <em>required</em></p>

---

## Post #17 by @Saima (2018-06-19 07:01 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="2232">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>uilt Slicer successfully this morning on Win10. Have you built from scratch?</p>
</blockquote>
</aside>
<p>Can you please list down the steps?</p>
<p>I am building slicer on window 10 but failed.</p>

---

## Post #18 by @Saima (2018-06-22 16:51 UTC)

<p>I didnt succeded on building slicer on window 10.<br>
Using visual studio 2013 update 5 x86(do you know where can I find x64) or can u post the community edition link.<br>
qt 4.8.7 easy build<br>
cmake 3.9.2<br>
git 2.17</p>
<p>Errors:<br>
Error	65	error LNK1181: cannot open input file ‘…\CTK-build\CTK-build\bin\Release\CTKScriptingPythonWidgets.lib’ [C:\Slicer4\Slicer4-superbuild\Slicer-build\Libs\MRML\Widgets\qMRMLWidgets.vcxproj]	C:\Slicer4\Slicer4-superbuild\LINK	Slicer<br>
Error	66	error LNK1112: module machine type ‘x64’ conflicts with target machine type ‘X86’ [C:\Slicer4\Slicer4-superbuild\Slicer-build\Base\QTCore\qSlicerBaseQTCore.vcxproj]	C:\Slicer4\Slicer4-superbuild\QtGui4.lib(QtGui4.dll)	Slicer<br>
Error	67	error C2664: ‘bool vtkMRMLTransformNode::AreTransformsEqual(vtkAbstractTransform *,vtkAbstractTransform *)’ : cannot convert argument 1 from ‘vtkNew’ to ‘vtkAbstractTransform *’ [C:\Slicer4\Slicer4-superbuild\Slicer-build\Libs\MRML\Core\Testing\MRMLCoreCxxTests.vcxproj]	C:\Slicer4\Libs\MRML\Core\Testing\vtkMRMLTransformNodeTest1.cxx	131	1	Slicer<br>
Error	68	error C2660: ‘vtkAddonTestingUtilities::CheckInt’ : function does not take 3 arguments [C:\Slicer4\Slicer4-superbuild\Slicer-build\Libs\MRML\Core\Testing\MRMLCoreCxxTests.vcxproj]	C:\Slicer4\Libs\MRML\Core\Testing\vtkMRMLTransformNodeTest1.cxx	131	1	Slicer<br>
Error	20	error LNK1181: cannot open input file ‘…\CTK-build\CTK-build\bin\Release\CTKScriptingPythonWidgets.lib’ [C:\Slicer4\Slicer4-superbuild\Slicer-build\Libs\MRML\Widgets\qMRMLWidgets.vcxproj]	C:\Slicer4\Slicer4-superbuild\LINK	Slicer<br>
Output:<br>
LINK : fatal error LNK1181: cannot open input file ‘…\CTK-build\CTK-build\bin\Release\CTKWidgets.lib’ [C:\Slicer4\Slicer4-superbuild\Slicer-build\Base\QTGUI\qSlicerIconEnginePlugin.vcxproj]<br>
53&gt;<br>
53&gt;      27 Warning(s)<br>
53&gt;      5 Error(s)<br>
53&gt;<br>
53&gt;  Time Elapsed 00:49:42.73<br>
54&gt;------ Build started: Project: ALL_BUILD, Configuration: Release Win32 ------<br>
========== Build: 52 succeeded, 2 failed, 0</p>

---

## Post #19 by @jamesobutler (2018-06-22 19:54 UTC)

<p>Hi Saima,</p>
<p>Thanks for your interest in 3D Slicer!</p>
<p>If you are not developing with Slicer and would simply like to use it, please consider downloading Slicer from the <a href="https://download.slicer.org/" rel="nofollow noopener">website</a> instead of manually building the program.</p>
<p>I would also highly suggest building the latest Slicer Nightly/Preview to take advantage of the latest features and fixes. You are more likely to receive help if problems arise while you are developing using the latest Slicer code.</p>
<p>Now, your current problems building Slicer are likely from configuration errors.  I’ll provide of list of some things to consider below. Also, if you have any more problems, it is probably best to open a new thread on the forum to help debug your specific issues.</p>
<p>For Slicer 4.8.1:</p>
<ul>
<li>Make sure you have checked out the correct source code. “master-48” branch, not the default “master”</li>
<li>Build qt 4.8.7 x64 using <a href="https://github.com/jcfr/qt-easy-build/tree/4.8.7" rel="nofollow noopener">qt-easy-build</a> with the correct build type (Debug vs. Release) that you want.  Make sure you are using the VS2013 x64 command prompt.</li>
<li>When you are configuring the build using CMake GUI, make sure you have picked the correct generator.  For this Slicer version you should select “Visual Studio 12 2013 Win64” and not “Visual Studio 12 2013”.</li>
<li>When you go to build the Slicer solution, make sure you are picking the same build type (Debug vs Release) as your Qt build.</li>
<li>If a previous build failed or you incorrectly configured with the wrong generator, it is best to completely clear your binary folder are start the build process over.</li>
</ul>
<p>Since the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions" rel="nofollow noopener">nightly build instructions</a> don’t seem up-to-date for the current Slicer Nightly/Preview here’s some hints:</p>
<ul>
<li>Check out the regular “master” branch of the Slicer repo.</li>
<li>Download the Qt5 binaries such as Qt 5.10.1 from their <a href="https://www.qt.io/download" rel="nofollow noopener">website</a>
</li>
<li>When you are configuring the build using CMake GUI, make sure you have picked the correct generator. I have <a href="https://visualstudio.microsoft.com/vs/community/" rel="nofollow noopener">Visual Studio 2017</a> installed with the “VC++ 2015.3 v14.00 (v140) toolset for desktop”.  In CMake-gui choose “Visual Studio 15 2017 Win64” and specify v140 as the optional toolset to use.</li>
<li>During configuration change Slicer_VTK_VERSION_MAJOR to 9.</li>
<li>Then configure and select your Qt5_DIR</li>
</ul>

---

## Post #20 by @Saima (2018-06-23 05:16 UTC)

<p>Thanks for your reply. I will be developing with Slicer. Can you please provide me the details on building the latest slicer.</p>
<p>Should I use this to download slicer source code:<br>
svn co <a href="http://svn.slicer.org/Slicer4/branches/Slicer-4-8" rel="nofollow noopener">http://svn.slicer.org/Slicer4/branches/Slicer-4-8</a> Slicer-r26813 -r 2681</p>
<p>Thanks</p>

---

## Post #21 by @lassoan (2018-06-23 14:45 UTC)

<aside class="quote no-group" data-username="Saima" data-post="20" data-topic="2232">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>I will be developing with Slicer</p>
</blockquote>
</aside>
<p>What do you plan to develop? You have full access to all Slicer internals from Python and there are many customization options, so there are very few things that actually requires rebuilding of Slicer.</p>
<p>Build instructions are up-to-date for latest stable (Slicer-4.8) and we’ll provide build instructions for latest version (Slicer-4.9) within a few weeks (you can monitor status of this task <a href="https://issues.slicer.org/view.php?id=4571">here</a>). Until then, you should be able to build based on hints provided by <a class="mention" href="/u/jamesobutler">@jamesobutler</a> above.</p>

---

## Post #22 by @Saima (2018-06-23 16:27 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="21" data-topic="2232">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What do you plan to develop?</p>
</blockquote>
</aside>
<p>Dear Andras,<br>
I am working with Karol Miller at ISML laboratory. I am a PhD student and just started my Phd. Initial plan is to integrate meshless (nodes not meshes) solutions developed at ISML for generating patient specific computational grids from MRI images.</p>
<p>I have to figure out how to generate this computational grid on images. any idea from where I can start after building slicer?</p>
<p>Regards,<br>
Saima</p>

---

## Post #23 by @lassoan (2018-06-23 18:08 UTC)

<p>Again, you don’t need to build Slicer to extend it.</p>
<p>We are collaborating with your group already (I think we even have some joint funded project), so the best would be to have a Skype call to have a quick discussion about this. Please <a href="https://discourse.slicer.org/u/lassoan">write me a private message</a> or send an email to find a suitable time.</p>

---

## Post #24 by @brhoom (2018-06-23 20:30 UTC)

<p>try uninstall python, restart, reconfigure using cmake. The best experience for me to build Slicer is using fresh installed windows  then build Slicer requirements, after that build Slicer.</p>
<p>Also, I found building and using Slicer in Ubuntu is mush simpler and faster.</p>

---

## Post #25 by @lassoan (2018-06-23 23:14 UTC)

<aside class="quote no-group" data-username="brhoom" data-post="24" data-topic="2232">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/brhoom/48/1228_2.png" class="avatar"> brhoom:</div>
<blockquote>
<p>Also, I found building and using Slicer in Ubuntu is mush simpler and faster</p>
</blockquote>
</aside>
<p>It is always the easiest to build on the platform you are the most familiar with.</p>
<p>There is some truth in the points you described above, but there are simpler solutions to address these issues.</p>
<p>You can have Python versions installed, but you should never add Python path to global (system or user) environment variables. You may uninstall Python as a solution, but it is enough if you check that your global environment is not polluted.</p>
<p>There is no need for a “clean” Windows install, the only important requirement is that if you must install multiple Visual Studio versions, always install the older versions first.</p>

---

## Post #26 by @Saima (2018-06-24 02:50 UTC)

<p>I build the slicer last night. I see the Slicer.exe now in superbuild folder.</p>
<p>But in the error list I also see the following errors:<br>
Severity	Code	Description	Project	File	Line	Suppression State<br>
Error	LNK1104	cannot open file ‘Qt5::Widgets-NOTFOUND.obj’ [C:\Slicer-r26813\superbuild4.9\CTKAppLauncherLib-build\CTKAppLauncher.vcxproj]	CTKAppLauncherLib	C:\Slicer-r26813\superbuild4.9\LINK	1	<br>
Severity	Code	Description	Project	File	Line	Suppression State<br>
Error	MSB6006	“cmd.exe” exited with code 1. [C:\Slicer-r26813\superbuild4.9\CTK-build\CTK-build\Libs\Widgets\CTKWidgetsPythonQt.vcxproj] [C:\Slicer-r26813\superbuild4.9\CTK-build\CTK.vcxproj]	CTK	C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Microsoft.CppCommon.targets	171</p>
<p>I also see lots of warnings in the output window of visual studio:<br>
about 900+ for deprecated and some others.</p>
<p>During configuration I did what suggested by James.<br>
Thanks James</p>

---

## Post #27 by @Saima (2018-06-24 07:01 UTC)

<p>While building Run_Tests under cmake predefined target folder. I received following errors.<br>
The following tests FAILED:<br>
1&gt;	  7 - py_cmake_slicer_extensions_index_build_without_upload (Failed)<br>
1&gt;	  8 - py_cmake_slicer_extensions_index_build_with_upload (Failed)<br>
1&gt;	  9 - py_cmake_slicer_extensions_index_build_with_upload_using_ctest (Failed)<br>
1&gt;	 10 - py_cmake_slicer_extensions_index_build_without_upload_using_ctest (Failed)<br>
1&gt;	177 - qMRMLLayoutManagerTest1 (Failed)<br>
1&gt;	180 - qMRMLLayoutManagerTest4 (Failed)<br>
1&gt;	181 - qMRMLLayoutManagerVisibilityTest (Failed)<br>
1&gt;	363 - py_NeurosurgicalPlanningTutorialMarkupsSelfTest (Failed)<br>
1&gt;	405 - qSlicerReformatModuleWidgetGenericTest (Failed)<br>
1&gt;	433 - py_VolumeRenderingThreeDOnlyLayout (Timeout)<br>
1&gt;	438 - py_nomainwindow_qSlicerDataProbeModuleGenericTest (Failed)<br>
1&gt;	439 - py_nomainwindow_qSlicerDMRIInstallModuleGenericTest (Failed)<br>
1&gt;	440 - py_nomainwindow_qSlicerEditorModuleGenericTest (Failed)<br>
1&gt;	441 - py_ThresholdThreadingTest (Failed)<br>
1&gt;	442 - py_StandaloneEditorWidgetTest (Failed)<br>
1&gt;	443 - py_nomainwindow_qSlicerLabelStatisticsModuleGenericTest (Failed)<br>
1&gt;	445 - py_nomainwindow_qSlicerPerformanceTestsModuleGenericTest (Failed)<br>
1&gt;	446 - py_nomainwindow_qSlicerSampleDataModuleGenericTest (Failed)<br>
1&gt;	447 - py_nomainwindow_qSlicerScreenCaptureModuleGenericTest (Failed)<br>
1&gt;	450 - py_nomainwindow_qSlicerSegmentStatisticsModuleGenericTest (Failed)<br>
1&gt;	452 - py_nomainwindow_qSlicerSelfTestsModuleGenericTest (Failed)<br>
1&gt;	453 - py_nomainwindow_qSlicerSurfaceToolboxModuleGenericTest (Failed)<br>
1&gt;	454 - py_nomainwindow_qSlicerVectorToScalarVolumeModuleGenericTest (Failed)<br>
1&gt;	455 - py_nomainwindow_qSlicerExtensionWizardModuleGenericTest (Failed)<br>
1&gt;	456 - py_nomainwindow_qSlicerEndoscopyModuleGenericTest (Failed)<br>
1&gt;	457 - py_nomainwindow_qSlicerDICOMModuleGenericTest (Failed)<br>
1&gt;	458 - py_nomainwindow_qSlicerDICOMPatcherModuleGenericTest (Failed)<br>
1&gt;	459 - py_DICOMPatcher (Failed)<br>
1&gt;	549 - slicer_nomainwindow_NoApplicationInformationOptionTest (Timeout)<br>
1&gt;	587 - py_nomainwindow_SlicerOptionDisableSettingsTest (Failed)<br>
1&gt;	603 - py_nomainwindow_DCMTKPrivateDictTest (Failed)<br>
1&gt;	609 - py_DICOMReaders (Failed)<br>
1&gt;	612 - py_SlicerMRBMultipleSaveRestoreLoopTest (Failed)<br>
1&gt;	614 - py_SlicerMRBSaveRestoreCheckPathsTest (Failed)<br>
1&gt;	617 - py_Charting (Failed)<br>
1&gt;	622 - py_RSNAVisTutorial (Failed)<br>
1&gt;	630 - py_JRC2013Vis (Failed)<br>
1&gt;	632 - py_SubjectHierarchyGenericSelfTest (Failed)<br>
1&gt;	638 - py_nomainwindow_qSlicerMultiVolumeImporterModuleGenericTest (Failed)<br>
1&gt;	639 - py_nomainwindow_qSlicerSimpleFiltersModuleGenericTest (Failed)<br>
1&gt;	640 - py_SimpleFiltersModuleTest (Failed)<br>
1&gt;	658 - EMSegCL_Task_BRAINS_MRIHumanBrain_scalartype_float_very_small_fetchData (Failed)<br>
1&gt;	659 - EMSegCL_Task_BRAINS_MRIHumanBrain_scalartype_float_very_small (Failed)<br>
1&gt;	660 - EMSegCL_Task_BRAINS_MRIHumanBrain_scalartype_uint_very_small_fetchData (Failed)<br>
1&gt;	661 - EMSegCL_Task_BRAINS_MRIHumanBrain_scalartype_uint_very_small (Failed)<br>
1&gt;	675 - py_nomainwindow_qSlicerLandmarkRegistrationModuleGenericTest (Failed)<br>
1&gt;	676 - py_LandmarkRegistration (Failed)<br>
1&gt;Errors while running CTest<br>
1&gt;C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Microsoft.CppCommon.targets(133,5): error MSB3073: The command “setlocal<br>
1&gt;C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Microsoft.CppCommon.targets(133,5): error MSB3073: “C:\Program Files\CMake\bin\ctest.exe” --force-new-ctest-process -C Release<br>
1&gt;C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Microsoft.CppCommon.targets(133,5): error MSB3073: if %errorlevel% neq 0 goto :cmEnd<br>
1&gt;C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Microsoft.CppCommon.targets(133,5): error MSB3073: :cmEnd<br>
1&gt;C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Microsoft.CppCommon.targets(133,5): error MSB3073: endlocal &amp; call :cmErrorLevel %errorlevel% &amp; goto :cmDone<br>
1&gt;C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Microsoft.CppCommon.targets(133,5): error MSB3073: :cmErrorLevel<br>
1&gt;C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Microsoft.CppCommon.targets(133,5): error MSB3073: exit /b %1<br>
1&gt;C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Microsoft.CppCommon.targets(133,5): error MSB3073: :cmDone<br>
1&gt;C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Microsoft.CppCommon.targets(133,5): error MSB3073: if %errorlevel% neq 0 goto :VCEnd<br>
1&gt;C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\V140\Microsoft.CppCommon.targets(133,5): error MSB3073: :VCEnd” exited with code 8.<br>
1&gt;Done building project “RUN_TESTS.vcxproj” – FAILED.<br>
========== Build: 0 succeeded, 1 failed, 1 up-to-date, 0 skipped ==========</p>

---

## Post #28 by @lassoan (2018-06-24 12:39 UTC)

<p>Have you started Visual Studio using <code>Slicer.exe --VisualStudio</code>?</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Debug_Instructions#Using_Visual_Studio" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Debug_Instructions#Using_Visual_Studio</a></p>

---

## Post #29 by @Saima (2018-06-24 14:45 UTC)

<p>No I did not. I will do like you mentioned.</p>

---

## Post #30 by @jamesobutler (2018-06-24 15:23 UTC)

<p>If you are building Slicer nightly that uses Qt5, I should probably provide some additional hints regarding the installation of Qt.</p>
<p>With the Qt5 installer, choose Qt 5.10.1 with the option for the “MSVC 2015 x64” binaries since you are building with the msvc 2015 toolset(v140). You will also need to check the option to install “QWebEngine” under the 5.10.1 heading and I believe also the “Qt Script (deprecated)” option.</p>
<p>Note for Qt 5.11, QWebEngine is now only available for MSVC 2017 due to Chromium requirements, so QWebEngine won’t actually install even if it is checked and you choose the “MSVC 2015 x64” for Qt Core. So stick with Qt version 5.10.1 for now. I know this to work.</p>
<p>Slicer developers will need to confirm all dependicies can be built with MSVC 2017 if QWebEngine is to be used from the latest Qt5 versions.</p>

---

## Post #31 by @Saima (2018-06-25 04:01 UTC)

<p>James, I have used qt5.10.1, Visual studio community 2017 with msvc 2015 toolset v140. Slicer source code downloaded using:<br>
svn co <a href="http://svn.slicer.org/Slicer4/branches/Slicer-4-8" class="inline-onebox" rel="noopener nofollow ugc">GitHub - NA-MIC/svn.slicer.org-Slicer4: Archive of source code originally available at svn.slicer.org/Slicer4</a> Slicer-r26813 -r 26813<br>
cmake 3.9.2.<br>
setting for qt5 in cmake.</p>
<p>I see the Slicer.exe and when I run it, it opens and show me the slicer application.</p>
<p>I did not build QT. Do I need to build it??? I just installed qt binary and provided paths to QT in cmake.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/70f2122be1177eb22968d4e69cc266b5a529b902.png" data-download-href="/uploads/short-url/g7a6U8lYXGFQ5Q3neZH8fvDBF0S.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/70f2122be1177eb22968d4e69cc266b5a529b902_2_690x388.png" alt="image" data-base62-sha1="g7a6U8lYXGFQ5Q3neZH8fvDBF0S" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/70f2122be1177eb22968d4e69cc266b5a529b902_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/70f2122be1177eb22968d4e69cc266b5a529b902_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/70f2122be1177eb22968d4e69cc266b5a529b902_2_1380x776.png 2x" data-dominant-color="E8C1C2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 373 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #32 by @jamesobutler (2018-06-25 04:54 UTC)

<p>So you were able to build Slicer and the application runs successfully. Congrats!</p>
<p>I’m a little confused that your cmake is showing paths to msvc2017_64 which would you would use if you were using the msvc2017 toolset(v141) and not msvc2015 toolset(v140), but if Slicer works I won’t complain.</p>
<p>You don’t have to manually build Qt to get a working build of Slicer. The downloaded binaries will work fine on their own. The qt-easy-build repo is for building Qt with OpenSSL support. I’ll provide an update to the windows powershell scripts for 5.10.0 in that repo soon.</p>

---

## Post #33 by @Saima (2018-06-25 05:33 UTC)

<p>James, Slicer.exe opens like this. It successfully imported 130 modules out of 136<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af165250c8c7dc94a00d0534aa483eb3fc35bfb7.png" data-download-href="/uploads/short-url/oYTnCDo8QVx9K629fRldk8NE8Cj.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/af165250c8c7dc94a00d0534aa483eb3fc35bfb7_2_690x388.png" alt="image" data-base62-sha1="oYTnCDo8QVx9K629fRldk8NE8Cj" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/af165250c8c7dc94a00d0534aa483eb3fc35bfb7_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/af165250c8c7dc94a00d0534aa483eb3fc35bfb7_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/af165250c8c7dc94a00d0534aa483eb3fc35bfb7_2_1380x776.png 2x" data-dominant-color="737374"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 324 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>what I did wrong. any step need to be corrected to correct it??? I am also confused whether it is build correctly or not??</p>

---

## Post #34 by @lassoan (2018-06-25 10:22 UTC)

<p>I think full DICOM support (pyDICOM) requires building Slicer with OpenSSL support enabled.</p>

---

## Post #35 by @jamesobutler (2018-06-25 12:17 UTC)

<p>Saima,</p>
<p>You mentioned using code from a Slicer-48 branch with revision number 26813. This is source code for building Slicer Stable 4.8.1 which should be built with Qt4 though I think there was early support for Qt5. Instead, you should be building the most recent Slicer Nightly/Preview which is using the source code found in the master branch of the Slicer github repo. You don’t need to do anything with svn right now.</p>
<p>Also make sure you download and use Qt 5.10.1 msvc2015_x64 with QWebEngine and Qt Script.</p>

---

## Post #36 by @Saima (2018-06-26 11:53 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="35" data-topic="2232">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>should be building the most recent Slicer Nightly/Preview</p>
</blockquote>
</aside>
<p>how can I get the source code for latest slicer</p>

---

## Post #37 by @Saima (2018-06-26 13:43 UTC)

<p>I did configuration with ssl support on in cmake but no change.</p>

---

## Post #38 by @jamesobutler (2018-06-26 13:59 UTC)

<p>Hi Saima,</p>
<p>I provided information about where to get the source code for the latest Slicer:</p>
<blockquote>
<p>Instead, you should be building the most recent Slicer Nightly/Preview which is using the source code found in the master branch of the Slicer github repo.</p>
</blockquote>
<p>Now I didn’t provide a link which I can do now (<a href="https://github.com/Slicer/Slicer" rel="noopener nofollow ugc">Slicer Github Repo</a>), but since right now you lack this introductory knowledge about Github, I <strong>highly</strong> suggest that you proceed development using the latest <a href="https://download.slicer.org/" rel="noopener nofollow ugc">Slicer binaries</a> and extending on the Slicer platform using <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting" rel="noopener nofollow ugc">Slicer Python Scripting</a> as suggested by <a class="mention" href="/u/lassoan">@lassoan</a> .</p>

---

## Post #39 by @timeanddoctor (2018-07-12 08:05 UTC)

<p>I built slicer in Win10 firstly. what can I do after following this error.<br>
Thanks!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5dd40212a439756b491eb33956590802f002711.png" data-download-href="/uploads/short-url/wNtmNEwnTNiNihqsCo08SRvrMT7.png?dl=1" title="%E6%8D%95%E8%8E%B7" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e5dd40212a439756b491eb33956590802f002711_2_689x373.png" alt="%E6%8D%95%E8%8E%B7" data-base62-sha1="wNtmNEwnTNiNihqsCo08SRvrMT7" width="689" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e5dd40212a439756b491eb33956590802f002711_2_689x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/5/e5dd40212a439756b491eb33956590802f002711_2_1033x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5dd40212a439756b491eb33956590802f002711.png 2x" data-dominant-color="F5A6A8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">%E6%8D%95%E8%8E%B7</span><span class="informations">1240×671 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #40 by @lassoan (2018-07-12 13:06 UTC)

<p>It all looks good! Where do you see an error?</p>
<p>Your source directory path (D:/slicer/Slicer) is a bit too long, which may cause problem later. I would recommend to use D:/D/S4 for source and D:/D/S4D (for debug) or D:/D/S4R (for release) binary directory.</p>

---

## Post #41 by @jamesobutler (2018-07-12 13:49 UTC)

<p>Since it appears you are building Slicer Nightly/Preview, it is probably best to build with Qt5 support even though Qt4 is still technically supported.  Build instructions for the Slicer nightly on Windows can be found <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Windows" rel="nofollow noopener">here</a>.</p>
<p>Also, your QT_QMAKE_EXECUTABLE entry was set to “C:/Qt/Qtcreator-2.5.2/bin/qtcreator.exe”.  It should be something like “…QT_DIR/bin/qmake.exe”</p>

---

## Post #42 by @Mian_Asbat_Ahmad (2019-01-25 23:01 UTC)

<p>Hi James and others,<br>
I followed all the documentation and I am still getting the error.<br>
I dont know why it is search for old version of qt when we have specified the qt 5.10. Any idea?<br>
I didnt know this step where we have to QT5_DIR variable before pressing configure in cmake.<br>
How can I set it. I added new entry with path option. I believe this is the variable.<br>
Thanks.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d54d1290467c59f39b938372a7aecd3df1cb28da.png" data-download-href="/uploads/short-url/uqWPm0kTzSmoaA1KroChi7xGE1s.png?dl=1" title="41" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d54d1290467c59f39b938372a7aecd3df1cb28da_2_690x411.png" alt="41" data-base62-sha1="uqWPm0kTzSmoaA1KroChi7xGE1s" width="690" height="411" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d54d1290467c59f39b938372a7aecd3df1cb28da_2_690x411.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d54d1290467c59f39b938372a7aecd3df1cb28da_2_1035x616.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d54d1290467c59f39b938372a7aecd3df1cb28da_2_1380x822.png 2x" data-dominant-color="F5BBBB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">41</span><span class="informations">2880×1716 450 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #43 by @pieper (2019-01-25 23:26 UTC)

<p>You also need to set the Qt version to 5.10.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3da0134db063940db4a9368999b7b1e3afc5135e.png" alt="image" data-base62-sha1="8Na5jjmebxBPujVxVKQCkqpVeeW" width="400" height="37"></p>
<p>I haven’t tried lately on windows, but maybe you can just change that through the cmake gui and reconfigure.</p>
<p>Usually I avoid the guis and write a little command line so I can blow away the build directory and get back to a known state if needed.</p>
<p>e.g. here’s a script for building against a homebrow installation of qt on mac.</p>
<pre><code class="lang-auto">cmake \
  -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
  -DSlicer_VTK_RENDERING_BACKEND:STRING=OpenGL2 \
  -DSlicer_REQUIRED_QT_VERSION=5 \
  -DQT_QMAKE_EXECUTABLE:FILEPATH=/usr/local/opt/qt5/bin/qmake \
  -DQt5_DIR:FILEPATH=/usr/local/opt/qt5/lib/cmake/Qt5 \
  -DQt5Core_DIR:FILEPATH=/usr/local/opt/qt5/lib/cmake/Qt5Core \
  -DCMAKE_OSX_DEPLOYMENT_TARGET:STRING=10.9 \
  -DSlicer_USE_PYTHONQT_WITH_TCL:BOOL=OFF \
  -DSlicer_USE_SimpleITK:BOOL=OFF \
  -DSlicer_USE_QtTesting:BOOL=ON \
  ~/slicer4/latest/Slicer
</code></pre>

---

## Post #44 by @jamesobutler (2019-01-25 23:43 UTC)

<p>Yes <a class="mention" href="/u/mian_asbat_ahmad">@Mian_Asbat_Ahmad</a>, the QT_QMAKE_EXECUTABLE entry is for building Slicer with Qt4, so you don’t need anything in that entry if you are going to build with Qt5. If you update the Slicer_REQUIRED_QT_VERSION to 5.10.0, then press Configure, a new entry will appear called Qt5_Dir and you will specify “C:/Qt/5.10.0/msvc2015_64/lib/cmake/Qt5”.  The latest version for full functionality in a Windows build of Slicer is Qt 5.10 series in which case there is actually a Qt 5.10.1 release you can use. That’s what I’ve been using lately.</p>
<p>This is different advice from <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Windows_2" rel="nofollow noopener">this</a> build instructions section. There it mentions “<strong>Do not configure yet</strong>”, to manually add the Qt5_Dir entry, and then configure. Not entirely sure why it is specified in bold to do things in this order, but I find it easiest to do what I suggested above.</p>

---

## Post #45 by @lassoan (2019-01-26 02:12 UTC)

<p>If a build tree is configured with a Qt version then you must build with that version, because any attempt to change to a different one will fail (it will be only partially successful; probably this is a bug in Qt CMake scripts). That is why it is very important to set Qt5_DIR before you configure the project.</p>
<p>If you have only one Qt version or CMake cannot find an incorrect Qt version then you may specify Qt5_DIR later, but in general you need to strictly follow the prescribed order.</p>

---

## Post #46 by @Mian_Asbat_Ahmad (2019-01-28 10:12 UTC)

<p>Dear team,<br>
Thank you for your response.<br>
To clarify I didnt change <code>Slicer_REQUIRED_QT_VERSION</code> to 4.7.4. It was automatically picked following the guide.</p>
<p>Okay I am a bit hasty so I tried James suggestions in two steps. I will try CLI after I fixed the cmake-gui.</p>
<p>First I changed the <code>Slicer_REQUIRED_QT_VERSION</code> to 5.10.0 and run the configure and I got the following error.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54f16301f9e8f028d2a282e5dcd7a896c530dbfa.png" data-download-href="/uploads/short-url/c7rh7SdY0FK6qOrZM0lZ5ueOZYK.png?dl=1" title="06" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/54f16301f9e8f028d2a282e5dcd7a896c530dbfa_2_690x412.png" alt="06" data-base62-sha1="c7rh7SdY0FK6qOrZM0lZ5ueOZYK" width="690" height="412" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/54f16301f9e8f028d2a282e5dcd7a896c530dbfa_2_690x412.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/54f16301f9e8f028d2a282e5dcd7a896c530dbfa_2_1035x618.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/54f16301f9e8f028d2a282e5dcd7a896c530dbfa_2_1380x824.png 2x" data-dominant-color="F4B9B8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">06</span><span class="informations">2876×1718 478 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I read more and found the second step so I set <code>QT5_DIR</code> to <code>C:/Qt/5.10.0/msvc2015_64/lib/cmake/Qt5</code> and run configure again. This time the red colour disappeared but I still have a bug. Here is the screenshot.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/25768fe57ca5139bd5fda10cd7a17c6e86aae016.png" data-download-href="/uploads/short-url/5lpGrjncFHudUuUy0MzZfmugkke.png?dl=1" title="48" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/25768fe57ca5139bd5fda10cd7a17c6e86aae016_2_690x411.png" alt="48" data-base62-sha1="5lpGrjncFHudUuUy0MzZfmugkke" width="690" height="411" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/25768fe57ca5139bd5fda10cd7a17c6e86aae016_2_690x411.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/25768fe57ca5139bd5fda10cd7a17c6e86aae016_2_1035x616.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/25768fe57ca5139bd5fda10cd7a17c6e86aae016_2_1380x822.png 2x" data-dominant-color="F7F7F7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">48</span><span class="informations">2878×1718 381 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Any idea for the new error. Do I have to install curl?</p>

---

## Post #47 by @lassoan (2019-01-30 01:49 UTC)

<p>The error is about not finding <code>External_curl.cmake</code> file. It is located in slicer source tree in SuperBuild folder. If it is not there then the cloning of the repository was incomplete. Pull from the Slicer repository again and if you still don’t get the file then clone the repository again.</p>

---

## Post #48 by @Mian_Asbat_Ahmad (2019-01-30 10:35 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> many thanks, after downloading the project again the error disappeared. It is generated successfully.<br>
Feedback: It would be very nice to have a separate guide for each major platform stable version windows, mac and linux because for new users like me it was difficult to follow and without your help it wouldn’t be possible.</p>

---

## Post #49 by @kookoo9999 (2021-09-17 05:54 UTC)

<p>Hello james.<br>
I wnat to build Slicer ( 4.11 20200930) on Windows10 but  build failed repeatedly.<br>
My env is<br>
Visual Studio 2017<br>
Qt 5.10.1(include WebEngine,Script)<br>
CMake 3.15.0-rc1.</p>
<p>There is no problem with Configuration in CMake(option Visual Studio 2017,x64) and generate too.<br>
but when I build the ALL_BUILD in Slicer.sln , I see the Message of Build Fail 48 out of 54 …</p>
<p>And I can’t find Slicer.exe at Slicer_build\build\ or Slicer_build.<br>
Did I do anything wrong?</p>

---

## Post #50 by @kookoo9999 (2021-09-17 07:27 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56e9783aa5c94343599427ea1d3aca16df531be4.png" data-download-href="/uploads/short-url/coRgFwgrYqLL4rzpvygzKJ9rT3S.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56e9783aa5c94343599427ea1d3aca16df531be4_2_690x373.png" alt="image" data-base62-sha1="coRgFwgrYqLL4rzpvygzKJ9rT3S" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56e9783aa5c94343599427ea1d3aca16df531be4_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56e9783aa5c94343599427ea1d3aca16df531be4_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/56e9783aa5c94343599427ea1d3aca16df531be4_2_1380x746.png 2x" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1038 47.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13da421558628a74a7e328d29add67b4a51233c7.png" data-download-href="/uploads/short-url/2PCGE4fqEPr9VGhIUJwjeNKTQc7.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13da421558628a74a7e328d29add67b4a51233c7.png" alt="image" data-base62-sha1="2PCGE4fqEPr9VGhIUJwjeNKTQc7" width="583" height="500" data-dominant-color="F2F1F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1101×943 28.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35ed1c844d607d0ee4d4245aedc2c5b5c417ce94.png" data-download-href="/uploads/short-url/7H3jvUdYwbEgJm42YtbRCYZvj3S.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/35ed1c844d607d0ee4d4245aedc2c5b5c417ce94.png" alt="image" data-base62-sha1="7H3jvUdYwbEgJm42YtbRCYZvj3S" width="690" height="308" data-dominant-color="484747"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1274×570 18.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>S4R is Slicer-4.11.20200930 source code.<br>
All_Build is failed so I can’t find Slicer.exe.<br>
I tried to build this <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html" rel="noopener nofollow ugc">link</a>.</p>

---
