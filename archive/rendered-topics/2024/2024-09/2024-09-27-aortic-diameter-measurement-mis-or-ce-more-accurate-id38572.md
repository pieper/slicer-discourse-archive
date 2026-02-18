# Aortic Diameter Measurement - MIS or CE more accurate?

**Topic ID**: 38572
**Date**: 2024-09-27
**URL**: https://discourse.slicer.org/t/aortic-diameter-measurement-mis-or-ce-more-accurate/38572

---

## Post #1 by @Joe_Makoid (2024-09-27 21:09 UTC)

<p>Hello,</p>
<p>. I am segmenting the entire aorta and running a centerline extraction then analyzing it in cross-section analysis module.</p>
<p>The MIS diameter and CE diameter seem to be materially different at some locations (specifically at the arch it seems). Do you know which one is more accurate? At first glance, it looks like CE is more accurate, except when you get to the arch it measures a plane that isn’t perfectly perpendicular to the centerline and therefore overestimates the true diameter.</p>
<p>Would love to know the thoughts of an expert on this!!</p>

---

## Post #2 by @lassoan (2024-09-27 21:16 UTC)

<p>Both values are accurate and they have different meanings. MIS characterizes the maximum diameter (value depends on the 3D shape of the vessel at that centerline position), while CE is computed solely from cross-sectional area (shape does not matter). When shape of the cross-section is perfect circle then the values are the same.</p>

---

## Post #3 by @Joe_Makoid (2024-09-27 21:25 UTC)

<p>awesome! Thank you <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>I am sort of getting it (I think(…i guess my question is, is it possible for the CE to be “tricked” in the aortic arch and not taking a measurement that is perpendicular to the centerline? (the true aortic diameter)…is the only way to truly get the max aortic diameter to straighten it somehow?</p>
<p>thanks so much!!</p>

---

## Post #4 by @chir.set (2024-09-27 21:33 UTC)

<aside class="quote no-group" data-username="Joe_Makoid" data-post="1" data-topic="38572">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/joe_makoid/48/78065_2.png" class="avatar"> Joe_Makoid:</div>
<blockquote>
<p>a plane that isn’t perfectly perpendicular to the centerline</p>
</blockquote>
</aside>
<p>If you use a curve centerline, this perception is greatly reduced. You may also increase the resolution of the curve by choosing a smaller ‘Curve sampling distance’ in the ‘Extract centerline module’.</p>
<aside class="quote no-group" data-username="Joe_Makoid" data-post="3" data-topic="38572">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/joe_makoid/48/78065_2.png" class="avatar"> Joe_Makoid:</div>
<blockquote>
<p>straighten it somehow</p>
</blockquote>
</aside>
<p>That’s a good option.</p>

---

## Post #5 by @chir.set (2024-09-27 21:38 UTC)

<aside class="quote no-group" data-username="Joe_Makoid" data-post="3" data-topic="38572">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/joe_makoid/48/78065_2.png" class="avatar"> Joe_Makoid:</div>
<blockquote>
<p>the only way to truly get the max aortic diameter to straighten it somehow?</p>
</blockquote>
</aside>
<p>To get a perfect straightening, you need also a perfect input curve: how should that be determined?</p>

---
