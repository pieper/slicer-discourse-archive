# Warping transform from fiducial registration doesnt work with volumes

**Topic ID**: 28978
**Date**: 2023-04-18
**URL**: https://discourse.slicer.org/t/warping-transform-from-fiducial-registration-doesnt-work-with-volumes/28978

---

## Post #1 by @muratmaga (2023-04-18 01:29 UTC)

<p>I have created a warping transfrom from two landmark sets. The resultant transform can be successfully applied to a 3D model (see the screenshot, green model is under the resultant transform, and has a slight deformation compared to the skull its generated from).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc9efb0a1e213ca4640aaa80f492631a56398fb9.jpeg" data-download-href="/uploads/short-url/qUCnukBOgysEUAaixxrQc5iXI5H.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc9efb0a1e213ca4640aaa80f492631a56398fb9_2_690x484.jpeg" alt="image" data-base62-sha1="qUCnukBOgysEUAaixxrQc5iXI5H" width="690" height="484" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc9efb0a1e213ca4640aaa80f492631a56398fb9_2_690x484.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc9efb0a1e213ca4640aaa80f492631a56398fb9_2_1035x726.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc9efb0a1e213ca4640aaa80f492631a56398fb9.jpeg 2x" data-dominant-color="BBB9C7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1253×880 80.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>However, when I put the volume under the same transform, I get strange deformation.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a85edecf5ea94dcc52d5087932dfa8e1bd72eee.jpeg" data-download-href="/uploads/short-url/3MDm6VClsAHYP9oOJyJ0OKQSGB0.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a85edecf5ea94dcc52d5087932dfa8e1bd72eee_2_690x358.jpeg" alt="image" data-base62-sha1="3MDm6VClsAHYP9oOJyJ0OKQSGB0" width="690" height="358" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a85edecf5ea94dcc52d5087932dfa8e1bd72eee_2_690x358.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a85edecf5ea94dcc52d5087932dfa8e1bd72eee.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a85edecf5ea94dcc52d5087932dfa8e1bd72eee.jpeg 2x" data-dominant-color="BDBDD7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">989×514 68.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>How can we make the warping transform work with volumes? Performance is rather slow with 3D models with large number of vertices, so I am testing if volume rendering can be used instead.</p>

---

## Post #2 by @pieper (2023-04-18 19:40 UTC)

<p>Probably you are seeing this issue?</p>
<aside class="quote quote-modified" data-post="4" data-topic="19001">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/understanding-ct-image-spacing-and-acquisition-geometry-regularization/19001/4">Understanding CT Image spacing and Acquisition geometry regularization</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    This is probably correct because the volume rendering doesn’t take non-linear transforms like the acquisition correction into account.  You can confirm this by making the slice views visible in the 3D view and they won’t match until you harden.  It needs to be fixed at the VTK level, and we’ve discussed it but it hasn’t been done yet as far as I know.  The volume rendering module should really generate a visible warning or error dialog when a volume with a nonlinear transform is selected. 
In an…
  </blockquote>
</aside>


---

## Post #3 by @muratmaga (2023-04-18 20:35 UTC)

<p>yes, apparently! (Slice view is correct). Meanwhile, is there a way to mitigate? Can I somehow use this transform to resample the image and render correctly?</p>

---

## Post #4 by @muratmaga (2023-04-18 20:38 UTC)

<p>Ok, it worked with resample. But it would be great if it can be done on the fly.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cbdc1aae2a311bf61f5b5de11a582862b6c4c614.jpeg" data-download-href="/uploads/short-url/t5quQQeV3gdHa7ctihXTSZlsf4g.jpeg?dl=1" title="Screen Shot 2023-04-18 at 1.38.15 PM"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cbdc1aae2a311bf61f5b5de11a582862b6c4c614_2_390x500.jpeg" alt="Screen Shot 2023-04-18 at 1.38.15 PM" data-base62-sha1="t5quQQeV3gdHa7ctihXTSZlsf4g" width="390" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cbdc1aae2a311bf61f5b5de11a582862b6c4c614_2_390x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cbdc1aae2a311bf61f5b5de11a582862b6c4c614_2_585x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cbdc1aae2a311bf61f5b5de11a582862b6c4c614_2_780x1000.jpeg 2x" data-dominant-color="8E8992"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2023-04-18 at 1.38.15 PM</span><span class="informations">994×1272 199 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @pieper (2023-04-18 20:53 UTC)

<p>Yes, agreed, we should perform the hardening step as part of the volume rendering displayable manager (one of the many improvements that are needed in the volume rendering module).</p>

---
