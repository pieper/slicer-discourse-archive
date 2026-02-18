# Logical operators intersect function causes selected segment to disappear

**Topic ID**: 28896
**Date**: 2023-04-14
**URL**: https://discourse.slicer.org/t/logical-operators-intersect-function-causes-selected-segment-to-disappear/28896

---

## Post #1 by @Shreya_Kashyap (2023-04-14 01:49 UTC)

<p>Hi everyone,<br>
I am trying to use the Intersect function to remove portions of segment1 (yellow) that are not inside segment2 (green). When I click intersect all of segment1 disappears, even portions that should be in segment2. What is going on?<br>
Before intersect:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e0a361439d11272f9c18c8e32da3d4b72319a49.png" data-download-href="/uploads/short-url/hZ02p25V0SoNsOtv41K4msaoTiN.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e0a361439d11272f9c18c8e32da3d4b72319a49.png" alt="image" data-base62-sha1="hZ02p25V0SoNsOtv41K4msaoTiN" width="489" height="500" data-dominant-color="838DA7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">617×630 254 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
With Segment2 removed (still no intersect):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4b7de64644a5cc55b4f8fd1c7ca3dcf2fdc0a04.png" data-download-href="/uploads/short-url/pMHSEQPo5Ceef4WhYGDLb9mGluY.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4b7de64644a5cc55b4f8fd1c7ca3dcf2fdc0a04_2_494x500.png" alt="image" data-base62-sha1="pMHSEQPo5Ceef4WhYGDLb9mGluY" width="494" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4b7de64644a5cc55b4f8fd1c7ca3dcf2fdc0a04_2_494x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4b7de64644a5cc55b4f8fd1c7ca3dcf2fdc0a04.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4b7de64644a5cc55b4f8fd1c7ca3dcf2fdc0a04.png 2x" data-dominant-color="9A9BD0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">640×647 32.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
After intersect:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/871eaa045b743752b341d183823d0e4816fc5bf5.png" data-download-href="/uploads/short-url/jhk9G3WSi9ntUU3w14Uh40Ninn7.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/871eaa045b743752b341d183823d0e4816fc5bf5.png" alt="image" data-base62-sha1="jhk9G3WSi9ntUU3w14Uh40Ninn7" width="487" height="500" data-dominant-color="838DAA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">631×647 243 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
with segment 1 removed:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee5b2459ee97c7367f6b59dbf596a4b8f5c2cf69.png" data-download-href="/uploads/short-url/y0AUlpollYPSWxsaf9NjZw84tbH.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee5b2459ee97c7367f6b59dbf596a4b8f5c2cf69.png" alt="image" data-base62-sha1="y0AUlpollYPSWxsaf9NjZw84tbH" width="503" height="500" data-dominant-color="9B9CD3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">652×648 4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks,<br>
Shreya</p>

---

## Post #2 by @lassoan (2023-04-15 03:08 UTC)

<p>Can you provide a sample data set that we can use to reproduce the behavior that you find unexpected?</p>

---
