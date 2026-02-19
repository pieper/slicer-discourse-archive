---
topic_id: 5440
title: "How To Get Slicerrt Runing On My Developer Installation"
date: 2019-01-21
url: https://discourse.slicer.org/t/5440
---

# How to get SlicerRT runing on my Developer Installation?

**Topic ID**: 5440
**Date**: 2019-01-21
**URL**: https://discourse.slicer.org/t/how-to-get-slicerrt-runing-on-my-developer-installation/5440

---

## Post #1 by @MachadoL (2019-01-21 12:55 UTC)

<p>Operating system: Linux<br>
Slicer version: Slicer 4.9</p>
<p>Hi Everyone,</p>
<p>I’d like to know how to install SlicerRT from source (GitHub) into my home Developer Installation.</p>
<p>Thank you all!</p>

---

## Post #2 by @Alex_Vergara (2019-01-21 15:15 UTC)

<p>Slicer stable is 4.10 and development is 4.11. Please do git pull.</p>

---

## Post #3 by @lassoan (2019-01-21 15:31 UTC)

<aside class="quote no-group" data-username="MachadoL" data-post="1" data-topic="5440">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/machadol/48/3372_2.png" class="avatar"> MachadoL:</div>
<blockquote>
<p>how to install SlicerRT from source</p>
</blockquote>
</aside>
<p>First you need to build from source (configure using CMake and build).</p>
<p>After that you can start Slicer and add SlicerRT module paths to additional module path in Slicer application settings. Alternatively, you can package SlicerRT extension (by building the PACKAGE target) and install the <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/ExtensionsManager#Installing_an_extension_without_network_connection">extension package</a>.</p>

---

## Post #4 by @MachadoL (2019-01-21 18:40 UTC)

<p>Thank you, Andras<br>
Similarly as we do with CLI modules?<br>
I’ll try it now!</p>

---

## Post #5 by @lassoan (2019-01-22 02:34 UTC)

<p>SlicerRT contains both CLI, loadable, and scripted modules. They are located in inner-build\lib\Slicer-4.11 subfolder of the build tree.</p>

---

## Post #6 by @MachadoL (2019-01-22 20:08 UTC)

<p>Lasso,</p>
<p>I am having a huge problem when trying to compile SlicerRT from source.And I guess it is related to my local configurations.<br>
I do load source and build directories inside CMake, then configure and generate.<br>
But when i gor for make, it craches with the following error:</p>
<pre><code>CMake Error at SuperBuild/External_Plastimatch.cmake:46 (ExternalProject_Add):
Unknown CMake command "ExternalProject_Add".
Call Stack (most recent call first):
 /home/leonardo/General_Sources/Slicer/CMake/ExternalProjectDependency.cmake:752 (include)
/home/leonardo/General_Sources/Slicer/CMake/ExternalProjectDependency.cmake:815 
(ExternalProject_Include_Dependencies)
SuperBuild.cmake:24 (ExternalProject_Include_Dependencies)
CMakeLists.txt:43 (include)


-- Configuring incomplete, errors occurred!
See also "/home/leonardo/Desktop/Modulos-Source/Modulos_to_Slicer/SlicerRT/Build/CMakeFiles/CMakeOutput.log".
See also "/home/leonardo/Desktop/Modulos-Source/Modulos_to_Slicer/SlicerRT/Build/CMakeFiles/CMakeError.log".
Makefile:564: recipe for target 'cmake_check_build_system' failed
make: *** [cmake_check_build_system] Error 1
</code></pre>
<p>The address</p>
<pre><code>  /home/leonardo/General_Sources/Slicer/CMake/ExternalProjectDependency.cmake:752 (include)
</code></pre>
<p>reffers to an old Slicer installation (4.9).</p>
<p>As well as the first files loaded in the beggining of make step:</p>
<pre><code>-- Found PythonLibs: /usr/local/Slicer/python-install/lib/libpython2.7.so (found version "2.7.13") 
-- Trying to find DCMTK expecting DCMTKConfig.cmake
-- Trying to find DCMTK expecting DCMTKConfig.cmake - ok
-- Found Qt4: /usr/bin/qmake (found version "4.8.7") 
-- RapidJSON found. Headers: ./include/Slicer-4.9
-- Trying to find DCMTK expecting DCMTKConfig.cmake
-- Trying to find DCMTK expecting DCMTKConfig.cmake - ok
-- Found PythonLibs: /usr/local/Slicer/python-install/lib/libpython2.7.so  
-- Found Qt4: /usr/bin/qmake (found version "4.8.7") 
-- Configuring SlicerRT with Qt 4.8.7 (using modules: QTCORE, QTGUI, QTNETWORK, QTOPENGL, QTUITOOLS, QTXML, QTXMLPATTERNS, QTWEBKIT, QTSVG, QTSQL, QTSCRIPT, QTTEST, )
</code></pre>
<p>I’d appreciate any help!</p>
<p>Thanks.</p>

---

## Post #7 by @lassoan (2019-01-22 20:56 UTC)

<p>Make sure to set Slicer_DIR to the correct folder when configuring SlicerRT build.</p>

---

## Post #8 by @MachadoL (2019-06-14 21:04 UTC)

<p>Guys, can you remind me the versions should I install 3DSlicer (Qt 5.11? , Slicer4.10 ??) with which <strong>Slicer RT</strong> is supposed to run?</p>
<p>I did it one… then I needed to reinstall… Now I am installing slicer RT from both Extension Manager and built from git, none of them are displayed in the modules scroll/search bar.</p>
<p>I am using now: Slicer <strong>4.10.1</strong> with <strong>Qt 5.11</strong>.</p>
<p>Thanks again.</p>

---

## Post #9 by @lassoan (2019-06-15 02:06 UTC)

<p>If you build Slicer then you need to build SlicerRT as well, using the exact same build environment. See instructions for <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions" rel="nofollow noopener">master</a> and <a href="https://www.slicer.org/wiki/Documentation/4.10/Developers/Build_Instructions" rel="nofollow noopener">4.10 branch</a>. If you stuck at any point then let us know.</p>

---
