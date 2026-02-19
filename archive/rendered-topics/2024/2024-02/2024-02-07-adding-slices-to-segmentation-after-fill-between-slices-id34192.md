---
topic_id: 34192
title: "Adding Slices To Segmentation After Fill Between Slices"
date: 2024-02-07
url: https://discourse.slicer.org/t/34192
---

# Adding slices to segmentation after fill between slices

**Topic ID**: 34192
**Date**: 2024-02-07
**URL**: https://discourse.slicer.org/t/adding-slices-to-segmentation-after-fill-between-slices/34192

---

## Post #1 by @jfkamhi (2024-02-07 18:26 UTC)

<p>Hi, I’m having a problem editing a segmentation after using the fill between slices tool. I am able to edit slices using the paint function that were included in the segmentation when fill between slices was implemented (e.g. slices 3-7), but I am not able to edit any additional slices outside of this to the segmentation (e.g. adding slice 2 or 8 to the segmentation).  Does anyone know a way to do this?  Thank you!</p>

---

## Post #2 by @muratmaga (2024-02-07 19:02 UTC)

<p>I am not sure i understood the question. Can you provide a screenshot of your problem?<br>
Did you click the Apply to finalize the segmentation (after you clicked initialize)</p>

---

## Post #3 by @jfkamhi (2024-02-16 16:01 UTC)

<p>Thanks for responding to this!  I played around with this more and it seems like a problem just in this image.  Even not initializing in another image doesn’t result in this problem, so I’m not sure what is going on here.</p>
<p>I’ll try to clarify the problem: If I use the paint function to edit segments and then use “fill between slices,” it will fill between the slices as expected.  However, if I try to paint a slice outside of the original slices that were in the segment when I implemented “fill between slices” it will not add that to the segment, it will just automatically delete it.  The only work around I can think of now is just to re-trace the entire segment so that the additional slices can be included, but if anyone has another idea, I’d greatly appreciate it!  Thank you!</p>

---
