---
topic_id: 1849
title: "Master With Qt5 Build Fails"
date: 2018-01-15
url: https://discourse.slicer.org/t/1849
---

# Master with Qt5 build fails

**Topic ID**: 1849
**Date**: 2018-01-15
**URL**: https://discourse.slicer.org/t/master-with-qt5-build-fails/1849

---

## Post #1 by @adamrankin (2018-01-15 21:11 UTC)

<p>Cloned Slicer master (b748b88cefa57bc126f3a5c64a4fb59c28e4bb9b) and tried to build with Qt 5.9.1.</p>
<p>Received many generation errors similar to:</p>
<pre><code>  CMake Error at Libs/vtkAddon/CMakeLists.txt:94 (add_library):
    Cannot find source file:

      C:/d/Slcr/S4D/Slicer-build/Libs/vtkAddon/vtkAddonHierarchy.stamp.txt

    Tried extensions .c .C .c++ .cc .cpp .cxx .m .M .mm .h .hh .h++ .hm .hpp
    .hxx .in .txx
</code></pre>
<p>Has anyone else experienced this?</p>
<p>Edit: not suprising, but build errors follow on the form:</p>
<p><code>CUSTOMBUILD : CMake error : CMake can not determine linker language for target: vtkAddon [C:\d\Slcr\S4D\Slicer.vcxproj]</code></p>

---

## Post #2 by @jcfr (2018-01-15 22:27 UTC)

