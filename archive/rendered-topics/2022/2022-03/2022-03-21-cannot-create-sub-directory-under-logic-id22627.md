---
topic_id: 22627
title: "Cannot Create Sub Directory Under Logic"
date: 2022-03-21
url: https://discourse.slicer.org/t/22627
---

# cannot create sub directory under Logic

**Topic ID**: 22627
**Date**: 2022-03-21
**URL**: https://discourse.slicer.org/t/cannot-create-sub-directory-under-logic/22627

---

## Post #1 by @Haoyin_Zhou (2022-03-21 22:58 UTC)

<p>hi,</p>
<p>I am trying to develop a Loadable module under Windows 10 + vs2022. I have a problem that I cannot create a sub folder under Logic. For example, I create an empty loadable module called “test”, and put a subfolder called as “dummy” in the Logic folder, and in the Logic CMakeLists.txt, I added</p>
<p>add_subdirectory(dummy)</p>
<p>set(${KIT}_TARGET_LIBRARIES<br>
${ITK_LIBRARIES}<br>
dummy<br>
)</p>
<p>Then CMake (3.23) give me this error:<br>
CMake Error in CMakeLists.txt:<br>
export called with target “vtkSlicertestModuleLogic” which requires target “dummy” that is not in any export set.</p>
<p>This code works well on Linux and Mac, but cannot work on Windows. Could you help me with this? Thanks!</p>

---
