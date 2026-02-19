---
topic_id: 20405
title: "Heart Valve Segmentation Tool"
date: 2021-10-28
url: https://discourse.slicer.org/t/20405
---

# Heart valve segmentation tool

**Topic ID**: 20405
**Date**: 2021-10-28
**URL**: https://discourse.slicer.org/t/heart-valve-segmentation-tool/20405

---

## Post #1 by @HodaJavadi (2021-10-28 19:24 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.11.20210226<br>
Expected behavior: Valve segmentation tool in SlicerHeart<br>
Actual behavior: Can’t find the tool</p>
<p>I have been trying to use slicer for Mitral valve leaflet segmentation but I cannot find the tool in the Cardiac extension. How can I add it or find it.</p>

---

## Post #2 by @lassoan (2021-10-28 21:49 UTC)

<p>We have not released the SlicerHeart valve segmentation module yet. We plan to release it along with our SlicerHeart journal paper, probably within a few months.</p>

---

## Post #3 by @lassoan (2021-10-29 00:39 UTC)

<blockquote>
<p>Thank you for your response. Is there any other way to segment the leaflets along the annulus with slicer?</p>
</blockquote>
<p>The valve segmentation tool is just a customized version of the Segment Editor module with convenience features such as it sets up slice orientation based on the annulus plane, resamples the image to have finer resolution, adds a tubular shape mask around the annulus to make it easier to exclude irrelevant regions from the segmentation, sets up views, etc. These all help but none of these are required - you can segment leaflets using the stock Segment Editor module.</p>

---

## Post #4 by @cherrygirl (2022-04-01 12:44 UTC)

<p>Excuse me, please are you releasing any relevant content or articles about slicerheart valve segmentation?</p>

---

## Post #5 by @lassoan (2022-04-01 13:59 UTC)

<p>The paper has been submitted and it is under review. We can hear from it anytime and if it is accepted then the code will be made open-source in a few weeks. If we need to resubmit the paper elsewhere then it can take several more months.</p>

---

## Post #6 by @cherrygirl (2022-04-08 09:14 UTC)

<p>Good luch to you and looking forward to your good news!</p>

---

## Post #7 by @whu (2022-05-10 06:11 UTC)

<p>Can that paper seen on the arXiv ?<br>
thanks</p>

---

## Post #8 by @whu (2022-06-11 06:15 UTC)

<p>Dear Sir,</p>
<p>does the  journal paper accept ? <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20">   waiting for your good annocement.</p>
<pre><code>And waiting for the 
</code></pre>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="20405">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>SlicerHeart valve segmentation module</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="20405">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>SlicerHeart journal paper</p>
</blockquote>
</aside>

---

## Post #9 by @whu (2022-06-11 07:42 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="20405">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>We have not released the SlicerHeart valve segmentation module yet.</p>
</blockquote>
</aside>
<p>But I found a link using valve segmentation two years ago…<br>
The net link:<a href="https://youtu.be/Ev-7mrz-bb0" rel="noopener nofollow ugc">https://youtu.be/Ev-7mrz-bb0</a><br>
And the capture:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5cb24e1288aea4cd64feb37400cd59bd43afbef4.jpeg" data-download-href="/uploads/short-url/de1WwqaGTGcTGQu9JpMHCsqil8w.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5cb24e1288aea4cd64feb37400cd59bd43afbef4_2_690x388.jpeg" alt="image" data-base62-sha1="de1WwqaGTGcTGQu9JpMHCsqil8w" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5cb24e1288aea4cd64feb37400cd59bd43afbef4_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5cb24e1288aea4cd64feb37400cd59bd43afbef4_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5cb24e1288aea4cd64feb37400cd59bd43afbef4_2_1380x776.jpeg 2x" data-dominant-color="6E6E76"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1754×988 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Or is there any early version that published the valve segmentation…</p>
<p>Thanks for your kind answers.</p>

---

## Post #10 by @lassoan (2022-06-12 00:54 UTC)

<p>We’ve been using this module for several years and shared with a few collaborators. We’ll make it public when SlicerHeart platform paper gets published (it was rejected from one journal, we resubmitted it to another and it is under review).</p>
<p>Unfortunately, clinical journals don’t really like these kind of platform papers, so it can take 1-2 years until we are lucky to find a good journal with an editorial board and reviewers who understand the importance of software tools and platforms.</p>

---

## Post #11 by @whu (2022-06-12 13:13 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="20405">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>shared with a few collaborators</p>
</blockquote>
</aside>
<p>can I get  a copy of share?<br>
Best wishes.</p>

---

## Post #12 by @lassoan (2022-06-13 12:57 UTC)

<p>Please contact the Principal Investigator of the project, Matthew A Jolley at CHOP for early access.</p>

---

## Post #13 by @whu (2022-06-14 01:29 UTC)

<aside class="quote no-group" data-username="whu" data-post="9" data-topic="20405">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/7ab992/48.png" class="avatar"> whu:</div>
<blockquote>
<p>The net link:<a href="https://youtu.be/Ev-7mrz-bb0" rel="noopener nofollow ugc">Mitral Valve Analysis: 3DSlicer - YouTube </a></p>
</blockquote>
</aside>
<p>thanks very much, I will try.</p>

---

## Post #14 by @whu (2022-12-01 13:04 UTC)

<p>Dear Sir,</p>
<pre><code>Since the new version with Valve Segmentation released. Can you or your team share a public/sample data of the US data contating Mitral Valve/ Annulus , just for the userguide, as to the Cardio CTA data.

thanks. Best wishes.
</code></pre>

---

## Post #15 by @Yangtting (2023-10-12 07:46 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="20405" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Please contact the Principal Investigator of the project, Matthew A Jolley at CHOP for early access.</p>
</blockquote>
</aside>
<p>Hello,I found that your paper had published! Congratulations! By the way, I noticed that Valve Segmentation funtion hasn’t updated in the New SlicerHeart, so I wander when it will be released, thank you <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20">.</p>

---
