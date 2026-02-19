---
topic_id: 21486
title: "Plots Axes Not Shown In Slicer 4 13 But Works With 4 11"
date: 2022-01-16
url: https://discourse.slicer.org/t/21486
---

# Plot's axes not shown in Slicer 4.13 (but works with 4.11)

**Topic ID**: 21486
**Date**: 2022-01-16
**URL**: https://discourse.slicer.org/t/plots-axes-not-shown-in-slicer-4-13-but-works-with-4-11/21486

---

## Post #1 by @keri (2022-01-16 18:27 UTC)

<p>Hi,</p>
<p>I wanted to report that in <strong>Slicer 4.13.0-2021-08-27</strong>  plot’s axes are not visible but in the same time <strong>Slicer 4.11.20210226</strong> (stable release as I remember) works fine:<br>
The code I have used is <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Plots#Constructing_a_plot" rel="noopener nofollow ugc">from the documentation</a><br>
<strong>Ubuntu 20.04</strong></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce60f3619d8dba96606918cc1f916cc8d6b156d2.png" data-download-href="/uploads/short-url/trI4DI7xWlNvYtWpZNMm5nw4IIW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce60f3619d8dba96606918cc1f916cc8d6b156d2_2_690x341.png" alt="image" data-base62-sha1="trI4DI7xWlNvYtWpZNMm5nw4IIW" width="690" height="341" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce60f3619d8dba96606918cc1f916cc8d6b156d2_2_690x341.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce60f3619d8dba96606918cc1f916cc8d6b156d2.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce60f3619d8dba96606918cc1f916cc8d6b156d2.png 2x" data-dominant-color="A5A7BD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">817×404 98.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42d42e50251190b42972c6b19f4391d810a7aa20.png" data-download-href="/uploads/short-url/9xc6JhmPqAA2hfK3xPF3JQprax2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/42d42e50251190b42972c6b19f4391d810a7aa20.png" alt="image" data-base62-sha1="9xc6JhmPqAA2hfK3xPF3JQprax2" width="690" height="371" data-dominant-color="BEC0D5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">742×399 113 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2022-01-16 21:15 UTC)

<p>Thanks for reporting <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<p>The axes are visible in a recent preview on mac.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/759184b146d5cab3c517204031f6909f66bddb30.png" data-download-href="/uploads/short-url/gM3DplEpfDuposFjqH9NE1Vfuy4.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/759184b146d5cab3c517204031f6909f66bddb30_2_690x427.png" alt="image" data-base62-sha1="gM3DplEpfDuposFjqH9NE1Vfuy4" width="690" height="427" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/759184b146d5cab3c517204031f6909f66bddb30_2_690x427.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/759184b146d5cab3c517204031f6909f66bddb30.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/759184b146d5cab3c517204031f6909f66bddb30.png 2x" data-dominant-color="92918E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">777×481 29.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But on my ubuntu 20.04 with a current build I get the missing axes and this message:</p>
<pre><code class="lang-auto">Generic Warning: In /home/pieper/slicer4/latest/Slicer-superbuild/VTK/Rendering/OpenGL2/vtkOpenGLFramebufferObject.cxx, line 1390
failed at glBlitFramebuffer 1 OpenGL errors detected
  0 : (1282) Invalid operation



Generic Warning: In /home/pieper/slicer4/latest/Slicer-superbuild/VTK/Rendering/OpenGL2/vtkOpenGLFramebufferObject.cxx, line 1390
failed at glBlitFramebuffer 1 OpenGL errors detected
  0 : (1282) Invalid operation



</code></pre>
<p>This looks like a VTK incompatibility of some kind.  It would be good to check if it can be reproduced in pure VTK and reported there.</p>

---

## Post #3 by @keri (2022-01-16 21:43 UTC)

<p>Forget to mention that I also get this error.</p>
<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="21486">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>This looks like a VTK incompatibility of some kind. It would be good to check if it can be reproduced in pure VTK and reported there.</p>
</blockquote>
</aside>
<p>To clarify a little: you mean to build Slicer with <a href="https://github.com/Kitware/VTK" rel="noopener nofollow ugc">VTK from original git repository</a> tagged under <code>v9.1.0</code>? If so I think I could do that.<br>
As I can see Slicer uses custom VTK from <a>Slicer’s repo</a></p>

---

## Post #4 by @pieper (2022-01-16 22:39 UTC)

