---
topic_id: 40667
title: "Loadable Module With External Binary Dependencies"
date: 2024-12-12
url: https://discourse.slicer.org/t/40667
---

# Loadable module with external binary dependencies

**Topic ID**: 40667
**Date**: 2024-12-12
**URL**: https://discourse.slicer.org/t/loadable-module-with-external-binary-dependencies/40667

---

## Post #1 by @PatrickR (2024-12-12 21:18 UTC)

<p>Hi,</p>
<p>I am new to slicer and I am trying to learn extension development for my Company’s internal use.</p>
<p>I am currently building an extension with a loadable module. This module depends on a few proprietary libraries distributed as .dll/.so.</p>
<p>So far I have managed to download these libraries from a server using Fetchcontent and linking against them.</p>
<p>I am not using Superbuild.</p>
<p>When I am trying to test my module using the SlicerWithExtension executable in the build folder, the required external dlls are not found.<br>
Manually copying these from the download folder to build/lib/Slicer-5.7/qt-loadable-modules folder allows me to run my extension. When I create an install package, these libraries are not included.</p>
<p>What is the best practice to build and test against an extension depending on external binary libraries?</p>
<p>How can include those libraries in my extension package?</p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2024-12-12 21:22 UTC)

<p>It is a small implementation detail that no build step is needed for this external library. You can follow any superbuild extension as an example (for example, SlicerOpenIGTLink). You will set the build command to an empty string and add an install command that places the dlls are into the third-party bin folder. On macOS younalso need to fix up the rpath in shared libraries.</p>

---

## Post #3 by @PatrickR (2024-12-13 12:16 UTC)

<p>Thank you, that brings me one step closer.</p>
<p>I have now created a superbuild extension. The external project uses copy to install the dlls into the third-party bin folder.</p>
<p>This now allows me to directly run the TestWithExtension executable.</p>
<p>However, if I understand correctly, to include the dlls in the installation package, I also need to create an install target in the top-level CMakeList.txt to install the files from the third party bin folder.</p>

---
