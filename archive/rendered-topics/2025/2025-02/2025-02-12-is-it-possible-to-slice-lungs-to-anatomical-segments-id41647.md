# Is it possible to slice lungs to anatomical segments?

**Topic ID**: 41647
**Date**: 2025-02-12
**URL**: https://discourse.slicer.org/t/is-it-possible-to-slice-lungs-to-anatomical-segments/41647

---

## Post #1 by @Ismail_Sarbay (2025-02-12 14:33 UTC)

<p>Hi there,</p>
<p>I loved the 3D segmentation of the lungs but it is only lobe level segmentation. Is it possible to make the segmentation further to anatomical segmentation of each lung lobe for example 3 segments of right upper lobe, 2 of middle, 5 of RML and so on. I would be happy if there is a return and solution.</p>

---

## Post #2 by @lassoan (2025-02-12 14:47 UTC)

<p>In current Slicer-based lung surgery planning workflows, lung lobes are split to segments using Scissors effect in 3D, by visualizing arteries, veins, and bronchi. It takes just a few minutes, the most challenging part is to learn the anatomy, so that you can confidently find the view orientation where the boundary between segments is visible and then draw the line. <a class="mention" href="/u/eserval">@Eserval</a> is an expert in this, he may provide more information.</p>
<p>There are ongoing efforts for making this more automated using AI. Automatic lobe segmentation is done, airway and vessel segmentation are mostly done. Artery/vein separation and lung segments segmentation needs more work (grant application submitted, will happen if gets funded).</p>

---

## Post #3 by @Ismail_Sarbay (2025-02-13 09:59 UTC)

<p>Thank you for your response. I will try to manually do that until any progress is achieved.</p>

---

## Post #4 by @Eserval (2025-02-13 20:51 UTC)

<p>Hello <a class="mention" href="/u/ismail_sarbay">@Ismail_Sarbay</a><br>
As Andras mentioned, the segmental division is performed manually by the professional conducting the reconstruction. Therefore, broad anatomical knowledge is essential for an accurate division, especially considering the high incidence of anatomical variations in pulmonary segments. I’d be happy to assist if you need help with a specific case.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da6a065bedc9142f02dfa06fb3f0cc603560c4eb.png" data-download-href="/uploads/short-url/vabfeArrWTuJPko5k6Vd8ZBMeRJ.png?dl=1" title="REC" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da6a065bedc9142f02dfa06fb3f0cc603560c4eb_2_460x500.png" alt="REC" data-base62-sha1="vabfeArrWTuJPko5k6Vd8ZBMeRJ" width="460" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da6a065bedc9142f02dfa06fb3f0cc603560c4eb_2_460x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da6a065bedc9142f02dfa06fb3f0cc603560c4eb.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da6a065bedc9142f02dfa06fb3f0cc603560c4eb.png 2x" data-dominant-color="D6C2B7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">REC</span><span class="informations">567×615 193 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>As a surgeon, I use the intersegmental veins to define the intersegmental plane.</p>
<p>Best!</p>

---

## Post #5 by @Ismail_Sarbay (2025-02-14 13:32 UTC)

<p>Thank you doctor.  I am wondering the tools to divide/subtract the segments. Do you have a tutorial about the procedure?</p>

---
