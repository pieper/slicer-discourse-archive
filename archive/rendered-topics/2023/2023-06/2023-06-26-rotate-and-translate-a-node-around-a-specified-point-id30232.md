---
topic_id: 30232
title: "Rotate And Translate A Node Around A Specified Point"
date: 2023-06-26
url: https://discourse.slicer.org/t/30232
---

# Rotate and translate a node around a specified point

**Topic ID**: 30232
**Date**: 2023-06-26
**URL**: https://discourse.slicer.org/t/rotate-and-translate-a-node-around-a-specified-point/30232

---

## Post #1 by @IsabelW96 (2023-06-26 09:01 UTC)

<p>Hi everyone,</p>
<p>I’ve tried to transform a node around a specified point script to work. The models are illustrated below. The red one is the reference model with the defined centroid (F-1).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa456354d3f8ea63547c08e857faa24957ef3bf3.png" data-download-href="/uploads/short-url/zI01UbkMzuV5eYQgE3JpD2LBQGL.png?dl=1" title="Schermafbeelding 2023-06-26 105816" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa456354d3f8ea63547c08e857faa24957ef3bf3_2_365x500.png" alt="Schermafbeelding 2023-06-26 105816" data-base62-sha1="zI01UbkMzuV5eYQgE3JpD2LBQGL" width="365" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa456354d3f8ea63547c08e857faa24957ef3bf3_2_365x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa456354d3f8ea63547c08e857faa24957ef3bf3.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa456354d3f8ea63547c08e857faa24957ef3bf3.png 2x" data-dominant-color="A0A2D3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Schermafbeelding 2023-06-26 105816</span><span class="informations">540×739 23.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I followed the video as described here:</p>
<aside class="quote" data-post="11" data-topic="9398">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/rotation-around-specific-point/9398/11">Rotation around specific point</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I’ve just tried the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#rotate-a-node-around-a-specified-point" rel="noopener nofollow ugc">script</a> that I posted earlier and it worked well. I’ve recorded it on a <a href="https://1drv.ms/v/s!Arm_AFxB9yqHucN9pd6edw1a1cgxbg?e=x5SJOd" rel="noopener nofollow ugc">video</a> so that you can see all the steps.
  </blockquote>
</aside>

<p>The results are illustrated below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48db7c2e3539734ebefe158992c5bbf7a22ba8aa.png" data-download-href="/uploads/short-url/aowCAQeGR9pQHtAeXzJy2AQnf7Q.png?dl=1" title="Schermafbeelding 2023-06-26 103833" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48db7c2e3539734ebefe158992c5bbf7a22ba8aa_2_467x500.png" alt="Schermafbeelding 2023-06-26 103833" data-base62-sha1="aowCAQeGR9pQHtAeXzJy2AQnf7Q" width="467" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/48db7c2e3539734ebefe158992c5bbf7a22ba8aa_2_467x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48db7c2e3539734ebefe158992c5bbf7a22ba8aa.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48db7c2e3539734ebefe158992c5bbf7a22ba8aa.png 2x" data-dominant-color="9B9CCE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Schermafbeelding 2023-06-26 103833</span><span class="informations">598×640 29 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d2414fe59c2bd74b29a1ed882611244678c830f4.png" data-download-href="/uploads/short-url/u00cmaVKlCkxkqfwq6fKNDUcCws.png?dl=1" title="Schermafbeelding 2023-06-26 104626" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d2414fe59c2bd74b29a1ed882611244678c830f4_2_562x500.png" alt="Schermafbeelding 2023-06-26 104626" data-base62-sha1="u00cmaVKlCkxkqfwq6fKNDUcCws" width="562" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d2414fe59c2bd74b29a1ed882611244678c830f4_2_562x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d2414fe59c2bd74b29a1ed882611244678c830f4.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d2414fe59c2bd74b29a1ed882611244678c830f4.png 2x" data-dominant-color="9999CD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Schermafbeelding 2023-06-26 104626</span><span class="informations">572×508 20.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So my question is, does this script only perform the rotation? Because I also need the translation that is needed to align these models.</p>
<p>I already performed ALPACA on these models to align them and get the transformation matrix that I copied to ‘rotationTransformNode’, but I want to know the total transform (rotation + translation) around a specific point (centroid) that I defined as F-1. I thought the script mentioned earlier would be the solution, but it only performs rotation, I guess…</p>
<p>Does anyone know how to include also the translations?</p>
<p>I’m working with slicer 5.2.2.</p>
<p>Any help would be appreciated!</p>

---
