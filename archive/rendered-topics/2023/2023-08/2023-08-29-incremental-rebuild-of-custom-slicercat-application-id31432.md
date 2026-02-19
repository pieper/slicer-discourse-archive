---
topic_id: 31432
title: "Incremental Rebuild Of Custom Slicercat Application"
date: 2023-08-29
url: https://discourse.slicer.org/t/31432
---

# Incremental rebuild of custom (SlicerCAT) application

**Topic ID**: 31432
**Date**: 2023-08-29
**URL**: https://discourse.slicer.org/t/incremental-rebuild-of-custom-slicercat-application/31432

---

## Post #1 by @darabi (2023-08-29 13:30 UTC)

<p>Hello,<br>
when I change something in my SlicerCAT based custom application, I would like to make an incremental build, such that only those changed parts are updated/compiled.</p>
<p>However, running <code>make</code> in the <code>$BUILD_DIR/Slicer-build</code> directory starts to re-generate wrappers, re-compile a lot of <code>.cxx</code> files and re-link a lot of shared libs and binaries, e.g.:</p>
<pre><code class="lang-auto">...

Consolidate compiler generated dependencies of target MRMLLogic
[ 32%] Building CXX object Libs/MRML/Logic/CMakeFiles/MRMLLogic.dir/vtkMRMLAbstractLogic.cxx.o
[ 32%] Building CXX object Libs/MRML/Logic/CMakeFiles/MRMLLogic.dir/vtkMRMLApplicationLogic.cxx.o
[ 32%] Building CXX object Libs/MRML/Logic/CMakeFiles/MRMLLogic.dir/vtkMRMLColorLogic.cxx.o
[ 33%] Building CXX object Libs/MRML/Logic/CMakeFiles/MRMLLogic.dir/vtkMRMLDisplayableHierarchyLogic.cxx.o
[ 33%] Building CXX object Libs/MRML/Logic/CMakeFiles/MRMLLogic.dir/vtkMRMLRemoteIOLogic.cxx.o
[ 33%] Building CXX object Libs/MRML/Logic/CMakeFiles/MRMLLogic.dir/vtkMRMLLayoutLogic.cxx.o
[ 33%] Building CXX object Libs/MRML/Logic/CMakeFiles/MRMLLogic.dir/vtkMRMLSliceLayerLogic.cxx.o
[ 33%] Building CXX object Libs/MRML/Logic/CMakeFiles/MRMLLogic.dir/vtkMRMLSliceLogic.cxx.o
[ 33%] Building CXX object Libs/MRML/Logic/CMakeFiles/MRMLLogic.dir/vtkMRMLSliceLinkLogic.cxx.o
[ 33%] Building CXX object Libs/MRML/Logic/CMakeFiles/MRMLLogic.dir/vtkMRMLViewLogic.cxx.o
[ 33%] Building CXX object Libs/MRML/Logic/CMakeFiles/MRMLLogic.dir/vtkMRMLViewLinkLogic.cxx.o
[ 33%] Linking CXX shared library ../../../bin/libMRMLLogic.so
[ 33%] Built target MRMLLogic
</code></pre>
<p>and then it continues with a lot of other targets:</p>
<pre><code class="lang-auto">Consolidate compiler generated dependencies of target MRMLLogicCxxTests
...
Consolidate compiler generated dependencies of target MRMLDisplayableManager
...
Consolidate compiler generated dependencies of target MRMLDisplayableManagerPython
...
Consolidate compiler generated dependencies of target MRMLDisplayableManagerCxxTests
...
</code></pre>
<p>I’m not a CMake expert and the generated Makefiles are far too complex and contain too many targets for my limited make-foo.</p>
<p>Is there a way of rebuilding without this time-consuming compilation step?</p>
<p>Thank you</p>
<p>Kambiz</p>

---

## Post #2 by @cpinter (2023-08-29 13:44 UTC)

<p>You find the directories corresponding to each target in the subfolders. For example if you have a Widgets target within your custom app it is here: [SuperBuildPath]\Slicer-build\E[CustomAppName]\Widgets</p>
<p>You can run make from that folder on Linux or build the vcxproj if you’re on Windows.</p>
<p>I had to made a bunch of assumptions so let me know if this helped…</p>

---

## Post #3 by @darabi (2023-08-29 14:42 UTC)

<p>Hi Csaba,<br>
thank you for your help and sorry for the incomplete information: I’m on Ubuntu 22.04 with gcc 11.4.</p>
<p>I do have a directory <code>SuperBuildPath/Slicer-build/E/</code> (not <code>ECustomAppName</code>) and in that directory, I find the <code>Home</code> module from the source tree <code>Modules/Scripted/</code> directory <strong>plus</strong> the modules and extensions which I added in my top-level <code>CMakeLists.txt</code> file.</p>
<p>When I add a new module, I probably have to re-run cmake to generate the Makefile. Will that lead to a recompile of the other (unrelated) parts?</p>
<p>Thanks</p>
<p>Kambiz</p>

---

## Post #4 by @cpinter (2023-08-29 15:12 UTC)

<p>I haven’t found a way to re-run CMake without running the superbuild. However, this does not bother me, because 1) adding new modules is not an everyday task, 2) If you’re in a hurry you can copy the new Python source files (only if the module is a scripted one of course) to [SuperBuildPath]\Slicer-build\lib[CustomAppName]-5.5\qt-scripted-modules and just start your application, which will instantiate the new module because it found the new .py file.</p>
<p>Just in case it helps: usually when I develop in Python I don’t run any build, but run a script that copies the source files to the appropriate directory in the superbuild. Some people change the AdditionalModulePaths in the ini file to point to their source codes, but I found that limiting. Still others make the Python changes directly in the superbuild and then copy those to the working copy of the source code, but I’m too cautious for that (a build would make those changes disappear).</p>

---

## Post #5 by @ebrahim (2023-08-29 15:56 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="4" data-topic="31432">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>If you’re in a hurry you can copy the new Python source files (only if the module is a scripted one of course) to [SuperBuildPath]\Slicer-build\lib[CustomAppName]-5.5\qt-scripted-modules and just start your application, which will instantiate the new module because it found the new .py file.</p>
</blockquote>
</aside>
<p>and there are these handy build targets to achieve this copy as well:</p>
<pre><code class="lang-auto">cmake --build ~/customapp-superbuild/Slicer-build --target CopySlicerPythonScriptFiles
cmake --build ~/customapp-superbuild/Slicer-build --target CopySlicerPythonResourceFiles
</code></pre>

---

## Post #6 by @darabi (2023-08-30 10:03 UTC)

<p>Thank you for your helpful tricks <a class="mention" href="/u/cpinter">@cpinter</a> and <a class="mention" href="/u/ebrahim">@ebrahim</a>!</p>

---
