# Error while building SlicerSALT

**Topic ID**: 7926
**Date**: 2019-08-07
**URL**: https://discourse.slicer.org/t/error-while-building-slicersalt/7926

---

## Post #1 by @lbumbolo (2019-08-07 20:17 UTC)

<p>Hi,<br>
I try to build SlicerSALT by myself but after the</p>
<blockquote>
<p>make -j 6</p>
</blockquote>
<p>I receive this error:</p>
<pre><code>CMake Error at CMake/ctkMacroGenerateMocs.cmake:30 (QT5_CREATE_MOC_COMMAND):
  QT5_CREATE_MOC_COMMAND Function invoked with incorrect arguments for
  function named: QT5_CREATE_MOC_COMMAND
Call Stack (most recent call first):
  CMake/ctkMacroBuildLib.cmake:121 (QT4_GENERATE_MOCS)
  Libs/Widgets/CMakeLists.txt:448 (ctkMacroBuildLib)


CMake Error at CMake/ctkMacroGenerateMocs.cmake:30 (QT5_CREATE_MOC_COMMAND):
  QT5_CREATE_MOC_COMMAND Function invoked with incorrect arguments for
  function named: QT5_CREATE_MOC_COMMAND
Call Stack (most recent call first):
  CMake/ctkMacroBuildLib.cmake:121 (QT4_GENERATE_MOCS)
  Libs/Widgets/CMakeLists.txt:448 (ctkMacroBuildLib)
</code></pre>
<p>Does anyone know how to fix this error?</p>
<p>Thank you for your help<br>
Louis.</p>

---

## Post #2 by @bpaniagua (2019-08-15 18:16 UTC)

<p>Hi Louis,</p>
<p>On what OS are you building SALT?</p>

---
