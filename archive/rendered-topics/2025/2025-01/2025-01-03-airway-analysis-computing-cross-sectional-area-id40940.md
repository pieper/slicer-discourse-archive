---
topic_id: 40940
title: "Airway Analysis Computing Cross Sectional Area"
date: 2025-01-03
url: https://discourse.slicer.org/t/40940
---

# Airway analysis, computing cross-sectional area

**Topic ID**: 40940
**Date**: 2025-01-03
**URL**: https://discourse.slicer.org/t/airway-analysis-computing-cross-sectional-area/40940

---

## Post #1 by @dcg494 (2025-01-03 08:01 UTC)

<p>Hi everyone, i would like to be able to replicate what another programme can do to analyze the airways in terms of cross-sectional area, including pinpointing the minimum cross-sectional airway, for the upper airway (see top image).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97529fc526afd45a0fa80904e9dabd52bb17b452.jpeg" data-download-href="/uploads/short-url/lAF7oOPAzgiOydUkQAHqRpJjszg.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97529fc526afd45a0fa80904e9dabd52bb17b452_2_542x500.jpeg" alt="image" data-base62-sha1="lAF7oOPAzgiOydUkQAHqRpJjszg" width="542" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97529fc526afd45a0fa80904e9dabd52bb17b452_2_542x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97529fc526afd45a0fa80904e9dabd52bb17b452.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97529fc526afd45a0fa80904e9dabd52bb17b452.jpeg 2x" data-dominant-color="8C928B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">650×599 48.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>What i’ve been able to do so far is just graph the cross-sectional area of a segment of the UA, which is good (see below picture). But is there a way to map these findings onto the segment in a color-coded map ? Or is there another module that will do a better job altogether ?</p>
<p>Thanks a lot for any and all help on this</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e9d12ab0acb392adf36c5a6ff6b7ded3b29b9fa.jpeg" data-download-href="/uploads/short-url/fMx326f479dvMeTONDv1imjL2B4.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e9d12ab0acb392adf36c5a6ff6b7ded3b29b9fa_2_592x500.jpeg" alt="image" data-base62-sha1="fMx326f479dvMeTONDv1imjL2B4" width="592" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e9d12ab0acb392adf36c5a6ff6b7ded3b29b9fa_2_592x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e9d12ab0acb392adf36c5a6ff6b7ded3b29b9fa_2_888x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e9d12ab0acb392adf36c5a6ff6b7ded3b29b9fa_2_1184x1000.jpeg 2x" data-dominant-color="5D5E57"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1543×1302 108 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @chir.set (2025-01-03 09:27 UTC)

<aside class="quote no-group" data-username="dcg494" data-post="1" data-topic="40940">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/cdc98d/48.png" class="avatar"> dcg494:</div>
<blockquote>
<p>another module</p>
</blockquote>
</aside>
<p>If you extract a centerline with the ‘Extract centerline’ module of the SlicerVMTK extension, you could next investigate the ‘Cross-section analysis’ module to get the minimum area. It won’t do any color mapping of the segment itself however. But you can do such a mapping with the centerline model.</p>

---
