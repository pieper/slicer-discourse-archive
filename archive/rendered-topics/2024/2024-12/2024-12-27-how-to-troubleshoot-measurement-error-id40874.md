# How to troubleshoot measurement error 

**Topic ID**: 40874
**Date**: 2024-12-27
**URL**: https://discourse.slicer.org/t/how-to-troubleshoot-measurement-error/40874

---

## Post #1 by @PitaChib (2024-12-27 21:26 UTC)

<p>So I’m measuring a bunch of basic measurements for a group of skulls, and I always follow the same protocol of getting an volume from imageStack.<br>
One of the current one I’m doing (resolution is 29.99 um), I exported from ImageStack as follows:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e9ad26cb17c13c3596c200e63fb626f33687e72.png" data-download-href="/uploads/short-url/fMse1RQhY4sfD889qhQxyrHZS4W.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e9ad26cb17c13c3596c200e63fb626f33687e72_2_689x500.png" alt="image" data-base62-sha1="fMse1RQhY4sfD889qhQxyrHZS4W" width="689" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e9ad26cb17c13c3596c200e63fb626f33687e72_2_689x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6e9ad26cb17c13c3596c200e63fb626f33687e72_2_1033x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e9ad26cb17c13c3596c200e63fb626f33687e72.png 2x" data-dominant-color="E8E8E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1356×984 49.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But when I went to measure condylobasal length for this specimen it’s averaging around 231mm<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9266bf42510de7bd863ca687d3442d43c83fd66.png" data-download-href="/uploads/short-url/xgxzg8C0T3fLfxz3Crszm4NG68u.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9266bf42510de7bd863ca687d3442d43c83fd66_2_690x367.png" alt="image" data-base62-sha1="xgxzg8C0T3fLfxz3Crszm4NG68u" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9266bf42510de7bd863ca687d3442d43c83fd66_2_690x367.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9266bf42510de7bd863ca687d3442d43c83fd66_2_1035x550.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9266bf42510de7bd863ca687d3442d43c83fd66.png 2x" data-dominant-color="EEEEEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1336×712 53.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
which is not possible given my other samples are averaging 23mm. I think it’s a scaling issue I might’ve mistaken, but I don’t know where to start troubleshooting. Any suggestions appreciated! Thanks.</p>

---

## Post #2 by @lassoan (2024-12-27 21:30 UTC)

<aside class="quote no-group" data-username="PitaChib" data-post="1" data-topic="40874">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pitachib/48/78512_2.png" class="avatar"> PitaChib:</div>
<blockquote>
<p>One of the current one I’m doing (resolution is 29.99 um), I exported from ImageStack</p>
</blockquote>
</aside>
<p>The screenshot shows that you entered 0.299 mm = 299 micrometer pixel size, so all the linear measurement results will be 10x larger than the actual size.</p>

---

## Post #3 by @PitaChib (2024-12-27 22:00 UTC)

<p>Thanks! I realized that immediately after I posted and I apologize for the brainfog. Is the only way to reverse this to change from ImageStack? I have a batch need to rescale it’d be nice not having to do that again.<br>
With lots of gratitude.</p>

---

## Post #4 by @lassoan (2024-12-27 23:54 UTC)

<p>You can change the image spacing in Volumes module / Volume information section.</p>

---
