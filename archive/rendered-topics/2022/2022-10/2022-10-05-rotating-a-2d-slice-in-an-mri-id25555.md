# Rotating a 2D slice in an MRI

**Topic ID**: 25555
**Date**: 2022-10-05
**URL**: https://discourse.slicer.org/t/rotating-a-2d-slice-in-an-mri/25555

---

## Post #1 by @gregpietsch (2022-10-05 05:40 UTC)

<p>I am new to slicer and have been learning how to look at images and perform segmentation.  The canine brain studies I have been working with display the images in a dorsally recumbent position which is the opposite position from the various atlases I have looked at.</p>
<p>How do I rotate these images 180 degrees so they are in the same orientation as the brain atlas I am consulting?  I have attached a screen shot of the current view I have.</p>
<p>Thanks!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf1e5d621902dfaedab3479ea7e3450f15ebcdf9.jpeg" data-download-href="/uploads/short-url/rgIfGT6uWOmpN6wF2Erp1veaBRv.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf1e5d621902dfaedab3479ea7e3450f15ebcdf9_2_690x368.jpeg" alt="image" data-base62-sha1="rgIfGT6uWOmpN6wF2Erp1veaBRv" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf1e5d621902dfaedab3479ea7e3450f15ebcdf9_2_690x368.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf1e5d621902dfaedab3479ea7e3450f15ebcdf9_2_1035x552.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf1e5d621902dfaedab3479ea7e3450f15ebcdf9_2_1380x736.jpeg 2x" data-dominant-color="5D5C5C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1922×1026 195 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @justomont (2022-10-05 09:50 UTC)

<p>You could use the Transforms Module.</p>
<p>For that, create a new Linear Transform and (I’m assuming that the image you show in the screenshot is an axial view) set the Rotation LR to 180º. Finally, apply the transform to the desired volume. Note that the rest of the views will also rotate accordingly, so you might also change the rotation values for PA and IS.</p>

---

## Post #3 by @gregpietsch (2022-10-05 19:16 UTC)

<p>Thanks!  That worked great!</p>

---
