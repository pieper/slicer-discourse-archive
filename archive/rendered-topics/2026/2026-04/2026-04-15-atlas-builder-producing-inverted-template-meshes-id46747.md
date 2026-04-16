---
topic_id: 46747
title: "Atlas Builder Producing Inverted Template Meshes"
date: 2026-04-15
url: https://discourse.slicer.org/t/46747
---

# ATLAS - BUILDER producing inverted template meshes?

**Topic ID**: 46747
**Date**: 2026-04-15
**URL**: https://discourse.slicer.org/t/atlas-builder-producing-inverted-template-meshes/46747

---

## Post #1 by @raranda22 (2026-04-15 14:36 UTC)

<p>Hello,</p>
<p>I’ve been attempting to make a template mesh via the BUILDER module of ATLAS. I’ve made several of these with different datasets, but this time it appears the template mesh produced is “inverted”. As you can see, the surface should be bright yellow, but instead its this orangish/brownish color. Usually, these meshes have a default surface yellow color with the orange in the interior surface.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e1b4486087f7cd34504d44e155c97e399e5b59c.jpeg" data-download-href="/uploads/short-url/20N6wLZtz60oLZ5GoR2pBmcAAe8.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0e1b4486087f7cd34504d44e155c97e399e5b59c.jpeg" alt="image" data-base62-sha1="20N6wLZtz60oLZ5GoR2pBmcAAe8" width="421" height="462"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">421×462 91.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e612146b7dcd6cd81834e437ca7d9b35cbea510.jpeg" data-download-href="/uploads/short-url/kjxTQOOHsxIegFrL92hXbKWTWrS.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e612146b7dcd6cd81834e437ca7d9b35cbea510_2_690x288.jpeg" alt="image" data-base62-sha1="kjxTQOOHsxIegFrL92hXbKWTWrS" width="690" height="288" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e612146b7dcd6cd81834e437ca7d9b35cbea510_2_690x288.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e612146b7dcd6cd81834e437ca7d9b35cbea510_2_1035x432.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e612146b7dcd6cd81834e437ca7d9b35cbea510.jpeg 2x" data-dominant-color="6A6260"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1161×486 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2026-04-15 15:18 UTC)

<p>This is usually an easy fix surface toolbox, just check flip surface normals option, and then output to a new model. Not sure why they came up in the wrong direction in the first place.</p>

---

## Post #3 by @raranda22 (2026-04-15 15:59 UTC)

<p>Murat,</p>
<p>Thank you! I didn’t realize how easy that was in Surface Toolbox.</p>
<p>Best,</p>
<p>Ricardo</p>

---
