---
topic_id: 9085
title: "Segmentation Gaps Fill In For Bone Model"
date: 2019-11-08
url: https://discourse.slicer.org/t/9085
---

# Segmentation gaps fill in for bone model

**Topic ID**: 9085
**Date**: 2019-11-08
**URL**: https://discourse.slicer.org/t/segmentation-gaps-fill-in-for-bone-model/9085

---

## Post #1 by @mccarthyvetsurg (2019-11-08 16:02 UTC)

<p>Attached is a screen shot of a project I have been working on.  My goal is to segment the sacrum.  I am trying to achieve a filled in bone model and I have pain stakingly been going through with paint to paint all of the defects within the bone, as you can see in the screen shot.</p>
<p>Is there anyway to “auto fill” in these segments that are only limited to the cortical circumference of the bone? I know there is a masking option, however, I still have to scroll through and paint even on 3d it takes a while.  Thanks.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6aad686c50657dac77d3e68f82691b77b17310fa.jpeg" data-download-href="/uploads/short-url/fdI8t2ddpOYVEUR0mqgfPIJIP8e.jpeg?dl=1" title="Screen%20Shot%20editing" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6aad686c50657dac77d3e68f82691b77b17310fa_2_690x406.jpeg" alt="Screen%20Shot%20editing" data-base62-sha1="fdI8t2ddpOYVEUR0mqgfPIJIP8e" width="690" height="406" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6aad686c50657dac77d3e68f82691b77b17310fa_2_690x406.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6aad686c50657dac77d3e68f82691b77b17310fa_2_1035x609.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6aad686c50657dac77d3e68f82691b77b17310fa_2_1380x812.jpeg 2x" data-dominant-color="A4A7A7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen%20Shot%20editing</span><span class="informations">1465×864 297 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2019-11-08 17:46 UTC)

<p>There are many useful tips for this problem on this forum (you can search for bone segmentation).</p>
<p>A fully automatic solution has been added recently, I would recommend to try that first: install Slicer Preview Release and <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify">SurfaceWrapSolidify</a> extension. Use Segment Editor module, Wrap Solidify effect, choose Filter method: Deep hull, Output type: Segmentation.</p>
<p><a class="mention" href="/u/sandress">@sandress</a>: There seems to be a great interest in your extension. Please update its GUI to make it more intuitive so that people can figure out how to use it successfully. If you don’t have the time then let us know.</p>

---

## Post #3 by @Leon (2019-11-08 18:55 UTC)

<p>Just a small tip.<br>
From what I see in the image you send there is a some noise in your CT that may effect your segmentation. My advice would be to filter that out (use the Simple Filter module). I personally prefer the CurvatureAnisotropicDiffusionImageFilter.</p>

---
