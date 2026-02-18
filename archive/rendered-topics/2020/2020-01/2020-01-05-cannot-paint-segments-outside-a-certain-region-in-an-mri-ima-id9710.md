# Cannot paint segments outside a certain region in an MRI image

**Topic ID**: 9710
**Date**: 2020-01-05
**URL**: https://discourse.slicer.org/t/cannot-paint-segments-outside-a-certain-region-in-an-mri-image/9710

---

## Post #1 by @momosukh (2020-01-05 03:40 UTC)

<p>I am facing a weird issue, I am unable to paint the layer of the outer abdomen, fat, using paint, draw, and other techniques, as shown as the red circle in the figure. The ROI of the area is well spaced in all 3 coordinates.</p>
<p>I would request if anyone can help me or guide me to get out of this glitch or error.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffecd179ce38c8c76a59fe2f217a40eba1ea2ec6.png" data-download-href="/uploads/short-url/Aw18pQGfbkfs95AVNz0DFLD3Jk2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ffecd179ce38c8c76a59fe2f217a40eba1ea2ec6_2_690x466.png" alt="image" data-base62-sha1="Aw18pQGfbkfs95AVNz0DFLD3Jk2" width="690" height="466" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ffecd179ce38c8c76a59fe2f217a40eba1ea2ec6_2_690x466.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ffecd179ce38c8c76a59fe2f217a40eba1ea2ec6_2_1035x699.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffecd179ce38c8c76a59fe2f217a40eba1ea2ec6.png 2x" data-dominant-color="918C8F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1340×905 196 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-01-05 04:07 UTC)

<p>This is because the segmentation’s geometry (including the extents) is set to the master volume by default. Click the button on the right side of the master volume node selector in Segment Editor module to define segmentation geometry based on a different node.</p>
<p>Your screenshots indicate that slice spacing is about 5-10x larger than in-slice image resolution (your volume is made up of long sticks instead of cubes). To be able to produce high-quality segmentation, you need to set segmentation geometry to be isotropic (approximately same spacing value along each all three axes).</p>

---
