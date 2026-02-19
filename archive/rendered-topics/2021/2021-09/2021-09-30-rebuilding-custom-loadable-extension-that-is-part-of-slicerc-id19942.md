---
topic_id: 19942
title: "Rebuilding Custom Loadable Extension That Is Part Of Slicerc"
date: 2021-09-30
url: https://discourse.slicer.org/t/19942
---

# Rebuilding custom loadable extension that is part of SlicerCAT

**Topic ID**: 19942
**Date**: 2021-09-30
**URL**: https://discourse.slicer.org/t/rebuilding-custom-loadable-extension-that-is-part-of-slicercat/19942

---

## Post #1 by @keri (2021-09-30 23:45 UTC)

<p>Hi,</p>
<p>I’m working on loadable extension and I after successively built SlicerCAT I want to edit my extension source code and rebuild it.</p>
<p>The extension is added to the SlicerCAT via <code>FetchContent_Populate</code>.<br>
Then I can see that in build dir there is my extension source code and extension is build in <code>Slicer-build/E/MyExtension</code>.</p>
<p>Then I do something like:</p>
<pre><code class="lang-bash">cd ~/SlicerCAT/d/Slicer-build/E/MyExtension
cmake ../../../MyExtension -DSlicer_DIR=../..
</code></pre>
<p>but I get error when configuring:</p>
<pre><code class="lang-auto">CMake Error at ~/Documents/Colada/d/slicersources-src/CMake/SlicerMacroBuildModuleVTKLibrary.cmake:120 (add_library):
  add_library cannot create target "vtkSlicerStackLoadModuleLogic" because an
  imported target with the same name already exists.
Call Stack (most recent call first):
  ~/Documents/Colada/d/slicersources-src/CMake/SlicerMacroBuildModuleLogic.cmake:98 (SlicerMacroBuildModuleVTKLibrary)
  StackLoad/Logic/CMakeLists.txt:20 (SlicerMacroBuildModuleLogic)
</code></pre>
<p>Thus I can’t rebuilt extension to the dir where SlicerCAT expects loadable modules to be built.<br>
It is highly likely that I can build my extension to different folder then set Slicer to import modules from that folder and delete previous (default) build files but that would be pretty awkward…</p>
<p>By the way I understand that these targets are defined in <code>SlicerTargets.cmake</code> and they should be loaded (all together with <code>SlicerConfig.cmake</code>) when <code>find(Slicer REQUIRED)</code> is processed but I can’t understand how to avoid the error.</p>
<p>For now I work on Ubuntu 20.04 with GCC 9.3<br>
My custom app <a href="https://github.com/tierra-colada/Colada" class="inline-onebox" rel="noopener nofollow ugc">GitHub - tierra-colada/Colada: Geophysical software (in progress)</a><br>
The extension <a href="https://github.com/tierra-colada/Seismic" class="inline-onebox" rel="noopener nofollow ugc">GitHub - tierra-colada/Seismic: Slicer 3D extension for seismic modules</a></p>

---

## Post #2 by @lassoan (2021-10-01 04:18 UTC)

<p>If Slicer already builds your custom modules then you must not build your modules as an extension, because it would want to add the same targets that you already have in your Slicer build. Just run make in the appropriate folder to build Slicer, including your modules.</p>

---
