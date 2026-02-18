# MSB8066 error while building 3DSlicer latest version

**Topic ID**: 26246
**Date**: 2022-11-15
**URL**: https://discourse.slicer.org/t/msb8066-error-while-building-3dslicer-latest-version/26246

---

## Post #1 by @Dya (2022-11-15 11:57 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/79efe6fe66bb239c6a2363629cfaf92934074e8c.png" data-download-href="/uploads/short-url/hoHLgb0WNayanX3I6qGSlAv0ZRi.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/79efe6fe66bb239c6a2363629cfaf92934074e8c.png" alt="image" data-base62-sha1="hoHLgb0WNayanX3I6qGSlAv0ZRi" width="690" height="362" data-dominant-color="2F2F2F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1012×531 44.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
The cmake has compiled and generated without any error. I am getting this error message while building 3DSlicer in visual studio 2022 .I have searched this topic and found out to use the latest version of 3d slicer patched after 28 SEP 2022. I have tried it with the latest version updated on 14-Nov-2022.But the error still persists. I have been stuck with his for the past one week. Kindly help. Many users had asked this question but there is no proper answer.</p>
<p>I tried with:<br>
CMake = 3.19.5, 3.22.4, 3.25.0<br>
Visual studio =  2019, 2022<br>
QT =  5.12.2<br>
OS = WIindows 10 64 bit<br>
git version 2.38.1.windows.1</p>

---

## Post #2 by @lassoan (2022-11-15 12:01 UTC)

<p>You may get the error because your build folder path is too long. Please restart the build from scratch using F:\D\S5 for source code and F:\D\S5R or F:\D\S5D for the build folder.</p>

---

## Post #3 by @Dya (2022-11-16 11:31 UTC)

<p>Hello Lassoan,<br>
I build the code as you suggested but still the error occurs.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5a1336afea7f2025cc33054d19d30ff65c8a358.png" data-download-href="/uploads/short-url/wLoI8MXQ1udnGdMY7UBtMzDBzuw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e5a1336afea7f2025cc33054d19d30ff65c8a358.png" alt="image" data-base62-sha1="wLoI8MXQ1udnGdMY7UBtMzDBzuw" width="690" height="254" data-dominant-color="2E2E2E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1167×430 27.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2022-11-22 12:42 UTC)

