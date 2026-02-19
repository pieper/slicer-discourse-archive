---
topic_id: 42484
title: "I Want To Increase The Thickness Height Of This Slice For 3D"
date: 2025-04-08
url: https://discourse.slicer.org/t/42484
---

# I want to increase the thickness / height of this slice for 3d printing and also i want to reduce the file , the file size is 79mb , i want 20mb

**Topic ID**: 42484
**Date**: 2025-04-08
**URL**: https://discourse.slicer.org/t/i-want-to-increase-the-thickness-height-of-this-slice-for-3d-printing-and-also-i-want-to-reduce-the-file-the-file-size-is-79mb-i-want-20mb/42484

---

## Post #1 by @Vikram (2025-04-08 06:44 UTC)

<p>I want to increase the thickness / height of this slice for 3d printing and also i want to reduce the file , the file size is 79mb , i want 20mb .<br>
Can you please help me how i can increase the height of slice and also reduce the mb size.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db3a970cb6dd2ad5aab66605bf70af14f9fa8a5c.png" data-download-href="/uploads/short-url/vho5RF5IpSJWDLE2WmwSGVprvs0.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db3a970cb6dd2ad5aab66605bf70af14f9fa8a5c_2_690x343.png" alt="image" data-base62-sha1="vho5RF5IpSJWDLE2WmwSGVprvs0" width="690" height="343" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db3a970cb6dd2ad5aab66605bf70af14f9fa8a5c_2_690x343.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db3a970cb6dd2ad5aab66605bf70af14f9fa8a5c_2_1035x514.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db3a970cb6dd2ad5aab66605bf70af14f9fa8a5c_2_1380x686.png 2x" data-dominant-color="CDD1E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1852×922 84.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2025-04-08 15:02 UTC)

<p>You can apply a transform to the model in Transforms module that changes the scale of the model. Scaling factors are in the diagonal of the transformation matrix.</p>
<p>You can decrease the size of a mesh using Surface Toolbox module (decimate or remesh).</p>

---
