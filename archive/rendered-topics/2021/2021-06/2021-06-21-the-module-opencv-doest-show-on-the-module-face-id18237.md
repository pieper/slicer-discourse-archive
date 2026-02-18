# The Module, OpenCV,does't show on the Module face

**Topic ID**: 18237
**Date**: 2021-06-21
**URL**: https://discourse.slicer.org/t/the-module-opencv-doest-show-on-the-module-face/18237

---

## Post #1 by @slicer365 (2021-06-21 01:28 UTC)

<p>Sys:WIN 64<br>
V 4.1120210226</p>
<p>As is this pic.,I have installed the  OpenCV ,</p>
<p>but when I restart the Slicer ,</p>
<p>I dont find it on the Module face.</p>
<p>I searched all modules,no result.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78f2783899fa739795792585992626fcb55fdac9.png" data-download-href="/uploads/short-url/hfWMGkpBCkXVcAT4wW6LhEtSI9b.png?dl=1" title="捕获" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78f2783899fa739795792585992626fcb55fdac9_2_517x352.png" alt="捕获" data-base62-sha1="hfWMGkpBCkXVcAT4wW6LhEtSI9b" width="517" height="352" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78f2783899fa739795792585992626fcb55fdac9_2_517x352.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78f2783899fa739795792585992626fcb55fdac9_2_775x528.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78f2783899fa739795792585992626fcb55fdac9.png 2x" data-dominant-color="E3E3EF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">捕获</span><span class="informations">1001×683 77.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-06-21 04:37 UTC)

<p>OpenCV extension does not provide any module, it just installs OpenCV. However, in current Slicer versions you probably don’t need the OpenCV extension anymore. You can just call <code>slicer.util.pip_install('opencv')</code> to install OpenCV.</p>

---
