---
topic_id: 42269
title: "Getting Measures Off Plane Or Roi Markups"
date: 2025-03-23
url: https://discourse.slicer.org/t/42269
---

# Getting measures off plane or ROI markups

**Topic ID**: 42269
**Date**: 2025-03-23
**URL**: https://discourse.slicer.org/t/getting-measures-off-plane-or-roi-markups/42269

---

## Post #1 by @Jordan_T (2025-03-23 20:43 UTC)

<p>Hi!</p>
<p>I am fairly new to Slicer and I imagine there is an easy solution to this, but I cannot find it.</p>
<p>I am trying to measure length and width of a condyle, but because the condyle bows out in places just getting the distance between points placed on the extreme edges does not work.</p>
<p>I have found that I can create an ROI that reasonably bounds the object- I can see in the ROI settings that the box bounds are really close to my caliper measurements. But the corners of the box are not points I can save, and I cannot figure out a way to save the settings in a way I can use.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d21c7417d28ec087fdee2f88eff73dc5b05fd13a.jpeg" data-download-href="/uploads/short-url/tYJegycaGzNu8yUHPZ8z7GGMvDI.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d21c7417d28ec087fdee2f88eff73dc5b05fd13a_2_341x500.jpeg" alt="image" data-base62-sha1="tYJegycaGzNu8yUHPZ8z7GGMvDI" width="341" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d21c7417d28ec087fdee2f88eff73dc5b05fd13a_2_341x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d21c7417d28ec087fdee2f88eff73dc5b05fd13a.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d21c7417d28ec087fdee2f88eff73dc5b05fd13a.jpeg 2x" data-dominant-color="91745C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">493×722 74 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This information, or something similar:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/0440060badd03bba921f146c262d21c7eba43541.png" data-download-href="/uploads/short-url/BB4WVuLuNUCeWAzzTURP3qJzj3.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/0440060badd03bba921f146c262d21c7eba43541.png" alt="image" data-base62-sha1="BB4WVuLuNUCeWAzzTURP3qJzj3" width="550" height="244"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">550×244 8.72 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Context: I only have ply files, no DICOM so I cannot just go to a slice. I need to get these outer bounds measures because I am trying to replicate what i get with calipers, as some of my data was taken by hand and I need to have comparable data. I have a lot of these to do (+80), so I would like to find some way to save the settings instead of having to manually record each of these numbers.</p>
<p>Any help would be greatly appreciated!</p>

---

## Post #2 by @pieper (2025-03-24 13:12 UTC)

<p>I’m not sure if that’s exposed easily, but here’s an example of going the other direction, creating an ROI from known geometry, so you would just need to use the same logic to calculate the metrics you need.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#markups-roi">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#markups-roi</a></p>

---
