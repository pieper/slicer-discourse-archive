---
topic_id: 46576
title: "How To Programmatically Run Grow From Seeds From A C Module"
date: 2026-03-26
url: https://discourse.slicer.org/t/46576
---

# How to programmatically run "Grow from seeds" from a C++ module (CMake include issues)

**Topic ID**: 46576
**Date**: 2026-03-26
**URL**: https://discourse.slicer.org/t/how-to-programmatically-run-grow-from-seeds-from-a-c-module-cmake-include-issues/46576

---

## Post #1 by @Victor_Wayne (2026-03-26 11:03 UTC)

<p>Hi everyone,</p>
<p>I am developing a custom C++ loadable module and I am trying to programmatically run the “Grow from seeds” effect on a segmentation node.</p>
<p>I already have my <code>qMRMLSegmentEditorWidget</code> and <code>vtkMRMLSegmentEditorNode</code> successfully set up, and I have populated the target segmentation and master volume nodes.</p>
<p>Originally, my plan was to grab the effect directly to run the preview and apply it. However, I am completely unable to include <code>qSlicerSegmentEditorAbstractEffect.h</code>. Even after modifying my <code>CMakeLists.txt</code>, I can’t seem to link the effects module, presumably because those headers are kept private/internal.</p>
<p>I also tried bypassing the C++ class entirely by setting attributes directly on the parameter node (e.g., <code>parameterNode-&gt;SetAttribute("Grow from seeds.AutoUpdate", "1")</code>). However, because the effect is Python-based, I run into timing issues where my C++ code finishes executing before the Python script actually generates the preview node in the background.</p>
<p>Since I can’t use the effect classes directly due to CMake restrictions, and I want to avoid messy UI-button-clicking hacks in my C++ code, what is the cleanest, recommended way to trigger the “Grow from seeds” calculation and retrieve the resulting preview node?</p>
<p>Thanks in advance for the guidance!</p>
<p>this the cmake</p>
<pre><code class="lang-auto">
#-----------------------------------------------------------------------------
set(MODULE_NAME customSegmentEditor)

string(TOUPPER ${MODULE_NAME} MODULE_NAME_UPPER)

#-----------------------------------------------------------------------------
add_subdirectory(Logic)
add_subdirectory(Widgets)

#-----------------------------------------------------------------------------
set(MODULE_EXPORT_DIRECTIVE "Q_SLICER_QTMODULES_${MODULE_NAME_UPPER}_EXPORT")

set(MODULE_DEPENDENCIES
  Segmentations
)

# Current_{source,binary} and Slicer_{Libs,Base} already included
set(MODULE_INCLUDE_DIRECTORIES
  ${CMAKE_CURRENT_SOURCE_DIR}/Logic
  ${CMAKE_CURRENT_BINARY_DIR}/Logic
  ${CMAKE_CURRENT_SOURCE_DIR}/Widgets
  ${CMAKE_CURRENT_BINARY_DIR}/Widgets
  ${qSlicerSegmentationsModuleWidgets_INCLUDE_DIRS}
  ${qSlicerplanManagerModule_INCLUDE_DIRS}
  ${vtkSlicerplanManagerModuleLogic_INCLUDE_DIRS}
  ${Slicer_SUPERBUILD_DIR}/slicersources-src/Modules/Loadable/Segmentations/EditorEffects
  ${Slicer_DIR}/Modules/Loadable/Segmentations/EditorEffects
  )

set(MODULE_SRCS
  qSlicer${MODULE_NAME}Module.cxx
  qSlicer${MODULE_NAME}Module.h
  qSlicer${MODULE_NAME}ModuleWidget.cxx
  qSlicer${MODULE_NAME}ModuleWidget.h
  )

set(MODULE_UI_SRCS
  Resources/UI/qSlicer${MODULE_NAME}ModuleWidget.ui
  )

set(MODULE_TARGET_LIBRARIES
  vtkSlicer${MODULE_NAME}ModuleLogic
  qSlicer${MODULE_NAME}ModuleWidgets
  qSlicerSegmentationsModuleWidgets
  vtkSlicerSegmentationsModuleLogic
  vtkSlicerSegmentationsModuleMRML
  vtkSlicerplanManagerModuleLogic
  qSlicerplanManagerModule
  vtkSliceracpcTransformCustomModuleLogic
  qSlicerSegmentationsEditorsEffects
  )

set(MODULE_RESOURCES
  Resources/qSlicer${MODULE_NAME}Module.qrc
  )

#-----------------------------------------------------------------------------
slicerMacroBuildLoadableModule(
  NAME ${MODULE_NAME}
  EXPORT_DIRECTIVE ${MODULE_EXPORT_DIRECTIVE}
  INCLUDE_DIRECTORIES ${MODULE_INCLUDE_DIRECTORIES}
  SRCS ${MODULE_SRCS}
  UI_SRCS ${MODULE_UI_SRCS}
  TARGET_LIBRARIES ${MODULE_TARGET_LIBRARIES}
  RESOURCES ${MODULE_RESOURCES}
  WITH_GENERIC_TESTS
  )

#-----------------------------------------------------------------------------
if(BUILD_TESTING)
  add_subdirectory(Testing)
endif()
</code></pre>
<p>This is my cmake. but still this is giving me this error.</p>
<pre><code class="lang-auto">/home/venkatesh-23803/vtitan/brain_probe_path_planning/src/vTitanNavWithPlanner/Planner/customSegmentEditor/qSlicercustomSegmentEditorModuleWidget.cxx:40:10: fatal error: qSlicerSegmentEditorAbstractEffect.h: No such file or directory40 | #include “qSlicerSegmentEditorAbstractEffect.h”|          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~compilation terminated.
</code></pre>
<p>And this is how I changed the brush diameter without using the qSlicer abstract effect type.</p>
<pre data-code-wrap="cpp"><code class="lang-cpp">if (d-&gt;SegmentEditorWidget)
  {
    // qSlicerSegmentEditorAbstractEffect *paintEffect = d-&gt;SegmentEditorWidget-&gt;effectByName("Paint");
    // qSlicerSegmentEditorAbstractEffect *eraseEffect = d-&gt;SegmentEditorWidget-&gt;effectByName("Erase");

    // if (paintEffect)
    //   paintEffect-&gt;setParameter(diameter);
    // if (eraseEffect)
    //   eraseEffect-&gt;setParameter(diameter);
    vtkMRMLSegmentEditorNode* parameterNode = d-&gt;SegmentEditorWidget-&gt;mrmlSegmentEditorNode();

    if (parameterNode)
    {
      //  Write the brush size directly into the node's background dictionary!
      // (We use std::to_string to convert the double into text)
      parameterNode-&gt;SetAttribute("BrushDiameterIsRelative", "0");
      parameterNode-&gt;SetAttribute("BrushAbsoluteDiameter", std::to_string(diameter).c_str());
    }
  }
</code></pre>

---
