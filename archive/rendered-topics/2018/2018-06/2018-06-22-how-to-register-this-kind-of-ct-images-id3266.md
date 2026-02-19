---
topic_id: 3266
title: "How To Register This Kind Of Ct Images"
date: 2018-06-22
url: https://discourse.slicer.org/t/3266
---

# How to register this kind of CT images?

**Topic ID**: 3266
**Date**: 2018-06-22
**URL**: https://discourse.slicer.org/t/how-to-register-this-kind-of-ct-images/3266

---

## Post #1 by @glhfgg1024 (2018-06-22 20:31 UTC)

<p>Operating system: Windows 10 64bit<br>
Slicer version: 4.8.0<br>
Expected behavior: Registration<br>
Actual behavior: None</p>
<p>Hi, all,</p>
<p>I have a question on registration between the whole-body CT (denoted as CT1) and the part-body CT (denoted as CT2). The two images are shown as follows:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5c5d85492006427f6356839dfe3410c808e0912a.jpeg" data-download-href="/uploads/short-url/db6ifsiYEDVnktwVgeDLGcgwC8y.jpg?dl=1" title="1111111111" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5c5d85492006427f6356839dfe3410c808e0912a_2_689x423.jpg" alt="1111111111" data-base62-sha1="db6ifsiYEDVnktwVgeDLGcgwC8y" width="689" height="423" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5c5d85492006427f6356839dfe3410c808e0912a_2_689x423.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5c5d85492006427f6356839dfe3410c808e0912a_2_1033x634.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5c5d85492006427f6356839dfe3410c808e0912a.jpeg 2x" data-dominant-color="201F1E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1111111111</span><span class="informations">1346×826 231 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Now I want to register the CT image (CT1) in the first row to the CT image (CT2) in the second row.</p>
<p>In the hospital, they provided the Velocity software to do this. The detail procedure is: first do the rigid registration by defining a bounding box on the bone (vertebra), then the lung region on CT2 will be registered to the lung region of CT1. Then define another bounding box on the lung region, and perform the deformable registration. Then the CT1 and CT2 will be registered (if they are well-aligned by the software).</p>
<p>My question is, in 3D Slicer with the SuperElasticx extension, are there any steps for the registration similar to those in the Velocity? Currently I cannot access the Velocity due to the license. Could you please help give an alternative way to do this in 3D Slicer? Thanks.</p>

---

## Post #2 by @lassoan (2018-06-22 20:58 UTC)

<p>SlicerElastix extension should be able to register in one step. I would recommend to crop the larger volume to include approximately the same body part as the partial CT (using Crop volume module). If you are interested in aligning a particular part of the volume then you can crop both volumes to that region.</p>

---

## Post #3 by @glhfgg1024 (2018-06-22 21:11 UTC)

<p>Hi Prof. Lasso, thanks a lot for your kind reply!</p>
<p>Yeah, the SlicerElastix extension can register the two images in one step, which is very convenient. In fact, I’m using the SlicerElastix to do the registration for PET and CT as described in <a href="https://discourse.slicer.org/t/does-slicer-support-this-kind-of-pet-ct-registration/2354">https://discourse.slicer.org/t/does-slicer-support-this-kind-of-pet-ct-registration/2354</a>. I want to do the registration with separate steps to check if we could get better results for some challenging cases.</p>
<p>Thanks for your suggestion! But I’m not sure if the crop step could be reasonable in my case, as I register CT1 to CT2 is to get the transformation for register PET1 to CT2.</p>

---

## Post #4 by @lassoan (2018-06-22 23:46 UTC)

<p>Yes, of course intra-modality (CT to CT) registration is expected to be much more robust, so do that if possible. To address challenging cases, I would recommend:</p>
<ul>
<li>crop to remove irrelevant part of the image (where you don’t need accurate registration)</li>
<li>if results are not good enough: apply masking (essentially same as cropping, but masks can have arbitrary shape)</li>
<li>if results are still not good enough: tune registration parameters (how metric is computed, how optimization is performed, what transformation is used and how it is parametrized).</li>
</ul>

---

## Post #5 by @glhfgg1024 (2018-06-25 20:36 UTC)

<p>Hi Prof. Lasso, thanks a lot for your kind comments and valuable suggestions! And I’m sorry to reply late as I’m busy on another thing these days.</p>
<p>I may find the main problem which leads to the challenging registration. We have CT1 and PET1, CT2 and SEG on CT2. In general, the CT1 and PET1 were recorded at the same time (may be at an interval due to the different mechanism). Ideally the CT1 and PET1 should be perfectly registered. But I checked the CT1 and PET1 of those cases. It seems they are not well-aligned (The tumor center on PET1 has some voxels shift with that of on CT1). Then I remembered that our physician tolded me that this may be because of the breathing. So if CT1 and PET1 don’t have a good registration, then we cannot guarantee that PET1 can be perfectly registered to CT2, which is quite challenging.</p>
<p>In addition, I have tried what you kind suggested, by defining an crop ROI. Yes, it seems the registration between CT1 and CT2 are good. But as described above, due to that PET1 didn’t well align with CT1, then after using the transformation obtained from the registration between CT1 and CT2, the PET1 still cannot be well-aligned with CT2.</p>

---
