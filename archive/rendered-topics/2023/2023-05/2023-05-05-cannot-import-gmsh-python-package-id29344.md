---
topic_id: 29344
title: "Cannot Import Gmsh Python Package"
date: 2023-05-05
url: https://discourse.slicer.org/t/29344
---

# Cannot import gmsh Python package

**Topic ID**: 29344
**Date**: 2023-05-05
**URL**: https://discourse.slicer.org/t/cannot-import-gmsh-python-package/29344

---

## Post #1 by @Saima (2023-05-05 03:41 UTC)

<p>Hi Andras,<br>
Slicer exit abnormally<br>
when I try to initialize <code>gmsh</code> in an extension but it did work with the built version of slicer but not with the executable version of slicer. could you please help to resolve?</p>
<pre><code class="lang-plaintext">Python console user input: import gmsh
Python console user input: gmsh.initialize()
error: [/media/useradmin/Disk2/Slicer-5.3.0-2023-01-21-linux-amd64/bin/SlicerApp-real] exit abnormally - Report the problem.
</code></pre>
<p>regards,<br>
Saima</p>

---

## Post #2 by @benzwick (2023-05-07 09:03 UTC)

<p>This is happening with the latest (5.2.2) stable version of Slicer as well:</p>
<pre><code class="lang-plaintext">Python console user input: import gmsh
Python console user input: gmsh.initialize()
error: [/opt/slicer/Slicer-5.2.2-linux-amd64/bin/SlicerApp-real] exit abnormally - Report the problem.
</code></pre>

---

## Post #3 by @benzwick (2023-05-11 08:21 UTC)

<p>Here is the output from GDB:</p>
<pre><code class="lang-auto">ben@p1:~$ gdb --pid 618067
GNU gdb (Debian 13.1-2) 13.1
Copyright (C) 2023 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later &lt;http://gnu.org/licenses/gpl.html&gt;
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
&lt;https://www.gnu.org/software/gdb/bugs/&gt;.
Find the GDB manual and other documentation resources online at:
    &lt;http://www.gnu.org/software/gdb/documentation/&gt;.

For help, type "help".
Type "apropos word" to search for commands related to "word".
Attaching to process 618067
[New LWP 618068]
[New LWP 618069]
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
0x00007f6783f1afff in poll () from /lib/x86_64-linux-gnu/libc.so.6
(gdb) continue
Continuing.
[New Thread 0x7f6723bff6c0 (LWP 618123)]
[New Thread 0x7f67233fe6c0 (LWP 618124)]
[New Thread 0x7f66fc5ff6c0 (LWP 618126)]
[New Thread 0x7f66f9dfe6c0 (LWP 618127)]
[New Thread 0x7f66f75fd6c0 (LWP 618128)]
[New Thread 0x7f66f4dfc6c0 (LWP 618129)]
[New Thread 0x7f66f45fb6c0 (LWP 618130)]
[New Thread 0x7f66f1dfa6c0 (LWP 618131)]
[New Thread 0x7f66ef5f96c0 (LWP 618132)]
[New Thread 0x7f66eadf86c0 (LWP 618133)]
[New Thread 0x7f66ea5f76c0 (LWP 618134)]
[New Thread 0x7f66e5df66c0 (LWP 618135)]
[New Thread 0x7f66e55f56c0 (LWP 618136)]
[New Thread 0x7f66dd5ff6c0 (LWP 618137)]
[New Thread 0x7f66dcdfe6c0 (LWP 618138)]
[New Thread 0x7f66d7fff6c0 (LWP 618139)]
[New Thread 0x7f669882b6c0 (LWP 618142)]
[New Thread 0x7f669802a6c0 (LWP 618143)]
[New Thread 0x7f66978296c0 (LWP 618144)]
[New Thread 0x7f66970286c0 (LWP 618145)]
[New Thread 0x7f66968276c0 (LWP 618146)]
[New Thread 0x7f66960266c0 (LWP 618147)]
[New Thread 0x7f66958256c0 (LWP 618148)]
[New Thread 0x7f66950246c0 (LWP 618149)]
[New Thread 0x7f66948236c0 (LWP 618150)]
[New Thread 0x7f666ffff6c0 (LWP 618151)]
[New Thread 0x7f666f7fe6c0 (LWP 618152)]
[New Thread 0x7f666effd6c0 (LWP 618153)]
[New Thread 0x7f664dbff6c0 (LWP 618154)]
[New Thread 0x7f664d3fe6c0 (LWP 618155)]
[Thread 0x7f669802a6c0 (LWP 618143) exited]
[Thread 0x7f66968276c0 (LWP 618146) exited]
[Thread 0x7f669882b6c0 (LWP 618142) exited]
[Thread 0x7f66948236c0 (LWP 618150) exited]
[Thread 0x7f666f7fe6c0 (LWP 618152) exited]
[Thread 0x7f66958256c0 (LWP 618148) exited]
[Thread 0x7f66960266c0 (LWP 618147) exited]
[Thread 0x7f666ffff6c0 (LWP 618151) exited]
[Thread 0x7f66950246c0 (LWP 618149) exited]
[Thread 0x7f66978296c0 (LWP 618144) exited]
[Thread 0x7f666effd6c0 (LWP 618153) exited]
[Thread 0x7f66970286c0 (LWP 618145) exited]
[New Thread 0x7f66970286c0 (LWP 618157)]
[New Thread 0x7f666effd6c0 (LWP 618158)]
[New Thread 0x7f66950246c0 (LWP 618159)]
[New Thread 0x7f66978296c0 (LWP 618160)]
[New Thread 0x7f669882b6c0 (LWP 618161)]
[New Thread 0x7f669802a6c0 (LWP 618162)]
[New Thread 0x7f66968276c0 (LWP 618163)]
[New Thread 0x7f66960266c0 (LWP 618164)]
[New Thread 0x7f66958256c0 (LWP 618165)]
[New Thread 0x7f66948236c0 (LWP 618166)]
[New Thread 0x7f666ffff6c0 (LWP 618167)]

