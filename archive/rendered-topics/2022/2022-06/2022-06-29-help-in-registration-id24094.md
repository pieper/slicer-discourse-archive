# Help in registration

**Topic ID**: 24094
**Date**: 2022-06-29
**URL**: https://discourse.slicer.org/t/help-in-registration/24094

---

## Post #1 by @mohammed_alshakhas (2022-06-29 05:42 UTC)

<p>I’m trying to register two head and neck ct volumes with BRAINS , yet I’m not having a good result, any suggestions?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/561fbfd3b9fbe23b70c3be93c8ffe05b2c8d1570.jpeg" data-download-href="/uploads/short-url/chT5h1a3sFQRUqPZEryfRBWhc8o.jpeg?dl=1" title="Screen Shot 2022-06-27 at 16.32.29" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/561fbfd3b9fbe23b70c3be93c8ffe05b2c8d1570_2_690x431.jpeg" alt="Screen Shot 2022-06-27 at 16.32.29" data-base62-sha1="chT5h1a3sFQRUqPZEryfRBWhc8o" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/561fbfd3b9fbe23b70c3be93c8ffe05b2c8d1570_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/561fbfd3b9fbe23b70c3be93c8ffe05b2c8d1570_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/561fbfd3b9fbe23b70c3be93c8ffe05b2c8d1570_2_1380x862.jpeg 2x" data-dominant-color="999997"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-06-27 at 16.32.29</span><span class="informations">1920×1200 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2022-08-04 06:17 UTC)

<p>I would recommend to remove the u-shaped head holder (e.g., using Mask volume effect in Segment Editor) before registration.</p>
<p>You may also need to tune registration parameters, because BRAINS often does not work well with the default settings. Alternatively, you can use SlicerElastix or SlicerANTs extension, because they typically provide good registration results with default settings.</p>

---
