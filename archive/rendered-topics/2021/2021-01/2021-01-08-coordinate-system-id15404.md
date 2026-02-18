# Coordinate system

**Topic ID**: 15404
**Date**: 2021-01-08
**URL**: https://discourse.slicer.org/t/coordinate-system/15404

---

## Post #1 by @danila (2021-01-08 13:51 UTC)

<p>Hi,<br>
I have an STL file of a virtual surgical planning and I would like to compare it with the 3D model, obtained from a post-operative CBCT. The goal is to evaluate the accuracy of the VSP.</p>
<p>When I load the two files (STL and vtk) in 3D slicer, I suppose they have a different coordinate system, because I get this situation:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/152d0ae44c9e1680111ef08d0ba657ee2f0d381c.jpeg" data-download-href="/uploads/short-url/31kwRF7SyAuNMxEc85liBUvJvbK.jpeg?dl=1" title="slicer coordinate" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/152d0ae44c9e1680111ef08d0ba657ee2f0d381c_2_690x387.jpeg" alt="slicer coordinate" data-base62-sha1="31kwRF7SyAuNMxEc85liBUvJvbK" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/152d0ae44c9e1680111ef08d0ba657ee2f0d381c_2_690x387.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/152d0ae44c9e1680111ef08d0ba657ee2f0d381c_2_1035x580.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/152d0ae44c9e1680111ef08d0ba657ee2f0d381c.jpeg 2x" data-dominant-color="BFC1DC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer coordinate</span><span class="informations">1366×768 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>How can I solve this problem?</p>
<p>Thank you in advance for your help</p>

---

## Post #2 by @lassoan (2021-01-08 16:17 UTC)

<p>The imaging technologist can choose the image origin for each CT/CBCT scan. Unless there is a strict imaging protocol in place, you typically end up with not well aligned images. So, if the two models are created from two different scans then what you see is normal.</p>
<p>If you want to make the models easier to compare then you can register them using any of the registration methods available in Slicer. For details, see <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html" class="inline-onebox">Registration — 3D Slicer documentation</a>.</p>

---
