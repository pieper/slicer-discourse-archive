# How to get GPU information using QT and VTK?

**Topic ID**: 35297
**Date**: 2024-04-04
**URL**: https://discourse.slicer.org/t/how-to-get-gpu-information-using-qt-and-vtk/35297

---

## Post #1 by @BerDom.Ing (2024-04-04 21:19 UTC)

<p>I’m trying to create a method that returns the graphics card information. To do this, I’m importing “from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor”.</p>
<pre><code class="lang-auto">
    def get_graphics_card_info():
        # Create a hidden QVTKRenderWindowInteractor
        qvtk_interactor = QVTKRenderWindowInteractor()
        qvtk_interactor.Initialize()

        # Create a vtkRenderWindow and set the interactor
        render_window = vtk.vtkRenderWindow()
        render_window.SetOffScreenRendering(1)
        render_window.SetInteractor(qvtk_interactor)

        # Now get the graphics card info
        info = render_window.ReportCapabilities()

        # Clean up
        render_window.Finalize()
        qvtk_interactor.TerminateApp()

        return info
</code></pre>
<p>I get this error</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "C:---\AppData\Local\slicer.org\Slicer 5.6.1\bin\Lib\site-packages\vtkmodules\qt\QVTKRenderWindowInteractor.py", line 80, in &lt;module&gt;
    import PySide6.QtCore
ModuleNotFoundError: No module named 'PySide6'
</code></pre>
<p>It appears that Slicer doesn’t find that library, and as far as I know, it should be included in Slicer.</p>

---

## Post #2 by @mau_igna_06 (2024-04-04 22:06 UTC)

<p>Try to write your code inside Slicer’s python interactor</p>
<p><code>qt</code> and <code>vtk</code> are available inside it. For example you can write:</p>
<p><code>pushb = qt.QPushButton()</code></p>
<p>to instantiate a PushButton</p>

---

## Post #3 by @jamesobutler (2024-04-04 23:18 UTC)

<aside class="quote" data-post="2" data-topic="13137">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-access-qtcore-constants-in-python/13137/2">How to access qtcore constants in Python?</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Slicer uses PythonQt library for Python wrapping of Qt. PyQt is not free to use (it has GPL/commercial license), so we have never even considered using it. Python for Qt is very popular, as it is provided by the Qt company, but PythonQt has many advantages - most importantly that it is intended for applications that embed Python. 
Anyway, Slicer imports all Qt packages in qt namespace. For example, QFile class in qtcore can be accessed as qt.QFile()
  </blockquote>
</aside>

<p><code>import qt</code> is how you will use PythonQt in Slicer. Pyside is not used as Pyside6 is actually for Qt6 and Slicer still uses Qt5.</p>

---

## Post #4 by @BerDom.Ing (2024-04-06 15:16 UTC)

<p>I tried using the import “from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor” from Slicer’s Python interactor, and it raises the same error. It indicates that the Python environment used by Slicer is unable to find any of the Python bindings for Qt (PyQt4, PyQt5, PyQt6, PySide, PySide2, or PySide6).</p>

---

## Post #5 by @pieper (2024-04-06 15:29 UTC)

