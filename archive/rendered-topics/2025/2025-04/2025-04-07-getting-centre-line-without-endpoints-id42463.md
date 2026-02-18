# Getting centre line without endpoints 

**Topic ID**: 42463
**Date**: 2025-04-07
**URL**: https://discourse.slicer.org/t/getting-centre-line-without-endpoints/42463

---

## Post #1 by @desireeb (2025-04-07 04:01 UTC)

<p>Hello!<br>
I am trying to generate centre line on my segmentation but without using endpoints. I am working on bony semi-circular structures, connected in the middle so there is not origin and end.<br>
I have specified to the system: no endpoints but keep asking me for two at least. (If I add multiple endpoints on the structure the result is not good either)<br>
Any ideas or suggestion?<br>
Many thanks!</p>

---

## Post #2 by @lassoan (2025-04-07 04:05 UTC)

<p>The “centerline” detection algorithm provides a centerline tree between specified endpoints. If you don’t know the endpoints then you can click the automatic endpoint detection, which should provide you the endpoints within seconds.</p>
<p>If your topology is not a tree (for example, it contains a loop) then you can use the “network” extraction algorithm. That does not require endpoints.</p>

---

## Post #3 by @desireeb (2025-04-07 08:14 UTC)

<p>Many thanks Andras! That works! It looks awesome actually!<br>
I managed to identify my initial mistake, thank you veeeeery much!!!</p>

---

## Post #4 by @desireeb (2025-04-07 12:45 UTC)

<p>Hello again!<br>
I have another question, related to previous one.<br>
I need to get the centre line from two separate structures which are on the same segmentation.<br>
When I set up the centre line, works only for one of the two structures.<br>
Many thanks!</p>

---
