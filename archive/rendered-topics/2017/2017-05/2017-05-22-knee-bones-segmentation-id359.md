---
topic_id: 359
title: "Knee Bones Segmentation"
date: 2017-05-22
url: https://discourse.slicer.org/t/359
---

# Knee bones segmentation

**Topic ID**: 359
**Date**: 2017-05-22
**URL**: https://discourse.slicer.org/t/knee-bones-segmentation/359

---

## Post #1 by @Hanaana (2017-05-22 10:53 UTC)

<p>Hello everyone!!</p>
<p>Needing your support. I am trying to segment a femur bone from a knee MRI data but when i finish the  segmentation editing and clique apply. the program freezes and then it shut down.</p>
<p>Am i doing it wrong? Can someone support me pllllease</p>

---

## Post #2 by @lassoan (2017-05-22 18:46 UTC)

<p>Do you use latest nightly Slicer version? Do you use the old Editor module or the new Segment Editor module?</p>

---

## Post #3 by @Hanaana (2017-06-05 04:47 UTC)

<p>I use operation system: windows 7 professional 64 bits<br>
Slicer version :4.6.2<br>
MRI data of the knee and trying to segment the knee bones: femur and tibia<br>
and fibula. These are the results i could get using Editor paint effect and<br>
model maker. do you think I can get better results using different<br>
segmentation method???</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52374ec316c21d53817dad70e73d6dfd719273bf.png" data-download-href="/uploads/short-url/bJjEdBDRLxmsNrMFA3NQI7FT2A7.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/52374ec316c21d53817dad70e73d6dfd719273bf_2_509x499.png" alt="image" data-base62-sha1="bJjEdBDRLxmsNrMFA3NQI7FT2A7" width="509" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/52374ec316c21d53817dad70e73d6dfd719273bf_2_509x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52374ec316c21d53817dad70e73d6dfd719273bf.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52374ec316c21d53817dad70e73d6dfd719273bf.png 2x" data-dominant-color="636260"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">631×619 216 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cba8bf70181a3ea4e01e94f455e7f2f50c911840.png" data-download-href="/uploads/short-url/t3EsXaaMySC0JGIvYrb80KolR5u.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cba8bf70181a3ea4e01e94f455e7f2f50c911840_2_534x500.png" alt="image" data-base62-sha1="t3EsXaaMySC0JGIvYrb80KolR5u" width="534" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/b/cba8bf70181a3ea4e01e94f455e7f2f50c911840_2_534x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cba8bf70181a3ea4e01e94f455e7f2f50c911840.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cba8bf70181a3ea4e01e94f455e7f2f50c911840.png 2x" data-dominant-color="636261"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">698×653 236 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @muratmaga (2017-06-05 05:15 UTC)

<p>Hi Hanaa,</p>
<p>Please use a more recent nightly version of the Slicer and try the segment editor to do your segmentation. From the snapshots (are those from Slicer?) you sent, it looks like you still need to play a bit more with your intensity ranges to cut out the noise. You can also use the scissors tools to remove dangling parts and then run a smoothing filter to get a nicer looking surface.</p>
<p>All of these are available within the new Segment editor module.<br>
HTH,<br>
M</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/677f06bdf711468707faf594c72c7993f90d2513.png" data-download-href="/uploads/short-url/eLzkAGZovUCazoJL65K1uagmWFJ.png?dl=1" title="77C3A3DB5AF54B56A741600A3E5A8000.png"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/677f06bdf711468707faf594c72c7993f90d2513.png" width="690" height="0" data-dominant-color="BFCDDB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">77C3A3DB5AF54B56A741600A3E5A8000.png</span><span class="informations">708×1 83 Bytes</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
