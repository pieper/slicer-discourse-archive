---
topic_id: 28899
title: "Anyone Know How To Coregistering Four Images"
date: 2023-04-14
url: https://discourse.slicer.org/t/28899
---

# Anyone Know How to coregistering four images

**Topic ID**: 28899
**Date**: 2023-04-14
**URL**: https://discourse.slicer.org/t/anyone-know-how-to-coregistering-four-images/28899

---

## Post #1 by @akmal871026 (2023-04-14 04:03 UTC)

<p>Anyone know, how to do coregistering using four images.</p>
<p>That I want to know is like the metric alignment for four images,</p>

---

## Post #2 by @ebrahim (2023-04-14 14:19 UTC)

<p>You could pick one image and register the other 3 images to it.</p>
<p>One way to make the choice less arbitrary could be to compute all <code>4 choose 2</code> pairwise registrations and choose whichever of the images has smallest mean deformation needed to align it to the other three images.</p>
<p>The other approach is atlas construction, but I guess four images is too few to do that.</p>

---
