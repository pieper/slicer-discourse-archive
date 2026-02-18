# Lung lesion segmentation

**Topic ID**: 21967
**Date**: 2022-02-14
**URL**: https://discourse.slicer.org/t/lung-lesion-segmentation/21967

---

## Post #1 by @Alexander_The_Great (2022-02-14 20:55 UTC)

<p>Hey. I am new to slicer segmentation. I try to segment lung nodules with the help of CIP lesion analyser, but unfortunately after the first successful nodule segmentation, I select the second nodule but I am unable to proceed with the segmentation button. Is there any way around? It is very useful in order to do a semi-automatic segmentation like that.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4bf83102b7245a77cfc7c360c650998c01f0a607.png" data-download-href="/uploads/short-url/aQ3yAYUUQqsdpjXAG9MECnqPNzx.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4bf83102b7245a77cfc7c360c650998c01f0a607_2_368x500.png" alt="image" data-base62-sha1="aQ3yAYUUQqsdpjXAG9MECnqPNzx" width="368" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4bf83102b7245a77cfc7c360c650998c01f0a607_2_368x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4bf83102b7245a77cfc7c360c650998c01f0a607_2_552x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4bf83102b7245a77cfc7c360c650998c01f0a607_2_736x1000.png 2x" data-dominant-color="EEF0F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1161×1576 66.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @rbumm (2022-02-14 21:49 UTC)

<p>Hi,<br>
This seems to be an outdated module that needs servicing.<br>
I can not get it running either even not in 4.10.2<br>
Please describe what you would expect to have in your clinical workflow.<br>
I am not the creator of that package.<br>
Best regards<br>
rudolf</p>

---

## Post #3 by @rbumm (2022-02-15 11:13 UTC)

<p>In the meantime, you could try to use the “Local threshold” effect of the “Segment Editor” with the following parameters:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/700d6598159c64f5c2c15f524b6444a4032514f5.jpeg" data-download-href="/uploads/short-url/fZgb7hk0y7vegNDTelrQnjh3Vjv.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/700d6598159c64f5c2c15f524b6444a4032514f5_2_690x469.jpeg" alt="image" data-base62-sha1="fZgb7hk0y7vegNDTelrQnjh3Vjv" width="690" height="469" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/700d6598159c64f5c2c15f524b6444a4032514f5_2_690x469.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/700d6598159c64f5c2c15f524b6444a4032514f5_2_1035x703.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/700d6598159c64f5c2c15f524b6444a4032514f5.jpeg 2x" data-dominant-color="979898"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1185×807 87.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>CTRL+left click into the nodule you want to segment - done.<br>
Please use Slicer preview 4.13. You need to install “Segment Editor Extra Effects” to have that effect available.</p>

---

## Post #4 by @Alexander_The_Great (2022-02-20 13:17 UTC)

<p>Thank you so much for the help. I used the CIP plug-in as it seemed more specific to lung nodule analysis. I will try your suggested method. I will use the MIP viewer from CIP extension and segment the nodules as you suggested. Tried installing the “segment editor extra effects” with no luck. I will use the latest slicer preview and try again.<br>
Thanks again for your help</p>

---

## Post #5 by @Alexander_The_Great (2022-02-20 14:53 UTC)

<p>Tried a lot of tricks in order to instal the “segment editor extra effects”. Just couldn’t. Could you please suggest a way? Thanks in advance.</p>

---

## Post #6 by @rbumm (2022-02-21 09:46 UTC)

<aside class="quote no-group" data-username="Alexander_The_Great" data-post="5" data-topic="21967">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alexander_the_great/48/14290_2.png" class="avatar"> Alexander_The_Great:</div>
<blockquote>
<p>Could you please suggest a way?</p>
</blockquote>
</aside>
<p>Install Slicer 4.13. (important)</p>
<p>Go extension manager:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11ffb2598710623e6a80064763dc43c39e0e5abd.png" alt="image" data-base62-sha1="2zdWz3O1Y2QHOTMWDISLB6Sy9yd" width="573" height="342"></p>
<p>Enter “extra” in the input box at the upper right edge of the window:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f8d07975528f425b4e318673992a490404ecab3.jpeg" data-download-href="/uploads/short-url/4v6XhIpLF7T8Un444Mhd706HTiP.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1f8d07975528f425b4e318673992a490404ecab3_2_690x207.jpeg" alt="image" data-base62-sha1="4v6XhIpLF7T8Un444Mhd706HTiP" width="690" height="207" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1f8d07975528f425b4e318673992a490404ecab3_2_690x207.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1f8d07975528f425b4e318673992a490404ecab3_2_1035x310.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1f8d07975528f425b4e318673992a490404ecab3_2_1380x414.jpeg 2x" data-dominant-color="F2F2F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1916×575 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Install and restart Slicer.</p>
<p>After that, you should find “Local threshold” in the Segment Editor.</p>

