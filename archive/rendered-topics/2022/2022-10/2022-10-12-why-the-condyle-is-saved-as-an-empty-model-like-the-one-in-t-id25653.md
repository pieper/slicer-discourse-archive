# Why the condyle is saved as an empty model like the one in the photo below?

**Topic ID**: 25653
**Date**: 2022-10-12
**URL**: https://discourse.slicer.org/t/why-the-condyle-is-saved-as-an-empty-model-like-the-one-in-the-photo-below/25653

---

## Post #1 by @Moh_d_Al-Watary (2022-10-12 10:59 UTC)

<p>Dears in 3D Slicer community,<br>
could any one please help me in regard to this issue:<br>
I have segmented the mandibular condyle, but when save it is empty from inside (not solid) as you can see in the figure below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23581a46ae720adb60b0235be6ec083ce6ea9852.png" data-download-href="/uploads/short-url/52FtaCaoqIgALk5xcfZmVOEsZbk.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23581a46ae720adb60b0235be6ec083ce6ea9852_2_690x387.png" alt="image" data-base62-sha1="52FtaCaoqIgALk5xcfZmVOEsZbk" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23581a46ae720adb60b0235be6ec083ce6ea9852_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23581a46ae720adb60b0235be6ec083ce6ea9852_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23581a46ae720adb60b0235be6ec083ce6ea9852.png 2x" data-dominant-color="C1C3DD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1366×768 99.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I need it to be solid for further analysis that is not running correctly now due to this problem?<br>
Could you help me knowing what it is like this? how could I save it to be in solid form not empty one?<br>
Thank you in advance</p>

---

## Post #2 by @mau_igna_06 (2022-10-12 12:29 UTC)

<p>Please try the <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify#surface-wrap-solidify" rel="noopener nofollow ugc">WrapSolidify</a> effect.</p>
<p>You can add it to the segment editor by using the extensions manager.</p>
<p>Hope it helps</p>

---

## Post #3 by @wael_telha (2022-10-12 12:59 UTC)

<p>same problem i am facing , following the segmentation and the clipped condyle were saved as VTK but can not till now  can not do  SPHARM PDM- generator  it comes as an error</p>

---

## Post #4 by @wael_telha (2022-10-13 07:49 UTC)

<p>what should be the form of model that can be used with no error during SPHARM PDM-generator???</p>

---

## Post #5 by @mau_igna_06 (2022-10-13 11:07 UTC)

<p>Maybe the model should be watertight</p>
<p>Hope it helps</p>

---

## Post #6 by @wael_telha (2022-10-13 12:58 UTC)

<p>thanks a lot, dear for your help, I have tried using the wrapSolidify but unfortunately  the problem getting it further processed in SPHARM PDM- generator still persists</p>

---
