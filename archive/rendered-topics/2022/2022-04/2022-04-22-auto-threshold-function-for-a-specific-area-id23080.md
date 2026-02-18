# Auto threshold function for a specific area?

**Topic ID**: 23080
**Date**: 2022-04-22
**URL**: https://discourse.slicer.org/t/auto-threshold-function-for-a-specific-area/23080

---

## Post #1 by @Jinny_Lee (2022-04-22 02:34 UTC)

<p>Hi,</p>
<p>I’m trying to segment a specific area from an FDG PET image and use the “Automatic threshold” function to get an automatic value from the selected area.</p>
<p>I’ve tried using the “Masking” function but it didn’t work because even when I select “Inside Segment_1” for “Editable area”, the automatic threshold would always give me the values for the entire image.</p>
<p>Does anyone know how to get a threshold value from a selected area of an image? Please let me know if you have experienced the same problem.</p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2022-04-23 05:17 UTC)

<p>The threshold preview applies for the entire displayed area of the image, but when you click “Apply” only those regions get filled that are inside the editable area.</p>

---

## Post #3 by @Jinny_Lee (2022-04-27 00:27 UTC)

<p>Hi,</p>
<p>thank you for your reply.</p>
<p>We have been trying clicking Apply button previously but it only showed the values for the entire image. Do you think it could an technical issue for the 3D slicer program?</p>

---

## Post #4 by @lassoan (2022-05-02 22:27 UTC)

<p>I see what you mean now. It is not a bug, auto-threshold is computed for the entire image. You can use mask volume to blank out image regions if you want to exclude some parts of the image from affecting the threshold computation. If you want to use a box-shaped region then you can use Crop volume module to create a volume that only contains that region, and use it as master volume when you compute the automatic threshold.</p>
<p>If you want to set the threshold from a histogram computed from a specific image region then you can use the <code>Local histogram</code> section. It allows you to define a region by click-and-drag in any of the slice views and use automatic minimum, mean, maximum, or manually-defined lower/medium/upper values on the histogram to set the threshold range:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c33e1374ac84bfb728ff64186f64440bfd637a5.png" data-download-href="/uploads/short-url/hIKmcS3X2QJtN5BtDeAd2onmrit.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c33e1374ac84bfb728ff64186f64440bfd637a5_2_690x371.png" alt="image" data-base62-sha1="hIKmcS3X2QJtN5BtDeAd2onmrit" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c33e1374ac84bfb728ff64186f64440bfd637a5_2_690x371.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c33e1374ac84bfb728ff64186f64440bfd637a5_2_1035x556.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c33e1374ac84bfb728ff64186f64440bfd637a5_2_1380x742.png 2x" data-dominant-color="A3A5A1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2050×1104 485 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
