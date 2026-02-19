---
topic_id: 23007
title: "Grow From Seeds Creates Unwanted Regions"
date: 2022-04-19
url: https://discourse.slicer.org/t/23007
---

# Grow from seeds creates unwanted regions

**Topic ID**: 23007
**Date**: 2022-04-19
**URL**: https://discourse.slicer.org/t/grow-from-seeds-creates-unwanted-regions/23007

---

## Post #1 by @bhowmisp (2022-04-19 01:30 UTC)

<p>Hi,</p>
<p>I have been using the “grow from seeds” effect to segment the ganglion from the following pictures. I paint in two segments, 1- for the ganglion(yellow)- in all three views across multiple slices and 2. for the background(green).</p>
<p>But ultimately the algorithm is unable to segment the ganglia. I have tried it for different levels of ganglion together and now even separately for each particular level. It generates a mass with a lot of noise from the surrounding regions from which the ganglion is nearly impossible to separate. I realize that there is a edit option after the initial segmentation result, but the generated 3D mass is not suitable for manual edits.</p>
<p>Is there a way out of this? Or this is a product of the image quality/type?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b56e7abc560317053f56a9289ffd9df3319ecb47.jpeg" data-download-href="/uploads/short-url/pT17DMmMRsBYjlcGWoibmdvTSsf.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b56e7abc560317053f56a9289ffd9df3319ecb47_2_690x313.jpeg" alt="image" data-base62-sha1="pT17DMmMRsBYjlcGWoibmdvTSsf" width="690" height="313" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b56e7abc560317053f56a9289ffd9df3319ecb47_2_690x313.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b56e7abc560317053f56a9289ffd9df3319ecb47_2_1035x469.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b56e7abc560317053f56a9289ffd9df3319ecb47.jpeg 2x" data-dominant-color="BCAEA2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1362×618 88.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @gaoyi.cn (2022-04-19 01:44 UTC)

<p>Hi,</p>
<p>Usually when you paint the seeds for “Grow from seeds”, you draw the target-seed (1 in your case) in the rough center of the target in all the 3 views. Surrounding them, in all 3 views, you also want to draw a circular using background-seed (2 in your case) in the background region around the target region, to form a “wall”.</p>
<p>Could you give a screenshot of the seeds you draw in 3-views and we can start from there.</p>
<p>HTH</p>
<p>Best,</p>
<p>yi</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a85400eb899b7201ef16816337be48a02539676.png" data-download-href="/uploads/short-url/8lHbc8ewzqTHYpSOyVLQwZxlrCe.png?dl=1" title="841F8A606C9E466C9FD5610F03B4BC6F.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a85400eb899b7201ef16816337be48a02539676_2_690x1.png" alt="841F8A606C9E466C9FD5610F03B4BC6F.png" data-base62-sha1="8lHbc8ewzqTHYpSOyVLQwZxlrCe" width="690" height="1" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a85400eb899b7201ef16816337be48a02539676_2_690x1.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a85400eb899b7201ef16816337be48a02539676.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a85400eb899b7201ef16816337be48a02539676.png 2x" data-dominant-color="BECCDA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">841F8A606C9E466C9FD5610F03B4BC6F.png</span><span class="informations">708×2 103 Bytes</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @bhowmisp (2022-04-19 02:22 UTC)

