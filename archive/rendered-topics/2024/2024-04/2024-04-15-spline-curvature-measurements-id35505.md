# Spline Curvature Measurements

**Topic ID**: 35505
**Date**: 2024-04-15
**URL**: https://discourse.slicer.org/t/spline-curvature-measurements/35505

---

## Post #1 by @chub (2024-04-15 19:41 UTC)

<p>Hello!</p>
<p>I am attempting to characterize curvature of lung anatomy. I am creating splines down the center of bronchi by placing  ~5 equidistant control points (~70mm total length). When looking at the curvature mean and curvature max outputs, I am getting a curvature mean of 0.071 mm-1 and a curvature max of 0.419mm-1. This curvature max measurement does not seem to be matching the curvature of my spline as least from a visual comparison standpoint. Was wondering how the software calculates the curvature max measurement based on the spline. Additionally, if there are any other recommended methods to characterize the “smallest” radius of curvature along the length of a spline, it would be much appreciated.</p>
<p>Thanks,<br>
Brandon</p>

---

## Post #2 by @bw3232 (2024-04-17 17:00 UTC)

<p>This would be really helpful for me as well! The measurements seem severe for curve max on many of my splines.</p>

---

## Post #3 by @lassoan (2024-04-17 17:32 UTC)

<aside class="quote no-group" data-username="chub" data-post="1" data-topic="35505">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chub/48/70059_2.png" class="avatar"> chub:</div>
<blockquote>
<p>This curvature max measurement does not seem to be matching the curvature of my spline as least from a visual comparison standpoint.</p>
</blockquote>
</aside>
<p>Can you show a screenshot?</p>
<p>You can color the curve by curvature in Markups module → Display → Scalars → visibility: enable, active scalar: curvature (and you may wan to set Scalar range mode to Manual and adjust the sliders manually). That may help explaining the numbers.</p>
<p>You may want to resample the curve (Markups module → Resample) to ensure that the curve is smooth and control points are uniformly spaced.</p>

---

## Post #4 by @chub (2024-04-17 22:32 UTC)

<p>Hi Andras,</p>
<p>Thanks for the reply! Tried out what you suggested and it looks like it improved the measurements. Curvature max went from 0.419mm-1 to 0.109mm-1.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c6e6cf1d9208b2d3ab79ed1153b152b6215068f.png" alt="image" data-base62-sha1="43vXcsId6nylVeLoEu0geglEhEb" width="463" height="369"></p>

---

## Post #5 by @lassoan (2024-04-17 23:58 UTC)

<p>Thanks for the update. This suggests that you got the high curvature value because there was some local noise on the curve points.</p>

---
