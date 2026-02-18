# Error "could not find PythonLibs" when building extension

**Topic ID**: 5336
**Date**: 2019-01-11
**URL**: https://discourse.slicer.org/t/error-could-not-find-pythonlibs-when-building-extension/5336

---

## Post #1 by @cpinter (2019-01-11 20:19 UTC)

<p>I’m trying to build SlicerVirtualReality on Windows, but I’m getting this error:</p>
<pre><code>3&gt; CMake Error at C:/Program Files/CMake/share/cmake-3.12/Modules/FindPackageHandleStandardArgs.cmake:137 (message):
3&gt;    Could NOT find PythonLibs (missing: PYTHON_LIBRARIES PYTHON_INCLUDE_DIRS)
</code></pre>
<p>after which I’m getting this error:</p>
<pre><code>4&gt;  CMake Error at C:/d/S4R/VTK/CMake/vtkModuleAPI.cmake:140 (message):
4&gt;    Requested modules not available:
4&gt;
4&gt;      vtkRenderingOpenVR
4&gt;  Call Stack (most recent call first):
4&gt;    C:/d/S4R/VTK-build/VTKConfig.cmake:130 (vtk_module_config)
4&gt;    VirtualReality/MRML/CMakeLists.txt:6 (find_package)
</code></pre>
<p>I’m not sure if they are related, but I have the feeling they are, because I can build other extensions like MarkupsToModel or SlicerRT without problems.</p>
<p>The reason this computer is different from my other computers on which SlicerVirtualReality builds fine is that I installed a Python 3.7 on this one. There was nothing in the environment variables related to that other python installation other than a path, but the error didn’t go away after removing that either.</p>
<p>Does anyone has an idea what to try next? Thanks a lot!</p>

---

## Post #2 by @jcfr (2019-01-11 20:37 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="1" data-topic="5336">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>Does anyone has an idea what to try next? Thanks a lot!</p>
</blockquote>
</aside>
<p>It looks like something is resetting the value of <code>PYTHON_LIBRARY</code> and <code>PYTHON_INCLUDE_DIR</code> CMake cache variable in the extension build tree.</p>
<p>If you add there lines after finding Slicer in <a href="https://github.com/KitwareMedical/SlicerVirtualReality/blob/42985c5297e38cac391ff08b3d32bbb583fc8c72/CMakeLists.txt#L23">KitwareMedical/SlicerVirtualReality/CMakeLists.txt</a>:</p>
<pre><code class="lang-auto">message("PYTHON_LIBRARY :${PYTHON_LIBRARY}")
message("PYTHON_INCLUDE_DIR :${PYTHON_INCLUDE_DIR}")
</code></pre>
<p>is there value correct ?</p>
<p>If yes, I suggest you do the same in<a href="https://github.com/Slicer/VTK/blob/slicer-v8.2.0-2018-10-02-74d9488523/Rendering/OpenVR/CMakeLists.txt#L10">Rendering/OpenVR/CMakeLists.txt</a></p>
<p>That should allow you to find out what is resetting the variables …</p>

---

## Post #3 by @cpinter (2019-01-11 20:45 UTC)

<p>Thanks for the suggestions, <a class="mention" href="/u/jcfr">@jcfr</a>!</p>
<p>Yes, the variables have the correct values in both the main SlicerVR CmakeLists.txt, and both in the one where the second error occurs (I put it just before line 6):</p>
<pre><code>3&gt;  PYTHON_LIBRARY :C:/d/S4R/python-install/libs/python27.lib
3&gt;  PYTHON_INCLUDE_DIR :C:/d/S4R/python-install/include
</code></pre>
<p>Rendering/OpenVR/CMakeLists.txt does not give me any output, I guess it never gets that far.</p>

---

## Post #4 by @jcfr (2019-01-11 21:55 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="1" data-topic="5336">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>CMake Error at C:/Program Files/CMake/share/cmake-3.12/Modules/FindPackageHandleStandardArgs.cmake:137 (message): 3&gt; Could NOT find PythonLibs (missing: PYTHON_LIBRARIES PYTHON_INCLUDE_DIRS)</p>
</blockquote>
</aside>
<p>Also what is the full stack, where does the error originate ?</p>

---

## Post #5 by @cpinter (2019-01-11 21:58 UTC)

<p>Here it is:</p>
<pre><code>3&gt;------ Build started: Project: VTKRenderingOpenVR, Configuration: Release x64 ------
...
3&gt;  CMake Error at C:/Program Files/CMake/share/cmake-3.12/Modules/FindPackageHandleStandardArgs.cmake:137 (message):
3&gt;    Could NOT find PythonLibs (missing: PYTHON_LIBRARIES PYTHON_INCLUDE_DIRS)
3&gt;  Call Stack (most recent call first):
3&gt;    C:/Program Files/CMake/share/cmake-3.12/Modules/FindPackageHandleStandardArgs.cmake:378 (_FPHSA_FAILURE_MESSAGE)
3&gt;    C:/d/S4R/VTK/CMake/FindPythonLibs.cmake:213 (FIND_PACKAGE_HANDLE_STANDARD_ARGS)
3&gt;    C:/d/S4R/VTK/CMake/vtkWrapPython.cmake:167 (find_package)
3&gt;    C:/d/S4R/VTK/CMake/vtkInitializeWrapPython.cmake:4 (include)
3&gt;    C:/d/S4R/VTK/CMake/vtkExternalModuleMacros.cmake:15 (include)
3&gt;    CMakeLists.txt:8 (include)</code></pre>

---

## Post #6 by @jcfr (2019-01-11 22:13 UTC)

<p>Then, could you check that the variable are set before the call of <code>vtkExternalModuleMacros</code> <a href="https://github.com/Slicer/VTK/blob/slicer-v8.2.0-2018-10-02-74d9488523/Rendering/OpenVR/CMakeLists.txt#L8" rel="nofollow noopener">here</a></p>

---

## Post #7 by @cpinter (2019-01-11 22:16 UTC)

<p>Good point, sorry!</p>
<pre><code>2&gt;  PYTHON_LIBRARY :PYTHON_LIBRARY-NOTFOUND
2&gt;  PYTHON_INCLUDE_DIR :
</code></pre>
<p>So one says not found, the other one is empty.<br>
Not sure why it’s not propagated. Thanks!</p>

---

## Post #8 by @jcfr (2019-01-11 22:22 UTC)

<p>Could you try adding:</p>
<pre><code class="lang-auto">-DPYTHON_LIBRARY:FILEPATH=${PYTHON_LIBRARY}
-DPYTHON_INCLUDE_DIR:PATH=${PYTHON_INCLUDE_DIR}
</code></pre>
<p>to <a href="https://github.com/KitwareMedical/SlicerVirtualReality/blob/master/SuperBuild/External_VTKRenderingOpenVR.cmake#L38" rel="nofollow noopener">https://github.com/KitwareMedical/SlicerVirtualReality/blob/master/SuperBuild/External_VTKRenderingOpenVR.cmake#L38</a></p>

---

## Post #9 by @cpinter (2019-02-04 16:30 UTC)

<p>An update about this:<br>
I removed all python-related environment variables and paths, which didn’t seem to solve the problem. Then I went on vacation for a few weeks, which involved windows update (and thus restart). Now I’m back and rebased SlicerVR on the master, tried to build, and now it worked. So either the env.var. thing or the update/restart, or both solved it. Thanks for the pointers.</p>

---
