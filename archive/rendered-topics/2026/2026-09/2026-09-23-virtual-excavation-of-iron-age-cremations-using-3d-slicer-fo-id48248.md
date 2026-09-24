---
topic_id: 48248
title: "Virtual Excavation of Iron Age Cremations: Using 3D Slicer for CT Analysis of Block-Lifted Graves."
date: 2026-09-23
url: https://discourse.slicer.org/t/48248
last_bumped: 2026-09-23T19:39:42.356Z
---

# Virtual Excavation of Iron Age Cremations: Using 3D Slicer for CT Analysis of Block-Lifted Graves.

**Topic ID**: 48248
**Date**: 2026-09-23
**URL**: https://discourse.slicer.org/t/virtual-excavation-of-iron-age-cremations-using-3d-slicer-for-ct-analysis-of-block-lifted-graves/48248

---

## Post #1 by @Danille_Melet (2026-09-23 14:49 UTC)

<p>Hi everyone,</p>
<p>I wanted to share a novel, non-clinical archaeological application of <strong>3D Slicer (v5.8.1)</strong> from my Bachelor’s thesis in Archaeology. A big thank you to the 3D Slicer developer community for providing such an adaptable tool! I’d love to hear thoughts, critiques, or ideas!</p>
<p>My study focused on the non-destructive 3D reconstruction and virtual excavation of intact, block-lifted (<em>en bloc</em>) unurned Iron Age cremation burials (c. 800–400 BC) from the site of Haps-Laarakker<sup></sup>. While clinical CT has occasionally been tested on ceramic cremation urns, applying a full open-source 3D workflow to <strong>unurned, soil-embedded cremation blocks</strong> has, to our knowledge, not ever been documented before<sup></sup>.</p>
<p>Destructive physical excavation permanently destroys the fine spatial relationships of fragmented calcined bone, grave cuts, and organic container voids<sup></sup>. Commercial imaging suites often create financial barriers for field archaeology units and cultural heritage labs. I committed to building an entirely open-source, fully reproducible workflow using <strong>3D Slicer</strong> to ensure other researchers can replicate my methodology without proprietary software<sup></sup>.</p>
<h3><a name="p-135975-key-technical-challenges-slicer-workflow-1" class="anchor" href="#p-135975-key-technical-challenges-slicer-workflow-1" aria-label="Heading link"></a>Key Technical Challenges &amp; Slicer Workflow</h3>
<p>The dataset was acquired on a Siemens SOMATOM Definition dual-source scanner (helical scan, reconstructed as DICOM image stacks across axial, coronal, and sagittal planes)<sup></sup>.</p>
<ol>
<li>
<p><strong>Scan Orientation Matters:</strong> I tested both horizontal and vertical scanning of the PVC block-lift tubes<sup></sup>. Horizontal positioning produced severe streak artifacts, blurred boundaries, and artificial fragment fusion<sup></sup>. Scanning the core vertically retained sharp density boundaries, which proved critical for segmenting sub-centimeter bone fragments<sup></sup>.</p>
</li>
<li>
<p><strong>Severe Density Overlap:</strong> Unlike fresh clinical bone, archaeological calcined bone, pottery shards, iron-rich sand, and gravel inclusions at Haps exhibit heavily overlapping radiodensities (attenuation values)<sup></sup>. Automated thresholding alone was insufficient<sup></sup>:</p>
<ul>
<li>
<p>I initiated segmentation using the <strong>Threshold</strong> effect combined with an island filter (<strong>Remove small islands &lt; 120 voxels</strong>, calibrated to exclude the local sand grain size of &lt;2000 μm)<sup></sup>.</p>
</li>
<li>
<p>I utilized <strong>Split islands to segments</strong> (resulting in over 800 individual candidate segments per core) followed by systematic multi-slice validation across all orthogonal views to remove noise and matrix false-positives<sup></sup>.</p>
</li>
</ul>
</li>
<li>
<p><strong>Negative Space &amp; Perishable Containers:</strong> Beyond bone, I used threshold masking and the <strong>Scissors/Cut</strong> tool to model negative space (voids and root structures)<sup></sup>. This allowed me to detect decayed organic structures (Type C cremation containers) and grave cut boundaries that were otherwise completely invisible during subsequent physical laboratory excavation<sup></sup>.</p>
</li>
<li>
<p><strong>Spatial Mapping with Markups/Glyphs:</strong> By matching numbered osteological fragments from laboratory excavation photos to our Slicer segments, we generated color-coded anatomical glyph models<sup></sup>.</p>
</li>
</ol>
<h3><a name="p-135975-archaeological-takeaway-2" class="anchor" href="#p-135975-archaeological-takeaway-2" aria-label="Heading link"></a>Archaeological Takeaway</h3>
<p>In one burial (cremation 6436), Slicer’s spatial mapping proved that <strong>24 of 29 identified skeletal fragments followed a deliberate anatomical sequence</strong> (cranium in the west, lower limbs in the east), with grave pottery positioned deliberately around rather than within the bone cluster<sup></sup>. Slicer allowed us to prove intentional burial rites in an assemblage that would have and has looked like a random heap of fragments in conventional and laboratory excavation alike<sup></sup>.</p>
<h3><a name="p-135975-paper-zenodo-doi-3" class="anchor" href="#p-135975-paper-zenodo-doi-3" aria-label="Heading link"></a>Paper &amp; Zenodo DOI</h3>
<p>For anyone interested in my resulting thesis:</p>
<p><strong>Zenodo DOI:</strong> <a href="https://www.google.com/search?q=https://doi.org/10.5281/zenodo.22917511&amp;utm_source=gemini" rel="noopener nofollow ugc">https://doi.org/10.5281/zenodo.22917511</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49034a698a51e87f3ad77171fd8be0a79e97264b.jpeg" data-download-href="/uploads/short-url/apTU92lTl1lL7Khmi2s5ZXPMYpZ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/49034a698a51e87f3ad77171fd8be0a79e97264b_2_690x476.jpeg" alt="image" data-base62-sha1="apTU92lTl1lL7Khmi2s5ZXPMYpZ" width="690" height="476" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/49034a698a51e87f3ad77171fd8be0a79e97264b_2_690x476.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49034a698a51e87f3ad77171fd8be0a79e97264b.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49034a698a51e87f3ad77171fd8be0a79e97264b.jpeg 2x" data-dominant-color="5F5F56"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">940×649 146 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><strong>Figure 1: Initial intensity thresholding in 3D Slicer.</strong> Raw density-based segmentation capturing calcined bone alongside surrounding sediment matrix and streak artifacts prior to voxel filtering.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d933e69b599bfa5ea94f948e4ae168c834f307c.png" data-download-href="/uploads/short-url/6vaXbjRupN07GH3NSoRGhk09rYg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d933e69b599bfa5ea94f948e4ae168c834f307c_2_690x436.png" alt="image" data-base62-sha1="6vaXbjRupN07GH3NSoRGhk09rYg" width="690" height="436" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d933e69b599bfa5ea94f948e4ae168c834f307c_2_690x436.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d933e69b599bfa5ea94f948e4ae168c834f307c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d933e69b599bfa5ea94f948e4ae168c834f307c.png 2x" data-dominant-color="F9F8F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">940×595 88.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><strong>Figure 2: Segmented bone cluster following manual validation.</strong> 3D volumetric reconstruction after connected-component filtering (&gt;120 voxels) and multi-slice manual clean-up, preserving the in situ spatial relationships of the cremation deposit.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/bed791780175fb9bc1a22eb4bda2eba37d71bf84.png" data-download-href="/uploads/short-url/regztycVOJvq2gCi7EI6INcNWza.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/bed791780175fb9bc1a22eb4bda2eba37d71bf84_2_690x473.png" alt="image" data-base62-sha1="regztycVOJvq2gCi7EI6INcNWza" width="690" height="473" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/bed791780175fb9bc1a22eb4bda2eba37d71bf84_2_690x473.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/bed791780175fb9bc1a22eb4bda2eba37d71bf84.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/bed791780175fb9bc1a22eb4bda2eba37d71bf84.png 2x" data-dominant-color="F9F9F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">940×645 35.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><strong>Figure 3: Spatial distribution of skeletal elements using color-coded glyphs.</strong> Integration of physical anthropological identifications with the 3D model, highlighting the deliberate anatomical ordering (cranium west to lower limbs east) in cremation 6436.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f8679885fe25afcdfedaeac230c94fc84546074.jpeg" data-download-href="/uploads/short-url/fUB6OTLntSwb6LjEX2NFAAJSDbe.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f8679885fe25afcdfedaeac230c94fc84546074_2_690x452.jpeg" alt="image" data-base62-sha1="fUB6OTLntSwb6LjEX2NFAAJSDbe" width="690" height="452" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6f8679885fe25afcdfedaeac230c94fc84546074_2_690x452.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f8679885fe25afcdfedaeac230c94fc84546074.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f8679885fe25afcdfedaeac230c94fc84546074.jpeg 2x" data-dominant-color="B5C9B5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">940×616 223 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><strong>Figure 4: Negative space segmentation revealing structural voids.</strong> Volumetric visualization of soil voids and diverted root paths, providing non-destructive evidence for a decayed organic container and grave cut outline (Type C cremation).</p>

---

## Post #2 by @mikebind (2026-09-23 19:39 UTC)

<p>Very cool!  Just FYI, the link took me to a google search page which said it didn’t find anything.  Pasting the search term directly as a URL worked though:  <a href="https://zenodo.org/records/22917511" rel="noopener nofollow ugc">https://zenodo.org/records/22917511</a></p>

---
