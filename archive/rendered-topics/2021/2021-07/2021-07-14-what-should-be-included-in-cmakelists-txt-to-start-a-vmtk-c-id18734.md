---
topic_id: 18734
title: "What Should Be Included In Cmakelists Txt To Start A Vmtk C"
date: 2021-07-14
url: https://discourse.slicer.org/t/18734
---

# What should be included in CMakeLists.txt to start a VMTK C++ project?

**Topic ID**: 18734
**Date**: 2021-07-14
**URL**: https://discourse.slicer.org/t/what-should-be-included-in-cmakelists-txt-to-start-a-vmtk-c-project/18734

---

## Post #1 by @frankiole (2021-07-14 16:09 UTC)

<p>Hi,</p>
<p>I am trying to implement VMTK functions in my C++ code. I am able to run my program using both ITK and VTK libraries, however I cannot access VMTK libraries. I’ve already built VMTK, and I’m tweaking my CMakeLists.txt file in the project folder. When recompiling, it either ignores VMTK or produces <a href="https://groups.google.com/g/vmtk-users/c/g1kGrt5Znwk" rel="noopener nofollow ugc">this problem</a>. Any help on how to write my CMakeLists.txt file to compile correctly would be greatly appreciated. Thank you!</p>
<p>-Frank</p>

---

## Post #2 by @lassoan (2021-08-10 21:01 UTC)

<p>You would normally use ExternalProject infrastructure of CMake to build dependencies, such as VMTK. You can find an example here: <a href="https://github.com/vmtk/SlicerExtension-VMTK" class="inline-onebox">GitHub - vmtk/SlicerExtension-VMTK</a></p>

---