<p>Hi <a class="mention" href="/u/berdom.ing">@BerDom.Ing</a> - as James says, Slicer doesn’t use any of those.  Slicer uses <a href="https://mevislab.github.io/pythonqt/">PythonQt</a>.</p>
<p>But you don’t need that to get GPU information, you can just create a render window directly.</p>
<pre><code class="lang-auto">&gt;&gt;&gt; rw = vtk.vtkRenderWindow()
&gt;&gt;&gt; print(rw.ReportCapabilities())
OpenGL vendor string:  ATI Technologies Inc.
OpenGL renderer string:  AMD Radeon Pro W5700X OpenGL Engine
OpenGL version string:  4.1 ATI-4.12.7
OpenGL extensions:  
  GL_ARB_blend_func_extended
  GL_ARB_draw_buffers_blend
  GL_ARB_draw_indirect
  GL_ARB_ES2_compatibility
  GL_ARB_explicit_attrib_location
  GL_ARB_gpu_shader_fp64
  GL_ARB_gpu_shader5
  GL_ARB_instanced_arrays
  GL_ARB_internalformat_query
  GL_ARB_occlusion_query2
  GL_ARB_sample_shading
  GL_ARB_sampler_objects
  GL_ARB_separate_shader_objects
  GL_ARB_shader_bit_encoding
  GL_ARB_shader_subroutine
  GL_ARB_shading_language_include
  GL_ARB_tessellation_shader
  GL_ARB_texture_buffer_object_rgb32
  GL_ARB_texture_cube_map_array
  GL_ARB_texture_gather
  GL_ARB_texture_query_lod
  GL_ARB_texture_rgb10_a2ui
  GL_ARB_texture_storage
  GL_ARB_texture_swizzle
  GL_ARB_timer_query
  GL_ARB_transform_feedback2
  GL_ARB_transform_feedback3
  GL_ARB_vertex_attrib_64bit
  GL_ARB_vertex_type_2_10_10_10_rev
  GL_ARB_viewport_array
  GL_EXT_debug_label
  GL_EXT_debug_marker
  GL_EXT_depth_bounds_test
  GL_EXT_texture_compression_s3tc
  GL_EXT_texture_filter_anisotropic
  GL_EXT_texture_mirror_clamp
  GL_EXT_texture_sRGB_decode
  GL_APPLE_client_storage
  GL_APPLE_container_object_shareable
  GL_APPLE_flush_render
  GL_APPLE_object_purgeable
  GL_APPLE_rgb_422
  GL_APPLE_row_bytes
  GL_APPLE_texture_range
  GL_ATI_texture_mirror_once
  GL_NV_texture_barrier
PixelFormat Descriptor:
  colorSize:  0
  alphaSize:  0
  stencilSize:  0
  depthSize:  0
  accumSize:  0
  double buffer:  No
  stereo:  No
  stencil:  0
  hardware acceleration:  No
  profile version:  0x0
</code></pre>

---

## Post #6 by @BerDom.Ing (2024-04-06 16:39 UTC)

<p>Thanks, that seems like the correct solution. However, for some reason, when I try it, it shows: ‘no device context’. I’ll keep researching until I make it work.</p>

---

## Post #7 by @BerDom.Ing (2024-04-06 16:42 UTC)

<p>Already working, i had to call rw.Render() first.</p>

---

## Post #8 by @muratmaga (2024-04-06 17:30 UTC)

<aside class="quote no-group" data-username="pieper" data-post="5" data-topic="35297">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>But you don’t need that to get GPU information, you can just create a render window directly.</p>
</blockquote>
</aside>
<p>This doesnt seem to report the GPU memory size. Is there a way to get that as well? It might be a useful value and report to the user when they are trying to render something large than available gpu memory (currently only an empty 3D render window is displayed).</p>

---

## Post #9 by @pieper (2024-04-06 18:14 UTC)

<p>This call only gives you opengl info, but there are platform-specific and device-specific calls that could be added to get GPU nominal memory size.  But of course that’s only helpful if other applications aren’t already using the memory for something else, so typically the most reliable path is to try allocating memory and reporting if it fails.  One possible feature could be to determine the largest texture available and resize the volume to fit in it.</p>

---

## Post #10 by @muratmaga (2024-04-06 20:02 UTC)

<aside class="quote no-group" data-username="pieper" data-post="9" data-topic="35297">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>but there are platform-specific and device-specific calls that could be added to get GPU nominal memory size.</p>
</blockquote>
</aside>
<p>In linux <code>glxinfo</code> returns both the max and free memory like this, though I am not sure if this specific for Nvidia GPUs or not.</p>
<pre><code class="lang-auto">Memory info (GL_NVX_gpu_memory_info):
    Dedicated video memory: 40960 MB
    Total available memory: 40960 MB
    Currently available dedicated video memory: 37702 MB
</code></pre>

---

## Post #11 by @pieper (2024-04-06 20:57 UTC)

<p>Yes <code>GL_NVX</code> is an Nvidia extension, but there should be others for all platforms.</p>

---
