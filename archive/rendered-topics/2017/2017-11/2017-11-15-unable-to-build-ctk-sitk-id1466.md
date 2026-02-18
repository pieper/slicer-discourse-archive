# Unable to Build CTK & SITK

**Topic ID**: 1466
**Date**: 2017-11-15
**URL**: https://discourse.slicer.org/t/unable-to-build-ctk-sitk/1466

---

## Post #1 by @purav70 (2017-11-15 22:19 UTC)

<p>I am building a fresh release build of slicer 4.7 (commit 42630e641fde4bb8f6e0903cf15ad3ac9cd00b78) using VS2013, Windows x64, QT 4.8.7, and get the following error. This error also seems to cause SITK to fail. I’ve tried a few different solutions but none seem to work - the problem seems to be with these 2 lines of code in FindPythonLibs.cmake. Everything else builds well. I would greatly appreciate some assistance.</p>
<p>Thanks.</p>
<pre><code class="lang-auto">CMake Error at C:/Program Files/CMake/share/cmake-3.7/Modules/FindPythonLibs.cmake:171 (get_filename_component):
11&gt;    get_filename_component unknown component
11&gt;    C:/Fall2017/s4r/python-install/libs/python27.lib
11&gt;  Call Stack (most recent call first):
11&gt;    CMakeExternals/PythonQt.cmake:61 (find_package)
11&gt;    CMake/ctkMacroCheckExternalProjectDependency.cmake:568 (include)
11&gt;    CMake/ctkMacroCheckExternalProjectDependency.cmake:614 (ExternalProject_Include_Dependencies)
11&gt;    CMake/ctkBlockCheckDependencies.cmake:127 (ExternalProject_Include_Dependencies)
11&gt;    CMakeLists.txt:970 (include)
11&gt;  
11&gt;  
11&gt;  CMake Error at C:/Program Files/CMake/share/cmake-3.7/Modules/FindPythonLibs.cmake:172 (get_filename_component):
11&gt;    get_filename_component called with incorrect number of arguments
11&gt;  Call Stack (most recent call first):
11&gt;    CMakeExternals/PythonQt.cmake:61 (find_package)
11&gt;    CMake/ctkMacroCheckExternalProjectDependency.cmake:568 (include)
11&gt;    CMake/ctkMacroCheckExternalProjectDependency.cmake:614 (ExternalProject_Include_Dependencies)
11&gt;    CMake/ctkBlockCheckDependencies.cmake:127 (ExternalProject_Include_Dependencies)
11&gt;    CMakeLists.txt:970 (include)
</code></pre>
<p>The lines of code referred to in FindPythonLibs.cmake</p>
<pre><code class="lang-auto">get_filename_component(_Python_PREFIX ${PYTHON_LIBRARY} PATH)
get_filename_component(_Python_PREFIX ${_Python_PREFIX} PATH)
</code></pre>

---

## Post #2 by @lassoan (2017-11-16 02:25 UTC)

<p>Many of us rebuild Slicer successfully every day using VS2013, Windows x64, Qt-4.8.7. Please use latest master version (Slicer 4.9) and follow build instructions closely.</p>
<ol>
<li>
<p>Build in a shorter build path: Source directory: C:\S4. Build directory: C:\S4R (or C:\S4D).</p>
</li>
<li>
<p>Build Qt using Jc’s one-liner (qt-easy-build)</p>
</li>
</ol>

---

## Post #3 by @ihnorton (2017-11-16 03:13 UTC)

<p>This likely means <code>${PYTHON_LIBRARY}</code> is not set, so there was probably another build error earlier.</p>
<p>But as Andras said, you are best off using the current tree.</p>

---

## Post #4 by @purav70 (2017-11-16 21:55 UTC)

<p>I tried using the master version and following all the instructions (I have built slicer several times in the past) but I still get the same errors. I have begun implementing this unofficial solution outlined here:</p>
<p><a href="https://cmake.org/pipermail/cmake/2017-January/064948.html" class="onebox" target="_blank" rel="nofollow noopener">https://cmake.org/pipermail/cmake/2017-January/064948.html</a></p>
<p>I believe the problem has to do with multiple Python Libraries, given that implementing this solution in several cmake files does seem to push the build further along (CTK now builds, but SITK does not, however I will implement this solution in some of the cmake files related to SITK that throw this same error). I was hoping this would provide insight to come up with a better fix.</p>

---

## Post #5 by @ihnorton (2017-11-17 02:52 UTC)

<p>Ah, ok, well a new enough CMake will have the official fix:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://gitlab.kitware.com/cmake/cmake/-/commit/a12d8a03af8430d0a570c97deb200e16830568eb">
  <header class="source">
      <img src="https://gitlab.kitware.com/uploads/-/system/appearance/favicon/1/KitwareMarkIcon.png" class="site-icon" width="32" height="32">

      <a href="https://gitlab.kitware.com/cmake/cmake/-/commit/a12d8a03af8430d0a570c97deb200e16830568eb" target="_blank" rel="noopener">GitLab</a>
  </header>

  <article class="onebox-body">
    <img src="https://gitlab.kitware.com/uploads/-/system/project/avatar/541/cmakelogo-centered.png" class="thumbnail onebox-avatar" width="330" height="330">

<h3><a href="https://gitlab.kitware.com/cmake/cmake/-/commit/a12d8a03af8430d0a570c97deb200e16830568eb" target="_blank" rel="noopener">FindPythonLibs: Tolerate call with PYTHON_LIBRARY already a list (a12d8a03) ·...</a></h3>

  <p>`PYTHON_LIBRARY` may contain a list because of `SelectLibraryConfigurations`. If it is the case, the list can be: optimized;;debug; Instead of directly using the value of `PYTHON_LIBRARY` in the CMake function...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @purav70 (2017-11-17 19:07 UTC)

<p>A newer cmake did help, and now everything except the Slicer project builds. The error I’m now getting is:</p>
<p>CMake Error at CMake/SlicerMacroBuildApplication.cmake:330 (message):<br>
LAUNCHER_SPLASHSCREEN_FILE is mandatory<br>
Call Stack (most recent call first):<br>
Applications/SlicerApp/CMakeLists.txt:95 (slicerMacroBuildApplication)</p>
<p>Any advice?</p>

---

## Post #7 by @ihnorton (2017-11-17 19:47 UTC)

<p>If you are customizing the Slicer build then you will need to set that variable yourself…<br>
Otherwise, it is defined in <code>Applications/SlicerApp/CMakeLists.txt</code> for standard builds.</p>

---
