# Create contour and volume

**Topic ID**: 21422
**Date**: 2022-01-12
**URL**: https://discourse.slicer.org/t/create-contour-and-volume/21422

---

## Post #1 by @BORIPHAT (2022-01-12 12:56 UTC)

<p>Dear Developers and users,</p>
<p>Hello, My goal is to compare the breast deformation between CBCT Set 1 and Set 2. I will create the volume of the breast for comparing to get the results, such as volume difference, HD, and DVF.</p>
<p>I would like to create a contour of the breast area in CBCT image set 1 and transfer this contour to CBCT image set 2 for the same situation. Previously, I tried to use the surface cut tool  from the segment editor, but it is difficult to create the line following the breast surface. Could you please give me some advice?</p>
<p>Thank you very much for your help.</p>

---

## Post #2 by @BORIPHAT (2022-01-18 07:04 UTC)

<p>Dear Developers and users,</p>
<p>Hello, When I create the volume between data sets 1 and 2, the volume on the other side is not the same.So when I compare the results, they also show the differences on the other sides. Could you please give me some advice? How to compare only the surface of the breast area? Thank you very much.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/94092daeb3a19c2fb9711070098392269c2147fe.png" data-download-href="/uploads/short-url/l7AktTFex238VXdsX8wH0nSESe2.png?dl=1" title="Picture1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/94092daeb3a19c2fb9711070098392269c2147fe_2_643x500.png" alt="Picture1" data-base62-sha1="l7AktTFex238VXdsX8wH0nSESe2" width="643" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/4/94092daeb3a19c2fb9711070098392269c2147fe_2_643x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/94092daeb3a19c2fb9711070098392269c2147fe.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/94092daeb3a19c2fb9711070098392269c2147fe.png 2x" data-dominant-color="8B8481"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Picture1</span><span class="informations">808×628 176 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/5674d5ca2ea1ecb67347b78e903faa683e0e477d.png" data-download-href="/uploads/short-url/ckPnANxq2hddzkTvpubiq7cPKB7.png?dl=1" title="Picture2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/5674d5ca2ea1ecb67347b78e903faa683e0e477d_2_690x340.png" alt="Picture2" data-base62-sha1="ckPnANxq2hddzkTvpubiq7cPKB7" width="690" height="340" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/5674d5ca2ea1ecb67347b78e903faa683e0e477d_2_690x340.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/5674d5ca2ea1ecb67347b78e903faa683e0e477d.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/5674d5ca2ea1ecb67347b78e903faa683e0e477d.png 2x" data-dominant-color="3D4343"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Picture2</span><span class="informations">986×487 167 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @BORIPHAT (2022-01-19 03:23 UTC)

<p>Dear Prof. <a class="mention" href="/u/lassoan">@lassoan</a> Could you please give me some advice? Thank you very much.</p>

---

## Post #4 by @lassoan (2022-03-13 04:19 UTC)

<p>You can <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html#semi-automatic-registration">register the volumes based on matching anatomical landmarks</a>. After that if you cut off the other side using the same plane or ROI then there will be no differences there.</p>
<p>In the very latest Slicer Preview Release you can now use the improved Curve cut tool in Dynamic  modeler module to robustly cut out regions from surfaces.</p>

---

## Post #5 by @BORIPHAT (2022-04-05 08:28 UTC)

<p>Thank you very much for your help.</p>

---
