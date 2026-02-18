# Registration of consecutive CT volumes

**Topic ID**: 11649
**Date**: 2020-05-21
**URL**: https://discourse.slicer.org/t/registration-of-consecutive-ct-volumes/11649

---

## Post #1 by @Farah (2020-05-21 05:23 UTC)

<p>Hi community,</p>
<p>I am trying to register consecutive CT volumes of the abdominal aortic aneurysm, I have 10 volumes during the cardiac cycle of the patient. I tried BSpline with different grid sizes but the algorithm is generating artifacts that is obvious on the picture attached, green segmentation is the reference geometry (segmented manually) and the yellow segmentation is the transformed geometry (created from registration 2 CT then applied the transform on the reference geometry).<br>
Could you recommend any reliable registration method or any previous work on registration of consecutive 3D volumes.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/7326fc7502c1ab82cb45bf1308d34594cb670ef8.png" data-download-href="/uploads/short-url/gqGr49HyQjfDdsrmg8yqplQBlos.png?dl=1" title="question" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/7326fc7502c1ab82cb45bf1308d34594cb670ef8.png" alt="question" data-base62-sha1="gqGr49HyQjfDdsrmg8yqplQBlos" width="488" height="500" data-dominant-color="8C8C8B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">question</span><span class="informations">689×705 21.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you very much,<br>
Farah</p>

---

## Post #2 by @pieper (2020-05-21 13:38 UTC)

<p>DRAMMS is a very powerful technique and might work well for this: <a href="https://www.med.upenn.edu/sbia/dramms.html">https://www.med.upenn.edu/sbia/dramms.html</a></p>

---

## Post #3 by @lassoan (2020-05-21 19:16 UTC)

<p>This registration looks pretty good (error is less than a voxel at most places).</p>
<p>Trying different registration packages is a good idea. Elastix (available in SlicerElastix extension) is very good, too, and it is highly customizable.</p>
<p>If you find that calcifications or devices, etc. misguide the registration then you may either suppress them by preprocessing (e.g., limit maximum intensity of the image using thresholding) or set a registration mask that excludes high-intensity regions.</p>

---

## Post #4 by @Farah (2020-05-22 01:38 UTC)

<p>Thanks Andras,<br>
I will try these 3 solutions.</p>

---

## Post #5 by @Farah (2020-05-23 16:51 UTC)

<p>Hi Andras,<br>
I was reading the elastix manual, and according to my case the following recommendations were mentioned: use BSpline transform type, use Mean Square Difference (MSD), and use full image sampler.<br>
My question is how can I select these parameters in 3D slicer (Elastix module)?<br>
Thank you very much,<br>
Farah</p>

---

## Post #6 by @lassoan (2020-05-23 18:27 UTC)

<p>See this documentation section about how to customize Elastix registration parameters: <a href="https://github.com/lassoan/SlicerElastix/blob/master/README.md#customize-registration-parameters">https://github.com/lassoan/SlicerElastix/blob/master/README.md#customize-registration-parameters</a></p>

---
