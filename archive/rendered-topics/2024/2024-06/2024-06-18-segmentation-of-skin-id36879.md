---
topic_id: 36879
title: "Segmentation Of Skin"
date: 2024-06-18
url: https://discourse.slicer.org/t/36879
---

# Segmentation of skin

**Topic ID**: 36879
**Date**: 2024-06-18
**URL**: https://discourse.slicer.org/t/segmentation-of-skin/36879

---

## Post #1 by @sanjivani (2024-06-18 15:04 UTC)

<p>As per the instructions in the FAQ, I first chose 2 segments and brushed the inner bud with segment 1 and the outer sapace with segment 2, followed by growing from the seeds &gt; initializing, and viewing in 3D.</p>
<p>afterwards i chose the option segmentations and unmarked the option called slice fill and in all 3 viwes as we see in image now only the outer surface is selected but then while viewing or exporting the file in STL the model in not apearing in hollow which is leading the confusion that how can I only extract skin membrane without any solid fill in</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69f254c611d419ac25bdad4a9914a3fa5c90bf7e.jpeg" data-download-href="/uploads/short-url/f7fkf0HgO9FElEKQOdU23n7oFCm.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69f254c611d419ac25bdad4a9914a3fa5c90bf7e_2_690x384.jpeg" alt="image" data-base62-sha1="f7fkf0HgO9FElEKQOdU23n7oFCm" width="690" height="384" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69f254c611d419ac25bdad4a9914a3fa5c90bf7e_2_690x384.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69f254c611d419ac25bdad4a9914a3fa5c90bf7e_2_1035x576.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69f254c611d419ac25bdad4a9914a3fa5c90bf7e_2_1380x768.jpeg 2x" data-dominant-color="75777C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1071 127 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you for your time</p>

---

## Post #2 by @lassoan (2024-06-18 17:32 UTC)

<p>STL files can only store surface meshes, which specify solid 3D regions by their outer surface.</p>
<aside class="quote no-group" data-username="sanjivani" data-post="1" data-topic="36879">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/d26b3c/48.png" class="avatar"> sanjivani:</div>
<blockquote>
<p>while viewing or exporting the file in STL the model in not apearing in hollow</p>
</blockquote>
</aside>
<p>It is actually not hollow, it is still a closed surface, which specifies a solid object. It is up to the application to decide how this surface is visualized. It may be a limitation or an intentional decision of that software you used to only show the boundary and not fill the object inside.</p>
<p>If you cut into the surface then the cut surface may be capped (keeping the surface closed and maintaining the object solid) or left uncapped (in this case the surface does not specify a solid object anymore).</p>

---

## Post #3 by @sanjivani (2024-06-19 11:11 UTC)

<p>Then how can I get the mesh of the only outer surface (skin) and no closing surfaces?</p>

---

## Post #4 by @lassoan (2024-06-19 20:50 UTC)

<p>You can use the <code>Hollow</code> effect in Segment Editor to get the outer surface as a thick shell.</p>

---
