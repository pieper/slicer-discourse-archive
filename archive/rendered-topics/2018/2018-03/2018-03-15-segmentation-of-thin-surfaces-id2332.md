---
topic_id: 2332
title: "Segmentation Of Thin Surfaces"
date: 2018-03-15
url: https://discourse.slicer.org/t/2332
---

# Segmentation of thin surfaces

**Topic ID**: 2332
**Date**: 2018-03-15
**URL**: https://discourse.slicer.org/t/segmentation-of-thin-surfaces/2332

---

## Post #1 by @hherhold (2018-03-15 22:24 UTC)

<p>Hey Slicers,</p>
<p>I’m curious if anyone has any suggestions on strategies for segmentation of some specimens we’re working on. These are micro-CT scanned insects (dried, pinned specimens) that have thin cuticular membranes internally that I want to segment out. The membranes are very thin and wind up having absorbances pretty close to the background air. Here’s a representative image as an example:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf774efee47905a01e944abd4d4b8f97b3c1f82b.jpeg" data-download-href="/uploads/short-url/tBks8wnZrTapD6Tub8v5r2spEPV.jpg?dl=1" title="Thin%20membrane" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf774efee47905a01e944abd4d4b8f97b3c1f82b_2_690x492.jpg" alt="Thin%20membrane" data-base62-sha1="tBks8wnZrTapD6Tub8v5r2spEPV" width="690" height="492" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf774efee47905a01e944abd4d4b8f97b3c1f82b_2_690x492.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cf774efee47905a01e944abd4d4b8f97b3c1f82b_2_1035x738.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf774efee47905a01e944abd4d4b8f97b3c1f82b.jpeg 2x" data-dominant-color="5B5A5A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Thin%20membrane</span><span class="informations">1272×908 228 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The red is my segmentation in progress, and you can see how the membrane is very thin and also very close to the background absorbance.</p>
<p>Thus far, my strategy has been to use sphere brush and symmetric scissors with a set intensity range as much as possible, periodically using island removal to “de-speckle”. This results in lots of holes in the reconstructed surface, however, that I wind up going back and cleaning up manually using a brush. This can be somewhat time consuming, and I’m looking for ways to speed up the process.</p>
<p>I’ve tried flood filling and other algorithms a couple of times without a lot of success. Just curious if anyone has run into any algorithms or anything that do any kind of “surface following”, for lack of a better term, or if there are any fancy ITK filters called “Automatic Insect Membrane Determination”. (OK, that last one is a bit of a stretch.)</p>
<p>Thanks in advance for any ideas anyone has!</p>
<p>-Hollister</p>

---

## Post #2 by @lassoan (2018-03-16 00:30 UTC)

<p>We had very similar problem when <a href="https://qspace.library.queensu.ca/bitstream/handle/1974/15290/Ibrahim_Amani_201612_MSc.pdf?sequence=2&amp;isAllowed=y">segmenting thin orbital bone</a>. Couple of things that helped:</p>
<ul>
<li>Crop and resample your volume to make the structures that you want to segment at least 4-5 voxel wide. Otherwise all the region-growing based method will fail, as due to random noise a few voxels may be missed and your structure may break to parts.</li>
<li>Apply filtering, which enhances thin structures. We have found that unsharp masking helped.</li>
<li>If the structure that you need to represent is a surface then instead of a volumetric representation, you may try to reconstruct a surface from points. See this <a href="https://gist.github.com/lassoan/74b5efb699b1c9d3a6ef76d98c77b697">complete example</a> that works in Slicer as is, See also these additional VTK examples: <a href="https://lorensen.github.io/VTKExamples/site/Cxx/Points/PoissonExtractSurface/">Poisson surface reconstruction</a>, <a href="https://lorensen.github.io/VTKExamples/site/Cxx/Points/CompareExtractSurface/">comparison of 3 surface reconstruction methods that are available in VTK</a>. If this approach works well then let me know and I can make a segment editor effect from it.</li>
<li>You may paint the structure manually on a couple of (non-neighbor) slices and use <code>Fill between slices</code> effect to create a complete segmentation out of it.</li>
</ul>

---

## Post #3 by @hherhold (2018-03-16 14:39 UTC)

<p>Hey Andras,</p>
<p>These are great ideas, and thanks for the reference.</p>
<p>I’ll report back on the surface ideas (it is indeed a surface we want out of this, not necessarily a volume) to see if it makes sense to make a segment editor effect.</p>
<p>Thanks again!!!</p>
<p>-Hollister</p>

---
