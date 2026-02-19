---
topic_id: 5627
title: "Building Slicer On A Freshly Installed Ubuntu 18 04"
date: 2019-02-03
url: https://discourse.slicer.org/t/5627
---

# Building Slicer on a freshly installed Ubuntu 18.04

**Topic ID**: 5627
**Date**: 2019-02-03
**URL**: https://discourse.slicer.org/t/building-slicer-on-a-freshly-installed-ubuntu-18-04/5627

---

## Post #1 by @Satya_Arjunan (2019-02-03 05:18 UTC)

<p>Hi all,</p>
<p>I am trying to build the most recent Slicer from github on a freshly installed Ubuntu 18.04 and I am getting the following error:<br>
error: [/home/satya/wrk/Slicer/build/Slicer-build/bin/./SlicerApp-real] exit abnormally - Report the problem.</p>
<p>To debug with gdb, I used an exec-wrapper but I got the following error:<br>
(gdb) set exec-wrapper ./WrapSlicer4<br>
(gdb) exec-file ./bin/SlicerApp-real<br>
(gdb) run<br>
Starting program: /home/satya/wrk/Slicer/build/Slicer-build/bin/SlicerApp-real<br>
[Thread debugging using libthread_db enabled]<br>
Using host libthread_db library “/lib/x86_64-linux-gnu/libthread_db.so.1”.<br>
[New Thread 0x7fffad95e700 (LWP 3618)]<br>
[New Thread 0x7fffa4fc4700 (LWP 3619)]<br>
[New Thread 0x7fff9ffff700 (LWP 3620)]<br>
[New Thread 0x7fff9c87a700 (LWP 3621)]<br>
[New Thread 0x7fff97d5c700 (LWP 3622)]</p>
<p>Thread 1 “SlicerApp-real” received signal SIGSEGV, Segmentation fault.<br>
__strcmp_ssse3 () at …/sysdeps/x86_64/multiarch/…/strcmp.S:173<br>
173	…/sysdeps/x86_64/multiarch/…/strcmp.S: No such file or directory.<br>
(gdb)<br>
[3]+  Stopped                 gdb</p>
<p>Here are the steps I followed to build Slicer:<br>
sudo apt install qtcreator qtdeclarative5-dev qtmultimedia5-dev qtbase5-private-dev libqt5xmlpatterns5-dev libqt5svg5-dev libqt5webenginewidgets5 qtwebengine5-dev qtscript5-dev qttools5-dev libxt-dev libqt5x11extras5-dev<br>
sudo apt install git cmake<br>
git clone --recursive <a href="https://github.com/Slicer/Slicer.git" rel="nofollow noopener">https://github.com/Slicer/Slicer.git</a><br>
cd Slicer<br>
mkdir build<br>
cd build<br>
cmake -DQt5_DIR=/usr/lib/qt5 -DCMAKE_BUILD_TYPE:STRING=Debug -DSlicer_USE_PYTHONQT_WITH_TCL:BOOL=OFF -DSlicer_USE_SimpleITK:BOOL=OFF -DSlicer_USE_QtTesting:BOOL=OFF -DSlicer_BUILD_DataStore:BOOL=OFF -DSlicer_USE_SYSTEM_QT:BOOL=1 …/<br>
make</p>
<p>During make, I got some errors in LibArchive and fixed them with the instructions provided here: <a href="https://github.com/libarchive/libarchive/commit/4925fd0ba817764f30b3d6837820351c3bd556d4" rel="nofollow noopener">https://github.com/libarchive/libarchive/commit/4925fd0ba817764f30b3d6837820351c3bd556d4</a></p>
<p>The contents of WrapSlicer4:<br>
#!/bin/bash<br>
BASE_DIR=/home/satya/wrk/Slicer/build<br>
APPLAUNCHER_DIR=$BASE_DIR/Slicer-build</p>
<p>LD_PATHS="<br>
$BASE_DIR/VTK-build/bin/<br>
$BASE_DIR/CTK-build/CTK-build/bin/<br>
/usr/lib<br>
$BASE_DIR/ITK-build/bin/<br>
$BASE_DIR/SlicerExecutionModel-build/ModuleDescriptionParser/bin/<br>
$BASE_DIR/teem-build/bin/<br>
$BASE_DIR/LibArchive-install/lib<br>
$APPLAUNCHER_DIR/bin/<br>
$APPLAUNCHER_DIR/lib/Slicer-4.11/qt-loadable-modules<br>
$APPLAUNCHER_DIR/lib/Slicer-4.11/cli-modules/<br>
$APPLAUNCHER_DIR/lib/Slicer-4.11/qt-loadable-modules/<br>
$BASE_DIR/tcl-build/lib<br>
$BASE_DIR/OpenIGTLink-build<br>
$BASE_DIR/OpenIGTLink-build/bin/<br>
$BASE_DIR/CTK-build/PythonQt-build/<br>
$BASE_DIR/python-build/lib<br>
$BASE_DIR/python-build/lib/python2.7/site-packages/numpy/core<br>
$BASE_DIR/python-build/lib/python2.7/site-packages/numpy/lib<br>
"<br>
for STR in <span class="math">LD_PATHS; do LD_LIBRARY_PATH="</span>{STR}:${LD_LIBRARY_PATH}"; done<br>
echo $LD_LIBRARY_PATH</p>
<p>QT_PLUGIN_PATH=$APPLAUNCHER_DIR/bin:$BASE_DIR/CTK-build/CTK-build/bin:/usr/lib/qt4/plugins<br>
SLICER_HOME=$BASE_DIR/Slicer-build<br>
PYTHONHOME=$BASE_DIR/python-build<br>
PYTHONPATH=$APPLAUNCHER_DIR:/bin:$APPLAUNCHER_DIR:/bin/Python:$BASE_DIR/python-build/lib/python2.7/site-packages:$APPLAUNCHER_DIR/lib/Slicer-4.0/qt-loadable-modules/.:$APPLAUNCHER_DIR/lib/Slicer-4.0/qt-loadable-modules/Python<br>
TCL_LIBRARY=$BASE_DIR/tcl-build/lib/tcl8.4<br>
TK_LIBRARY=$BASE_DIR/tcl-build/lib/tk8.4<br>
TCLLIBPATH=$BASE_DIR/tcl-build/lib/itcl3.2:$BASE_DIR/tcl-build/lib/itk3.2</p>
<p>export QTPLUGIN_PATH=$QT_PLUGIN_PATH<br>
export SLICER_HOME=$SLICER_HOME<br>
export PYTHONHOME=$PYTHONHOME<br>
export PYTHONPATH=$PYTHONPATH<br>
export TCL_LIBRARY=$TCL_LIBRARY<br>
export TK_LIBRARY=$TK_LIBRARY<br>
export TCLLIBPATH=$TCLLIBPATH<br>
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH</p>
<p>exec “$@”</p>
<p>What should I do next? Thank you!</p>
<p>Satya</p>

