---
topic_id: 22430
title: "How To Generate Vascular Stent"
date: 2022-03-10
url: https://discourse.slicer.org/t/22430
---

# How to generate Vascular stent?

**Topic ID**: 22430
**Date**: 2022-03-10
**URL**: https://discourse.slicer.org/t/how-to-generate-vascular-stent/22430

---

## Post #1 by @junqiangchen (2022-03-10 08:50 UTC)

<p>hi,i want generate Virtual Vascular Stent in VTK，i can generate simple Vascular Stent,like this<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2c551b19b6b867bed6261538470c176de199a66b.png" data-download-href="/uploads/short-url/6kblwvrbEicfpSehAoAlkEfMbyj.png?dl=1" title="筒状支架" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2c551b19b6b867bed6261538470c176de199a66b_2_678x499.png" alt="筒状支架" data-base62-sha1="6kblwvrbEicfpSehAoAlkEfMbyj" width="678" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2c551b19b6b867bed6261538470c176de199a66b_2_678x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2c551b19b6b867bed6261538470c176de199a66b.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2c551b19b6b867bed6261538470c176de199a66b.png 2x" data-dominant-color="686B7A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">筒状支架</span><span class="informations">765×564 49.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
i want make simple Vascular Stent more truely，like this result：<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/258fd5197d0a7a464a49edebb8e13c13d2767e2b.jpeg" data-download-href="/uploads/short-url/5mhPcVXYzJ8t4ybuDqlSu6UEVKz.jpeg?dl=1" title="41598_2016_Article_BFsrep21724_Fig1_HTML" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/258fd5197d0a7a464a49edebb8e13c13d2767e2b_2_571x500.jpeg" alt="41598_2016_Article_BFsrep21724_Fig1_HTML" data-base62-sha1="5mhPcVXYzJ8t4ybuDqlSu6UEVKz" width="571" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/258fd5197d0a7a464a49edebb8e13c13d2767e2b_2_571x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/258fd5197d0a7a464a49edebb8e13c13d2767e2b.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/258fd5197d0a7a464a49edebb8e13c13d2767e2b.jpeg 2x" data-dominant-color="CBCCCE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">41598_2016_Article_BFsrep21724_Fig1_HTML</span><span class="informations">685×599 89.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
can anyone know how to do it?<br>
thank you!!</p>

---

## Post #2 by @lassoan (2022-03-12 05:44 UTC)

<p>There are many options for this, depending on what you want to do.</p>
<p>You can scan a real stent and warp it to the vessel’s geometry using the transform computed by <a href="https://github.com/PerkLab/SlicerSandbox#curved-planar-reformat">Curved Planar Reformat module</a>.</p>
<p>You can paint the stent pattern in Gimp or Inkscape, save it as a png, then apply it as a pattern to the model. You can warp this to the exact geometry using Cardiac Device Simulator module in <a href="https://github.com/SlicerHeart/SlicerHeart">SlicerHeart extension</a> as we did it for a non-textured model <a href="https://pubmed.ncbi.nlm.nih.gov/30444053/">here</a>.</p>
<p>For more realistic warping, you can design a straight stent in a CAD software then use finite-element modeling to fit it into the vessel. It is not a very simple simulation (first you need to compress the stent, then enable vessel surface boundary condition and gradually decrease the compression force to let the stent open), but we have done a successful feasibility study of this with Slicer and FEBio Studio.</p>

---

## Post #3 by @junqiangchen (2022-03-15 03:23 UTC)

<p>thank you,i will try those methods.</p>

---
