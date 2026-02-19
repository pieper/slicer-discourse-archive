---
topic_id: 35337
title: "Include And Compile Itk Vtk As An Externalproject Or Submodu"
date: 2024-04-07
url: https://discourse.slicer.org/t/35337
---

# Include and compile itk, vtk as an ExternalProject or Submodule

**Topic ID**: 35337
**Date**: 2024-04-07
**URL**: https://discourse.slicer.org/t/include-and-compile-itk-vtk-as-an-externalproject-or-submodule/35337

---

## Post #1 by @weidonglian (2024-04-07 19:25 UTC)

<p>In my c++ application, I need to use both itk, vtk and qt. In order to make the development reproducible without build itk/vtk as a seperate cmake project which definitely has a lot overhead.<br>
I have tried so far add itk/vtk as submodule into my third_party/itk and third_party/vtk folder. It ended up the following conflict targets (zlib, h5detect, such), as below. I also tried to use the CMake’s new feature FetchContent instead of ExternalProject_Add, I got the same error as below. I reckon the <code>FetchContent and FetchContent_MakeAvailable</code> works the same as my submodule solution.<br>
Any suggestion to mitigate this limitation? I do not want to hack into vtk and change those target name or CMP0002.<br>
Thanks in advanced,<br>
Weidong</p>
<pre><code class="lang-auto">CMake Error at build/_deps/vtk-src/CMake/vtkModule.cmake:3829 (add_library):
  add_library cannot create target "zlib" because another target with the
  same name already exists.  The existing target is a static library created
  in source directory
  "/home/weidong/develop/brain-flow-app/build/_deps/itk-src/Modules/ThirdParty/ZLIB/src/itkzlib-ng".
  See documentation for policy CMP0002 for more details.
Call Stack (most recent call first):
  build/_deps/vtk-src/ThirdParty/zlib/vtkzlib/CMakeLists.txt:118 (vtk_module_add_module)


CMake Warning at build/_deps/vtk-src/Rendering/OpenGL2/CMakeLists.txt:408 (message):
  X11::Xcursor not found; custom cursors will be ignored.


CMake Error at build/_deps/vtk-src/ThirdParty/hdf5/vtkhdf5/src/CMakeLists.txt:1067 (add_executable):
  add_executable cannot create target "H5detect" because another target with
  the same name already exists.  The existing target is an executable created
  in source directory
  "/home/weidong/develop/brain-flow-app/build/_deps/itk-src/Modules/ThirdParty/HDF5/src/itkhdf5/src".
  See documentation for policy CMP0002 for more details.


CMake Error at build/_deps/vtk-src/ThirdParty/hdf5/vtkhdf5/src/CMakeLists.txt:1128 (add_executable):
  add_executable cannot create target "H5make_libsettings" because another
  target with the same name already exists.  The existing target is an
  executable created in source directory
  "/home/weidong/develop/brain-flow-app/build/_deps/itk-src/Modules/ThirdParty/HDF5/src/itkhdf5/src".
  See documentation for policy CMP0002 for more details.
</code></pre>

---

## Post #2 by @lassoan (2024-04-07 19:32 UTC)

<p>Youncan set <code>USE_SYSTEM_...</code> CMake variable if you want tonuse any externally built libraries. Note that Slicer’s VTK fork contains a number of carefully selected patches that are required for correct functioning of the application,  so make sure you include all those in your externally built VTK. The same may apply to ITK, too.</p>
<p>So, it is probably simpler if you use Slicer’s VTK and ITK in your application. I would recommend to use SlicerCAT to build your application and Slicer together.</p>

---

## Post #3 by @weidonglian (2024-04-07 19:47 UTC)

<p>Indeed, your pointed SlicerCAT is really interesting and is exactly what I am looking for. That saves a lot of time to build everything from scrach.<br>
I will take a look and thanks so much for your help<br>
BR,<br>
Weidong</p>

---
