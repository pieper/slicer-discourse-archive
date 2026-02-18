# loadable module to integrate a haptic device 

**Topic ID**: 24332
**Date**: 2022-07-15
**URL**: https://discourse.slicer.org/t/loadable-module-to-integrate-a-haptic-device/24332

---

## Post #1 by @leo (2022-07-15 15:48 UTC)

<p>Hey everyone,<br>
I am trying to create a loadable module in order to integrate a haptic device within Slicer.<br>
Now I currently managed to have prototypical usage of the devices framework within the module, my next issue is how to integrate the device into the slicer scene and access the mrml methods and scenes data.<br>
I would be really glad for any advice.</p>
<p>Kind regards,<br>
Leo</p>

---

## Post #2 by @jcfr (2022-07-15 16:42 UTC)

<p>Cc: <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> <a class="mention" href="/u/jadh4v">@jadh4v</a></p>

---

## Post #3 by @Sam_Horvath (2022-07-15 16:46 UTC)

<p>Could you share what haptic device you are using, and what so of interaction you are trying to achieve?</p>
<p>The basic method of interfacing would be to represent the position of the haptic device as a transform node.</p>

---

## Post #4 by @leo (2022-07-20 11:31 UTC)

<p>Thankyou very much for your reply! So the device I am using is a 3d Systems Phantom touch. And I actually wanted to achieve a Haptic response based on the graphic data of the volume represented in Slicer. So besides the position I would need to access the data of the nodes in vtk, e.g. to use greyscale value and other values of interest for the graphic rendering. Have you got any resources that you would reccomend?</p>

---

## Post #5 by @Sam_Horvath (2022-07-20 21:10 UTC)

<p>So, for interfacing with the 3D Systems Phantom Omni / Geomagic Touch, we use the OpenHaptics interface through our simulation library <a href="https://www.imstk.org/">IMSTK</a>.  We have a prototype extension <a href="https://github.com/KitwareMedical/SlicerIMSTK">SlicerIMSTK</a> which bundles IMSTK, and has <a href="https://github.com/KitwareMedical/SlicerIMSTK/blob/897ab3175ba0fc5275ea4f47e4bdacad99aac7de/IMSTK/Logic/vtkSlicerIMSTKLogic.cxx#L121">example code</a> for using OpenHaptics with IMSTK. Note, that the OpenHaptics support in the extension is off by default, you would need to change the <a href="https://github.com/KitwareMedical/SlicerIMSTK/blob/897ab3175ba0fc5275ea4f47e4bdacad99aac7de/CMakeLists.txt#L42">CMakeLists</a> to test it out.</p>

---

## Post #6 by @leo (2022-07-21 16:16 UTC)

