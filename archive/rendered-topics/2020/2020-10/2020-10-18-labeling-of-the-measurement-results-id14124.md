---
topic_id: 14124
title: "Labeling Of The Measurement Results"
date: 2020-10-18
url: https://discourse.slicer.org/t/14124
---

# Labeling of the measurement results

**Topic ID**: 14124
**Date**: 2020-10-18
**URL**: https://discourse.slicer.org/t/labeling-of-the-measurement-results/14124

---

## Post #1 by @Andreas (2020-10-18 21:07 UTC)

<p>Hello everybody,</p>
<p>how can the labeling of the measurement results be better and clearly legible? The rows of numbers should not be shifted into one another and should also be displayed in a smaller format. (Image 1)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f2a0a74db96caf9b1bc7aae71da92e2e89bf5631.jpeg" data-download-href="/uploads/short-url/yCnKhlCCzwcjqjtfLKflaqz5Yit.jpeg?dl=1" title="Messungen (2)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f2a0a74db96caf9b1bc7aae71da92e2e89bf5631_2_690x388.jpeg" alt="Messungen (2)" data-base62-sha1="yCnKhlCCzwcjqjtfLKflaqz5Yit" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f2a0a74db96caf9b1bc7aae71da92e2e89bf5631_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f2a0a74db96caf9b1bc7aae71da92e2e89bf5631_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f2a0a74db96caf9b1bc7aae71da92e2e89bf5631_2_1380x776.jpeg 2x" data-dominant-color="9A9AB0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Messungen (2)</span><span class="informations">3840×2160 644 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>In picture 2 the markups are almost invisible. Can this be shown clearly and clearly with a contrasting color? How can I hide the zoomed label?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/51e98d26e1e0d16518a2cb47b031261ba16280f0.jpeg" data-download-href="/uploads/short-url/bGD3vDNy67xy9w6Q6UPPpRzoD3a.jpeg?dl=1" title="Messungen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/51e98d26e1e0d16518a2cb47b031261ba16280f0_2_690x388.jpeg" alt="Messungen" data-base62-sha1="bGD3vDNy67xy9w6Q6UPPpRzoD3a" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/51e98d26e1e0d16518a2cb47b031261ba16280f0_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/51e98d26e1e0d16518a2cb47b031261ba16280f0_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/51e98d26e1e0d16518a2cb47b031261ba16280f0_2_1380x776.jpeg 2x" data-dominant-color="998992"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Messungen</span><span class="informations">3840×2160 713 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Last question:<br>
How can I graphically represent the wall thickness of the vessel (connecting line of the two markup points)?</p>
<p>best regards</p>

---

## Post #2 by @muratmaga (2020-10-18 21:10 UTC)

<p>You can control the label size and color in the Display Tab of the Markups module (glyph for point size, text for label size). However, to do that you should use the Line tool of Markups instead of the deprecated Ruler tool that you have been using. You will find it easier to adjust the text easier with its Markups equivalent (which adjust the text in 3D viewer and cross-sections much better than the Ruler tool).</p>

---
