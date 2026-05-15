---
topic_id: 47022
title: "Shift And Wrap Around Voxels Transform"
date: 2026-05-14
url: https://discourse.slicer.org/t/47022
---

# Shift and wrap-around voxels transform

**Topic ID**: 47022
**Date**: 2026-05-14
**URL**: https://discourse.slicer.org/t/shift-and-wrap-around-voxels-transform/47022

---

## Post #1 by @brizolara.lt (2026-05-14 06:43 UTC)

<p>Hi all,</p>
<p>I would like to apply a shift in a definite direction (in my case, X) to the voxel values (not the coordinates) of a volume - keeping, thus, origin, spacing and dimensions intact.</p>
<p>Also, I would like to wrap around the voxels that were shifted outside of the region - i.e., if I’m shifting the voxels to the right, the ones that would fall outside of the region start to appear at the other side.</p>
<p>I am trying to use a GridTransform, but I know I’ll have a problem at the wrap around border. Also, it’s a dense transform and what I need is really a manipulation of voxels.</p>
<p>Maybe a custom transform in C++ is the way? Or is there any solution at the Python level?</p>
<p>I would love to know your thought on this. Thanks in advance,</p>
<p>Tiago</p>

---

## Post #2 by @pieper (2026-05-14 13:24 UTC)

<p>You can do almost anything with fancy numpy indexing.  It can be a challenge to find the right recipe, but you should be able to easily iterate and inspect the results until you get what you want.  Look in the script repository for examples and use LLMs to help with the syntax.</p>

---
