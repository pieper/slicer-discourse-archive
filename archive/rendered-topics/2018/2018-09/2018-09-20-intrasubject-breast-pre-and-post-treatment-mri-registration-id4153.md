---
topic_id: 4153
title: "Intrasubject Breast Pre And Post Treatment Mri Registration"
date: 2018-09-20
url: https://discourse.slicer.org/t/4153
---

# Intrasubject Breast pre- and post-treatment MRI registration

**Topic ID**: 4153
**Date**: 2018-09-20
**URL**: https://discourse.slicer.org/t/intrasubject-breast-pre-and-post-treatment-mri-registration/4153

---

## Post #1 by @labixin (2018-09-20 02:04 UTC)

<p>Hi everyone,<br>
I have some questions about Slicer Registration Library Case <span class="hashtag">#6:</span> Breast MRI Cancer Treatment. (<a href="https://www.slicer.org/wiki/Documentation:Nightly:Registration:RegistrationLibrary:RegLib_C06" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation:Nightly:Registration:RegistrationLibrary:RegLib_C06</a></p>
<ol>
<li>Does the mask really make sense dealing with this situation? If it does work, is this tumor recession situation similar to the tumor resection problem? (I have searched the RegistrationLibrary but tumor resection related case is still under construction) Can I use the method in Case <span class="hashtag">#6</span> to register preoperative and post-surgical breast MRI?</li>
<li>Is the B-Spline Transform in General Registration (BRAINS) based on image intensity by default? Is there any similarity metrics based on the texture such as adipose, mammary gland or fibro glandular tissue? Where can I know more details about the registration elements like the optimization method?<br>
I am a novice in registration field and happy to find 3DSlicer which helps me a lot.<br>
Hope for any kind help or comment, thanks a lot!</li>
</ol>

---

## Post #2 by @lassoan (2018-09-20 03:48 UTC)

<aside class="quote no-group" data-username="labixin" data-post="1" data-topic="4153">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/labixin/48/1965_2.png" class="avatar"> labixin:</div>
<blockquote>
<p>Does the mask really make sense dealing with this situation? If it does work, is this tumor recession situation similar to the tumor resection problem?</p>
</blockquote>
</aside>
<p>Yes.</p>
<aside class="quote no-group" data-username="labixin" data-post="1" data-topic="4153">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/labixin/48/1965_2.png" class="avatar"> labixin:</div>
<blockquote>
<p>Is the B-Spline Transform in General Registration (BRAINS) based on image intensity by default?</p>
</blockquote>
</aside>
<p>Transformation and similarity metric are unrelated. You can choose transformation (rigid, affine, bspline, etc.) independently from similarity metric (MMI - Mattes Mutual Information, MSE - Mean Square Error, etc.).</p>
<aside class="quote no-group" data-username="labixin" data-post="1" data-topic="4153">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/labixin/48/1965_2.png" class="avatar"> labixin:</div>
<blockquote>
<p>Is there any similarity metrics based on the texture</p>
</blockquote>
</aside>
<p>From all the similarity metrics that have been evaluated in the past decades, mutual information emerged as one of the best (or the best?) for general use. So, I would recommend to explore what you can achieve with it before you start experimenting with other metrics.</p>
<p>Based on my experience, defining correct region of interest and a good optimization scheme is more critical than the similarity metric. “General registration (BRAINS)” module often requires tuning of optimization parameters, while “General registration (Elastix)” module (provided by SlicerElastix extension) typically works very robustly without any manual parameter tuning. If you don’t have success with BRAINS module then it may worth trying Elastix, too.</p>

---