<p>Thankyou very much for replying! I actually tried to build slicer with the IMSTK extension and before building I have done the steps you recommended, unfortunatly I was not able to build and run slicer with the extension. Do you have any advise or resources besides the git repository you could point me to?</p>
<pre><code class="lang-auto">Build started...
1&gt;------ Build started: Project: ZERO_CHECK, Configuration: Debug x64 ------
1&gt;Checking Build System
2&gt;------ Build started: Project: OpenVR, Configuration: Debug x64 ------
3&gt;------ Build started: Project: vtkRenderingVR, Configuration: Debug x64 ------
4&gt;------ Build started: Project: Assimp, Configuration: Debug x64 ------
5&gt;------ Build started: Project: Eigen3, Configuration: Debug x64 ------
6&gt;------ Build started: Project: Libusb, Configuration: Debug x64 ------
7&gt;------ Build started: Project: VegaFEM, Configuration: Debug x64 ------
8&gt;------ Build started: Project: g3log, Configuration: Debug x64 ------
9&gt;------ Build started: Project: tbb, Configuration: Debug x64 ------
10&gt;------ Build started: Project: vtkRenderingExternal, Configuration: Debug x64 ------
11&gt;------ Skipped Build: Project: Continuous, Configuration: Debug x64 ------
11&gt;Project not selected to build for this solution configuration 
12&gt;------ Skipped Build: Project: Experimental, Configuration: Debug x64 ------
12&gt;Project not selected to build for this solution configuration 
13&gt;------ Skipped Build: Project: Nightly, Configuration: Debug x64 ------
13&gt;Project not selected to build for this solution configuration 
14&gt;------ Skipped Build: Project: NightlyMemoryCheck, Configuration: Debug x64 ------
14&gt;Project not selected to build for this solution configuration 
15&gt;------ Skipped Build: Project: RUN_TESTS, Configuration: Debug x64 ------
15&gt;Project not selected to build for this solution configuration 
2&gt;Performing update step for 'OpenVR'
2&gt;Skip step
2&gt;Building Custom Rule C:/Users/Leonard/SlicerIMSTK/CMakeLists.txt
2&gt;No patch step for 'OpenVR'
2&gt;Performing configure step for 'OpenVR'
2&gt;Skip step
2&gt;Performing build step for 'OpenVR'
3&gt;Performing configure step for 'vtkRenderingVR'
2&gt;Skip step
2&gt;Performing install step for 'OpenVR'
2&gt;Skip step
2&gt;Completed 'OpenVR'
4&gt;Performing update step for 'Assimp'
3&gt;loading initial cache file C:/Users/Leonard/SlicerIMSTK/vtkRenderingVR-prefix/tmp/vtkRenderingVR-cache-Debug.cmake
3&gt;-- Setting VTK_MODULE_SOURCE_DIR to C:/D/S4D/VTK-build/../VTK/Rendering/VR
3&gt;-- Setting VTK_MODULE_NAME to RenderingVR
3&gt;-- Setting VTK_MODULE_CMAKE_MODULE_PATH to C:/D/S4D/VTK-build/../VTK/CMake
3&gt;-- Selecting Windows SDK version 10.0.19041.0 to target Windows 10.0.19043.
4&gt;Building Custom Rule C:/Users/Leonard/SlicerIMSTK/CMakeLists.txt
6&gt;Performing update step for 'Libusb'
5&gt;Building Custom Rule C:/Users/Leonard/SlicerIMSTK/CMakeLists.txt
7&gt;Building Custom Rule C:/Users/Leonard/SlicerIMSTK/CMakeLists.txt
4&gt;No patch step for 'Assimp'
8&gt;Performing install step for 'g3log'
6&gt;Skip step
6&gt;Building Custom Rule C:/Users/Leonard/SlicerIMSTK/CMakeLists.txt
3&gt;CMake Error at C:/D/S4D/VTK-build/lib/cmake/vtk-9.0/vtkModule.cmake:569 (message):
3&gt;  No module files given to scan.
3&gt;Call Stack (most recent call first):
3&gt;  CMakeLists.txt:105 (vtk_module_scan)
3&gt;
3&gt;
4&gt;Performing configure step for 'Assimp'
4&gt;loading initial cache file C:/Users/Leonard/SlicerIMSTK/External/Assimp/tmp/Assimp-cache-Debug.cmake
4&gt;CMake Deprecation Warning at CMakeLists.txt:39 (cmake_minimum_required):
4&gt;  Compatibility with CMake &lt; 2.8.12 will be removed from a future version of
4&gt;  CMake.
4&gt;
4&gt;  Update the VERSION argument &lt;min&gt; value or use a ...&lt;max&gt; suffix to tell
4&gt;  CMake that the project does not need compatibility with older versions.
4&gt;
4&gt;
4&gt;-- Selecting Windows SDK version 10.0.19041.0 to target Windows 10.0.19043.
6&gt;No patch step for 'Libusb'
6&gt;Performing configure step for 'Libusb'
3&gt;-- Configuring incomplete, errors occurred!
3&gt;See also "C:/Users/Leonard/SlicerIMSTK/vtkRenderingVR-build/CMakeFiles/CMakeOutput.log".
3&gt;See also "C:/Users/Leonard/SlicerIMSTK/vtkRenderingVR-build/CMakeFiles/CMakeError.log".
3&gt;C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(241,5): error MSB8066: Custom build for 'C:\Users\Leonard\SlicerIMSTK\CMakeFiles\eca52943f586b733d2b9eb7c0e350129\vtkRenderingVR-configure.rule;C:\Users\Leonard\SlicerIMSTK\CMakeFiles\eca52943f586b733d2b9eb7c0e350129\vtkRenderingVR-build.rule;C:\Users\Leonard\SlicerIMSTK\CMakeFiles\eca52943f586b733d2b9eb7c0e350129\vtkRenderingVR-install.rule;C:\Users\Leonard\SlicerIMSTK\CMakeFiles\4cd7eb71559f6efa497210c55da60646\vtkRenderingVR-complete.rule;C:\Users\Leonard\SlicerIMSTK\CMakeFiles\511a6a1116940676e843c42da3309406\vtkRenderingVR.rule;C:\Users\Leonard\SlicerIMSTK\CMakeLists.txt' exited with code 1.
3&gt;Done building project "vtkRenderingVR.vcxproj" -- FAILED.
8&gt;Error copying file "C:/Users/Leonard/SlicerIMSTK/g3log-build/Debug/g3loggerd.lib" to "C:/Users/Leonard/SlicerIMSTK/g3log-install/lib/g3loggerd.lib".
8&gt;C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(241,5): error MSB8066: Custom build for 'C:\Users\Leonard\SlicerIMSTK\CMakeFiles\7707c36ca0334f5c9d41006a4638df2f\g3log-install.rule;C:\Users\Leonard\SlicerIMSTK\CMakeFiles\4cd7eb71559f6efa497210c55da60646\g3log-complete.rule;C:\Users\Leonard\SlicerIMSTK\CMakeFiles\511a6a1116940676e843c42da3309406\g3log.rule;C:\Users\Leonard\SlicerIMSTK\CMakeLists.txt' exited with code 1.
8&gt;Done building project "g3log.vcxproj" -- FAILED.
16&gt;------ Build started: Project: vtkRenderingOpenVR, Configuration: Debug x64 ------
6&gt;Skip step
6&gt;Performing build step for 'Libusb'
6&gt;Skip step
6&gt;Performing install step for 'Libusb'
9&gt;Generate version-tbb.txt and license-tbb.txt
4&gt;-- Could NOT find PkgConfig (missing: PKG_CONFIG_EXECUTABLE)
10&gt;Building Custom Rule C:/Users/Leonard/SlicerIMSTK/CMakeLists.txt
6&gt;Completed 'Libusb'
4&gt;-- Looking for DirectX...
4&gt;-- DirectX_PREFIX_PATH changed.
16&gt;Performing configure step for 'vtkRenderingOpenVR'
4&gt;-- Found DirectX: C:/Program Files (x86)/Windows Kits/10/Lib/10.0.19041.0/um/x64/d3d9.lib
4&gt;-- DX lib dir: C:/Program Files (x86)/Windows Kits/10/Lib/10.0.19041.0/um/x64
4&gt;-- Looking for ZLIB...
4&gt;-- Could NOT find PkgConfig (missing: PKG_CONFIG_EXECUTABLE)
4&gt;-- Found ZLIB: optimized;C:/dev/vcpkg/installed/x64-windows/lib/zlib.lib;debug;C:/dev/vcpkg/installed/x64-windows/debug/lib/zlibd.lib
4&gt;-- Build an import-only version of Assimp.
4&gt;CMake Deprecation Warning at code/CMakeLists.txt:45 (cmake_minimum_required):
4&gt;  Compatibility with CMake &lt; 2.8.12 will be removed from a future version of
4&gt;  CMake.
4&gt;
4&gt;  Update the VERSION argument &lt;min&gt; value or use a ...&lt;max&gt; suffix to tell
4&gt;  CMake that the project does not need compatibility with older versions.
4&gt;
4&gt;
16&gt;loading initial cache file C:/Users/Leonard/SlicerIMSTK/vtkRenderingOpenVR-prefix/tmp/vtkRenderingOpenVR-cache-Debug.cmake
16&gt;-- Setting VTK_MODULE_SOURCE_DIR to C:/D/S4D/VTK-build/../VTK/Rendering/OpenVR
16&gt;-- Setting VTK_MODULE_NAME to RenderingOpenVR
16&gt;-- Setting VTK_MODULE_CMAKE_MODULE_PATH to C:/D/S4D/VTK-build/../VTK/CMake
16&gt;-- Selecting Windows SDK version 10.0.19041.0 to target Windows 10.0.19043.
4&gt;-- Enabled formats: 3DS AC ASE ASSBIN ASSXML B3D BVH COLLADA DXF CSM HMP IRRMESH IRR LWO LWS MD2 MD3 MD5 MDC MDL NFF NDO OFF OBJ OGRE OPENGEX PLY MS3D COB BLEND IFC XGL FBX Q3D Q3BSP RAW SIB SMD STL TERRAGEN 3D X GLTF 3MF
4&gt;-- Disabled formats:
4&gt;-- Configuring done
9&gt;Building Custom Rule C:/Users/Leonard/SlicerIMSTK/CMakeLists.txt
9&gt;Completed 'tbb'
4&gt;-- Generating done
4&gt;-- Build files have been written to: C:/Users/Leonard/SlicerIMSTK/Assimp-build
4&gt;Performing build step for 'Assimp'
4&gt;Microsoft (R) Build Engine version 16.11.2+f32259642 for .NET Framework
4&gt;Copyright (C) Microsoft Corporation. All rights reserved.
4&gt;
16&gt;-- Configuring done
4&gt;  Checking Build System
16&gt;-- Generating done
16&gt;-- Build files have been written to: C:/Users/Leonard/SlicerIMSTK/vtkRenderingOpenVR-build
16&gt;Building Custom Rule C:/Users/Leonard/SlicerIMSTK/CMakeLists.txt
16&gt;Performing build step for 'vtkRenderingOpenVR'
16&gt;Microsoft (R) Build Engine version 16.11.2+f32259642 for .NET Framework
16&gt;Copyright (C) Microsoft Corporation. All rights reserved.
16&gt;
4&gt;  assimp.vcxproj -&gt; C:\Users\Leonard\SlicerIMSTK\Assimp-build\code\Debug\assimp.dll
4&gt;  Building Custom Rule C:/Users/Leonard/SlicerIMSTK/Assimp/CMakeLists.txt
4&gt;Performing install step for 'Assimp'
4&gt;Microsoft (R) Build Engine version 16.11.2+f32259642 for .NET Framework
4&gt;Copyright (C) Microsoft Corporation. All rights reserved.
4&gt;
16&gt;  Checking Build System
16&gt;  RenderingOpenVR.vcxproj -&gt; C:\Users\Leonard\SlicerIMSTK\bin\Debug\vtkRenderingOpenVRd.dll
16&gt;  Building Custom Rule C:/Users/Leonard/SlicerIMSTK/VTKExternalModule/CMakeLists.txt
16&gt;  vtkRenderingOpenVRPython.vcxproj -&gt; C:\Users\Leonard\SlicerIMSTK\vtkRenderingOpenVR-build\bin\Lib\site-packages\vtkmodules\vtkRenderingOpenVR.cp36-win_amd64.pyd
16&gt;  Building Custom Rule C:/Users/Leonard/SlicerIMSTK/VTKExternalModule/CMakeLists.txt
4&gt;  assimp.vcxproj -&gt; C:\Users\Leonard\SlicerIMSTK\Assimp-build\code\Debug\assimp.dll
16&gt;No install step for 'vtkRenderingOpenVR'
16&gt;Completed 'vtkRenderingOpenVR'
16&gt;C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(241,5): warning MSB8064: Custom build for item "C:\Users\Leonard\SlicerIMSTK\CMakeFiles\225a4934b41d8cf019587d3277529564\vtkRenderingOpenVR-configure.rule" succeeded, but specified dependency "c:\users\leonard\slicerimstk\vtkrenderingvr-prefix\src\vtkrenderingvr-stamp\debug\vtkrenderingvr-done" does not exist. This may cause incremental build to work incorrectly.
4&gt;  -- Install configuration: "Debug"
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/./lib/Slicer-4.13/cmake/assimp-3.3/assimp-config.cmake
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/./lib/Slicer-4.13/cmake/assimp-3.3/assimp-config-version.cmake
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/./lib/Slicer-4.13/pkgconfig/assimp.pc
16&gt;Done building project "vtkRenderingOpenVR.vcxproj".
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/./lib/Slicer-4.13/assimp.lib
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/./bin/assimp.dll
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/anim.h
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/ai_assert.h
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/camera.h
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/color4.h
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/color4.inl
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/config.h
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/defs.h
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/cfileio.h
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/light.h
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/material.h
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/material.inl
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/matrix3x3.h
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/matrix3x3.inl
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/matrix4x4.h
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/matrix4x4.inl
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/mesh.h
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/postprocess.h
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/quaternion.h
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/quaternion.inl
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/scene.h
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/metadata.h
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/texture.h
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/types.h
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/vector2.h
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/vector2.inl
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/vector3.h
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/vector3.inl
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/version.h
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/cimport.h
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/importerdesc.h
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/Importer.hpp
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/DefaultLogger.hpp
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/ProgressHandler.hpp
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/IOStream.hpp
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/IOSystem.hpp
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/Logger.hpp
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/LogStream.hpp
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/NullLogger.hpp
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/cexport.h
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/Exporter.hpp
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/Compiler/pushpack1.h
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/Compiler/poppack1.h
4&gt;  -- Up-to-date: C:/Users/Leonard/SlicerIMSTK/Assimp-install/include/assimp/Compiler/pstdint.h
4&gt;  -- Installing: C:/Users/Leonard/SlicerIMSTK/Assimp-install/./lib/Slicer-4.13/assimp.pdb
4&gt;Completed 'Assimp'
17&gt;------ Build started: Project: iMSTK, Configuration: Debug x64 ------
17&gt;Performing configure step for 'iMSTK'
17&gt;loading initial cache file C:/Users/Leonard/SlicerIMSTK/iMSTK-prefix/tmp/iMSTK-cache-Debug.cmake
17&gt;-- Selecting Windows SDK version 10.0.19041.0 to target Windows 10.0.19043.
17&gt;-- Setting C++ standard
17&gt;-- Setting C++ standard - C++11
17&gt;-- iMSTK Audio support - OFF (iMSTK_ENABLE_AUDIO is SET)
17&gt;CMake Error at C:/Program Files/CMake/share/cmake-3.22/Modules/FindPackageHandleStandardArgs.cmake:230 (message):
17&gt;  Could NOT find g3log (missing: g3log_LIBRARIES)
17&gt;Call Stack (most recent call first):
17&gt;  C:/Program Files/CMake/share/cmake-3.22/Modules/FindPackageHandleStandardArgs.cmake:594 (_FPHSA_FAILURE_MESSAGE)
17&gt;  CMake/Utilities/imstkFind.cmake:199 (find_package_handle_standard_args)
17&gt;  CMake/Findg3log.cmake:14 (imstk_find_package)
17&gt;  CMakeLists.txt:301 (find_package)
17&gt;
17&gt;
17&gt;-- Configuring incomplete, errors occurred!
17&gt;See also "C:/Users/Leonard/SlicerIMSTK/imstk-build/CMakeFiles/CMakeOutput.log".
17&gt;C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(241,5): error MSB8066: Custom build for 'C:\Users\Leonard\SlicerIMSTK\CMakeFiles\00a65ebf7df0384334e0555dc84e73f1\iMSTK-configure.rule;C:\Users\Leonard\SlicerIMSTK\CMakeFiles\00a65ebf7df0384334e0555dc84e73f1\iMSTK-build.rule;C:\Users\Leonard\SlicerIMSTK\CMakeFiles\00a65ebf7df0384334e0555dc84e73f1\iMSTK-install.rule;C:\Users\Leonard\SlicerIMSTK\CMakeFiles\4cd7eb71559f6efa497210c55da60646\iMSTK-complete.rule;C:\Users\Leonard\SlicerIMSTK\CMakeFiles\511a6a1116940676e843c42da3309406\iMSTK.rule;C:\Users\Leonard\SlicerIMSTK\CMakeLists.txt' exited with code 1.
17&gt;Done building project "iMSTK.vcxproj" -- FAILED.
18&gt;------ Build started: Project: inner, Configuration: Debug x64 ------
18&gt;Performing configure step for 'inner'
18&gt;loading initial cache file C:/Users/Leonard/SlicerIMSTK/inner-prefix/tmp/inner-cache-Debug.cmake
18&gt;-- Selecting Windows SDK version 10.0.19041.0 to target Windows 10.0.19043.
18&gt;-- Trying to find DCMTK expecting DCMTKConfig.cmake
18&gt;-- Trying to find DCMTK expecting DCMTKConfig.cmake - ok
18&gt;-- Using previously found TBB::tbb
18&gt;-- Using previously found TBB::tbbmalloc
18&gt;-- Using previously found TBB::tbbmalloc_proxy
18&gt;-- Using previously found TBB::tbb
18&gt;-- Using previously found TBB::tbbmalloc
18&gt;-- Using previously found TBB::tbbmalloc_proxy
18&gt;-- Using previously found TBB::tbb
18&gt;-- Using previously found TBB::tbbmalloc
18&gt;-- Using previously found TBB::tbbmalloc_proxy
18&gt;-- RapidJSON found. Headers: ./include/Slicer-4.13
18&gt;-- Trying to find DCMTK expecting DCMTKConfig.cmake
18&gt;-- Trying to find DCMTK expecting DCMTKConfig.cmake - ok
18&gt;-- Configuring SlicerIMSTK with Qt 5.15.2 (using modules: Core, Widgets, Network, OpenGL, PrintSupport, UiTools, Xml, XmlPatterns, Svg, Sql, Multimedia, MultimediaWidgets, WebEngine, WebEngineWidgets, WebChannel, Script, Test, )
18&gt;-- Setting QT_PLUGINS_DIR: C:/Qt/5.15.2/msvc2019_64/plugins
18&gt;-- Setting QT_BINARY_DIR: C:/Qt/5.15.2/msvc2019_64/bin
18&gt;-- Checking EXTENSION_NAME variable
18&gt;-- Checking EXTENSION_NAME variable - NOTDEFINED
18&gt;-- Checking MODULE_NAME variable
18&gt;-- Checking MODULE_NAME variable - NOTDEFINED
18&gt;-- Checking PROJECT_NAME variable
18&gt;-- Checking PROJECT_NAME variable - SlicerIMSTK
18&gt;-- Setting EXTENSION_NAME ......................: SlicerIMSTK
18&gt;-- Adding ConfigureAdditionalLauncherSettings target
18&gt;-- Adding ConfigureAdditionalLauncherSettings target - yes (because configuring inner-build)
18&gt;-- Setting EXTENSION_SOURCE_DIR ................: C:/Users/Leonard/SlicerIMSTK
18&gt;-- Setting EXTENSION_SUPERBUILD_BINARY_DIR .....: C:/Users/Leonard/SlicerIMSTK
18&gt;-- Setting EXTENSION_BUILD_SUBDIRECTORY ........: inner-build
18&gt;-- Setting EXTENSION_DEPENDS ...................: NA
18&gt;-- Setting EXTENSION_BUILD_SUBDIRECTORY ........: inner-build
18&gt;-- Setting EXTENSION_HOMEPAGE ..................: http://slicer.org/slicerWiki/index.php/Documentation/Nightly/Extensions/S [...]
18&gt;-- Setting EXTENSION_CONTRIBUTORS ..............: Johan Andruejol (Kitware Inc.)
18&gt;-- Setting EXTENSION_CATEGORY ..................: Simulation
18&gt;-- Setting EXTENSION_ICONURL ...................: https://gitlab.kitware.com/iMSTK/iMSTK/blob/v1.0.0/Docs/source/media/logo [...]
18&gt;-- Setting EXTENSION_DESCRIPTION ...............: SlicerIMSTK provides Slicer with an interface to the iMSTK simulation lib [...]
18&gt;-- Setting EXTENSION_SCREENSHOTURLS ............: http://www.example.com/Slicer/Extensions/SlicerIMSTK/Screenshots/1.png
18&gt;-- Setting EXTENSION_ENABLED ...................: 1
18&gt;-- Setting EXTENSION_STATUS ....................: NOT DEFINED
18&gt;-- Setting default for EXTENSION_STATUS ........:
18&gt;CMake Error at iMSTK/CMakeLists.txt:24 (file):
18&gt;  file problem creating directory: C:/Program Files (x86)/SlicerIMSTK/bin
18&gt;
18&gt;
18&gt;CMake Error at iMSTK/CMakeLists.txt:25 (file):
18&gt;  file problem creating directory: C:/Program Files (x86)/SlicerIMSTK/include
18&gt;
18&gt;
18&gt;CMake Error at iMSTK/CMakeLists.txt:26 (file):
18&gt;  file problem creating directory: C:/Program Files (x86)/SlicerIMSTK/lib
18&gt;
18&gt;
18&gt;-- Setting C++ standard
18&gt;-- Setting C++ standard - C++11
18&gt;-- iMSTK Audio support - ON (default initialization)
18&gt;-- Found Python: C:/Program Files/WindowsApps/PythonSoftwareFoundation.Python.3.10_3.10.1520.0_x64__qbz5n2kfra8p0/python3.10.exe (found version "3.10.5") found components: Interpreter
18&gt;-- SuperBuild - First pass
18&gt;-- SuperBuild - First pass - done
18&gt;-- SuperBuild - iMSTK =&gt; Requires Uncrustify, Assimp, Eigen3, g3log, OpenVR, TBB, VegaFEM, VTK, SFML, GTest, iMSTKData,
18&gt;-- SuperBuild -   Uncrustify[OK]
18&gt;-- SuperBuild -   Assimp[OK]
18&gt;-- SuperBuild -   Eigen3[OK]
18&gt;-- SuperBuild -   g3log[OK]
18&gt;-- SuperBuild -   OpenVR[OK]
18&gt;-- SuperBuild -   TBB[OK]
18&gt;-- SuperBuild -   VegaFEM[OK]
18&gt;-- SuperBuild -   VTK =&gt; Requires OpenVR[INCLUDED],
18&gt;-- SuperBuild -   VTK[OK]
18&gt;-- SuperBuild -   SFML[OK]
18&gt;-- SuperBuild -   GTest[OK]
18&gt;-- SuperBuild -   iMSTKData[OK]
18&gt;-- SuperBuild - iMSTK[OK]
18&gt;-- Extension description has been written to: C:/Users/Leonard/SlicerIMSTK/SlicerIMSTK.s4ext
18&gt;-- Checking if extension type is SuperBuild
18&gt;-- Checking if extension type is SuperBuild - true
18&gt;-- Setting 'CTEST_MODEL' variable with default value 'Experimental'
18&gt;-- Setting 'SLICER_EXTENSION_MANAGER_CLIENT_EXECUTABLE' variable with default value 'SLICER_EXTENSION_MANAGER_CLIENT_EXECUTABLE-NOTDEFINED'
18&gt;-- Setting 'SLICER_EXTENSION_MANAGER_URL' variable with default value 'SLICER_EXTENSION_MANAGER_URL-NOTDEFINED'
18&gt;-- Setting 'SLICER_EXTENSION_MANAGER_API_KEY' variable with default value 'OBFUSCATED'
18&gt;-- Configuring incomplete, errors occurred!
18&gt;See also "C:/Users/Leonard/SlicerIMSTK/CMakeFiles/CMakeOutput.log".
18&gt;C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(241,5): error MSB8066: Custom build for 'C:\Users\Leonard\SlicerIMSTK\CMakeFiles\ff5507f875e6d32e3f7224609425b2e6\inner-configure.rule;C:\Users\Leonard\SlicerIMSTK\CMakeFiles\ff5507f875e6d32e3f7224609425b2e6\inner-build.rule;C:\Users\Leonard\SlicerIMSTK\CMakeFiles\ff5507f875e6d32e3f7224609425b2e6\inner-forceconfigure.rule;C:\Users\Leonard\SlicerIMSTK\CMakeFiles\ff5507f875e6d32e3f7224609425b2e6\inner-install.rule;C:\Users\Leonard\SlicerIMSTK\CMakeFiles\4cd7eb71559f6efa497210c55da60646\inner-complete.rule;C:\Users\Leonard\SlicerIMSTK\CMakeFiles\511a6a1116940676e843c42da3309406\inner.rule;C:\Users\Leonard\SlicerIMSTK\CMakeLists.txt' exited with code 1.
18&gt;Done building project "inner.vcxproj" -- FAILED.
19&gt;------ Build started: Project: ALL_BUILD, Configuration: Debug x64 ------
19&gt;Building Custom Rule C:/Users/Leonard/SlicerIMSTK/CMakeLists.txt
20&gt;------ Skipped Build: Project: PACKAGE, Configuration: Debug x64 ------
20&gt;Project not selected to build for this solution configuration 
========== Build: 10 succeeded, 4 failed, 0 up-to-date, 6 skipped ==========

