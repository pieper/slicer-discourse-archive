# Save the latest version

**Topic ID**: 14194
**Date**: 2020-10-21
**URL**: https://discourse.slicer.org/t/save-the-latest-version/14194

---

## Post #1 by @Andreas (2020-10-21 21:00 UTC)

<p>Which files do I need later to save the latest (segmented) version? (Image)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e31ddda5c69efee082d4c15eed3176078201fa5.jpeg" data-download-href="/uploads/short-url/khUDElQz0Lcgbpfc3J3LE5SoxHT.jpeg?dl=1" title="save the latest version" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8e31ddda5c69efee082d4c15eed3176078201fa5_2_446x500.jpeg" alt="save the latest version" data-base62-sha1="khUDElQz0Lcgbpfc3J3LE5SoxHT" width="446" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8e31ddda5c69efee082d4c15eed3176078201fa5_2_446x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8e31ddda5c69efee082d4c15eed3176078201fa5_2_669x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e31ddda5c69efee082d4c15eed3176078201fa5.jpeg 2x" data-dominant-color="EFEFEF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">save the latest version</span><span class="informations">834×934 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I usually save all files so that no data is lost, but this usually takes a long time and takes up a lot of storage space. (with slicer supported file would be good to load the model quickly)</p>
<p>And I have one more question about the Cast Scalar Volume (Short) module.<br>
Do you only use this function if you have too little memory or should you avoid it if possible, since there is a risk of getting a model with a lower accuracy?</p>
<p>Many thanks for your help.</p>
<p>Best regards</p>

---

## Post #2 by @lassoan (2020-10-22 03:01 UTC)

<aside class="quote no-group" data-username="Andreas" data-post="1" data-topic="14194">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ee7513/48.png" class="avatar"> Andreas:</div>
<blockquote>
<p>Which files do I need later to save the latest (segmented) version?</p>
</blockquote>
</aside>
<p>In general, if you are not sure which node corresponds to what then you can go to Data module and click the eye icons to show/hide a node - whatever disappears and reappears is that node.</p>
<aside class="quote no-group" data-username="Andreas" data-post="1" data-topic="14194">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ee7513/48.png" class="avatar"> Andreas:</div>
<blockquote>
<p>question about the Cast Scalar Volume (Short) module.<br>
Do you only use this function if you have too little memory or should you avoid it if possible, since there is a risk of getting a model with a lower accuracy?</p>
</blockquote>
</aside>
<p>You can check the scalar range in Volumes module’s Volume information section. If scalar range can be represented using the chosen output scalar type then no information is lost during the conversion.</p>

---