Thread 1 "SlicerApp-real" received signal SIGABRT, Aborted.
0x00007f6783ea9ccc in ?? () from /lib/x86_64-linux-gnu/libc.so.6
(gdb) backtrace
#0  0x00007f6783ea9ccc in ?? () from /lib/x86_64-linux-gnu/libc.so.6
#1  0x00007f6783e5aef2 in raise () from /lib/x86_64-linux-gnu/libc.so.6
#2  0x00007f6783e45472 in abort () from /lib/x86_64-linux-gnu/libc.so.6
#3  0x00007f6783e9e2d0 in ?? () from /lib/x86_64-linux-gnu/libc.so.6
#4  0x00007f6783eb364a in ?? () from /lib/x86_64-linux-gnu/libc.so.6
#5  0x00007f6783eb53d4 in ?? () from /lib/x86_64-linux-gnu/libc.so.6
#6  0x00007f6783eb7d2f in free () from /lib/x86_64-linux-gnu/libc.so.6
#7  0x00007f663791b09f in std::__detail::_Compiler&lt;std::__cxx11::regex_traits&lt;char&gt; &gt;::_Compiler(char const*, char const*, std::locale const&amp;, std::regex_constants::syntax_option_type) ()
   from /opt/slicer/Slicer-5.2.2-linux-amd64/lib/Python/lib/libgmsh.so.4.11