---

## Post #7 by @Alexander_The_Great (2022-02-22 19:22 UTC)

<p>I am grateful to you for your guidance. Followed your screenshots and installed the extra effects extension. However, I don’t think I can do the segmentation. I followed the instructions but when I ctlr + left click, the whole are of the image flashes and I cannot continue with the segmentation. Are there some additional options I need to select?<br>
Thanks again for the help</p>

---

## Post #8 by @rbumm (2022-02-22 19:58 UTC)

<p>I produced a short clip, hope that helps.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="NmG16cSwUHg" data-video-title='Segmenting a lung nodule with 3D Slicer and "Local Threshold"' data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=NmG16cSwUHg" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/NmG16cSwUHg/maxresdefault.jpg" title='Segmenting a lung nodule with 3D Slicer and "Local Threshold"' width="" height="">
  </a>
</div>


---

## Post #9 by @Alexander_The_Great (2022-02-22 20:36 UTC)

<p>Did exactly what you didi but the nodule just doesn’t want to get segmentated. I add a video of my try.</p>
<p><a href="https://youtu.be/uXjJVoOIJyk" rel="noopener nofollow ugc">https://youtu.be/uXjJVoOIJyk</a></p>

---

## Post #10 by @rbumm (2022-02-22 20:41 UTC)

<p>You are using “Watershed” in your Local threshold dropdown field, I am using “GrowCut”</p>

---

## Post #11 by @Alexander_The_Great (2022-02-23 17:24 UTC)

<p>I did it with grow cut. The output is the same as I presented in the video</p>

---

## Post #12 by @rbumm (2022-02-23 18:55 UTC)

<p>Are you able to share an anonymized dataset?</p>

---

## Post #13 by @Luis_Santos (2022-02-24 03:06 UTC)

<p>Try to use grow from seeds.</p><div class="youtube-onebox lazy-video-container" data-video-id="R-lBsqAvSTA" data-video-title="3D Slicer Tutorial #3: Scissors. Grow from seeds." data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=R-lBsqAvSTA" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/R-lBsqAvSTA/maxresdefault.jpg" title="3D Slicer Tutorial #3: Scissors. Grow from seeds." width="" height="">
  </a>
</div>


---

## Post #14 by @rbumm (2022-02-24 07:44 UTC)

<aside class="quote no-group" data-username="Alexander_The_Great" data-post="9" data-topic="21967">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alexander_the_great/48/14290_2.png" class="avatar"> Alexander_The_Great:</div>
<blockquote>
<p>Did exactly what you did</p>
</blockquote>
</aside>
<p>Please try to adjust the “Local threshold” threshold slider in a way that the nodule gets completely filled, even gets a bit “overfilled”. Then CTRL+Left Click into the nodule again.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b40214fa4eda4093a9bd92bfb792db43226e1911.jpeg" data-download-href="/uploads/short-url/pGqp7GJqYmQKvVTxaHneZhnkMyB.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b40214fa4eda4093a9bd92bfb792db43226e1911_2_635x500.jpeg" alt="image" data-base62-sha1="pGqp7GJqYmQKvVTxaHneZhnkMyB" width="635" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b40214fa4eda4093a9bd92bfb792db43226e1911_2_635x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b40214fa4eda4093a9bd92bfb792db43226e1911.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b40214fa4eda4093a9bd92bfb792db43226e1911.jpeg 2x" data-dominant-color="6A7281"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">849×668 78.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Make sure that “Editable intensity range” is unchecked.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e62e2e4086d1baacfeaef12658ae15f87b6114e.png" alt="image" data-base62-sha1="bbr6xV5CTBxq9kWOZLEtN3OGMCG" width="183" height="36"></p>

---

## Post #15 by @Alexander_The_Great (2022-03-01 11:04 UTC)

<p>sorry to bother you again, but unfortunately I couldn’t manage to do it. Tried everything you said, experimented with other suggestions found online, but I couldn’t.<br>
The CIP plugin is a more user friendly way of doing the segmentations. Is there a way to install an older version of Slicer 3D that worked well with that?</p>
<p>Thanks in advance</p>

---

## Post #16 by @rbumm (2022-03-01 12:58 UTC)

<p>No, I am not aware of such a version.<br>
The Slicer version that is recommended on the Chest Imaging Platform homepage and linked there for download does not include a fully working Lung Lesion Analyzer extension. I am not prepared to go further back in time for testing.</p>

---
