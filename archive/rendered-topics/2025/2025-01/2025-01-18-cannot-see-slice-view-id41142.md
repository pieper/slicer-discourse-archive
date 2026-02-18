# Cannot see slice view

**Topic ID**: 41142
**Date**: 2025-01-18
**URL**: https://discourse.slicer.org/t/cannot-see-slice-view/41142

---

## Post #1 by @coenwang01 (2025-01-18 09:08 UTC)

<p>I want to set three points to form a slice, then cut models with it. Therefore, I referred to <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#set-slice-position-and-orientation-from-3-markups-control-points" rel="noopener nofollow ugc">this</a> script. All the operations I performed are as follows: I dropped 3 markups control points in the scene and copy-paste the code below into the Python console. But can not see slice view.<br>
Is there something I’m doing incorrectly?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d5401b8ae98bd6d0478f49129f93ea2284f3cc1.png" data-download-href="/uploads/short-url/6sZt7HPRJisRffelwpQtTQiocTv.png?dl=1" title="no_slcier" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d5401b8ae98bd6d0478f49129f93ea2284f3cc1_2_690x354.png" alt="no_slcier" data-base62-sha1="6sZt7HPRJisRffelwpQtTQiocTv" width="690" height="354" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d5401b8ae98bd6d0478f49129f93ea2284f3cc1_2_690x354.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d5401b8ae98bd6d0478f49129f93ea2284f3cc1_2_1035x531.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d5401b8ae98bd6d0478f49129f93ea2284f3cc1_2_1380x708.png 2x" data-dominant-color="D8D9ED"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">no_slcier</span><span class="informations">1913×982 68.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2025-01-20 12:17 UTC)

<p>Hi! I noticed that you recently added and deleted some pages, and now seem to be confused about layouts. I suggest you slow down a bit and read about how to use the main functions of Slicer:<br>
<a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#using-slicer" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#using-slicer</a></p>

---

## Post #3 by @lassoan (2025-01-20 14:59 UTC)

<p>You have double-clicked on the 3D view to maximize it. You can double-click the 3D view again to restore.</p>

---

## Post #4 by @coenwang01 (2025-01-21 08:02 UTC)

<p>Sorry Sir, I’ve read the documentation multiple times. I just expressed myself incorrectly. What I meant was that when I run <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#set-slice-position-and-orientation-from-3-markups-control-points" rel="noopener nofollow ugc">this</a> piece of code, I don’t see any changes in the Red Slicer View. I’m not sure where I might have gone wrong.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9459c3feadb4b662cd5cbafd8ab4ea9331b5fcc.png" data-download-href="/uploads/short-url/xhCobyj4ugG1NU4mUsV1fSzwqIc.png?dl=1" title="markups_points" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9459c3feadb4b662cd5cbafd8ab4ea9331b5fcc_2_690x361.png" alt="markups_points" data-base62-sha1="xhCobyj4ugG1NU4mUsV1fSzwqIc" width="690" height="361" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9459c3feadb4b662cd5cbafd8ab4ea9331b5fcc_2_690x361.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9459c3feadb4b662cd5cbafd8ab4ea9331b5fcc_2_1035x541.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9459c3feadb4b662cd5cbafd8ab4ea9331b5fcc_2_1380x722.png 2x" data-dominant-color="E6F4D5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">markups_points</span><span class="informations">1674×878 96.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/961886b7d3951e525cc84d23bbbe40449e823715.jpeg" data-download-href="/uploads/short-url/lpOap1jQPmXhW7Uy5Q7gpO67XBb.jpeg?dl=1" title="Red_Slice_View" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/961886b7d3951e525cc84d23bbbe40449e823715_2_690x356.jpeg" alt="Red_Slice_View" data-base62-sha1="lpOap1jQPmXhW7Uy5Q7gpO67XBb" width="690" height="356" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/961886b7d3951e525cc84d23bbbe40449e823715_2_690x356.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/961886b7d3951e525cc84d23bbbe40449e823715_2_1035x534.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/961886b7d3951e525cc84d23bbbe40449e823715_2_1380x712.jpeg 2x" data-dominant-color="A0A0A6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Red_Slice_View</span><span class="informations">1920×992 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @cpinter (2025-01-21 10:02 UTC)

<p>Thanks for the clarification! What you expect to see in the slice views are the three points? If so, the reason you don’t see them is that the points are not exactly on the slices that you see. They are infinitely small objects, and only visible on the slice they coincide with spatially. If you click a point in 3D, the slice views will jump to the point. Also you have the option to see the projection of the points, it is an advanced option in the Markups module.</p>

---

## Post #6 by @coenwang01 (2025-01-21 13:34 UTC)

<p>Yes, it worked! Thank you very much for your patient explanation.</p>

---
