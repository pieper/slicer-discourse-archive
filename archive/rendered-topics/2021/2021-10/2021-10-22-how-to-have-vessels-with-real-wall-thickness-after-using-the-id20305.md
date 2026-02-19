---
topic_id: 20305
title: "How To Have Vessels With Real Wall Thickness After Using The"
date: 2021-10-22
url: https://discourse.slicer.org/t/20305
---

# how to have vessels with real wall thickness after using the hollow?

**Topic ID**: 20305
**Date**: 2021-10-22
**URL**: https://discourse.slicer.org/t/how-to-have-vessels-with-real-wall-thickness-after-using-the-hollow/20305

---

## Post #1 by @Sevda_Zarei (2021-10-22 18:51 UTC)

<p>Hello<br>
I hope this massage find you well.</p>
<p>I used hollow to my model but it changes vessel’s wall thickness to a constant thickness like 0.4 mm thickness in whole model.<br>
we know that vessel wall thickness changes during generation and bifurcations.<br>
I want to have real wall thickness in up to down of the vessels. how can i do that??</p>
<p>My another question is that how can i cut end of the vessels to gives me free end? like ends free cylinder.</p>

---

## Post #2 by @lassoan (2021-10-22 18:55 UTC)

<p>You can put the large vessels in one segment and small vessels in another one. Then when you make each segment hollow you can choose a different wall thickness.</p>
<p>You can cut the ends open very easily using Scissors effect, in 3D views.</p>

---

## Post #3 by @Sevda_Zarei (2021-10-22 19:10 UTC)

<p>How can i know the real thickness of the vessels before using hollow?</p>
<p>I tried to use Scissors effect but it gives me closed ends again.</p>

---

## Post #4 by @lassoan (2021-10-23 15:22 UTC)

<aside class="quote no-group" data-username="Sevda_Zarei" data-post="3" data-topic="20305">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sevda_zarei/48/9336_2.png" class="avatar"> Sevda_Zarei:</div>
<blockquote>
<p>How can i know the real thickness of the vessels before using hollow?</p>
</blockquote>
</aside>
<p>In general, you don’t know the real thickness, as on typical clinical CT images you cannot measure it accurately. You can measure it directly using IVUS or ex vivo using microCT. However, even if you can measure thickness, you cannot measure mechanical properties in vivo, which may highly patient specific and spatially varying due to calcifications and other changes in the vessel.</p>
<p>Even if you knew exactly the geometry, wall thickness, material properties, etc. you would not be able to reproduce those exactly with current 3D printing technology.</p>
<p>What I see is that most projects start out with the ambition of creating very high fidelity physical or in silico models, but along the way lots of assumptions, arbitrary decisions, simplifications are made. Therefore, the efforts invested early on to determine some parameters with extreme accuracy (e.g., wall thickness measurement) often do not pay off, because they may very little practical difference in the fidelity of the end result.</p>
<p>I would recommend to start with the simplest possible model, with approximate generic model parameters, analyze stability of that model, sensitivity to model parameter changes, test its accuracy (by comparing to in vivo results) and improve those parts that you determine to be critical to success.</p>

---
