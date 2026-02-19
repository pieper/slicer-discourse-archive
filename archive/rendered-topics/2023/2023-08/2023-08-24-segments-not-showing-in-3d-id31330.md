---
topic_id: 31330
title: "Segments Not Showing In 3D"
date: 2023-08-24
url: https://discourse.slicer.org/t/31330
---

# Segments not showing in 3d

**Topic ID**: 31330
**Date**: 2023-08-24
**URL**: https://discourse.slicer.org/t/segments-not-showing-in-3d/31330

---

## Post #1 by @mohammed_alshakhas (2023-08-24 09:45 UTC)

<p>I have this file where suddenly segments disappear from 3D and can’t be shown.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31f2268c96019781469848ba1609324be52b1d28.jpeg" data-download-href="/uploads/short-url/77QctJipx0fecOWQqt7jQzS7Mh2.jpeg?dl=1" title="Screenshot 2023-08-24 at 12.47.55" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31f2268c96019781469848ba1609324be52b1d28_2_547x500.jpeg" alt="Screenshot 2023-08-24 at 12.47.55" data-base62-sha1="77QctJipx0fecOWQqt7jQzS7Mh2" width="547" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31f2268c96019781469848ba1609324be52b1d28_2_547x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31f2268c96019781469848ba1609324be52b1d28_2_820x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31f2268c96019781469848ba1609324be52b1d28_2_1094x1000.jpeg 2x" data-dominant-color="555553"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-08-24 at 12.47.55</span><span class="informations">1836×1678 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2023-08-24 10:09 UTC)

<p>What do you mean suddenly? There must be some action that makes it disappear…</p>
<p>Try clicking the center 3D view button in the header of the 3D view. You can also confirm the presence of the closed surface representation in the Segment Editor module (if you were segmenting) or the Segmentations module.</p>
<p>The background of the 3D view is white on purpose? Did you choose that color or is it also part of the segments disappearing issue?</p>

---

## Post #3 by @mohammed_alshakhas (2023-08-24 10:30 UTC)

<p>i was segmenting. suddenly it disappears.  I can’t exactly remember the step I was doing. but I was doing my routine workflow.<br>
the background is purposefully white and I tried centering and toggling on and off visibility.   nothing works</p>

---

## Post #4 by @cpinter (2023-08-24 10:41 UTC)

<aside class="quote no-group" data-username="mohammed_alshakhas" data-post="3" data-topic="31330">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mohammed_alshakhas/48/10025_2.png" class="avatar"> mohammed_alshakhas:</div>
<blockquote>
<p>toggling on and off visibility</p>
</blockquote>
</aside>
<p>Please check if the closed surface representation is present or not: Segmentations module, Representations section.</p>

---

## Post #5 by @mohammed_alshakhas (2023-08-24 13:51 UTC)

<p>there is a green check next to closed surface</p>

---

## Post #6 by @cpinter (2023-08-24 13:55 UTC)

<p>Thanks. Maybe post a video about trying to do centering and show/hide and show/hide 3D, the content of Segment Editor module and Segmentations module, then we can save a lot of time we’d spend with small questions and small answers…</p>

---

## Post #7 by @pieper (2023-08-24 14:00 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="6" data-topic="31330">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>we can save a lot of time we’d spend with small questions and small answers…</p>
</blockquote>
</aside>
<p>Agreed.</p>
<p><a class="mention" href="/u/mohammed_alshakhas">@mohammed_alshakhas</a> We are here to help, but to help us help you, it’s important to provide succinct but complete reporting.  The ideal report is short, but shows the issue and the exact steps to replicate it on a different computer using public data.</p>

---

## Post #8 by @mohammed_alshakhas (2023-08-25 15:38 UTC)

<p>I cant really share videos of private data.  Just be assured that there is no simple mistake here. im using 3dslicer for more than 2 years already and never had this issue before<br>
I’m not really concerned about fixing this particular file. I can re-do work In 15 minutes or less.<br>
I’m just reporting this issue for the development team acknowledgment</p>

---

## Post #9 by @mohammed_alshakhas (2023-08-25 16:51 UTC)

<p>now I just had the same issue again exactly after deleting one segment that was actually blank. all other segments disappear from 3d view.  Pressing undo brought all segments back to 3D again while nothing was affected in slice views<br>
<a class="mention" href="/u/cpinter">@cpinter</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #10 by @lassoan (2023-08-25 16:54 UTC)

<p>Could you describe what you did so that we can reproduce it?</p>

---

## Post #11 by @chir.set (2023-08-25 17:06 UTC)

<aside class="quote no-group" data-username="mohammed_alshakhas" data-post="8" data-topic="31330">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mohammed_alshakhas/48/10025_2.png" class="avatar"> mohammed_alshakhas:</div>
<blockquote>
<p>private data</p>
</blockquote>
</aside>
<p>Can you reproduce the unexpected behaviour with sample data from the ‘Sample’ module? It could be your data is corrupt.</p>
<p>[By the way, arguing ‘private data (enterprise or personal?)’ on a ‘public’ forum of benevolent volunteers of an ‘open source’ project is somehow a breach of logic to me (and others?), just a comment.]</p>

---

## Post #12 by @mohammed_alshakhas (2023-08-25 17:34 UTC)

<p>privacy of my data is  my concern, not yours<br>
just comment</p>

---

## Post #13 by @mohammed_alshakhas (2023-08-25 17:42 UTC)

<p>during regular segmentation workflow.  using threshold and painting and erasing.<br>
I usually create a few segments until I get the color I like ( being lazy in selecting a color).</p>
<p>then I usually delete the segment I created and not used,  but for a few instances other than this one I had the segments disappearing from the from 3d view.</p>
<p>this time undoing delete for this segment I didn’t use brought them again to the 3D view.<br>
previously I was not paying enough attention to what made segments disappear</p>

---

## Post #14 by @mohammed_alshakhas (2023-08-31 12:02 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> i opened the same file again and noticed that rendering is also not showing this time.</p>
<p>i tried using dual 3d.  segments  and rendering are showing in 3d in view 2  but not in view 1</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/143660c6a984157fb2e7f64cf25ff98c1c42d210.jpeg" data-download-href="/uploads/short-url/2SO3kOXn8WPF4JjNKDWm2tGkPi8.jpeg?dl=1" title="Screenshot 2023-08-31 at 14.59.32" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/143660c6a984157fb2e7f64cf25ff98c1c42d210_2_690x250.jpeg" alt="Screenshot 2023-08-31 at 14.59.32" data-base62-sha1="2SO3kOXn8WPF4JjNKDWm2tGkPi8" width="690" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/143660c6a984157fb2e7f64cf25ff98c1c42d210_2_690x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/143660c6a984157fb2e7f64cf25ff98c1c42d210_2_1035x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/143660c6a984157fb2e7f64cf25ff98c1c42d210_2_1380x500.jpeg 2x" data-dominant-color="999796"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-08-31 at 14.59.32</span><span class="informations">1920×696 82.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
