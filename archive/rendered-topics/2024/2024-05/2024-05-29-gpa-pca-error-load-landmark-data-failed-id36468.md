# GPA + PCA Error: Load landmark data failed

**Topic ID**: 36468
**Date**: 2024-05-29
**URL**: https://discourse.slicer.org/t/gpa-pca-error-load-landmark-data-failed/36468

---

## Post #1 by @kgies10 (2024-05-29 13:53 UTC)

<p>Operating system: Mac OS 14.4.1<br>
Slicer version: 5.6.2<br>
Expected behavior: Generate GPA and PCA<br>
Actual behavior: The following Error and warning messages:</p>
<blockquote>
<p>QRegularExpressionPrivate::doMatch(): called on an invalid QRegularExpression object</p>
<p>QRegularExpressionPrivate::doMatch(): called on an invalid QRegularExpression object</p>
<p>QRegularExpressionPrivate::doMatch(): called on an invalid QRegularExpression object</p>
<p>QRegularExpressionPrivate::doMatch(): called on an invalid QRegularExpression object</p>
</blockquote>
<p>AND then:</p>
<blockquote>
<p>Load landmark data failed: Could not create an array from landmark files</p>
</blockquote>
<p>I’m looking at 8 specimens I’ve landmarked using ALPACA. I’ve moved all the .mrk.json landmark files produced from running ALPACA into a single directory to run the GPA +PCA. I’ve examined the files briefly to make sure they have the same number of landmarks and they have all have 4066 pseudolandmarks. I’ve tried running GPA on only 2 or 3 specimens and get the same errors.</p>
<p>When I ran ALPACA, it took my computer several hours. Did I do something wrong when I ran ALPACA? I left scaling and projection unchecked. I’ve included an image of some of the specimens and landmarks. Thank you for your help. I am a SlicerMorph novice and appreciate any insight you can provide. Thanks.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/28d9cdbfba6ca84f02aa82e96f8d76db38b1d4c8.jpeg" data-download-href="/uploads/short-url/5PnJWOHlu8eCq8dKcBaNDjbmQcM.jpeg?dl=1" title="Screenshot 2024-05-28 at 9.14.19 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/28d9cdbfba6ca84f02aa82e96f8d76db38b1d4c8_2_557x500.jpeg" alt="Screenshot 2024-05-28 at 9.14.19 AM" data-base62-sha1="5PnJWOHlu8eCq8dKcBaNDjbmQcM" width="557" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/28d9cdbfba6ca84f02aa82e96f8d76db38b1d4c8_2_557x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/28d9cdbfba6ca84f02aa82e96f8d76db38b1d4c8_2_835x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/8/28d9cdbfba6ca84f02aa82e96f8d76db38b1d4c8_2_1114x1000.jpeg 2x" data-dominant-color="9793C9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-05-28 at 9.14.19 AM</span><span class="informations">1174×1052 99.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2024-05-29 15:20 UTC)

<aside class="quote no-group" data-username="kgies10" data-post="1" data-topic="36468">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/74df32/48.png" class="avatar"> kgies10:</div>
<blockquote>
<p>I’m looking at 8 specimens I’ve landmarked using ALPACA. I’ve moved all the .mrk.json landmark files produced from running ALPACA into a single directory to run the GPA +PCA. I’ve examined the files briefly to make sure they have the same number of landmarks and they have all have 4066 pseudolandmarks. I’ve tried running GPA on only 2 or 3 specimens and get the same errors.</p>
</blockquote>
</aside>
<p>If you can share the data we can take a look.</p>

---

## Post #3 by @kgies10 (2024-05-29 16:10 UTC)

<p>Thank you for your reply! I reran the analysis and used fewer landmarks (600 instead of 4k) and checked projection and scaling and now it works! I used the projected landmarks in the analysis. I think it was either number of landmarks I used or that I didn’t project or scale the data.</p>

---

## Post #4 by @muratmaga (2024-05-29 18:55 UTC)

<aside class="quote no-group" data-username="kgies10" data-post="3" data-topic="36468">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/74df32/48.png" class="avatar"> kgies10:</div>
<blockquote>
<p>project or scale the data.</p>
</blockquote>
</aside>
<p>Projecting the points can take a while for dense point clouds like this. Try the original without choosing the project points. The caveat it they may end up not on the surface of the target model.</p>

---
