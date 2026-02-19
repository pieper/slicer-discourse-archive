---
topic_id: 21099
title: "Custom Module Presentation Straight Curve Gauge"
date: 2021-12-16
url: https://discourse.slicer.org/t/21099
---

# Custom module presentation : Straight Curve Gauge

**Topic ID**: 21099
**Date**: 2021-12-16
**URL**: https://discourse.slicer.org/t/custom-module-presentation-straight-curve-gauge/21099

---

## Post #1 by @chir.set (2021-12-16 19:54 UTC)

<p>Custom module presentation : Straight Curve Gauge</p>
<p>To core developers,</p>
<p>I wish to propose this <a href="https://github.com/chir-set/StraightCurveGauge" rel="noopener nofollow ugc">custom module</a> for inclusion in a relevant Slicer repository.</p>
<p>I am aware that it’s possible to propose it as a custom downloadable extension on its own. Before, I wish to know if it is felt a useful addition to the vast panel of Slicer tools.</p>
<p>Its goal is quite <a href="https://en.wikipedia.org/wiki/KISS_principle" rel="noopener nofollow ugc">KISS</a>-like : straighten a markups open curve and measure distances between control points.</p>
<p>It is primarily intended to quantify arterial stenosis by diameter in slice views, an activity that may be performed many times a day in vascular surgery. It allows to do this very quickly and thus saves much time. This is why I believe it may be useful to others, and hence this proposal.</p>
<p>The same final result can be obtained by drawing multiple markups lines on a single slice, or one single markups line that is stretched as many times as required, then calculate multiple values one by one. This is of course more tedious for a simple common task.</p>
<p>It may be further customized of course. For example, straightening the curve may be performed on demand, and distances are then computed on curved portions. It is not implemented because I don’t find a practical use case for this. Code quality can also be optimized, it’s the best I can do as it is however.</p>
<p>As for a repository, I think SlicerSandbox would be an appropriate home for it.</p>
<p>If you think it’s not fit for any Slicer usual tool repositories, no problem at all, it will remain available in my Github repository.</p>
<p>Regards.</p>

---

## Post #2 by @pieper (2021-12-16 20:45 UTC)

<p>It sounds very useful to me.  It could be it’s own extension as a start, but integrating it in to the Markups natively sounds handy to me.</p>

---

## Post #3 by @chir.set (2021-12-17 07:35 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="21099">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>It could be it’s own extension</p>
</blockquote>
</aside>
<p>Great, I’ll look forward  how to do that, thanks.</p>

---