</code></pre>
<p>I have tried  the steps recommended in the FAQs as well just to check that this was not the problem at hand and it did not seem to be resolving the issue. I am looking forward to your reply and thanks again.</p>

---

## Post #7 by @Sam_Horvath (2022-07-21 20:04 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> Do these error look familiar to you for the standalone build?</p>
<p><a class="mention" href="/u/leo">@leo</a> So, I would not recommend building in Debug, IMSTK doesn’t support that very well.  What version of CMake are you using?</p>

---

## Post #8 by @siqueirl (2022-07-22 14:34 UTC)

<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> I’m working with <a class="mention" href="/u/leo">@leo</a> on this issue, so I’ll answer on his behalf for now. We have tried building in both Debug and Release. We’re using CMake 3.22.1.</p>
<p>If I may ask another question: does SlicerIMSTK require specific versions of Slicer, Qt, VTK, or other dependencies? Is building standalone IMSTK required?</p>
<p>Thank you!</p>

---

## Post #9 by @Sam_Horvath (2022-07-22 14:47 UTC)

<p>So, SlicerIMSTK should be built against a current/recent Slicer preview (we are actively developing this module for internal projects, so it is in a rather constant state of change).  In our current usage of the module, we are bundling in into a custom application based on this commit of Slicer:</p><aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/Slicer/commit/177f3b324247de4e77d4497cc9121fe37dd5b3f3">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/commit/177f3b324247de4e77d4497cc9121fe37dd5b3f3" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/commit/177f3b324247de4e77d4497cc9121fe37dd5b3f3" target="_blank" rel="noopener">COMP: Update slicerInstallLibrary to ensure tbb debug libs are not packaged</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2022-06-02" data-time="02:31:35" data-timezone="UTC">02:31AM - 02 Jun 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener">
          <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>

      <div class="lines" title="changed 1 files with 1 additions and 0 deletions">
        <a href="https://github.com/Slicer/Slicer/commit/177f3b324247de4e77d4497cc9121fe37dd5b3f3" target="_blank" rel="noopener">
          <span class="added">+1</span>
          <span class="removed">-0</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This commit ensure libraries filename with suffix "_debug" are not
