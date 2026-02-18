# No ExperimentalUpload target when building extension index

**Topic ID**: 1818
**Date**: 2018-01-11
**URL**: https://discourse.slicer.org/t/no-experimentalupload-target-when-building-extension-index/1818

---

## Post #1 by @gregsharp.geo (2018-01-11 22:00 UTC)

<p>Hi, I am trying to upload the extension using the method here:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_ExtensionsIndex" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_ExtensionsIndex</a></p>
<p>But I don’t get a target for ExperimentalUpload.  Is the documentation up to date?  Below is what I got.</p>
<p>Thanks,<br>
Greg</p>
<pre><code class="lang-auto">-- Found PythonLibs: C:/S64/python-install/libs/python27.lib (found version "2.7.13")
-- Trying to find DCMTK expecting DCMTKConfig.cmake
-- Trying to find DCMTK expecting DCMTKConfig.cmake - ok
-- Found Qt4: C:/Qt/4.8.7/qt-4.8.7-64-vs2013-rel/bin/qmake.exe (found version "4.8.7")
-- RapidJSON found. Headers: ./include/Slicer-4.9
-- Trying to find DCMTK expecting DCMTKConfig.cmake
-- Trying to find DCMTK expecting DCMTKConfig.cmake - ok
-- Found PythonLibs: C:/S64/python-install/libs/python27.lib
-- Found Qt4: C:/Qt/4.8.7/qt-4.8.7-64-vs2013-rel/bin/qmake.exe (found version "4.8.7")
-- Configuring CUDAProbe with Qt 4.8.7 (using modules: QTCORE, QTGUI, QTNETWORK, QTOPENGL, QTUITOOLS, QTXML, QTXMLPATTERNS, QTWEBKIT, QTSVG, QTSQL, PHONON, QTSCRIPT, )
-- Checking EXTENSION_NAME variable
-- Checking EXTENSION_NAME variable - NOTDEFINED
-- Checking MODULE_NAME variable
-- Checking MODULE_NAME variable - NOTDEFINED
-- Checking PROJECT_NAME variable
-- Checking PROJECT_NAME variable - CUDAProbe
-- Setting EXTENSION_NAME ......................: CUDAProbe
-- Adding ConfigureAdditionalLauncherSettings target
-- Adding ConfigureAdditionalLauncherSettings target - yes
-- Setting EXTENSION_SOURCE_DIR ................: C:/gcs6/build/slicer-4/ExtensionsIndex-build/Slicer-CUDAProbe
-- Setting EXTENSION_SUPERBUILD_BINARY_DIR .....: C:/gcs6/build/slicer-4/ExtensionsIndex-build/Slicer-CUDAProbe-build
-- Setting EXTENSION_BUILD_SUBDIRECTORY ........: .
-- Setting MIDAS_PACKAGE_URL ...................: http://slicer.kitware.com/midas3
-- Setting MIDAS_PACKAGE_EMAIL .................: OBFUSCATED
-- Setting MIDAS_PACKAGE_API_KEY ...............: OBFUSCATED
-- Setting EXTENSION_SVNUSERNAME ...............: NOT DEFINED
-- Setting EXTENSION_SVNPASSWORD ...............: NOT DEFINED
-- Setting EXTENSION_DEPENDS ...................: NA
-- Setting EXTENSION_BUILD_SUBDIRECTORY ........: .
-- Setting EXTENSION_HOMEPAGE ..................: http://slicer.org/slicerWiki/index.php/Documentation/Nightly/Extensions/C [...]
-- Setting EXTENSION_CONTRIBUTORS ..............: Gregory Sharp (Massachusetts General Hospital)
-- Setting EXTENSION_CATEGORY ..................: Utilities
-- Setting EXTENSION_ICONURL ...................: http://www.example.com/Slicer/Extensions/CUDAProbe.png
-- Setting EXTENSION_DESCRIPTION ...............: This extension queries your computer for its CUDA capabilities.
-- Setting EXTENSION_SCREENSHOTURLS ............: http://www.example.com/Slicer/Extensions/CUDAProbe/Screenshots/1.png
-- Setting EXTENSION_ENABLED ...................: 1
-- Setting EXTENSION_STATUS ....................: NOT DEFINED
-- Setting default for EXTENSION_STATUS ........:
-- CUDA Version 8.0
-- CUDA Build Level: Build system Compute Capability ONLY!
-- Configuring SEM CLI module: CUDAProbe
-- Extension description has been written to: C:/gcs6/build/slicer-4/ExtensionsIndex-build/Slicer-CUDAProbe-build/CUDAProbe.s4ext
-- Checking if extension type is SuperBuild
-- Checking if extension type is SuperBuild - false
-- Configuring done
-- Generating done
CMake Warning:
  Manually-specified variables were not used by the project:

    Slicer_UPLOAD_EXTENSIONS


-- Build files have been written to: C:/gcs6/build/slicer-4/ExtensionsIndex-build/Slicer-CUDAProbe-build
</code></pre>

---

## Post #2 by @jcfr (2018-01-12 03:41 UTC)

<p>Hi Greg,</p>
<p>Support for use of <code>ExperimentalUpload</code> has been removed when we simplified the extension build system.</p>
<p>The wiki page has been updated accordingly.</p>

---

## Post #3 by @gregsharp.geo (2018-01-12 13:41 UTC)

<p>This works great now.  Thanks!</p>

---
