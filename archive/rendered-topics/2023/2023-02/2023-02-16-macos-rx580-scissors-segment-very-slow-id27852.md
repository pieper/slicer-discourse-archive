---
topic_id: 27852
title: "Macos Rx580 Scissors Segment Very Slow"
date: 2023-02-16
url: https://discourse.slicer.org/t/27852
---

# MacOS RX580 Scissors Segment very slow

**Topic ID**: 27852
**Date**: 2023-02-16
**URL**: https://discourse.slicer.org/t/macos-rx580-scissors-segment-very-slow/27852

---

## Post #1 by @zyy (2023-02-16 07:10 UTC)

<p>my computer<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d2aa117ab8ac9333c4a585cfcd0aaf87aeb8fde6.png" data-download-href="/uploads/short-url/u3CDA0Tdao6rh9VP0GKdLmRZKWW.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d2aa117ab8ac9333c4a585cfcd0aaf87aeb8fde6_2_271x500.png" alt="image" data-base62-sha1="u3CDA0Tdao6rh9VP0GKdLmRZKWW" width="271" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d2aa117ab8ac9333c4a585cfcd0aaf87aeb8fde6_2_271x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d2aa117ab8ac9333c4a585cfcd0aaf87aeb8fde6.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d2aa117ab8ac9333c4a585cfcd0aaf87aeb8fde6.png 2x" data-dominant-color="888A89"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">280×515 59.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I want segment the vessel from cta film,but scissor tool so slow compare by in windows.<br>
windows just need 1 second will give response.mac need 3 second to 1 minute or more，It is unormal.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45c5e4b015b8eb1a5ab7352a8294fdab3c41525c.jpeg" data-download-href="/uploads/short-url/9XeVEDs8hJWmpoqT4BXRG7sxxJq.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45c5e4b015b8eb1a5ab7352a8294fdab3c41525c_2_690x381.jpeg" alt="image" data-base62-sha1="9XeVEDs8hJWmpoqT4BXRG7sxxJq" width="690" height="381" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45c5e4b015b8eb1a5ab7352a8294fdab3c41525c_2_690x381.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45c5e4b015b8eb1a5ab7352a8294fdab3c41525c_2_1035x571.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45c5e4b015b8eb1a5ab7352a8294fdab3c41525c_2_1380x762.jpeg 2x" data-dominant-color="34323B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1061 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<a href="https://drive.google.com/file/d/17s8dvz2-1PI8mKNaV9Jx3OOXI5ZBImSv/view?usp=sharing" rel="noopener nofollow ugc">cta image file</a></p>

---

## Post #2 by @zyy (2023-02-16 08:29 UTC)

<p>3DSicer Version is 5.2.1<br>
5.2.1 r31317 / 77da381</p>

---

## Post #3 by @pieper (2023-02-16 15:05 UTC)

<p>I have a similar mac pro and it took only a few seconds to perform the scissors operation.  If it takes a very long time you could use the ActivityMonitor to sample the process to see what operation is taking time.  For me it was too quick to even measure.  Maybe there’s something else going on with your machine?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b3ae6103f0d3b85f4736049368f17e801032172.jpeg" data-download-href="/uploads/short-url/d13DERrNFnVhnneGVJYdLo8XQQy.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b3ae6103f0d3b85f4736049368f17e801032172_2_690x390.jpeg" alt="image" data-base62-sha1="d13DERrNFnVhnneGVJYdLo8XQQy" width="690" height="390" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b3ae6103f0d3b85f4736049368f17e801032172_2_690x390.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b3ae6103f0d3b85f4736049368f17e801032172_2_1035x585.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b3ae6103f0d3b85f4736049368f17e801032172.jpeg 2x" data-dominant-color="363C3A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1046×592 110 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @zyy (2023-02-17 01:53 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/395afa045bd2ded07b4c60c526a43af71e82fdfe.jpeg" data-download-href="/uploads/short-url/8bo8cJlR97pH8RIs9F4XVLjNDR4.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/395afa045bd2ded07b4c60c526a43af71e82fdfe_2_690x388.jpeg" alt="image" data-base62-sha1="8bo8cJlR97pH8RIs9F4XVLjNDR4" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/395afa045bd2ded07b4c60c526a43af71e82fdfe_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/395afa045bd2ded07b4c60c526a43af71e82fdfe_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/395afa045bd2ded07b4c60c526a43af71e82fdfe_2_1380x776.jpeg 2x" data-dominant-color="483935"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
seem e-core in cpu not work<br>
maybe only Intel 12gen、13gen CPU in hackintosh have this problem,<br>
becuse another computer have amd 5900 in hackintosh work well.<br>
macos no official support Intel big.LITTLE cpu framework,<br>
current solution is opencore,it closed CPU HT,and set logic core number to thread number.<br>
13600kf have 6 p-core and 8 e-core 20 thead,in OpenCore 8.8 set it 20 logic core<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f43165b49459f537166a10185f8c4587e68b642c.png" alt="image" data-base62-sha1="yQekPxo72v0Grs5Pox0bdcHj8rG" width="389" height="203"></p>

---

## Post #5 by @zyy (2023-02-17 13:39 UTC)

<p>I saw this issues</p><aside class="quote quote-modified" data-post="11" data-topic="22564">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/performance-issues-on-mac-m1/22564/11">Performance issues on Mac M1?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Thanks for reporting.  There does seem to be some instability on macs with Apple chips.  I have run some simple tests and things run fine, but we have seen <a href="https://github.com/pieper/SlicerParallelProcessing/commit/2cf7d7d61e7b17cc949cb8fd31acefe9e4de25a1" rel="noopener nofollow ugc">previous issues</a> indicating that the on-the-fly run time code conversion is not the same as running on native hardware.  So until Apple fixes their emulation layer or Slicer is ported to the new architecture there are likely to be edge cases that fail. 
I tested the basic flow described by <a class="mention" href="/u/semredogan">@semredogan</a> and got the crash report below basically i…
  </blockquote>
</aside>
<p>
and I test this film in macbook pro 16 m1pro(Slicer5.2.1)<br>
scissors operation is twice as fast as 13600kf in hackintosh.<br>
but slow too much than 13600kf in windows11(too quick to even measure),<br>
and do 3-6 times big scissors will crashed.<br>
m1pro in macos problem looked so same with 13600kf in hackintosh.<br>
m1pro also is big.LITTLE design,have 8 p-core,2 e-core.<br>
So I suspect big.LITTLE design is the reason<br>
If m1pro could fix this problem,please take intel 13gen cpu in hackintosh,thanks a lot.<br>
white mac is too expensive in memory and disk for medical image developer</p>

---

## Post #6 by @pieper (2023-02-17 15:12 UTC)

<p>Interesting - thanks for reporting.  I don’t have experience with hackintosh but I can believe there would be CPU related performance issues.  I agree mac computers are not cost effective for development, and I typically use linux for this kind of work.</p>

---
