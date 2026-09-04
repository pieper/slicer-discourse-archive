---
topic_id: 48044
title: "Segmentations Module - Opacity Issue"
date: 2026-09-02
url: https://discourse.slicer.org/t/48044
last_bumped: 2026-09-03T17:15:34.756Z
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

## Post #3 by @Esteban_Barreiro (2026-09-03 17:15 UTC)

<p>Hi Malaquias<br>
You can change opacities in this two ways:</p>
<ol>
<li>Going to Segmentations Module, descending to Display, with the slider in 3D, like this:</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0cffa5a4554eb59553fe6fbeb80b3e5d95e684e8.png" data-download-href="/uploads/short-url/1QZrXg4teQi968Vn8PD4HoFKgbu.png?dl=1" title="01" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0cffa5a4554eb59553fe6fbeb80b3e5d95e684e8_2_269x500.png" alt="01" data-base62-sha1="1QZrXg4teQi968Vn8PD4HoFKgbu" width="269" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0cffa5a4554eb59553fe6fbeb80b3e5d95e684e8_2_269x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/c/0cffa5a4554eb59553fe6fbeb80b3e5d95e684e8_2_403x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0cffa5a4554eb59553fe6fbeb80b3e5d95e684e8.png 2x" data-dominant-color="3B4242"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">01</span><span class="informations">525×973 54.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="2">
<li>By pressing right click on the eye icon of the segment you need, in the Data Module. It will display a pop up with a slider for opacity:</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62533c7cfed5fafeca3c68fca68f895476ea6d9c.png" data-download-href="/uploads/short-url/e1P7KyTgwouhgi7FxRvrS0RqWSw.png?dl=1" title="02" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62533c7cfed5fafeca3c68fca68f895476ea6d9c_2_690x456.png" alt="02" data-base62-sha1="e1P7KyTgwouhgi7FxRvrS0RqWSw" width="690" height="456" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62533c7cfed5fafeca3c68fca68f895476ea6d9c_2_690x456.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62533c7cfed5fafeca3c68fca68f895476ea6d9c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62533c7cfed5fafeca3c68fca68f895476ea6d9c.png 2x" data-dominant-color="434A4F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">02</span><span class="informations">719×476 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