packaged.</p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The extension handles building IMSTK, so you do not need to build it yourself.  The Slicer version handles Qt/VTK versions.</p>

---

## Post #10 by @siqueirl (2022-07-22 15:30 UTC)

<p>Thank you for your quick reply. I will retry building it with this commit, but I will have to leave Slicer build running overnight today, as it takes me 4+ hours. When building Slicer, Cmake has an option to do it with VTK 8 or 9, does that make a difference? When attempting to build SlicerIMSTK, there is a notice that VTK 8.9+ is required.</p>

---

## Post #11 by @Sam_Horvath (2022-07-22 15:35 UTC)

<p>Use VTK 9, that is currently most supported for Slicer / IMSTK.</p>

---

## Post #12 by @siqueirl (2022-07-25 15:26 UTC)

<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> Thank you for these instructions. Building this commit failed, although I followed the same steps that have been resulting on successful builds (Release and Debug) for Slicer 4.13.0-2021-09-12. Is there an optimal way to share the errors? I have 10 CMakeError.log files inside my S4R folder.</p>

---

## Post #13 by @Sam_Horvath (2022-07-25 16:04 UTC)

<p>You could copy/paste the errors into a reply here, or you could upload the files somewhere and link them.</p>
<p>One question, did you build the new commit as a clean build or an incremental build on top of a previous one?</p>

