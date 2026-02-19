---
topic_id: 33183
title: "How To Add Some Holes By Script"
date: 2023-12-03
url: https://discourse.slicer.org/t/33183
---

# How to add some holes by script?

**Topic ID**: 33183
**Date**: 2023-12-03
**URL**: https://discourse.slicer.org/t/how-to-add-some-holes-by-script/33183

---

## Post #1 by @slicer365 (2023-12-03 01:23 UTC)

<p>When I am splitting the skin, I want to add some holes on the surface of the skin model. This can be achieved using the eraser tool. Currently, I have placed some points on the surface of the skin model, and I want to write a script that obtains the RAS coordinates of each point and then iteratively creates holes using the eraser tool. How can I accomplish this? I am able to obtain the current segmentation node and markups node."<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/17480983da5249b642bc81d59a03c2dd7724fa2b.png" data-download-href="/uploads/short-url/3jXjSVDsWrsUHDOeq5cNULBHGgb.png?dl=1" title="44" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/17480983da5249b642bc81d59a03c2dd7724fa2b_2_690x343.png" alt="44" data-base62-sha1="3jXjSVDsWrsUHDOeq5cNULBHGgb" width="690" height="343" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/17480983da5249b642bc81d59a03c2dd7724fa2b_2_690x343.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/17480983da5249b642bc81d59a03c2dd7724fa2b_2_1035x514.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/17480983da5249b642bc81d59a03c2dd7724fa2b_2_1380x686.png 2x" data-dominant-color="A7B7B5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">44</span><span class="informations">1914×954 301 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2023-12-03 02:02 UTC)

<p>You can add a small sphere-shaped segment at each point as shown in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-histogram-of-a-segmented-region">this example</a>. You can then use Logical operators effect to subtract these sphere segments from the skull cap segment.</p>

---
