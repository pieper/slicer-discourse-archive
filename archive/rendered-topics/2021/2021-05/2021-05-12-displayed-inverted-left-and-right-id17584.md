# displayed inverted left and right

**Topic ID**: 17584
**Date**: 2021-05-12
**URL**: https://discourse.slicer.org/t/displayed-inverted-left-and-right/17584

---

## Post #1 by @jhchoi (2021-05-12 06:37 UTC)

<p>I am working by importing the dicom file obtained through Rat’s heart micro ct. Unlike the actual captured image, like the screenshot, the 3d slicer’s working image is displayed inverted left and right. Is there a way to fix it?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/9330f921d799d7eb7230dc451c292f0d80152b83.jpeg" data-download-href="/uploads/short-url/l076ZcfByf4SUKmjatKzD9OB1Pd.jpeg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9330f921d799d7eb7230dc451c292f0d80152b83_2_690x373.jpeg" alt="1" data-base62-sha1="l076ZcfByf4SUKmjatKzD9OB1Pd" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9330f921d799d7eb7230dc451c292f0d80152b83_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9330f921d799d7eb7230dc451c292f0d80152b83_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9330f921d799d7eb7230dc451c292f0d80152b83_2_1380x746.jpeg 2x" data-dominant-color="A8A3AA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1920×1040 470 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-05-13 05:36 UTC)

<p>Slicer shows the images in the orientation that was specified during image acquisition. You can either <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#apply-transform-to-a-node">transform the volume to the correct orientation</a> or use Reformat module to change orientation of slice views (e.g., flip any slice view by any axis by applying 180deg rotation using LR/PA/IS sliders).</p>

---
