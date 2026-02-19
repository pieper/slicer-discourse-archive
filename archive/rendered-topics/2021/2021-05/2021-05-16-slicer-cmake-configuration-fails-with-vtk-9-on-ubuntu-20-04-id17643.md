---
topic_id: 17643
title: "Slicer Cmake Configuration Fails With Vtk 9 On Ubuntu 20 04"
date: 2021-05-16
url: https://discourse.slicer.org/t/17643
---

# Slicer cmake-configuration fails with VTK 9 on Ubuntu 20.04

**Topic ID**: 17643
**Date**: 2021-05-16
**URL**: https://discourse.slicer.org/t/slicer-cmake-configuration-fails-with-vtk-9-on-ubuntu-20-04/17643

---

## Post #1 by @keri (2021-05-16 23:49 UTC)

<p>Hi,</p>
<p>Trying to build SlicerCAT with VTK 9 and I get this error:</p>
<pre data-code-wrap="cmake"><code class="lang-cmake">CMake Error at CMakeLists.txt:813 (find_package):
  Found package configuration file:

    /home/kerim/Documents/Colada_prj/d/VTK-build/vtk-config.cmake

  but it set VTK_FOUND to FALSE so package "VTK" is considered to be NOT
  FOUND.  Reason given by package:

  Could not find the VTK package with the following required components:
  GUISupportQtOpenGL.
</code></pre>
<p>Can’t find a way to turn <code>GUISupportQtOpenGL</code> <strong>ON</strong>.<br>
I can see that <code>External_VTK.cmake</code> has:</p>
<pre data-code-wrap="cmake"><code class="lang-cmake">  if("${Slicer_VTK_RENDERING_BACKEND}" STREQUAL "OpenGL2")
    list(APPEND EXTERNAL_PROJECT_OPTIONAL_VTK8_CMAKE_CACHE_ARGS
      -DModule_vtkGUISupportQtOpenGL:BOOL=ON
      )
    list(APPEND EXTERNAL_PROJECT_OPTIONAL_VTK9_CMAKE_CACHE_ARGS
      -DVTK_MODULE_ENABLE_VTK_GUISupportQtOpenGL:STRING=YES
      )
  endif()
</code></pre>
<p>i.e. it probably should set <code>GUISupportQtOpenGL</code> <strong>ON</strong> and in my case <code>Slicer_VTK_RENDERING_BACKEND</code> is equal to <code>OpenGL2</code>. I have checked <code>if("${Slicer_VTK_RENDERING_BACKEND}" STREQUAL "OpenGL2")</code> statement returns <code>TRUE</code>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0febbc495d8f071fc7d30e54ba418afd145210c7.png" data-download-href="/uploads/short-url/2gQdPiWfFTzN7s5Puvw45I0b4yj.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0febbc495d8f071fc7d30e54ba418afd145210c7_2_690x120.png" alt="image" data-base62-sha1="2gQdPiWfFTzN7s5Puvw45I0b4yj" width="690" height="120" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0febbc495d8f071fc7d30e54ba418afd145210c7_2_690x120.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0febbc495d8f071fc7d30e54ba418afd145210c7.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0febbc495d8f071fc7d30e54ba418afd145210c7.png 2x" data-dominant-color="422237"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">730×127 90.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>With VTK 8.2.0 there was no such error</p>
<p><strong>My Slicer GIT tag:</strong></p>
<pre data-code-wrap="cmake"><code class="lang-cmake">GIT_REPOSITORY git://github.com/Slicer/Slicer
GIT_TAG        "e7ac45bf36195dc2d676d9edca153d86b89ab77d"
GIT_PROGRESS   1
</code></pre>

---

## Post #2 by @keri (2021-05-17 11:24 UTC)

<p>I guess the thing is that in Slicer’s CMakeLists.txt we have:</p>
<pre><code class="lang-auto">set(_default_vtk "8")
set(Slicer_VTK_VERSION_MAJOR ${_default_vtk} CACHE STRING "VTK major version (8 or 9)")
set_property(CACHE Slicer_VTK_VERSION_MAJOR PROPERTY STRINGS "8" "9")
if(NOT "${Slicer_VTK_VERSION_MAJOR}" MATCHES "^(8|9)$")
  message(FATAL_ERROR "error: Slicer_VTK_VERSION_MAJOR must be 8 or 9.")
