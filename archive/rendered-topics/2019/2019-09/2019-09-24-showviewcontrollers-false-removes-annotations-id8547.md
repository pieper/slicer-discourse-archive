# showViewControllers(False) removes annotations

**Topic ID**: 8547
**Date**: 2019-09-24
**URL**: https://discourse.slicer.org/t/showviewcontrollers-false-removes-annotations/8547

---

## Post #1 by @aiden.zhu (2019-09-24 13:51 UTC)

<p>Operating system: windows<br>
Slicer version: 3D Slcier 4.11.0-2019-06-23</p>
<p>Expected behavior: While I try to use<br>
cap.showViewControllers(False)<br>
via the instruction here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Capture" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Capture</a>, I wold like to see annotations of mine still there</p>
<p>Actual behavior: Right now while I use cap.showViewControllers(False), all my own annotations disappear as well.</p>
<p>Is there a way I may use cap.showViewControllers(False) on the same time keeping my annotations on? Thanks a lot.</p>

---

## Post #2 by @lassoan (2019-09-24 16:04 UTC)

<aside class="quote no-group" data-username="aiden.zhu" data-post="1" data-topic="8547">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/f19dbf/48.png" class="avatar"> aiden.zhu:</div>
<blockquote>
<p>I wold like to see annotations of mine still there</p>
</blockquote>
</aside>
<p>I could not reproduce this. What annotations do you mean? Could you attach a screenshot and mark what you are missing?</p>

---

## Post #3 by @aiden.zhu (2019-09-24 16:21 UTC)

<p>I first load an image and with some annotations created by:<br>
viewer.cornerAnnotation()<br>
as shown on the following screen shot:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3ff8993499dfb0030444d4d37fa1a069eac69bec.png" data-download-href="/uploads/short-url/97UHqgawVRAkPwmEqA7gi91vzg8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3ff8993499dfb0030444d4d37fa1a069eac69bec.png" alt="image" data-base62-sha1="97UHqgawVRAkPwmEqA7gi91vzg8" width="545" height="500" data-dominant-color="908D8C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">693×635 22.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>then I do:<br>
import ScreenCapture<br>
cap = ScreenCapture.ScreenCaptureLogic()<br>
cap.showViewControllers(False)</p>
<p>after the above, I do have such screen shot as follows:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb08f81d7e3ffb3f5b876d9d0b4bed647add9f9f.png" data-download-href="/uploads/short-url/qGAvd3swrNEJnE8AO5sVpuJqtOf.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb08f81d7e3ffb3f5b876d9d0b4bed647add9f9f.png" alt="image" data-base62-sha1="qGAvd3swrNEJnE8AO5sVpuJqtOf" width="542" height="500" data-dominant-color="8A8A8A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">684×630 17.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>so you see, my own annotation has been gone after showViewControllers(False).</p>
<p>Thanks a lot!</p>

---

## Post #4 by @lassoan (2019-09-24 16:38 UTC)

<p>DataProbe module uses corner annotations to display information. You can override it temporarily but on the next update, DataProbe will reset the displayed texts. Apparently, <code>showViewControllers</code> triggers a DataProbe update, so you need to set your custom corner annotation after calling <code>showViewControllers</code>.</p>

---

## Post #5 by @aiden.zhu (2019-09-24 21:29 UTC)

<p>Thanks a lot! It works!</p>

---
