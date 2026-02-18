# Issue about Aruco tracker

**Topic ID**: 22732
**Date**: 2022-03-28
**URL**: https://discourse.slicer.org/t/issue-about-aruco-tracker/22732

---

## Post #1 by @user5 (2022-03-28 16:59 UTC)

<p>Does anybody have experience in the Aruco tracker?</p>
<p>I have tried to use the Aruco tracker by following this <a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day2_2_PLUS.pptx" rel="noopener nofollow ugc">link</a>.</p>
<p>I generate the tracker successfully, but the moving range is very limited and it cannot move close to my model.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b0011e1405bbbdb73ce88c2fe1fdcdaec3e671b5.jpeg" data-download-href="/uploads/short-url/p70qB8I6Qndl1nclsoQUU2KCjJj.jpeg?dl=1" title="IMG_1747" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b0011e1405bbbdb73ce88c2fe1fdcdaec3e671b5_2_281x500.jpeg" alt="IMG_1747" data-base62-sha1="p70qB8I6Qndl1nclsoQUU2KCjJj" width="281" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b0011e1405bbbdb73ce88c2fe1fdcdaec3e671b5_2_281x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b0011e1405bbbdb73ce88c2fe1fdcdaec3e671b5_2_421x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b0011e1405bbbdb73ce88c2fe1fdcdaec3e671b5_2_562x1000.jpeg 2x" data-dominant-color="8181B9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_1747</span><span class="informations">1080×1920 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Did anyone face a similar problem before? If yes, would you mind telling me that how to fix this problem?<br>
Thank you.</p>

---

## Post #2 by @user5 (2022-03-29 04:29 UTC)

<p>Since I am using the iPad to be the webcam, is it able to solve this issue by using NDI product for tracking?</p>
<p>Thank you</p>

---

## Post #3 by @slicer365 (2022-03-29 12:05 UTC)

<p>what about depth Camera（binocular camera）?</p>

---

## Post #4 by @user5 (2022-03-29 13:21 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57869be01e4f28369a0c1aa2d9a5307ec7636f03.jpeg" data-download-href="/uploads/short-url/cuhWadF5ay1HzbCgVDwih6RxSXp.jpeg?dl=1" title="61RUKI5LI3L.AC_SL1000" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/57869be01e4f28369a0c1aa2d9a5307ec7636f03_2_396x375.jpeg" alt="61RUKI5LI3L.AC_SL1000" data-base62-sha1="cuhWadF5ay1HzbCgVDwih6RxSXp" width="396" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/57869be01e4f28369a0c1aa2d9a5307ec7636f03_2_396x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/57869be01e4f28369a0c1aa2d9a5307ec7636f03_2_594x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/57869be01e4f28369a0c1aa2d9a5307ec7636f03_2_792x750.jpeg 2x" data-dominant-color="A5A3A0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">61RUKI5LI3L.AC_SL1000</span><span class="informations">1000×944 55.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Is it similar to this camera?</p>
<p>Did you face similar problem before and fix it by using this camera?</p>

---

## Post #5 by @user5 (2022-03-30 05:09 UTC)

<p>Since I have changed to use MacBook webcam and smaller size aruco tracker, moving range seems better, but I still need to move very close to the camera which is not useful for real applications.</p>
<p>Does this problem occur to the view angle of the camera? If I need to buy a new webcam, which is view angle of camera that you would like to suggest to buy?</p>
<p>Thank you</p>

---

## Post #6 by @JBeninca (2022-04-01 14:28 UTC)

<p>hello.<br>
We do have worked with aruco markers , in neuro navigation.<br>
To get some precision with them, first your image must be good enough. a common web cam , also a the Logitech Brio 4k  is not good<br>
We choose to use a Sony a 6300 no-mirror camera. it has a resolution of 4k. but it takes some time on the loop. The resolution was dawngrade to 2 k (1920 x 1080)<br>
The image quality, with good ilumination was excelent and the library works fine with these images.</p>
<p>We had to use filters: low-pass, butterworth, or kalman to cutt off higher frecuencies (noise) to retain that movement was significant to locate an object</p>
<p>but there was a problem with the rotation vectors that the library gives. it has some-inherent-noise and error to give the proper results</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/17e3a3fc41f13f96ef4962aa8b6aeb243fac1568.png" data-download-href="/uploads/short-url/3pkHmPvuxVMteF0rmscDenYSSCI.png?dl=1" title="_the_Scene" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/17e3a3fc41f13f96ef4962aa8b6aeb243fac1568_2_689x479.png" alt="_the_Scene" data-base62-sha1="3pkHmPvuxVMteF0rmscDenYSSCI" width="689" height="479" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/17e3a3fc41f13f96ef4962aa8b6aeb243fac1568_2_689x479.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/17e3a3fc41f13f96ef4962aa8b6aeb243fac1568_2_1033x718.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/17e3a3fc41f13f96ef4962aa8b6aeb243fac1568.png 2x" data-dominant-color="9794C2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">_the_Scene</span><span class="informations">1290×897 132 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
