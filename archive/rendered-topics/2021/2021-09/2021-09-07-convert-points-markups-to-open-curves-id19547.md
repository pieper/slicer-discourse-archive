---
topic_id: 19547
title: "Convert Points Markups To Open Curves"
date: 2021-09-07
url: https://discourse.slicer.org/t/19547
---

# Convert points markups to open curves

**Topic ID**: 19547
**Date**: 2021-09-07
**URL**: https://discourse.slicer.org/t/convert-points-markups-to-open-curves/19547

---

## Post #1 by @Ale (2021-09-07 13:53 UTC)

<p>Hi all, I’m using Slicer and Slicermorph to place landmarks and semilandmarks (open curves) into mammalian skulls. I’m testing ALPACA to transfer point configuration to others skulls. I have two open curves describing zygomatic arch curvature, but when I use ALPACA to transfer those curves, they are converted to point markups or landmarks in target skulls. Is there a way to restore or convert those transferred points to open curves again?<br>
Thanks in advance!</p>
<p>Ale</p>

---

## Post #2 by @muratmaga (2021-09-07 15:23 UTC)

<p>You can copy and paste the control points into a blank curves markup node to reconstitute the curve.</p>
<p>The question is why do you need to redo the curve? It is only the markup control points used in the morphometric analysis.</p>

---

## Post #3 by @Ale (2021-09-07 17:39 UTC)

<p>Hi Murat, ALPACA shows very good correlation in general but in the zygomatic archs, the resulting points need some “by hand” correction.<br>
This is the reference curve:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac62e3682fa8903e58013c8e80b29f4363df1dce.jpeg" data-download-href="/uploads/short-url/oAZZvN044n5qEDNV9Oqa3h58dJ4.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ac62e3682fa8903e58013c8e80b29f4363df1dce_2_345x186.jpeg" alt="image" data-base62-sha1="oAZZvN044n5qEDNV9Oqa3h58dJ4" width="345" height="186" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ac62e3682fa8903e58013c8e80b29f4363df1dce_2_345x186.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ac62e3682fa8903e58013c8e80b29f4363df1dce_2_517x279.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ac62e3682fa8903e58013c8e80b29f4363df1dce_2_690x372.jpeg 2x" data-dominant-color="A9A96E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1025×554 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>And the transferred curve points to other skull:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7fd3245e69c91a080967b48da0611314151f11e0.jpeg" data-download-href="/uploads/short-url/ieN0wOrNAgUzv0dzsIvav7uVWco.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7fd3245e69c91a080967b48da0611314151f11e0_2_345x235.jpeg" alt="image" data-base62-sha1="ieN0wOrNAgUzv0dzsIvav7uVWco" width="345" height="235" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7fd3245e69c91a080967b48da0611314151f11e0_2_345x235.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7fd3245e69c91a080967b48da0611314151f11e0_2_517x352.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7fd3245e69c91a080967b48da0611314151f11e0_2_690x470.jpeg 2x" data-dominant-color="9284B0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">695×474 59.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>As can be seen, some points need some degree of correction. If they represents an open curve, I can use the resample function to correct in part the inter point distance.</p>
<p>Kind regards,</p>
<p>Ale</p>

---

## Post #4 by @muratmaga (2021-09-07 18:24 UTC)

<p>I am really not sure if ALPACA is of much use in here. You have a very specific region, and you can outline it very easily with the open curve, and  resample them as you said. If you will have to retouch output of ALPACA and resample again, I am not seeing the benefit of using ALPACA, since you can simply do the same by directly digitizing the curve on the zygomatic arch, possibly quicker.<br>
And you won’t need the additional step of converting those points to curves again (see my previous post on how to do that).</p>

---
