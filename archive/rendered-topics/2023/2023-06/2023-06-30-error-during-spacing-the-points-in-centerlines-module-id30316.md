# Error during spacing the points in centerlines module

**Topic ID**: 30316
**Date**: 2023-06-30
**URL**: https://discourse.slicer.org/t/error-during-spacing-the-points-in-centerlines-module/30316

---

## Post #1 by @SANTIAGO_PENDON_MING (2023-06-30 10:36 UTC)

<p>Hi to everyone once again  <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>In this ocassion I found a strange issue during the extract centerlines process with ‘extract centerlines’ module.</p>
<p>I need a specific curve sampling for my centerlines so I select ‘Curve sampling distance’ as 0.2500mm and the run the module.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b5913e2654e1b5cb4e20997317da88890229e15.png" data-download-href="/uploads/short-url/aKyEOzJaPyit2kXPPapGt6kmOGh.png?dl=1" title="settings" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b5913e2654e1b5cb4e20997317da88890229e15_2_483x500.png" alt="settings" data-base62-sha1="aKyEOzJaPyit2kXPPapGt6kmOGh" width="483" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b5913e2654e1b5cb4e20997317da88890229e15_2_483x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b5913e2654e1b5cb4e20997317da88890229e15_2_724x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b5913e2654e1b5cb4e20997317da88890229e15.png 2x" data-dominant-color="3B3B3B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">settings</span><span class="informations">732×757 27.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When the module ends, it returns the centerlines pretty good but, if you look closer to bifurcations, the points spacing is not the selected one as you can see in the next image:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/269ed0ce3eb057186c34566e94cf4bb7e97abe32.png" data-download-href="/uploads/short-url/5vEp6aHGgT3GIqSnGnj6Prm1Nbc.png?dl=1" title="points" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/269ed0ce3eb057186c34566e94cf4bb7e97abe32_2_646x500.png" alt="points" data-base62-sha1="5vEp6aHGgT3GIqSnGnj6Prm1Nbc" width="646" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/269ed0ce3eb057186c34566e94cf4bb7e97abe32_2_646x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/269ed0ce3eb057186c34566e94cf4bb7e97abe32.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/269ed0ce3eb057186c34566e94cf4bb7e97abe32.png 2x" data-dominant-color="42436A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">points</span><span class="informations">840×650 36.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The whole centerlines ends in the pink point, but the gap between points here it´s too big.</p>
<p>I solved this applying a resampling in markups module, but it would be great if the ‘extract centerlines’ would do the correct spacing.</p>
<p>Thanks a lot ^^.</p>

---

## Post #2 by @lassoan (2023-06-30 11:45 UTC)

<p>Sampling distance does not apply to the line segment that connects the bifurcation point to the branch. Length of that segment depends on the vessel diameter. Resampling the curve is a good way to force the same control point spacing along the entire curve.</p>

---
