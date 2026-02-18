# Using other Qt modules in loadable extension

**Topic ID**: 17250
**Date**: 2021-04-22
**URL**: https://discourse.slicer.org/t/using-other-qt-modules-in-loadable-extension/17250

---

## Post #1 by @LorenzE (2021-04-22 12:07 UTC)

<p>I am trying to include the QtConcurrent module into my loadable extension. So far I tried to set <code>find_package(Qt5 COMPONENTS Concurrent REQUIRED)</code> in my module’s CMakeLists file. I know that Slicer does not use this module. I saw that the qt modules used by Slicer are included in <code>\S4\CMake\SlicerBlockFindQtAndCheckVersion.cmake</code>. I do not want to change anything in the Slicer build though, since only the extension is supposed to depend on QtConcurrent. Any ideas on how to achieve that?</p>

---

## Post #2 by @pieper (2021-04-22 14:42 UTC)

<p>You might be able to add a binary that matches Slicer’s Qt but that could be difficult.</p>
<p>I wonder if we should enable these.  I had thought the were available, since I know we had experimented with QFuture and related classes in CTK and elsewhere.</p>
<p>C++11 threads should be available if you want to use those.</p>

---

## Post #3 by @LorenzE (2021-04-26 12:43 UTC)

<p>That would be great if the concurrent module could be included in the slicer build directly.</p>

---