#8  0x00007f663791b158 in std::enable_if&lt;std::__detail::__is_contiguous_normal_iter&lt;char const*&gt;::value, std::shared_ptr&lt;std::__detail::_NFA&lt;std::__cxx11::regex_traits&lt;char&gt; &gt; const&gt; &gt;::type std::__detail::__compile_nfa&lt;char const*, std::__cxx11::regex_traits&lt;char&gt; &gt;(char const*, char const*, std::__cxx11::regex_traits&lt;char&gt;::locale_type const&amp;, std::regex_constants::syntax_option_type) () from /opt/slicer/Slicer-5.2.2-linux-amd64/lib/Python/lib/libgmsh.so.4.11
#9  0x00007f6637909bcb in ?? () from /opt/slicer/Slicer-5.2.2-linux-amd64/lib/Python/lib/libgmsh.so.4.11
#10 0x00007f6637909d53 in ?? () from /opt/slicer/Slicer-5.2.2-linux-amd64/lib/Python/lib/libgmsh.so.4.11
#11 0x00007f66378e1b1e in ?? () from /opt/slicer/Slicer-5.2.2-linux-amd64/lib/Python/lib/libgmsh.so.4.11
#12 0x00007f66378bee91 in ?? () from /opt/slicer/Slicer-5.2.2-linux-amd64/lib/Python/lib/libgmsh.so.4.11
#13 0x00007f66378df65a in ?? () from /opt/slicer/Slicer-5.2.2-linux-amd64/lib/Python/lib/libgmsh.so.4.11
#14 0x00007f663789dcae in ?? () from /opt/slicer/Slicer-5.2.2-linux-amd64/lib/Python/lib/libgmsh.so.4.11
#15 0x00007f6637933205 in gmsh::initialize(int, char**, bool, bool) () from /opt/slicer/Slicer-5.2.2-linux-amd64/lib/Python/lib/libgmsh.so.4.11
#16 0x00007f663857a1d5 in gmshInitialize () from /opt/slicer/Slicer-5.2.2-linux-amd64/lib/Python/lib/libgmsh.so.4.11
#17 0x00007f674a4be052 in ?? () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Python/lib/libpython3.9.so
#18 0x00007f674a4bb64e in ?? () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Python/lib/libpython3.9.so
#19 0x00007f674a4b199d in _ctypes_callproc () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Python/lib/libpython3.9.so
#20 0x00007f674a4aaa76 in ?? () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Python/lib/libpython3.9.so
#21 0x00007f674a297e5a in _PyObject_MakeTpCall () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Python/lib/libpython3.9.so
#22 0x00007f674a2765fb in ?? () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Python/lib/libpython3.9.so
#23 0x00007f674a27d070 in _PyEval_EvalFrameDefault () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Python/lib/libpython3.9.so
#24 0x00007f674a27542b in ?? () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Python/lib/libpython3.9.so
#25 0x00007f674a276597 in ?? () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Python/lib/libpython3.9.so
#26 0x00007f674a27d070 in _PyEval_EvalFrameDefault () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Python/lib/libpython3.9.so
#27 0x00007f674a3c0b37 in _PyEval_EvalCode () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Python/lib/libpython3.9.so
#28 0x00007f674a3c0ed2 in _PyEval_EvalCodeWithName () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Python/lib/libpython3.9.so
#29 0x00007f674a3c0f1e in PyEval_EvalCodeEx () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Python/lib/libpython3.9.so
#30 0x00007f674a3c0f4b in PyEval_EvalCode () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Python/lib/libpython3.9.so
#31 0x00007f674a3bbd41 in ?? () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Python/lib/libpython3.9.so
#32 0x00007f674a302f15 in ?? () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Python/lib/libpython3.9.so
#33 0x00007f674a27c101 in _PyEval_EvalFrameDefault () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Python/lib/libpython3.9.so
#34 0x00007f674a27542b in ?? () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Python/lib/libpython3.9.so
#35 0x00007f674a276597 in ?? () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Python/lib/libpython3.9.so
#36 0x00007f674a277fa2 in _PyEval_EvalFrameDefault () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Python/lib/libpython3.9.so
#37 0x00007f674a3c0b37 in _PyEval_EvalCode () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Python/lib/libpython3.9.so
#38 0x00007f674a297c41 in _PyFunction_Vectorcall () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Python/lib/libpython3.9.so
#39 0x00007f674a276597 in ?? () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Python/lib/libpython3.9.so
#40 0x00007f674a277fa2 in _PyEval_EvalFrameDefault () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Python/lib/libpython3.9.so
#41 0x00007f674a27542b in ?? () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Python/lib/libpython3.9.so
#42 0x00007f674a2b0586 in ?? () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Python/lib/libpython3.9.so
#43 0x00007f674a29a19c in PyObject_CallMethod () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Python/lib/libpython3.9.so
#44 0x00007f6783c083ea in ?? () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Slicer-5.2/libCTKScriptingPythonWidgets.so.0.1
#45 0x00007f6783c08b51 in ctkPythonConsole::executeCommand(QString const&amp;) () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Slicer-5.2/libCTKScriptingPythonWidgets.so.0.1
#46 0x00007f67832cd359 in ctkConsolePrivate::internalExecuteCommand() () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Slicer-5.2/libCTKWidgets.so.0.1
#47 0x00007f67832ce941 in ctkConsolePrivate::keyPressEvent(QKeyEvent*) () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Slicer-5.2/libCTKWidgets.so.0.1
#48 0x00007f67821a20a7 in QWidget::event(QEvent*) () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Slicer-5.2/libQt5Widgets.so.5
#49 0x00007f678224a21e in QFrame::event(QEvent*) () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Slicer-5.2/libQt5Widgets.so.5
#50 0x00007f678224cef3 in QAbstractScrollArea::event(QEvent*) () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Slicer-5.2/libQt5Widgets.so.5
--Type &lt;RET&gt; for more, q to quit, c to continue without paging--c
#51 0x00007f6782318f7a in QTextEdit::event(QEvent*) () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Slicer-5.2/libQt5Widgets.so.5
#52 0x00007f678216343c in QApplicationPrivate::notify_helper(QObject*, QEvent*) () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Slicer-5.2/libQt5Widgets.so.5
#53 0x00007f678216ab55 in QApplication::notify(QObject*, QEvent*) () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Slicer-5.2/libQt5Widgets.so.5
#54 0x00007f6784e8b3b6 in qSlicerApplication::notify(QObject*, QEvent*) () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Slicer-5.2/libqSlicerBaseQTGUI.so
#55 0x00007f678109d808 in QCoreApplication::notifyInternal2(QObject*, QEvent*) () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Slicer-5.2/libQt5Core.so.5
#56 0x00007f67821bdd0b in ?? () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Slicer-5.2/libQt5Widgets.so.5
#57 0x00007f678216343c in QApplicationPrivate::notify_helper(QObject*, QEvent*) () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Slicer-5.2/libQt5Widgets.so.5
#58 0x00007f6782169f20 in QApplication::notify(QObject*, QEvent*) () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Slicer-5.2/libQt5Widgets.so.5
#59 0x00007f6784e8b3b6 in qSlicerApplication::notify(QObject*, QEvent*) () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Slicer-5.2/libqSlicerBaseQTGUI.so
#60 0x00007f678109d808 in QCoreApplication::notifyInternal2(QObject*, QEvent*) () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Slicer-5.2/libQt5Core.so.5
#61 0x00007f678176be1b in QGuiApplicationPrivate::processKeyEvent(QWindowSystemInterfacePrivate::KeyEvent*) () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Slicer-5.2/libQt5Gui.so.5
#62 0x00007f6781770935 in QGuiApplicationPrivate::processWindowSystemEvent(QWindowSystemInterfacePrivate::WindowSystemEvent*) () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Slicer-5.2/libQt5Gui.so.5
#63 0x00007f678174c8ab in QWindowSystemInterface::sendWindowSystemEvents(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Slicer-5.2/libQt5Gui.so.5
#64 0x00007f673466569a in ?? () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Slicer-5.2/libQt5XcbQpa.so.5
#65 0x00007f678571c7a9 in g_main_context_dispatch () from /lib/x86_64-linux-gnu/libglib-2.0.so.0
#66 0x00007f678571ca38 in ?? () from /lib/x86_64-linux-gnu/libglib-2.0.so.0
#67 0x00007f678571cacc in g_main_context_iteration () from /lib/x86_64-linux-gnu/libglib-2.0.so.0
#68 0x00007f67810f91cc in QEventDispatcherGlib::processEvents(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Slicer-5.2/libQt5Core.so.5
#69 0x00007f678109c21a in QEventLoop::exec(QFlags&lt;QEventLoop::ProcessEventsFlag&gt;) () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Slicer-5.2/libQt5Core.so.5
#70 0x00007f67810a51d3 in QCoreApplication::exec() () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Slicer-5.2/libQt5Core.so.5
#71 0x00007f6782a5361a in qSlicerCoreApplication::exec() () from /opt/slicer/Slicer-5.2.2-linux-amd64/bin/../lib/Slicer-5.2/libqSlicerBaseQTCore.so
#72 0x0000000000404a77 in ?? ()
#73 0x00007f6783e4618a in ?? () from /lib/x86_64-linux-gnu/libc.so.6
#74 0x00007f6783e46245 in __libc_start_main () from /lib/x86_64-linux-gnu/libc.so.6
#75 0x0000000000404b6c in ?? ()
(gdb) 
</code></pre>