---

## Post #14 by @siqueirl (2022-07-26 10:03 UTC)

<p>Thank you for your reply. The failed Slicer build was a clean one. It was an attempt using this command:</p>
<pre><code class="lang-auto">"C:\Program Files\CMake\bin\cmake.exe" --build . --config Release
</code></pre>
<p>On my last attempt, I cleaned the cache, manually deleted S4R’s contents, and tried building it using Visual Studio. This time, I got Slicer to build and produce a working Slicer.exe despite Visual Studio 2019 showing one error, although several CMakeError.log files were produced.</p>
<p>I tried building SlicerIMSTK against this Slicer version based on the commit you suggested, but I still had many errors in Visual Studio 2019. I organized all the CMakeError.log files from both Slicer and the extension here:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://wetransfer.com/downloads/95456898452d8a64b1d0c58c3d96cf7020220726095934/78a2e5">
  <header class="source">
      <img src="https://prod-cdn.wetransfer.net/packs/media/images/favicon-a34a7465.ico" class="site-icon" width="64" height="64">

      <a href="https://wetransfer.com/downloads/95456898452d8a64b1d0c58c3d96cf7020220726095934/78a2e5" target="_blank" rel="noopener nofollow ugc">wetransfer.com</a>
  </header>

  <article class="onebox-body">
    <img src="https://prod-cdn.wetransfer.net/packs/media/images/wt-facebook-9db47080.png" class="thumbnail onebox-avatar" width="200" height="200">

