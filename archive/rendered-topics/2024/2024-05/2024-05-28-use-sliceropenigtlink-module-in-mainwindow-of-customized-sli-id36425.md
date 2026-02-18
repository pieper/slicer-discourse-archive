# Use SlicerOpenIGTLink module in mainwindow of customized Slicer

**Topic ID**: 36425
**Date**: 2024-05-28
**URL**: https://discourse.slicer.org/t/use-sliceropenigtlink-module-in-mainwindow-of-customized-slicer/36425

---

## Post #1 by @schcat (2024-05-28 03:12 UTC)

<p>I am developing customized Slicer by <a href="https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/" rel="noopener nofollow ugc">SlicerCAT</a>. I added an button to toolbar of slicer mainwindow to allow toggling IGTLConnector. So I import vtkMRMLIGTLConnectorNode.h file of SlicerOpenIGTLink module in c++ code. But I encountered “No such file” error when compiling the source code:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/329d5e7b501d787ede389978bf2374d8373b82d5.png" data-download-href="/uploads/short-url/7dL2biG3YGraL6qDvB9whHgeiO1.png?dl=1" title="Screenshot from 2024-05-28 09-54-09" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/329d5e7b501d787ede389978bf2374d8373b82d5_2_690x101.png" alt="Screenshot from 2024-05-28 09-54-09" data-base62-sha1="7dL2biG3YGraL6qDvB9whHgeiO1" width="690" height="101" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/329d5e7b501d787ede389978bf2374d8373b82d5_2_690x101.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/329d5e7b501d787ede389978bf2374d8373b82d5.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/329d5e7b501d787ede389978bf2374d8373b82d5.png 2x" data-dominant-color="3F1C32"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2024-05-28 09-54-09</span><span class="informations">877×129 24.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I have added SlicerOpenIGTLink module in CMakelist.txt of SlicerCAT</p>
<pre><code class="lang-auto">set(extension_name "SlicerOpenIGTLink")
set(${extension_name}_SOURCE_DIR "${CMAKE_BINARY_DIR}/${extension_name}")
FetchContent_Populate(${extension_name}
  SOURCE_DIR     ${${extension_name}_SOURCE_DIR}
  GIT_REPOSITORY /home/lizhixue/project/3D_Slicer/SlicerDependency/extensions/SlicerOpenIGTLink
  GIT_TAG        schcat
  GIT_PROGRESS   1
  QUIET
  )
message(STATUS "Remote - ${extension_name} [OK]")
list(APPEND Slicer_EXTENSION_SOURCE_DIRS ${${extension_name}_SOURCE_DIR})
</code></pre>
<p>And it can be used in GUI and python code in my customized Slicer.<br>
How can I made .h file of SlicerOpenIGTLink module be find when compiling c++ source code?</p>

---

## Post #2 by @schcat (2024-06-01 01:42 UTC)

<p>Who can help me?  (;´▽`)</p>

---

## Post #3 by @lassoan (2024-06-01 11:59 UTC)

<p>You need to add SlicerIGT folders that include relevant .h files to include files and add relevant .lib files to link targets. See for example <a href="https://github.com/SlicerIGT/SlicerPathReconstruction/blob/master/PathReconstruction/MRML/CMakeLists.txt" class="inline-onebox">SlicerPathReconstruction/PathReconstruction/MRML/CMakeLists.txt at master · SlicerIGT/SlicerPathReconstruction · GitHub</a></p>

---

## Post #4 by @schcat (2024-06-02 02:49 UTC)

<p>Thank you！I will try it.</p>

---

## Post #5 by @schcat (2024-06-16 02:03 UTC)

<p>I did it when I found the correct parameter name such as “vtkSlicerOpenIGTLinkIFModuleMRML_INCLUDE_DIRS”. Example is very useful !</p>

---