---

## Post #4 by @lassoan (2023-05-12 04:35 UTC)

<p>Probably something is messed up in what/how C runtime libraries are linked into the gmsh shared library. Gmsh uses non-permissive (GPL) license, so I would not recommend ever using it as a library.</p>
<p>Instead, you can use <a href="https://github.com/wildmeshing/fTetWild">fTetWild</a>. I haven’t used it myself but many people told it worked well for them. If you don’t find a Python distribution for it then you could add it to <a href="https://github.com/lassoan/SlicerSegmentMesher">SegmentMesher extension</a>.</p>

---

## Post #5 by @benzwick (2023-05-12 05:05 UTC)

<p>We have quite a complicated meshing workflow already implemented in Gmsh, and I don’t think it will be feasible to switch to something like fTetWild. Do you have any suggestions on how we could fix the issue with loading Gmsh in Slicer?</p>

---

## Post #6 by @jcfr (2023-05-12 10:03 UTC)

<blockquote>
<p>Do you have any suggestions on how we could fix the issue with loading Gmsh in Slicer?</p>
</blockquote>
<h2><a name="p-94776-analysis-1" class="anchor" href="#p-94776-analysis-1" aria-label="Heading link"></a>Analysis</h2>
<p>The library <code>libgmsh.so.4.11</code> shipped in the gmsh wheel references  <code>std::__cxx11::basic_string</code></p>
<details><summary>See details</summary>
<pre>$ readelf -W -s ~/Downloads/gmsh-4.11.1-py2.py3-none-manylinux1_x86_64/gmsh-4.11.1.data/data/lib/libgmsh.so.4.11 | \
  cut -c60- | c++filt | ack "::basic_string" | head -n1
