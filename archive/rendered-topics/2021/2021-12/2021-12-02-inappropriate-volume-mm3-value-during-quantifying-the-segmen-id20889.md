# Inappropriate volume mm3 value during quantifying the segments

**Topic ID**: 20889
**Date**: 2021-12-02
**URL**: https://discourse.slicer.org/t/inappropriate-volume-mm3-value-during-quantifying-the-segments/20889

---

## Post #1 by @rupadevim (2021-12-02 17:51 UTC)

<p>Steps which I have followed to process in 3D slicer:</p>
<ol>
<li>
<p>When I loaded the nii file in 3d slicer, the brain image was displayed upside down.</p>
</li>
<li>
<p>Rotated the image using linear transform.</p>
</li>
<li>
<p>Segmented the region of interest (Hemispheric volume) using segment editor.</p>
</li>
<li>
<p>Quantified the segmented hemispheric volume using segment statistics.</p>
</li>
<li>
<p>But the volume mm3 (6.71646e+09) is not the right one.</p>
</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40088f625cf36b66a01106b9c552bf64d19b24c4.jpeg" data-download-href="/uploads/short-url/98sTG0XUOyA4sZtHBpDixLtjGmM.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/40088f625cf36b66a01106b9c552bf64d19b24c4_2_690x376.jpeg" alt="image" data-base62-sha1="98sTG0XUOyA4sZtHBpDixLtjGmM" width="690" height="376" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/40088f625cf36b66a01106b9c552bf64d19b24c4_2_690x376.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/40088f625cf36b66a01106b9c552bf64d19b24c4_2_1035x564.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/40088f625cf36b66a01106b9c552bf64d19b24c4_2_1380x752.jpeg 2x" data-dominant-color="828184"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1770×966 201 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Help me to sort this problem.<br>
Thank you</p>

---

## Post #2 by @pieper (2021-12-02 18:15 UTC)

<p>If the data loads upside down with the wrong spacing it probably comes from some source that does not keep track of the image geometry.  Look in the Volumes module and set the spacing to whatever the correct values are.  Also be careful with left/right measurements with this data as it may not be clear (or recorded) whether there has been a rotation vs. a flip.</p>

---
