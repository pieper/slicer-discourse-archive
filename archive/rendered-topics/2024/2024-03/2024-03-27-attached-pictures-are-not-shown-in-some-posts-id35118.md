---
topic_id: 35118
title: "Attached Pictures Are Not Shown In Some Posts"
date: 2024-03-27
url: https://discourse.slicer.org/t/35118
---

# Attached pictures are not shown in some posts

**Topic ID**: 35118
**Date**: 2024-03-27
**URL**: https://discourse.slicer.org/t/attached-pictures-are-not-shown-in-some-posts/35118

---

## Post #1 by @VincentYu (2024-03-27 04:49 UTC)

<p>Environment: Windows 10, Firefox (124.0.1, 64-bit).</p>
<p>Some attached pictures are disappeared, and this happens in several posts (but not all posts). I have tried different browsers (Chrome, Firefox and MS Edge) and laptops (borrow from my colleague), but this problem still exists.</p>
<p><a href="https://discourse.slicer.org/t/new-feature-basic-support-for-physically-based-rendering-pbr/21725">For example</a>, in the picture below, there should be a picture inside the red rectangle area, but it is only a space now.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/956dd1123a515fe9bbf040284fd3d8182fdcd12e.png" data-download-href="/uploads/short-url/ljUqiQAbTK5TQOxfNwG8o1By3Bc.png?dl=1" title="圖片" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/956dd1123a515fe9bbf040284fd3d8182fdcd12e_2_690x355.png" alt="圖片" data-base62-sha1="ljUqiQAbTK5TQOxfNwG8o1By3Bc" width="690" height="355" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/956dd1123a515fe9bbf040284fd3d8182fdcd12e_2_690x355.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/956dd1123a515fe9bbf040284fd3d8182fdcd12e_2_1035x532.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/956dd1123a515fe9bbf040284fd3d8182fdcd12e_2_1380x710.png 2x" data-dominant-color="1D1C1C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">圖片</span><span class="informations">1481×763 39.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If I right-click the space, the “picture” can be open in new tab, but it’s a “transparent.png” all the time, with 1x1 pixel.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7e869fe0592b7a710c03e76dda98a37844a36f9.png" alt="圖片" data-base62-sha1="zn5SyBauzVqQN5wyDwTO0hEmBMl" width="639" height="133"></p>
<p>Is this a known issue? I did a quick search but found no related discussion in Slicer forum.</p>

---

## Post #2 by @VincentYu (2024-03-27 04:50 UTC)

<p>Another example:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56ac1a17234ba5e52e0a3fcb14b44ece6dfc5620.png" data-download-href="/uploads/short-url/cmJMVlweWIxALOaYIxQlsW2f4Ws.png?dl=1" title="圖片" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56ac1a17234ba5e52e0a3fcb14b44ece6dfc5620.png" alt="圖片" data-base62-sha1="cmJMVlweWIxALOaYIxQlsW2f4Ws" width="690" height="409" data-dominant-color="282626"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">圖片</span><span class="informations">1274×757 37.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p><aside class="quote quote-modified" data-post="4" data-topic="18804">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/charleschen/48/8444_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-display-the-blended-colors-in-the-view-of-volume-rendering/18804/4">How to display the blended colors in the view of 'volume rendering'?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hello Dr. Andras Lasso, 
Thank you so much for your reply! 

If these are two independent image acquisitions 

Yes, the red and green channels shown in the figures above are two independent 16-bit TIFF images(named ‘cell-new-red.tif’ and ‘cell-new-green.tif’), as shown in Figure1 and 2(I got them from FIJI). 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/156ad2adbdf08b54e3f978dcb1b545ead8e10cee.jpeg" data-download-href="/uploads/short-url/33sTqCOaLylfgxKrio5tqgr91XU.jpeg?dl=1" title="16 bit red channel" rel="noopener nofollow ugc">[16 bit red channel]</a> 
[16 bit Green Channel] 
After I followed the method you suggested, in the view of ‘Volume rendering’, the blended colors of the two channels still cannot be displayed…
  </blockquote>
</aside>


---

## Post #3 by @pieper (2024-03-27 13:06 UTC)

<p>I’ve seen this a few times too - our forum is hosted by discourse and I guess this is a bug that should be reported to them.</p>

---

## Post #4 by @lassoan (2024-03-27 13:10 UTC)

<p>I’ve noticed missing pictures here and there, too.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> could you report this to discourse? I know that you have a lot on your plate, I’m just asking because mostly you have been communicating with discourse folks.</p>

