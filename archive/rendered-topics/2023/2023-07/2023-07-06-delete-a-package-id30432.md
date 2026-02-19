---
topic_id: 30432
title: "Delete A Package"
date: 2023-07-06
url: https://discourse.slicer.org/t/30432
---

# Delete a package

**Topic ID**: 30432
**Date**: 2023-07-06
**URL**: https://discourse.slicer.org/t/delete-a-package/30432

---

## Post #1 by @Kening_Zhang (2023-07-06 14:00 UTC)

<p>Dear developers,<br>
I want to know how to uninstall a package from the slicer’s python, since I have tried many ways but not work.<br>
Best wishes,<br>
Joshua</p>

---

## Post #2 by @pieper (2023-07-06 14:01 UTC)

<p>/path/to/Slicer -m pip uninistall </p>

---

## Post #3 by @lassoan (2023-07-06 14:04 UTC)

<p>You can also use <code>slicer.util.pip_uninstall()</code> function. You may need to restart Slicer after this if the package was loaded when you tried to uninstall it.</p>

---

## Post #4 by @Kening_Zhang (2023-07-06 14:06 UTC)

<p>Sorry, but I tried this way, it says<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a221e824105f7d73b04d4f5e492db12bfea25598.jpeg" data-download-href="/uploads/short-url/n8hZHxofs0jZ1NncZwTq86889ZK.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a221e824105f7d73b04d4f5e492db12bfea25598_2_690x292.jpeg" alt="image" data-base62-sha1="n8hZHxofs0jZ1NncZwTq86889ZK" width="690" height="292" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a221e824105f7d73b04d4f5e492db12bfea25598_2_690x292.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a221e824105f7d73b04d4f5e492db12bfea25598_2_1035x438.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a221e824105f7d73b04d4f5e492db12bfea25598_2_1380x584.jpeg 2x" data-dominant-color="303030"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1790×758 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @pieper (2023-07-06 15:04 UTC)

<p>There was a typo - it should be <code>uninstall</code></p>

---
