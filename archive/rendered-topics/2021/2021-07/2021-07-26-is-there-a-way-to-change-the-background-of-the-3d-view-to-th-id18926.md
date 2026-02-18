# Is there a way to change the background of the 3D view to the dynamic content of the computer camera?

**Topic ID**: 18926
**Date**: 2021-07-26
**URL**: https://discourse.slicer.org/t/is-there-a-way-to-change-the-background-of-the-3d-view-to-the-dynamic-content-of-the-computer-camera/18926

---

## Post #1 by @slicer365 (2021-07-26 08:40 UTC)

<p>I want to use slicer to implement  AR technology,</p>
<p>which means I need to set the background of the 3D model to the real content captured by the computer camera.</p>
<p>Is there a way to change the background of the 3D view to the dynamic content of the computer camera?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb30e2e32069757bd1e247ba661edd96c41cc3a6.png" data-download-href="/uploads/short-url/qHY1zpGI0gCEPxEPAVD1WbHPItU.png?dl=1" title="捕获" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb30e2e32069757bd1e247ba661edd96c41cc3a6_2_517x355.png" alt="捕获" data-base62-sha1="qHY1zpGI0gCEPxEPAVD1WbHPItU" width="517" height="355" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb30e2e32069757bd1e247ba661edd96c41cc3a6_2_517x355.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bb30e2e32069757bd1e247ba661edd96c41cc3a6_2_775x532.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb30e2e32069757bd1e247ba661edd96c41cc3a6.png 2x" data-dominant-color="33333D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">捕获</span><span class="informations">908×625 17.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2021-07-26 14:22 UTC)

<p>If you are willing to write some python scripts, you can create a model node with a texture from the video.  There’s some <a href="https://github.com/pieper/facenav">example code</a> you can look at.</p>
<p>But for AR in general you can look at the status of these projects: <a href="https://projectweek.na-mic.org/PW35_2021_Virtual/#vrar-and-rendering" class="inline-onebox">Welcome to the web page for the 35th Project Week! | NA-MIC Project Weeks</a></p>

---
