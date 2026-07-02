---
topic_id: 47522
title: "Smallest specimen possible to image with Slicer Photogrammetry?"
date: 2026-07-01
url: https://discourse.slicer.org/t/47522
last_bumped: 2026-07-01T15:59:26.483Z
---

# Smallest specimen possible to image with Slicer Photogrammetry?

**Topic ID**: 47522
**Date**: 2026-07-01
**URL**: https://discourse.slicer.org/t/smallest-specimen-possible-to-image-with-slicer-photogrammetry/47522

---

## Post #1 by @imfeldts001 (2026-07-01 15:31 UTC)

<p>Greetings!</p>
<p>My students and I have begun a project using Slicer Photogrammetry to create 3D models of songbird skulls from natural history collection in the area. The platform has worked well for us with the largest specimens we’ve received on loan, which are about 55-60mm in maximum length. However, we’ve run into issues with our smallest specimens, which are ~25mm in maximum length. We’ve tried factorial combinations of troubleshooting fixes like taking up to 64 pictures per set of photos, increasing to 6 unique photo sets (instead of 5), and using a macro lens to make the specimen larger in the actual images while still being totally in focus. At best, the ODM model made a fragmented model with “bone fragments” floating in space, like so:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85b5bd8541adc4a869b765fd4fae9b3a3ce255a5.jpeg" data-download-href="/uploads/short-url/j4QSAftFBOm5a17LWldHrx5kj2d.jpeg?dl=1" title="a fragmented model of a warbler skull" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85b5bd8541adc4a869b765fd4fae9b3a3ce255a5_2_690x330.jpeg" alt="a fragmented model of a warbler skull" data-base62-sha1="j4QSAftFBOm5a17LWldHrx5kj2d" width="690" height="330" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/85b5bd8541adc4a869b765fd4fae9b3a3ce255a5_2_690x330.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85b5bd8541adc4a869b765fd4fae9b3a3ce255a5.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/85b5bd8541adc4a869b765fd4fae9b3a3ce255a5.jpeg 2x" data-dominant-color="504C75"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">a fragmented model of a warbler skull</span><span class="informations">826×396 61.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>or a poorly resolved skull with non-overlapping regions opposed from each other:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/802ee165c3a38608624b186f7ee33e15eb07eb39.jpeg" data-download-href="/uploads/short-url/ihXyxDwLIdqrpQ73FuxgmsCA8IN.jpeg?dl=1" title="a poorly assembled model of a warbler skull" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/802ee165c3a38608624b186f7ee33e15eb07eb39_2_690x232.jpeg" alt="a poorly assembled model of a warbler skull" data-base62-sha1="ihXyxDwLIdqrpQ73FuxgmsCA8IN" width="690" height="232" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/802ee165c3a38608624b186f7ee33e15eb07eb39_2_690x232.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/802ee165c3a38608624b186f7ee33e15eb07eb39.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/802ee165c3a38608624b186f7ee33e15eb07eb39.jpeg 2x" data-dominant-color="5E597E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">a poorly assembled model of a warbler skull</span><span class="informations">868×292 70.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, basically all of our ODM runs with this specimen have failed to assemble and gave an error saying that we need more photos with more overlap.</p>
<p>My question for the community is: What is the smallest size of specimen/object you’ve successfully used Slicer Photogrammetry to digitize? We will keep plugging away on larger specimens as best we can, but any idea of whether we need more photos, more photo sets, or if there’s a limit of how small this tool can go for handling our smallest specimens would be graciously appreciated. Many many thanks!</p>
<p>Tyler Imfeld</p>

---

## Post #2 by @muratmaga (2026-07-01 15:59 UTC)

<p>Photogrammetry doesn’t know anything about the scale. For small specimens the photography is the real battle, and two things matter most: the lens and the framing.</p>
<p><strong>On the lens — skip the macro</strong>. Macros introduce geometric distortion (fisheye-type warping) that’s unacceptable for morphometrics. Use a good telephoto and zoom in on the specimen instead. You also want a lens you can stop down to a high f-number to keep the entire specimen within the depth of field; the tele lenses that do this well aren’t cheap (think the ones birders and wildlife shooters use).</p>
<p><strong>On the framing</strong> — the specimen needs to be entirely in focus and fill ~80% of the frame. A small skull in the center of a mostly-empty frame is the classic failure mode: the feature matcher can’t find enough to lock onto and can’t separate the specimen from the background. That’s exactly what your “need more photos with more overlap” error is — ODM saying consecutive views don’t share enough matched features. Shoot in small angular increments with heavy overlap between adjacent frames.</p>
<p><strong>One more thing working against you at this size:</strong> bird skulls are smooth and low-texture, so use diffuse, even lighting (kill any specular hotspots) against a plain background. With small, shiny bone, lighting is often what makes or breaks a run. In our 2023 paper, one extremely bleached mountain beaver skull was the one that consistently failed the reconstruction using the exact protocol for photography and photogrammetry.</p>
<p>Also photogrammetry within Slicer ecosystem is fairly niche. You might get better support and advise directly from the OpenDroneMap community forum. Browse those as well: <a href="https://community.opendronemap.org/" rel="noopener nofollow ugc">https://community.opendronemap.org/</a></p>

---
