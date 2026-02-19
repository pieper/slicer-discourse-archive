---
topic_id: 3835
title: "Cmake Error When Building A New C Loadable Extension Module"
date: 2018-08-19
url: https://discourse.slicer.org/t/3835
---

# Cmake error when building a new C++ loadable extension module

**Topic ID**: 3835
**Date**: 2018-08-19
**URL**: https://discourse.slicer.org/t/cmake-error-when-building-a-new-c-loadable-extension-module/3835

---

## Post #1 by @kerry (2018-08-19 20:07 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.7<br>
CMake: 3.8.2</p>
<p>I added a new module using the extension manager and the module is set to be a loadable module. Try to build the extension using CMake. The Slicer_DIR was set to be the Slicer_build directory in CMake.<br>
I got the following error in CMake:</p>
<p>CMake Error at Logic/CMakeLists.txt:20 (SlicerMacroBuildModuleLogic):<br>
Unknown CMake command<br>
“SlicerMacroBuildModuleLogic”</p>
<p>Could you please let me know what is missing here?</p>
<p>Thanks,</p>
<p>Shelly</p>

---

## Post #2 by @lassoan (2018-08-20 01:00 UTC)

<p>So many things have been changed, fixed, and improved since 4.7 that probably none of the developers would want to go back and investigate issues in that old version.</p>
<p>Could you update to the latest master version and see if you can reproduce the issue?</p>

---
