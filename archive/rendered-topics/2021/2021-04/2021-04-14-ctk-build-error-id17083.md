# CTK build error

**Topic ID**: 17083
**Date**: 2021-04-14
**URL**: https://discourse.slicer.org/t/ctk-build-error/17083

---

## Post #1 by @1116 (2021-04-14 10:51 UTC)

<p>I’m building 3dSlicer in release version<br>
Due to errors during CTK build, Slicer.exe doesn’t exist.</p>
<p>Is there Any way to suppress those warnings?</p>
<p>those prerequisites were used:<br>
MSVC v142 - VS2019 C++ x64<br>
CMake 3.19.2<br>
Qt5.15.0</p>
<p>1&gt;------ 모두 다시 빌드 시작: 프로젝트: CTK, 구성: Release x64 ------<br>
1&gt;Creating directories for ‘CTK’<br>
1&gt;Performing download step (git clone) for ‘CTK’<br>
1&gt;-- Avoiding repeated git clone, stamp file is up to date: ‘D:/slicer_project/R/CTK-prefix/src/CTK-stamp/CTK-gitclone-lastrun.txt’<br>
1&gt;Performing update step for ‘CTK’<br>
1&gt;Generate version-CTK.txt and license-CTK.txt<br>
1&gt;No patch step for ‘CTK’<br>
1&gt;Performing configure step for ‘CTK’<br>
1&gt;loading initial cache file D:/slicer_project/R/CTK-prefix/tmp/CTK-cache-Release.cmake<br>
1&gt;-- Selecting Windows SDK version 10.0.19041.0 to target Windows 10.0.18363.<br>
1&gt;-- Generated: D:/slicer_project/R/CTK-build/DGraphInput-alldep.txt<br>
1&gt;-- Generated: D:/slicer_project/R/CTK-build/DGraphInput-alldep-withext.txt<br>
1&gt;-- Generated: D:/slicer_project/R/CTK-build/DGraphInput.txt<br>
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
1&gt;-- Build files have been written to: D:/slicer_project/R/CTK-build<br>
1&gt;Performing build step for ‘CTK’<br>
1&gt;.NET Framework용 Microsoft (R) Build Engine 버전 16.9.0+5e4b48a27<br>
1&gt;Copyright (C) Microsoft Corporation. All rights reserved.<br>
1&gt;<br>
1&gt;  Performing update step for ‘PythonQt’<br>
1&gt;  No patch step for ‘PythonQt’<br>
1&gt;  Performing configure step for ‘PythonQt’<br>
1&gt;  loading initial cache file D:/slicer_project/R/CTK-build/PythonQt-cmake/tmp/PythonQt-cache-Release.cmake<br>
1&gt;  – Selecting Windows SDK version 10.0.19041.0 to target Windows 10.0.18363.<br>
1&gt;  – PythonQt: Required Qt components [Core;Widgets;Multimedia;PrintSupport;Network;UiTools]<br>
1&gt;  – Configuring done<br>
1&gt;  – Generating done<br>
1&gt;  – Build files have been written to: D:/slicer_project/R/CTK-build/PythonQt-build<br>
1&gt;  No build step for ‘PythonQt’<br>
1&gt;  Performing install step for ‘PythonQt’<br>
1&gt;  .NET Framework용 Microsoft (R) Build Engine 버전 16.9.0+5e4b48a27<br>
1&gt;  Copyright (C) Microsoft Corporation. All rights reserved.<br>
1&gt;<br>
1&gt;    PythonQt.vcxproj → D:\slicer_project\R\CTK-build\PythonQt-build\Release\PythonQt.dll<br>
1&gt;    – Install configuration: “Release”<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/lib/PythonQt.lib<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/bin/PythonQt.dll<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtBoolResult.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtClassInfo.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtClassWrapper.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtConversion.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtCppWrapperFactory.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtDoc.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQt.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtImporter.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtImportFileInterface.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtInstanceWrapper.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtMethodInfo.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtMisc.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtObjectPtr.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtProperty.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtQFileImporter.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtSignalReceiver.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtSlot.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtSlotDecorator.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtSignal.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtStdDecorators.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtStdIn.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtStdOut.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtSystem.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtThreadSupport.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtUtils.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtVariants.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQtPythonInclude.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/PythonQt/PythonQt_QtBindings.h<br>
1&gt;  Completed ‘PythonQt’<br>
1&gt;  Performing update step for ‘QtTesting’<br>
1&gt;  No patch step for ‘QtTesting’<br>
1&gt;  Performing configure step for ‘QtTesting’<br>
1&gt;  loading initial cache file D:/slicer_project/R/CTK-build/QtTesting-cmake/tmp/QtTesting-cache-Release.cmake<br>
1&gt;  – Selecting Windows SDK version 10.0.19041.0 to target Windows 10.0.18363.<br>
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
1&gt;  – Build files have been written to: D:/slicer_project/R/CTK-build/QtTesting-build<br>
1&gt;  Performing build step for ‘QtTesting’<br>
1&gt;  .NET Framework용 Microsoft (R) Build Engine 버전 16.9.0+5e4b48a27<br>
1&gt;  Copyright (C) Microsoft Corporation. All rights reserved.<br>
1&gt;<br>
1&gt;    QtTesting.vcxproj → D:\slicer_project\R\CTK-build\QtTesting-build\Release\QtTesting.dll<br>
1&gt;  Performing install step for ‘QtTesting’<br>
1&gt;  .NET Framework용 Microsoft (R) Build Engine 버전 16.9.0+5e4b48a27<br>
1&gt;  Copyright (C) Microsoft Corporation. All rights reserved.<br>
1&gt;<br>
1&gt;    QtTesting.vcxproj → D:\slicer_project\R\CTK-build\QtTesting-build\Release\QtTesting.dll<br>
1&gt;    – Install configuration: “Release”<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/lib/QtTesting.lib<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/bin/QtTesting.dll<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/QtTestingExport.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pq3DViewEventPlayer.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pq3DViewEventTranslator.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqAbstractActivateEventPlayer.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqAbstractBooleanEventPlayer.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqAbstractButtonEventTranslator.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqAbstractDoubleEventPlayer.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqAbstractIntEventPlayer.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqAbstractItemViewEventPlayer.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqAbstractItemViewEventPlayerBase.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqAbstractItemViewEventTranslator.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqAbstractItemViewEventTranslatorBase.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqAbstractMiscellaneousEventPlayer.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqAbstractSliderEventTranslator.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqAbstractStringEventPlayer.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqBasicWidgetEventPlayer.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqBasicWidgetEventTranslator.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqCheckEventOverlay.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqComboBoxEventTranslator.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqComboBoxEventPlayer.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqCommentEventPlayer.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqDoubleSpinBoxEventTranslator.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqEventComment.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqEventDispatcher.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqEventObserver.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqEventPlayer.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqEventRecorder.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqEventSource.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqEventTranslator.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqEventTypes.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqLineEditEventTranslator.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqListViewEventPlayer.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqListViewEventTranslator.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqMenuEventTranslator.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqNativeFileDialogEventPlayer.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqNativeFileDialogEventTranslator.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqObjectNaming.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqPlayBackEventsDialog.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqRecordEventsDialog.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqSpinBoxEventTranslator.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqStdoutEventObserver.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqTabBarEventPlayer.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqTabBarEventTranslator.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqTableViewEventPlayer.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqTableViewEventTranslator.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqTestUtility.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqThreadedEventSource.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqTimer.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqTreeViewEventPlayer.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqTreeViewEventTranslator.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqWidgetEventPlayer.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/pqWidgetEventTranslator.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/include/QtTesting/QtTestingConfigure.h<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/lib/cmake/qttesting/QtTestingConfig.cmake<br>
1&gt;    – Up-to-date: D:/slicer_project/R/CTK-build/CMakeExternals/Install/lib/cmake/qttesting/QtTestingTargets.cmake<br>
1&gt;    – Installing: D:/slicer_project/R/CTK-build/CMakeExternals/Install/lib/cmake/qttesting/QtTestingTargets-release.cmake<br>
1&gt;  Completed ‘QtTesting’<br>
1&gt;  Performing configure step for ‘CTK’<br>
1&gt;  loading initial cache file D:/slicer_project/R/CTK-build/CTK-prefix/tmp/CTK-cache-Release.cmake<br>
1&gt;  – Selecting Windows SDK version 10.0.19041.0 to target Windows 10.0.18363.<br>
1&gt;  – Generated: D:/slicer_project/R/CTK-build/CTK-build/DGraphInput-alldep.txt<br>
1&gt;  – Generated: D:/slicer_project/R/CTK-build/CTK-build/DGraphInput-alldep-withext.txt<br>
1&gt;  – Generated: D:/slicer_project/R/CTK-build/CTK-build/DGraphInput.txt<br>
1&gt;  – SuperBuild - First pass<br>
1&gt;  – SuperBuild - First pass - done<br>
1&gt;  – Trying to find DCMTK expecting DCMTKConfig.cmake<br>
1&gt;  – Trying to find DCMTK expecting DCMTKConfig.cmake - ok<br>
1&gt;  – [ITK] Skipping nonexistent library directory or not set variable [ITK_LIBRARY_DIRS]<br>
1&gt;  – [VTK] Skipping nonexistent library directory or not set variable [VTK_LIBRARY_DIRS]<br>
1&gt;  – CTKCore: BFD support disabled<br>
1&gt;  – Looking for decorator header ctkCorePythonQtDecorators.h<br>
1&gt;  – Looking for decorator header ctkCorePythonQtDecorators.h - Found<br>
1&gt;  CMake Warning (dev) at D:/KHK/LIBRARY/Qt5/5.15.0/msvc2019_64/lib/cmake/Qt5Core/Qt5CoreMacros.cmake:44 (message):<br>
1&gt;    qt5_get_moc_flags is not part of the official API, and might be removed in<br>
1&gt;    Qt 6.<br>
1&gt;  Call Stack (most recent call first):<br>
1&gt;    D:/KHK/LIBRARY/Qt5/5.15.0/msvc2019_64/lib/cmake/Qt5Core/Qt5CoreMacros.cmake:86 (_qt5_warn_deprecated)<br>
1&gt;    CMake/ctkMacroGenerateMocs.cmake:8 (QT5_GET_MOC_FLAGS)<br>
1&gt;    CMake/ctkMacroBuildLib.cmake:131 (QT4_GENERATE_MOCS)<br>
1&gt;    Libs/Widgets/CMakeLists.txt:448 (ctkMacroBuildLib)<br>
1&gt;  This warning is for project developers.  Use -Wno-dev to suppress it.<br>
1&gt;<br>
1&gt;  CMake Warning (dev) at D:/KHK/LIBRARY/Qt5/5.15.0/msvc2019_64/lib/cmake/Qt5Core/Qt5CoreMacros.cmake:44 (message):<br>
1&gt;    qt5_create_moc_command is not part of the official API, and might be<br>
1&gt;    removed in Qt 6.<br>
1&gt;  Call Stack (most recent call first):<br>
1&gt;    D:/KHK/LIBRARY/Qt5/5.15.0/msvc2019_64/lib/cmake/Qt5Core/Qt5CoreMacros.cmake:120 (_qt5_warn_deprecated)<br>
1&gt;    CMake/ctkMacroGenerateMocs.cmake:32 (QT5_CREATE_MOC_COMMAND)<br>
1&gt;    CMake/ctkMacroBuildLib.cmake:131 (QT4_GENERATE_MOCS)<br>
1&gt;    Libs/Widgets/CMakeLists.txt:448 (ctkMacroBuildLib)<br>
1&gt;  This warning is for project developers.  Use -Wno-dev to suppress it.<br>
1&gt;<br>
1&gt;  CMake Warning (dev) at D:/KHK/LIBRARY/Qt5/5.15.0/msvc2019_64/lib/cmake/Qt5Core/Qt5CoreMacros.cmake:44 (message):<br>
1&gt;    qt5_create_moc_command is not part of the official API, and might be<br>
1&gt;    removed in Qt 6.<br>
1&gt;  Call Stack (most recent call first):<br>
1&gt;    D:/KHK/LIBRARY/Qt5/5.15.0/msvc2019_64/lib/cmake/Qt5Core/Qt5CoreMacros.cmake:120 (_qt5_warn_deprecated)<br>
1&gt;    CMake/ctkMacroGenerateMocs.cmake:32 (QT5_CREATE_MOC_COMMAND)<br>
1&gt;    CMake/ctkMacroBuildLib.cmake:131 (QT4_GENERATE_MOCS)<br>
1&gt;    Libs/Widgets/CMakeLists.txt:448 (ctkMacroBuildLib)<br>
1&gt;  This warning is for project developers.  Use -Wno-dev to suppress it.<br>
1&gt;<br>
1&gt;  – Looking for decorator header ctkWidgetsPythonQtDecorators.h<br>
1&gt;  – Looking for decorator header ctkWidgetsPythonQtDecorators.h - Found<br>
1&gt;  – Looking for decorator header ctkDICOMCorePythonQtDecorators.h<br>
1&gt;  – Looking for decorator header ctkDICOMCorePythonQtDecorators.h - Found<br>
1&gt;  – Looking for decorator header ctkDICOMWidgetsPythonQtDecorators.h<br>
1&gt;  – Looking for decorator header ctkDICOMWidgetsPythonQtDecorators.h - Found<br>
1&gt;  – Looking for decorator header ctkImageProcessingITKCorePythonQtDecorators.h<br>
1&gt;  – Looking for decorator header ctkImageProcessingITKCorePythonQtDecorators.h - Not found<br>
1&gt;  – Looking for decorator header ctkScriptingPythonWidgetsPythonQtDecorators.h<br>
1&gt;  – Looking for decorator header ctkScriptingPythonWidgetsPythonQtDecorators.h - Not found<br>
1&gt;  – Looking for decorator header ctkVisualizationVTKCorePythonQtDecorators.h<br>
1&gt;  – Looking for decorator header ctkVisualizationVTKCorePythonQtDecorators.h - Not found<br>
1&gt;  – Checking if QVTKOpenGLNativeWidget.h exists<br>
1&gt;  – Checking if QVTKOpenGLNativeWidget.h exists - found<br>
1&gt;  – Looking for decorator header ctkVisualizationVTKWidgetsPythonQtDecorators.h<br>
1&gt;  – Looking for decorator header ctkVisualizationVTKWidgetsPythonQtDecorators.h - Found<br>
1&gt;  – Looking for decorator header ctkQtTestingPythonQtDecorators.h<br>
1&gt;  – Looking for decorator header ctkQtTestingPythonQtDecorators.h - Not found<br>
1&gt;  – Including CMake built-in module CMakePackageConfigHelpers<br>
1&gt;  – Including CMake built-in module CMakePackageConfigHelpers - ok<br>
1&gt;  – Configuring done<br>
1&gt;  – Generating done<br>
1&gt;  – Build files have been written to: D:/slicer_project/R/CTK-build/CTK-build<br>
1&gt;  Performing build step for ‘CTK’<br>
1&gt;  .NET Framework용 Microsoft (R) Build Engine 버전 16.9.0+5e4b48a27<br>
1&gt;  Copyright (C) Microsoft Corporation. All rights reserved.<br>
1&gt;<br>
1&gt;    CTKCore.vcxproj → D:\slicer_project\R\CTK-build\CTK-build\bin\Release\CTKCore.dll<br>
1&gt;    CTKCorePythonQt.vcxproj → D:\slicer_project\R\CTK-build\CTK-build\bin\Release\CTKCorePythonQt.pyd<br>
1&gt;    CTKDICOMCore.vcxproj → D:\slicer_project\R\CTK-build\CTK-build\bin\Release\CTKDICOMCore.dll<br>
1&gt;    CTKDICOMCorePythonQt.vcxproj → D:\slicer_project\R\CTK-build\CTK-build\bin\Release\CTKDICOMCorePythonQt.pyd<br>
1&gt;    CTKWidgets.vcxproj → D:\slicer_project\R\CTK-build\CTK-build\bin\Release\CTKWidgets.dll<br>
1&gt;    CTKDICOMWidgets.vcxproj → D:\slicer_project\R\CTK-build\CTK-build\bin\Release\CTKDICOMWidgets.dll<br>
1&gt;    CTKDICOMWidgetsPlugins.vcxproj → D:\slicer_project\R\CTK-build\CTK-build\bin\designer\Release\CTKDICOMWidgetsPlugins.dll<br>
1&gt;    CTKDICOMWidgetsPythonQt.vcxproj → D:\slicer_project\R\CTK-build\CTK-build\bin\Release\CTKDICOMWidgetsPythonQt.pyd<br>
1&gt;    CTKImageProcessingITKCore.vcxproj → D:\slicer_project\R\CTK-build\CTK-build\bin\Release\CTKImageProcessingITKCore.dll<br>
1&gt;    CTKImageProcessingITKCorePythonQt.vcxproj → D:\slicer_project\R\CTK-build\CTK-build\bin\Release\CTKImageProcessingITKCorePythonQt.pyd<br>
1&gt;    CTKVisualizationVTKCore.vcxproj → D:\slicer_project\R\CTK-build\CTK-build\bin\Release\CTKVisualizationVTKCore.dll<br>
1&gt;    CTKVisualizationVTKWidgets.vcxproj → D:\slicer_project\R\CTK-build\CTK-build\bin\Release\CTKVisualizationVTKWidgets.dll<br>
1&gt;    CTKQtTesting.vcxproj → D:\slicer_project\R\CTK-build\CTK-build\bin\Release\CTKQtTesting.dll<br>
1&gt;    CTKQtTestingPythonQt.vcxproj → D:\slicer_project\R\CTK-build\CTK-build\bin\Release\CTKQtTestingPythonQt.pyd<br>
1&gt;    CTKScriptingPythonCore.vcxproj → D:\slicer_project\R\CTK-build\CTK-build\bin\Release\CTKScriptingPythonCore.dll<br>
1&gt;    CTKScriptingPythonWidgets.vcxproj → D:\slicer_project\R\CTK-build\CTK-build\bin\Release\CTKScriptingPythonWidgets.dll<br>
1&gt;    CTKScriptingPythonWidgetsPlugins.vcxproj → D:\slicer_project\R\CTK-build\CTK-build\bin\designer\Release\CTKScriptingPythonWidgetsPlugins.dll<br>
1&gt;    CTKScriptingPythonWidgetsPythonQt.vcxproj → D:\slicer_project\R\CTK-build\CTK-build\bin\Release\CTKScriptingPythonWidgetsPythonQt.pyd<br>
1&gt;    CTKVisualizationVTKCorePythonQt.vcxproj → D:\slicer_project\R\CTK-build\CTK-build\bin\Release\CTKVisualizationVTKCorePythonQt.pyd<br>
1&gt;    CTKVisualizationVTKWidgetsPlugins.vcxproj → D:\slicer_project\R\CTK-build\CTK-build\bin\designer\Release\CTKVisualizationVTKWidgetsPlugins.dll<br>
1&gt;    CTKVisualizationVTKWidgetsPythonQt.vcxproj → D:\slicer_project\R\CTK-build\CTK-build\bin\Release\CTKVisualizationVTKWidgetsPythonQt.pyd<br>
1&gt;    CTKWidgetsPlugins.vcxproj → D:\slicer_project\R\CTK-build\CTK-build\bin\designer\Release\CTKWidgetsPlugins.dll<br>
1&gt;    CTKWidgetsPythonQt.vcxproj → D:\slicer_project\R\CTK-build\CTK-build\bin\Release\CTKWidgetsPythonQt.pyd<br>
1&gt;    ctkDICOM.vcxproj → D:\slicer_project\R\CTK-build\CTK-build\bin\Release\ctkDICOM.exe<br>
1&gt;  No install step for ‘CTK’<br>
1&gt;  Forcing configure step for ‘CTK’<br>
1&gt;  Completed ‘CTK’<br>
1&gt;C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(240,5): warning MSB8065: “D:\slicer_project\R\CTK-build\CMakeFiles\437b916531525ad80f8a6f393a84c741\CTK-configure.rule” 항목에 대한 사용자 지정 빌드에 성공했지만 지정한 출력 "d:\slicer_project\r\ctk-build\ctk-prefix\src\ctk-stamp\release\ctk-configure"이(가) 생성되지 않았습니다. 이 오류로 인해 증분 빌드가 제대로 작동하지 않을 수 있습니다. [D:\slicer_project\R\CTK-build\CTK.vcxproj]<br>
1&gt;C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(240,5): warning MSB8064: “D:\slicer_project\R\CTK-build\CMakeFiles\437b916531525ad80f8a6f393a84c741\CTK-build.rule” 항목에 대한 사용자 지정 빌드에 성공했지만 지정한 종속성 "d:\slicer_project\r\ctk-build\ctk-prefix\src\ctk-stamp\release\ctk-configure"이(가) 없습니다. 이 오류로 인해 증분 빌드가 제대로 작동하지 않을 수 있습니다. [D:\slicer_project\R\CTK-build\CTK.vcxproj]<br>
1&gt;No install step for ‘CTK’<br>
1&gt;Completed ‘CTK’<br>
1&gt;Building Custom Rule D:/slicer_project/Slicer/CMakeLists.txt<br>
1&gt;“CTK.vcxproj” 프로젝트를 빌드했습니다.<br>
========== 모두 다시 빌드: 성공 1, 실패 0, 생략 0 ==========</p>

---
