---
topic_id: 858
title: "Tubetk Build With Slicer"
date: 2017-08-11
url: https://discourse.slicer.org/t/858
---

# TubeTK build with Slicer

**Topic ID**: 858
**Date**: 2017-08-11
**URL**: https://discourse.slicer.org/t/tubetk-build-with-slicer/858

---

## Post #1 by @leochan2009 (2017-08-11 16:09 UTC)

<p>Hi,</p>
<p>Does anyone build TubeTk successfully with the latest slicer?<br>
i receive this kind of error message<br>
Make Error at /usr/local/Cellar/cmake/3.9.0/share/cmake/Modules/FindPackageHandleStandardArgs.cmake:137 (message):<br>
Could NOT find JsonCpp (missing: JsonCpp_LIBRARIES JsonCpp_INCLUDE_DIRS)<br>
Call Stack (most recent call first):<br>
/usr/local/Cellar/cmake/3.9.0/share/cmake/Modules/FindPackageHandleStandardArgs.cmake:377 (_FPHSA_FAILURE_MESSAGE)<br>
/Users/longquanchen/Desktop/Github/Slicer-build/SlicerExecutionModel-build/CMake/FindJsonCpp.cmake:58 (find_package_handle_standard_args)<br>
CMakeLists.txt:509 (find_package)</p>
<p>I think possible solution could be using the latest SlicerExecutionModel.<br>
Any thoughts?</p>
<p>Best Regards,<br>
Longquan</p>

---

## Post #2 by @lassoan (2017-08-11 18:21 UTC)

<p>TubeTK build worked fine for me in the past, I just had to set in CMake <code>-DSlicer_DIR:PATH=%SLICER_BIN_DIR_DBG_X64% -DTubeTK_BUILD_SLICER_EXTENSION:BOOL=ON</code>.</p>
<p>The build now fails for me, too, with an error complaining that Slicer is configured with different JsonCpp. It seems that you have to make TubeTK to use Slicer’s JsonCpp - the same way TubeTK already uses VTK, CTK, etc. built by Slicer.</p>

---

## Post #3 by @leochan2009 (2017-08-11 19:08 UTC)

<p>Hi Andras,</p>
<p>Thanks for the prompt reply.<br>
Yes i make it build using your suggestion.<br>
However, the TubeTk is not maintained very well with the current Slicer API change.<br>
such as  <a href="https://github.com/KitwareMedical/ITKTubeTK/issues/921" rel="nofollow noopener">https://github.com/KitwareMedical/ITKTubeTK/issues/921</a><br>
I contact the developer in TubeTk, hope they could solve the issue.</p>
<p>Best Regards,<br>
Longquan</p>

---

## Post #4 by @lassoan (2017-08-11 19:52 UTC)

<p>All these should be very easy to fix. We just did not detect these errors because there was no automatic build set up for it. Let me know if you are stuck at any point.</p>

---

## Post #5 by @leochan2009 (2017-08-11 21:15 UTC)

<p>thanks, i will let you know if any question arises.</p>
<p>best,<br>
longquan</p>

---