<h3><a href="https://wetransfer.com/downloads/95456898452d8a64b1d0c58c3d96cf7020220726095934/78a2e5" target="_blank" rel="noopener nofollow ugc">CMakeError.zip</a></h3>

  <p>1 file sent via WeTransfer, the simplest way to send your files around the world</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Thank you again for your support!</p>

---

## Post #15 by @Sam_Horvath (2022-07-26 14:29 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a>, looking at the errors for SlicerIMSTK, most seem to be related to pthread - wasn’t this removed from the IMSTK build?</p>
<pre><code class="lang-auto">C:\D\SE\SlicerIMSTKR\vtkRenderingOpenVR-build\CMakeFiles\CMakeTmp\CheckIncludeFile.c(1,10): fatal error C1083: Cannot open include file: 'pthread.h': No such file or directory [C:\D\SE\SlicerIMSTKR\vtkRenderingOpenVR-build\CMakeFiles\CMakeTmp\cmTC_2ea46.vcxproj]
</code></pre>

---

## Post #16 by @siqueirl (2022-07-29 18:35 UTC)

<p>Thank you for your analysis. I don’t know much about pthread, but from what I understood, it should not be on Windows. I tried setting these on different CMakeLists, but it didn’t change a thing:</p>
<p><code>CMAKE_HAVE_PTHREAD_H:INTERNAL=0 FIND_PACKAGE_MESSAGE_DETAILS_Threads:INTERNAL=[FALSE][v()]  set(THREADS_PREFER_PTHREAD_FLAG OFF)</code></p>
<p>Should I try making pthread available to Windows instead? Thank you.</p>

---

## Post #17 by @jcfr (2022-07-29 19:09 UTC)

<p>To help move forward with this, I initiated a build of <code>SlicerIMSTK</code> (commit <a href="https://github.com/KitwareMedical/SlicerIMSTK/commit/897ab3175ba0fc5275ea4f47e4bdacad99aac7de">SlicerIMSTK@897ab3175</a>) against the Slicer build tree associated with the latest release <sup class="footnote-ref"><a href="#footnote-81488-1" id="footnote-ref-81488-1">[1]</a></sup>.</p>
<p><a class="mention" href="/u/siqueirl">@siqueirl</a> While I am aware that you are using <code>Visual Studio 2019</code>, could you still compare the output you got with tone I shared below ? More specifically, I am curious about the output associated with <code>Looking for pthread.h</code> and <code>Found Threads</code></p>
<p>The following command was used:</p>
<pre><code class="lang-auto">C:\cmake-3.22.1\bin\cmake.exe ^
  -G "Visual Studio 17 2022" ^
  -A x64 ^
  -T v143
  -DSlicer_DIR:PATH=D:\D\S\S-0-build\Slicer-build ^
  ..\SlicerIMSTK