<p>I meant it would be good to know if this is an issue with VTK itself, or something related to Slicer’s edits or the way we build it.  You could try starting with a pure VTK example to see if you get the same issues.</p>
<p><a href="https://kitware.github.io/vtk-examples/site/Cxx/Plotting/LinePlot/" class="onebox" target="_blank" rel="noopener">https://kitware.github.io/vtk-examples/site/Cxx/Plotting/LinePlot/</a></p>

---

## Post #5 by @keri (2022-01-16 23:10 UTC)

<p>It seems that VTK 9 which is used by <a href="https://github.com/slicer/VTK.git" rel="noopener nofollow ugc">Slicer</a> under git tag <code>98d686bb509f46543ebe04fdd5d120fdab87893b</code> (slicer-v9.0.20201111-733234c785-v3)  works fine with the given example:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/dff9c079f13dc33c3cdd7c50b111eb4cd9eb1472.png" alt="image" data-base62-sha1="vXnz8Nehn3N2wjpOIY8ndnpzM5A" width="300" height="337"></p>
<p>I should mention that the script given by VTK is in fact needed as without it the app breaks at start:</p>
<pre data-code-wrap="cmake"><code class="lang-cmake">  # vtk_module_autoinit is needed
  vtk_module_autoinit(
    TARGETS LinePlot
    MODULES ${VTK_LIBRARIES}
    )
</code></pre>
<p>the error without <code>vtk_module_autoinit</code>:<br>
<strong>2022-01-17 02:04:48.988 (   0.051s) [        5E1A0940] vtkContextDevice2D.cxx:32    WARN| Error: no override found for ‘vtkContextDevice2D’.<br>
Segmentation fault (core dumped)</strong></p>

---

## Post #6 by @pieper (2022-01-17 13:42 UTC)

<p>Thanks for checking - this suggests maybe it’s something about VTK and Qt at the OpenGL level.  If you have more time to look at this you might explore porting that example to CTK or ideally a native VTK/Qt example to see what exactly is broken.</p>

---

## Post #7 by @keri (2022-01-17 16:26 UTC)

<p>Hi,</p>
<p>I just downloaded the <a href="https://kitware.github.io/vtk-examples/site/Cxx/Qt/BarChartQt/" rel="noopener nofollow ugc">VTK Qt BarChartQt example</a> and build it preliminary added <code>find_package(Slicer REQUIRED)</code> to the <code>CMakeLists.txt</code>. This allows to find VTK and Qt that were used to compile Slicer (Slicer’s custom VTK).<br>
The example works fine:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/eaaffdd24d7a230817e8f00f7936237ae75e709f.png" data-download-href="/uploads/short-url/xu8MRvBtVJFojXQ1LAelpmZOKaX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/eaaffdd24d7a230817e8f00f7936237ae75e709f_2_589x500.png" alt="image" data-base62-sha1="xu8MRvBtVJFojXQ1LAelpmZOKaX" width="589" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/eaaffdd24d7a230817e8f00f7936237ae75e709f_2_589x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/eaaffdd24d7a230817e8f00f7936237ae75e709f.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/eaaffdd24d7a230817e8f00f7936237ae75e709f.png 2x" data-dominant-color="C7C2B6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">654×555 92.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The example uses <code>QVTKOpenGLNativeWidget</code> and sets <code>QSurfaceFormat::setDefaultFormat(QVTKOpenGLNativeWidget::defaultFormat());</code><br>
I don’t know how excatly OpenGL related staff works but here are my thoughts (I write this maybe because probably I will refer to this later):</p>
<ul>
<li>
<p><a href="https://github.com/Slicer/Slicer/blob/cb3a1ff14fac3419f3e3f08632a6cac6bedb52ca/Libs/MRML/Widgets/qMRMLWidget.cxx#L89-L129" rel="noopener nofollow ugc">qMRMLWidget</a> set some <code>QSurfaceFormat</code> property and it differs for Windows;</p>
</li>
<li>
<p>Slicer uses <code>QVTKOpenGLNativeWidget</code> through <code>ctkVTKOpenGLNativeWidget</code> (inherits <code>QVTKOpenGLNativeWidget</code>) wich in concluded in macros and in my case it looks this way:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a26812e9d16b54969863a01cb1343a38f022fa92.jpeg" data-download-href="/uploads/short-url/naIkiNXpdkhzHS9az0ZkDtpdcS6.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a26812e9d16b54969863a01cb1343a38f022fa92_2_446x375.jpeg" alt="image" data-base62-sha1="naIkiNXpdkhzHS9az0ZkDtpdcS6" width="446" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a26812e9d16b54969863a01cb1343a38f022fa92_2_446x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a26812e9d16b54969863a01cb1343a38f022fa92_2_669x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a26812e9d16b54969863a01cb1343a38f022fa92.jpeg 2x" data-dominant-color="F4F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">866×727 124 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p><code>ctkVTKChartView</code> inherits from <code>ctkVTKOpenGLNativeWidget</code></p>
</li>
<li>
<p><code>qMRMLPlotView</code> inherits from <code>ctkVTKChartView</code></p>
</li>
</ul>
<p>I have tested all of these VTK OpenGL widgets (<code>QVTKOpenGLNativeWidget</code>, <code>ctkVTKOpenGLNativeWidget</code>, <code>ctkVTKChartView</code>, <code>qMRMLPlotView</code>) and all of them work.</p>
<p>I uploaded this slightly modified <a href="https://drive.google.com/file/d/1rsf60p6llagFHoN-ECHLlgA_vdO2EPSd/view?usp=sharing" rel="noopener nofollow ugc">BarChartQt_Slicer</a> example so you can try to configure and build it using <code>cmake .. -DSlicer_DIR=/path/to/Slicer-build</code> and the application should be run from Slicer environment <code>./Slicer --launch BarChartQt</code> (I usually laucn vscode this way <code>./Slicer --launch code</code> and then I can simply run the app using <code>./BarChartQt</code> from the build folder)</p>
<p>The modifications are made in <code>CMakeLists.txt</code> aimed to find Slicer and CTK and link them.<br>
And in <code>BarChartQt</code> where I do <code>include &lt;&gt;</code> and delete <code>QVTKOpenGLNativeWidget</code> and create any derived widget (code lines 50-107).</p>

