# Liver blood vessel segmentation

**Topic ID**: 37555
**Date**: 2024-07-25
**URL**: https://discourse.slicer.org/t/liver-blood-vessel-segmentation/37555

---

## Post #1 by @Matteboo (2024-07-25 09:12 UTC)

<p>Hello everyone,</p>
<p>In my work, I need to segment the liver blood vessel. For some time, I used the “liver vessel” task in total segmentator in version 5.4 when it was still using TotalsegmentatorV1. This task is no longer supported and it also has some limitations.</p>
<ul>
<li>It only works on CT scan, not MRI</li>
<li>It only works on human liver (I would also need porcine liver)</li>
</ul>
<p>However, blood  vessel segmentation seems like a task that could be done without AI.<br>
So my question is :<br>
<strong>Is there a known method to segment liver blood vessel in human for CT and/or MRI ?<br>
Do you think that this method will work well in porcine liver?</strong></p>
<p>I found several scientific paper but I don’t know wich one I should follow <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=12" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20"><br>
Any guidance is welcomed</p>

---

## Post #2 by @rfenioux (2024-07-25 11:54 UTC)

<p>If you haven’t already, have a look at the <a href="https://github.com/R-Vessel-X/SlicerRVXLiverSegmentation" rel="noopener nofollow ugc">SlicerRVXLiverSegmentation</a> extension that is dedicated to liver segmentation.</p>

---

## Post #3 by @Matteboo (2024-07-25 12:36 UTC)

<p>Thank you for your quick answer <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
I looked at it but it needs the user to manually place point for the blood vessel segmentation. This is exactly what I’m trying to avoid.<br>
I’m looking for a fully automated way to segment the blood vessel. Also I don’t know if this is relevant but I don’t need the blood vessel tree, I just want to know wich voxel are blood vessel and wich are liver parenchyma.</p>

---