</code></pre>
<details>
<summary>
Click to see configuration output</summary>
<p>– Selecting Windows SDK version 10.0.22000.0 to target Windows 10.0.19044.<br>
– The C compiler identification is MSVC 19.30.30709.0<br>
– The CXX compiler identification is MSVC 19.30.30709.0<br>
– Detecting C compiler ABI info<br>
– Detecting C compiler ABI info - done<br>
– Check for working C compiler: C:/Program Files/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC/14.30.30705/bin/Hostx64/x64/cl.exe - skipped<br>
– Detecting C compile features<br>
– Detecting C compile features - done<br>
– Detecting CXX compiler ABI info<br>
– Detecting CXX compiler ABI info - done<br>
– Check for working CXX compiler: C:/Program Files/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC/14.30.30705/bin/Hostx64/x64/cl.exe - skipped<br>
– Detecting CXX compile features<br>
– Detecting CXX compile features - done<br>
– Looking for pthread.h<br>
– Looking for pthread.h - not found<br>
– Found Threads: TRUE<br>
– Found OpenGL: opengl32  found components: OpenGL<br>
– Found Python3: D:/D/S/S-0-build/python-install/bin/PythonSlicer.exe (found suitable version “3.9.10”, minimum required is “3.9”) found components: Interpreter Development.Module Development.Embed<br>
– Found PythonLibs: D:/D/S/S-0-build/python-install/libs/python39.lib (found version “3.9.10”)<br>
– Trying to find DCMTK expecting DCMTKConfig.cmake<br>
– Trying to find DCMTK expecting DCMTKConfig.cmake - ok<br>
– Found CURL: D:/D/S/S-0-build/curl-install/lib/libcurl.lib (found version “7.70.0-DEV”)<br>
– RapidJSON found. Headers: ./include/Slicer-5.0<br>
– Trying to find DCMTK expecting DCMTKConfig.cmake<br>
– Trying to find DCMTK expecting DCMTKConfig.cmake - ok<br>
– Found PythonInterp: D:/D/S/S-0-build/python-install/bin/PythonSlicer.exe (found version “3.9.10”)<br>
– Found SWIG: D:/D/S/S-0-build/swigwin-4.0.2/swig.exe (found version “4.0.2”)<br>
– Configuring SlicerIMSTK with Qt 5.15.2 (using modules: Core, Widgets, Network, OpenGL, PrintSupport, UiTools, Xml, XmlPatterns, Svg, Sql, Multimedia, MultimediaWidgets, WebEngine, WebEngineWidgets, WebChannel, Script, LinguistTools, Test, )<br>
– Setting QT_PLUGINS_DIR: D:/Support/Qt2/5.15.2/msvc2019_64/plugins<br>
– Setting QT_BINARY_DIR: D:/Support/Qt2/5.15.2/msvc2019_64/bin<br>
– Setting QT_LIBRARY_DIR: D:/Support/Qt2/5.15.2/msvc2019_64/lib<br>
– Checking EXTENSION_NAME variable<br>
– Checking EXTENSION_NAME variable - NOTDEFINED<br>
– Checking MODULE_NAME variable<br>
– Checking MODULE_NAME variable - NOTDEFINED<br>
– Checking PROJECT_NAME variable<br>
– Checking PROJECT_NAME variable - SlicerIMSTK<br>
– Setting EXTENSION_NAME …: SlicerIMSTK<br>
– ITK is setting SlicerIMSTK’s MSVC_RUNTIME_LIBRARY to dynamic<br>
– Checking to see if CXX compiler accepts flag -features=no%anachronisms<br>
– Checking to see if CXX compiler accepts flag -features=no%anachronisms - No<br>
– Adding ConfigureAdditionalLauncherSettings target<br>
– Adding ConfigureAdditionalLauncherSettings target - no (because configuring top-level project)<br>
– Setting EXTENSION_SOURCE_DIR …: D:/T/SlicerIMSTK<br>
– Setting EXTENSION_SUPERBUILD_BINARY_DIR …: D:/T/SlicerIMSTK-Release<br>
– Setting EXTENSION_BUILD_SUBDIRECTORY …: inner-build<br>
– Setting EXTENSION_DEPENDS …: NA<br>
– Setting EXTENSION_BUILD_SUBDIRECTORY …: inner-build<br>
– Setting EXTENSION_HOMEPAGE …: <a href="http://slicer.org/slicerWiki/index.php/Documentation/Nightly/Extensions/S">http://slicer.org/slicerWiki/index.php/Documentation/Nightly/Extensions/S</a> […]<br>
– Setting EXTENSION_CONTRIBUTORS …: Johan Andruejol (Kitware Inc.)<br>
– Setting EXTENSION_CATEGORY …: Simulation<br>
– Setting EXTENSION_ICONURL …: <a href="https://gitlab.kitware.com/iMSTK/iMSTK/blob/v1.0.0/Docs/source/media/logo" class="inline-onebox">Files · v1.0.0 · iMSTK / iMSTK · GitLab</a> […]<br>
– Setting EXTENSION_DESCRIPTION …: SlicerIMSTK provides Slicer with an interface to the iMSTK simulation lib […]<br>
– Setting EXTENSION_SCREENSHOTURLS …: <a href="http://www.example.com/Slicer/Extensions/SlicerIMSTK/Screenshots/1.png">http://www.example.com/Slicer/Extensions/SlicerIMSTK/Screenshots/1.png</a><br>
– Setting EXTENSION_ENABLED …: 1<br>
– Setting EXTENSION_STATUS …: NOT DEFINED<br>
– Setting default for EXTENSION_STATUS …:<br>
– Found Git: C:/Users/svc-dashboard/AppData/Local/Programs/Git/cmd/git.exe<br>
– SlicerIMSTK_BUILD_ViewerVTK is not defined. Defaulting to ‘ON’<br>
– SlicerIMSTK_EXTERNAL_PROJECT_DEPENDENCIES:iMSTK;vtkRenderingOpenVR<br>
– Remote - iMSTK [OK]<br>
– Remote - iMSTK_SOURCE_DIR:D:/T/SlicerIMSTK-Release/iMSTK<br>
– Remote - VTKExternalModule [OK]<br>
– Remote - VTKExternalModule_SOURCE_DIR:D:/T/SlicerIMSTK-Release/VTKExternalModule<br>
– SuperBuild - First pass<br>
– SuperBuild - First pass - done<br>
– SuperBuild - inner =&gt; Requires iMSTK, vtkRenderingOpenVR,<br>
– SuperBuild -   iMSTK =&gt; Requires Assimp, Eigen3, g3log, Libusb, VegaFEM, OpenVR, vtkRenderingExternal, vtkRenderingOpenVR,<br>
– SuperBuild -     Assimp[OK]<br>
– SuperBuild -     Assimp_ROOT_DIR:D:/T/SlicerIMSTK-Release/Assimp-install<br>
– SuperBuild -     Assimp_LIB_DIR:./lib/Slicer-5.0<br>
– SuperBuild -     Eigen3[OK]<br>
– SuperBuild -     Eigen3_DIR:D:/T/SlicerIMSTK-Release/Eigen3-install/share/eigen3/cmake<br>
– SuperBuild -     g3log[OK]<br>
– SuperBuild -     g3log_ROOT_DIR:D:/T/SlicerIMSTK-Release/g3log-install<br>
– SuperBuild -     g3log_LIB_DIR:lib<br>
– SuperBuild -     Libusb[OK]<br>
– SuperBuild -     Libusb_ROOT_DIR:D:/T/SlicerIMSTK-Release/Libusb-install<br>
– SuperBuild -     Libusb_LIB_DIR:lib<br>
– SuperBuild -     VegaFEM[OK]<br>
– SuperBuild -     VegaFEM_DIR:D:/T/SlicerIMSTK-Release/VegaFEM-install/lib/cmake/VegaFEM<br>
– SuperBuild -     OpenVR[OK]<br>
– SuperBuild -     OpenVR_INCLUDE_DIR:D:/T/SlicerIMSTK-Release/OpenVR/headers<br>
– SuperBuild -     OpenVR_LIBRARY:D:/T/SlicerIMSTK-Release/OpenVR/lib/win64/openvr_api.lib<br>
– SuperBuild -     OpenVR_ROOT_DIR:D:/T/SlicerIMSTK-Release/OpenVR<br>
– SuperBuild -     OpenVR_LIB_DIR:lib/win64<br>
– SuperBuild -     OpenVR_INC_DIR:headers<br>
– SuperBuild -     vtkRenderingExternal[OK]<br>
– SuperBuild -     VTK_SOURCE_DIR:D:/D/S/S-0-build/VTK-build/…/VTK<br>
– SuperBuild -     vtkRenderingExternal_DIR:D:/T/SlicerIMSTK-Release/vtkRenderingExternal-build<br>
– SuperBuild -     vtkRenderingOpenVR =&gt; Requires OpenVR[INCLUDED], vtkRenderingVR,<br>
– SuperBuild -       vtkRenderingVR[OK]<br>
– SuperBuild -       VTK_SOURCE_DIR:D:/D/S/S-0-build/VTK-build/…/VTK<br>
– SuperBuild -       vtkRenderingVR_DIR:D:/T/SlicerIMSTK-Release/vtkRenderingVR-build<br>
– SuperBuild -     vtkRenderingOpenVR[OK]<br>
– SuperBuild -     VTK_SOURCE_DIR:D:/D/S/S-0-build/VTK-build/…/VTK<br>
– SuperBuild -     vtkRenderingOpenVR_DIR:D:/T/SlicerIMSTK-Release/vtkRenderingOpenVR-build<br>
– SuperBuild -   iMSTK[OK]<br>
– SuperBuild -   iMSTK[vtkRenderingExternal:ON]<br>
– SuperBuild -   iMSTK[vtkRenderingOpenVR:ON]<br>
– SuperBuild - inner[OK]<br>
– Configuring done<br>
– Generating done<br>
– Build files have been written to: D:/T/SlicerIMSTK-Release</p>
</details>
<hr class="footnotes-sep">

