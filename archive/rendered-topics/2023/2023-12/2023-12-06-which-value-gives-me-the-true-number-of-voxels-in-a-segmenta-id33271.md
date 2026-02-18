# Which value gives me the true number of voxels in a segmentation segment?

**Topic ID**: 33271
**Date**: 2023-12-06
**URL**: https://discourse.slicer.org/t/which-value-gives-me-the-true-number-of-voxels-in-a-segmentation-segment/33271

---

## Post #1 by @jashrand (2023-12-06 23:07 UTC)

<p>I made a segmentation, and want to know the total number of voxels in the label I made.<br>
I right-clicked on the segmentation and chose “Calculate statistics…”</p>
<p>It gave me the statistics in the table, shown in the attached image here.<br>
However, there are two different values for the number of voxels.</p>
<pre><code class="lang-auto">Number of voxels [voxels] (1) :   577
Number of voxels [voxels] (2) :   699
</code></pre>
<p>Which of these values is the true number of voxels in my segment? And what is the difference between these two values?</p>
<p>Thanks!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea3b791d3ec718b778d39bc59fd53d63f9b6bfa9.jpeg" data-download-href="/uploads/short-url/xq79dibY7xk8ce2DUrJWOepADR7.jpeg?dl=1" title="Screen Shot 2023-12-06 at 4.33.06 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea3b791d3ec718b778d39bc59fd53d63f9b6bfa9_2_690x230.jpeg" alt="Screen Shot 2023-12-06 at 4.33.06 PM" data-base62-sha1="xq79dibY7xk8ce2DUrJWOepADR7" width="690" height="230" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea3b791d3ec718b778d39bc59fd53d63f9b6bfa9_2_690x230.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea3b791d3ec718b778d39bc59fd53d63f9b6bfa9_2_1035x345.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea3b791d3ec718b778d39bc59fd53d63f9b6bfa9_2_1380x460.jpeg 2x" data-dominant-color="8C8B82"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2023-12-06 at 4.33.06 PM</span><span class="informations">1932×646 156 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2023-12-06 23:10 UTC)

<p>You can find more information (e.g., which plugin computed the values) in the tooltip when you hover over the value in the table. Specification of all the computed values are available in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html">module’s documentation</a>.</p>

---

## Post #3 by @mikebind (2023-12-07 18:16 UTC)

<p>I noticed in the documentation that <a class="mention" href="/u/lassoan">@lassoan</a> linked that the count of the number of segment voxels as computed by the scalar volume statistics is limited to the spatial region where the scalar volume is defined, whereas the number of voxels as reported by the labelmap statistics is based on the count of the voxels in the binary labelmap for the segment.  If the segmentation geometry is the same as the scalar image volume geometry and the segment does not extend outside the scalar image region, then these two counts should be identical.  However, they will differ if the segment extends outside of the scalar image volume.  Is it possible that your segment is partially outside of the image volume?</p>

---

## Post #4 by @jashrand (2023-12-08 20:46 UTC)

<p>Yes, I think that was the issue. Thanks for helping me figure that out!</p>

---
