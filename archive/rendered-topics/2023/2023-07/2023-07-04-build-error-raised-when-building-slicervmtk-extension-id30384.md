---
topic_id: 30384
title: "Build Error Raised When Building Slicervmtk Extension"
date: 2023-07-04
url: https://discourse.slicer.org/t/30384
---

# Build error raised when building SlicerVMTK extension

**Topic ID**: 30384
**Date**: 2023-07-04
**URL**: https://discourse.slicer.org/t/build-error-raised-when-building-slicervmtk-extension/30384

---

## Post #1 by @paul.w (2023-07-04 04:46 UTC)

<p>Build error raised when building SlicerVMTK extension <a href="https://github.com/vmtk/SlicerExtension-VMTK" rel="noopener nofollow ugc">SlicerExtension-VMTK</a> within VS2022, the  error code shows below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/2427820febdc3fba742f45addef4d7235c2d2cc6.png" data-download-href="/uploads/short-url/59PPK1IFe130Ud3dnJd185Ikyhw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/2427820febdc3fba742f45addef4d7235c2d2cc6_2_690x344.png" alt="image" data-base62-sha1="59PPK1IFe130Ud3dnJd185Ikyhw" width="690" height="344" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/2427820febdc3fba742f45addef4d7235c2d2cc6_2_690x344.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/2427820febdc3fba742f45addef4d7235c2d2cc6_2_1035x516.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/2427820febdc3fba742f45addef4d7235c2d2cc6_2_1380x688.png 2x" data-dominant-color="EAEBF1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1762×880 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The Slicer 5.3.0 has been successfully built with Release, thus the environment should be okay, which is Win11 64bit (Windows SDK version 10.0.22000.0 to target Windows 10.0.22621) + VS2022 Community + CMake 3.24.3 + C compiler (MSVC 19.36.32535.0)</p>

---

## Post #2 by @jamesobutler (2023-07-04 15:12 UTC)

<p>Xref</p>
<aside class="quote" data-post="2" data-topic="30355">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/vmtk-extension-fails-to-build-for-preview/30355/2">VMTK extension fails to build for preview</a> <a class="badge-category__wrapper " href="/c/community/vmtk/28"><span data-category-id="28" data-parent-category-id="12" data-drop-close="true" class="badge-category --has-parent" title="This is the new home of the VMTK community (moved from VMTK Google Groups)"><span class="badge-category__name">VMTK</span></span></a>
  </div>
  <blockquote>
    Thank you for reporting. We’ve noticed this, too, and working on a fix. I expect it will work again by the end of this week.
  </blockquote>
</aside>


---

## Post #3 by @lassoan (2023-07-04 15:37 UTC)

<p>The VMTK extension build error has been <a href="https://github.com/vmtk/SlicerExtension-VMTK/commit/48a071a88de626dc305134a1ac6e252fe0d5bed9">fixed</a>. The VMTK extension should be available again in Slicer Preview Releases from tomorrow.</p>

---