<p>Hi,</p>
<p>Attached is the screenshot of the seeds in 3 views. I should mention that the Segment 2 is my region of interest, which I want to grow and segment 1 is the surrounding. Does the numbering matter? I am also curious to know if the seed painting needs to be exact, because if you see my seeds they are roughly centered but doesn’t cover the entire area.</p>
<p>This picture is from one slice, I have selected similar seeds in multiple other slices. I am also skipping some slices.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb48e5c12ba96685a2688102d1601d50e1aaf994.jpeg" data-download-href="/uploads/short-url/zQY1GB4X4QNJPmcicaJ6uUj4bAw.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fb48e5c12ba96685a2688102d1601d50e1aaf994_2_690x310.jpeg" alt="image" data-base62-sha1="zQY1GB4X4QNJPmcicaJ6uUj4bAw" width="690" height="310" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fb48e5c12ba96685a2688102d1601d50e1aaf994_2_690x310.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fb48e5c12ba96685a2688102d1601d50e1aaf994_2_1035x465.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb48e5c12ba96685a2688102d1601d50e1aaf994.jpeg 2x" data-dominant-color="D3B9B0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1358×612 81.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @gaoyi.cn (2022-04-19 02:36 UTC)

<p>Hi,</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bdd89dc796d93e5352fd67fdce5865aa0d89d5e2.jpeg" data-download-href="/uploads/short-url/r5sl5Wb145gqAhZIvq9tjNy5sKS.jpeg?dl=1" title="19BC39F962274E4FA89162A5ED4EE4BE.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bdd89dc796d93e5352fd67fdce5865aa0d89d5e2_2_682x500.jpeg" alt="19BC39F962274E4FA89162A5ED4EE4BE.jpg" data-base62-sha1="r5sl5Wb145gqAhZIvq9tjNy5sKS" width="682" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bdd89dc796d93e5352fd67fdce5865aa0d89d5e2_2_682x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bdd89dc796d93e5352fd67fdce5865aa0d89d5e2_2_1023x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bdd89dc796d93e5352fd67fdce5865aa0d89d5e2_2_1364x1000.jpeg 2x" data-dominant-color="C19789"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">19BC39F962274E4FA89162A5ED4EE4BE.jpg</span><span class="informations">2073×1518 493 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a85400eb899b7201ef16816337be48a02539676.png" data-download-href="/uploads/short-url/8lHbc8ewzqTHYpSOyVLQwZxlrCe.png?dl=1" title="841F8A606C9E466C9FD5610F03B4BC6F.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a85400eb899b7201ef16816337be48a02539676_2_690x1.png" alt="841F8A606C9E466C9FD5610F03B4BC6F.png" data-base62-sha1="8lHbc8ewzqTHYpSOyVLQwZxlrCe" width="690" height="1" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a85400eb899b7201ef16816337be48a02539676_2_690x1.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a85400eb899b7201ef16816337be48a02539676.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a85400eb899b7201ef16816337be48a02539676.png 2x" data-dominant-color="BECCDA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">841F8A606C9E466C9FD5610F03B4BC6F.png</span><span class="informations">708×2 103 Bytes</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @bhowmisp (2022-04-19 04:32 UTC)

<p>Thanks! that was a very helpful tip! It seems like I need to this detailed segmentation for every level at every slice separately to have some kind of meaningful structures.</p>
<p>But an issue remains, the final 3D model is very porous and looks discontinuous. I tried smoothing operations but it is not altering much. What can be done about these surface undulations?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/96868e904e23156bb59854c66b47f1b94ad2fdab.png" alt="image" data-base62-sha1="ltBUfWtYfHi2Gghkt9Pid6Yhnvl" width="387" height="275"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/5874660d75da48d498ee812a242752a1403cf4a2.jpeg" alt="image" data-base62-sha1="cCvoOUEqb4is8BMaSnui47bCVxw" width="406" height="295"></p>

---

## Post #6 by @cpinter (2022-04-19 09:03 UTC)

<p>Grow from seeds is an iterative method, in which after the first run you can refine the seeds that you change in the regions where it erred to improve the segmentation. Just saying that you don’t need to paint the “perfect” seeds to begin with, you can adjust later.</p>
<p>For filling the porous segmentation you can for example use the SurfaceWrapSolidify extension that adds the effect “Wrap solidify” to Segment Editor. You can also as I said above refine the seeds at the borders where the speckles are and in the interior where the holes are, or use the Islands effect to remove the smallest islands.</p>

---