endif()
mark_as_superbuild(Slicer_VTK_VERSION_MAJOR)
</code></pre>
<p>I guess this overrides my <code>Slicer_VTK_VERSION_MAJOR </code> that I previously set up in my main SlicerCAT’s CMakeLists.txt and I can see the output right before the error appears:</p>
<pre><code class="lang-auto">-- Configuring VTK
--   Slicer_VTK_RENDERING_BACKEND is OpenGL2
--   Slicer_VTK_SMP_IMPLEMENTATION_TYPE is Sequential
--   Slicer_VTK_VERSION_MAJOR is 8
-- Configuring Colada with Qt 5.15.2 (using modules: Core, Widgets, Multimedia, Network, OpenGL, PrintSupport, UiTools, Xml, XmlPatterns, Svg, Sql, WebEngine, WebEngineWidgets, WebChannel, )
-- Setting QT_PLUGINS_DIR: /home/kerim/Qt/5.15.2/gcc_64/plugins
-- Setting QT_BINARY_DIR: /home/kerim/Qt/5.15.2/gcc_64/bin
-- Setting ExternalData_OBJECT_STORES to '/home/kerim/Documents/Colada_prj/d/Slicer-build/ExternalData/Objects'
-- Configuring Colada for [linux-amd64]
CMake Error at CMakeLists.txt:813 (find_package):
  Found package configuration file:

    /home/kerim/Documents/Colada_prj/d/VTK-build/vtk-config.cmake

  but it set VTK_FOUND to FALSE so package "VTK" is considered to be NOT
  FOUND.  Reason given by package:

  Could not find the VTK package with the following required components:
  GUISupportQtOpenGL.



-- Configuring incomplete, errors occurred!
</code></pre>
<p>As you can see the <code>Slicer_VTK_VERSION_MAJOR </code> is equal now to 8.<br>
Do I misunderstand something?</p>

---

## Post #3 by @keri (2021-05-17 13:01 UTC)

<p>I’m sorry. The error was invoked by my misunderstanding of CMake CACHE variable’s behaviour.</p>
<p>I used to set VTK version with the code in my main SlicerCAT CMakeLists.txt:</p>
<pre><code class="lang-auto">set(Slicer_VTK_VERSION_MAJOR 9)
mark_as_superbuild(Slicer_VTK_VERSION_MAJOR)
</code></pre>
<p>but as I noticed in Slicer’s main CMakeLists.txt <code>Slicer_VTK_VERSION_MAJOR</code> is CACHE type.<br>
So to solve my error I simply overwrote the above line with the command:</p>
<pre><code class="lang-auto">set(Slicer_VTK_VERSION_MAJOR 9 CACHE STRING "VTK major version (8 or 9)" FORCE)
mark_as_superbuild(Slicer_VTK_VERSION_MAJOR)
</code></pre>
<p>Now I for the first time successfully compiled SlicerCAT with VTK 9 <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #4 by @lassoan (2021-05-17 20:06 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> How can you set the VTK version for a Slicer custom application?<br>
<a class="mention" href="/u/cpinter">@cpinter</a> As far as I remember you had a similar issue. What did you end up doing?</p>

---

## Post #5 by @jcfr (2021-05-17 23:50 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="17643">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>How can you set the VTK version for a Slicer custom application?</p>
</blockquote>
</aside>
<p>Adding a snippet like this one in the top-level <code>CMakeLists.txt</code> of your custom application will do it:</p>
<pre><code class="lang-auto"># Custom VTK
set(Slicer_${proj}_GIT_REPOSITORY "${EP_GIT_PROTOCOL}://github.com/myorg/VTK")
set(Slicer_${proj}_GIT_TAG "abcdef1234...")
</code></pre>
<h3><a name="p-59730-example-1" class="anchor" href="#p-59730-example-1" aria-label="Heading link"></a>Example</h3>
<p><em>In this example, CTK is customized</em></p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/BICCN/cell-locator/blob/acf3fa31eb30358c724fec71c86a534cb7799a05/CMakeLists.txt#L116-L118">
  <header class="source">

      <a href="https://github.com/BICCN/cell-locator/blob/acf3fa31eb30358c724fec71c86a534cb7799a05/CMakeLists.txt#L116-L118" target="_blank" rel="noopener">github.com/BICCN/cell-locator</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/BICCN/cell-locator/blob/acf3fa31eb30358c724fec71c86a534cb7799a05/CMakeLists.txt#L116-L118" target="_blank" rel="noopener">CMakeLists.txt</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/BICCN/cell-locator/blob/acf3fa31eb30358c724fec71c86a534cb7799a05/CMakeLists.txt#L116-L118" rel="noopener"><code>acf3fa31e</code></a>
