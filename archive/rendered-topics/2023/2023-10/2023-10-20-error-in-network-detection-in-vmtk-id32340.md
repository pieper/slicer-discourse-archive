---
topic_id: 32340
title: "Error In Network Detection In Vmtk"
date: 2023-10-20
url: https://discourse.slicer.org/t/32340
---

# Error in network detection in vmtk

**Topic ID**: 32340
**Date**: 2023-10-20
**URL**: https://discourse.slicer.org/t/error-in-network-detection-in-vmtk/32340

---

## Post #1 by @b_gop (2023-10-20 11:13 UTC)

<p>Hi all,</p>
<p>I am trying to do the centerline computation and network extraction for a volume.</p>
<p>The network extraction is fine for most of the volume, but at one point it seems to break down and gives a false detection. [On the bottom, the very dense center of branches]</p>
<p>Would anyone know why this is happening?</p>
<p>P.S: I also tried the network extraction on other volumes, and it always seems to have one such over dense center.</p>
<p>Image 1: only network, with the visible error<br>
Image 2: segmentation + network<br>
Image 3: segmentation + centerline<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b01debd748bbd650b0677787b123de14cdeaf61.png" data-download-href="/uploads/short-url/jPInfz0yODbWcJSwXxoWO9mbgA1.png?dl=1" title="error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b01debd748bbd650b0677787b123de14cdeaf61_2_548x500.png" alt="error" data-base62-sha1="jPInfz0yODbWcJSwXxoWO9mbgA1" width="548" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b01debd748bbd650b0677787b123de14cdeaf61_2_548x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b01debd748bbd650b0677787b123de14cdeaf61_2_822x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b01debd748bbd650b0677787b123de14cdeaf61.png 2x" data-dominant-color="9798CC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error</span><span class="informations">1034×942 150 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1ca6ee38b09ab2e776b51a8ff96497e9cc6e2369.jpeg" data-download-href="/uploads/short-url/45t10ovV6zMoYhs5U4jNsofQaLf.jpeg?dl=1" title="Screenshot_long_vol (1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1ca6ee38b09ab2e776b51a8ff96497e9cc6e2369_2_548x500.jpeg" alt="Screenshot_long_vol (1)" data-base62-sha1="45t10ovV6zMoYhs5U4jNsofQaLf" width="548" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1ca6ee38b09ab2e776b51a8ff96497e9cc6e2369_2_548x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1ca6ee38b09ab2e776b51a8ff96497e9cc6e2369_2_822x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1ca6ee38b09ab2e776b51a8ff96497e9cc6e2369.jpeg 2x" data-dominant-color="8E94BC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_long_vol (1)</span><span class="informations">1034×942 166 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
**![|294px;x505px;]<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8bc2aad53f8ce85275eae73d5924d44daeeb764a.png" data-download-href="/uploads/short-url/jWnrlWXktqevIQW26jEOiGbYyjo.png?dl=1" title="Screenshot 2023-10-20 at 1.12.41 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8bc2aad53f8ce85275eae73d5924d44daeeb764a_2_287x500.png" alt="Screenshot 2023-10-20 at 1.12.41 PM" data-base62-sha1="jWnrlWXktqevIQW26jEOiGbYyjo" width="287" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8bc2aad53f8ce85275eae73d5924d44daeeb764a_2_287x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8bc2aad53f8ce85275eae73d5924d44daeeb764a_2_430x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8bc2aad53f8ce85275eae73d5924d44daeeb764a.png 2x" data-dominant-color="818D9D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-10-20 at 1.12.41 PM</span><span class="informations">478×832 347 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
