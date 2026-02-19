---
topic_id: 26052
title: "Volumetric Mesh Generation For Finite Element Analysis Of Sp"
date: 2022-11-02
url: https://discourse.slicer.org/t/26052
---

# Volumetric mesh generation for finite element analysis of spine

**Topic ID**: 26052
**Date**: 2022-11-02
**URL**: https://discourse.slicer.org/t/volumetric-mesh-generation-for-finite-element-analysis-of-spine/26052

---

## Post #1 by @Ron (2022-11-02 17:03 UTC)

<p>Andras hi</p>
<p>Dr. Zahra Soltani is working with me on an NIH patient study as part of our MIT collaboration.  Previously, we have used Medtool to 1) create tet-based meshes for the vertebrae (it uses CGAL for this purpose) and 2) the application of material cards to the mesh based on HU-bone modulus calibration curve (medtool has scripts to map modulus to the tets, based the volumetric CT). We are hoping to move the complete pipeline to Slicer.  We are evaluating Tetgen and would like to evaluate Gmesh as we had experience with this 3Dmesher prior.  We are grateful for any advice for both processes.  Ron</p>

---

## Post #2 by @lassoan (2022-11-03 12:39 UTC)

<p>SegmentMesher extension can create multi-material tetrahedral meshes from segmentation. You can add CT densities to the mesh using “Probe volume with model” module. The resulting mesh with all these metadata can be saved as a VTK unstructured grid, you can run simulations on it in FEBio, and read the results back into Slicer for visualization and analysis.</p>

---

## Post #3 by @Ron (2022-11-03 12:58 UTC)

<p>Andras, thank you.  Our simulations are running using a specialized code from MIT for modeling damage.  We hope to replace some of the tools previously used in our pipeline to 1) mesh (CGAL)and apply materials( internal scripts) using medtool, <a href="http://www.dr-pahr.at/medtool/" class="inline-onebox" rel="noopener nofollow ugc">medtool</a>, which recently switched its segmentation tools to Slicer.  Our previous experience with Cleaver for mesh generation was less the par regarding mesh quality, and we had to use MIT-based tools to improve the mesh quality,  Hence we are looking at tetgen and Gmesh, the latter has been used by our colleagues in swizetrland for generating meshes for spines.  Our pipeline uses the CT to apply modulus to the different bone compartments (cancellous, vertebral cortex, cortical bone) based on empirical formula driven by CT density.  Could elaborate a bit more regarding “Probe volume with model” module?</p>

---

## Post #4 by @pieper (2022-11-03 14:19 UTC)

<p><a class="mention" href="/u/ron">@Ron</a> the “Probe volume with model” module will assign the CT value to each vertex of the mesh.  You can then map that to material properties using whatever method you prefer.</p>
<p>You can also use whatever meshing tools you want external to Slicer, and feedback about how they compare to options available in Slicer is very valuable.  We’re just not able/willing to build code into Slicer that comes under a GPL license.  Historically the non-GPL code usually ends up being as good or better than other options but that may not be the case in meshing.  Probably the resulting meshes can be interoperable.</p>

---

## Post #5 by @Ron (2022-11-03 14:37 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> Steve that makes sense.  we are looking at Tetgen to see if the quality of the mesh is comparable to CGAL and test if we need to use the MIT tools to fix the output. If this works well, then the issue is moot. I was unaware of the “Probe volume with model” module. That might be the solution for what we need as we can then apply the portion of the code we already have to map the density to modulus and then write it as mesh with material cards.  It might be worth it to create an extension within segment mesher that carries out this mapping based on user-based input equations.  Happy to use the CT code for that</p>

---

## Post #6 by @lassoan (2022-11-03 15:17 UTC)

<aside class="quote no-group" data-username="Ron" data-post="5" data-topic="26052">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ron/48/10835_2.png" class="avatar"> Ron:</div>
<blockquote>
<p>we are looking at Tetgen to see if the quality of the mesh is comparable to CGAL</p>
</blockquote>
</aside>
<p>FYI, Tetgen’s free license is AGPL, which is even more restrictive than GPL. You can of course still use Tetgen, but you may need to replace it at some point anyway (as you want to control what you do with your software), and for us it is harder to justify spending any time with it (because any time we invest into someone else’s AGPL/commercial offering is time taken away from supporting restriction-free open-source projects).</p>
<aside class="quote no-group" data-username="Ron" data-post="3" data-topic="26052">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ron/48/10835_2.png" class="avatar"> Ron:</div>
<blockquote>
<p>Our previous experience with Cleaver for mesh generation was less the par regarding mesh quality</p>
</blockquote>
</aside>
<p>Cleaver can generate multimaterial volumetric meshes directly from binary labelmaps. This is a significant advantage compared to all other meshers, which require a surface mesh as input (because generating a smooth surface mesh from a binary segmentation is a non-trivial task). That said, Cleaver may not have as many features as some other meshers, may be slower than some, and you may need to tune a few parameters to get good quality results.</p>
<p>If you provide some sample input segmentations and your existing sufficiently good quality volumetric meshes then I can give it a try to generate similar meshes using Cleaver.</p>
<p>While we are testing Cleaver, please also try <a href="https://github.com/wildmeshing/fTetWild">fTetWild</a>. I’ve heard good things about TetWild, but that has some CGAL dependencies, so it would be nice to see how this new fTetWild variant (without any complicated dependencies) work. If it seems to produce better results than Cleaver then we will add it to SegmentMesher extension.</p>

