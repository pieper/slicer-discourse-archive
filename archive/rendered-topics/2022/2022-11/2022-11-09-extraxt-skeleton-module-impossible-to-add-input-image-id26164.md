# Extraxt Skeleton Module: impossible to add input image

**Topic ID**: 26164
**Date**: 2022-11-09
**URL**: https://discourse.slicer.org/t/extraxt-skeleton-module-impossible-to-add-input-image/26164

---

## Post #1 by @gboels (2022-11-09 15:11 UTC)

<p>Operating system: windows<br>
Slicer version: 5.0.3<br>
Expected behavior: Add an input image to extract a skeleton from it.<br>
Actual behavior: I can’t select an image from my computer when clicking on “SelectLabelMapVolume”. Why?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b7c3215462da1ae31db6fa5557582e3d9e152968.jpeg" data-download-href="/uploads/short-url/qdDrnwI3WafGWt8irDjgSqKRk6I.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b7c3215462da1ae31db6fa5557582e3d9e152968_2_690x367.jpeg" alt="image" data-base62-sha1="qdDrnwI3WafGWt8irDjgSqKRk6I" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b7c3215462da1ae31db6fa5557582e3d9e152968_2_690x367.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b7c3215462da1ae31db6fa5557582e3d9e152968_2_1035x550.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b7c3215462da1ae31db6fa5557582e3d9e152968.jpeg 2x" data-dominant-color="5F6077"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1057×563 99.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @muratmaga (2022-11-10 03:20 UTC)

<p>From the screensgot, it is not clear whether that’s a segmentation or a 3d model. Either way, for to module work you need to convert them to a label map.</p>
<p>İf it is segmentation, right click on it and choose export label map. İf it is a 3d model, first right click and select convert “segmentatition” and once it is converted to a segmentatition object, repeat the previous step of exporting to a label map.</p>

---
