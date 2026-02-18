# Using VTK Remote module in Python scripted Slicer module

**Topic ID**: 2617
**Date**: 2018-04-17
**URL**: https://discourse.slicer.org/t/using-vtk-remote-module-in-python-scripted-slicer-module/2617

---

## Post #1 by @mschumaker (2018-04-17 21:14 UTC)

<p>There is a Remote VTK module (SplineDrivenImageSlicer) that I am hoping to use from a scripted module, and I’m wondering what the most straightforward way to accomplish this is. I would eventually like to make this extension available from the Extension Manager, and able to be used from a Slicer pre-built binary. Building VTKv9 with the CMake option Module_SplineDrivenImageSlicer set to ON adds it to the vtk Python-wrapped library, and avoids any intermediary modules.</p>
<p>I guess my question is, do I need to create a loadable module as an intermediate step, or is there a way I can package a VTK Remote module into a scripted module in a simpler way?</p>

---

## Post #2 by @lassoan (2018-04-17 21:18 UTC)

<p>I think SlicerVirtualReality extension uses a VTK remote module.</p>

---

## Post #3 by @mschumaker (2018-04-17 21:59 UTC)

<p>Excellent, thank you. That’s a good example for how to fetch an external project and include it in a loadable module.<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/KitwareMedical/SlicerVirtualReality/blob/master/SuperBuild/External_OpenVR.cmake" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/KitwareMedical/SlicerVirtualReality/blob/master/SuperBuild/External_OpenVR.cmake" target="_blank" rel="nofollow noopener">KitwareMedical/SlicerVirtualReality/blob/master/SuperBuild/External_OpenVR.cmake</a></h4>
<pre><code class="lang-cmake">set(proj OpenVR)

# Set dependency list
set(${proj}_DEPENDENCIES "")

# Sanity checks
if(DEFINED OPENVR_INCLUDE_DIR AND NOT EXISTS ${OPENVR_INCLUDE_DIR})
  message(FATAL_ERROR "OPENVR_INCLUDE_DIR variable is defined but corresponds to nonexistent directory")
endif()
if(DEFINED OPENVR_LIBRARY AND NOT EXISTS ${OPENVR_LIBRARY})
  message(FATAL_ERROR "OPENVR_LIBRARY variable is defined but corresponds to nonexistent path")
endif()

if(${CMAKE_PROJECT_NAME}_USE_SYSTEM_${proj})
  unset(OPENVR_INCLUDE_DIR CACHE)
  unset(OPENVR_LIBRARY CACHE)
  find_package(OpenVR REQUIRED MODULE)
endif()

# Include dependent projects if any
</code></pre>

  This file has been truncated. <a href="https://github.com/KitwareMedical/SlicerVirtualReality/blob/master/SuperBuild/External_OpenVR.cmake" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---
