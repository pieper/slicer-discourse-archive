---
topic_id: 30035
title: "How To Include Other Modules In Plugins"
date: 2023-06-14
url: https://discourse.slicer.org/t/30035
---

# How to include other modules in plugins

**Topic ID**: 30035
**Date**: 2023-06-14
**URL**: https://discourse.slicer.org/t/how-to-include-other-modules-in-plugins/30035

---

## Post #1 by @ma1282029525 (2023-06-14 12:43 UTC)

<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/CreateLoadableModule" rel="noopener nofollow ugc">文档/每晚/开发人员/教程/创建可加载模块 - 切片器维基 (slicer.org)</a></p>
<p>I used this tutorial to build extensions, but I still couldn’t successfully compile them。</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>严重性</th>
<th>代码</th>
<th>说明</th>
<th>项目</th>
<th>文件</th>
<th>行</th>
<th>禁止显示状态</th>
</tr>
</thead>
<tbody>
<tr>
<td>错误</td>
<td>LNK2019</td>
<td>无法解析的外部符号 __declspec(dllimport) public: static class vtkSlicerVolumesLogic * __cdecl vtkSlicerVolumesLogic::SafeDownCast(class vtkObjectBase *) (_<em>imp</em>?SafeDownCast@vtkSlicerVolumesLogic@<span class="mention">@SAPEAV1</span>@PEAVvtkObjectBase@@<span class="mention">@Z</span>)，函数 public: void __cdecl qSlicertestModuleWidget::Moveimage(void) (?Moveimage@qSlicertestModuleWidget@<span class="mention">@QEAAXXZ</span>) 中引用了该符号</td>
<td>qSlicertestModule</td>
<td>E:\Slicer_all\testmodule\build\test\qSlicertestModuleWidget.obj</td>
<td>1</td>
<td></td>
</tr>
</tbody>
</table>
</div><pre><code class="lang-auto">cmake_minimum_required(VERSION 3.16.3...3.19.7 FATAL_ERROR)

project(test)

#-----------------------------------------------------------------------------
# Extension meta-information
set(EXTENSION_HOMEPAGE "https://www.slicer.org/wiki/Documentation/Nightly/Extensions/test")
set(EXTENSION_CATEGORY "Examples")
set(EXTENSION_CONTRIBUTORS "John Doe (AnyWare Corp.)")
set(EXTENSION_DESCRIPTION "This is an example of a simple extension")
set(EXTENSION_ICONURL "https://www.example.com/Slicer/Extensions/test.png")
set(EXTENSION_SCREENSHOTURLS "https://www.example.com/Slicer/Extensions/test/Screenshots/1.png")
set(EXTENSION_DEPENDS "NA") # Specified as a list or "NA" if no dependencies

#-----------------------------------------------------------------------------
# Extension dependencies
find_package(Slicer REQUIRED)
include(${Slicer_USE_FILE})

  set(MODULE_INCLUDE_DIRECTORIES
   ${CMAKE_CURRENT_SOURCE_DIR}/Widgets
   ${CMAKE_CURRENT_BINARY_DIR}/Widgets
   ${vtkSlicerVolumesModuleLogic_SOURCE_DIR}
   ${vtkSlicerVolumesModuleLogic_BINARY_DIR}
   )

set(MODULE_TARGET_LIBRARIES
  ${MODULE_TARGET_LIBRARIES}
  vtkSlicerVolumesModuleLogic
)

#-----------------------------------------------------------------------------
# Extension modules
add_subdirectory(test)
## NEXT_MODULE

#-----------------------------------------------------------------------------
include(${Slicer_EXTENSION_GENERATE_CONFIG})
include(${Slicer_EXTENSION_CPACK})
</code></pre>
<p>this is my cmakelists</p>

---

## Post #2 by @lassoan (2023-06-16 14:29 UTC)

<p>You may have missed adding the volumes logic to the list of target libraries for linking. See <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Loadable/Transforms/Logic/CMakeLists.txt#L18">this example</a> of Markups module logic linked into the Transforms module logic.</p>

---
