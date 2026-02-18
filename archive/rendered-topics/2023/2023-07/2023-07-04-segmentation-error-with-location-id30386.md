# Segmentation error with location

**Topic ID**: 30386
**Date**: 2023-07-04
**URL**: https://discourse.slicer.org/t/segmentation-error-with-location/30386

---

## Post #1 by @mohammed_alshakhas (2023-07-04 08:08 UTC)

<p>I did this segmentation. however, the position  is incorrect as in the picture</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/0417930b349a24d022a863a0dad14673c3be34b6.jpeg" data-download-href="/uploads/short-url/AcpTWoLwAxbHx0TtdbEUM8UhUy.jpeg?dl=1" title="Screenshot 2023-07-04 at 11.05.14" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/0417930b349a24d022a863a0dad14673c3be34b6_2_690x448.jpeg" alt="Screenshot 2023-07-04 at 11.05.14" data-base62-sha1="AcpTWoLwAxbHx0TtdbEUM8UhUy" width="690" height="448" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/0417930b349a24d022a863a0dad14673c3be34b6_2_690x448.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/0417930b349a24d022a863a0dad14673c3be34b6_2_1035x672.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/0417930b349a24d022a863a0dad14673c3be34b6_2_1380x896.jpeg 2x" data-dominant-color="A7A7A8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-07-04 at 11.05.14</span><span class="informations">3024×1964 276 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2023-07-04 15:10 UTC)

<p>It looks like you have a coordinate system issue.  please describe the steps you took and provide sample data so people can help you sort this out.</p>

---

## Post #3 by @lassoan (2023-07-04 15:57 UTC)

<p>Most likely you have applied a warping transform on the volume. It is a <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumerendering.html#limitations">limitation</a> of Volume Rendering module that non-linear transform must be hardened on the image to make it appear in correct position.</p>

---

## Post #4 by @mohammed_alshakhas (2023-07-14 08:44 UTC)

<p>i actually didn’t do anything, i just uploaded a file and segmented as my routine workflow.</p>

---

## Post #5 by @lassoan (2023-07-14 13:17 UTC)

<p>Can you take a screenshot of your Data module to see what volumes you have in your scene and if any transforms were automatically added?</p>

---
