# How to use observer?

**Topic ID**: 29526
**Date**: 2023-05-18
**URL**: https://discourse.slicer.org/t/how-to-use-observer/29526

---

## Post #1 by @dsa934 (2023-05-18 07:07 UTC)

<p>Operating system: window 10<br>
Slicer version: 5.2.1</p>
<p>Whenever a new node is added to the scene, I know that observer is used to process the function for the added node.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee77ba215786717d2bdd7517e78d0386f1541e14.png" data-download-href="/uploads/short-url/y1A9qpXEloxsenVvnzifO1RKqJ6.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee77ba215786717d2bdd7517e78d0386f1541e14_2_680x499.png" alt="image" data-base62-sha1="y1A9qpXEloxsenVvnzifO1RKqJ6" width="680" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee77ba215786717d2bdd7517e78d0386f1541e14_2_680x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee77ba215786717d2bdd7517e78d0386f1541e14.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee77ba215786717d2bdd7517e78d0386f1541e14.png 2x" data-dominant-color="9FA0A7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">933×686 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
(ref: <em>Stanford</em> bunny)</p>
<p>I would like to implement a function that prevents the currently selected markups point in the Bunny mesh from exceeding the range of the Bunny mesh.</p>
<p>In order to perform the above process, it seems that the markupsNode needs to be accessible every time it is added to secne. Is there a way?</p>
<p>Any ideas how to prevent the markupsNode from going beyond the bounds of the mesh?</p>

---

## Post #2 by @lassoan (2023-05-18 19:14 UTC)

<p>You can add observers to the scene - so that you <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-volume-rendering-automatically-when-a-volume-is-loaded">get a notification when a new node is added</a>; or to a markup node - so that you get a notification when <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-a-notification-if-a-markup-control-point-position-is-modified">points are modified or interaction with a point is finished</a>. Check out <a href="https://slicer.readthedocs.io/en/latest/developer_guide/api.html#tutorials">developer tutorials</a> and examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-a-notification-if-a-markup-control-point-position-is-modified">script repository</a>.</p>

---
