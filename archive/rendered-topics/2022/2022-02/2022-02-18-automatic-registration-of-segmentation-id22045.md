---
topic_id: 22045
title: "Automatic Registration Of Segmentation"
date: 2022-02-18
url: https://discourse.slicer.org/t/22045
---

# Automatic registration of segmentation

**Topic ID**: 22045
**Date**: 2022-02-18
**URL**: https://discourse.slicer.org/t/automatic-registration-of-segmentation/22045

---

## Post #1 by @Cam_Arnt (2022-02-18 13:52 UTC)

<p>Hi everyone,</p>
<p>I’ve got a problem with the automatic registration. I will explain you :<br>
I’ve achieved the segmentation of bones on CT-scan images and catilages on MRI images. I would like to register the segmentation with an automatic way. Currently, I’ve just done it manually, and when I try to achieve the registration, only the images are registered.</p>
<p>If everyone can help me, I would be grateful.<br>
Have a good day !</p>

---

## Post #2 by @lassoan (2022-02-18 16:17 UTC)

<p>Registration modules can also compute a transform. You can then <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#apply-transform-to-a-node">apply the computed transform to the segmentation</a>.</p>

---

## Post #3 by @Cam_Arnt (2022-02-22 07:39 UTC)

<p>I’ve done a new linear transform with brain registration module with</p>
<ul>
<li>
<p>fixed image: scan (where there is the bone segmentation)</p>
</li>
<li>
<p>moving image: MRI (where there is the menisci segmentation)<br>
it created the output image 4 and the linear transform</p>
</li>
<li>
<p>I’ve applied the new transform to the menisci segmentation: it worked</p>
</li>
</ul>
<p>but bones are linked to the fixed image but still turned in the wrong way as you can see below, and that I don’t understand.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/255909827c7b5bce369951efe195570181dc278a.jpeg" data-download-href="/uploads/short-url/5koqvKCbnKemeg6nah34puDdcAq.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/255909827c7b5bce369951efe195570181dc278a_2_672x500.jpeg" alt="image" data-base62-sha1="5koqvKCbnKemeg6nah34puDdcAq" width="672" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/255909827c7b5bce369951efe195570181dc278a_2_672x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/255909827c7b5bce369951efe195570181dc278a_2_1008x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/255909827c7b5bce369951efe195570181dc278a.jpeg 2x" data-dominant-color="43454E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1190×885 133 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2022-02-22 13:48 UTC)

<p>The computed transform must be applied to the moving image. You can switch up the fixed and moving image if you want to transform the other image.</p>

---

## Post #5 by @Cam_Arnt (2022-02-22 16:15 UTC)

<p>Thanks for all! My problem was on a registration parameter and not on my segmentation. However, your explication of the transform matrix was very helpful.</p>

---
