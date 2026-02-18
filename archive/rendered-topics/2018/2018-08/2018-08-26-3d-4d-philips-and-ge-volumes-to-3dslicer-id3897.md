# 3D / 4D Philips and GE volumes to 3dSlicer

**Topic ID**: 3897
**Date**: 2018-08-26
**URL**: https://discourse.slicer.org/t/3d-4d-philips-and-ge-volumes-to-3dslicer/3897

---

## Post #1 by @diogopmartins (2018-08-26 16:27 UTC)

<p>Dear all,</p>
<p>I need some help to import 3d volume data from Philips epic7 and GE e95 to 3dSlicer.</p>
<p>I installed SlicerHeart with  Philips 4D patcher. I can convert those files because show this message:</p>
<p>Examining ./us003.dcm…<br>
Not Philips 4D ultrasound DICOM file. Skipped.<br>
DICOM patching completed.</p>
<p>Also when I try to import those volumes directly that shows like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/4613716ba49589b0d9b5961dd624e14c9caa6ba0.png" data-download-href="/uploads/short-url/9ZV4Vue5JODDT6L85EG7GAsUpMs.png?dl=1" title="47" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4613716ba49589b0d9b5961dd624e14c9caa6ba0_2_566x499.png" alt="47" data-base62-sha1="9ZV4Vue5JODDT6L85EG7GAsUpMs" width="566" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4613716ba49589b0d9b5961dd624e14c9caa6ba0_2_566x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4613716ba49589b0d9b5961dd624e14c9caa6ba0_2_849x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4613716ba49589b0d9b5961dd624e14c9caa6ba0_2_1132x998.png 2x" data-dominant-color="434A57"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">47</span><span class="informations">1662×1468 140 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Same for GE volumes.</p>
<p>Not sure what I’m doing wrong.</p>
<p>Many thanks!</p>

---

## Post #2 by @lassoan (2018-08-26 19:47 UTC)

<p>You are not doing anything wrong. Unfortunately, ultrasound devices usually do not store 3D/4D image data in standard DICOM fields and therefore there are limitations of what and how can be loaded. See details in <a href="https://github.com/SlicerHeart/SlicerHeart">documentation of SlicerHeart extension</a>.</p>

---
