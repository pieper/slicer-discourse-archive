---
topic_id: 16161
title: "Merging Two Modules"
date: 2021-02-23
url: https://discourse.slicer.org/t/16161
---

# Merging two modules

**Topic ID**: 16161
**Date**: 2021-02-23
**URL**: https://discourse.slicer.org/t/merging-two-modules/16161

---

## Post #1 by @will_kim (2021-02-23 15:58 UTC)

<p>Hi rather new to Slicer and have two general questions. I have two scripted modules that share common information. So is there a way I can load this information for one module and it gets automatically uploads to the other script?</p>
<p>Also, does Slicer have an extension or a method to measure the radius and give out the center-coordinates of the volume?</p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2021-02-23 16:21 UTC)

<aside class="quote no-group" data-username="will_kim" data-post="1" data-topic="16161">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/779978/48.png" class="avatar"> will_kim:</div>
<blockquote>
<p>Hi rather new to Slicer and have two general questions. I have two scripted modules that share common information. So is there a way I can load this information for one module and it gets automatically uploads to the other script?</p>
</blockquote>
</aside>
<p>In general, modules share all data via the MRML scene and communicate via node modified events. You can also call another module’s logic objects, which is useful when one module uses algorithms implemented in the other. See more details in this tutorial: <a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx?raw=true">https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx?raw=true</a></p>
<aside class="quote no-group" data-username="will_kim" data-post="1" data-topic="16161">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/779978/48.png" class="avatar"> will_kim:</div>
<blockquote>
<p>Also, does Slicer have an extension or a method to measure the radius and give out the center-coordinates of the volume?</p>
</blockquote>
</aside>
<p>Yes, this is available in Segment Statistics module. See details here: <a href="https://discourse.slicer.org/t/new-segment-statistics-oriented-bounding-box-diameter-and-more/10203" class="inline-onebox">New Segment Statistics: Oriented Bounding Box, Diameter and More</a></p>

---

## Post #3 by @will_kim (2021-02-24 05:12 UTC)

<p>Great, understood. Thank you!</p>

---
