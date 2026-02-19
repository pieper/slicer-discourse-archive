---
topic_id: 8672
title: "Images Registration"
date: 2019-10-04
url: https://discourse.slicer.org/t/8672
---

# Images registration

**Topic ID**: 8672
**Date**: 2019-10-04
**URL**: https://discourse.slicer.org/t/images-registration/8672

---

## Post #1 by @zahiraabdala (2019-10-04 14:21 UTC)

<p>Hi all, i´m traing to register two images but there have different sizes.<br>
An image has a size of 256x256x256 and the other one has 256x256x89. Someone can help me?<br>
thank a lot</p>

---

## Post #2 by @pieper (2019-10-04 14:36 UTC)

<p>As long as the <a href="https://www.slicer.org/wiki/Coordinate_systems" rel="nofollow noopener">image geometry</a> is correct the shouldn’t matter much, within reason.  Did you try?</p>

---

## Post #3 by @Prashant_Pandey (2019-10-04 16:19 UTC)

<p>Try the elastix registration module, it will resample your moving image to the fixed image domain.</p>

---
