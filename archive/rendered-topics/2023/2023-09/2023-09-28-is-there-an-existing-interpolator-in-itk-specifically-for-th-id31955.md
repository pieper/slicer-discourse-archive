---
topic_id: 31955
title: "Is There An Existing Interpolator In Itk Specifically For Th"
date: 2023-09-28
url: https://discourse.slicer.org/t/31955
---

# Is there an existing "interpolator" in ITK specifically for the Slice-to-Volume registration?

**Topic ID**: 31955
**Date**: 2023-09-28
**URL**: https://discourse.slicer.org/t/is-there-an-existing-interpolator-in-itk-specifically-for-the-slice-to-volume-registration/31955

---

## Post #1 by @Shuwei (2023-09-28 21:43 UTC)

<p>Hi All,</p>
<p>I am working on the slice-to-volume registration topic using ITK. Conventionally, slice-to-volume registration (e.g. US-CT) needs to reslice the volume data based on the transformation and then convert it to a 2D-2D registration problem.  In this <a href="https://discourse.itk.org/t/slice-to-volume-registration/3659" rel="noopener nofollow ugc">discussion</a>, <a href="https://github.com/InsightSoftwareConsortium/ITKTwoProjectionRegistration" rel="noopener nofollow ugc">TwoProjectionRegistration</a> was suggested to kick off the slice-to-volume registration. However, there are still lots of differences.</p>
<p>I wonder whether there is an existing “interpolator”, which can achieve the volume data reslicing and interpolation tasks, similar to the “itkRayCastInterpolateImageFunction”. I think that if this interpolator exists, we can connect with other components (similarity metric, optimizer) to achieve the slice-to-volume registration. If not, any suggestions to write one?</p>
<p>Thanks</p>
<p><span data-date="2023-09-28" class="discourse-local-date" data-timezone="America/New_York" data-email-preview="2023-09-28T04:00:00Z UTC">2023-09-28T04:00:00Z</span></p>

---

## Post #2 by @lassoan (2023-09-30 04:34 UTC)

<p>Slice-to-volume registration does not require any special interpolator, as it directly aligns voxels of the slice to the voxels of the volume. Single-slice-to-volume registration is a simple 3D-3D registration task (just one of the 3D volumes happen to have only a single slice). The only thing you need to pay attention to is to use the single-slice image as fixed image (otherwise ITK will return with the error that most voxels of the fixed image lie outside of the moving image).</p>

---

## Post #3 by @Shuwei (2023-09-30 14:36 UTC)

<p>I see. Thank you, <a class="mention" href="/u/lassoan">@lassoan</a>. I will give it a try.</p>

---

## Post #4 by @Shuwei (2023-10-02 22:40 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I tried the solution you mentioned, and it worked well. I really appreciate it!</p>
<p>For now, I have two more questions about the slice-to-volume registration, I hope you could provide me with some ideas:</p>
<p>(1) In SimpleITK/ITK, there are some existing similarity metrics to facilitate the registration task. If I wish to develop my own similarity metric, instead of rewriting a new similarity metric API (based on C++), is there a more straightforward solution available? I am guessing that my own similarity metric has to integrate with the well-streamlined registration workflow in SimpleITK/ITK, It seems that writing a new API, similar to other existing similarity metrics, might be the only option.</p>
<p>(2) From my understanding, similarity metrics are mostly calculated based on the entire image pairs or masked image pairs, is it possible to calculate patch-level-based similarity metrics? In other words, can I randomly choose many patches (let’s say 1000) from the fixed and moving images respectively, and then evaluate the patch-level-based similarity metric for the following optimization?  I am not sure how these patches integrate into the registration workflow.</p>
<p>Any suggestions will be appreciated! Thank you!</p>

---

## Post #5 by @lassoan (2023-10-03 04:07 UTC)

<aside class="quote no-group" data-username="Shuwei" data-post="4" data-topic="31955">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shuwei/48/67695_2.png" class="avatar"> Shuwei:</div>
<blockquote>
<p>From my understanding, similarity metrics are mostly calculated based on the entire image pairs or masked image pairs</p>
</blockquote>
</aside>
<p>Similarity is typically evaluated on a set of sample points, e.g., 10% of the fixed image voxels.</p>
<p>There are many metrics in ITK already, so you may not need to implement yet another one. But if you want then you can write a new one or combine existing similarity metrics in C++ for sure. Maybe in Python, too, but you can get definitive answer for this on the <a href="https://discourse.itk.org/">ITK forum</a>.</p>

---

## Post #6 by @Shuwei (2023-10-03 12:16 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> , thank you for your quick response and for clarifying my misunderstanding. I will certainly look into it.</p>
<p>Regarding question 2, which I previously inquired about, I am also wondering how I can calculate patch-level-based similarity metrics. Do we also need to write a new function to break images into small patches and integrate them into the registration workflow? Any thoughts about that?</p>

---

## Post #7 by @lassoan (2023-10-03 13:39 UTC)

<p>There has not been much work on patch-based similarity metrics in ITK, most likely because intensity-based metrics work so well for medical images (see for example <a href="https://insight-users.itk.narkive.com/0xyBi0AC/sift-feature-based-registration-in-itk">this old discussion</a>). SIFT based registration was evaluated for challenging registration tasks (e.g., ultrasound slice registration to ultrasound or MRI volume) with some success, but these are niche applications, so I’m not sure that they have made it into any commonly used registration toolkits.</p>
<p>You can implement any similarity metric, including patch-based metric. Since the metric has to be evaluated at hundreds of thousands or millions of positions in each iteration and typically you need hundreds of iterations, you probably have to do it in C++ (perhaps with some CUDA acceleration) for a reasonable computation time.</p>
<p>There are many registration experts in the ITK forum, so I would recommend posting further questions on this topic there.</p>

---

## Post #8 by @Shuwei (2023-10-03 13:57 UTC)

<p>Thank you so much, <a class="mention" href="/u/lassoan">@lassoan</a>. I really appreciate your response.</p>
<p>I will post my further questions on the ITK forum in the future. Thank you for explaining the considerations of implementing a patch-based metric.</p>

---
