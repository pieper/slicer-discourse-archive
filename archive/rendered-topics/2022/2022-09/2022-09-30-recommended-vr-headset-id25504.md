---
topic_id: 25504
title: "Recommended Vr Headset"
date: 2022-09-30
url: https://discourse.slicer.org/t/25504
---

# Recommended VR headset

**Topic ID**: 25504
**Date**: 2022-09-30
**URL**: https://discourse.slicer.org/t/recommended-vr-headset/25504

---

## Post #1 by @dhcortes (2022-09-30 14:34 UTC)

<p>Hi there,<br>
I am planning on using the VR and AR extensions of 3D slicer. Is there a headset brand/model  recommended for this?<br>
Thanks</p>

---

## Post #2 by @pieper (2022-09-30 14:56 UTC)

<p>I used a quest 2 headset with SlicerVR and it’s pretty seamless (and it’s cheap).</p>
<aside class="quote" data-post="3" data-topic="22653">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/gtc-keynote-monai-and-slicer/22653/3">GTC Keynote MONAI and Slicer</a> <a class="badge-category__wrapper " href="/c/announcements/7"><span data-category-id="7" data-drop-close="true" class="badge-category " title="Low-traffic category for 3D Slicer, extension, and community news and announcements."><span class="badge-category__name">Announcements</span></span></a>
  </div>
  <blockquote>
    If anyone has trouble accessing the GTC link to the SlicerVR+CloudXR video you should be able to access it here: <a href="https://vimeo.com/user26958043/review/678951613/08807e6148" class="inline-onebox">AWS Steve Pieper V1.mp4 on Vimeo</a>
  </blockquote>
</aside>


---

## Post #3 by @rlinke (2023-08-25 14:37 UTC)

<p>Were you able to use the quest link to connect or did you have to use Steam?</p>
<p>Thanks!</p>

---

## Post #4 by @rbumm (2023-08-27 08:04 UTC)

<p>You can use the USB link cable as well as Airlink to connect a Quest 2 to 3D Slicer. However, the last Slicer VR version that fully supported the Quest 2 has been seen in 4.11.</p>

---

## Post #5 by @cpinter (2023-08-28 09:29 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="4" data-topic="25504">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>that fully supported the Quest 2 has been seen in 4.11</p>
</blockquote>
</aside>
<p>Can you please elaborate Rudolf? I was not aware of any issues, I thought the latest version behaved identically to the last working 4.11 for VR. Apparently this is not the case so I’d like to make sure we all have them recorded as tickets in the SlicerVR GitHub repo. Thank you!</p>

---

## Post #6 by @rbumm (2023-08-30 08:47 UTC)

<p>This all concerns the Quest 2 VR headset.</p>
<p>As far as I remember in 5.2.2 VR never worked properly on the Quest 2 and we had a short period in which the JSON files for the controllers had to be transferred to the Slicer directories. That is why I always kept a 4.11 version on my computers for cases in which I needed VR.</p>
<p>Then there was an update for 5.3 preview which I tested and in which both JSON files and basic functionality of VR was restored.</p>
<p>I was then able to:</p>
<p>Move an object to and away from the observer position with on pair of joystick actions (right joystick)<br>
Grab the object with both controllers grab keys and rotate it<br>
Call up the exit menu with the left controller’s B button.</p>
<p>When I tried 5.4 stable recently the only thing that halfway worked was moving the 3D model to and from the observer in the mentioned 45-degree trajectory. So you can see a 3D object in space in the Quest2 headset, but can not really do much with it.</p>

---

## Post #7 by @rbumm (2023-08-30 09:01 UTC)

<p>What I hoped for in 3D Slicer and would be very welcome for daily use would be<br>
something like this:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="fbfLqdhgOW4" data-video-title="Human Anatomy VR 2022" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=fbfLqdhgOW4" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/fbfLqdhgOW4/maxresdefault.jpg" title="Human Anatomy VR 2022" width="" height="">
  </a>
</div>

<p>Available in the Oculus Lab</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e49a7b3f066498d37d1cace245b3a802e0f590ac.jpeg" data-download-href="/uploads/short-url/wCjPY2GrIGw73u5vUucXLE9fcpm.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e49a7b3f066498d37d1cace245b3a802e0f590ac_2_690x224.jpeg" alt="image" data-base62-sha1="wCjPY2GrIGw73u5vUucXLE9fcpm" width="690" height="224" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e49a7b3f066498d37d1cace245b3a802e0f590ac_2_690x224.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e49a7b3f066498d37d1cace245b3a802e0f590ac_2_1035x336.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e49a7b3f066498d37d1cace245b3a802e0f590ac.jpeg 2x" data-dominant-color="354A55"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1120×365 90.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<div class="youtube-onebox lazy-video-container" data-video-id="9zufDNWCaro" data-video-title="VR DICOM" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=9zufDNWCaro" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/9zufDNWCaro/maxresdefault.jpg" title="VR DICOM" width="" height="">
  </a>
</div>


---

## Post #8 by @cpinter (2023-08-31 08:58 UTC)

<p>Thank you Rudolf for the explanations!</p>
<aside class="quote no-group" data-username="rbumm" data-post="6" data-topic="25504">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>Grab the object with both controllers grab keys and rotate it</p>
</blockquote>
</aside>
<p>Just as a side note, this has never been possible. What you can do with pressing grab on both controllers is scaling/moving/rotating the world, not an object. So if you have various objects they would all “move” (when in reality it is you that moves/grows/shrinks).</p>
<aside class="quote no-group" data-username="rbumm" data-post="6" data-topic="25504">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>the only thing that halfway worked</p>
</blockquote>
</aside>
<p>Sorry I still have been too busy to hook up the VR system again and try all the things but at the end of June these things worked for me perfectly:</p>
<ul>
<li>Fly using the joystick</li>
<li>Grab an object and move it</li>
<li>Do the action I described above, which we call 3D pinch, where we can move/scale the world</li>
</ul>
<p>I don’t have access to an Oculus Quest 2, but we tried an HTC Vive Pro (1) and an HP Reverb 2 (Windows Mixed Reality type headset), and those worked great.<br>
Is it possible that the JSON that you use for the Quest 2 is not appropriate? Can someone else with a Quest 2 please try?</p>

---
