---
topic_id: 48044
title: "Segmentations Module - Opacity Issue"
date: 2026-09-02
url: https://discourse.slicer.org/t/48044
last_bumped: 2026-09-02T18:26:59.254Z
---

# Segmentations Module - Opacity Issue

**Topic ID**: 48044
**Date**: 2026-09-02
**URL**: https://discourse.slicer.org/t/segmentations-module-opacity-issue/48044

---

## Post #1 by @Malaquias_Cerrillo (2026-09-02 17:57 UTC)

<p>Hi everybody, i’m experiencing some trouble in the latest version 5.12.3 trying to shift the opacity of the different segmentations. However, I can shift the overall opacity of de segmentation node, does this happens to anybody else? does anyone know how to fix this?</p>

---

## Post #2 by @mikebind (2026-09-02 18:26 UTC)

<p>Try turning off ambient shadows and see if that helps:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5c3ac44344202008dd7d7b065d4faa0f96577a22.jpeg" data-download-href="/uploads/short-url/d9TPIRqUXKQTuSTKajkqGyKPBRM.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c3ac44344202008dd7d7b065d4faa0f96577a22_2_690x434.jpeg" alt="image" data-base62-sha1="d9TPIRqUXKQTuSTKajkqGyKPBRM" width="690" height="434" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c3ac44344202008dd7d7b065d4faa0f96577a22_2_690x434.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c3ac44344202008dd7d7b065d4faa0f96577a22_2_1035x651.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c3ac44344202008dd7d7b065d4faa0f96577a22_2_1380x868.jpeg 2x" data-dominant-color="EAE5DF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1210 305 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>My experience has been that ambient shadows does not play well with intermediate transparency values, so this is always my first troubleshooting check for visualizations.</p>

---
