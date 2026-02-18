# How to understand SegmentMesher with Image spacing and Image Dimensions

**Topic ID**: 44632
**Date**: 2025-09-30
**URL**: https://discourse.slicer.org/t/how-to-understand-segmentmesher-with-image-spacing-and-image-dimensions/44632

---

## Post #1 by @Shajia_Ali (2025-09-30 11:47 UTC)

<p>Hello everyone,</p>
<p>I am using SegmentMesher for meshing, and so far things are going well. However, I am still trying to understand how image dimensions and voxel spacing influence the element size and the total number of elements.</p>
<p>For instance, I worked with a 3D image of a cube that I downscaled to <strong>155 × 155 × 155 pixels</strong> with a spacing of <strong>1 mm</strong>. Using the parameters shown in the attached screenshot, SegmentMesher generated about <strong>2.6 million elements</strong>.</p>
<p>In contrast, the original dataset had <strong>310 × 310 × 310 pixels</strong>, and the actual physical size of the cube was only <strong>0.2 mm</strong>. After I applied the same parameters on SegmentMesher to this dataset, I received <strong>over 10 million elements</strong>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/312b144ad19e70bd54273b3802b9954478146380.png" data-download-href="/uploads/short-url/70XGXIBHsigZSQcZHM7dX2ISNnq.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/312b144ad19e70bd54273b3802b9954478146380.png" alt="image" data-base62-sha1="70XGXIBHsigZSQcZHM7dX2ISNnq" width="623" height="466"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">623×466 10.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2025-10-02 21:10 UTC)

<p>In general, 2x increase of resolution on an axis results in 8x more elements.</p>
<p>However, Cleaver can dynamically adjust the element size - creating larger elements inside a segment, while creating smaller elements on the surface to preserve small details. This dynamic adjustment is controlled by rate of change (how much size difference is allowed between neighbor elements) and feature scaling parameters (overall responsiveness of element size to mesh details).</p>
<p>I would recommend to experiment with features scaling and sampling rate parameters. I think adjustment of sampling rate is equivalent with resampling your input segmentation/labelmap.</p>

---
