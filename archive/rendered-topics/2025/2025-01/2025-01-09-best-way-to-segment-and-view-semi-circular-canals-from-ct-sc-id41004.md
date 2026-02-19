---
topic_id: 41004
title: "Best Way To Segment And View Semi Circular Canals From Ct Sc"
date: 2025-01-09
url: https://discourse.slicer.org/t/41004
---

# Best way to segment and view semi-circular canals from CT scan in 3D

**Topic ID**: 41004
**Date**: 2025-01-09
**URL**: https://discourse.slicer.org/t/best-way-to-segment-and-view-semi-circular-canals-from-ct-scan-in-3d/41004

---

## Post #1 by @Holdmybrain (2025-01-09 00:39 UTC)

<p>Hey guys and gals,</p>
<p>I’m a patient with a keen interest in understanding and visualising scans better and have just started learning to use Slicer (on Macosx version 5.2.2).</p>
<p>I’ve been playing around with creating basic renders and just scratching the surface of segmentation but I’d like to try and get a better look at my inner ear (especially the semi-circular canals) somewhat in the position they are within the temporal bone. I feel as though I am way out of my depth with this one. What would be the best way to do this?</p>
<p>Thanks!</p>

---

## Post #2 by @muratmaga (2025-01-09 01:08 UTC)

<p>Welcome to the community.</p>
<aside class="quote no-group" data-username="Holdmybrain" data-post="1" data-topic="41004">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/b5ac83/48.png" class="avatar"> Holdmybrain:</div>
<blockquote>
<p>started learning to use Slicer (on Macosx version 5.2.2).</p>
</blockquote>
</aside>
<p>Please use the latest stable (or even better yet a preview version, which soon will be the new stable). The version you are using is not maintained, and there have been many improvements and bug fixes.</p>
<p>I am not sure what organism you are working with but visibility of the inner ear, cochlea, semi circular canal  (SCC) will highly be dependent on the resolution of your data. In mouse, we can’t even see SCC at 35 micron resolution. And at 18 micron they will be only couple voxels wide. So you need to have really high resolution to have high quality segmentation/rendering of internal aspects of inner ear.</p>
<p>(so if you are working with medical CT scan, you may not be able to see SCC), but you should be able to visualize cochlea.</p>

---

## Post #3 by @Holdmybrain (2025-01-09 07:10 UTC)

<p>Thanks for the welcome and response!</p>
<p>5.2.2 is unfortunately the latest version I’m able to use on my current operating system (10.15) due to a hardware issue preventing me from upgrading my OS (non OEM hdd installed) but will hopefully be able to have that fixed soon.</p>
<p>The organism I’m working with is a human, these are my images. I’ve had a dehiscence identfied on the left superior canal so I’d like to get a look at it in context, including with the part of the temporal-bone that forms the “roof” above it.</p>
<p>I can appreciate what you’re saying about the issues with resolution for these delicate structures. How can I determine what the resolution of my images is?</p>
<p>Thanks</p>

---

## Post #4 by @pieper (2025-01-09 14:07 UTC)

<p>To determine the resolution of your images, open the Volumes module and the Volume Information tab.  Comparing the spacing values to the size of the structures you want to see will give you a rough idea of how much detail you can expect to see.</p>

---

## Post #5 by @lanala (2025-05-30 14:36 UTC)

<p>Hello,</p>
<p>I have a similar interest on this. I would like to segment the inner ear CT and MRI (if possible) scans of 4 years old kid. I am not a radiologist, so I would appreciate any help from someone interested in inner ear segmentation.</p>
<p>Thanks in advance!</p>

---

## Post #6 by @nagy.attila (2025-06-02 10:59 UTC)

<p>Hi,</p>
<p>I have some experience with segmenting inner ears.<br>
Actually, depending on the resolution of the scan, it doesn’t take too much to do; if you have a nice CT (somewhere in the 0.3mm x 0.3mm x 0.3mm resolution range), using simple thresholding can do the trick pretty nicely.</p>
<p>Ping me if you need more help or details!<br>
Attila</p>

---
