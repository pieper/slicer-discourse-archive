---
topic_id: 4368
title: "Improved Interactions In Virtual Reality"
date: 2018-10-11
url: https://discourse.slicer.org/t/4368
---

# Improved interactions in virtual reality

**Topic ID**: 4368
**Date**: 2018-10-11
**URL**: https://discourse.slicer.org/t/improved-interactions-in-virtual-reality/4368

---

## Post #1 by @cpinter (2018-10-11 20:29 UTC)

<p>New features in <a href="https://github.com/KitwareMedical/SlicerVirtualReality">SlicerVirtualReality</a>:</p>
<ul>
<li>Position MRML objects in VR</li>
<li>Two-handed world manipulation gesture for pan, rotate, zoom</li>
</ul>
<p>The video shows the improvements used for pedicle screw placement procedure with three visualization techniques:</p>
<ul>
<li>Volume rendering with dynamic slice view</li>
<li>Solid volume rendering</li>
<li>Surface rendering</li>
</ul>
<p>Available for 3D Slicer version 4.10</p>
<div class="lazyYT" data-youtube-id="F_UBoE4FaoY" data-youtube-title="Pedicle screw insertion in virtual reality" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>

---

## Post #2 by @pieper (2018-10-11 21:44 UTC)

<p>Looks great!</p>
<p>A couple questions come to mind:</p>
<ul>
<li>
<p>watching the video, it appears you are very confidently just putting the screw in the right place.  Compared to doing the same operation with the mouse, how does the interaction feel in terms of accuracy and efficiency?</p>
</li>
<li>
<p>do you get ‘<a href="https://phys.org/news/2017-05-gorilla-arm-fatigue-mid-air-usage.html">gorilla arm</a>’ with that style of interaction?</p>
</li>
</ul>

---

## Post #3 by @lassoan (2018-10-12 03:59 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="4368">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>it appears you are very confidently just putting the screw in the right place</p>
</blockquote>
</aside>
<p>It was more like putting it to approximately correct position in 5-10 seconds then spend tens of seconds to look at it from various directions and fine-tune the position.</p>
<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="4368">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>do you get ‘<a href="https://phys.org/news/2017-05-gorilla-arm-fatigue-mid-air-usage.html">gorilla arm </a>’ with that style of interaction?</p>
</blockquote>
</aside>
<p>I didn’t experience any arm fatigue when I tried it. I always moved/rotated/zoomed the world to be close to me (it is quite intuitive now with the two-handed grab gestures) and so I could keep my arms close to my body, in a comfortably bent position. Csaba does it similarly in the video - he reaches out, pulls the model to be right in front of him, and then the rest is mostly fine manipulation. Also, I always tried this only for couple of minutes at a time, so maybe this was just not long enough to get tired.</p>
<p><a class="mention" href="/u/cpinter">@cpinter</a> did you have the same experience?</p>

---

## Post #4 by @pieper (2018-10-12 11:50 UTC)

<p>Thanks for the info.  Sounds like a NASA-TLX style of study would be interesting.</p>

---

## Post #5 by @cpinter (2018-10-12 13:38 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="4368">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>it appears you are very confidently just putting the screw in the right place</p>
</blockquote>
</aside>
<p>It’s very easy to see in stereo the approximate position it needs to be, so it’s basically one hand motion to move it there. But then as the canal where the screw needs to be is quite narrow, a lot of small adjustments are needed. And for that clipping is super useful. Looking forward to the sphere clipping you guys prototyped in Las Palmas!</p>
<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="4368">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>do you get ‘<a href="https://phys.org/news/2017-05-gorilla-arm-fatigue-mid-air-usage.html">gorilla arm</a>’ with that style of interaction?</p>
</blockquote>
</aside>
<p>I have worked for weeks on the controller interactions, which means I was basically continually waving my arms. I experienced no fatigue. As <a class="mention" href="/u/lassoan">@lassoan</a> says it is intuitive to pull the objects close to me for better visibility, and in that position I can even put my elbows on the armrest of my chair sometimes and then it becomes effortless. I’d argue that it’s more ergonomic than a regular mouse, for which one has to hold their wrists in an unnatural angle.<br>
I can imagine fatigue if you have to do it for half an hour without interruption and without supporting your elbows, but I don’t see that with our current applications.</p>

---