---

## Post #5 by @jcfr (2024-03-27 13:24 UTC)

<p>Thanks for bringing this to my attention. I just sent a message to the Discourse support team, I will follow up when I hear back.</p>

---

## Post #6 by @VincentYu (2024-03-27 14:49 UTC)

<p>Thank you for the quick response and support !<br>
I’m looking forward to the good news so that I can thoroughly catch up with the highlights of updates across Slicer 5.2 and Slicer 5.6. I’ve missed the new releases for a long time…</p>

---

## Post #7 by @jcfr (2024-03-28 15:56 UTC)

<p>Here is an update from support:</p>
<blockquote>
<p>We understand users on your forum are experiencing issues with images. We appreciate you providing us with link to the topic your users have created. I just wanted to let you know we are looking into this for you and will get back to you once we have more information.</p>
<p>In the meantime, are you able to grab additional information on how the users uploaded the images and possibly send over a copy of the image in that topic? Also, when would you say the issue was originally noticed?</p>
</blockquote>
<p>Would it be possible to help me answer these questions:</p>
<ul>
<li>Are you able to grab additional information on how the users uploaded the images and possibly send over a copy of the image in that topic?</li>
<li>When would you say the issue was originally noticed?</li>
</ul>

---

## Post #8 by @lassoan (2024-03-28 16:08 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="7" data-topic="35118">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Are you able to grab additional information on how the users uploaded the images and possibly send over a copy of the image in that topic?</p>
</blockquote>
</aside>
<p>I don’t think we have the images in any of these cases. The images are uploaded, others can see it (proven by the discussions in the topic), and then sometimes the images later disappear.</p>
<aside class="quote no-group" data-username="jcfr" data-post="7" data-topic="35118">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>When would you say the issue was originally noticed?</p>
</blockquote>
</aside>
<p>I noticed missing images several times over the past 1-2 years.</p>
<p>I don’t think it ever occurs for active topics, because if there is any issue with an image upload while the discussion is ongoing then we still have the images and upload again. For me, this was always an issue with older topics.</p>

---

## Post #9 by @mikebind (2024-03-28 16:42 UTC)

<p>I have had the same experience:  I have noticed missing images only in older posts and have occasionally seen this for a while (I’d estimate at least a year).   I have not ever noticed this in new or recent posts.  I assumed that perhaps under some conditions discourse discarded old images, and that they were therefore no longer available.   I feel like I have seen threads were some images were present and others had disappeared; if I come across one of those again, I will post back here with the example.</p>

---

## Post #10 by @mikebind (2024-03-28 16:51 UTC)

<p>Here is an example from a post I made in 2019:  <a href="https://discourse.slicer.org/t/mixed-volume-rendering-and-surface-representation-of-segmentation-has-incorrect-3d-appearance-if-segment-is-not-fully-opaque/6532/3" class="inline-onebox">Mixed volume rendering and surface representation of segmentation has incorrect 3D appearance if segment is not fully opaque - #3 by mikebind</a></p>
<p>I posted three screenshots in that thread, almost certainly all as Win-Shift-S captures and then pasted into the text box. The first two have disappeared, and the third is still visible. A screenshot from Andras is also still visible.</p>

---

## Post #11 by @jamesobutler (2024-04-02 17:49 UTC)

<p>Here’s an example from 2022 which doesn’t seem too old for it to not be working:</p><aside class="quote quote-modified" data-post="1" data-topic="21350">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shahnawaz_vora/48/13667_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-change-view-controller-slider-horizontal-to-vertical/21350">How to change view controller slider horizontal to vertical</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    How i can move slicer viewcontroller slider horizontal to vertical with python script 
[Screenshot (66)]
  </blockquote>
</aside>


---

## Post #12 by @jcfr (2024-04-18 21:39 UTC)

<p>To follow-up on this, the Discourse support team is still looking into this and will follow-up as soon as they have an update.</p>

---

## Post #13 by @jcfr (2024-05-20 16:29 UTC)

<p>The discourse support team followed up earlier today indicating the issue has been fixed.</p>
<p>Thanks everyone for your patience <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>

---

## Post #14 by @pieper (2024-05-20 16:36 UTC)

<p>Thanks Jc!  Yes, it looks like the links are working now.</p>

---

## Post #15 by @VincentYu (2024-05-21 13:18 UTC)

<p>Thank you! The resources in this forum are precious for us learners</p>

---
