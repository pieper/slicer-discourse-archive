# Build Slicer with IGT

**Topic ID**: 33037
**Date**: 2023-11-26
**URL**: https://discourse.slicer.org/t/build-slicer-with-igt/33037

---

## Post #1 by @1116 (2023-11-26 15:54 UTC)

<p>I am building Slicer with SlicerIGT.<br>
I want the IGT module to be automatically added in Slicer when the Slicer.exe is created.</p>
<p>Where should I put the following commands in the top CMakeLists.txt of the Slicer code?  Is it OK to put the commands at the end?</p>
<pre><code class="lang-auto">#-----------------------------------------------------------------------------
# SlicerIGT
set(extension_name "SlicerIGT")
set(${extension_name}_SOURCE_DIR "${CMAKE_BINARY_DIR}/${extension_name}")
FetchContent_Populate(${extension_name}
  SOURCE_DIR ${${extension_name}_SOURCE_DIR}
  GIT_REPOSITORY ${EP_GIT_PROTOCOL}://github.com/slicerigt/slicerigt.git
  GIT_TAG master
  GIT_PROGRESS 1
  QUIET
  )
list(APPEND Slicer_EXTENSION_SOURCE_DIRS ${${extension_name}_SOURCE_DIR})
</code></pre>
<p>Further, is there any example of using Slicer_EXTENSION_SOURCE_DIRS in cmakelist.txt instead of using the above commands?</p>
<p>Thank you</p>

---
