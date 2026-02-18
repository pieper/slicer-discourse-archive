# Bugs with ROI - Red panes or panes with text

**Topic ID**: 45788
**Date**: 2026-01-15
**URL**: https://discourse.slicer.org/t/bugs-with-roi-red-panes-or-panes-with-text/45788

---

## Post #1 by @marklumberjack (2026-01-15 20:46 UTC)

<p>I’m new here so I’m not sure if I’m even using everything correctly, but I’m experiencing some bugs when using ROI clipping on an image stack volume.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/1278a56971f9dfac0e6eba9ccb9c3dd2d355807d.jpeg" data-download-href="/uploads/short-url/2Dp4OpJqx3KsSAxzYdBrAb0GspL.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/1278a56971f9dfac0e6eba9ccb9c3dd2d355807d_2_690x308.jpeg" alt="image" data-base62-sha1="2Dp4OpJqx3KsSAxzYdBrAb0GspL" width="690" height="308" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/1278a56971f9dfac0e6eba9ccb9c3dd2d355807d_2_690x308.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/1278a56971f9dfac0e6eba9ccb9c3dd2d355807d_2_1035x462.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/1278a56971f9dfac0e6eba9ccb9c3dd2d355807d_2_1380x616.jpeg 2x" data-dominant-color="463031"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×859 272 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/03dbf7349ea04b8f5d2a505dddb9c507a65c47ce.jpeg" data-download-href="/uploads/short-url/y8HOj6pflG19nVuTchC5fX1vGu.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/03dbf7349ea04b8f5d2a505dddb9c507a65c47ce_2_690x428.jpeg" alt="image" data-base62-sha1="y8HOj6pflG19nVuTchC5fX1vGu" width="690" height="428" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/03dbf7349ea04b8f5d2a505dddb9c507a65c47ce_2_690x428.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/03dbf7349ea04b8f5d2a505dddb9c507a65c47ce_2_1035x642.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/03dbf7349ea04b8f5d2a505dddb9c507a65c47ce.jpeg 2x" data-dominant-color="8486AF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1086×675 184 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2026-01-15 23:11 UTC)

<p>That looks very odd, like the GPU texture got corrupted.  What kind of data is it?  Try different computers and see if you get the same result.  Share sample data to see if others can reproduce this.</p>

---
