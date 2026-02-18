# Crash on startup

**Topic ID**: 12835
**Date**: 2020-08-03
**URL**: https://discourse.slicer.org/t/crash-on-startup/12835

---

## Post #1 by @gcsharp (2020-08-03 16:24 UTC)

<p>This is on linux. gcc 8.3.0, Qt 5.11.3.  I have to build with Slicer_USE_PYTHONQT_WITH_OPENSSL disabled, but all other options as default.  Any ideas?</p>
<pre><code>Thread 1 "SlicerApp-real" received signal SIGSEGV, Segmentation fault.
0x00007fffe31644ac in ?? () from /usr/lib/x86_64-linux-gnu/libQt5Widgets.so.5
(gdb) bt
#0  0x00007fffe31644ac in  () at /usr/lib/x86_64-linux-gnu/libQt5Widgets.so.5
#1  0x00007fffe3165300 in QDialogButtonBox::setStandardButtons(QFlags&lt;QDialogButtonBox::StandardButton&gt;) () at /usr/lib/x86_64-linux-gnu/libQt5Widgets.so.5
#2  0x00007ffff72f5699 in Ui_ctkSettingsDialog::setupUi(QDialog*)
    (this=0x5555563e40e0, ctkSettingsDialog=0x555556f09a40)
    at /PHShome/gcs6/build/slicer-4/Slicer-debug/CTK-build/CTK-build/Libs/Widgets/ui_ctkSettingsDialog.h:57
#3  0x00007ffff72f26d5 in ctkSettingsDialogPrivate::init()
    (this=0x5555563e40e0)
    at /PHShome/gcs6/build/slicer-4/Slicer-debug/CTK/Libs/Widgets/ctkSettingsDialog.cpp:75
#4  0x00007ffff72f3446 in ctkSettingsDialog::ctkSettingsDialog(QWidget*)
    (this=0x555556f09a40, _parent=0x0)
    at /PHShome/gcs6/build/slicer-4/Slicer-debug/CTK/Libs/Widgets/ctkSettingsDialog.cpp:187
#5  0x00007ffff7ad23bd in qSlicerApplicationPrivate::init() (this=
    0x555555aa20e0)
    at /PHShome/gcs6/build/slicer-4/Slicer/Base/QTGUI/qSlicerApplication.cxx:252
#6  0x00007ffff7ad307f in qSlicerApplication::qSlicerApplication(int&amp;, char**)
    (this=0x7fffffffda20, _argc=@0x7fffffffd9cc: 1, _argv=0x7fffffffdb88)
    at /PHShome/gcs6/build/slicer-4/Slicer/Base/QTGUI/qSlicerApplication.cxx:358
#7  0x000055555555c9a9 in (anonymous namespace)::SlicerAppMain(int, char**)
    (argc=1, argv=0x7fffffffdb88)
    at /PHShome/gcs6/build/slicer-4/Slicer/Applications/SlicerApp/Main.cxx:40
#8  0x000055555555ccbb in main(int, char**) (argc=1, argv=0x7fffffffdb88)
    at /PHShome/gcs6/build/slicer-4/Slicer/Base/QTApp/qSlicerApplicationMainWrapper.cxx:56</code></pre>

---
