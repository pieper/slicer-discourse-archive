# Slicer build in linux freezes when building simpleitk

**Topic ID**: 2679
**Date**: 2018-04-25
**URL**: https://discourse.slicer.org/t/slicer-build-in-linux-freezes-when-building-simpleitk/2679

---

## Post #1 by @samira (2018-04-25 00:55 UTC)

<p>Hi All,</p>
<p>I am trying to build Slicer in Ubuntu but it freezes when it’s building SimpleITK. It seems to be working all the time but it doesn’t show any progress.<br>
I tried building it several times from the scratch but same thing happens every time.<br>
BTW, I keep everything in the Cmake as default.<br>
Any suggestions?</p>
<p>Thanks,</p>

---

## Post #2 by @lassoan (2018-04-25 01:14 UTC)

<p>SimpleITK takes a while to build. If you don’t see any progress for 24 hours then upload the complete build log somewhere and copy-paste the link here.</p>

---

## Post #3 by @ihnorton (2018-04-25 12:40 UTC)

<p>SimpleITK can also be disabled if you don’t need it, with <code>Slicer_USE_SimpleITK=OFF</code>.</p>

---

## Post #4 by @samira (2018-04-30 23:21 UTC)

<p>Thank you guys,</p>
<p>I am still struggling building the slicer on Linux. I started building it this morning again, I will wait till tomorrow and if it doesn’t build, I will upload the build log here.</p>

---

## Post #5 by @samira (2018-05-07 18:11 UTC)

<p>OK, I decided to turn off the simpleITK for now and also build the slicer with QT5. Now I have some errors when building CTK.<br>
I uploaded some output and error log files here:</p>
<p><a href="https://drive.google.com/drive/folders/11r_wY-wDT9yrfKJQGITR731eMxFU6YIF?usp=sharing" class="onebox" target="_blank" rel="nofollow noopener">https://drive.google.com/drive/folders/11r_wY-wDT9yrfKJQGITR731eMxFU6YIF?usp=sharing</a></p>
<p>Any help is appreciated. It’s my first time building slicer in Linux and it is really frustrating <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=5" title=":frowning:" class="emoji" alt=":frowning:"></p>
<p>Thanks,<br>
Samira</p>

---

## Post #6 by @pieper (2018-05-07 23:56 UTC)

<p>Sorry you are running into trouble.  I’m not sure what’s up but this message from the error log indicates perhaps the compiler is not installed right:</p>
<blockquote>
<p>/home/samira/slicer/debug/VTKv9/Utilities/KWIML/vtkkwiml/include/kwiml/int.h:1052:1: note: in expansion of macro ‘KWIML_INT_private_VERIFY_SIGN’<br>
KWIML_INT_private_VERIFY_SIGN(KWIML_INT_uintptr_t, KWIML_INT_uintptr_t, &gt;);<br>
^<br>
c++: internal compiler error: Killed (program cc1plus)<br>
Please submit a full bug report,</p>
</blockquote>
<p>You might try building vtk independent of Slicer and see if you can narrow down what leads to this.</p>
<p>(FWIW I regularly build on unbuntu 16.04 with no problems)</p>

---

## Post #7 by @samira (2018-05-08 23:26 UTC)

