---
topic_id: 44092
title: "Where To Put Libraries Needed For Installation Import"
date: 2025-08-15
url: https://discourse.slicer.org/t/44092
---

# Where to put libraries needed for installation/import?

**Topic ID**: 44092
**Date**: 2025-08-15
**URL**: https://discourse.slicer.org/t/where-to-put-libraries-needed-for-installation-import/44092

---

## Post #1 by @Canada101 (2025-08-15 08:08 UTC)

<p>I am developing an extension and am in the very early phases. I see in the 3d slicer documentation that there is a superbuild extension template, does that whole template replace the CmakeLists file the extension creation template gives you?</p>

---

## Post #2 by @Thibault_Pelletier (2025-08-19 06:17 UTC)

<p>Hi <a class="mention" href="/u/canada101">@Canada101</a>,</p>
<p>The SuperBuild template is meant for extensions that have external C++ dependencies they need to build prior to C++ CLI or Loadable extensions.</p>
<p>In the CMakeLists.txt, a few variables will indicate that you are working in a SuperBuild:</p>
<pre><code class="lang-auto">set(EXTENSION_BUILD_SUBDIRECTORY inner-build)
set(SUPERBUILD_TOPLEVEL_PROJECT inner)
mark_as_superbuild(Slicer_DIR)

#-----------------------------------------------------------------------------
# SuperBuild setup
option(${EXTENSION_NAME}_SUPERBUILD "Build ${EXTENSION_NAME} and the projects it depends on." ON)
mark_as_advanced(${EXTENSION_NAME}_SUPERBUILD)
if(${EXTENSION_NAME}_SUPERBUILD)
  include("${CMAKE_CURRENT_SOURCE_DIR}/SuperBuildPrerequisites.cmake")
  include("${CMAKE_CURRENT_SOURCE_DIR}/SuperBuild.cmake")
  return()
endif()
</code></pre>
<p>If you are only using Python for your extension or only depend on Slicer’s libraries (VTK / ITK / CTK / Qt …) for your C++ extension, you can leave aside the SuperBuild.</p>
<p>Best,<br>
Thibault</p>

---
