---
topic_id: 17523
title: "Realization Of Neuronavigation"
date: 2021-05-08
url: https://discourse.slicer.org/t/17523
---

# Realization of neuronavigation

**Topic ID**: 17523
**Date**: 2021-05-08
**URL**: https://discourse.slicer.org/t/realization-of-neuronavigation/17523

---

## Post #1 by @slicer365 (2021-05-08 14:21 UTC)

<div class="youtube-onebox lazy-video-container" data-video-id="MOqh6wgOOYs" data-video-title="Webcam-based tracking in 3D Slicer/SlicerIGT" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=MOqh6wgOOYs" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/MOqh6wgOOYs/maxresdefault.jpg" title="Webcam-based tracking in 3D Slicer/SlicerIGT" width="" height="">
  </a>
</div>

<p>I would love to try the navigation function of this camera, but how should I operate it and which app should I download?Where can I get a more detailed tutorial</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e3b3cad3d00d29eab6e9ea8fb6ad6dcaf43dca6.jpeg" data-download-href="/uploads/short-url/mzMm0Q9POumN73gAlqnCOskmrvE.jpeg?dl=1" title="捕获" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9e3b3cad3d00d29eab6e9ea8fb6ad6dcaf43dca6_2_517x288.jpeg" alt="捕获" data-base62-sha1="mzMm0Q9POumN73gAlqnCOskmrvE" width="517" height="288" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9e3b3cad3d00d29eab6e9ea8fb6ad6dcaf43dca6_2_517x288.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9e3b3cad3d00d29eab6e9ea8fb6ad6dcaf43dca6_2_775x432.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e3b3cad3d00d29eab6e9ea8fb6ad6dcaf43dca6.jpeg 2x" data-dominant-color="ECECF1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">捕获</span><span class="informations">898×501 95.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-05-10 04:48 UTC)

<p>You can find step-by-step instructions in <a>this PerkLab bootcamp tutorial</a>.</p>

---

## Post #3 by @slicer365 (2021-05-11 01:48 UTC)

<p>Thank you very much Professor Lasso,I strictly follow the steps of PPT, but every time I get here, I cannot get these three transforms.It show empty！<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f38049f1ba1fe81291b07537a9fb74be62fc0fb2.png" alt="无标题" data-base62-sha1="yK6SJS63omiXye066m6n28vJzQ6" width="321" height="398"></p>

---

## Post #4 by @lassoan (2021-05-11 04:28 UTC)

<p>You need to place the markers in the field of view of your camera. The markers that Plus recognizes will show up in the IN nodes.</p>

---

## Post #5 by @slicer365 (2021-05-12 13:07 UTC)

<p>Thank you very much for your answers, thank you for your patience, now I am all ready, but there is one more question, how to register the Sign and the Entity.For example, I put a skull model on the table, and the matching CT model is displayed in Slicer at the same time, but how can I make them registered like the video?</p>

---

## Post #6 by @lassoan (2021-05-12 13:39 UTC)

<aside class="quote no-group" data-username="slicer365" data-post="5" data-topic="17523">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/slicer365/48/67549_2.png" class="avatar"> slicer365:</div>
<blockquote>
<p>I put a skull model on the table, and the matching CT model is displayed in Slicer at the same time, but how can I make them registered like the video?</p>
</blockquote>
</aside>
<p>Registration of this patient-attached tracking marker to the patient image is typically performed using landmark registration. The process is described in <a href="http://www.slicerigt.org/wp/user-tutorial/">SlicerIGT tutorials</a>.</p>

---

## Post #7 by @fanyifeng (2021-11-09 10:07 UTC)

<p>Can you send me the PPT, I cannot open the URL:<a href="http://www.slicerigt.org/wp/user-tutorial/" class="inline-onebox" rel="noopener nofollow ugc">User tutorial | SlicerIGT</a></p>

---

## Post #8 by @fanyifeng (2021-11-09 10:12 UTC)

<p>Dear Lasson, Can you send me the documents in <a href="http://www.slicerigt.org/wp/user-tutorial/" rel="noopener nofollow ugc">SlicerIGT tutorials</a>, I cannot open the URL:<a href="http://www.slicerigt.org/wp/user-tutorial/" class="inline-onebox" rel="noopener nofollow ugc">User tutorial | SlicerIGT</a> in China. I also want to realize a neuronavigation using 3D Slicer.</p>

---

## Post #9 by @lassoan (2021-11-11 05:55 UTC)

<p>Accessibility of SlicerIGT tutorials from China is discussed further here:</p>
<aside class="quote" data-post="7" data-topic="20536">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/50afbb/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/the-user-tutorial-cannot-be-readed-in-china/20536/7">The user-tutorial cannot be readed in China</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Thanks for confirming. Sounds like that to the user, the OneDrive dependency is at least partially hidden (it isn’t explicitly declared, but it might be visible in the link). 
If OneDrive is uniformly used, and if it turns out that it’s the reason why the tutorials aren’t available in China, some sort of note like (“Can’t access these tutorials?”) which links off to a workaround page might be the most helpful to a beginning user.
  </blockquote>
</aside>


---
