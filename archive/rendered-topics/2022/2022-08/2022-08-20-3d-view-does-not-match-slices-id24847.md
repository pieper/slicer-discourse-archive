# 3D view does not match slices

**Topic ID**: 24847
**Date**: 2022-08-20
**URL**: https://discourse.slicer.org/t/3d-view-does-not-match-slices/24847

---

## Post #1 by @baptiste (2022-08-20 20:32 UTC)

<p>Hi.<br>
I am trying to register a CT scan to stereotaxic coordinates (where the AP plane passes through the ear canal and lower ridge of the eyes). When I align the 2D slices so that they are roughly in stereotaxic coordinates like below, the 3D view does not match the orientation of the slices. If I export segmented features to open it in a different software, let’s say in a CAD software, the orientation is wrong. Furthermore this error seems specific to orientations. Segmented areas are properly translated to (0,0,0) but the orientation is wrong. For example I drew a cross of the RGY axes of the slices, and you can see that the orientation of the cross is wrong when opened in meshlab. I used to be able to do that in 3D Slicer, am I forgetting to set an option correctly or is this a bug specific to the version of Slicer I have?<br>
Thanks.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/433feb1a7f9f75b8cf52f3dbeed77c6dcd017f86.jpeg" data-download-href="/uploads/short-url/9AUVY9m8z5CWpOklTw2xIfQZKEC.jpeg?dl=1" title="Screenshot from 2022-08-20 17-58-16" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/433feb1a7f9f75b8cf52f3dbeed77c6dcd017f86_2_541x500.jpeg" alt="Screenshot from 2022-08-20 17-58-16" data-base62-sha1="9AUVY9m8z5CWpOklTw2xIfQZKEC" width="541" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/433feb1a7f9f75b8cf52f3dbeed77c6dcd017f86_2_541x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/433feb1a7f9f75b8cf52f3dbeed77c6dcd017f86_2_811x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/433feb1a7f9f75b8cf52f3dbeed77c6dcd017f86.jpeg 2x" data-dominant-color="595963"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2022-08-20 17-58-16</span><span class="informations">998×921 81.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/747a5f73055e9c15cc8e4ddb6bce634cff77f195.png" data-download-href="/uploads/short-url/gCpzhYhoB4fPEHVzjTAEEyHOy0J.png?dl=1" title="Screenshot from 2022-08-20 18-12-49" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/747a5f73055e9c15cc8e4ddb6bce634cff77f195_2_617x499.png" alt="Screenshot from 2022-08-20 18-12-49" data-base62-sha1="gCpzhYhoB4fPEHVzjTAEEyHOy0J" width="617" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/747a5f73055e9c15cc8e4ddb6bce634cff77f195_2_617x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/747a5f73055e9c15cc8e4ddb6bce634cff77f195.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/747a5f73055e9c15cc8e4ddb6bce634cff77f195.png 2x" data-dominant-color="494983"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2022-08-20 18-12-49</span><span class="informations">906×734 100 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @baptiste (2022-09-08 11:48 UTC)

<p>Ok I figured out that the default views are now “reformat”, and not by default sagital, axial and coronal as they used to. This is visible in my screenshots from the cubes being in arbitrary orientations. This must have been introduced between the last time I used Slicer and now.<br>
When properly selecting the views everything works as expected.</p>

---

## Post #3 by @lassoan (2022-09-08 15:46 UTC)

<p>It is up to you if you prefer to align slice views to anatomical axes or image axes, by right-clicking on the “eye” icon of your CT image in Data module and check/uncheck “Reset view orientation on show”.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/67a01db7a094e4aa187e3ec61d880486bca8213c.png" data-download-href="/uploads/short-url/eMIe2YUUU1e5MN3G0lAcAgWPC2w.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67a01db7a094e4aa187e3ec61d880486bca8213c_2_690x380.png" alt="image" data-base62-sha1="eMIe2YUUU1e5MN3G0lAcAgWPC2w" width="690" height="380" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67a01db7a094e4aa187e3ec61d880486bca8213c_2_690x380.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/67a01db7a094e4aa187e3ec61d880486bca8213c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/67a01db7a094e4aa187e3ec61d880486bca8213c.png 2x" data-dominant-color="4C4E52"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">760×419 39.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Reset view orientation means that the slice view orientation will be reset to the volume’s axes when you show the volume.</p>

---
