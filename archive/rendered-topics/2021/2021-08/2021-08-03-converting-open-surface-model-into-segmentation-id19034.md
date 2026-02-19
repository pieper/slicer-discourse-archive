---
topic_id: 19034
title: "Converting Open Surface Model Into Segmentation"
date: 2021-08-03
url: https://discourse.slicer.org/t/19034
---

# Converting open surface model into segmentation

**Topic ID**: 19034
**Date**: 2021-08-03
**URL**: https://discourse.slicer.org/t/converting-open-surface-model-into-segmentation/19034

---

## Post #1 by @siaeleni (2021-08-03 00:58 UTC)

<p>Hello,<br>
I am wondering whether the result from the segmentation is correct.<br>
I load a .stl file and, right-click “convert model to segmentation mode”.<br>
The result that I get seems weird, but I am not sure if that is correct. Please see attached image.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40651072741f52ea54824141bf8cfd78bb950734.png" data-download-href="/uploads/short-url/9bF5pq2HJiUUx7obk4fV6uTKhMg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40651072741f52ea54824141bf8cfd78bb950734_2_690x401.png" alt="image" data-base62-sha1="9bF5pq2HJiUUx7obk4fV6uTKhMg" width="690" height="401" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40651072741f52ea54824141bf8cfd78bb950734_2_690x401.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40651072741f52ea54824141bf8cfd78bb950734_2_1035x601.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40651072741f52ea54824141bf8cfd78bb950734.png 2x" data-dominant-color="3B3C37"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1272×741 40.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2021-08-03 01:57 UTC)

<p>Segmentation can be imported from a closed surface, but it looks like you have an open surface (surface with many large holes). You would need to close the surface before you can import it into a segmentation.</p>
<p>You can give it a try to fill the holes after you imported the surface into a segment, using <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify#surface-wrap-solidify">SurfaceWrapSolidify extension</a>.</p>
<p>If this does not work well then you can slightly modify this wrap solidify effect to allow it to take a model node as input (not a segment) and then it is almost sure that it will be able to fill all the holes nicely.</p>

---