std::__cxx11::basic_string&lt;char, std::char_traits, std::allocator &gt;::assign(char const*)@GLIBCXX_3.4.21 (5)
<h1><a name="p-94776-cxx11basic_string-2" class="anchor" href="#p-94776-cxx11basic_string-2" aria-label="Heading link"></a>cxx11::basic_string</h1>
<p>$ readelf -W -s ~/Downloads/gmsh-4.11.1-py2.py3-none-manylinux1_x86_64/gmsh-4.11.1.data/data/lib/libgmsh.so.4.11 | <br>
cut -c60- | c++filt | ack “cxx11::basic_string” | wc -l<br>
364</p>
<h1><a name="p-94776-stdbasic_string-3" class="anchor" href="#p-94776-stdbasic_string-3" aria-label="Heading link"></a>std::basic_string</h1>
<p>$ readelf -W -s ~/Downloads/gmsh-4.11.1-py2.py3-none-manylinux1_x86_64/gmsh-4.11.1.data/data/lib/libgmsh.so.4.11 | <br>
cut -c60- | c++filt | ack “std::basic_string” | wc -l<br>
0<br>
</p></pre><p></p>
</details>
<p>whereas the libraries associated with the Slicer release references <code>std::basic_string</code></p>
<details><summary>See details</summary>
<pre>$ readelf -W -s ~/Downloads/Slicer-5.2.2-linux-amd64/lib/Slicer-5.2/libMRMLCore.so | \
  cut -c60- | c++filt | ack "::basic_string" | head -n1
