---
topic_id: 2057
title: "Crash On Exit Not Related To Charts"
date: 2018-02-09
url: https://discourse.slicer.org/t/2057
---

# Crash on exit (not related to charts)

**Topic ID**: 2057
**Date**: 2018-02-09
**URL**: https://discourse.slicer.org/t/crash-on-exit-not-related-to-charts/2057

---

## Post #1 by @cpinter (2018-02-09 16:04 UTC)

<p>Many python tests are failing because there is a crash on exit, most of these not related to the charts-related crash that is being fixed now. Here’s a <a href="http://slicer.cdash.org/viewTest.php?onlyfailed&amp;buildid=1197956">Slicer</a> and a <a href="http://slicer.cdash.org/viewTest.php?onlyfailed&amp;buildid=1198152">SlicerRT</a> dashboard.</p>
<p>I did some debugging with two of the RT tests, and the call stack is the same:</p>
<details>
<summary>
Call stack (Windows)</summary>
<pre><code>python27.dll!00007ffdef0b33cb()	Unknown
python27.dll!00007ffdef0b2bb6()	Unknown
python27.dll!00007ffdef068934()	Unknown
PythonQt.dll!PythonQtShell_QDialog::nativeEvent(const QByteArray &amp; eventType0, void * message1, long * result2) Line 6233	C++
Qt5Widgetsd.dll!QWidgetWindow::nativeEvent(const QByteArray &amp; eventType, void * message, long * result) Line 975	C++
Qt5Guid.dll!QGuiApplicationPrivate::processNativeEvent(QWindow * window, const QByteArray &amp; eventType, void * message, long * result) Line 1726	C++
Qt5Guid.dll!QWindowSystemInterface::handleNativeEvent(QWindow * window, const QByteArray &amp; eventType, void * message, long * result) Line 728	C++
qwindowsd.dll!QWindowsContext::windowsProc(HWND__ * hwnd, unsigned int message, QtWindows::WindowsEventType et, unsigned __int64 wParam, __int64 lParam, __int64 * result, QWindowsWindow * * platformWindowPtr) Line 871	C++
qwindowsd.dll!qWindowsWndProc(HWND__ * hwnd, unsigned int message, unsigned __int64 wParam, __int64 lParam) Line 1298	C++
[External Code]	
qwindowsd.dll!QWindowsWindow::destroyWindow() Line 1117	C++
qwindowsd.dll!QWindowsWindow::~QWindowsWindow() Line 1074	C++
[External Code]	
Qt5Guid.dll!QWindowPrivate::destroy() Line 1832	C++
Qt5Guid.dll!QWindow::destroy() Line 1787	C++
Qt5Widgetsd.dll!QWidgetPrivate::deleteTLSysExtra() Line 1917	C++
Qt5Widgetsd.dll!QWidget::destroy(bool destroyWindow, bool destroySubWindows) Line 12390	C++
Qt5Widgetsd.dll!QApplication::~QApplication() Line 820	C++
qSlicerBaseQTCore.dll!qSlicerCoreApplication::~qSlicerCoreApplication() Line 660	C++
qSlicerBaseQTGUI.dll!qSlicerApplication::~qSlicerApplication() Line 375	C++
SlicerApp-real.exe!`anonymous namespace'::SlicerAppMain(int argc, char * * argv) Line 268	C++
SlicerApp-real.exe!main(int argc, char * * argv) Line 303	C++
</code></pre>
</details>
<p>It seems to be related to processing events when destroying a window. Could it be related to --no-main-window? Any other ideas? Thanks!</p>

---

## Post #2 by @lassoan (2018-02-09 16:48 UTC)

<p>Do any of the test failures in the Slicer core look similar to the test failures that you experience in SlicerRT?</p>
<p>Currently these tests fail in the Slicer core:</p>
<ul>
<li>qMRMLLayoutManagerVisibilityTest (Failed)</li>
<li>py_VolumeRenderingThreeDOnlyLayout (Failed)</li>
<li>py_nomainwindow_SlicerOptionDisableSettingsTest (Failed)</li>
<li>py_AtlasTests (Failed)</li>
<li>py_AbdominalAtlasTest (Failed)</li>
<li>py_FiducialLayoutSwitchBug1914 (Failed)</li>
<li>py_SimpleFiltersModuleTest (Failed)</li>
<li>py_LandmarkRegistration (Failed)</li>
</ul>

---

## Post #3 by @cpinter (2018-02-09 18:17 UTC)

<p>I tried two Slicer tests but one passed and the other one crashed Visual Studio too, but now I have to take the computer to the store because of fan issues, so no luck yet. I’ll keep trying at home.</p>

---

## Post #4 by @cpinter (2018-02-15 14:42 UTC)

<p>The dashboard shows passing tests now, so the crash doesn’t seem to happen any more. If it starts again I’ll do more investigation.</p>

---