<p>Most likely related to the VTKv9 update.</p>
<p>I submitted issue <a href="https://gitlab.kitware.com/vtk/vtk/issues/17217">17217</a> to upstream VTK project and proposed a fix in <a href="https://gitlab.kitware.com/vtk/vtk/merge_requests/3794">MR vtk/vtk#3794</a> (already added to Slicer fork of VTK).</p>
<p>This addressed issues I experienced on Linux.</p>
<p>Look like there are still some issues.</p>
<p>Here are some related references that will be helpful to debug:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/b748b88cefa57bc126f3a5c64a4fb59c28e4bb9b/Libs/vtkAddon/CMakeLists.txt#L146-L151" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/b748b88cefa57bc126f3a5c64a4fb59c28e4bb9b/Libs/vtkAddon/CMakeLists.txt#L146-L151" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/b748b88cefa57bc126f3a5c64a4fb59c28e4bb9b/Libs/vtkAddon/CMakeLists.txt#L146-L151</a></h4>
<pre class="onebox"><code class="lang-txt"><ol class="start lines" start="146" style="counter-reset: li-counter 145 ;">
<li>vtkMacroKitPythonWrap(</li>
<li>  KIT_NAME ${lib_name}</li>
<li>  KIT_SRCS ${vtkAddon_SRCS}</li>
<li>  KIT_INSTALL_BIN_DIR ${${PROJECT_NAME}_INSTALL_BIN_DIR}</li>
<li>  KIT_INSTALL_LIB_DIR ${${PROJECT_NAME}_INSTALL_LIB_DIR}</li>
<li>  )</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/b748b88cefa57bc126f3a5c64a4fb59c28e4bb9b/CMake/vtkMacroKitPythonWrap.cmake#L121-L138" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/b748b88cefa57bc126f3a5c64a4fb59c28e4bb9b/CMake/vtkMacroKitPythonWrap.cmake#L121-L138" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/b748b88cefa57bc126f3a5c64a4fb59c28e4bb9b/CMake/vtkMacroKitPythonWrap.cmake#L121-L138</a></h4>
<pre class="onebox"><code class="lang-cmake"><ol class="start lines" start="121" style="counter-reset: li-counter 120 ;">
<li>include(${VTK_CMAKE_DIR}/vtkWrapHierarchy.cmake)</li>
<li>
</li>
<li># Set variables for this and future runs of vtk_wrap_hierarchy:</li>
<li>#  - &lt;module_name&gt;_WRAP_DEPENDS</li>
<li>#  - &lt;module_name&gt;_WRAP_HIERARCHY_FILE</li>
<li>set(${MY_KIT_NAME}_WRAP_DEPENDS "${_kit_wrap_depends}" CACHE INTERNAL "${MY_KIT_NAME} wrapping dependencies" FORCE)</li>
<li>set(_wrap_hierarchy_file "${Slicer_BINARY_DIR}/${MY_KIT_NAME}Hierarchy.txt")</li>
<li>set(_wrap_hierarchy_stamp_file ${CMAKE_CURRENT_BINARY_DIR}/${MY_KIT_NAME}Hierarchy.stamp.txt)</li>
<li>set(${MY_KIT_NAME}_WRAP_HIERARCHY_FILE "${_wrap_hierarchy_file}" CACHE INTERNAL "${MY_KIT_NAME} wrap hierarchy file" FORCE)</li>
<li>
</li>
<li>set_property(GLOBAL APPEND PROPERTY SLICER_WRAP_HIERARCHY_TARGETS ${MY_KIT_NAME})</li>
<li>
</li>
<li># Set variables for vtk_wrap_python3:</li>
<li>#   - KIT_HIERARCHY_FILE</li>
<li>set(KIT_HIERARCHY_FILE "${_wrap_hierarchy_file}")</li>
<li>
</li>
<li># Generate hierarchy files</li>
<li>vtk_wrap_hierarchy(${MY_KIT_NAME} ${Slicer_BINARY_DIR} "${TMP_WRAP_FILES}")</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/VTK/blob/slicer-v9.0.0-2018-01-11-590b341/CMake/vtkWrapHierarchy.cmake" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/VTK/blob/slicer-v9.0.0-2018-01-11-590b341/CMake/vtkWrapHierarchy.cmake" target="_blank" rel="nofollow noopener">Slicer/VTK/blob/slicer-v9.0.0-2018-01-11-590b341/CMake/vtkWrapHierarchy.cmake</a></h4>
<pre><code class="lang-cmake">#
# a cmake macro to generate a text file with the class hierarchy
#
macro(VTK_WRAP_HIERARCHY module_name OUTPUT_DIR SOURCES)
  if(NOT VTK_WRAP_HIERARCHY_EXE)
    if(TARGET vtkWrapHierarchy)
      set(VTK_WRAP_HIERARCHY_EXE vtkWrapHierarchy)
    else()
      message(SEND_ERROR "VTK_WRAP_HIERARCHY_EXE not specified when calling VTK_WRAP_HIERARCHY")
    endif()
  endif()

  # collect the common wrapper-tool arguments
  if(NOT VTK_ENABLE_KITS)
    # write wrapper-tool arguments to a file
    set(_args_file ${module_name}Hierarchy.$&lt;CONFIGURATION&gt;.args)
    file(GENERATE OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/${_args_file} CONTENT "
$&lt;$&lt;BOOL:$&lt;TARGET_PROPERTY:${module_name},COMPILE_DEFINITIONS&gt;&gt;:
-D\"$&lt;JOIN:$&lt;TARGET_PROPERTY:${module_name},COMPILE_DEFINITIONS&gt;,\"
-D\"&gt;\"&gt;
</code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/VTK/blob/slicer-v9.0.0-2018-01-11-590b341/CMake/vtkWrapHierarchy.cmake" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @jcfr (2018-01-15 22:32 UTC)

<p>It turns out that the hierarchy stamp file has been removed in latest VTK:</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/VTK/commit/a8ada6f05b950d8df50e2f6c7427591064d10f17#diff-5ce2dfc7465c1fe39c43979d84de3629">
  <header class="source">

      <a href="https://github.com/Slicer/VTK/commit/a8ada6f05b950d8df50e2f6c7427591064d10f17#diff-5ce2dfc7465c1fe39c43979d84de3629" target="_blank" rel="noopener">github.com/Slicer/VTK</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/VTK/commit/a8ada6f05b950d8df50e2f6c7427591064d10f17" target="_blank" rel="noopener">vtkWrapHierarchy: remove the stamp file</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2017-12-13" data-time="16:31:50" data-timezone="UTC">04:31PM - 13 Dec 17 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/mathstuf" target="_blank" rel="noopener">
          <img alt="mathstuf" src="https://avatars.githubusercontent.com/u/97253?v=4" class="onebox-avatar-inline" width="20" height="20">
          mathstuf
        </a>
      </div>

      <div class="lines" title="changed 1 files with 2 additions and 4 deletions">
        <a href="https://github.com/Slicer/VTK/commit/a8ada6f05b950d8df50e2f6c7427591064d10f17" target="_blank" rel="noopener">
          <span class="added">+2</span>
          <span class="removed">-4</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Instead, just use the hierarchy file as an output.</p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>This means the following Slicer file would have to be updated accordingly:</p>
<p><a href="https://github.com/Slicer/Slicer/blob/b748b88cefa57bc126f3a5c64a4fb59c28e4bb9b/CMake/vtkMacroKitPythonWrap.cmake#L149-L154" class="onebox" target="_blank" rel="noopener">https://github.com/Slicer/Slicer/blob/b748b88cefa57bc126f3a5c64a4fb59c28e4bb9b/CMake/vtkMacroKitPythonWrap.cmake#L149-L154</a></p>

---

## Post #4 by @jcfr (2018-01-16 12:47 UTC)

<p>Thanks for the patch <a class="mention" href="/u/adamrankin">@adamrankin</a></p>
<p>For future reference:</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/866">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/866" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/866" target="_blank" rel="noopener">Crash during proprocessing using a 3.4 mrml in 3.6</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:33:28" data-timezone="UTC">10:33PM - 12 Mar 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:33:29" data-timezone="UTC">10:33PM - 12 Mar 20 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/slicerbot" target="_blank" rel="noopener">
          <img alt="slicerbot" src="https://avatars.githubusercontent.com/u/10277015?v=4" class="onebox-avatar-inline" width="20" height="20">
          slicerbot
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">_This issue was created automatically from an original [Mantis Issue](https://ma<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ntisarchive.slicer.org/view.php?id=866). Further discussion may take place here._</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>It has been integrated in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26834">r26834</a></p>

---
