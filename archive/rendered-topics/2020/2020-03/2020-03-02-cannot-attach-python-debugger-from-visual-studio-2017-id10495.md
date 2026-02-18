# Cannot attach Python Debugger from Visual Studio 2017

**Topic ID**: 10495
**Date**: 2020-03-02
**URL**: https://discourse.slicer.org/t/cannot-attach-python-debugger-from-visual-studio-2017/10495

---

## Post #1 by @rprueckl (2020-03-02 15:11 UTC)

<p>Hi, I tried to debug a custom python scripted module using Visual Studio 2017.</p>
<p>I use Slicer 4.11.0-2020-02-26 and installed the python debugger module.</p>
<p>I followed these steps: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/DebuggingTools#Debugging_in_VisualStudio" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/Extensions/DebuggingTools - Slicer Wiki</a></p>
<p>In Visual Studio, I created my SlicerPython environment:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/67ac1664b4c3a0fe2872c0935beb1dc3a71f136d.png" data-download-href="/uploads/short-url/eN7Sg9krwTZQvFwvtFfUFE3RgL3.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/67ac1664b4c3a0fe2872c0935beb1dc3a71f136d.png" alt="image" data-base62-sha1="eN7Sg9krwTZQvFwvtFfUFE3RgL3" width="464" height="500" data-dominant-color="2F363E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">477×514 10.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I click 'Connect to VisualStudio 2017 debugger" in the module.</p>
<p>When I try to attach, an error is displayed:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e40d0ce654ce1a84afc54ca1ee5c5c4103ba05d4.png" data-download-href="/uploads/short-url/wxqP3TimGKqUf14CLZra2xIo4uw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e40d0ce654ce1a84afc54ca1ee5c5c4103ba05d4_2_686x500.png" alt="image" data-base62-sha1="wxqP3TimGKqUf14CLZra2xIo4uw" width="686" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e40d0ce654ce1a84afc54ca1ee5c5c4103ba05d4_2_686x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e40d0ce654ce1a84afc54ca1ee5c5c4103ba05d4_2_1029x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e40d0ce654ce1a84afc54ca1ee5c5c4103ba05d4_2_1372x1000.png 2x" data-dominant-color="7E7E7F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1615×1177 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The packages for my python environment show the ptvsd:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/806ed3542a4d2216759668a72630864c70b693cb.png" alt="image" data-base62-sha1="ikayDSLYuulLqMyFOTi2Yjxzb4f" width="477" height="269"></p>
<p>I don’t know what I am doing wrong, please help.</p>

---

## Post #2 by @lassoan (2020-03-02 19:17 UTC)

<p>It seems that Python tools were updated in VS2017. Could you try if you can connect if you choose “Visual Studio Code” as debugger in Slicer?</p>

---
