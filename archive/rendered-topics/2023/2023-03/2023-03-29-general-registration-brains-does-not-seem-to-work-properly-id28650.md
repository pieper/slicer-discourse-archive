---
topic_id: 28650
title: "General Registration Brains Does Not Seem To Work Properly"
date: 2023-03-29
url: https://discourse.slicer.org/t/28650
---

# General Registration (BRAINS) does not seem to work properly

**Topic ID**: 28650
**Date**: 2023-03-29
**URL**: https://discourse.slicer.org/t/general-registration-brains-does-not-seem-to-work-properly/28650

---

## Post #1 by @luke90 (2023-03-29 10:18 UTC)

<p>Hello guys,</p>
<p>I have done a registration in the general registration module (BRAINS) but the output image volume does not match with the fixed image volume. The goal is to apply a linear transformation (rotation and translation) to a CT dicom volume and then save the transformed volume as dicom. As you can see, I have imported the CT dicom volume (fix_img) and I have cloned it (mov_img).<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/9804b89bd60dd906b19206c79c86ae36fb1fabbf.png" alt="image" data-base62-sha1="lGOGOcfXtcClAiLXwgefAoNR8rJ" width="245" height="90"><br>
In the Transform module I have created a new linear transform,<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f7eeb89e07d0607ba85af43a366db50192e4d93.png" alt="image" data-base62-sha1="6MamHkRvMkwnoK0WesPPh3pACll" width="254" height="98"><br>
I have moved the fix_img under Transformed<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/773c5d349ea6f22f8546316460178b4bd7eaa8ac.png" alt="image" data-base62-sha1="h0O9cALmJyBtSzOTBeAJGlxrFTu" width="249" height="88"><br>
and then I have rotated and translated the volume.<br>
As you can see in the image below, I created a transform matrix with different rotations and translations. Strangely, unlike the translations, the rotations of the planes seem set to 0° despite being present in the Transform matrix. In other words, for example if I rotate the LR plane of 20° and then rotate the IS plane of 10°, then the rotation of the LR plane will be shown at 0°. I don’t know if this will affect the final result in any way.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/3110aecc9fd25a92b60d1c4b2c3b71ce5d82c952.png" alt="image" data-base62-sha1="7038BzDMDr5T9b8bn5IwciDdeue" width="247" height="229"><br>
Then I have applied the transformations to the fix_img using Harden transform.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/4/9478df3f72be01ab51a1c3d6b5142d006d8e2659.png" alt="image" data-base62-sha1="lbrDezQIbSzrVRyIvA1KpFs2zVL" width="243" height="121"><br>
In the general registration (BRAINS) module, I have set as Fixed Image volume the fix_img and as Moving Image volume the mov_img that will be transformed into the fixed image space using the linear transformation.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2011c508f9036f613f3ddd48d0f3fa544dde093.png" data-download-href="/uploads/short-url/n79JeR7M8kRE8Xj9L7466dHvpvl.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a2011c508f9036f613f3ddd48d0f3fa544dde093.png" alt="image" data-base62-sha1="n79JeR7M8kRE8Xj9L7466dHvpvl" width="279" height="375" data-dominant-color="3E3E3E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">511×684 10.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Unfortunately, Output image volume is not properly rotated and translated.<br>
Another strange thing I have noticed is that if I go back to Data and display the fix_img volume, it doesn’t seem rotated and translated even though I have used harden transform. If I re-apply the linear transformation to the fix_img volume it is correctly rotated and moved. But this should not happen as I have already applied the linear transformation using harden transform. It is as if selecting a volume in Data, each transformation is deleted.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/99435f6795dc7c4ac49ea44003d8b095dbb6ac92.png" alt="image" data-base62-sha1="lRPoGWmf7D5znlUCMhhh6EOVsAi" width="221" height="77"><br>
Does anyone know how to save a dicom volume with a new reference system after a linear transformation?<br>
Thank you</p>

---

## Post #2 by @luke90 (2023-03-29 17:53 UTC)

<p>I found a solution. I used the resample image module and was able to save the transformed volume without any problems</p>

---
