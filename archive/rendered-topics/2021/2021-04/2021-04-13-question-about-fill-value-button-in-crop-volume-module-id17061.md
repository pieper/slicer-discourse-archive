---
topic_id: 17061
title: "Question About Fill Value Button In Crop Volume Module"
date: 2021-04-13
url: https://discourse.slicer.org/t/17061
---

# Question about "Fill value" button in "Crop Volume" module.

**Topic ID**: 17061
**Date**: 2021-04-13
**URL**: https://discourse.slicer.org/t/question-about-fill-value-button-in-crop-volume-module/17061

---

## Post #1 by @Orestis_Gaides (2021-04-13 12:59 UTC)

<p>Hello, I am researcher from Greece. I would like to ask, what does is the meaning of the option “fill value” in “crop volume” module? And what range of values is appropriate? Thanks in advance. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/ebe24f6cfd54b2aa59082280af78654459fd9235.png" data-download-href="/uploads/short-url/xEJ4wMyA0Egr51VQK7KxgLt8sHH.png?dl=1" title="Fill value" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/ebe24f6cfd54b2aa59082280af78654459fd9235_2_329x500.png" alt="Fill value" data-base62-sha1="xEJ4wMyA0Egr51VQK7KxgLt8sHH" width="329" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/ebe24f6cfd54b2aa59082280af78654459fd9235_2_329x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/ebe24f6cfd54b2aa59082280af78654459fd9235_2_493x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/ebe24f6cfd54b2aa59082280af78654459fd9235_2_658x1000.png 2x" data-dominant-color="F8F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Fill value</span><span class="informations">684×1038 36.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2021-04-13 17:32 UTC)

<p>If the ROI extends beyond the original volume anywhere the new voxels will be set to that fill value.  Sometimes, like in CT, you might want it to be an ‘air’ value like -1000.</p>

---
