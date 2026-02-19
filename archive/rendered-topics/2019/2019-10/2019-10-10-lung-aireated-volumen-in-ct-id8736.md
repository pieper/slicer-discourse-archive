---
topic_id: 8736
title: "Lung Aireated Volumen In Ct"
date: 2019-10-10
url: https://discourse.slicer.org/t/8736
---

# Lung aireated volumen in CT

**Topic ID**: 8736
**Date**: 2019-10-10
**URL**: https://discourse.slicer.org/t/lung-aireated-volumen-in-ct/8736

---

## Post #1 by @titotitoide (2019-10-10 23:12 UTC)

<p>I everyone. First of all thank you very much for this amazing software!!.<br>
I am traying to calculate the lung aereated volumen, I mean, the volumen of the air inside the lung. Now i am making it whit segment editor–&gt;select a thresholg between -1000 and -200HU–&gt;and segment statics–&gt;Volumen.<br>
My questions are:<br>
Is this volumen exactly the air volumen or is the sum of total tissues and a geometrical volumen?<br>
How can I exactly measure the air content inside the lung?<br>
Thank you very much.</p>

---

## Post #2 by @lassoan (2019-10-11 00:35 UTC)

<aside class="quote no-group" data-username="titotitoide" data-post="1" data-topic="8736">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/9de053/48.png" class="avatar"> titotitoide:</div>
<blockquote>
<p>Is this volumen exactly the air volumen or is the sum of total tissues and a geometrical volumen?</p>
</blockquote>
</aside>
<p>The reported segment volume is the volume of the region that you see in the viewers. If you see that the segment only appears where there is air on the CT then you will measure the air volume.</p>

---
