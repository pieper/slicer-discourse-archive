# Adding volume in C++

**Topic ID**: 19174
**Date**: 2021-08-12
**URL**: https://discourse.slicer.org/t/adding-volume-in-c/19174

---

## Post #1 by @keri (2021-08-12 18:26 UTC)

<p>I’m working on custom slicer app and now I need to understand how to add volume in C++.</p>
<p>For example I have <code>Eigen::MatrixXf</code> that can be represented as <code>vtkImageData</code>.<br>
To display my data I guess I need to call <code>GetScene()</code> (or <code>GetMRMLScene()</code> I don’t know exactly) and then call <code>AddNode(myVtkImage)</code>.</p>
<p>If so I cannot understand how to call <code>GetScene()</code> from mainwindow class? What header contains this <code>GetScene</code>?</p>

---

## Post #2 by @lassoan (2021-08-12 18:47 UTC)

<p>When your module is instantiated the scene is passed to both the module logic and widget classes and they can be accessed as <code>this-&gt;GetMRMLScene()</code> and <code>this-&gt;mrmlScene()</code>, respectively.</p>
<p>All other classes should get the scene from these classes (e.g., the module widget sets the scene in its child widgets), but if you need any quick hack anywhere then you can access the application singleton, get the application logic from it, and from that you can get the scene. It is better to avoid getting the scene from the application though, because it adds unnecessary dependencies and assumptions, which make the class less reusable.</p>

---

## Post #3 by @keri (2021-08-12 21:51 UTC)

<p>Thank you!</p>
<p>One another related question that has now appeared:</p>
<p>If my module depends on my SlicerCAT library wich is added via <code>slicerMacroBuildAppLibrary(NAME qColada ...)</code> and thus should be called <code>qColada</code>, how can I <code>find_package(qColada REQUIRED)</code> from my loadable module’s CMakeLists? As I can see <code>slicerMacroBuildAppLibrary()</code> doesn’t produce something like <code>qColadaConfig.cmake</code> inside <code>Slicer-build</code>. (in contrast to <code>SlicerConfig.cmake</code> wich resides in this folder and thus can be easily found).</p>
<p>I guess I need somehow pass <code>-DqColada_DIR=/path/to/ColadaConfig.cmake</code> when configuring my module…</p>
<p>I forgot to notice that I’m trying to build module externally</p>

---

## Post #4 by @lassoan (2021-08-13 04:39 UTC)

<p><code>find_package</code> is for external packages. Within Slicer, the module libraries and headers are available as CMake variables. See for example, <a href="https://github.com/SlicerIGT/SlicerIGT/blob/master/PathExplorer/CMakeLists.txt">here</a> how libraries of Subject Hierarchy and Markups modules are used in a SlicerIGT module.</p>

---

## Post #5 by @keri (2021-08-13 10:23 UTC)

<p>I think now I see how this works. Variables marked <code>mark_as_superbuild(...)</code> are kept in <code>SlicerConfig.cmake</code> and thus I can use them to find my dependencies.</p>
<p>Thank you!</p>

---

## Post #6 by @keri (2021-08-13 13:43 UTC)

<p>Also I can see now that the target <code>qColadaApp</code> is defined as:</p>
<pre data-code-wrap="cmake"><code class="lang-cmake">if (TARGET qColadaApp)
  message("qColadaApp EXIST")
endif()
</code></pre>
<p>prints: <code>qColadaApp EXIST</code></p>
<p>But when I link this target <code>qColadaApp</code> to my module:</p>
<pre data-code-wrap="cmake"><code class="lang-cmake">set(MODULE_TARGET_LIBRARIES
  vtkSlicer${MODULE_NAME}ModuleLogic
  qSlicer${MODULE_NAME}ModuleWidgets
  qColadaApp    # my custom Slicer library
  )

#-----------------------------------------------------------------------------
slicerMacroBuildLoadableModule(
  NAME ${MODULE_NAME}
  TITLE ${MODULE_TITLE}
  EXPORT_DIRECTIVE ${MODULE_EXPORT_DIRECTIVE}
  INCLUDE_DIRECTORIES ${MODULE_INCLUDE_DIRECTORIES}
  SRCS ${MODULE_SRCS}
  MOC_SRCS ${MODULE_MOC_SRCS}
  UI_SRCS ${MODULE_UI_SRCS}
  TARGET_LIBRARIES ${MODULE_TARGET_LIBRARIES}
  RESOURCES ${MODULE_RESOURCES}
  WITH_GENERIC_TESTS
  )
</code></pre>
<p>I see that IDE can’t include headers from that target. Picture below. Probably some target properties are missing?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/861900b7c396cb62a326aca712534be35fef5439.png" data-download-href="/uploads/short-url/j8hy3vK3YoBdfQPCFKjeLfg6wt3.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/861900b7c396cb62a326aca712534be35fef5439_2_690x367.png" alt="image" data-base62-sha1="j8hy3vK3YoBdfQPCFKjeLfg6wt3" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/861900b7c396cb62a326aca712534be35fef5439_2_690x367.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/861900b7c396cb62a326aca712534be35fef5439_2_1035x550.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/861900b7c396cb62a326aca712534be35fef5439_2_1380x734.png 2x" data-dominant-color="F4F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1600×852 86.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @keri (2021-08-13 16:42 UTC)

<p>I guess I have found a solution. I should have manually added include folders to my <code>ColadaApp</code> headers (and export header wich is in <code>Slicer-build/Applications/ColadaApp</code>:</p>
<pre><code class="lang-auto"># Current_{source,binary} and Slicer_{Libs,Base} already included
set(MODULE_INCLUDE_DIRECTORIES
  ${CMAKE_CURRENT_SOURCE_DIR}/Logic
  ${CMAKE_CURRENT_BINARY_DIR}/Logic
  ${CMAKE_CURRENT_SOURCE_DIR}/Widgets
  ${CMAKE_CURRENT_BINARY_DIR}/Widgets

  # These two are my dirs
  ${CMAKE_CURRENT_SOURCE_DIR}/../../../Applications/ColadaApp
  ${Slicer_BINARY_DIR}/Applications/ColadaApp
  )

slicerMacroBuildLoadableModule(
...
  INCLUDE_DIRECTORIES ${MODULE_INCLUDE_DIRECTORIES}
...
  )
</code></pre>
<p>I hope the number of my questions grows slower than the answers on them <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #8 by @lassoan (2021-08-16 22:21 UTC)

<p>A post was split to a new topic: <a href="/t/change-memory-layout-of-images/19217">Change memory layout of images</a></p>

---