slicer_itk::ProcessObject::RemoveInput(std::basic_string&lt;char, std::char_traits, std::allocator &gt; const&amp;)
<h1><a name="p-94776-cxx11basic_string-4" class="anchor" href="#p-94776-cxx11basic_string-4" aria-label="Heading link"></a>cxx11::basic_string</h1>
<p>$ readelf -W -s ./bin/libMRMLCore.so | <br>
cut -c60- | c++filt | ack “cxx11::basic_string” | wc -l<br>
1310</p>
<h1><a name="p-94776-stdbasic_string-5" class="anchor" href="#p-94776-stdbasic_string-5" aria-label="Heading link"></a>std::basic_string</h1>
<p>$ readelf -W -s ./bin/libMRMLCore.so | <br>
cut -c60- | c++filt | ack “std::basic_string” | wc -l<br>
0<br>
</p></pre><p></p>
</details>
<p>I suspect this is due to incompatibility associated with the <a href="https://gcc.gnu.org/onlinedocs/libstdc++/manual/using_dual_abi.html">Dual ABI</a> introduced in gcc 5<sup class="footnote-ref"><a href="#footnote-94776-1" id="footnote-ref-94776-1">[1]</a></sup><sup class="footnote-ref"><a href="#footnote-94776-2" id="footnote-ref-94776-2">[2]</a></sup>.</p>
<blockquote>
<p>[…] since GCC 5 there are <em>two implementations of <code>std::string</code></em> available in libstdc++. The two implementations are not link-compatible (they have different mangled names, so can’t be linked together) but can co-exist in the same binary (they have different mangled names, so don’t conflict if one object uses <code>std::string</code> and the other uses <code>std::__cxx11::string</code>). If your objects use <code>std::string</code> then usually they should all be compiled with the same string implementation. Compile with <code>-D_GLIBCXX_USE_CXX11_ABI=0</code> to select the original <code>gcc4-compatible</code> implementation, or <code>-D_GLIBCXX_USE_CXX11_ABI=1</code> to select the new <code>cxx11</code> implementation (don’t be fooled by the name, it can be used in C++03 too, it’s called <code>cxx11</code> because it conforms to the C++11 requirements).</p>
</blockquote>
<p><em>Source: <a href="https://stackoverflow.com/questions/46746878/is-it-safe-to-link-c17-c14-and-c11-objects/49119902#49119902">https://stackoverflow.com/questions/46746878/is-it-safe-to-link-c17-c14-and-c11-objects/49119902#49119902</a></em></p>
<h3><a name="p-94776-arent-manylinux1-wheels-suppose-to-use-_glibcxx_use_cxx11_abi0-6" class="anchor" href="#p-94776-arent-manylinux1-wheels-suppose-to-use-_glibcxx_use_cxx11_abi0-6" aria-label="Heading link"></a>Aren’t manylinux1 wheels suppose to use <code>_GLIBCXX_USE_CXX11_ABI=0</code> ?</h3>
<p>Yes, there are suppose to be compatible.</p>
<p>The problem is that the process to generate the <code>gmsh</code> wheels does not seem to be compliant as it is re-packaging its SDK.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a9a582ed3805c61c595f07a42a111b3d2de9130.png" data-download-href="/uploads/short-url/jM8zulPtrhXnNFOdUocrAiusjDO.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a9a582ed3805c61c595f07a42a111b3d2de9130_2_517x150.png" alt="image" data-base62-sha1="jM8zulPtrhXnNFOdUocrAiusjDO" width="517" height="150" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a9a582ed3805c61c595f07a42a111b3d2de9130_2_517x150.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a9a582ed3805c61c595f07a42a111b3d2de9130_2_775x225.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a9a582ed3805c61c595f07a42a111b3d2de9130_2_1034x300.png 2x" data-dominant-color="C7BCC9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2008×586 159 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><em>Source: <a href="https://gitlab.onelab.info/gmsh/gmsh/-/blob/master/.gitlab-ci.yml#L436">https://gitlab.onelab.info/gmsh/gmsh/-/blob/master/.gitlab-ci.yml#L436</a></em></p>
<h3><a name="p-94776-does-this-mean-initializing-the-library-on-slicer-compiled-a-newer-system-compiler-work-7" class="anchor" href="#p-94776-does-this-mean-initializing-the-library-on-slicer-compiled-a-newer-system-compiler-work-7" aria-label="Heading link"></a>Does this mean initializing the library on Slicer compiled a newer system compiler work ?</h3>
<p>Yes, assuming this is the only issue, this should indeed work.</p>
<details><summary>See details</summary>
<pre></pre>
</details>
<p>That said, attempting to initialize the library still lead to a segfault.</p>
<p>There are likely additional symbol clashes to be investigated.</p>
<h2><a name="p-94776-path-forward-8" class="anchor" href="#p-94776-path-forward-8" aria-label="Heading link"></a>Path forward</h2>
<p>As mentioned by <a class="mention" href="/u/lassoan">@lassoan</a> , considering that the library is distributed under the term of a copyleft (non-permissive) license<sup class="footnote-ref"><a href="#footnote-94776-1" id="footnote-ref-94776-0">[1:1]</a></sup>, I suggest you consider reaching out to one of the commercial partner listed <a href="https://www.slicer.org/commercial-use.html">here</a>.</p>
<p>The steps would be to revamp the build-system of gmsh to build compliant wheels  (e.g by leveraging <a href="https://scikit-build.org">https://scikit-build.org</a> &amp; relevant manylinux docker image)</p>
<h2><a name="p-94776-h-9" class="anchor" href="#p-94776-h-9" aria-label="Heading link"></a></h2>
<hr class="footnotes-sep">

<ol class="footnotes-list">
<li id="footnote-94776-1" class="footnote-item"><p><a href="https://en.wikipedia.org/wiki/Permissive_software_license" class="inline-onebox">Permissive software license - Wikipedia</a> <a href="#footnote-ref-94776-1" class="footnote-backref">↩︎</a> <a href="#footnote-ref-94776-1" class="footnote-backref">↩︎</a></p>
</li>
<li id="footnote-94776-2" class="footnote-item"><p><a href="https://gcc.gnu.org/onlinedocs/libstdc++/manual/api.html#api.rel_51" class="inline-onebox">API Evolution and Deprecation History</a> <a href="#footnote-ref-94776-2" class="footnote-backref">↩︎</a></p>
</li>
</ol>

---

## Post #7 by @benzwick (2023-05-15 04:41 UTC)

<p>Thanks for the detailed analysis <a class="mention" href="/u/jcfr">@jcfr</a></p>
<p>I’ve contacted the Gmsh developers here: <a href="https://gitlab.onelab.info/gmsh/gmsh/-/issues/2474" rel="noopener nofollow ugc">https://gitlab.onelab.info/gmsh/gmsh/-/issues/2474</a></p>
<p>Are there any plans for Slicer to migrate to the modern C++11 ABI at some point?</p>

---

## Post #8 by @lassoan (2023-05-16 05:05 UTC)

<p>Using manylinux wheels allows to fulfill our goal of making Slicer compatible with computers that are bought in the past 5 years. I don’t think we would compromise on this for an incorrectly packaged GPL/commercial library. Also, based on what Jc described above, flipping the cxx11 abi flag might not solve all problems.</p>
<p>I would recommend to get/build <code>gmsh</code> binary and launch it in Slicer in <a href="https://github.com/Slicer/Slicer/blob/main/Base/Python/slicer/util.py#L3445">the startup environment</a> instead of trying to install it as a Python package in Slicer’s virtual Python environment.</p>
<p>Or - even better in the long term - use open solutions, such as fTetWild or Cleaver.</p>

---

## Post #9 by @benzwick (2023-05-16 06:43 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="29344">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Using manylinux wheels allows to fulfill our goal of making Slicer compatible with computers that are bought in the past 5 years. I don’t think we would compromise on this for an incorrectly packaged GPL/commercial library. Also, based on what Jc described above, flipping the cxx11 abi flag might not solve all problems.</p>
</blockquote>
</aside>
<p>Thanks for the explanation. There’s an interesting discussion on pytorch where they have the opposite problem (trying to link to pytorch Python packages in a project that uses <code>_GLIBCXX_USE_CXX11_ABI=1</code>):</p>
<ul>
<li><a href="https://github.com/pytorch/pytorch/issues/51039" class="inline-onebox" rel="noopener nofollow ugc">Status of pip wheels with _GLIBCXX_USE_CXX11_ABI=1 · Issue #51039 · pytorch/pytorch · GitHub</a></li>
<li><a href="https://github.com/pytorch/pytorch/pull/79409" class="inline-onebox" rel="noopener nofollow ugc">Add new checks in CI system to verify the built linux pip wheel with cpu-cxx11-abi by zhuhong61 · Pull Request #79409 · pytorch/pytorch · GitHub</a></li>
</ul>
<p>I guess there is also the fact that <a href="https://github.com/Slicer/Slicer/pull/6237" rel="noopener nofollow ugc">Slicer requires at least C++17</a>. It seems there isn’t really a clear solution for this at the moment.</p>
<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="29344">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I would recommend to get/build <code>gmsh</code> binary and launch it in Slicer in <a href="https://github.com/Slicer/Slicer/blob/main/Base/Python/slicer/util.py#L3445" rel="noopener nofollow ugc">the startup environment</a> instead of trying to install it as a Python package in Slicer’s virtual Python environment.</p>
</blockquote>
</aside>
<p>This sounds like a good idea, but it will require us to change a lot of the code and won’t allow interactive use of Gmsh within Slicer (although this probably doesn’t matter too much at the moment). I’ll try first to compile Gmsh from source and import the library that way.</p>
<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="29344">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Or - even better in the long term - use open solutions, such as fTetWild or Cleaver.</p>
</blockquote>
</aside>
<p>Unfortunately, all the free options apart from Gmsh that I have seen do not have the features that we need to create body-conforming meshes with multiple parts, but I will keep looking.</p>

---

## Post #10 by @lassoan (2023-05-16 11:25 UTC)

<aside class="quote no-group" data-username="benzwick" data-post="9" data-topic="29344">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/benzwick/48/80521_2.png" class="avatar"> benzwick:</div>
<blockquote>
<p>all the free options apart from Gmsh that I have seen do not have the features that we need to create body-conforming meshes</p>
</blockquote>
</aside>
<p>Just for our information (to know what to keep or eye on), could you tell more about the missing features? Maybe also include 1-2 pictures to illustrate.</p>

---

## Post #11 by @benzwick (2023-05-17 03:33 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="29344">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Just for our information (to know what to keep or eye on), could you tell more about the missing features? Maybe also include 1-2 pictures to illustrate.</p>
</blockquote>
</aside>
<p>The main feature we require is to be able to create meshes from multiple surfaces that conform at the interfaces defined by the surfaces. The volume mesh should use exactly the same triangles as those of the surfaces (although sometimes we remesh the surface to match the element size of the volume elements depending on the application). The surfaces define a change in material or contact between different parts. Here is an example from <a href="https://bioparr.mech.uwa.edu.au" rel="noopener nofollow ugc">BioPARR</a> of an abdominal aortic aneurysm (AAA) with intraluminal thrombus (ILT).</p>
<p>These are the three surfaces (AAA exterior surface in blue, interior surface in yellow and ILT surface in red):</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b5c38c9abc7fb8b6da20ca651120d3e3474fcce0.png" alt="image" data-base62-sha1="pVXnPQXdce8wIVZbabOQsqaLVJK" width="231" height="380"></p>
<p>This is the generated tetrahedral mesh (wall in blue and ILT in red):</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4ef7544305fb86f0ecb2b0ed9c09282173e754c3.jpeg" alt="image" data-base62-sha1="bgz8Rv0yG7yLzs33seJwTRIEZd9" width="512" height="370"></p>
<p>For many applications, we need to use hexahedral meshes with multiple parts and material interfaces, which is more difficult to generate and often requires commercial meshing software such as HyperMesh or Cubit.</p>
<p>The only free option which has tetrahedral and hexahedral meshers that compares to the commercial software that I have found is <a href="https://www.salome-platform.org" rel="noopener nofollow ugc">SALOME</a>. This has more features than Gmsh but is a much bigger software (it actually includes Gmsh as a <a href="https://docs.salome-platform.org/latest/gui/GMSHPLUGIN/gmsh_2d_3d_hypo_page.html" rel="noopener nofollow ugc">plugin</a>). It would be nice to add 3D Slicer as a module within SALOME, similar to what they did with ParaView in their <a href="https://docs.salome-platform.org/latest/dev/PARAVIS" rel="noopener nofollow ugc">PARAVIS</a> module. This would enable a complete numerical simulation framework for medical images in a single application.</p>

---

## Post #12 by @lassoan (2023-05-17 15:00 UTC)

<p>Thanks for the additional information, it is very interesting and useful.</p>
<p>If SALOME’s built-in SMESH meshing tool can do all what you need (without using Gmsh) then it could be a good solution. To get a complete numerical simulation framework for medical images in a single application, SALOME could be used directly via Slicer’s GUI, executing SALOME functions using Python scripting. Or a bridge could be built between Slicer and SALOME to synchronize the scene content between the two applications in real-time (both applications are Python-scriptable, so it would not be hard to implement it at all).</p>

---

## Post #13 by @benzwick (2023-05-19 06:21 UTC)

<p>I now have Gmsh Python working inside 3D Slicer by recompiling Gmsh using the <code>_GLIBCXX_USE_CXX11_ABI=0</code> flag.</p>
<p>Full details can be found here: <a href="https://github.com/SlicerCBM/SlicerCBM/issues/41#issuecomment-1553212336" class="inline-onebox" rel="noopener nofollow ugc">Cannot import gmsh Python package · Issue #41 · SlicerCBM/SlicerCBM · GitHub</a></p>
<p>Is there any way to automate this so that Gmsh (or other similar dependencies) is compiled when a user installs an extension?</p>

---

## Post #14 by @lassoan (2023-05-21 00:17 UTC)

<p>Your can build the extension as part of your extension and bundle it with your extension, as it is done in some other extensions.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> what do you think? Can you suggest extensions that can serve as example?</p>

---
