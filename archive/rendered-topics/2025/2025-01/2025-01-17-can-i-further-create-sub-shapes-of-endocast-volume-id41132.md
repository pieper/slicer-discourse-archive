---
topic_id: 41132
title: "Can I Further Create Sub Shapes Of Endocast Volume"
date: 2025-01-17
url: https://discourse.slicer.org/t/41132
---

# Can I further create sub-shapes of endocast volume?

**Topic ID**: 41132
**Date**: 2025-01-17
**URL**: https://discourse.slicer.org/t/can-i-further-create-sub-shapes-of-endocast-volume/41132

---

## Post #1 by @PitaChib (2025-01-17 18:14 UTC)

<p>I have a bunch of micro-CT scanned mice skulls that I have thresholded them into skull segmentations.<br>
Then, I used wrap solidify to get the whole endocast volume of the biggest cavity.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fcfd7351676823beaab2dcd54038291a326e4e8e.jpeg" data-download-href="/uploads/short-url/A63kVY7Lcm18MQUNp6kJPnFrZPE.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fcfd7351676823beaab2dcd54038291a326e4e8e_2_562x500.jpeg" alt="image" data-base62-sha1="A63kVY7Lcm18MQUNp6kJPnFrZPE" width="562" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fcfd7351676823beaab2dcd54038291a326e4e8e_2_562x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fcfd7351676823beaab2dcd54038291a326e4e8e_2_843x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/c/fcfd7351676823beaab2dcd54038291a326e4e8e_2_1124x1000.jpeg 2x" data-dominant-color="161C15"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1166×1036 118 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Since I don’t have any wet tissues when I did the scan, I can’t use methods like grow from seeds/fast marching to get regionalization, but I’m wondering if I can place reference points along the endocast to differentiate into different regions.</p>
<p>so far what I’ve figured out is to manually erase and fill different layers using logical operators and masking, or sometimes when wrap solidify failed to fill some parts (like olfactory) and then I go paint fill them out.<br>
I’d like to ask for the brilliant minds here a way that is faster, more reliable (reproducible) to get regions of this endocast segmentation.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4c629b55dd778eb5fd906618f64ea469cee3fde.jpeg" data-download-href="/uploads/short-url/wDPqn7bbSH2jZ3OEhCQL53vA1I2.jpeg?dl=1" title="104954_Unsmoothed" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4c629b55dd778eb5fd906618f64ea469cee3fde_2_638x500.jpeg" alt="104954_Unsmoothed" data-base62-sha1="wDPqn7bbSH2jZ3OEhCQL53vA1I2" width="638" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4c629b55dd778eb5fd906618f64ea469cee3fde_2_638x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4c629b55dd778eb5fd906618f64ea469cee3fde_2_957x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4c629b55dd778eb5fd906618f64ea469cee3fde_2_1276x1000.jpeg 2x" data-dominant-color="EBF1EE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">104954_Unsmoothed</span><span class="informations">1920×1503 93.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
^This is one that’s purely by chance, but I’d like to further split out the cerebellum, etc.</p>
<p>Thanks so much!</p>

---

## Post #2 by @muratmaga (2025-01-17 19:42 UTC)

<p>If you can draw curves to separate regions (olfactory bulb, cerebellum, etc), you can use the Dynamic Modeler to cut them into different regions.</p>
<p>it would probably be faster and easier than doing through Segment Editor tools.</p>

---

## Post #3 by @PitaChib (2025-02-26 05:56 UTC)

<p>this worked, thanks!</p>

---
