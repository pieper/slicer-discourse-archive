---
topic_id: 15111
title: "Bias Estimation Of Volume Changes"
date: 2020-12-17
url: https://discourse.slicer.org/t/15111
---

# Bias estimation of Volume changes

**Topic ID**: 15111
**Date**: 2020-12-17
**URL**: https://discourse.slicer.org/t/bias-estimation-of-volume-changes/15111

---

## Post #1 by @Ash_Alarfaj (2020-12-17 13:18 UTC)

<p>Hello<br>
I’ve used slicer for measuring muscle volume change offer 4-time points threshold effect. I’ve compared two different MRI sequences but covered a quite similar area. The volume changes are different between the two sequences. Do you have any explanation or studies discuss this issue?</p>

---

## Post #2 by @lassoan (2020-12-17 22:16 UTC)

<p>What is the percentage difference?<br>
Can you attach a few screenshots that show the different segmentations?</p>

---

## Post #3 by @Ash_Alarfaj (2020-12-23 15:43 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/5082c302142ade3dcc41650841e22ec9e1da33eb.png" data-download-href="/uploads/short-url/buelUrK2MXsaMpIPoSKqx9DKzKr.png?dl=1" title="Screenshot.C4.V1.R" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/5082c302142ade3dcc41650841e22ec9e1da33eb_2_690x464.png" alt="Screenshot.C4.V1.R" data-base62-sha1="buelUrK2MXsaMpIPoSKqx9DKzKr" width="690" height="464" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/5082c302142ade3dcc41650841e22ec9e1da33eb_2_690x464.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/5082c302142ade3dcc41650841e22ec9e1da33eb_2_1035x696.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/5082c302142ade3dcc41650841e22ec9e1da33eb.png 2x" data-dominant-color="5D4D4E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot.C4.V1.R</span><span class="informations">1373×925 208 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
These are from the same subject. actually, I’ve run measurements for 8 subjects two thighs the results not consistent. even the percentage change between visits, as the scan repeated 3 times after specific intervention.<br>
the 2nd issue I’ve found slicer 10.2 the best. the others 10.0 and 11 versions have not worked perfectly.</p>
<p>thanks</p>

---

## Post #4 by @lassoan (2020-12-23 15:47 UTC)

<aside class="quote no-group" data-username="Ash_Alarfaj" data-post="3" data-topic="15111">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ash_alarfaj/48/3327_2.png" class="avatar"> Ash_Alarfaj:</div>
<blockquote>
<p>I’ve run measurements for 8 subjects two thighs the results not consistent.</p>
</blockquote>
</aside>
<p>What are the the total volumes that you measure on the different images? What is the voxel spacing of your volumes (you can see that in Volumes module / Volume information section)?</p>
<aside class="quote no-group" data-username="Ash_Alarfaj" data-post="3" data-topic="15111">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ash_alarfaj/48/3327_2.png" class="avatar"> Ash_Alarfaj:</div>
<blockquote>
<p>the 2nd issue I’ve found slicer 10.2 the best. the others 10.0 and 11 versions have not worked perfectly</p>
</blockquote>
</aside>
<p>In general, newer Slicer versions work better. If you encounter any specific issues then let us know.</p>

---

## Post #5 by @Ash_Alarfaj (2020-12-23 21:32 UTC)

<p>Hello<br>
the total volume I’ve used is the last column (O) volume(3) as I’ve run a test on phantom and it was the most correct one.</p>
<p>please find the dimensions of the images as screenshots. They are different but I thought the change of muscle volume in both sequences would be similar but it is not.</p>
<ul>
<li>yes I’ve found the contrast adjust effect it is changed in the new slicer. perfect</li>
</ul>
<p>Thanks a lot, Mr Andras for your support</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f3ba1296a1a236ec41f44de56b6cc974b3fd3b80.png" data-download-href="/uploads/short-url/yM6Gpu97ALHxHzxjL7aUvl0AlxK.png?dl=1" title="Screenshot.volum dimension.T1.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f3ba1296a1a236ec41f44de56b6cc974b3fd3b80_2_690x488.png" alt="Screenshot.volum dimension.T1.png" data-base62-sha1="yM6Gpu97ALHxHzxjL7aUvl0AlxK" width="690" height="488" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f3ba1296a1a236ec41f44de56b6cc974b3fd3b80_2_690x488.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/3/f3ba1296a1a236ec41f44de56b6cc974b3fd3b80_2_1035x732.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f3ba1296a1a236ec41f44de56b6cc974b3fd3b80.png 2x" data-dominant-color="606862"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot.volum dimension.T1.png</span><span class="informations">1307×925 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/baf06faccb0d5d5e1d7cf26bf90e9505af6ab731.png" data-download-href="/uploads/short-url/qFJWo5HRHVu01QWph9FwX9KJsnn.png?dl=1" title="Screenshot.volum dimensions.wats.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/baf06faccb0d5d5e1d7cf26bf90e9505af6ab731_2_690x487.png" alt="Screenshot.volum dimensions.wats.png" data-base62-sha1="qFJWo5HRHVu01QWph9FwX9KJsnn" width="690" height="487" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/baf06faccb0d5d5e1d7cf26bf90e9505af6ab731_2_690x487.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/baf06faccb0d5d5e1d7cf26bf90e9505af6ab731_2_1035x730.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/baf06faccb0d5d5e1d7cf26bf90e9505af6ab731.png 2x" data-dominant-color="776162"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot.volum dimensions.wats.png</span><span class="informations">1309×925 248 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
