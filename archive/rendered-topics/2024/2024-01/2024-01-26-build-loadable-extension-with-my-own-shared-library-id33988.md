---
topic_id: 33988
title: "Build Loadable Extension With My Own Shared Library"
date: 2024-01-26
url: https://discourse.slicer.org/t/33988
---

# Build loadable extension with my own shared library

**Topic ID**: 33988
**Date**: 2024-01-26
**URL**: https://discourse.slicer.org/t/build-loadable-extension-with-my-own-shared-library/33988

---

## Post #1 by @nnzzll (2024-01-26 09:36 UTC)

<p>I’m developing a loadable extension.</p>
<p>As I know, a C++ loadable extension has three part: <code>vtkSlicer${Module_Name}ModuleLogic</code>, <code>qSlicer${MODULE_NAME}ModuleWidgets</code>, and the module itself.</p>
<p>If I build moduleLogic or ModuleWidgets with my own shared libraries, CMake will throw an error below<br>
<code>export called with target "*ModuleWidgets/ModuleLogic*" which requires target "*SomeSharedLibrary*" that is not in any export set.</code></p>
<p>My <code>CMakeLists.txt</code> for ModuleWidgets is shown below.<br>
It works fine when I link a library to module,but doesn’t work when link to logic or widgets.</p>
<pre><code class="lang-auto">project(qSlicer${MODULE_NAME}ModuleWidgets)

set(KIT ${PROJECT_NAME})

set(${KIT}_EXPORT_DIRECTIVE "Q_SLICER_MODULE_${MODULE_NAME_UPPER}_WIDGETS_EXPORT")

set(${KIT}_INCLUDE_DIRECTORIES
  )

set(${KIT}_SRCS
...
  )

set(${KIT}_MOC_SRCS
  qSlicer${MODULE_NAME}FooBarWidget.h
...
  )

set(${KIT}_UI_SRCS
  ../Resources/UI/qSlicer${MODULE_NAME}FooBarWidget.ui
...
  )

set(${KIT}_RESOURCES
  ../Resources/qSlicer${MODULE_NAME}Module.qrc
  )

set(${KIT}_TARGET_LIBRARIES
  vtkSlicer${MODULE_NAME}ModuleLogic
  SomeSharedLibary
  )

#-----------------------------------------------------------------------------
SlicerMacroBuildModuleWidgets(
  NAME ${KIT}
  EXPORT_DIRECTIVE ${${KIT}_EXPORT_DIRECTIVE}
  INCLUDE_DIRECTORIES ${${KIT}_INCLUDE_DIRECTORIES}
  SRCS ${${KIT}_SRCS}
  MOC_SRCS ${${KIT}_MOC_SRCS}
  UI_SRCS ${${KIT}_UI_SRCS}
  TARGET_LIBRARIES ${${KIT}_TARGET_LIBRARIES}
  RESOURCES ${${KIT}_RESOURCES}
  WRAP_PYTHONQT
  )

</code></pre>
<p>How can I fix this problem?</p>

---
