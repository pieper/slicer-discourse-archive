# Model registration from fiducial point

**Topic ID**: 25462
**Date**: 2022-09-28
**URL**: https://discourse.slicer.org/t/model-registration-from-fiducial-point/25462

---

## Post #1 by @jegberink (2022-09-28 09:20 UTC)

<p>Hello everyone,</p>
<p>I’ve overlapped a preoperative femur and postoperative femur, where the femoral head position was changed. I’ve overlapped them using ALPACA to measure the rotations and translations.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/995648eaec25bb9b8215a3f28f3184b00044bade.png" data-download-href="/uploads/short-url/lStUSqmW7K9soeKzAJqavQGTuWO.png?dl=1" title="before" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/995648eaec25bb9b8215a3f28f3184b00044bade_2_417x500.png" alt="before" data-base62-sha1="lStUSqmW7K9soeKzAJqavQGTuWO" width="417" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/995648eaec25bb9b8215a3f28f3184b00044bade_2_417x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/9/995648eaec25bb9b8215a3f28f3184b00044bade_2_625x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/995648eaec25bb9b8215a3f28f3184b00044bade.png 2x" data-dominant-color="9D95C4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">before</span><span class="informations">657×786 78.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27f452e2876d9cbe0757bdb41d2d551ee8be032d.png" data-download-href="/uploads/short-url/5Hs57xVAPtBBerpDL7v4rvRRupv.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27f452e2876d9cbe0757bdb41d2d551ee8be032d_2_332x500.png" alt="image" data-base62-sha1="5Hs57xVAPtBBerpDL7v4rvRRupv" width="332" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27f452e2876d9cbe0757bdb41d2d551ee8be032d_2_332x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/7/27f452e2876d9cbe0757bdb41d2d551ee8be032d_2_498x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/7/27f452e2876d9cbe0757bdb41d2d551ee8be032d.png 2x" data-dominant-color="9C93C3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">513×771 84.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Now i managed to use the “rotate a node around a specified point” script to be able to rotate the head from a point relative to its shaft, so we have a singular point to measure from with other patients.</p>
<p>However, i can not figure out how to measure the ALPACA overlap from this new point, is there a way to do this.</p>
<p>Thank you in advance.</p>

---