</div>



    <pre class="onebox"><code class="lang-txt">
      <ol class="start lines" start="116" style="counter-reset: li-counter 115 ;">
          <li># Custom CTK</li>
          <li>set(Slicer_CTK_GIT_REPOSITORY "${EP_GIT_PROTOCOL}://github.com/KitwareMedical/CTK.git")</li>
          <li>set(Slicer_CTK_GIT_TAG "22d47a7cfe5b2c2c9bc354da31040deadb45ad25") # cell-locator-2021-03-29-7a515ccf</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<h3><a name="p-59730-references-2" class="anchor" href="#p-59730-references-2" aria-label="Heading link"></a>References</h3>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/7d9c2f2488dbbc050baef22aedfd4d83bae6cc48/SuperBuild/External_VTK.cmake#L169-L190">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/7d9c2f2488dbbc050baef22aedfd4d83bae6cc48/SuperBuild/External_VTK.cmake#L169-L190" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/7d9c2f2488dbbc050baef22aedfd4d83bae6cc48/SuperBuild/External_VTK.cmake#L169-L190" target="_blank" rel="noopener">SuperBuild/External_VTK.cmake</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/Slicer/blob/7d9c2f2488dbbc050baef22aedfd4d83bae6cc48/SuperBuild/External_VTK.cmake#L169-L190" rel="noopener"><code>7d9c2f248</code></a>