---

## Post #7 by @Ron (2022-11-03 16:24 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>, <a class="mention" href="/u/pieper">@pieper</a></p>
<blockquote>
<p>FYI, Tetgen’s free license is AGPL, which is even more restrictive than GPL. You can of course still use Tetgen, but you may need to replace it at some point anyway (as you want to control what you do with your software), and for us it is harder to justify spending any time with it (because any time we invest into someone else’s AGPL/commercial offering is the time taken away from supporting restriction-free open-source projects).</p>
</blockquote>
<p>Ah,  We thought of going with the option offered as part of the segment mesher install.</p>
<blockquote>
<p>Cleaver can generate multimaterial volumetric meshes directly from binary labelmaps. This is a significant advantage compared to all other meshers, which require a surface mesh as input (because generating a smooth surface mesh from a binary segmentation is a non-trivial task). That said, Cleaver may not have as many features as some other meshers, may be slower than some, and you may need to tune a few parameters to get good quality results.</p>
</blockquote>
<p>My colleague at MIT is not impressed with the mesh quality from Cleaver.  But what we can do is produce meshes using Cleaver, as I have better segmentation of the vertebrae, and evaluate/send them over.</p>
<blockquote>
<p>While we are testing Cleaver, please also try <a href="https://github.com/wildmeshing/fTetWild" rel="noopener nofollow ugc">fTetWild</a>. I’ve heard good things about TetWild, but that has some CGAL dependencies, so it would be nice to see how this new fTetWild variant (without any complicated dependencies) work. If it seems to produce better results than Cleaver then we will add it to SegmentMesher extension</p>
</blockquote>
<p>We would be happy to.</p>
<p>As a related issue, I think it would be advantageous to have an extension of the segmentmesher to write material cards based on mapping of density to modulus once the HU values are mapped with the user selecting from existing empirical equations or inputting his calibration curve/values.  Happy to contribute some code for this effort.  the question is how the mapping of HU values is performed for the FE elements (Git?)</p>
<p>Thanks for all you help, R</p>

---

## Post #8 by @lassoan (2022-11-03 16:34 UTC)

<aside class="quote no-group" data-username="Ron" data-post="7" data-topic="26052">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ron/48/10835_2.png" class="avatar"> Ron:</div>
<blockquote>
<p>the question is how the mapping of HU values is performed for the FE elements</p>
</blockquote>
</aside>
<p>“Probe volume with model” assigns the voxel values of the input volume as point data for each mesh point. If you want to assign not the radiologic density (HU) but some other value, then a simple option would be to transform all the voxel values by applying the calibration curve and probe this modified volume. A very small Python scripted module could be added, similar to the <a href="https://github.com/acil-bwh/SlicerCIP/blob/develop/Scripted/CIP_Calibration/CIP_Calibration.py">image intensity calibration module in CIP</a>.</p>

---

## Post #9 by @Ron (2022-11-03 16:57 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a><br>
Andras, thank you, Great, Zahra has a lot of experience in programming with C++ and python related to FE and mesh codes.  we would be happy to contribute.  I will ask Zahra to look at the module. R</p>

---

## Post #10 by @ZSoltani (2022-11-03 17:30 UTC)

<p>More than happy to contribute and learn more. Thanks all.</p>

---

## Post #11 by @pieper (2022-11-03 17:39 UTC)

<p>Great Zahra!  A good place to start would be to have a look at the extension code and also the Slicer programming tutorial resources.  Let us know if you need pointers.</p>

---

## Post #12 by @ZSoltani (2022-11-03 18:12 UTC)

<p>Sure, we will get back to you then.</p>

---

## Post #13 by @ZSoltani (2022-11-15 17:29 UTC)

<p>HI Andras,</p>
<p>I can’t find “Probe volume with model” module among the in the extension manager. Is it still available of 3D Slicer, version 5.0.3 r30893 / 7ea0f43?</p>
<p>Thanks,<br>
Zahra</p>

---

## Post #14 by @lassoan (2022-11-15 17:30 UTC)

<p><code>Probe volume with model</code> is not an extension, it is a module included in Slicer core.</p>

---

## Post #15 by @ZSoltani (2022-11-15 17:44 UTC)

<p>Thank you for your reply.</p>
<p>Zahra</p>

---
