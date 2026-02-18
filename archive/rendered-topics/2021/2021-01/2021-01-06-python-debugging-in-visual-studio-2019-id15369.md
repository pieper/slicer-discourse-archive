# Python debugging in Visual Studio 2019

**Topic ID**: 15369
**Date**: 2021-01-06
**URL**: https://discourse.slicer.org/t/python-debugging-in-visual-studio-2019/15369

---

## Post #1 by @stephan (2021-01-06 06:16 UTC)

<p>Hi,</p>
<p>has anyone managed to attach the Visual Studio 2019 (community edition) debugger to Slicer’s python? I installed the Slicer DebuggingTools extension and followed the steps in the extension’s <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/DebuggingTools#Debugging_in_VisualStudio" rel="noopener nofollow ugc">documentation</a> for attaching SlicerPython to the Visual Studio <em>2017</em> debugger, but this seems to no longer apply to the 2019 version. There is no connection type “Python remote (ptvsd)”, just “Python remote (debugpy)”, but when I choose that one and input the target “tcp://slicer@localhost:5678” , it fails with an error message I don’t really understand (see screenshot) when I click “Find…”</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a3a835235339b68131df232fa3aa02e72eee854.png" data-download-href="/uploads/short-url/8j73w9MTXQfmp2QDctxh0N7JVVW.png?dl=1" title="grafik" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a3a835235339b68131df232fa3aa02e72eee854_2_690x389.png" alt="grafik" data-base62-sha1="8j73w9MTXQfmp2QDctxh0N7JVVW" width="690" height="389" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a3a835235339b68131df232fa3aa02e72eee854_2_690x389.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a3a835235339b68131df232fa3aa02e72eee854_2_1035x583.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a3a835235339b68131df232fa3aa02e72eee854_2_1380x778.png 2x" data-dominant-color="A1A4B1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">grafik</span><span class="informations">1519×857 65.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Has someone run into this problem before? Any advice would be greatly appreciated.</p>
<p>Thank you very much.<br>
Stephan</p>

---

## Post #2 by @lassoan (2021-01-06 15:45 UTC)

<p>Port Selector is not implemented (not necessary) for the Python debugger. See more information here: <a href="https://github.com/Microsoft/PTVS/issues/1390#issuecomment-229479669">https://github.com/Microsoft/PTVS/issues/1390#issuecomment-229479669</a></p>
<p>I’ve tried Visual Studio’s Python debugger about a year ago and it worked OK then. Visual Studio code is quite similar in capability. I usually use PyCharm because it can automatically reconnect when I restart Slicer, which is a huge convenience (you need the “professional” version, which you get for free if you are a student or have a university email address).</p>

---

## Post #3 by @stephan (2021-01-07 19:39 UTC)

<p>Thank you very much, I will give it another try soon. Otherwise I’ll install PyCharm.</p>

---
