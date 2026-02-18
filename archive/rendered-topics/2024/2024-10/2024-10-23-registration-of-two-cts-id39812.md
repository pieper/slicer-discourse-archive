# Registration of two CTs

**Topic ID**: 39812
**Date**: 2024-10-23
**URL**: https://discourse.slicer.org/t/registration-of-two-cts/39812

---

## Post #1 by @Bor_Antolic (2024-10-23 05:45 UTC)

<p>Hi!<br>
I would like to register a 4D planning CT to a ECG triggered contrast enhanced CT for radiotherapy planning. I tried to do it manually, but I cannot seem to get that both CTs would be displayed at the same time and that the opacity slicer would show on or the other (or a mix of the two). It would of course be best, if it could be done (semi) automatically, but for now, just this step is giving me problems.<br>
Can you direct me to a manual? Similar post about this problem?<br>
Should CTs be of the same pixel size? Cropped to a similar size?<br>
Thanks!</p>

---

## Post #2 by @muratmaga (2024-10-23 18:06 UTC)

<p>Please read the relevant section of the documentation:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/user_guide/registration.html</a></p>

---

## Post #3 by @Bor_Antolic (2024-10-24 18:16 UTC)

<p>Thank you for the reply. I’ve read it again and I am still lost. I open to DICOM CTs in Slicer and I cannot get them both two be shown overlapping. Is there any step I fail to do before this step? Is cropping and making the voxel size the same mandatory?</p>

---

## Post #4 by @muratmaga (2024-10-24 18:48 UTC)

<p>If the two images are not occupying the same space, you cannot display them together. You have to do some sort of (manual or automatic) registration first.</p>
<p>What did you try and it didn’t work?</p>

---

## Post #5 by @Bor_Antolic (2024-10-25 05:43 UTC)

<p>I cropped the two CT to approximatelly same size, also checked isotropic spacing and made sure that the voxels are (almost) the same size. Then I lay them on top of each other… When I try to change transparency so I could manually register them, but nothing happens. I cannot see the other one.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f3eec3881550af6dd431e20c7d8bdae57a7fb95.jpeg" data-download-href="/uploads/short-url/i9FrU8ZdMykw7AH1JhSiTxvd1uB.jpeg?dl=1" title="{93AEFBCA-4DBC-45F0-98FE-F22B32CE8226}" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f3eec3881550af6dd431e20c7d8bdae57a7fb95_2_690x357.jpeg" alt="{93AEFBCA-4DBC-45F0-98FE-F22B32CE8226}" data-base62-sha1="i9FrU8ZdMykw7AH1JhSiTxvd1uB" width="690" height="357" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f3eec3881550af6dd431e20c7d8bdae57a7fb95_2_690x357.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f3eec3881550af6dd431e20c7d8bdae57a7fb95_2_1035x535.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/f/7f3eec3881550af6dd431e20c7d8bdae57a7fb95_2_1380x714.jpeg 2x" data-dominant-color="4B4B51"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">{93AEFBCA-4DBC-45F0-98FE-F22B32CE8226}</span><span class="informations">1874×972 214 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @pieper (2024-10-25 13:31 UTC)

<p>The dimensions and spacings don’t matter, but you need to be sure the two volumes are in the same physical space.  You can look at the origins and directions in the Volume Information in the Volumes module to get an idea, but probably easier is to make both visible in Volume Rendering and look at where they are in the 3D view.  You can add a transform and move one of them on the other and then you can see them both in the same slice views.  Even easier and better could be to <a href="https://slicer.readthedocs.io/en/5.6/user_guide/registration.html">rigidly register</a> them with a pre-alignment option.  You can use the “Register this” option in the context menu of the data module to set things up easily.</p>

---

## Post #7 by @Bor_Antolic (2024-10-25 18:09 UTC)

<p>Thank you so much!<br>
Finally I understand what the issue was and got it to work!<br>
Thanks!</p>

---
