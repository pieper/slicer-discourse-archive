# Adding a library to a custom loadable module

**Topic ID**: 44945
**Date**: 2025-11-03
**URL**: https://discourse.slicer.org/t/adding-a-library-to-a-custom-loadable-module/44945

---

## Post #1 by @Suhaim (2025-11-03 08:58 UTC)

<p>Hi,<br>
I wanted some support on adding a library in my custom loadable module.<br>
This is my cmake for adding a library called “SystemChecker” which is inside a directory called “SystemCheck”.<br>
The library is building correctly as the subdirectory’s cmake is working fine.<br>
When I try to link the built library with the loadable module I am getting this error.</p>
<pre><code class="lang-auto">CMake Error in CMakeLists.txt:
  export called with target "vtkSlicerplanManagerModuleLogic" which requires
  target "SystemChecker" that is not in any export set.
</code></pre>
<p>planManager is the name of my extension, it’s cmake is :-</p>
<pre><code class="lang-auto">project(vtkSlicer${MODULE_NAME}ModuleLogic)

find_package(wxWidgets REQUIRED)
find_package(OpenSSL REQUIRED)

include(${wxWidgets_USE_FILE})
add_subdirectory(SystemCheck)

set(KIT ${PROJECT_NAME})

set(${KIT}_EXPORT_DIRECTIVE "VTK_SLICER_${MODULE_NAME_UPPER}_MODULE_LOGIC_EXPORT")

set(${KIT}_INCLUDE_DIRECTORIES
  ${PYTHON_INCLUDE_DIRS}
)

set(${KIT}_SRCS
  vtkSlicer${MODULE_NAME}Logic.cxx
  vtkSlicer${MODULE_NAME}Logic.h
)

set(${KIT}_TARGET_LIBRARIES
  ${PYTHON_LIBRARIES}
  ${ITK_LIBRARIES}
  SystemChecker
)

#-----------------------------------------------------------------------------
SlicerMacroBuildModuleLogic(
  NAME ${KIT}
  EXPORT_DIRECTIVE ${${KIT}_EXPORT_DIRECTIVE}
  INCLUDE_DIRECTORIES ${${KIT}_INCLUDE_DIRECTORIES}
  SRCS ${${KIT}_SRCS}
  TARGET_LIBRARIES ${${KIT}_TARGET_LIBRARIES}
)

</code></pre>
<p>Further the directory SystemCheck has another Cmake file :-</p>
<pre><code class="lang-auto">cmake_minimum_required(VERSION 3.10)

add_library(SystemChecker STATIC
    src/MACAddressUtility.cpp
    src/sha.cpp
    src/isValidMachine.cpp
)

target_include_directories(
    SystemChecker
    PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/include
    ${OPENSSL_INCLUDE_DIR}
    ${wxWidgets_INCLUDE_DIRS}
)

target_link_libraries(
    SystemChecker
    PUBLIC
    ${wxWidgets_LIBRARIES}
    ${OPENSSL_LIBRARIES}
)

</code></pre>
<p>I realize this issue is due to a lack of good knowledge in Cmake, but I am having doubts on using Cmake with the slicer macros.</p>

---

## Post #2 by @Suhaim (2025-11-05 08:48 UTC)

<p>Hi,<br>
Any help on this matter would be much appreciated. I forgot to mention that I am building Slicer using the <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate" rel="noopener nofollow ugc">custom app template</a> provided.</p>

---
