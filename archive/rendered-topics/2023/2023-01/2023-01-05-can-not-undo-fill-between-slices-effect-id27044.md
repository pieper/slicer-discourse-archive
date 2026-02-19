---
topic_id: 27044
title: "Can Not Undo Fill Between Slices Effect"
date: 2023-01-05
url: https://discourse.slicer.org/t/27044
---

# Can not undo Fill Between Slices effect

**Topic ID**: 27044
**Date**: 2023-01-05
**URL**: https://discourse.slicer.org/t/can-not-undo-fill-between-slices-effect/27044

---

## Post #1 by @Damaya (2023-01-05 03:28 UTC)

<p>Hello Everyone,<br>
I hope this is an easy fix. I am working on two segmentations on CT data. One was complete. However, upon performing the Fill Between slices effect on the second segmentation I noticed it had also performed the function on my first segmentation. I had forgotten to unselect the first segmentation. Unfortunately, I noticed this too late and I can not remove it as I am limited by the Undo functions limit. Is there a way around this that doesn’t involve me having to redo the first segmentation? Is there for example a history log where I can delete steps? Any help would be appreciated. Thanks.</p>

---

## Post #2 by @rbumm (2023-01-05 19:50 UTC)

<p>Unfortunately, there is no easy fix. Undo/redo seems to be limited to 9 operations and there is no history log.</p>

---

## Post #3 by @Damaya (2023-01-06 09:34 UTC)

<p>I was afraid of that. A history Log would be a good feature. Ok, thanks for the reply.</p>

---

## Post #4 by @lassoan (2023-01-07 00:38 UTC)

<p>If you often find you want to go back more than the default segmentation undo history and you have enough memory in your computer to store more states then <a href="https://discourse.slicer.org/t/segment-editor-undo-queue-length/14766">you can increase the maximum number of undo states</a>.</p>
<p>However, it might be better to just save your work more frequently. You can easily save independent copies of the full scene by clicking on the package icon in Save data window; or you can quickly save just the modified nodes by saving using the default options.</p>

---

## Post #5 by @Damaya (2023-01-07 06:12 UTC)

<p>Great! Thats good advice. I try to save often but not as separate files of the nodes.  I think I will try to get into the habit as a way of having bookmarks of my progress.  Unfortunately I lost a days work by making an avoidable mistake, but now I know . Thanks.</p>

---

## Post #6 by @muratmaga (2023-01-07 06:33 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="27044">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>However, it might be better to just save your work more frequently.</p>
</blockquote>
</aside>
<p>I would second this. A trick I use before committing a significant change in segmentation, is to go to Data module, right-click on the segmentation and choose “Export File” and save a copy of segmentation. It is faster than saving the whole scene and packaging it. If the segmentation experiment was successful, you can re-write the file in the same way. if not, delete it (instead of undo) and reload the file you just exported.</p>

---
