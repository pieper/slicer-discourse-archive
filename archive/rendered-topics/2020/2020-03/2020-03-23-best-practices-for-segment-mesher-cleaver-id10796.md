# Best Practices for Segment Mesher, Cleaver

**Topic ID**: 10796
**Date**: 2020-03-23
**URL**: https://discourse.slicer.org/t/best-practices-for-segment-mesher-cleaver/10796

---

## Post #1 by @Fluvio_Lobo (2020-03-23 17:10 UTC)

<p>Hello,</p>
<p>Our team is trying to use the <strong>segment mesher</strong> extension on a multi-material model of breast tissue, segmented from an MRI dataset. We are having great success, but still have some questions related to best practices for implementing this plug-in.</p>
<p><strong>Our process/pipeline:</strong></p>
<ol>
<li>In general, we segment three (3) materials: skin, breast tissue (adipose + glandular), and tumor/mass</li>
<li>We use <strong>segment mesher</strong> to create a tetrahedral mesh</li>
<li>We perform mechanical simulation on the mesh using FEBio</li>
</ol>
<p><strong>Our issue:</strong></p>
<ol>
<li><strong>We currently get a very fine mesh on the outside surface of our model</strong> (Figure 1, below). <em>The screenshot is from FEBio.</em> This mesh follows the “stepping” of the model due to the scan. We have tried median and Gaussian filters on the segmentation and the result above is one of the best results we have achieved. I have played with the cleaver parameters, but varying these ends-up affecting the mesh internal features.</li>
</ol>
<p><strong>Does anyone have any advice on how to segment and smooth data prior to meshing?</strong></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8bf8591e003824c46279455765ffeb55d5a30b61.png" data-download-href="/uploads/short-url/jYes0C6mVkhegwy4fTyMR4poyu5.png?dl=1" title="Figure 1: Fine Mesh" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8bf8591e003824c46279455765ffeb55d5a30b61_2_690x373.png" alt="Figure 1: Fine Mesh" data-base62-sha1="jYes0C6mVkhegwy4fTyMR4poyu5" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8bf8591e003824c46279455765ffeb55d5a30b61_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8bf8591e003824c46279455765ffeb55d5a30b61_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8bf8591e003824c46279455765ffeb55d5a30b61_2_1380x746.png 2x" data-dominant-color="B4B5D4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Figure 1: Fine Mesh</span><span class="informations">1920×1040 1.02 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Also, separate issue I have found with the <strong>segment mesher</strong> plug-in:</p>
<ol start="2">
<li><strong>The .VTK file in the temp folder that results from cleaver’s meshing is ASCII while the file saved from the Slicer interface is Binary.</strong> Is there a way for the plug-in to use/save the ASCII file? Programs like FEBioStudio do not have .VTK Binary readers</li>
</ol>

---

## Post #2 by @lassoan (2020-03-23 18:11 UTC)

<aside class="quote no-group" data-username="Fluvio_Lobo" data-post="1" data-topic="10796">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/fluvio_lobo/48/81262_2.png" class="avatar"> Fluvio_Lobo:</div>
<blockquote>
<p>This mesh follows the “stepping” of the model due to the scan</p>
</blockquote>
</aside>
<p>To fix this, resample the input volume to have isotropic spacing (cube shaped voxels) <em>before</em> you start segmentation, using Crop volume module.</p>
<p>Other than that, I would recommend to experiment with meshing parameters described <a href="https://github.com/lassoan/SlicerSegmentMesher#mesh-generation-parameters">here</a> on a small volume.</p>
<aside class="quote no-group" data-username="Fluvio_Lobo" data-post="1" data-topic="10796">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/fluvio_lobo/48/81262_2.png" class="avatar"> Fluvio_Lobo:</div>
<blockquote>
<p>The .VTK file in the temp folder that results from cleaver’s meshing is ASCII while the file saved from the Slicer interface is Binary.</p>
</blockquote>
</aside>
<p>When you save the mesh in Slicer, uncheck “Compress” option in Save data window to save as ASCII.</p>

---

## Post #3 by @Vasko (2024-02-20 23:32 UTC)

<p>Can You please help me find the “Compress” option in save data window. I need to save volumetric mesh as ascii.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/20f27782851f17943a1b8aff17b1dfe5aa6ee339.jpeg" alt="save data" data-base62-sha1="4HsLeyXiyHMoFDa83XWO4hMNpTH" width="632" height="337"></p>

---

## Post #4 by @pieper (2024-04-20 15:47 UTC)

<p>Click the “Show options” box.</p>

---
