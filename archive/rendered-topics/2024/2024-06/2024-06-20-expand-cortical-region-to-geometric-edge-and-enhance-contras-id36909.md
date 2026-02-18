# Expand Cortical Region to Geometric Edge and Enhance Contrast at Edge

**Topic ID**: 36909
**Date**: 2024-06-20
**URL**: https://discourse.slicer.org/t/expand-cortical-region-to-geometric-edge-and-enhance-contrast-at-edge/36909

---

## Post #1 by @William_Kuo (2024-06-20 03:40 UTC)

<p>I want to expand the cortical bone to edges of the masked region, marked by my geometric line in the scan. After I expand the cortical region to those edges, I want to enhance the contrast at that edge. Are there a set of filters that can produce this effect?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd5a23979a27d2e3b2cb01ab9b30bdf17c0f7418.png" data-download-href="/uploads/short-url/r15myPD22BqNJ6HV2qFdcLeBeLC.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd5a23979a27d2e3b2cb01ab9b30bdf17c0f7418_2_458x500.png" alt="image" data-base62-sha1="r15myPD22BqNJ6HV2qFdcLeBeLC" width="458" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd5a23979a27d2e3b2cb01ab9b30bdf17c0f7418_2_458x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/d/bd5a23979a27d2e3b2cb01ab9b30bdf17c0f7418_2_687x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/d/bd5a23979a27d2e3b2cb01ab9b30bdf17c0f7418.png 2x" data-dominant-color="222320"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">703×766 73.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-06-22 05:06 UTC)

<p>You can blank out the v9lume outside the segment using <code>Mask volume</code> effect in Segment Editor module.</p>
<p>We would need more information to give you advice on filtering. You need to specify what you consider useful signal (that you want to enhance) and what you consider noise (that tou want to suppress). What is your end goal?Quentitative analysis, 3D printing, surgical simulation, …?</p>

---

## Post #3 by @William_Kuo (2024-06-25 11:52 UTC)

<p>The volume I showed above is already masked by a segmentation.</p>
<p>I want to edit the HU values of the pixels near the border. I want to be able to select the pixels between the cortical bone and the edge and increase them to the level of the cortical bone. Since the highest density cortical bone appears to be about 2 pixels layers away from the geometric boundary, I want to incorporate a filter that raises the HU of the pixels in between closer to the HU of the cortical bone. I tried several filters to generate this effect but I have been unsuccessful. The goal is to reduce partial volume effects and mitigate segmentation accuracy for finite element analysis. I believe partial volume effects and the capture of low HU pixels (due to segmentation accuracy) are causing underprediction in the strength of my finite element results.</p>

---
