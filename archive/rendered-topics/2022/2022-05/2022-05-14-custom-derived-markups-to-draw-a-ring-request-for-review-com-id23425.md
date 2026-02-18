# Custom derived markups to draw a ring : request for review, comments

**Topic ID**: 23425
**Date**: 2022-05-14
**URL**: https://discourse.slicer.org/t/custom-derived-markups-to-draw-a-ring-request-for-review-comments/23425

---

## Post #1 by @chir.set (2022-05-14 09:48 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/cpinter">@cpinter</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a> <span class="mention">@coreDevs</span></p>
<p>This <a href="https://github.com/chir-set/ExtraMarkups" rel="noopener nofollow ugc">custom</a> markups uses a base markups line to draw a ring in 2 modes.</p>
<ol>
<li>The first control point of the base line is the center of the ring, and the<br>
line’s length is its radius.</li>
<li>Both control points of the base line lie on the circumference of the ring.<br>
The line’s length is its diameter.</li>
</ol>
<p>A couple of points are unclear to me, as commented inline. I wish core developpers could comment on these.</p>
<p>I don’t primarily intend to make a self-contained extension of this work. If you find value in it, I’ll be glad to fix anything upon your instructions, and prepare it for a merge in the markups module eventually. Else, it will be available in my repository.</p>
<p>Regards.</p>

---

## Post #2 by @cpinter (2022-05-16 09:32 UTC)

<p>Thank you for the contribution! I tried to find these questions, but I don’t see and issues or PRs, and I don’t have time to read the whole code. Can you please point us to these questions? Thank you!</p>
<blockquote>
<p>I don’t primarily intend to make a self-contained extension of this work.</p>
</blockquote>
<p>In my opinion making this repository an extension in the Extension Manager would be the best option. The Markups module contains the most frequently used markups, and the list (and the toolbar) is already quite long. I’d not make it longer by default, and some really useful markups are in extensions too (see this extension for example <a href="https://github.com/SlicerHeart/SlicerSurfaceMarkup" class="inline-onebox">GitHub - SlicerHeart/SlicerSurfaceMarkup: Extension to test the new grid surface markup with</a>).</p>

---

## Post #3 by @chir.set (2022-05-20 15:43 UTC)

<p>Hi,</p>
<p>Sorry for the late reply.</p>
<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="23425">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>making this repository an extension in the Extension Manager would be the best option.</p>
</blockquote>
</aside>
<p>That might be the best option, I’m not yet ready for that now.</p>
<p>I updated the code thoroughly, it’s in a better shape now. I’ll get back when I’ll stumble on blocking events.</p>
<p>Thank you for your input.</p>

---
