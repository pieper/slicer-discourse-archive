---
topic_id: 2557
title: "Cant Build Slicer Ctk Component Mac 10 12 Qt 5 9"
date: 2018-04-10
url: https://discourse.slicer.org/t/2557
---

# Can't build Slicer CTK component (Mac 10.12, Qt 5.9)

**Topic ID**: 2557
**Date**: 2018-04-10
**URL**: https://discourse.slicer.org/t/cant-build-slicer-ctk-component-mac-10-12-qt-5-9/2557

---

## Post #1 by @mschumaker (2018-04-10 15:14 UTC)

<p>I’m currently unable to build the newest master branch Slicer. It’s failing at the CTK target. I can see in my CMake configuration that the value of Qt5Network_DIR is defined, but when Xcode attempts to build the CTK target within the CTK project, I get an error message that Qt5NetworkConfig.cmake can’t be found. How can I fix or work around this? Thanks.</p>
<pre><code>=== BUILD AGGREGATE TARGET CTK OF PROJECT CTK WITH CONFIGURATION Debug ===

Check dependencies

Write auxiliary files
write-file /Users/michaelschumaker/Packages/Slicer-SuperBuild/CTK-build/CTK.build/Debug/CTK.build/Script-7681B4976ADF47A3822956B5.sh
chmod 0755 /Users/michaelschumaker/Packages/Slicer-SuperBuild/CTK-build/CTK.build/Debug/CTK.build/Script-7681B4976ADF47A3822956B5.sh

PhaseScriptExecution CMake\ Rules /Users/michaelschumaker/Packages/Slicer-SuperBuild/CTK-build/CTK.build/Debug/CTK.build/Script-7681B4976ADF47A3822956B5.sh
    cd /Users/michaelschumaker/Packages/Slicer-SuperBuild/CTK
    /bin/sh -c /Users/michaelschumaker/Packages/Slicer-SuperBuild/CTK-build/CTK.build/Debug/CTK.build/Script-7681B4976ADF47A3822956B5.sh
echo "Performing configure step for 'CTK'"
Performing configure step for 'CTK'
cd /Users/michaelschumaker/Packages/Slicer-SuperBuild/CTK-build/CTK-build &amp;&amp; /Applications/CMake.app/Contents/bin/cmake -C/Users/michaelschumaker/Packages/Slicer-SuperBuild/CTK-build/CTK-prefix/tmp/CTK-cache-Debug.cmake -GXcode /Users/michaelschumaker/Packages/Slicer-SuperBuild/CTK
loading initial cache file /Users/michaelschumaker/Packages/Slicer-SuperBuild/CTK-build/CTK-prefix/tmp/CTK-cache-Debug.cmake
CMake Error at /Users/michaelschumaker/Qt/5.9/Src/qtxmlpatterns/lib/cmake/Qt5XmlPatterns/Qt5XmlPatternsConfig.cmake:83 (find_package):
  Could not find a package configuration file provided by "Qt5Network"
  (requested version 5.9.0) with any of the following names:

    Qt5NetworkConfig.cmake
    qt5network-config.cmake

  Add the installation prefix of "Qt5Network" to CMAKE_PREFIX_PATH or set
  "Qt5Network_DIR" to a directory containing one of the above files.  If
  "Qt5Network" provides a separate development package or SDK, be sure it has
  been installed.
Call Stack (most recent call first):
  /Users/michaelschumaker/Qt/5.9/Src/qtbase/lib/cmake/Qt5/Qt5Config.cmake:28 (find_package)
  CMake/ctkMacroSetupQt.cmake:50 (find_package)
  CMakeLists.txt:421 (ctkMacroSetupQt)


-- Configuring incomplete, errors occurred!
See also "/Users/michaelschumaker/Packages/Slicer-SuperBuild/CTK-build/CTK-build/CMakeFiles/CMakeOutput.log".
make[1]: *** [/Users/michaelschumaker/Packages/Slicer-SuperBuild/CTK-build/CTK-prefix/src/CTK-stamp/Debug/CTK-configure] Error 1
Command /bin/sh failed with exit code 2</code></pre>

---

## Post #2 by @ihnorton (2018-04-10 15:41 UTC)

<p>A post was merged into an existing topic: <a href="/t/build-failing-in-python-related-targets-on-macos-10-12-slicer-nightly-vtk-nightly-qt-5-9/2551">Build failing in python-related targets on MacOS 10.12, Slicer nightly, VTK nightly, Qt 5.9</a></p>

---

## Post #3 by @ihnorton (2018-04-10 15:41 UTC)



---

## Post #4 by @ihnorton (2018-04-10 15:43 UTC)



---
