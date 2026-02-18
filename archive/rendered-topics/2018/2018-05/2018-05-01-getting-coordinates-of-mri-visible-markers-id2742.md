# Getting coordinates of MRI visible markers

**Topic ID**: 2742
**Date**: 2018-05-01
**URL**: https://discourse.slicer.org/t/getting-coordinates-of-mri-visible-markers/2742

---

## Post #1 by @Hanaana (2018-05-01 02:47 UTC)

<p>Hello Slicer community,</p>
<p>Hope you all are good. I am interested in getting the coordinates of MRI visible markers and their center points.  Do you have any idea how I can do this work?</p>
<p>Best,</p>
<p>Hanaa</p>

---

## Post #2 by @lassoan (2018-05-01 04:11 UTC)

<p>You can place markup fiducials at each marker position by clicking place button on the toolbar then clicking on the marker position in the image. You can see in Markups module list of point positions and you can also save the markup list as a csv file, which contains point position coordinates.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6ef033688c81e40f9261f10e666fd309aff98671.jpeg" data-download-href="/uploads/short-url/fPp9h8DVjlZ1DVKhfOTGFqoDtQt.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6ef033688c81e40f9261f10e666fd309aff98671_2_690x434.jpeg" alt="image" data-base62-sha1="fPp9h8DVjlZ1DVKhfOTGFqoDtQt" width="690" height="434" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6ef033688c81e40f9261f10e666fd309aff98671_2_690x434.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6ef033688c81e40f9261f10e666fd309aff98671_2_1035x651.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6ef033688c81e40f9261f10e666fd309aff98671_2_1380x868.jpeg 2x" data-dominant-color="AEAEAF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1869×1176 327 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Enable “Click to jump slices” option to jump to the markup selected in the list to allow fine-tuning of the position.</p>
<p>Also note that there are various landmark-based methods available in Slicer to align patient images or tools/devices. Let us know if you are interested in more details related to this.</p>

---
