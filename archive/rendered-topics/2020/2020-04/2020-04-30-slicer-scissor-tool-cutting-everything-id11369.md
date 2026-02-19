---
topic_id: 11369
title: "Slicer Scissor Tool Cutting Everything"
date: 2020-04-30
url: https://discourse.slicer.org/t/11369
---

# Slicer Scissor Tool Cutting everything

**Topic ID**: 11369
**Date**: 2020-04-30
**URL**: https://discourse.slicer.org/t/slicer-scissor-tool-cutting-everything/11369

---

## Post #1 by @fullerkj (2020-04-30 18:46 UTC)

<p>I have segmented and registered two images to one another as attached, but would like to cut the moving image segmentation as well as the fixed image down to just two vertebrae, however the moving segmentation when I try using the scissor tool cuts everything (the whole segmentation) while the other segmentation (the fixed image) cuts normally.</p>
<p>Has anyone else seen this issue or know how to resolve this? I assume it may have something to do with registering the image so I’ve also put how I registered the images together below in case it has something to do with it:</p>
<ul>
<li>Fiducial Registration (Translation)-&gt; General Registration (Rigid 6DOF)-&gt;Deformable Registration (Brains DEMONS - linear using floats)</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/89464be4ebc0327b3213d711c1053b43cd640fa5.jpeg" data-download-href="/uploads/short-url/jAo1q7ZeLOHbRodmgYFKG93WPpb.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89464be4ebc0327b3213d711c1053b43cd640fa5_2_690x328.jpeg" alt="image" data-base62-sha1="jAo1q7ZeLOHbRodmgYFKG93WPpb" width="690" height="328" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89464be4ebc0327b3213d711c1053b43cd640fa5_2_690x328.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89464be4ebc0327b3213d711c1053b43cd640fa5_2_1035x492.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/9/89464be4ebc0327b3213d711c1053b43cd640fa5_2_1380x656.jpeg 2x" data-dominant-color="9E9BA0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1622×773 340 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-04-30 18:56 UTC)

<p>There are limitations in editing of a segmentation node that is under a dynamically applied non-linear transform. I would recommend to harden the transformation on the segmentation in Transforms module before starting editing.</p>

---

## Post #3 by @fullerkj (2020-05-01 14:19 UTC)

<p>Thank you so much! That worked.</p>

---
