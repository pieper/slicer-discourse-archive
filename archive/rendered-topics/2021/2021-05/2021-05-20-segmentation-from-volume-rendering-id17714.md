---
topic_id: 17714
title: "Segmentation From Volume Rendering"
date: 2021-05-20
url: https://discourse.slicer.org/t/17714
---

# Segmentation from volume rendering

**Topic ID**: 17714
**Date**: 2021-05-20
**URL**: https://discourse.slicer.org/t/segmentation-from-volume-rendering/17714

---

## Post #1 by @muratmaga (2021-05-20 18:59 UTC)

<p>This is sort of a variation <a href="https://discourse.slicer.org/t/is-centerline-extraction-from-volume-rendering-possible/16922">on this inquiry</a></p>
<p>My colleagues do a quite a bit of manual segmentations from optical microscopy data. They use a software called Imaris, in which they manually trace small vessels they are interested by drawing on a volume rendered image of the structure. Then they keep adding to grow the network by rotating the volume rendering and keep painting .</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d518b50cac4d09379dd6028b249d2a02163708c4.jpeg" data-download-href="/uploads/short-url/up8DrvXg0PAz1qZhz0I78hg9ohK.jpeg?dl=1" title="IMG_20210520_113707"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d518b50cac4d09379dd6028b249d2a02163708c4_2_666x500.jpeg" alt="IMG_20210520_113707" data-base62-sha1="up8DrvXg0PAz1qZhz0I78hg9ohK" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d518b50cac4d09379dd6028b249d2a02163708c4_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d518b50cac4d09379dd6028b249d2a02163708c4_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d518b50cac4d09379dd6028b249d2a02163708c4_2_1332x1000.jpeg 2x" data-dominant-color="5A7A74"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_20210520_113707</span><span class="informations">1823×1367 187 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Would it be possible to do something like this in Slicer?</p>

---

## Post #2 by @pieper (2021-05-20 19:07 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="1" data-topic="17714">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Would it be possible to do something like this in Slicer?</p>
</blockquote>
</aside>
<p>Yes, I don’t see why not.  We can already place markups on volume rendering, so it would be a matter of converting that to segmentation in the local volume around the markup, probably using a threshold and a distance map, perhaps with a shape constraint to deal with noisy / sparsely sampled data.</p>

---

## Post #3 by @lassoan (2021-05-21 04:41 UTC)

<p>You can also use Draw Tube segment editor effect (in SegmentEditorExtraEffects extension) in combination with intensity range masking to paint vessel near a markups curve.</p>
<p>However, there is a good chance that you can add vessel segments much faster by using “Local thresholding” effect (or maybe even “Fast marching”). It may require some experimentation to find good parameters, but once you determined those, you can use the same settings on many cases and it could easily result in 10x faster segmentation process.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="yi07mjr3JeU" data-video-title="New vessel branch extraction module for 3D Slicer" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=yi07mjr3JeU" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/yi07mjr3JeU/maxresdefault.jpg" title="New vessel branch extraction module for 3D Slicer" width="" height="">
  </a>
</div>

<p>You may also extract the entire vessel tree and let Slicer automatically find path between two designated vessel end points.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="UpfDP6ejCjg" data-video-title="Finding shortest path between two points in the bronchial tree" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=UpfDP6ejCjg" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/UpfDP6ejCjg/maxresdefault.jpg" title="Finding shortest path between two points in the bronchial tree" width="" height="">
  </a>
</div>


---
