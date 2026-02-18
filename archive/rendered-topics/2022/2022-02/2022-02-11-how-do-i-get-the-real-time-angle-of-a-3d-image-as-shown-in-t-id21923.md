# How do I get the real-time Angle of a 3D image, as shown in the figure?

**Topic ID**: 21923
**Date**: 2022-02-11
**URL**: https://discourse.slicer.org/t/how-do-i-get-the-real-time-angle-of-a-3d-image-as-shown-in-the-figure/21923

---

## Post #1 by @gavinricky (2022-02-11 18:09 UTC)

<p>Operating system:windows 10<br>
Slicer version:4.8.1<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/3512e9c8d623540bc0ceeb02d782c8f2f94fa824.jpeg" data-download-href="/uploads/short-url/7zvPie63zq299XKdndo1FXsGxEw.jpeg?dl=1" title="福昕截屏20220212020655449.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3512e9c8d623540bc0ceeb02d782c8f2f94fa824_2_690x414.jpeg" alt="福昕截屏20220212020655449.PNG" data-base62-sha1="7zvPie63zq299XKdndo1FXsGxEw" width="690" height="414" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3512e9c8d623540bc0ceeb02d782c8f2f94fa824_2_690x414.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3512e9c8d623540bc0ceeb02d782c8f2f94fa824_2_1035x621.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/3512e9c8d623540bc0ceeb02d782c8f2f94fa824.jpeg 2x" data-dominant-color="64635F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">福昕截屏20220212020655449.PNG</span><span class="informations">1321×793 116 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2022-02-11 18:19 UTC)

<p>You can add a small Python script that observes the slice node and adds this angle information. I would not recommend doing this, as the values are only meaningful if only one (if you introduce certain constraints then two) of the 3 angles is significantly different from zero. For example, it is impossible for a human to decipher what orientation the (LR 28, IS 88, AP 31) angles refer to.</p>
<p>Would you like to use this for getting C-arm anatomical angles (CRA/CAU, RAO/LAO, L-arm)? That is a quite tightly constrained use case, so for that a small Python scripted module could be added. Would you be interested in working on that? (it would be just a tiny Python scripted module, which would observe a view node and display the angles in a corner annotation).</p>

---

## Post #3 by @gavinricky (2022-02-11 18:26 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="21923">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>getting C-arm anatomical angles</p>
</blockquote>
</aside>
<p>Thank you for your reply. That’s exactly what I want to do. I wanna get C-arm anatomical angles before the operation.I would appreciate your assistance if you could help me.</p>

---

## Post #4 by @lassoan (2022-02-11 19:03 UTC)

<p>Do you have experience with Python scripting?</p>

---

## Post #5 by @gavinricky (2022-02-11 22:57 UTC)

<p>Sorry, I have no experience with Python scripting.</p>

---

## Post #6 by @gavinricky (2022-02-14 17:30 UTC)

<p>I would appreciate it if you could spare some time to help me resolve the problem.<br>
Even though I have no experience with Python scripting, I can learn.<br>
I look forward to your reply</p>

---

## Post #7 by @timeanddoctor (2022-02-19 14:57 UTC)

<p>I am the author of this video. This is a script written a long time ago. If you find it useful, we can communicate.</p>
<p>我是这个视频的作者，这个是很久前写的一个脚本，你如果觉得有用，我们可以沟通下。</p>

---

## Post #8 by @gavinricky (2022-02-19 15:50 UTC)

<p>Thank you so much, I have been looking for you for a long time!  I also left a comment on station B, I hope to get your help</p>
<p>太感谢了，找了您很久！B站上也留过言，希望能得到您的帮助 <img src="https://emoji.discourse-cdn.com/twitter/hand_with_index_finger_and_thumb_crossed.png?v=12" title=":hand_with_index_finger_and_thumb_crossed:" class="emoji" alt=":hand_with_index_finger_and_thumb_crossed:" loading="lazy" width="20" height="20"><br>
<a href="mailto:wenchang.guo@163.com">wenchang.guo@163.com</a></p>

---

## Post #9 by @lili-yu22 (2022-02-28 10:24 UTC)

<p>teacher Li，have you use SPHARM PDM，can you tell me the priciple，thank you very much</p>

---

## Post #10 by @timeanddoctor (2022-03-02 13:13 UTC)

<p>I did not use this, Thanks.</p>

---

## Post #11 by @lassoan (2022-07-21 19:05 UTC)

<p>You can find a script that prints anatomical angles (RAO/LAO, CRA/CAU) in the corner of a 3D view in <a href="https://discourse.slicer.org/t/angles-measurement-in-3d-view/24435/3">this post</a>.</p>

---

## Post #12 by @learn_shape (2024-03-26 00:31 UTC)

<p>hi, i need your help. 来自一个学习者</p>

---
