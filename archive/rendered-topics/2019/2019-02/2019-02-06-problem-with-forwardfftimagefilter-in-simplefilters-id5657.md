# Problem with ForwardFFTImageFilter in SimpleFilters

**Topic ID**: 5657
**Date**: 2019-02-06
**URL**: https://discourse.slicer.org/t/problem-with-forwardfftimagefilter-in-simplefilters/5657

---

## Post #1 by @torquil (2019-02-06 10:18 UTC)

<p>Hi!</p>
<p>In an attempt to determine the real 3d resolution of an X-ray scan, I’m tried to use the ForwardFFTImageFilter function in the SimpleFilters module, but I’m getting an error message saying that it does not support 32-bit signed integers:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7ffc6f8293cc1ee565165841278f0fbd6b3d7db5.png" alt="slicer_forward_fft_bug" data-base62-sha1="igdtJbm1Elluvt2yZAnDjdGhHOR" width="525" height="165"></p>
<p>Is this a bug, or do I need to convert to pixel values to something that this filter supports first?</p>
<p>Best regards,<br>
Torquil Sørensen</p>

---

## Post #2 by @lassoan (2019-02-06 16:31 UTC)

<p>The error message tells that 32-bit signed integer voxel type is not supported by the selected filter. You can use “Cast scalar volume” module to change the voxel type.</p>

---

## Post #3 by @pieper (2019-02-06 16:36 UTC)

<p>See this line:</p>
<p><code>This filter works only for real single-component input image types</code></p>
<p>from <a href="https://itk.org/Doxygen/html/classitk_1_1ForwardFFTImageFilter.html" rel="nofollow noopener">https://itk.org/Doxygen/html/classitk_1_1ForwardFFTImageFilter.html</a></p>

---
