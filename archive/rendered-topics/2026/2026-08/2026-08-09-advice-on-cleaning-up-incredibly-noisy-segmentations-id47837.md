---
topic_id: 47837
title: "Advice on cleaning up incredibly noisy segmentations"
date: 2026-08-09
url: https://discourse.slicer.org/t/47837
last_bumped: 2026-08-16T18:37:54.345Z
---

# Advice on cleaning up incredibly noisy segmentations

**Topic ID**: 47837
**Date**: 2026-08-09
**URL**: https://discourse.slicer.org/t/advice-on-cleaning-up-incredibly-noisy-segmentations/47837

---

## Post #1 by @Chelonian (2026-08-09 08:36 UTC)

<p>I’m trying to segment the internals of some incredibly noisy CT scans.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/273178911c8ba53abea1b1d44fe5f254995de496.jpeg" data-download-href="/uploads/short-url/5AIBY3XofmXpX6x2oJNkUffEh26.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/273178911c8ba53abea1b1d44fe5f254995de496_2_342x250.jpeg" alt="image" data-base62-sha1="5AIBY3XofmXpX6x2oJNkUffEh26" width="342" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/273178911c8ba53abea1b1d44fe5f254995de496_2_342x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/273178911c8ba53abea1b1d44fe5f254995de496_2_513x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/273178911c8ba53abea1b1d44fe5f254995de496_2_684x500.jpeg 2x" data-dominant-color="414141"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1272×928 159 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>example of what I’m working with</p>
<p>I’ve managed to segment the intestines but I’m not happy at all with the quality of the segments or the amount of manual labor it would take to clean them</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d60dab5cbe78c9420447e2864f608411f24c4381.jpeg" data-download-href="/uploads/short-url/uxBsQdfhOU3vNvRuPXZzmJbYK2t.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d60dab5cbe78c9420447e2864f608411f24c4381_2_345x237.jpeg" alt="image" data-base62-sha1="uxBsQdfhOU3vNvRuPXZzmJbYK2t" width="345" height="237" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d60dab5cbe78c9420447e2864f608411f24c4381_2_345x237.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d60dab5cbe78c9420447e2864f608411f24c4381_2_517x355.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d60dab5cbe78c9420447e2864f608411f24c4381_2_690x474.jpeg 2x" data-dominant-color="44434A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1313×905 211 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/407f2ee996b29fb5368a0d6a60c8a102273a4c6b.jpeg" data-download-href="/uploads/short-url/9cz2Uy1kqmRUYS6XrgyV4xfrBTd.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/407f2ee996b29fb5368a0d6a60c8a102273a4c6b_2_310x250.jpeg" alt="image" data-base62-sha1="9cz2Uy1kqmRUYS6XrgyV4xfrBTd" width="310" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/407f2ee996b29fb5368a0d6a60c8a102273a4c6b_2_310x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/407f2ee996b29fb5368a0d6a60c8a102273a4c6b_2_465x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/407f2ee996b29fb5368a0d6a60c8a102273a4c6b_2_620x500.jpeg 2x" data-dominant-color="3E3D42"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1160×934 161 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I’m fine with the larger segment, the one outlined in red is what I’d like to really fix. I’ve tried all of the filters and smoothing extensions that I can find and I believe none of them are able to work on such an extreme case as this (at least as much as I’ve been able to use them).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/470f0d64430ed786e3181f73cfe2d4cfd4fa908a.jpeg" data-download-href="/uploads/short-url/a8C9hWCxqNZqETWg1aeArGvMv4C.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/470f0d64430ed786e3181f73cfe2d4cfd4fa908a_2_345x227.jpeg" alt="image" data-base62-sha1="a8C9hWCxqNZqETWg1aeArGvMv4C" width="345" height="227" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/470f0d64430ed786e3181f73cfe2d4cfd4fa908a_2_345x227.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/470f0d64430ed786e3181f73cfe2d4cfd4fa908a_2_517x340.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/470f0d64430ed786e3181f73cfe2d4cfd4fa908a_2_690x454.jpeg 2x" data-dominant-color="7C7DC1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1359×898 223 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/32faff9b8b363b010988d937e108816ec5b8f721.jpeg" data-download-href="/uploads/short-url/7gZDnVONa5VcLOb0tHwsAw4SYQ9.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32faff9b8b363b010988d937e108816ec5b8f721_2_345x190.jpeg" alt="image" data-base62-sha1="7gZDnVONa5VcLOb0tHwsAw4SYQ9" width="345" height="190" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32faff9b8b363b010988d937e108816ec5b8f721_2_345x190.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32faff9b8b363b010988d937e108816ec5b8f721_2_517x285.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32faff9b8b363b010988d937e108816ec5b8f721_2_690x380.jpeg 2x" data-dominant-color="6869CA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1294×715 282 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I know this is a pretty hopeless case but I’m wondering if there’s anything I haven’t tried that will be able to just follow the general shape of the intestines and fill in all of the holes? I don’t need much accuracy at all, just a similar form. Any advice is welcome!</p>

---

## Post #2 by @chir.set (2026-08-09 09:11 UTC)

<p>Try some denoising filters on the input volume before performing segmentation.</p>

---

## Post #3 by @pieper (2026-08-09 11:59 UTC)

<p>Agreed,  This looks like exactly the scenario for classical image processing like gaussians and median filters before segmentation.</p>

---

## Post #4 by @Deep_Learning (2026-08-10 14:22 UTC)

<p>Preprocessing is a good suggestion.  But I have three others.  1) nninteractive is great in these and other situations 2) Post processing the segmentation:  Look in the Segmentation Module.  Try Fill Holes and Smoothing.  Experiment with different kernal sizes.   3) Take a look at the wrap solidify extension.   I’m not sure exactly what you are after, but this is probably your solution.  It shrink wraps the segmentation.  Also need to experiment with the many parameters.</p>

---

## Post #5 by @JaredAmudeo (2026-08-10 21:23 UTC)

<p>Hi! I’ve seen very similar cases in the datasets I work with, mainly fossils. In my opinion, if you can request a new reconstruction of the CT scan, it would be great to reduce the beam-hardening effect, which is making the bones appear excessively bright.</p>
<p>The other type of noise, which is more opaque and looks like many randomly distributed pixels, seems to me to be related to an incorrect combination of tube current (mA or µA) and filter. Unfortunately, there is not much that can be changed without performing the scan again, but applying some smoothing in the CT reconstruction software might help</p>

---

## Post #6 by @Chelonian (2026-08-16 18:36 UTC)

<p>The wrap solidify extension definitely worked the best, and I could smooth it out from there.</p>

---

## Post #7 by @Chelonian (2026-08-16 18:37 UTC)

<p>I have requested a new reconstruction, I don’t think I’ll be able to get much further than where I am with this scan.</p>

---