---

## Post #2 by @pieper (2019-02-03 08:12 UTC)

<p>You shouldn’t need this <code>WrapSlicer4</code> script.  Did you try starting with just the Slicer launcher in the Slicer-build directory?</p>

---

## Post #3 by @Satya_Arjunan (2019-02-03 09:39 UTC)

<p>Thanks Steve. When I run ./Slicer in the Slicer-build directory I get:<br>
error: [/home/satya/wrk/Slicer/build/Slicer-build/bin/./SlicerApp-real] exit abnormally - Report the problem.</p>
<p>When I run ./SlicerApp-real in the Slicer-build/bin directory I get:<br>
Segmentation fault (core dumped)</p>
<p>BTW, if it helps, I was able to install and run SlicerSALT git on the same system without any problem with the following steps:<br>
sudo apt remove cmake<br>
sudo pip install --upgrade cmake (to install cmake version &gt;= 3.11)<br>
in ~/.bashrc<br>
export PATH=/usr/local/bin:$PATH<br>
sudo apt install gfortran libqtwebkit-dev qt4-default<br>
git clone <a href="mailto:git@github.com">git@github.com</a>:Kitware/slicerSALT.git<br>
cd slicerSALT<br>
mkdir build<br>
cd build<br>
cmake …/<br>
make -j2<br>
./Slicer-build/SlicerSALT</p>

---

## Post #4 by @Satya_Arjunan (2019-02-03 09:46 UTC)

<p>When I run Slicer with gdb in the Slicer-build directory this is what I get:<br>
(gdb) exec-file Slicer<br>
(gdb) run<br>
Starting program: /home/satya/wrk/Slicer/build/Slicer-build/Slicer<br>
[Thread debugging using libthread_db enabled]<br>
Using host libthread_db library “/lib/x86_64-linux-gnu/libthread_db.so.1”.<br>
[New Thread 0x7ffff34af700 (LWP 24211)]<br>
error: [/home/satya/wrk/Slicer/build/Slicer-build/bin/./SlicerApp-real] exit abnormally - Report the problem.<br>
[Thread 0x7ffff34af700 (LWP 24211) exited]<br>
[Inferior 1 (process 24207) exited with code 01]</p>

