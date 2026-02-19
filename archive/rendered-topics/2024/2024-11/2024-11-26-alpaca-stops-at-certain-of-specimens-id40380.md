---
topic_id: 40380
title: "Alpaca Stops At Certain Of Specimens"
date: 2024-11-26
url: https://discourse.slicer.org/t/40380
---

# ALPACA stops at certain # of specimens

**Topic ID**: 40380
**Date**: 2024-11-26
**URL**: https://discourse.slicer.org/t/alpaca-stops-at-certain-of-specimens/40380

---

## Post #1 by @stineblom (2024-11-26 13:14 UTC)

<p>Hi all!<br>
I hope you can help me - I am using ALPACA to produce semilandmark datasets for scapulae of 6 species, but I am experiencing a weird problem. All scapulae are mesh .ply and prepared in the same way. The first time I ran ALPACA, I had 80-something scapulae, where it only gave me landmarks for 75. At that point, I saw it was one species that hadn’t been completely included and I thought it was a resolution problem because those meshes are of lower resolution than the others. But now I have 109 scapulae, including a new species with great resolution, and it still only provides me with the same 75 landmark sets - same as last time. So, it doesn’t have anything to do with the resolution (I checked, and it landmarks the meshes fine), rather it’s almost like it’s ignoring the newly added scapulae (from after I made the template)? It does not seem to ‘crash’, it seems to ‘finish’. I have tried to look around for the limitations of ALPACA, but it doesn’t say anywhere that it should have a specimen limit.<br>
I am crossing my fingers someone else have experience with this. Thank you!</p>

---

## Post #2 by @muratmaga (2024-11-26 15:28 UTC)

<p>Can you provide the log.file?</p>
<p>Can you share a few those models that alpaca doesnt seem to work along with your template model and its landmarks?</p>

---

## Post #3 by @muratmaga (2024-11-28 17:19 UTC)

<p>Thanks for sharing your models. The issue is the scale of the data is off (very very small), causing the point sampling to fail.</p>
<p>If you can go back to wherever this data originated and correct the scale that would be great. If that is not possible you can create a big scaling transform in Slicer by setting the first three diagonals to something like 1000 and then applying it to these data (and any other derivative data, e.g. landmarks) and trying this again.</p>
<p>I will open an issue to track this, but for time being if you scale them, things should work out.</p>

---
