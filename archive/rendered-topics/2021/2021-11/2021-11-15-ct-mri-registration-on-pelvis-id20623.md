# CT / MRI Registration on pelvis

**Topic ID**: 20623
**Date**: 2021-11-15
**URL**: https://discourse.slicer.org/t/ct-mri-registration-on-pelvis/20623

---

## Post #1 by @Vincebisca (2021-11-15 10:50 UTC)

<p>Hello,</p>
<p>I am seeking some help on the available features for automatic image registration involving CT + MRI images. I am searching a way on 3D Slicer to align 2 stacks of images, one being a CT, the other a T2-weighted MRI. I tried BRAINS Registration and Elastix, but I always end up having errors or incoherent results. I am able to do the alignement by hand, but that is not my goal, so I wondered if anyone has any experience with the automatic registration methods in 3D Slicer working on CT + MRI data of the pelvic area.</p>
<p>Thanks a lot !</p>

---

## Post #2 by @lassoan (2021-11-15 13:26 UTC)

<p>BRAINS usually requires parameter tuning for any other registration tasks than brain MRI.</p>
<p>Elastix usually gives reasonable result without parameter tuning, as long as the images are cropped to the same anatomical region.</p>
<p>You can also try SlicerANTs extension. It seems t have similar performance as Elastix and it is a bit easier to modify registration parameters using the GUI.</p>

---

## Post #3 by @Vincebisca (2021-11-15 14:11 UTC)

<p>I understand for BRAINS.</p>
<p>I retried with Elastix, I centered both volume to get them close, then did a manual transform to do a quick pre-alignement. I cropped around the area I am interested in (using the same ROI for both volumes), and applied Elastix on the cropped volumes. I tried different combination (CT fixed, MRI moving and vice versa, general rigid mode, CT/MR-based pseudo-CT (pelvis(prostate)) mode, etc…) but none of it worked, I get weird offsets on the result everytime and didn’t come even close to a good alignement (the result is always worse than my manual pre-alignement…). So I don’t really know how I should use Elastix to make it work.</p>
<p>For SlicerANTs, I didn’t find it in the Extension Manager…</p>
<p>Thank you for your help as always !</p>

---

## Post #4 by @lassoan (2021-11-15 14:23 UTC)

<p>Please attach a few example images. If you can share anonymized data sets then it is even better.</p>
<p>You need to harden the initial transform on the images.</p>
<p>SlicerANTs is relatively new, so you may need to use a recent Slicer Preview Release.</p>

---

## Post #5 by @Vincebisca (2021-11-15 14:52 UTC)

<p>So, I am trying to aligne the MRI (B) on the CT (A) :</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/003aea0904be5a21a23bd6fec62d33f516510b52.png" alt="image" data-base62-sha1="22dPyYvQSnvcmcCKbGAh8CO6Sm" width="374" height="442"></p>
<p>First I Center the volumes (in the Volumes module, center volume) :</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee0965618a8a2407511d447188f9fa971f0d89ff.png" alt="image" data-base62-sha1="xXLLFrxw8570JP38knAwjt1oDoz" width="327" height="399"></p>
<p>From there, I do a manual transform that I then harden, and crop the result using a single ROI for both volumes, so that I’m sure it’s the same :</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0bfd765081162acce6e4be6b74ad109160942f48.jpeg" data-download-href="/uploads/short-url/1I4i7PMTkGsLd6K5FUV5BftoKne.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0bfd765081162acce6e4be6b74ad109160942f48_2_690x386.jpeg" alt="image" data-base62-sha1="1I4i7PMTkGsLd6K5FUV5BftoKne" width="690" height="386" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0bfd765081162acce6e4be6b74ad109160942f48_2_690x386.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0bfd765081162acce6e4be6b74ad109160942f48_2_1035x579.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0bfd765081162acce6e4be6b74ad109160942f48_2_1380x772.jpeg 2x" data-dominant-color="3C3C45"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1556×871 96.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Once it’s cropped, I go into Elastix, and generally use “general rigid (all)” with the CT (A) as fixed and the MRI (B) as moving :</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e352660ff8cc5cc604e3e1bc710abe4da81a7a6.jpeg" data-download-href="/uploads/short-url/i0u28qlXfkD7o3hUFPN5wU7p4Lc.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7e352660ff8cc5cc604e3e1bc710abe4da81a7a6_2_690x332.jpeg" alt="image" data-base62-sha1="i0u28qlXfkD7o3hUFPN5wU7p4Lc" width="690" height="332" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7e352660ff8cc5cc604e3e1bc710abe4da81a7a6_2_690x332.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7e352660ff8cc5cc604e3e1bc710abe4da81a7a6_2_1035x498.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7e352660ff8cc5cc604e3e1bc710abe4da81a7a6_2_1380x664.jpeg 2x" data-dominant-color="6A6972"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×926 128 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here’s the result : the new volume, which should be aligned with the CT, is instead offsetted by a lot… And I don’t really know why :</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/242d68cb95fa478f98e5f84ec36b63779e168368.png" alt="image" data-base62-sha1="5a2tDyOPPL1tJ2Be6nqdjAhObck" width="393" height="443"></p>

---

## Post #6 by @lassoan (2021-11-16 00:15 UTC)

<p>Thank you, the images were useful. You need to <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#harden-transform-on-a-node">harden the transform</a> on the volume after you apply centering or other manual transformation.</p>

---

## Post #7 by @Vincebisca (2021-11-16 08:38 UTC)

<p>Indeed ! I didn’t see the fact that centering doesn’t harden automatically (since there is no button directly on the GUI allowing to harden, maybe that would be something to add) so I hardened directly in the “data” window and proceeded as mentionned before. The registration worked just fine ! Thank you very much !</p>

---
