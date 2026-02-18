# Separate vessels from bones

**Topic ID**: 15703
**Date**: 2021-01-27
**URL**: https://discourse.slicer.org/t/separate-vessels-from-bones/15703

---

## Post #1 by @Sevilay_Karasu (2021-01-27 21:11 UTC)

<p>Dear sir,<br>
when volume rendering is performed on the ct angiography data, arteries is obtained with bone. ı want to see just arteries from ct angiography data, without bone.but ı want to make a transparency on the bone. is it possible? how to make transparency on bone<br>
thanks in advance.</p>

---

## Post #2 by @lassoan (2021-01-27 21:15 UTC)

<p>This is a commonly needed task and you should be easily solve this (for reasonably good quality images) by segmenting the vessels as described in <a href="https://lassoan.github.io/SlicerSegmentationRecipes/AortaMaskedGrowFromSeeds/">this recipe</a>.</p>
<p>You can then for example show the vasculature as segmentation (as solid structure) and show surrounding anatomy using volume rendering.</p>

---

## Post #3 by @Sevilay_Karasu (2021-01-27 21:26 UTC)

<p>thanks a million. ı want to ask one more thing. ı loaded a picture from an article -<a href="https://pubmed.ncbi.nlm.nih.gov/22160178/" class="inline-onebox" rel="noopener nofollow ugc">Anatomical relationship between cranial surface landmarks and venous sinus in posterior cranial fossa using CT angiography - PubMed</a>. I wonder that is it possible to make the same thing for arteries. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff28ea9de188308f97c9b76b831b488410c50229.jpeg" data-download-href="/uploads/short-url/ApfpVb4hkYT73nXL5Qcy1EtsYoV.jpeg?dl=1" title="Ekran Resmi 2021-01-28 00.19.36" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ff28ea9de188308f97c9b76b831b488410c50229_2_690x321.jpeg" alt="Ekran Resmi 2021-01-28 00.19.36" data-base62-sha1="ApfpVb4hkYT73nXL5Qcy1EtsYoV" width="690" height="321" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ff28ea9de188308f97c9b76b831b488410c50229_2_690x321.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff28ea9de188308f97c9b76b831b488410c50229.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff28ea9de188308f97c9b76b831b488410c50229.jpeg 2x" data-dominant-color="A79B8E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Ekran Resmi 2021-01-28 00.19.36</span><span class="informations">902×420 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2021-01-27 22:31 UTC)

<p>The left image is created by segmenting the vessels and then using that to mask the volume (in Slicer: Mask volume effect in Segment Editor; provided by SegmentEditorExtraEffects extension).</p>
<p>The right image seems to be the same as the left, with the cranium overlaid. This can be achieved by:</p>
<ol>
<li>segment the cranium and then use that to mask the volume and render it along the vessel volume using multi-volume rendering</li>
</ol>
<p>Example with aorta and bones:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb96097803a10bea5c5463561fdea2e518bac4bb.jpeg" data-download-href="/uploads/short-url/qLsJRy5BjX5VKhECwOpAqiGcDnd.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bb96097803a10bea5c5463561fdea2e518bac4bb_2_477x500.jpeg" alt="image" data-base62-sha1="qLsJRy5BjX5VKhECwOpAqiGcDnd" width="477" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bb96097803a10bea5c5463561fdea2e518bac4bb_2_477x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bb96097803a10bea5c5463561fdea2e518bac4bb_2_715x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bb96097803a10bea5c5463561fdea2e518bac4bb_2_954x1000.jpeg 2x" data-dominant-color="453C3B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1169×1224 267 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<ol start="2">
<li>render the cranium as segmentation, setting its 3D opacity to &lt;1</li>
</ol>
<p>Example with aorta and soft tissues surface:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1cfabda1bfc943c1f4b1ce5af3b85c9e862e8084.jpeg" data-download-href="/uploads/short-url/48mzSIrjITTHo8vdToi5d4QbCMA.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1cfabda1bfc943c1f4b1ce5af3b85c9e862e8084_2_480x500.jpeg" alt="image" data-base62-sha1="48mzSIrjITTHo8vdToi5d4QbCMA" width="480" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1cfabda1bfc943c1f4b1ce5af3b85c9e862e8084_2_480x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1cfabda1bfc943c1f4b1ce5af3b85c9e862e8084.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1cfabda1bfc943c1f4b1ce5af3b85c9e862e8084.jpeg 2x" data-dominant-color="3D3D33"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">582×606 99 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @Sevilay_Karasu (2021-02-03 18:09 UTC)

<p>Thanks for your interest</p>

---
