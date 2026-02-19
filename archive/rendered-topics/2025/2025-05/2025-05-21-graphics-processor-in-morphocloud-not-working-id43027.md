---
topic_id: 43027
title: "Graphics Processor In Morphocloud Not Working"
date: 2025-05-21
url: https://discourse.slicer.org/t/43027
---

# Graphics processor in MorphoCloud not working?

**Topic ID**: 43027
**Date**: 2025-05-21
**URL**: https://discourse.slicer.org/t/graphics-processor-in-morphocloud-not-working/43027

---

## Post #1 by @Dave_Matthews (2025-05-21 20:11 UTC)

<p>I recently initiated a MorphoCloud instance (Instance-277, g3.xl) and it was working great this morning.</p>
<p>However, this afternoon I unshelved it and tried to load in the same dataset I was working with earlier. This time the volume rendering 3D view is almost completely non-functional due to extreme lag. I switched to CPU graphics and it worked significantly better, but “show 3D” in the segment editor tab is still unusably slow.</p>
<p>So I’m fairly sure that for some reason the graphics processor isn’t working. I’m just wondering if there is an error, or if this is due to heavy resource usage by other people on the system?</p>
<p>Thanks for any help!</p>

---

## Post #2 by @muratmaga (2025-05-21 20:17 UTC)

<p>You might have landed in an instance with a problematic gpu. Open a terminal and type nvidia-smi and see if any error is reported.</p>

---

## Post #3 by @Dave_Matthews (2025-05-21 20:22 UTC)

<p>Thanks for responding Murat!</p>
<p>You’re right on, it says “no devices were found”. If I shelve it and then unshelve it will I end up in a different instance?</p>

---
