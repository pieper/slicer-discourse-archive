---
topic_id: 44369
title: "Joint Smooth In 2D"
date: 2025-09-05
url: https://discourse.slicer.org/t/44369
---

# Joint smooth in 2d

**Topic ID**: 44369
**Date**: 2025-09-05
**URL**: https://discourse.slicer.org/t/joint-smooth-in-2d/44369

---

## Post #1 by @sulli419 (2025-09-05 21:06 UTC)

<p>Hi,</p>
<p>The joint smoothening tool historically works very well for me, but now I have a series of atlas segments that are very poorly sampled in Z.  The X Y edges are also rather rough, and so I want to improve these by upsampling the segmentations and then joint smoothen. I know how to do this part, and it has worked well in the past with higher Z sampled images, but now the abrupt jumps in Z make the joint smoothen tool do odd things.  Is there a simple set of commands to run this tool in 2D, i.e., in each plane of Z?</p>
<p>p.s., One hack I did was to inflate the volume with replicate images (e.g, z x 10), which improved the outcome, but this seems like waste of resources and it still misbehaved for this odd use case.</p>
<p>Thanks,<br>
Steve</p>

---