<ol class="footnotes-list">
<li id="footnote-81488-1" class="footnote-item">
<p>The latest release build tree was used because last night nightly failed. See <a href="https://slicer.cdash.org/viewBuildError.php?type=0&amp;buildid=2755183" class="inline-onebox">CDash</a> <a href="#footnote-ref-81488-1" class="footnote-backref">↩︎</a></p>
</li>
</ol>

---

## Post #18 by @jcfr (2022-07-29 19:48 UTC)

<p>After configuring using the command-line report above, I was then able to built the extension using the following command executed within a regular windows command line terminal from the directory <code>D:\T\SlicerIMSTK-Release</code>:</p>
<pre><code class="lang-auto">C:\cmake-3.22.1\bin\cmake.exe --build . --config Release -- /maxcpucount:4
</code></pre>

---

## Post #19 by @jcfr (2022-07-29 20:02 UTC)

<aside class="quote no-group" data-username="Sam_Horvath" data-post="15" data-topic="24332">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sam_horvath/48/3092_2.png" class="avatar"> Sam_Horvath:</div>
<blockquote>
<pre><code class="lang-auto">C:\D\SE\SlicerIMSTKR\vtkRenderingOpenVR-build\CMakeFiles\CMakeTmp\CheckIncludeFile.c(1,10): fatal error C1083: Cannot open include file: 'pthread.h': No such file or directory [C:\D\SE\SlicerIMSTKR\vtkRenderingOpenVR-build\CMakeFiles\CMakeTmp\cmTC_2ea46.vcxproj]
</code></pre>
</blockquote>
</aside>
<p>This message is expected, it is one of the result of the system introspection tests performed during configuration. This message was reported while attempting to check if the <code>pthread.h</code> header is available on the system. As expected on Windows using Visual Studio, it indicates it is not available.</p>
<p>Now reading the posts (especially <a href="https://discourse.slicer.org/t/loadable-module-to-integrate-a-haptic-device/24332/6" class="inline-onebox">loadable module to integrate a haptic device  - #6 by leo</a>), I am not able to clearly understand what is the actual error. Considering that Visual Studio parallelized the build, I suspect it was displayed earlier in the log.</p>
<p>To move forward, it would be great to provide:</p>
<ul>
<li>Version of <code>Slicer</code> and <code>SlicerIMSTK</code> used</li>
<li>Commands used to configure and build <code>Slicer</code>  and <code>SlicerIMSTK</code> (e.g is it a Release or Debug) build</li>
<li>Configuration or build error(s) reported</li>
</ul>
<p>I suggest the following use at least Slicer <code>v5.0.3</code>. Once we sort out the issue reported on the Dashboard (link above as well as <a href="https://discourse.slicer.org/t/windows-preview-build-failing-yesterday-and-today/24567" class="inline-onebox">Windows preview build failing yesterday and today</a>), using the latest version would be sensible too.</p>

---

## Post #20 by @siqueirl (2022-08-01 15:23 UTC)

<p>Thank you for your analysis and help!</p>
<p>I just managed to get back to my lab and try what you have suggested. I have finally managed to build SlicerIMSTK Release (897ab31)  against Slicer 5.1.0-2022-06-17 Release using Visual Studio 2019. I configured using CMake GUI (3.23.3) and built it using <code>cmake  --build . --config Release</code>. This was my output:</p>
<p>I uploaded the output and cmake files here as they were too large to paste: <a href="https://we.tl/t-qQ1TGLkPtz" class="inline-onebox" rel="noopener nofollow ugc">WeTransfer - Send Large Files &amp; Share Photos Online - Up to 2GB Free</a></p>
<p>Oddly enough, I still get many pthread.h - not found on my output, but this time inner-build had SlicerWithSlicerIMSTK.exe launching.</p>
<p>So far, I haven’t managed to get a haptic response and Slicer crashes after I hit the Stop Haptics demo, but I still have a lot to try before asking more questions as at least now that the extension is running.</p>
<p>Please let me know if I should share any Cmake or output files to help you understand what the errors possibly were. Thank you again.</p>

---
