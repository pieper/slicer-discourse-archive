---
topic_id: 2758
title: "Slicer Nightly Version Does Not Launch On Windows"
date: 2018-05-04
url: https://discourse.slicer.org/t/2758
---

# Slicer nightly version does not launch on windows

**Topic ID**: 2758
**Date**: 2018-05-04
**URL**: https://discourse.slicer.org/t/slicer-nightly-version-does-not-launch-on-windows/2758

---

## Post #1 by @zjx1805 (2018-05-04 03:47 UTC)

<p>I installed the latest nightly build (v4.9.0, built on 05/02) on my desktop and when I opened it, it disappeared after just showing a loading screen. I tried a dozen of times, and only for one time it launched, but the interface looks something like below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d9253e188693cca01d7642f9be8d4efc801a2e2.png" data-download-href="/uploads/short-url/4dBlPTfwEyYnaPWOGVJXZ0BKEaS.png?dl=1" title="aaa" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d9253e188693cca01d7642f9be8d4efc801a2e2_2_690x432.png" alt="aaa" data-base62-sha1="4dBlPTfwEyYnaPWOGVJXZ0BKEaS" width="690" height="432" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d9253e188693cca01d7642f9be8d4efc801a2e2_2_690x432.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d9253e188693cca01d7642f9be8d4efc801a2e2_2_1035x648.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d9253e188693cca01d7642f9be8d4efc801a2e2.png 2x" data-dominant-color="FBFCFC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">aaa</span><span class="informations">1307×819 26.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The picture above comes from another earlier nightly build but also suffered from the same problem. You can vaguely see the interface but it looks like for some reason it becomes transparent. I have stable 4.8.1 version installed and it works fine. I tried to install the same nightly build on my older laptop, which also has 4.8.1 version installed, and that nightly build seems to work just fine. The specifications of my desktop are: i7-6700k+gtx1080+windows10 64 bit. Any ideas on how to solve this is greatly appreciated!</p>

---

## Post #2 by @lassoan (2018-05-04 04:03 UTC)

<p>This looks like a graphics card driver bug. Are you using latest graphics card driver version?</p>
<p>Could you please also try erasing (or temporarily moving somewhere else) your <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/DirectoryStructure#API">Slicer.ini and Slicer-NNN.ini files</a> and try again?</p>
<p>Could you try downloading and running a recent version of <a href="https://www.paraview.org/download/">Paraview</a>? Does it work well?</p>

---

## Post #3 by @zjx1805 (2018-05-04 04:28 UTC)

<p>Thank you Iassoan for such a quick reply! Yes I am using the latest driver version (v391.35 in Geforce Experience software, v24.21.13.9731 in device manager). I can only find Slicer.ini but not Slicer-NNN.ini file and removing the Slicer.ini file does not help. I also tried installing Paraview v5.5 and it also fails to launch, throwing an OpenGL driver error. The complete error message is as follows:</p>
<pre><code>ERROR: In C:\bbd\7cc78367\build\superbuild\paraview\src\VTK\Rendering\OpenGL2\vtkWin32OpenGLRenderWindow.cxx, line 685
vtkWin32OpenGLRenderWindow (000001D8CFFD40A0): failed to get wglChoosePixelFormatARB

ERROR: In C:\bbd\7cc78367\build\superbuild\paraview\src\VTK\Rendering\OpenGL2\vtkWin32OpenGLRenderWindow.cxx, line 769
vtkWin32OpenGLRenderWindow (000001D8CFFD40A0): failed to get valid pixel format.

ERROR: In C:\bbd\7cc78367\build\superbuild\paraview\src\VTK\Rendering\OpenGL2\vtkOpenGLRenderWindow.cxx, line 781
vtkWin32OpenGLRenderWindow (000001D8CFFD40A0): GLEW could not be initialized.

ERROR: In C:\bbd\7cc78367\build\superbuild\paraview\src\VTK\Rendering\OpenGL2\vtkOpenGLRenderWindow.cxx, line 781
vtkWin32OpenGLRenderWindow (000001D8CFFD40A0): GLEW could not be initialized.

ERROR: In C:\bbd\7cc78367\build\superbuild\paraview\src\VTK\Rendering\OpenGL2\vtkWin32OpenGLRenderWindow.cxx, line 685
vtkWin32OpenGLRenderWindow (000001D8D61D65F0): failed to get wglChoosePixelFormatARB

ERROR: In C:\bbd\7cc78367\build\superbuild\paraview\src\VTK\Rendering\OpenGL2\vtkWin32OpenGLRenderWindow.cxx, line 769
vtkWin32OpenGLRenderWindow (000001D8D61D65F0): failed to get valid pixel format.

ERROR: In C:\bbd\7cc78367\build\superbuild\paraview\src\VTK\Rendering\OpenGL2\vtkOpenGLRenderWindow.cxx, line 781
vtkWin32OpenGLRenderWindow (000001D8D61D65F0): GLEW could not be initialized.

