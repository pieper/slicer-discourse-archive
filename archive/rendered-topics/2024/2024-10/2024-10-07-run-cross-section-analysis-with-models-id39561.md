# Run Cross-Section Analysis with models

**Topic ID**: 39561
**Date**: 2024-10-07
**URL**: https://discourse.slicer.org/t/run-cross-section-analysis-with-models/39561

---

## Post #1 by @SANTIAGO_PENDON_MING (2024-10-07 09:58 UTC)

<p>Hi to everyone. My team and I were in troubles with Cross-Section Analysis extension a few months ago. The problem remains today… (See more in<br>
<a href="https://discourse.slicer.org/t/cross-section-analysis-freezing/37206/17">https://discourse.slicer.org/t/cross-section-analysis-freezing/37206/17</a>)</p>
<p>We see that the manual module execution allows the usage of models data instead segmentation+segment inputs. Is possible to call <code>logic.setLumenSurface()</code> with the model? At the moment I have the models in shNode folders…</p>
<p>Also, one quick question: What happen when the centerline is outside the segment/model? Or more hardcore, when the complete segment is empty?</p>
<p>Thanks a lot <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @chir.set (2024-10-07 11:11 UTC)

<aside class="quote no-group" data-username="SANTIAGO_PENDON_MING" data-post="1" data-topic="39561">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/santiago_pendon_ming/48/66060_2.png" class="avatar"> SANTIAGO_PENDON_MING:</div>
<blockquote>
<p>What happen when the centerline is outside the segment/model? Or more hardcore, when the complete segment is empty?</p>
</blockquote>
</aside>
<p>GIGO: Good Input, Good Output.</p>
<p>Please use valid data per the design of the module.</p>
<p>As for your questions here and in the other thread, please provide the scene as an MRB file, application log, version and platform.</p>

---