</div>



    <pre class="onebox"><code class="lang-cmake">
      <ol class="start lines" start="169" style="counter-reset: li-counter 168 ;">
          <li>ExternalProject_SetIfNotDefined(</li>
          <li>  Slicer_${proj}_GIT_REPOSITORY</li>
          <li>  "${EP_GIT_PROTOCOL}://github.com/slicer/VTK.git"</li>
          <li>  QUIET</li>
          <li>  )</li>
          <li></li>
          <li>set(_git_tag)</li>
          <li>if("${Slicer_VTK_VERSION_MAJOR}" STREQUAL "8")</li>
          <li>  set(_git_tag "97904fdcc7e73446b3131f32eac9fc9781b23c2d") # slicer-v8.2.0-2018-10-02-74d9488523</li>
          <li>  set(vtk_egg_info_version "8.2.0")</li>
          <li>elseif("${Slicer_VTK_VERSION_MAJOR}" STREQUAL "9")</li>
          <li>  set(_git_tag "f3c1a72fbf0f7287575ae876efced9c85776d9b4") # slicer-v9.0.20201111-733234c785</li>
          <li>  set(vtk_egg_info_version "9.0.20201111")</li>
          <li>else()</li>
          <li>  message(FATAL_ERROR "error: Unsupported Slicer_VTK_VERSION_MAJOR: ${Slicer_VTK_VERSION_MAJOR}")</li>
          <li>endif()</li>
          <li></li>
          <li>ExternalProject_SetIfNotDefined(</li>
          <li>  Slicer_${proj}_GIT_TAG</li>
          <li>  ${_git_tag}</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/7d9c2f2488dbbc050baef22aedfd4d83bae6cc48/SuperBuild/External_VTK.cmake#L169-L190" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @lassoan (2021-05-17 23:58 UTC)

<p>Thank you <a class="mention" href="/u/jcfr">@jcfr</a>. Does this also set the VTK major version (8/9) or that should be set using another variable?</p>

---

## Post #7 by @jcfr (2021-05-18 00:07 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="17643">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Does this also set the VTK major version (8/9) or that should be set using another variable?</p>
</blockquote>
</aside>
<p>Doing the following will ensure proper initialization of the cache:</p>
<pre data-code-wrap="cmake"><code class="lang-cmake"># Custom VTK
set(Slicer_VTK_VERSION_MAJOR 9 CACHE STRING "VTK major version")
set(Slicer_${proj}_GIT_REPOSITORY "${EP_GIT_PROTOCOL}://github.com/myorg/VTK")
set(Slicer_${proj}_GIT_TAG "abcdef1234...")
</code></pre>
<h3><a name="p-59732-example-1" class="anchor" href="#p-59732-example-1" aria-label="Heading link"></a>Example</h3>
<aside class="onebox githubblob" data-onebox-src="https://github.com/KitwareMedical/SlicerQReads/blob/d40ce875aa49f396fc8fe2b578e477d6cd02894f/CMakeLists.txt#L108">
  <header class="source">

      <a href="https://github.com/KitwareMedical/SlicerQReads/blob/d40ce875aa49f396fc8fe2b578e477d6cd02894f/CMakeLists.txt#L108" target="_blank" rel="noopener">github.com/KitwareMedical/SlicerQReads</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/KitwareMedical/SlicerQReads/blob/d40ce875aa49f396fc8fe2b578e477d6cd02894f/CMakeLists.txt#L108" target="_blank" rel="noopener">CMakeLists.txt</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/KitwareMedical/SlicerQReads/blob/d40ce875aa49f396fc8fe2b578e477d6cd02894f/CMakeLists.txt#L108" rel="noopener"><code>d40ce875a</code></a>
</div>



    <pre class="onebox"><code class="lang-txt">
      <ol class="start lines" start="98" style="counter-reset: li-counter 97 ;">
          <li>option(Slicer_USE_QtTesting                     "Build application with QtTesting support"            OFF)</li>
          <li>option(Slicer_USE_SimpleITK                     "Build application with SimpleITK support"            OFF)</li>
          <li></li>
          <li>option(Slicer_BUILD_BRAINSTOOLS                 "Build application with BRAINSTools module"           OFF)</li>
          <li>option(Slicer_BUILD_DataStore                   "Build application with DataStore module"             OFF)</li>
          <li>option(Slicer_BUILD_CompareVolumes              "Build application with CompareVolumes module"        OFF)</li>
          <li>option(Slicer_BUILD_LandmarkRegistration        "Build application with LandmarkRegistration module"  OFF)</li>
          <li>option(Slicer_BUILD_SurfaceToolbox              "Build application with SurfaceToolbox module"        OFF)</li>
          <li></li>
          <li>option(Slicer_BUILD_CLI                         "Build Slicer CLI Plugins"                            OFF)</li>
          <li class="selected">set(Slicer_VTK_VERSION_MAJOR 9 CACHE STRING "VTK major version (8 or 9)")</li>
          <li></li>
          <li># Enable Slicer built-in modules</li>
          <li>set(Slicer_CLIMODULES_ENABLED</li>
          <li>  ResampleDTIVolume             # Needed by ResampleScalarVectorDWIVolume</li>
          <li>  ResampleScalarVectorDWIVolume # Depends on DiffusionApplications, needed by CropVolume</li>
          <li>  )</li>
          <li>set(Slicer_QTLOADABLEMODULES_ENABLED</li>
          <li>  )</li>
          <li>set(Slicer_QTSCRIPTEDMODULES_ENABLED</li>
          <li>  )</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #8 by @lassoan (2021-05-18 00:47 UTC)

<p>Great, thank you. <a class="mention" href="/u/keri">@keri</a> tried to do this but probably it failed because of a previous configuration with version 8. Your complete working example above should be sufficient for anyone who needs to use a custom VTK version.</p>

---

## Post #9 by @cpinter (2021-05-18 08:45 UTC)

<p>Thanks <a class="mention" href="/u/jcfr">@jcfr</a> this could be potentially quite useful to use as well.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="17643">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>As far as I remember you had a similar issue. What did you end up doing?</p>
</blockquote>
</aside>
<p>I did not have this specific issue. Maybe what you remember is that I tried to configure an extension used by a custom app with an additional option (still haven’t figured it out btw).</p>

---