## Post #7 by @gaoyi.cn (2022-04-19 12:50 UTC)

<p>Hi,</p>
<p>Great to know that helped.</p>
<p>But maybe doing a detailed segmentation for every level (slice) is not necessary. For a “nodular” shaped target object, I often locate the intersection of the three views (red, green, yellow) at roughly the center of the target. Then, when I’m drawing the seed, I just draw in the center in each view with just one click, and then use another color (label) to draw in each slice an enclosing circle inside the background region. Then I run the “Grow from seed” and it should give a descent 3D segmentation.</p>
<p>For more complicated shaped target, we definitely need more seeds. But not for the nodular shaped ones.</p>
<p>Regarding the smoothness of the surface, yes the “grow from seed” is a first order PDE based algorithm and does not take the surface smoothness into consideration. As Csaba pointed out, we can use other modules to smooth the surface as a post-processing. Maybe I should add some smoothing within the Grow from seed, that maybe helpful.</p>
<p>Best,</p>
<p>yi</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a85400eb899b7201ef16816337be48a02539676.png" data-download-href="/uploads/short-url/8lHbc8ewzqTHYpSOyVLQwZxlrCe.png?dl=1" title="841F8A606C9E466C9FD5610F03B4BC6F.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a85400eb899b7201ef16816337be48a02539676_2_690x1.png" alt="841F8A606C9E466C9FD5610F03B4BC6F.png" data-base62-sha1="8lHbc8ewzqTHYpSOyVLQwZxlrCe" width="690" height="1" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3a85400eb899b7201ef16816337be48a02539676_2_690x1.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a85400eb899b7201ef16816337be48a02539676.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a85400eb899b7201ef16816337be48a02539676.png 2x" data-dominant-color="BECCDA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">841F8A606C9E466C9FD5610F03B4BC6F.png</span><span class="informations">708×2 103 Bytes</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @bhowmisp (2022-04-19 19:26 UTC)

<p>Thank you <a class="mention" href="/u/gaoyi.cn">@gaoyi.cn</a> and <a class="mention" href="/u/cpinter">@cpinter</a> for the suggestions!</p>
<p>I added the Wrap Solidify extension, although it takes sometime but it produces a desired result.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f267bc1bf45b00a9855d44a506d180ca2529f32c.png" alt="image" data-base62-sha1="yApNvXjFW5OrRG7lvrQJWeWNSck" width="406" height="308"></p>
<p>However, I have another basic question about the segmenting. How to select which segments I want to activate? As you know there are 31pairs of DRG, what if I want to segment them in the same file.  I have used segment 1(boundary) and 2(DRG) in the picture above. What if I want to use Segment 3 and 4 for the next level of DRG? I am unable to hide/inactivate Segments 1,2(not delete) and use only 3 and 4. Is this even possible?</p>
<p>Or in a better way, Can I specify all the DRGs at all levels and their boundaries in segments1,2 itself? Or I paint all the DRGs in separate segments but paint a common boundary, will that work? Since the DRGs/Boundaries are discontinuous?</p>
<p>I want to understand what is the best option of the three, based on your experience. It is difficult to try all of these, as this is taking multiple hours to compute at times.</p>
<p>I am referencing this video, which is very helpful, but the issue is everything I want to segment is not continuous and I don’t want to use too much memory which might cause the software to crash.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="BJoIexIvtGo" data-video-title="Whole heart segmentation from cardiac CT in 10 minutes" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=BJoIexIvtGo" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/BJoIexIvtGo/maxresdefault.jpg" title="Whole heart segmentation from cardiac CT in 10 minutes" width="" height="">
  </a>
</div>


---

## Post #9 by @cpinter (2022-04-19 20:11 UTC)

<p>I’d probably try creating new segmentation nodes for the “grow from seeds” seeds, and then before saving, drag&amp;dropping the useful segments using the Data module in the first segmentation (or a new one) and then save.</p>

---
