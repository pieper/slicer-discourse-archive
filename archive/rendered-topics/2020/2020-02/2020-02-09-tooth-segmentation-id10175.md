---
topic_id: 10175
title: "Tooth Segmentation"
date: 2020-02-09
url: https://discourse.slicer.org/t/10175
---

# Tooth segmentation

**Topic ID**: 10175
**Date**: 2020-02-09
**URL**: https://discourse.slicer.org/t/tooth-segmentation/10175

---

## Post #1 by @flaviu2 (2020-02-09 22:13 UTC)

<p>I am struggling to find a segmentation solution to isolate from an CBCT a tooth from a teeth. But I didn’t found any example of how to do this using SimpleITK/ITK. Can you point me a starting of how to achieve this task ? Is important to me to solve this. Can you help me ?</p>

---

## Post #2 by @manjula (2020-02-09 22:53 UTC)

<p>Hi,</p>
<p>Check this example.</p>
<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="9775">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"><a href="https://discourse.slicer.org/t/teeth-segmentation/9775/9">Teeth Segmentation</a></div>
<blockquote>
<p>I’ve checked this and found that all teeth can be quite quickly and accurately segmented at once by the following ste</p>
</blockquote>
</aside>
<p>Also you can use split volume effect to separate individual teeth once you segment them out.</p>

---

## Post #3 by @flaviu2 (2020-02-10 08:03 UTC)

<p>Hi Manjula. I appreciated your post. That example reveal how to segment a tooth with 3DSlicer. I saw that you have done that segmentation and you solved your task. For you has been enough doing that in 3DSlicer, but my task is to do that inside my VC++ application … so, is there a way to do that segmentation in my app from 3DSlicer ? The source code is huge, and I don’t think I can find the code that do the proper segmentation … I guess … did you identified the code source that done segmentation ?</p>

---

## Post #4 by @manjula (2020-02-10 20:10 UTC)

<aside class="quote no-group" data-username="flaviu2" data-post="3" data-topic="10175">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/74df32/48.png" class="avatar"> flaviu2:</div>
<blockquote>
<p>task is to do that inside my VC++ application</p>
</blockquote>
</aside>
<p>I am sorry  i will not be able to help in that part as i have not gone through the c++ code of slicer as i don’t understand it. But others here will help you for sure with that.</p>

---

## Post #5 by @lassoan (2020-02-11 00:41 UTC)

<aside class="quote no-group" data-username="flaviu2" data-post="3" data-topic="10175">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/74df32/48.png" class="avatar"> flaviu2:</div>
<blockquote>
<p>my task is to do that inside my VC++ application</p>
</blockquote>
</aside>
<p>If this is a homework assignment then sure, it is a good idea to create your own application so that you learn how things work. You can study the source code of 3D Slicer and feel free to take whatever you find useful.</p>
<p>If you are developing a research application or product then developing your own application from scratch is huge waste of time that prevents you from focusing on the things that matter. If you want to have a robust and feature rich application then you typically very soon reach the point that all your efforts are spent on maintenance and support.</p>
<p>If you just want to have “something quick and simple” then forget desktop applications. Today people expect that they can do simple things in their web browser and refuse to install a desktop application for that.</p>
<aside class="quote no-group" data-username="flaviu2" data-post="3" data-topic="10175">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/74df32/48.png" class="avatar"> flaviu2:</div>
<blockquote>
<p>The source code is huge</p>
</blockquote>
</aside>
<p>This is a common misconception. Actually, Slicer source code is tiny:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e5c104e9d265d5aee5baa321cf07a2b0ec523a4.png" data-download-href="/uploads/short-url/mAUGwAAJ9zS46goTNMyHyVNlk0c.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e5c104e9d265d5aee5baa321cf07a2b0ec523a4_2_597x500.png" alt="image" data-base62-sha1="mAUGwAAJ9zS46goTNMyHyVNlk0c" width="597" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e5c104e9d265d5aee5baa321cf07a2b0ec523a4_2_597x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e5c104e9d265d5aee5baa321cf07a2b0ec523a4.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e5c104e9d265d5aee5baa321cf07a2b0ec523a4.png 2x" data-dominant-color="D1BCB6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">812×680 45.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If your application uses Qt, VTK, ITK, DCMTK then your application is already 85% the same as Slicer.</p>

---

## Post #6 by @flaviu2 (2020-02-13 18:17 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Can you point me the proper filter to do a teeth segmentation ? I ask that because maybe I can find in the slicer source code that filter … in order to read it and understand it and to apply it on myself <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
