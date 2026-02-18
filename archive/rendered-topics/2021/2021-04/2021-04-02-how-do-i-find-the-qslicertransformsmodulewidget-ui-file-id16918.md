# How do i find the qslicerTransformsModuleWidget.ui file

**Topic ID**: 16918
**Date**: 2021-04-02
**URL**: https://discourse.slicer.org/t/how-do-i-find-the-qslicertransformsmodulewidget-ui-file/16918

---

## Post #1 by @Carl098 (2021-04-02 06:54 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/2434b4588cec693ceff1d62f373f1bb68da10100.png" alt="image" data-base62-sha1="5ai6GdaOAGEh4YARh9tmL0ewQPS" width="406" height="331"><br>
I’d like to use the Transforms module UI file and invoke some widgets.<br>
I use Python language, but I can’t do that like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed9f50ac0f8d05fa80b90dcd16ad6e6c2ac91084.png" data-download-href="/uploads/short-url/xU6utCUJ6Z1pR6xczErDuzhSZ2k.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed9f50ac0f8d05fa80b90dcd16ad6e6c2ac91084.png" alt="image" data-base62-sha1="xU6utCUJ6Z1pR6xczErDuzhSZ2k" width="690" height="29" data-dominant-color="2D2D2D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1030×44 2.58 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-04-03 01:22 UTC)

<p>Module widgets are not designed to be reusable from other modules. It is for internal use of the module. However, since module widgets are assembled from high-level widgets, you can place those widgets into your own module widget. You can open the .ui file in Qt Designer and see what widgets are used and you can see in the module widget cxx file how they are used (what connections are set, etc.).</p>

---