---

## Post #5 by @pieper (2019-02-05 14:44 UTC)

<p>Hmm, not sure what that is.  About the best I can think is to start with a fresh virtual machine and then write a script that exactly replicates the build steps that lead to this.</p>
<p>Anyone on discourse have a better idea?</p>

---

## Post #6 by @Satya_Arjunan (2019-02-10 10:02 UTC)

<p>What is the best way to debug? GDB output does not give any useful information.</p>

---

## Post #7 by @lassoan (2019-02-10 14:43 UTC)

<p>Build Slicer Debug or RelWithDebInfo mode to have debug symbols (see variable and method names, mapping to line numbers, etc).</p>

---

## Post #8 by @Satya_Arjunan (2019-02-10 23:15 UTC)

<p>Thanks Andras, but as I wrote in my first message, I built Slicer with the Debug option:</p>
<aside class="quote no-group" data-username="Satya_Arjunan" data-post="1" data-topic="5627">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/bcef8e/48.png" class="avatar"> Satya_Arjunan:</div>
<blockquote>
<p>cmake -DQt5_DIR=/usr/lib/qt5 -DCMAKE_BUILD_TYPE:STRING=Debug -</p>
</blockquote>
</aside>
<p>but I am not getting any useful information from GDB except:</p>
<blockquote>
<p>(gdb) exec-file Slicer<br>
(gdb) run<br>
Starting program: /home/satya/wrk/Slicer/build/Slicer-build/Slicer<br>
[Thread debugging using libthread_db enabled]<br>
Using host libthread_db library “/lib/x86_64-linux-gnu/libthread_db.so.1”.<br>
[New Thread 0x7ffff34af700 (LWP 24211)]<br>
error: [/home/satya/wrk/Slicer/build/Slicer-build/bin/./SlicerApp-real] exit abnormally - Report the problem.<br>
[Thread 0x7ffff34af700 (LWP 24211) exited]<br>
[Inferior 1 (process 24207) exited with code 01]</p>
</blockquote>

---

## Post #9 by @lassoan (2019-02-11 00:11 UTC)

<p>Can you get a call stack?</p>

---

## Post #10 by @Satya_Arjunan (2019-02-11 00:56 UTC)