<p>I’ve set up build on a completely new machine</p>
<p>CMake = 3.22.4 (with 3.25.0 or fails, see <a href="https://gitlab.kitware.com/cmake/cmake/-/issues/24180" class="inline-onebox">CHECK_TYPE_SIZE regression in CMake-3.25.0 (#24180) · Issues · CMake / CMake · GitLab</a>)<br>
Visual studio = 2022, toolset v143<br>
QT = 5.15.2<br>
OS = WIindows 11 64 bit</p>
<p>The build completed suxxeasfully.</p>
<p>The main difference that I see that you tried to use Qt-5.12. In the build instructions the required Qt version is 5.15.2. Try to use that and let us know if it fixed the issue.</p>

---

## Post #7 by @Dya (2022-11-24 08:37 UTC)

<p>Thanks for replying, I have build the slicer as per your suggestion .<br>
CMake = 3.22.4<br>
Visual Studio 2022, v143<br>
QT=  5.15.2<br>
OS = Windows 10 ,64 bit.</p>
<p>The build still fails at CTK.</p>
<blockquote>
<p>C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets(247,5): warning MSB8065: Custom build for item “F:\D\S5D\CTK-build\CMakeFiles\efd08cadf5a1ea590d1828fc661b072b\CTK-configure.rule” succeeded, but specified output “f:\d\s5d\ctk-build\ctk-prefix\src\ctk-stamp\release\ctk-configure” has not been created. This may cause incremental build to work incorrectly. [F:\D\S5D\CTK-build\CTK.vcxproj]</p>
<p>36&gt;C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets(247,5): warning MSB8064: Custom build for item “F:\D\S5D\CTK-build\CMakeFiles\efd08cadf5a1ea590d1828fc661b072b\CTK-build.rule” succeeded, but specified dependency “f:\d\s5d\ctk-build\ctk-prefix\src\ctk-stamp\release\ctk-configure” does not exist. This may cause incremental build to work incorrectly. [F:\D\S5D\CTK-build\CTK.vcxproj]</p>
</blockquote>

---

## Post #8 by @Dya (2022-11-24 11:38 UTC)

<p>This is the build log of CTK.</p>
<blockquote>
<p>Build started…<br>
1&gt;------ Build started: Project: CTK, Configuration: Release x64 ------<br>
1&gt;Performing update step for ‘CTK’<br>
1&gt;No patch step for ‘CTK’<br>
1&gt;Performing configure step for ‘CTK’<br>
1&gt;loading initial cache file F:/D/S5D/CTK-prefix/tmp/CTK-cache-Release.cmake<br>
1&gt;-- Selecting Windows SDK version 10.0.19041.0 to target Windows 10.0.17134.<br>
1&gt;CMake Deprecation Warning at F:/D/S5D/CTK/Utilities/DGraph/CMakeLists.txt:21 (cmake_minimum_required):<br>
1&gt;  Compatibility with CMake &lt; 2.8.12 will be removed from a future version of<br>
1&gt;  CMake.<br>
1&gt;<br>
1&gt;  Update the VERSION argument  value or use a … suffix to tell<br>
1&gt;  CMake that the project does not need compatibility with older versions.<br>
1&gt;<br>
1&gt;<br>
1&gt;-- Generated: F:/D/S5D/CTK-build/DGraphInput-alldep.txt<br>
1&gt;-- Generated: F:/D/S5D/CTK-build/DGraphInput-alldep-withext.txt<br>
1&gt;-- Generated: F:/D/S5D/CTK-build/DGraphInput.txt<br>
1&gt;-- SuperBuild - First pass<br>
1&gt;-- SuperBuild - First pass - done<br>
1&gt;-- SuperBuild - Log4Qt[OPTIONAL]<br>
1&gt;-- SuperBuild - ZMQ[OPTIONAL]<br>
1&gt;-- SuperBuild - QtSOAP[OPTIONAL]<br>
1&gt;-- SuperBuild - qxmlrpc[OPTIONAL]<br>
1&gt;-- SuperBuild - qRestAPI[OPTIONAL]<br>
1&gt;-- SuperBuild - OpenIGTLink[OPTIONAL]<br>
1&gt;-- SuperBuild - CTK =&gt; Requires VTK, PythonQt, DCMTK, ITK, QtTesting,<br>
1&gt;-- SuperBuild -   VTK[OK]<br>
1&gt;-- SuperBuild -   PythonQt[OK]<br>
1&gt;-- SuperBuild -   DCMTK[OK]<br>
1&gt;-- SuperBuild -   ITK[OK]<br>
1&gt;-- SuperBuild -   QtTesting[OK]<br>
1&gt;-- Adding project:QtTesting<br>
1&gt;-- SuperBuild - CTK[OK]<br>
1&gt;-- Configuring done<br>
1&gt;-- Generating done<br>
1&gt;-- Build files have been written to: F:/D/S5D/CTK-build<br>
1&gt;Performing build step for ‘CTK’<br>
1&gt;MSBuild version 17.3.1+2badb37d1 for .NET Framework<br>
1&gt;  Performing update step for ‘PythonQt’<br>
1&gt;  No patch step for ‘PythonQt’<br>
1&gt;  Performing configure step for ‘PythonQt’<br>
1&gt;  loading initial cache file F:/D/S5D/CTK-build/PythonQt-cmake/tmp/PythonQt-cache-Release.cmake<br>
1&gt;  – Selecting Windows SDK version 10.0.19041.0 to target Windows 10.0.17134.<br>
1&gt;  – PythonQt: Required Qt components [Core;Widgets;Multimedia;PrintSupport;Network;MultimediaWidgets;UiTools]<br>
1&gt;  – Configuring done<br>
1&gt;  – Generating done<br>
1&gt;  – Build files have been written to: F:/D/S5D/CTK-build/PythonQt-build<br>
1&gt;  No build step for ‘PythonQt’<br>
1&gt;  Performing install step for ‘PythonQt’<br>
1&gt;  MSBuild version 17.3.1+2badb37d1 for .NET Framework<br>
1&gt;    PythonQt.vcxproj → F:\D\S5D\CTK-build\PythonQt-build\Release\PythonQt.dll<br>
1&gt;    – Install configuration: “Release”<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/lib/PythonQt.lib<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/bin/PythonQt.dll<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtBoolResult.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtClassInfo.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtClassWrapper.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtConversion.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtCppWrapperFactory.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtDoc.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQt.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtImporter.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtImportFileInterface.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtInstanceWrapper.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtMethodInfo.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtMisc.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtObjectPtr.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtProperty.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtQFileImporter.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtSignalReceiver.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtSlot.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtSlotDecorator.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtSignal.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtStdDecorators.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtStdIn.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtStdOut.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtSystem.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtThreadSupport.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtUtils.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtVariants.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtPythonInclude.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQt_QtBindings.h<br>
1&gt;  Completed ‘PythonQt’<br>
1&gt;  Performing update step for ‘QtTesting’<br>
1&gt;  No patch step for ‘QtTesting’<br>
1&gt;  Performing configure step for ‘QtTesting’<br>
1&gt;  loading initial cache file F:/D/S5D/CTK-build/QtTesting-cmake/tmp/QtTesting-cache-Release.cmake<br>
1&gt;  – Selecting Windows SDK version 10.0.19041.0 to target Windows 10.0.17134.<br>
1&gt;  – Configuring done<br>
1&gt;  CMake Warning (dev) in CMakeLists.txt:<br>
1&gt;    Policy CMP0020 is not set: Automatically link Qt executables to qtmain<br>
1&gt;    target on Windows.  Run “cmake --help-policy CMP0020” for policy details.<br>
1&gt;    Use the cmake_policy command to set the policy and suppress this warning.<br>
1&gt;  This warning is for project developers.  Use -Wno-dev to suppress it.<br>
1&gt;<br>
1&gt;  CMake Warning (dev) in CMakeLists.txt:<br>
1&gt;    Policy CMP0020 is not set: Automatically link Qt executables to qtmain<br>
1&gt;    target on Windows.  Run “cmake --help-policy CMP0020” for policy details.<br>
1&gt;    Use the cmake_policy command to set the policy and suppress this warning.<br>
1&gt;  This warning is for project developers.  Use -Wno-dev to suppress it.<br>
1&gt;<br>
1&gt;  CMake Warning (dev) in CMakeLists.txt:<br>
1&gt;    Policy CMP0020 is not set: Automatically link Qt executables to qtmain<br>
1&gt;    target on Windows.  Run “cmake --help-policy CMP0020” for policy details.<br>
1&gt;    Use the cmake_policy command to set the policy and suppress this warning.<br>
1&gt;  This warning is for project developers.  Use -Wno-dev to suppress it.<br>
1&gt;<br>
1&gt;  CMake Warning (dev) in CMakeLists.txt:<br>
1&gt;    Policy CMP0020 is not set: Automatically link Qt executables to qtmain<br>
1&gt;    target on Windows.  Run “cmake --help-policy CMP0020” for policy details.<br>
1&gt;    Use the cmake_policy command to set the policy and suppress this warning.<br>
1&gt;  This warning is for project developers.  Use -Wno-dev to suppress it.<br>
1&gt;<br>
1&gt;  CMake Warning (dev) in CMakeLists.txt:<br>
1&gt;    Policy CMP0020 is not set: Automatically link Qt executables to qtmain<br>
1&gt;    target on Windows.  Run “cmake --help-policy CMP0020” for policy details.<br>
1&gt;    Use the cmake_policy command to set the policy and suppress this warning.<br>
1&gt;  This warning is for project developers.  Use -Wno-dev to suppress it.<br>
1&gt;<br>
1&gt;  CMake Warning (dev) in CMakeLists.txt:<br>
1&gt;    Policy CMP0020 is not set: Automatically link Qt executables to qtmain<br>
1&gt;    target on Windows.  Run “cmake --help-policy CMP0020” for policy details.<br>
1&gt;    Use the cmake_policy command to set the policy and suppress this warning.<br>
1&gt;  This warning is for project developers.  Use -Wno-dev to suppress it.<br>
1&gt;<br>
1&gt;  CMake Warning (dev) in CMakeLists.txt:<br>
1&gt;    Policy CMP0020 is not set: Automatically link Qt executables to qtmain<br>
1&gt;    target on Windows.  Run “cmake --help-policy CMP0020” for policy details.<br>
1&gt;    Use the cmake_policy command to set the policy and suppress this warning.<br>
1&gt;  This warning is for project developers.  Use -Wno-dev to suppress it.<br>
1&gt;<br>
1&gt;  CMake Warning (dev) in CMakeLists.txt:<br>
1&gt;    Policy CMP0020 is not set: Automatically link Qt executables to qtmain<br>
1&gt;    target on Windows.  Run “cmake --help-policy CMP0020” for policy details.<br>
1&gt;    Use the cmake_policy command to set the policy and suppress this warning.<br>
1&gt;  This warning is for project developers.  Use -Wno-dev to suppress it.<br>
1&gt;<br>
1&gt;  – Generating done<br>
1&gt;  – Build files have been written to: F:/D/S5D/CTK-build/QtTesting-build<br>
1&gt;  Performing build step for ‘QtTesting’<br>
1&gt;  MSBuild version 17.3.1+2badb37d1 for .NET Framework<br>
1&gt;    QtTesting.vcxproj → F:\D\S5D\CTK-build\QtTesting-build\Release\QtTesting.dll<br>
1&gt;  Performing install step for ‘QtTesting’<br>
1&gt;  MSBuild version 17.3.1+2badb37d1 for .NET Framework<br>
1&gt;    QtTesting.vcxproj → F:\D\S5D\CTK-build\QtTesting-build\Release\QtTesting.dll<br>
1&gt;    – Install configuration: “Release”<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/lib/QtTesting.lib<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/bin/QtTesting.dll<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/QtTestingExport.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pq3DViewEventPlayer.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pq3DViewEventTranslator.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqAbstractActivateEventPlayer.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqAbstractBooleanEventPlayer.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqAbstractButtonEventTranslator.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqAbstractDoubleEventPlayer.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqAbstractIntEventPlayer.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqAbstractItemViewEventPlayer.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqAbstractItemViewEventPlayerBase.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqAbstractItemViewEventTranslator.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqAbstractItemViewEventTranslatorBase.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqAbstractMiscellaneousEventPlayer.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqAbstractSliderEventTranslator.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqAbstractStringEventPlayer.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqBasicWidgetEventPlayer.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqBasicWidgetEventTranslator.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqCheckEventOverlay.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqComboBoxEventTranslator.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqComboBoxEventPlayer.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqCommentEventPlayer.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqDoubleSpinBoxEventTranslator.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqEventComment.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqEventDispatcher.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqEventObserver.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqEventPlayer.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqEventRecorder.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqEventSource.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqEventTranslator.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqEventTypes.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqLineEditEventTranslator.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqListViewEventPlayer.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqListViewEventTranslator.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqMenuEventTranslator.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqNativeFileDialogEventPlayer.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqNativeFileDialogEventTranslator.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqObjectNaming.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqPlayBackEventsDialog.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqRecordEventsDialog.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqSpinBoxEventTranslator.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqStdoutEventObserver.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqTabBarEventPlayer.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqTabBarEventTranslator.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqTableViewEventPlayer.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqTableViewEventTranslator.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqTestUtility.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqThreadedEventSource.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqTimer.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqTreeViewEventPlayer.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqTreeViewEventTranslator.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqWidgetEventPlayer.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/pqWidgetEventTranslator.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/include/QtTesting/QtTestingConfigure.h<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/lib/cmake/qttesting/QtTestingConfig.cmake<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/lib/cmake/qttesting/QtTestingTargets.cmake<br>
1&gt;    – Up-to-date: F:/D/S5D/CTK-build/CMakeExternals/Install/lib/cmake/qttesting/QtTestingTargets-release.cmake<br>
1&gt;  Completed ‘QtTesting’<br>
1&gt;  Performing configure step for ‘CTK’<br>
1&gt;  loading initial cache file F:/D/S5D/CTK-build/CTK-prefix/tmp/CTK-cache-Release.cmake<br>
1&gt;  – Selecting Windows SDK version 10.0.19041.0 to target Windows 10.0.17134.<br>
1&gt;  CMake Deprecation Warning at F:/D/S5D/CTK/Utilities/DGraph/CMakeLists.txt:21 (cmake_minimum_required):<br>
1&gt;    Compatibility with CMake &lt; 2.8.12 will be removed from a future version of<br>
1&gt;    CMake.<br>
1&gt;<br>
1&gt;    Update the VERSION argument  value or use a … suffix to tell<br>
1&gt;    CMake that the project does not need compatibility with older versions.<br>
1&gt;<br>
1&gt;<br>
1&gt;  – Generated: F:/D/S5D/CTK-build/CTK-build/DGraphInput-alldep.txt<br>
1&gt;  – Generated: F:/D/S5D/CTK-build/CTK-build/DGraphInput-alldep-withext.txt<br>
1&gt;  – Generated: F:/D/S5D/CTK-build/CTK-build/DGraphInput.txt<br>
1&gt;  – SuperBuild - First pass<br>
1&gt;  – SuperBuild - First pass - done<br>
1&gt;  – Trying to find DCMTK expecting DCMTKConfig.cmake<br>
1&gt;  – Trying to find DCMTK expecting DCMTKConfig.cmake - ok<br>
1&gt;  – [ITK] Skipping nonexistent library directory or not set variable [ITK_LIBRARY_DIRS]<br>
1&gt;  – [VTK] Skipping nonexistent include directory or not set variable [VTK_INCLUDE_DIRS]<br>
1&gt;  – [VTK] Skipping nonexistent library directory or not set variable [VTK_LIBRARY_DIRS]<br>
1&gt;  – CTKCore: BFD support disabled<br>
1&gt;  – Looking for decorator header ctkCorePythonQtDecorators.h<br>
1&gt;  – Looking for decorator header ctkCorePythonQtDecorators.h - Found<br>
1&gt;  – Looking for decorator header ctkWidgetsPythonQtDecorators.h<br>
1&gt;  – Looking for decorator header ctkWidgetsPythonQtDecorators.h - Found<br>
1&gt;  – Looking for decorator header ctkDICOMCorePythonQtDecorators.h<br>
1&gt;  – Looking for decorator header ctkDICOMCorePythonQtDecorators.h - Found<br>
1&gt;  – Looking for decorator header ctkDICOMWidgetsPythonQtDecorators.h<br>
1&gt;  – Looking for decorator header ctkDICOMWidgetsPythonQtDecorators.h - Found<br>
1&gt;  – ITK is setting CTKImageProcessingITKCore’s MSVC_RUNTIME_LIBRARY to dynamic<br>
1&gt;  – Looking for decorator header ctkImageProcessingITKCorePythonQtDecorators.h<br>
1&gt;  – Looking for decorator header ctkImageProcessingITKCorePythonQtDecorators.h - Not found<br>
1&gt;  – Looking for decorator header ctkScriptingPythonWidgetsPythonQtDecorators.h<br>
1&gt;  – Looking for decorator header ctkScriptingPythonWidgetsPythonQtDecorators.h - Not found<br>
1&gt;  – Looking for decorator header ctkVisualizationVTKCorePythonQtDecorators.h<br>
1&gt;  – Looking for decorator header ctkVisualizationVTKCorePythonQtDecorators.h - Not found<br>
1&gt;  – Looking for decorator header ctkVisualizationVTKWidgetsPythonQtDecorators.h<br>
1&gt;  – Looking for decorator header ctkVisualizationVTKWidgetsPythonQtDecorators.h - Found<br>
1&gt;  – Looking for decorator header ctkQtTestingPythonQtDecorators.h<br>
1&gt;  – Looking for decorator header ctkQtTestingPythonQtDecorators.h - Not found<br>
1&gt;  – Including CMake built-in module CMakePackageConfigHelpers<br>
1&gt;  – Including CMake built-in module CMakePackageConfigHelpers - ok<br>
1&gt;  – Configuring done<br>
1&gt;  – Generating done<br>
1&gt;  – Build files have been written to: F:/D/S5D/CTK-build/CTK-build<br>
1&gt;  Performing build step for ‘CTK’<br>
1&gt;  MSBuild version 17.3.1+2badb37d1 for .NET Framework<br>
1&gt;    CTKCore.vcxproj → F:\D\S5D\CTK-build\CTK-build\bin\Release\CTKCore.dll<br>
1&gt;    CTKCorePythonQt.vcxproj → F:\D\S5D\CTK-build\CTK-build\bin\Release\CTKCorePythonQt.pyd<br>
1&gt;    CTKDICOMCore.vcxproj → F:\D\S5D\CTK-build\CTK-build\bin\Release\CTKDICOMCore.dll<br>
1&gt;    CTKDICOMCorePythonQt.vcxproj → F:\D\S5D\CTK-build\CTK-build\bin\Release\CTKDICOMCorePythonQt.pyd<br>
1&gt;    CTKWidgets.vcxproj → F:\D\S5D\CTK-build\CTK-build\bin\Release\CTKWidgets.dll<br>
1&gt;    CTKDICOMWidgets.vcxproj → F:\D\S5D\CTK-build\CTK-build\bin\Release\CTKDICOMWidgets.dll<br>
1&gt;    CTKDICOMWidgetsPlugins.vcxproj → F:\D\S5D\CTK-build\CTK-build\bin\designer\Release\CTKDICOMWidgetsPlugins.dll<br>
1&gt;    CTKDICOMWidgetsPythonQt.vcxproj → F:\D\S5D\CTK-build\CTK-build\bin\Release\CTKDICOMWidgetsPythonQt.pyd<br>
1&gt;    CTKImageProcessingITKCore.vcxproj → F:\D\S5D\CTK-build\CTK-build\bin\Release\CTKImageProcessingITKCore.dll<br>
1&gt;    CTKImageProcessingITKCorePythonQt.vcxproj → F:\D\S5D\CTK-build\CTK-build\bin\Release\CTKImageProcessingITKCorePythonQt.pyd<br>
1&gt;    CTKVisualizationVTKCore.vcxproj → F:\D\S5D\CTK-build\CTK-build\bin\Release\CTKVisualizationVTKCore.dll<br>
1&gt;    CTKVisualizationVTKWidgets.vcxproj → F:\D\S5D\CTK-build\CTK-build\bin\Release\CTKVisualizationVTKWidgets.dll<br>
1&gt;    CTKQtTesting.vcxproj → F:\D\S5D\CTK-build\CTK-build\bin\Release\CTKQtTesting.dll<br>
1&gt;    CTKQtTestingPythonQt.vcxproj → F:\D\S5D\CTK-build\CTK-build\bin\Release\CTKQtTestingPythonQt.pyd<br>
1&gt;    CTKScriptingPythonCore.vcxproj → F:\D\S5D\CTK-build\CTK-build\bin\Release\CTKScriptingPythonCore.dll<br>
1&gt;    CTKScriptingPythonWidgets.vcxproj → F:\D\S5D\CTK-build\CTK-build\bin\Release\CTKScriptingPythonWidgets.dll<br>
1&gt;    CTKScriptingPythonWidgetsPlugins.vcxproj → F:\D\S5D\CTK-build\CTK-build\bin\designer\Release\CTKScriptingPythonWidgetsPlugins.dll<br>
1&gt;    CTKScriptingPythonWidgetsPythonQt.vcxproj → F:\D\S5D\CTK-build\CTK-build\bin\Release\CTKScriptingPythonWidgetsPythonQt.pyd<br>
1&gt;    CTKVisualizationVTKCorePythonQt.vcxproj → F:\D\S5D\CTK-build\CTK-build\bin\Release\CTKVisualizationVTKCorePythonQt.pyd<br>
1&gt;    CTKVisualizationVTKWidgetsPlugins.vcxproj → F:\D\S5D\CTK-build\CTK-build\bin\designer\Release\CTKVisualizationVTKWidgetsPlugins.dll<br>
1&gt;    CTKVisualizationVTKWidgetsPythonQt.vcxproj → F:\D\S5D\CTK-build\CTK-build\bin\Release\CTKVisualizationVTKWidgetsPythonQt.pyd<br>
1&gt;    CTKWidgetsPlugins.vcxproj → F:\D\S5D\CTK-build\CTK-build\bin\designer\Release\CTKWidgetsPlugins.dll<br>
1&gt;    CTKWidgetsPythonQt.vcxproj → F:\D\S5D\CTK-build\CTK-build\bin\Release\CTKWidgetsPythonQt.pyd<br>
1&gt;    ctkDICOM.vcxproj → F:\D\S5D\CTK-build\CTK-build\bin\Release\ctkDICOM.exe<br>
1&gt;  Forcing configure step for ‘CTK’<br>
1&gt;  No install step for ‘CTK’<br>
1&gt;  Completed ‘CTK’<br>
1&gt;C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets(247,5): warning MSB8065: Custom build for item “F:\D\S5D\CTK-build\CMakeFiles\efd08cadf5a1ea590d1828fc661b072b\CTK-configure.rule” succeeded, but specified output “f:\d\s5d\ctk-build\ctk-prefix\src\ctk-stamp\release\ctk-configure” has not been created. This may cause incremental build to work incorrectly. [F:\D\S5D\CTK-build\CTK.vcxproj]<br>
1&gt;C:\Program Files\Microsoft Visual Studio\2022\Community\MSBuild\Microsoft\VC\v170\Microsoft.CppCommon.targets(247,5): warning MSB8064: Custom build for item “F:\D\S5D\CTK-build\CMakeFiles\efd08cadf5a1ea590d1828fc661b072b\CTK-build.rule” succeeded, but specified dependency “f:\d\s5d\ctk-build\ctk-prefix\src\ctk-stamp\release\ctk-configure” does not exist. This may cause incremental build to work incorrectly. [F:\D\S5D\CTK-build\CTK.vcxproj]<br>
1&gt;No install step for ‘CTK’<br>
1&gt;Completed ‘CTK’<br>
1&gt;Done building project “CTK.vcxproj”.</p>
</blockquote>

---

## Post #9 by @cpinter (2022-11-24 11:56 UTC)

<aside class="quote no-group" data-username="Dya" data-post="8" data-topic="26246">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/6bbea6/48.png" class="avatar"> Dya:</div>
<blockquote>
<p>1&gt;Completed ‘CTK’<br>
1&gt;Done building project “CTK.vcxproj”.</p>
</blockquote>
</aside>
<p>This build is successful.</p>

---

## Post #10 by @Dya (2022-11-24 12:01 UTC)

<p>Yes. But there is MSB8065 warning in CTK build, which is eventually making MSB8066 error.</p>

---

## Post #11 by @lassoan (2022-11-25 06:16 UTC)

<p>You were building CTK in release mode in a folder named S5D. Is this a debug or release mode build?</p>

---

## Post #12 by @Dya (2022-11-25 06:33 UTC)

<p>It is a x64 release mode build.</p>

---

## Post #13 by @lassoan (2022-11-25 06:44 UTC)

<p>I don’t see any issue here then. Open the top-level Slicer.sln, build in Release mode, and if any External project fails to build then open the .sln file of that (as you did for CTK). You’ll then be able to find the actual error message. Hopefully from the error message it will be obvious what the problem is and how to fix it.</p>

---

## Post #15 by @Dya (2022-12-02 06:41 UTC)

<p>Hello Lassoan,<br>
Thank you for your help.<br>
I tried to build slicer in a new system and the build has succeeded. The system that I tried to build before has lot of dependencies in system path and I couldn’t remove it till the slicer was building because I need to use them for my other projects also, Anyways, Now if I copy the source and build folder from the succeeded system and copy it in my system , can I able to execute it without any issues?</p>

---

## Post #16 by @lassoan (2022-12-02 15:14 UTC)

<p>Yes, if you build Slicer in Release mode and create a package then it can be used on any computer.</p>

---
