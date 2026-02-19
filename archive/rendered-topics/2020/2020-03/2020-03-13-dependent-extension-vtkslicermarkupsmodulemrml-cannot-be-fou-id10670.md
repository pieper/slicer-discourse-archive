---
topic_id: 10670
title: "Dependent Extension Vtkslicermarkupsmodulemrml Cannot Be Fou"
date: 2020-03-13
url: https://discourse.slicer.org/t/10670
---

# Dependent extension vtkSlicerMarkupsModuleMRML cannot be found by CMake

**Topic ID**: 10670
**Date**: 2020-03-13
**URL**: https://discourse.slicer.org/t/dependent-extension-vtkslicermarkupsmodulemrml-cannot-be-found-by-cmake/10670

---

## Post #1 by @Tiffas (2020-03-13 10:24 UTC)

<p>Hi,</p>
<p>I try to build a loadable module which need a vtkMRMLMarkupsFiducialNode. I have a linker error during the build. I think the problem is related with the following warning:</p>
<p>Dependent extension vtkSlicerMarkupsModuleMRML cannot be found by CMake<br>
find_package(), therefore paths variables cannot be imported from this<br>
extension.  The problem can be resolved by generating<br>
vtkSlicerMarkupsModuleMRMLConfig.cmake by adding<br>
include(${Slicer_EXTENSION_GENERATE_CONFIG}) to the top-level<br>
CMakeLists.txt of the dependent extension.</p>
<p>The problem is include(${Slicer_EXTENSION_GENERATE_CONFIG}) is present in the top-level CMakeLists and I cannot find any vtkSlicerMarkupsModuleMRMLConfig.cmake file. Any idea on how to solve it ?</p>
<p>Many thanks !</p>

---

## Post #2 by @Mik (2020-03-15 10:35 UTC)

<p>In case of a linking problem i think you must add MRMLMarkups library to the CMakeLists.txt where you want to use markup nodes:</p>
<p>For example if you are going to use markups in logic, then in Logic directory CMakeLists.txt</p>
<p><code>set(${KIT}_TARGET_LIBRARIES</code><br>
<code>...</code><br>
<code> vtkSlicerMarkupsModuleMRML</code><br>
<code>...</code><br>
<code> )</code></p>

---
