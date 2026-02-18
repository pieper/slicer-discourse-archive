# Apply a ROI on another series of images

**Topic ID**: 26233
**Date**: 2022-11-14
**URL**: https://discourse.slicer.org/t/apply-a-roi-on-another-series-of-images/26233

---

## Post #1 by @kylin (2022-11-14 14:27 UTC)

<p>I have drawn a ROI on the contrast enhanced T1 MR images, and I’d like to apply this ROI on the corresponding T1 MR images of the same patient. How to achieve this goal in 3D slicer?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c49adff1fc743c0ac704770c0804c616afd73436.jpeg" data-download-href="/uploads/short-url/s3foUVHzug7u277LN3gUsfC8LSC.jpeg?dl=1" title="无标题" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c49adff1fc743c0ac704770c0804c616afd73436_2_690x277.jpeg" alt="无标题" data-base62-sha1="s3foUVHzug7u277LN3gUsfC8LSC" width="690" height="277" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c49adff1fc743c0ac704770c0804c616afd73436_2_690x277.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/4/c49adff1fc743c0ac704770c0804c616afd73436_2_1035x415.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c49adff1fc743c0ac704770c0804c616afd73436.jpeg 2x" data-dominant-color="6F716F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">无标题</span><span class="informations">1069×430 71.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2022-11-14 14:34 UTC)

<p>What do you mean by <em>applying</em> the segment (this is how free-form segmented regions are referred to in Slicer, see <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#glossary">glossary</a>) to another image?</p>
<ul>
<li>Do you want to blank out the image inside or outside the segment? You can do that using Mask volume effect.</li>
<li>Would you like to get that segment as a labelmap image that matches the geometry of the other MR image? You can do that by exporting the segmentation to labelmap using the other image as reference.</li>
<li>Transfer the segmentation to the other image? You can do that by spatially registering the two volumes using Elastix or ANTs extensions.</li>
<li>Something else?</li>
</ul>

---

## Post #3 by @kylin (2022-11-15 05:14 UTC)

<p>Thank you very much!!</p>

---
