---
topic_id: 35623
title: "Unable To Compute The Ferret Diameter On Segmentation From T"
date: 2024-04-19
url: https://discourse.slicer.org/t/35623
---

# Unable to compute the ferret diameter on segmentation from totalsegmentator

**Topic ID**: 35623
**Date**: 2024-04-19
**URL**: https://discourse.slicer.org/t/unable-to-compute-the-ferret-diameter-on-segmentation-from-totalsegmentator/35623

---

## Post #1 by @Matteboo (2024-04-19 14:32 UTC)

<p>Hello,</p>
<p>I did the following step :</p>
<ol>
<li>
<p>Load “CT Chest” from the sample data module</p>
</li>
<li>
<p>Segment it using totalsegmentator (task total, fast mode activated)</p>
</li>
<li>
<p>Compute the statistic using the “Segment Statistics” module, it’s a success</p>
</li>
<li>
<p>Enable the statistics “Ferret Diameter mm” in Advanced &gt;Labelmap Statistics. Slicer runs indefinitely without raising an error.</p>
</li>
</ol>
<p>If I create my segmentation by right-clicking the volume and doing " Segment this …", I can calculate the ferret diameter</p>
<p>I tried on version 5.6.0 and 5.6.2 and I got the error in both cases<br>
If it’s a known issue and a fix is already available, I would gladly use it.</p>

---

## Post #2 by @pieper (2024-04-19 14:38 UTC)

<p>It may just take a long time to compute for a complex segment.</p>

---

## Post #3 by @Matteboo (2024-04-19 15:04 UTC)

<p>You’re right, <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=12" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20"><br>
I did a test using only the “spleen” segment from totalsegmentator and the computation completed</p>
<p>I’m surprised that the computation time increases that much with the volume of the segment.</p>
<p>Anyway, thank you so much and sorry for bothering you with such a simple question <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=12" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @pieper (2024-04-19 15:15 UTC)

<p>No problem - glad it’s working for you <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---
