---
topic_id: 2950
title: "Volume Rendering Crop Roi Inverse"
date: 2018-05-28
url: https://discourse.slicer.org/t/2950
---

# Volume rendering crop ROI - inverse?

**Topic ID**: 2950
**Date**: 2018-05-28
**URL**: https://discourse.slicer.org/t/volume-rendering-crop-roi-inverse/2950

---

## Post #1 by @hherhold (2018-05-28 13:58 UTC)

<p>Hey guys,</p>
<p>Right now, the volume rendering crop ROI excludes everything outside the ROI. Does VTK support the opposite? Meaning, exclude everything INSIDE the ROI? This would be useful for certain kinds of cutaways. I know it’s possible to do this kind of thing with the crop volume module and other methods, but those aren’t interactive (I think) like the volume rendering ROI crop is.</p>
<p>If VTK supports this (or there’s another way to do it), I’m willing to look into how to do it (probably with more than a few questions along the way).</p>
<p>Any thoughts?</p>
<p>Thanks tons!</p>
<p>-Hollister</p>

---

## Post #2 by @lassoan (2018-05-28 14:18 UTC)

<p>Yes, there is a flag that switches between inside/outside. <a class="mention" href="/u/cpinter">@cpinter</a> has some recent experience with this, he can probably comment on where this could be added.</p>
<p>At the upcoming project week in Gran Canaria we plan to look into using custom shaders in volume renderer, which will allow more sophisticated clipping (sphere-shaped cutouts, etc).</p>

---

## Post #3 by @hherhold (2018-05-28 15:14 UTC)

<p>Very cool! Thanks!</p>
<p>Hope you all have a good time!</p>
<p>-Hollister</p>

---