---

## Post #8 by @keri (2022-03-15 23:42 UTC)

<p>I just rebuilt Slicer with the newest commit <a href="https://github.com/Slicer/Slicer/commit/d14f18f386f83943d6717cedb5d18f1ce423cada" rel="noopener nofollow ugc">d14f18f386f83943d6717cedb5d18f1ce423cada</a> and noticed the problem seems to be solved.</p>
<p>Thank you</p>

---

## Post #9 by @keri (2022-03-17 13:20 UTC)

<p>Oh, it seems I simply didn’t notice the warnings even though the axes are shown:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f0295eec67dbddf96e99fa5038439b24cdcf146.png" alt="image" data-base62-sha1="bgXg7eRHbK99jXi7jvXYGtlcixM" width="431" height="296"></p>
<pre><code class="lang-auto">Generic Warning: In /home/kerim/Documents/Colada/d/VTK/Rendering/OpenGL2/vtkOpenGLState.cxx, line 1069
Error glEnable/Disable1 OpenGL errors detected
  0 : (1282) Invalid operation

 with stack trace of
0x7f7d4638400c : ??? [(???) ???:-1]
0x7f7d4637e921 : vtksys::SystemInformation::GetProgramStack[abi:cxx11](int, int) [(libvtksys-9.1.so.1) ???:-1]
0x7f7d50c7a03a : ??? [(???) ???:-1]
0x7f7d50c7ddb2 : vtkOpenGLState::SetEnumState(unsigned int, bool) [(libvtkOpenGL-9.1.so.1) ???:-1]
0x7f7d50b02707 : ??? [(???) ???:-1]
0x7f7d50c812d3 : vtkOpenGLState::vtkglBlitFramebuffer(int, int, int, int, int, int, int, int, unsigned int, unsigned int) [(libvtkOpenGL-9.1.so.1) ???:-1]
0x7f7d50d19897 : vtkTextureObject::CopyFromFrameBuffer(int, int, int, int, int, int) [(libvtkOpenGL-9.1.so.1) ???:-1]
0x7f7d50b946c0 : vtkOpenGLFXAAFilter::LoadInput() [(libvtkOpenGL-9.1.so.1) ???:-1]
0x7f7d50b939c3 : vtkOpenGLFXAAFilter::Execute(vtkOpenGLRenderer*) [(libvtkOpenGL-9.1.so.1) ???:-1]
0x7f7d50c5689c : vtkOpenGLRenderer::UpdateGeometry(vtkFrameBufferObjectBase*) [(libvtkOpenGL-9.1.so.1) ???:-1]
0x7f7d50c55a51 : vtkOpenGLRenderer::DeviceRender() [(libvtkOpenGL-9.1.so.1) ???:-1]

and it continues for many many lines
</code></pre>

---

## Post #10 by @lassoan (2022-03-17 15:39 UTC)

<p>You can try disabling FXAA anti-aliasing and see if the messages go away. It is turned on in Slicer or CTK, you should be able to find it by searching for FXAA.</p>

---
