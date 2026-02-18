# Threshold range in Segment Editor includes values outside of range

**Topic ID**: 20869
**Date**: 2021-12-01
**URL**: https://discourse.slicer.org/t/threshold-range-in-segment-editor-includes-values-outside-of-range/20869

---

## Post #1 by @koeglfryderyk (2021-12-01 18:41 UTC)

<p>I’m using Slicer 4.11.20210226 on Windows 11.</p>
<p>I want to create a segmentation of all values greater than zero.</p>
<p>When I set the lower threshold to e.g. 0.2 it still includes pixels with values equal to zero (you can see in the screenshot that I was hovering over a value that is 0 and the entire screen is in green). Only when I set the threshold &gt;= 1 the 0 values disappear.</p>
<p>Is it maybe related to the fact that that the data array of the image is in uint8, so a float threshold doesn’t work?</p>
<p>(why I’m doing this - I want to create a segmentation of the entire volume and this seemed to be the easiest way)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8e05228ab25d0d0f0e40ed45b615016ac7f168d.png" data-download-href="/uploads/short-url/xe7nt3vXKGZjb2LV6qRM44tPdzD.png?dl=1" title="threshold" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8e05228ab25d0d0f0e40ed45b615016ac7f168d_2_690x364.png" alt="threshold" data-base62-sha1="xe7nt3vXKGZjb2LV6qRM44tPdzD" width="690" height="364" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8e05228ab25d0d0f0e40ed45b615016ac7f168d_2_690x364.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8e05228ab25d0d0f0e40ed45b615016ac7f168d_2_1035x546.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8e05228ab25d0d0f0e40ed45b615016ac7f168d_2_1380x728.png 2x" data-dominant-color="C4CEC8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">threshold</span><span class="informations">1920×1015 201 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
