# Conditional island removal?

**Topic ID**: 16570
**Date**: 2021-03-16
**URL**: https://discourse.slicer.org/t/conditional-island-removal/16570

---

## Post #1 by @hherhold (2021-03-16 13:02 UTC)

<p>I would like to be able to remove small islands (under a certain threshold) <em>if</em> they are a certain distance away from other islands. I have segmentations of some very thin insect tracheae that are basically “archipelagoes”, long stretches of very small islands, but also in the background there are single small islands that are far away from everything else (noise, basically). I’d like to remove the isolated islands but keep the archipelagoes, so I’m thinking I could check for island size, then see if anything is nearby, and if not, delete it.</p>
<p>Does this sound doable? I’ve taken a brief look at vtkITKIslandMath and it seems like there are a lot of possibilities with ITK filters, but I’m not sure how feasible this would be.</p>
<p>Thanks!</p>
<p>-Hollister</p>

---

## Post #2 by @lassoan (2021-03-16 16:07 UTC)

<p>You can create a mask segment that prevents deleting your archipelagoes. The mask segment can be created by applying Margin effect → Grow to a segment that contains all the segments, followed by Island effect → Keep selected island.</p>

---

## Post #3 by @hherhold (2021-03-16 21:32 UTC)

<p>I’ll give this a try. Thanks!!!</p>

---
