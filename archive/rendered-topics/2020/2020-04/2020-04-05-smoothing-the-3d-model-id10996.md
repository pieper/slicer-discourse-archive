# Smoothing the 3D model

**Topic ID**: 10996
**Date**: 2020-04-05
**URL**: https://discourse.slicer.org/t/smoothing-the-3d-model/10996

---

## Post #1 by @Angel (2020-04-05 01:40 UTC)

<p>Hi,</p>
<p>I am new to Slicer and I am trying to use it to model a chicken embryo heart affected by Tetralogy of Fallot. I have been looking into the smoothing options in Segment Editor and I have watched the tutorials, but it is not making the components of the 3D model any smoother. How can I properly refine and smooth my model?</p>
<p>I would appreciate any help!</p>

---

## Post #2 by @lassoan (2020-04-05 01:42 UTC)

<p>You probably need to oversample your input volume before you start segmentation. You can do it using Crop volume module, by setting Space scaling to a value &lt; 1.0 (for example, 0.5 or maybe 0.3). See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation">tutorials</a> for step-by-step instructions.</p>

---

## Post #3 by @Angel (2020-04-05 22:16 UTC)

<p>Hello,</p>
<p>Thank you for responding. However, setting the space scaling value below 1 kept making the system crash. Is there any other reason why the smoothing is not affecting the 3D model?</p>
<p>Thanks</p>

---

## Post #4 by @lassoan (2020-04-05 22:29 UTC)

<p>Resampling the volume at higher resolution requires more memory and your default system configuration may need to be adjusted to have more virtual memory space. You can try keeping 1.0 scale and just force isotropic spacing.</p>
<p>If course without seeing your images we can only guess what’s happening. Could you attach a few screenshots?</p>

---

## Post #6 by @lassoan (2020-04-07 22:59 UTC)

<p>I assumed you wanted to smooth staircase artifacts, that’s why I recommended resampling. This image already has very decent resolution, so there is no need for oversampling.</p>
<p>Instead, you can use Smoothing effect (try joint smoothing method first, and if it is not good enough then try all the others).</p>
<p>You may also use anisotropic smoothing filters on the input image before starting segmentation (in modules: Filtering / Denoising) or if you use Slicer-4.10.x then you can try filters provided by <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/AnomalousFilters">AnomalousFilters extension</a>.</p>

---

## Post #7 by @Angel (2020-04-07 23:54 UTC)

<p>Thank you so much for your help! I’m excited to try the extension.</p>

---
