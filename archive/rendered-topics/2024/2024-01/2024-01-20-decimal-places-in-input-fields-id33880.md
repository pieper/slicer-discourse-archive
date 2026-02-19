---
topic_id: 33880
title: "Decimal Places In Input Fields"
date: 2024-01-20
url: https://discourse.slicer.org/t/33880
---

# Decimal places in input fields

**Topic ID**: 33880
**Date**: 2024-01-20
**URL**: https://discourse.slicer.org/t/decimal-places-in-input-fields/33880

---

## Post #1 by @Hamburgerfinger (2024-01-20 04:27 UTC)

<p>Can I increase the precision of input fields in Slicer?  For example, say I want to rescale an image using the ShiftScaleImageFilter (Simple Filters module), and my scale factor needs to be small - say it is 0.0002311…  I run out of digits because only 5 are allowed after the decimal point:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7fc30ef70a558cc1d525c22cd64191d8c146900.png" data-download-href="/uploads/short-url/uOGYkZ55EfKChfgfPpZckYyukJq.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7fc30ef70a558cc1d525c22cd64191d8c146900_2_690x405.png" alt="image" data-base62-sha1="uOGYkZ55EfKChfgfPpZckYyukJq" width="690" height="405" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d7fc30ef70a558cc1d525c22cd64191d8c146900_2_690x405.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7fc30ef70a558cc1d525c22cd64191d8c146900.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7fc30ef70a558cc1d525c22cd64191d8c146900.png 2x" data-dominant-color="3D3D3D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">801×471 23.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is there an easy fix/setting for this that I am missing?</p>
<p>Thanks!</p>

---

## Post #2 by @muratmaga (2024-01-20 04:49 UTC)

<p>Temporarily you can increase the precision fields by hitting ctrl+ (or command + if you are in Mac).</p>
<p>If you want to make these changes permanent go to Application Settings-&gt;Units and change the precision of the length field.</p>

---

## Post #3 by @Hamburgerfinger (2024-01-20 13:25 UTC)

<p>Thanks!  That solution works for some modules (like the “transforms” or “volumes” module), but it does not work in the “simple filters” module for some reason…</p>

---

## Post #4 by @muratmaga (2024-01-20 17:23 UTC)

<p>Interesting, which filter are you using, and what platform are you on? For resample, it works fine for me on Mac.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/7669efb7124a73ca60edd7c9d4ef51a5921d09e7.png" data-download-href="/uploads/short-url/gTxjatft5cVfPIT6kJBBCqDPN6n.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/7669efb7124a73ca60edd7c9d4ef51a5921d09e7_2_690x475.png" alt="image" data-base62-sha1="gTxjatft5cVfPIT6kJBBCqDPN6n" width="690" height="475" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/7669efb7124a73ca60edd7c9d4ef51a5921d09e7_2_690x475.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/6/7669efb7124a73ca60edd7c9d4ef51a5921d09e7_2_1035x712.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/7669efb7124a73ca60edd7c9d4ef51a5921d09e7.png 2x" data-dominant-color="E7E7E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1132×780 55.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @muratmaga (2024-01-20 17:25 UTC)

<p>I see you are using shiftscale and indeed it doesn’t work. Can you file a quick issues report at the slicer github page <a href="https://github.com/Slicer/Slicer" class="inline-onebox">GitHub - Slicer/Slicer: Multi-platform, free open source software for visualization and image computing.</a>?</p>

---
