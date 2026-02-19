---
topic_id: 9764
title: "Align Images To The Side"
date: 2020-01-09
url: https://discourse.slicer.org/t/9764
---

# Align images to the side

**Topic ID**: 9764
**Date**: 2020-01-09
**URL**: https://discourse.slicer.org/t/align-images-to-the-side/9764

---

## Post #1 by @jonasteuwen (2020-01-09 20:16 UTC)

<p>For the reading of mammography images there are two views per breast. The straight edge touches the side of the laterality of the breast. However, typically you would like to have the images aligned to this edge (so that the images touch). How can I do this programmatically through the Python API?</p>
<p>Attached an example.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c3b64177b694a90235cd6f980c73dee817dced86.jpeg" data-download-href="/uploads/short-url/rVlArFND0c3660HDp7IKeDxWMAK.jpeg?dl=1" title="Screenshot 2020-01-09 at 20.56.33" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c3b64177b694a90235cd6f980c73dee817dced86_2_690x396.jpeg" alt="Screenshot 2020-01-09 at 20.56.33" data-base62-sha1="rVlArFND0c3660HDp7IKeDxWMAK" width="690" height="396" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c3b64177b694a90235cd6f980c73dee817dced86_2_690x396.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c3b64177b694a90235cd6f980c73dee817dced86_2_1035x594.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c3b64177b694a90235cd6f980c73dee817dced86_2_1380x792.jpeg 2x" data-dominant-color="242422"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2020-01-09 at 20.56.33</span><span class="informations">2878×1652 617 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2020-01-15 02:19 UTC)

<p>You can change what physical location is shown where in a slice view by adjusting SliceToRAS transformation. The current fitting algorithm (that places the slice view center at the volume center) is available <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Logic/vtkMRMLSliceLogic.cxx#L1569-L1637">here</a>. You need to slightly tune this algorithm to shift the image to left/right by half of the difference between the volume’s width and the view’s width.</p>
<p>By the way, the huge empty space that off-centering the images may not look very nice at the end. So, instead of pushing the images to the sides, I would recommend to <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Customize_viewer_layout">specify a custom layout</a> that makes the slice views relatively narrow and tall (e.g., you can place additional views on the left or right from these slice views that you can resize using a splitter).</p>

---

## Post #3 by @jonasteuwen (2020-02-12 10:53 UTC)

<p>Thanks Andras, yes for mammography we would typically have four images next to each other (left right breast in two different views). I’ll try to make it work, and post the result here.</p>

---
