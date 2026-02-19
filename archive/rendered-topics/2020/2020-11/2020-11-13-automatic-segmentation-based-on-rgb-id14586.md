---
topic_id: 14586
title: "Automatic Segmentation Based On Rgb"
date: 2020-11-13
url: https://discourse.slicer.org/t/14586
---

# Automatic segmentation based on rgb

**Topic ID**: 14586
**Date**: 2020-11-13
**URL**: https://discourse.slicer.org/t/automatic-segmentation-based-on-rgb/14586

---

## Post #1 by @Calumanderson5 (2020-11-13 15:03 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/387f9be1dc1026e4ee8bcf41fca5f5364df769a8.png" data-download-href="/uploads/short-url/83O8D1DKgCZcHEeSKTJwScMipsc.png?dl=1" title="segmentation second try" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/387f9be1dc1026e4ee8bcf41fca5f5364df769a8_2_608x500.png" alt="segmentation second try" data-base62-sha1="83O8D1DKgCZcHEeSKTJwScMipsc" width="608" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/387f9be1dc1026e4ee8bcf41fca5f5364df769a8_2_608x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/387f9be1dc1026e4ee8bcf41fca5f5364df769a8_2_912x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/387f9be1dc1026e4ee8bcf41fca5f5364df769a8.png 2x" data-dominant-color="B39D9B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">segmentation second try</span><span class="informations">951×781 96.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Hello,</p>
<p>Im using 3D slicer 4.10.2</p>
<p>I’ve done some annotations on qupath and now im looking at creating a 2d model of the annotations. I’ve attached a picture of the annotations. Is there a way to automatically segment based on the rgb value? I need 3 segmentations. 1 for each colour ignoring the grey. I can remove the grey if that will lead to problems</p>

---

## Post #2 by @lassoan (2020-11-13 15:24 UTC)

<p>Slicer should be able to load these segmentations directly. Small adjustments may be necessary in the image header to specify how to interpret each image dimension.</p>
<p>Can you export your segmentation to nrrd file format? If not, what export formats are available in qupath?</p>
<p>How the segmentation is saved if you have more than 3 segments? Is it still and RGB image with more colors, or you then have a multi-channel image (one channel for each segment)?</p>
<p>Do you work with 2D or 3D images? Is generating a surface mesh from each segment is all you need? What is the end goal of the project?</p>

---
