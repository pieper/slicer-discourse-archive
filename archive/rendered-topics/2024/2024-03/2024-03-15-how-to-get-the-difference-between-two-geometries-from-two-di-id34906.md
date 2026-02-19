---
topic_id: 34906
title: "How To Get The Difference Between Two Geometries From Two Di"
date: 2024-03-15
url: https://discourse.slicer.org/t/34906
---

# how to get the difference between two geometries from two different scans

**Topic ID**: 34906
**Date**: 2024-03-15
**URL**: https://discourse.slicer.org/t/how-to-get-the-difference-between-two-geometries-from-two-different-scans/34906

---

## Post #1 by @Clement_Bouchard (2024-03-15 06:27 UTC)

<p>Hello,</p>
<p>I have two different tracheas, one completely open and the other closed with a collapse. I would like to get the difference between these volumes or try to move them. Ideally I’d like to be able to align my two scans in terms of position to see the difference. The final objective is to obtain the structure of the trachea as it closes, as at present I only have the fluid that has flowed inside. The fluid is a liquid, so I’m doing total liquid ventilation.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86bb096e353a210585ba2e0fa35ec5f8d94dd394.jpeg" data-download-href="/uploads/short-url/jdSHKolgsjMGqDHtI8f957OhwYk.jpeg?dl=1" title="thumbnail_image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86bb096e353a210585ba2e0fa35ec5f8d94dd394_2_690x447.jpeg" alt="thumbnail_image" data-base62-sha1="jdSHKolgsjMGqDHtI8f957OhwYk" width="690" height="447" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86bb096e353a210585ba2e0fa35ec5f8d94dd394_2_690x447.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86bb096e353a210585ba2e0fa35ec5f8d94dd394_2_1035x670.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86bb096e353a210585ba2e0fa35ec5f8d94dd394_2_1380x894.jpeg 2x" data-dominant-color="1F1F1E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">thumbnail_image</span><span class="informations">1432×928 55.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c4cbc56e54203fb794011449e0b9a16702e07d4b.png" data-download-href="/uploads/short-url/s4Wa2OoZK4Yoo7zbQkh5zOdb2QP.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c4cbc56e54203fb794011449e0b9a16702e07d4b_2_344x500.png" alt="image" data-base62-sha1="s4Wa2OoZK4Yoo7zbQkh5zOdb2QP" width="344" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c4cbc56e54203fb794011449e0b9a16702e07d4b_2_344x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c4cbc56e54203fb794011449e0b9a16702e07d4b_2_516x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c4cbc56e54203fb794011449e0b9a16702e07d4b.png 2x" data-dominant-color="9C9DCE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">591×857 52.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-03-17 01:57 UTC)

<p>You can align images using the <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html">registration techniques described in the Slicer documentation</a>.</p>

---
