# Spine segmentation

**Topic ID**: 11393
**Date**: 2020-05-03
**URL**: https://discourse.slicer.org/t/spine-segmentation/11393

---

## Post #1 by @TMrt (2020-05-03 23:51 UTC)

<p>Ok that’s great and I will try that.</p>
<p>While segmenting individual similar lumbar vertebrae, I want to copy a completed single lumbar segmentation and move it to the next one and edit anything that didn’t match just to see how that compares to my current work flow.</p>
<p>The vertebrae all need to be separated.  Straight threshold or grow from seeds requires a fair amount of post editing cleanup.  I’m experimenting with a few work flows using threshold masking, flood fill, closing and median smoothing for each one to achieve an accurate and faster process.</p>
<p>Thanks so much</p>

---

## Post #2 by @lassoan (2020-05-04 03:13 UTC)

<aside class="quote no-group" data-username="TMrt" data-post="1" data-topic="11393">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tmrt/48/5432_2.png" class="avatar"> TMrt:</div>
<blockquote>
<p>While segmenting individual similar lumbar vertebrae, I want to copy a completed single lumbar segmentation and move it to the next one and edit anything that didn’t match</p>
</blockquote>
</aside>
<p>This idea may work but might not be ideal, due to:</p>
<ol>
<li>Fixing an imperfect a segmentation usually takes more time than creating it from scratch</li>
<li>If you start from a similar segmentation then that may end up with less accurate segmentation, as you are more likely to leave small segmentation errors unfixed; and if you make small fixes then they editing may leave artifacts.</li>
</ol>
<p>If you try it then at least don’t do a simple rigid transform but do landmark-based warping. You can use SlicerIGT extension’s Fiducial Registration Wizard module for this; or you may try automatic image-based registration using SlicerElastix.</p>
<p>Also, it may be better to register a set of vertebrae at once instead of a single vertebra. It may save you time, it may make automatic intensity-based registration more robust, and vertebrae at the same level may be more similar to each other (even if they are from different patients).</p>
<aside class="quote no-group" data-username="TMrt" data-post="1" data-topic="11393">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tmrt/48/5432_2.png" class="avatar"> TMrt:</div>
<blockquote>
<p>I’m experimenting with a few work flows using threshold masking, flood fill, closing and median smoothing for each one to achieve an accurate and faster process.</p>
</blockquote>
</aside>
<p>Grow from seeds with intensity-based masking (see <a href="https://lassoan.github.io/SlicerSegmentationRecipes/AortaMaskedGrowFromSeeds/">this</a> segmentation recipe for an example) is always better than threshold and flood fill. You can put a different seed in each vertebra, which gives you automatic separation between vertebrae.</p>
<p>Basic smoothing operations, such as closing and median filtering can fill small holes but if “Grow from seeds” cannot fill cancellous internals of vertebral bodies then you can use “<a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify">Wrap Solidify</a>” effect (provided by SurfaceWrapSolidify extension).</p>
<p>Keep us updated about what you find working for you or if you need more details about any of the above techniques.</p>

---

## Post #3 by @TMrt (2020-05-04 21:36 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d5ef7b23b93babb3e2499044d023fd0094f80c9.png" data-download-href="/uploads/short-url/b2seoVnxRljXkRohz2Y2ozklq8V.png?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d5ef7b23b93babb3e2499044d023fd0094f80c9_2_677x500.png" alt="Screenshot" data-base62-sha1="b2seoVnxRljXkRohz2Y2ozklq8V" width="677" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4d5ef7b23b93babb3e2499044d023fd0094f80c9_2_677x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d5ef7b23b93babb3e2499044d023fd0094f80c9.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d5ef7b23b93babb3e2499044d023fd0094f80c9.png 2x" data-dominant-color="6C6480"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">829×612 167 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Thank you for all of the options included in your response.</p>
<p>The included screenshot is L-1 (red) transformed onto to L-2 (pink), which had the best results for me.   The conclusion was best said in your first and second point about creating each lumbar individually. It was a cleaner and faster process, but I’m very happy to learn and interchange the many options available.</p>
<p>I appreciate your help.  Many thanks!</p>

---