ERROR: In C:\bbd\7cc78367\build\superbuild\paraview\src\VTK\Rendering\OpenGL2\vtkOpenGLRenderWindow.cxx, line 781
vtkWin32OpenGLRenderWindow (000001D8D61D65F0): GLEW could not be initialized.

ERROR: In C:\bbd\7cc78367\build\superbuild\paraview\src\VTK\Rendering\OpenGL2\vtkWin32OpenGLRenderWindow.cxx, line 685
vtkWin32OpenGLRenderWindow (000001D8D61D65F0): failed to get wglChoosePixelFormatARB

ERROR: In C:\bbd\7cc78367\build\superbuild\paraview\src\VTK\Rendering\OpenGL2\vtkWin32OpenGLRenderWindow.cxx, line 769
vtkWin32OpenGLRenderWindow (000001D8D61D65F0): failed to get valid pixel format.

ERROR: In C:\bbd\7cc78367\build\superbuild\paraview\src\VTK\Rendering\OpenGL2\vtkOpenGLRenderWindow.cxx, line 781
vtkWin32OpenGLRenderWindow (000001D8D61D65F0): GLEW could not be initialized.

ERROR: In C:\bbd\7cc78367\build\superbuild\paraview\src\VTK\Rendering\OpenGL2\vtkOpenGLRenderWindow.cxx, line 781
vtkWin32OpenGLRenderWindow (000001D8D61D65F0): GLEW could not be initialized.

ERROR: In C:\bbd\7cc78367\build\superbuild\paraview\src\VTK\Rendering\OpenGL2\vtkWin32OpenGLRenderWindow.cxx, line 685
vtkWin32OpenGLRenderWindow (000001D8D61D65F0): failed to get wglChoosePixelFormatARB

ERROR: In C:\bbd\7cc78367\build\superbuild\paraview\src\VTK\Rendering\OpenGL2\vtkWin32OpenGLRenderWindow.cxx, line 769
vtkWin32OpenGLRenderWindow (000001D8D61D65F0): failed to get valid pixel format.

ERROR: In C:\bbd\7cc78367\build\superbuild\paraview\src\VTK\Rendering\OpenGL2\vtkOpenGLRenderWindow.cxx, line 781
vtkWin32OpenGLRenderWindow (000001D8D61D65F0): GLEW could not be initialized.

ERROR: In C:\bbd\7cc78367\build\superbuild\paraview\src\VTK\Rendering\OpenGL2\vtkOpenGLRenderWindow.cxx, line 781
vtkWin32OpenGLRenderWindow (000001D8D61D65F0): GLEW could not be initialized.
</code></pre>
<p>So it does seem like a graphics card driver issue. I am wondering if there is a fix to this? Thanks!</p>

---

## Post #4 by @lassoan (2018-05-04 04:43 UTC)

<p>Report the error to Paraview developers, maybe they have some more hints.</p>
<p>What computer is this (laptop/desktop)? Does it have additional video cards? Does it have any other special hardware? Do you have Nahimic sound device?</p>

---

## Post #5 by @zjx1805 (2018-05-04 04:54 UTC)

<p>The one that is having problem is a desktop and it only has one video card (gtx1080). The other hardware are pretty standard in my opinion (1T SSD+2T HDD+16GB RAM+dual monitors+Logitech G430 headphone, please let me know if you are referring to other hardware). I don’t have Nahimic sound device and all I have are NVIDIA High Definition Audio + NVIDIA Virtual Audio Device (Wave Extensible) (WDM) + Realtek High Definition Audio + Logitech G430 headphone. The nightly build runs well on my old laptop probably because the video cards are old (Intel HD4600+GT755M) and the drivers are also outdated for some time. Since it is a video card driver issue, does that mean I probably would not be able to use any newer version of slicer than 4.8.1 in the near future?</p>
<p>Update:<br>
I upgraded the NVIDIA video card driver to the latest one (397.31). Now the Paraview no longer throws OpenGL drive error at startup, however, it now looks exactly like nightly build of slicer: semi-transparent interface as below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f4fb406bea53dee59ca30e2c246f4bc965b6de7d.jpeg" data-download-href="/uploads/short-url/yXcO1X8CKPQTmIDRN0CIUlxAwUt.jpg?dl=1" title="bbb" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f4fb406bea53dee59ca30e2c246f4bc965b6de7d_2_690x478.jpg" alt="bbb" data-base62-sha1="yXcO1X8CKPQTmIDRN0CIUlxAwUt" width="690" height="478" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f4fb406bea53dee59ca30e2c246f4bc965b6de7d_2_690x478.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f4fb406bea53dee59ca30e2c246f4bc965b6de7d_2_1035x717.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f4fb406bea53dee59ca30e2c246f4bc965b6de7d.jpeg 2x" data-dominant-color="AFB1B8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">bbb</span><span class="informations">1218×845 495 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @lassoan (2018-05-04 16:01 UTC)

<p>I would recommend to raise this issue on ParaView mailing list. They may have more clue about how to address this.</p>

---

## Post #7 by @zjx1805 (2018-05-04 16:18 UTC)

<p>Thank you anyway for your help! I would update this post if Paraview people are able to solve this.</p>

---
