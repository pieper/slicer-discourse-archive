# How to achiewved the result as is shown in the pic

**Topic ID**: 30036
**Date**: 2023-06-14
**URL**: https://discourse.slicer.org/t/how-to-achiewved-the-result-as-is-shown-in-the-pic/30036

---

## Post #1 by @slicer365 (2023-06-14 13:31 UTC)

<p>This is achieved by other software by adjusting the distance between layers to display different tissue images on multi-planar reconstruction. Can slicer achieve this?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0c1db34166a500cab82a281579d5384ef2b987d.jpeg" data-download-href="/uploads/short-url/tMKEeGI3n0VGXiCq93t8gMXK6lf.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0c1db34166a500cab82a281579d5384ef2b987d.jpeg" alt="image" data-base62-sha1="tMKEeGI3n0VGXiCq93t8gMXK6lf" width="517" height="301" data-dominant-color="A4A5A6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">878×512 39.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2023-06-15 11:52 UTC)

<p>Looks like a MIP of a slab.  You can try this code:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository/volumes.html#thick-slab-reconstruction-and-maximum-minimum-intensity-volume-projections" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository/volumes.html#thick-slab-reconstruction-and-maximum-minimum-intensity-volume-projections</a></p>

---

## Post #3 by @lassoan (2023-06-16 14:09 UTC)

<p>If you want to see maximum intensity projection in the 3D view then you can use Volume rendering module. You can enable projection in Advanced → Techniques → Technique → Maximum intensity projection. You can use the crop function to limit the projection to a thick slab instead of the entire volume.</p>

---
