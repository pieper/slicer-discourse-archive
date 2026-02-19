---
topic_id: 25969
title: "Rmse In Landmarks Registration"
date: 2022-10-30
url: https://discourse.slicer.org/t/25969
---

# RMSE in Landmarks Registration

**Topic ID**: 25969
**Date**: 2022-10-30
**URL**: https://discourse.slicer.org/t/rmse-in-landmarks-registration/25969

---

## Post #1 by @domP (2022-10-30 11:07 UTC)

<p>Hello everyone,<br>
I’m trying to register two volumes using “Fiducial Registration Wizard” module. My goal is to find the minimum number of fiducial points that give me best result in the alignment.<br>
What I observe when I increase the number of landmarks is that RMSE increases but visual alignment seems better in axial, coronal and sagittal views.<br>
If I want to quantify registration with respect to the number of fiducials is it fair to consider RMSE or is there another way?</p>

---

## Post #2 by @lassoan (2022-10-30 12:29 UTC)

<p>It is a somewhat unintuitive but but a well proven fact that fiducial registration (residual error shown as RMSE) is different from target registration error (accuracy of aligning important target positions).</p>
<p>You need minimum 3 points for a rigid registration, but the more points you add, the higher the chances that you reduce the effect of random errors in your imaging and point marking. However, the more points you add, the more time it takes, you may become less careful when placing the points, and you may only find lower-quality landmark points (that you are not so sure about or are farther from the region of interest), which may not improve the end result.</p>
<p>Most often you would end up using 6-8 high-quality landmarks, placed carefully.</p>
<p>If you don’t have this many good landmarks then there are alternative methods. For example, you can collect a large number of surface points using a tracked stylus or surface scanner and use points to surface registration.</p>

---

## Post #3 by @KatS (2023-03-06 15:21 UTC)

<p>Hello,</p>
<p>I have a similar problem and am looking for a way to quantify the “success” of registration.<br>
In my case, I use the “Fiducial Registration Wizard” to coregister a 3D MRI dataset and a 3D stack of histological images obtained with light sheet microscopy. I placed fiducials on anatomical landmarks and want to somehow quantify the registration result. Qualitatively, the more fiducials I place, the better the visual alignment of the datasets and the higher the RMSE.<br>
Is there any way to quantify the visual impression of “the more fiducials the better”? Is there a way to calculate at which number of fiducials the result is best, i.e. alignment doesn’t get better by adding more fiducials once a certain number has been placed?<br>
Thanks in advance! Any input on this is highly appreciated! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @lassoan (2023-03-06 20:49 UTC)

<p>There is no general solution for objective evaluation of accuracy of landmark registration. To measure the error you would need ground truth information that is about a magnitude more accurate than the expected error, but such ground truth information is usyallynot available.</p>
<p>Most common TRE estimation method is that an expert determines some matching landmarks in the region of interest that are not used for registration. Unfortunately, this method takes a lot of effort and its accuracy is usually worse than the registration error that we want to measure.</p>
<p>There may be better solutions for special cases. You can search on the web for papers on “target registration error estimation” or just search for papers on MR/histology registration and see if you like any of the registration error evaluation methods.</p>
<p>MR/histology registration is a particularly difficult problem because it is a 2D/3D deformable registration. Registration evaluation techniques are both very tedious and very inaccurate.</p>
<aside class="quote no-group" data-username="KatS" data-post="3" data-topic="25969">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/a8b319/48.png" class="avatar"> KatS:</div>
<blockquote>
<p>Is there any way to quantify the visual impression of “the more fiducials the better”?</p>
</blockquote>
</aside>
<p>For manual point marking, I would say this is only true up to maybe 10-15 points. Usually you cannot place any number of fiducial points with equal accuracy (there are some easy ones that you can place quickly and accurately and you may be able to find more, but they take more effort to mark). Often there are practical limitations on available time, so marking more points may lead to less carefully placed points. Usually you cannot place the points evenly distributed (there may be some regions where you can find many fiducials and there may be large homogeneous areas where you cannot easily find any corresponding points), so you may have higher accuracy in regions where you can easily find points, potentially at the cost of having lower accuracy in the region of interest.</p>

---

## Post #5 by @KatS (2023-03-22 07:46 UTC)

<p>Thank you a lot for your reply!<br>
We are now trying to compare displacement vector fields of transforms based on varying numbers and locations of fiducials to the transform, which visually rendered the best result to get an idea of the variation. With that, we came across a problem when trying to save the output displacement field generated in the “Transforms”-module. When we try to save it via the “Save” panel", we get an error message, but we are able to save it via the Python interactor with a simple “saveNode”-command. It’s not a bis issue to use this work-around, however we wondered, why this error occurs.</p>

---

## Post #6 by @lassoan (2023-03-27 18:50 UTC)

<p>You get an error when you try to save the inverse transform or choose incorrect file format. I would recommend to export the displacement values into a vector image in Transform module. You can then save it into nrrd file format.</p>

---

## Post #7 by @KatS (2023-04-03 14:33 UTC)

<p>Thank you, that worked!</p>

---
