# Cannot segment after using Transforms and Resample Scalar/vectorDWI Volume modules

**Topic ID**: 39134
**Date**: 2024-09-28
**URL**: https://discourse.slicer.org/t/cannot-segment-after-using-transforms-and-resample-scalar-vectordwi-volume-modules/39134

---

## Post #1 by @Stuart (2024-09-28 18:54 UTC)

<p>I reoriented a skull using the Transforms module and then Resample Scalar/Vector/DWI Volume module. The resulting volume is properly oriented but I cannot segment it. Here are copies of how I set up the Resample page as well as the Error Log when trying to segment.</p>
<p>Thanks for your help in resolving this issue.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f2cc20ac8f1227f09b9270223ad87aecd5b6b2d.png" data-download-href="/uploads/short-url/6JkkKkOVsqTkPtXv90wpVZBA0MZ.png?dl=1" title="Resample Scalar:Vector:DWI Volume" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f2cc20ac8f1227f09b9270223ad87aecd5b6b2d_2_420x500.png" alt="Resample Scalar:Vector:DWI Volume" data-base62-sha1="6JkkKkOVsqTkPtXv90wpVZBA0MZ" width="420" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f2cc20ac8f1227f09b9270223ad87aecd5b6b2d_2_420x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f2cc20ac8f1227f09b9270223ad87aecd5b6b2d_2_630x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/f/2f2cc20ac8f1227f09b9270223ad87aecd5b6b2d_2_840x1000.png 2x" data-dominant-color="E6E6E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Resample Scalar:Vector:DWI Volume</span><span class="informations">1282×1524 164 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad9891432dbc404632d3f6acf51ed8de5e4a8a25.png" data-download-href="/uploads/short-url/oLHty3xBxRt1jr65RdYOYOJFHG5.png?dl=1" title="Error log" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad9891432dbc404632d3f6acf51ed8de5e4a8a25_2_690x131.png" alt="Error log" data-base62-sha1="oLHty3xBxRt1jr65RdYOYOJFHG5" width="690" height="131" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad9891432dbc404632d3f6acf51ed8de5e4a8a25_2_690x131.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad9891432dbc404632d3f6acf51ed8de5e4a8a25_2_1035x196.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad9891432dbc404632d3f6acf51ed8de5e4a8a25_2_1380x262.png 2x" data-dominant-color="ECECEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Error log</span><span class="informations">2574×492 80.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2024-09-29 01:15 UTC)

<p>The only error listed there is from the Resample module, not from the Segment Editor, and then it appears you loaded a different MRB file.</p>

---

## Post #3 by @Stuart (2024-09-29 16:30 UTC)

<p>Thanks. I repeated the Resample process and now it’s all working as expected; i.e., I can segment at will.</p>

---