<p>Here is what I am getting when I execute gdb with bin/SlicerApp-real:</p>
<p>(gdb) exec-file SlicerApp-real</p>
<p>(gdb) run</p>
<p>Starting program: /home/satya/wrk/Slicer/build/Slicer-build/bin/SlicerApp-real</p>
<p>[Thread debugging using libthread_db enabled]</p>
<p>Using host libthread_db library “/lib/x86_64-linux-gnu/libthread_db.so.1”.</p>
<p>[New Thread 0x7fffad95a700 (LWP 8620)]</p>
<p>qt5ct: using qt5ct plugin</p>
<p>[New Thread 0x7fffa59e1700 (LWP 8621)]</p>
<p>[New Thread 0x7fffa5127700 (LWP 8622)]</p>
<p>Thread 1 “SlicerApp-real” received signal SIGSEGV, Segmentation fault.</p>
<p>__strcmp_ssse3 () at …/sysdeps/x86_64/multiarch/…/strcmp.S:173</p>
<p>173	…/sysdeps/x86_64/multiarch/…/strcmp.S: No such file or directory.</p>
<p>(gdb) backtrace</p>
<p><span class="hashtag">#0</span>  0x00007fffc8fa4d76 in __strcmp_ssse3 ()</p>
<p>at …/sysdeps/x86_64/multiarch/…/strcmp.S:173</p>
<p><span class="hashtag">#1</span>  0x00007fffebafcb0d in lh_insert ()</p>
<p>at /home/satya/wrk/Slicer/build/OpenSSL/libcrypto.so.1.0.0</p>
<p><span class="hashtag">#2</span>  0x00007fffeba45f5b in OBJ_NAME_add ()</p>
<p>at /home/satya/wrk/Slicer/build/OpenSSL/libcrypto.so.1.0.0</p>
<p><span class="hashtag">#3</span>  0x00007fff9f949708 in  () at /usr/lib/x86_64-linux-gnu/libssl.so.1.1</p>
<p><span class="hashtag">#4</span>  0x00007fffe358f827 in __pthread_once_slow (once_control=0x7fff9fb877fc, init_routine=0x7fff9f949600) at pthread_once.c:116</p>
<p><span class="hashtag">#5</span>  0x00007fff9fd31939 in CRYPTO_THREAD_run_once ()</p>
<p>at /usr/lib/x86_64-linux-gnu/libcrypto.so.1.1</p>
<p><span class="hashtag">#6</span>  0x00007fff9f9498eb in OPENSSL_init_ssl ()</p>
<p>at /usr/lib/x86_64-linux-gnu/libssl.so.1.1</p>
<p><span class="hashtag">#7</span>  0x00007fffeb0ac7ac in  () at /usr/lib/x86_64-linux-gnu/libQt5Network.so.5</p>
<p><span class="hashtag">#8</span>  0x00007ffff5c08a0b in qSlicerCoreApplicationPrivate::init() (this=0x555555781f00)</p>
<p>at /home/satya/wrk/Slicer/Base/QTCore/qSlicerCoreApplication.cxx:271</p>
<p><span class="hashtag">#9</span>  0x00007ffff6f0e716 in qSlicerApplicationPrivate::init() (this=0x555555781f00)</p>
<p>at /home/satya/wrk/Slicer/Base/QTGUI/qSlicerApplication.cxx:205</p>
<p>—Type  to continue, or q  to quit—</p>
<p><span class="hashtag">#10</span> 0x00007ffff6f0f460 in qSlicerApplication::qSlicerApplication(int&amp;, char**) (this=</p>
<p>0x7fffffffdbb0, _argc=@0x7fffffffdb5c: 1, _argv=0x7fffffffdd18)</p>
<p>at /home/satya/wrk/Slicer/Base/QTGUI/qSlicerApplication.cxx:359</p>
<p><span class="hashtag">#11</span> 0x0000555555559fc1 in  ()</p>
<p><span class="hashtag">#12</span> 0x00007fffffffdd18 in  ()</p>
<p><span class="hashtag">#13</span> 0x0000000100000000 in  ()</p>
<p><span class="hashtag">#14</span> 0x0000000000000000 in  ()</p>
<p>(gdb) info frame</p>
<p>Stack level 0, frame at 0x7fffffffd730:</p>
<p>rip = 0x7fffc8fa4d76 in __strcmp_ssse3</p>
<p>(…/sysdeps/x86_64/multiarch/…/strcmp.S:173); saved rip = 0x7fffebafcb0d</p>
<p>called by frame at 0x7fffffffd770</p>
<p>source language asm.</p>
<p>Arglist at 0x7fffffffd720, args:</p>
<p>Locals at 0x7fffffffd720, Previous frame’s sp is 0x7fffffffd730</p>
<p>Saved registers:</p>
<p>rip at 0x7fffffffd728</p>

---

## Post #11 by @Satya_Arjunan (2019-02-11 01:42 UTC)

<p>This is probably related to using system Qt which was reported previously here: <a href="https://issues.slicer.org/view.php?id=4617" rel="nofollow noopener">https://issues.slicer.org/view.php?id=4617</a></p>
<p>I will follow the workaround provided there and report back.</p>

---

## Post #12 by @Satya_Arjunan (2019-02-11 09:35 UTC)

<p>I can confirm that the following steps resolved this issue:</p>
<ol>
<li>sudo apt install libcurl4-openssl-dev libssl-dev</li>
<li>git clone --recursive <a href="https://github.com/Slicer/Slicer.git" rel="nofollow noopener">https://github.com/Slicer/Slicer.git</a>
</li>
<li>cd Slicer &amp;&amp; mkdir build</li>
<li>cd build</li>
<li>cmake -DQt5_DIR=/usr/lib/qt5 -DCMAKE_BUILD_TYPE:STRING=Debug -DSlicer_USE_SYSTEM_OpenSSL=1 -DSlicer_USE_SYSTEM_curl:BOOL=1 …/</li>
<li>make -j2</li>
</ol>
<p>Should the status on <a href="https://issues.slicer.org/view.php?id=4617" rel="nofollow noopener">https://issues.slicer.org/view.php?id=4617</a> be set to resolved? I think it is somewhat misleading.</p>

---
