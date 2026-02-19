---
topic_id: 23848
title: "Show The Full Volume And Not Only Slices"
date: 2022-06-13
url: https://discourse.slicer.org/t/23848
---

# Show the full volume and not only slices

**Topic ID**: 23848
**Date**: 2022-06-13
**URL**: https://discourse.slicer.org/t/show-the-full-volume-and-not-only-slices/23848

---

## Post #1 by @hmaguilera (2022-06-13 08:27 UTC)

<p>Hi,<br>
I was wondering if it is possible to show the entire volume cone, and not only the three slices as shown in the bottom right corner.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2887958dd6a264f6efa7329904537ff21a3a040.jpeg" data-download-href="/uploads/short-url/nbPK9BNViW7RgsCFw9paFZVNnC8.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a2887958dd6a264f6efa7329904537ff21a3a040_2_690x372.jpeg" alt="image" data-base62-sha1="nbPK9BNViW7RgsCFw9paFZVNnC8" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a2887958dd6a264f6efa7329904537ff21a3a040_2_690x372.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a2887958dd6a264f6efa7329904537ff21a3a040_2_1035x558.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a2887958dd6a264f6efa7329904537ff21a3a040_2_1380x744.jpeg 2x" data-dominant-color="3B3B48"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1036 73.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @mau_igna_06 (2022-06-13 09:38 UTC)

<p>Yes. You first need to reconstruct the 3D volume from your sequence of 2D slices and then you need to do volume rendering of it. Probably you would need ultrasound that is tracked.</p>
<p>Maybe someone with more expertise on that can help</p>

---

## Post #3 by @lassoan (2022-06-13 13:39 UTC)

<p>You can use <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumerendering.html#display-a-ct-or-mri-volume">volume rendering</a> to display 3D/4D ultrasound.</p>
<p>We have created a specialized echo volume renderer volume that can produce similar looking brown-to-blue distance based coloring as you can see on the ultrasound cart, but we haven’t made it public yet.</p>
<p>                    <a href="https://pbs.twimg.com/media/Ed_SnQiWAAYcxir?format=png&amp;name=medium" target="_blank" rel="noopener" class="onebox">
            <img src="https://pbs.twimg.com/media/Ed_SnQiWAAYcxir?format=png&amp;name=medium" width="667" height="500">
          </a>

</p>

---
