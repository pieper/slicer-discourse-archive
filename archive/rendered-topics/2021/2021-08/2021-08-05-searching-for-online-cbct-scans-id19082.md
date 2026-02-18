# Searching for online CBCT scans

**Topic ID**: 19082
**Date**: 2021-08-05
**URL**: https://discourse.slicer.org/t/searching-for-online-cbct-scans/19082

---

## Post #1 by @Tekk_ya (2021-08-05 13:42 UTC)

<p>Dear all,</p>
<p>I am looking for some online CBCT scan datasets for my project. Mainly, I am interested in datasets of human jaws including teeth and jawbones. Could you please let me know if there are any available datasets that I can use in my research?</p>
<p>Best</p>

---

## Post #2 by @dzenanz (2021-08-05 13:54 UTC)

<p>I can give you <a href="https://www.dropbox.com/s/kt3mhbyrpn4w2km/DZ_CBCT.nrrd?dl=0" rel="noopener nofollow ugc">my own</a>, which is a start. I am not aware of an online repository, but <a class="mention" href="/u/bpaniagua">@bpaniagua</a> might be.</p>

---

## Post #3 by @lassoan (2021-08-05 17:30 UTC)

<p><a class="mention" href="/u/dzenanz">@dzenanz</a> This is a very nice quality CBCT. Would you like to contribute it to the Slicer sample data sets?</p>

---

## Post #4 by @Tekk_ya (2021-08-05 19:42 UTC)

<p>Thanks, I appreciate your help <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #5 by @tsehrhardt (2021-08-06 11:46 UTC)

<p>You can check <a href="https://www.embodi3d.com/" rel="noopener nofollow ugc">https://www.embodi3d.com/</a>.</p>

---

## Post #6 by @dzenanz (2021-08-11 18:40 UTC)

<p>Yes, how do I do that? If you can add it, you have my permission to do so.</p>

---

## Post #7 by @lassoan (2021-08-11 19:19 UTC)

<aside class="quote no-group" data-username="dzenanz" data-post="6" data-topic="19082">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/dzenanz/48/1992_2.png" class="avatar"> dzenanz:</div>
<blockquote>
<p>you have my permission to do so.</p>
</blockquote>
</aside>
<p>Great, thanks, I’ll add it.</p>

---

## Post #8 by @dzenanz (2021-08-31 19:19 UTC)

<p>This is not in the latest nightly’s <code>Sample Data</code> module. Did you add it, and where?</p>

---

## Post #9 by @lassoan (2021-08-31 19:22 UTC)

<p>Haven’t got around to adding it yet.</p>

---

## Post #10 by @dzenanz (2021-08-31 19:40 UTC)

<p>There is also an accompanying <a href="https://www.dropbox.com/s/xe2x8z1ds1uhcb9/tmj_DZ.nrrd?dl=0" rel="noopener nofollow ugc">MRI</a> taken a few weeks after the CBCT. The pair is probably more interesting then CBCT alone.</p>

---

## Post #11 by @dzenanz (2021-08-31 19:43 UTC)

<p>I also manually created a rigid <a href="https://www.dropbox.com/s/l6vm1bpcspz57nl/dz_CBCT_to_MRI.tfm?dl=0" rel="noopener nofollow ugc">transform</a> to register them:</p>
<pre><code class="lang-nohighlight">#Insight Transform File V1.0
#Transform 0
Transform: AffineTransform_double_3_3
Parameters: 0.9940781967960048 -0.09133167899340905 0.05888177194215917 0.09694405147534274 0.9901711118493441 -0.10081180557146947 -0.04909571812642784 0.10592305542835587 0.9931615763763577 -3.10842487001195 55.49648178586631 5.639941288765998
FixedParameters: 0 0 0
</code></pre>

---

## Post #12 by @lassoan (2021-09-15 04:50 UTC)

<p><a class="mention" href="/u/dzenanz">@dzenanz</a> Thanks for shating the additional image and transform. The data set is now added to Sample Data module as “CBCT-MR Head”:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/191d9820809d8ee6642413622a6820cfab31d187.jpeg" data-download-href="/uploads/short-url/3AbldbICzLYZLjRCvjXfOfcvu8T.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/191d9820809d8ee6642413622a6820cfab31d187_2_690x405.jpeg" alt="image" data-base62-sha1="3AbldbICzLYZLjRCvjXfOfcvu8T" width="690" height="405" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/191d9820809d8ee6642413622a6820cfab31d187_2_690x405.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/191d9820809d8ee6642413622a6820cfab31d187_2_1035x607.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/191d9820809d8ee6642413622a6820cfab31d187_2_1380x810.jpeg 2x" data-dominant-color="727072"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1127 164 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #13 by @dzenanz (2021-09-16 13:41 UTC)

<p>I downloaded the latest nightly, and I didn’t notice it at first. I found it by looking at your screenshot. The reason: thumbnail is missing from it.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/821903c488e4fbca3c7b2ed3783ab1846653a5fe.png" data-download-href="/uploads/short-url/iyTFe2I0iyDifiDILYF1Coehz8G.png?dl=1" title="Screenshot 2021-09-16 09.37.38" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/821903c488e4fbca3c7b2ed3783ab1846653a5fe_2_323x499.png" alt="Screenshot 2021-09-16 09.37.38" data-base62-sha1="iyTFe2I0iyDifiDILYF1Coehz8G" width="323" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/821903c488e4fbca3c7b2ed3783ab1846653a5fe_2_323x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/821903c488e4fbca3c7b2ed3783ab1846653a5fe_2_484x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/821903c488e4fbca3c7b2ed3783ab1846653a5fe_2_646x998.png 2x" data-dominant-color="B6B3B2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2021-09-16 09.37.38</span><span class="informations">1026×1588 206 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Am I the only one with this symptom?</p>
<p><strong>Edit:</strong> the data is downloaded properly once the button is clicked.</p>

---

## Post #14 by @lassoan (2021-09-16 14:07 UTC)

<p>Thank you, I’ve fixed the thumbnail now.</p>

---
