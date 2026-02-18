# Slicer.util.array: format, grayscale and RGB

**Topic ID**: 4312
**Date**: 2018-10-07
**URL**: https://discourse.slicer.org/t/slicer-util-array-format-grayscale-and-rgb/4312

---

## Post #1 by @virginia_fgc (2018-10-07 22:57 UTC)

<p>Hello,</p>
<p>I am using the Python console to create a script that handles my imported image as an array thanks to:<br>
<code>image = slicer.util.array('T2IMAGE')</code></p>
<p>The image is in an ‘nrrd’ format, and it’s a T2 weighted MR acquisition. When I use the above clause, I get a 4x256x256 array (dimensions are correct: there are 4 slices with a 256x256 resolution), but I do not understand the values themselves.</p>
<p>I have noticed that the minimum value is 0 and the maximum value is 32767 (using image.max() and image.min()). How does Slicer reads ‘nrrd’ files?</p>
<p>In addition to that doubt, I have the following issue: the image is supposed to be a grayscale image, but I need to change the value of some pixels to a <strong>color</strong> . Hence, is there a way to handle that grayscale image as an RGB?</p>
<p>Thank you very much for any suggestion.<br>
Kind regards,</p>
<p>Virginia</p>

---

## Post #2 by @lassoan (2018-10-08 04:03 UTC)

<aside class="quote no-group" data-username="virginia_fgc" data-post="1" data-topic="4312">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/virginia_fgc/48/3309_2.png" class="avatar"> virginia_fgc:</div>
<blockquote>
<p>I have noticed that the minimum value is 0 and the maximum value is 32767 (using image.max() and image.min()).</p>
</blockquote>
</aside>
<p>This behavior is probably incorrect. Most likely the software that created this nrrd image used incorrect byte ordering (endianness). How did you create the nrrd file?</p>
<aside class="quote no-group" data-username="virginia_fgc" data-post="1" data-topic="4312">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/virginia_fgc/48/3309_2.png" class="avatar"> virginia_fgc:</div>
<blockquote>
<p>In addition to that doubt, I have the following issue: the image is supposed to be a grayscale image, but I need to change the value of some pixels to a <strong>color</strong> .</p>
</blockquote>
</aside>
<p>When you segment a volume by “painting” voxels you don’t change voxels of the original volume node but you modify segmentation node overlaid on the original volume, using <a href="https://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html">Segment Editor module</a>.</p>

---