<p>Thanks Steve,</p>
<p>I have already built the CTK independent and it was successful. Now all the dependencies are built. Here is the error I am getting now:</p>
<pre><code>c++: internal compiler error: Killed (program cc1plus)
Please submit a full bug report,
with preprocessed source if appropriate.
See &lt;file:///usr/share/doc/gcc-5/README.Bugs&gt; for instructions.
Libs/MRML/Widgets/Testing/CMakeFiles/qMRMLWidgetsCxxTests.dir/build.make:1229: recipe for target 'Libs/MRML/Widgets/Testing/CMakeFiles/qMRMLWidgetsCxxTests.dir/qMRMLScalarInvariantComboBoxEventTranslatorPlayerTest1.cxx.o' failed
make[5]: *** [Libs/MRML/Widgets/Testing/CMakeFiles/qMRMLWidgetsCxxTests.dir/qMRMLScalarInvariantComboBoxEventTranslatorPlayerTest1.cxx.o] Error 4
make[5]: *** Waiting for unfinished jobs....
[ 53%] Built target qMRMLWidgetsPlugins
In file included from /home/samira/slicer/Slicer/Libs/MRML/Widgets/Testing/qMRMLLayoutManagerWithCustomFactoryTest.cxx:23:0:
/home/samira/slicer/Slicer/Libs/MRML/Widgets/Testing/qMRMLLayoutManagerTestHelper.cxx:13:6: warning: ‘bool {anonymous}::checkViewArrangement(int, qMRMLLayoutManager*, vtkMRMLLayoutNode*, int)’ defined but not used [-Wunused-function]
 bool checkViewArrangement(int line, qMRMLLayoutManager* layoutManager,
      ^
[ 53%] Linking CXX shared library ../../bin/libqSlicerBaseQTGUI.so
In file included from /home/samira/slicer/Slicer/Libs/MRML/Widgets/Testing/qMRMLLayoutManagerVisibilityTest.cxx:23:0:
/home/samira/slicer/Slicer/Libs/MRML/Widgets/Testing/qMRMLLayoutManagerTestHelper.cxx:13:6: warning: ‘bool {anonymous}::checkViewArrangement(int, qMRMLLayoutManager*, vtkMRMLLayoutNode*, int)’ defined but not used [-Wunused-function]
 bool checkViewArrangement(int line, qMRMLLayoutManager* layoutManager,
      ^
In file included from /home/samira/slicer/Slicer/Libs/MRML/Widgets/Testing/qMRMLLayoutManagerTest1.cxx:23:0:
/home/samira/slicer/Slicer/Libs/MRML/Widgets/Testing/qMRMLLayoutManagerTestHelper.cxx:13:6: warning: ‘bool {anonymous}::checkViewArrangement(int, qMRMLLayoutManager*, vtkMRMLLayoutNode*, int)’ defined but not used [-Wunused-function]
 bool checkViewArrangement(int line, qMRMLLayoutManager* layoutManager,
      ^
CMakeFiles/Makefile2:2626: recipe for target 'Libs/MRML/Widgets/Testing/CMakeFiles/qMRMLWidgetsCxxTests.dir/all' failed
make[4]: *** [Libs/MRML/Widgets/Testing/CMakeFiles/qMRMLWidgetsCxxTests.dir/all] Error 2
make[4]: *** Waiting for unfinished jobs....
[ 53%] Built target qSlicerBaseQTGUI
Makefile:162: recipe for target 'all' failed
make[3]: *** [all] Error 2
CMakeFiles/Slicer.dir/build.make:141: recipe for target 'Slicer-prefix/src/Slicer-stamp/Slicer-build' failed
make[2]: *** [Slicer-prefix/src/Slicer-stamp/Slicer-build] Error 2
CMakeFiles/Makefile2:101: recipe for target 'CMakeFiles/Slicer.dir/all' failed
make[1]: *** [CMakeFiles/Slicer.dir/all] Error 2
Makefile:94: recipe for target 'all' failed
make: *** [all] Error 2
</code></pre>
<p>I have built the Slicer in windows million times, it’s my first time in linux and I might do something wrong that’s totally possible.<br>
Do you still think it can be the compiler?</p>
<p>Samira</p>

---

## Post #8 by @lassoan (2018-05-09 03:48 UTC)

<p>This may be due to running out of memory. Try to disable parallel build by running <code>make -j1</code> or increase amount of physical RAM or swap size.</p>

---

## Post #9 by @samira (2018-05-09 18:14 UTC)

<p>Yes! Thanks Andras, I disabled the parallel build and it worked <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
