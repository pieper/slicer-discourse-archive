---
topic_id: 12222
title: "Model To Label Map In 4 11 Vs 4 10"
date: 2020-06-25
url: https://discourse.slicer.org/t/12222
---

# Model To Label Map in 4.11 vs 4.10

**Topic ID**: 12222
**Date**: 2020-06-25
**URL**: https://discourse.slicer.org/t/model-to-label-map-in-4-11-vs-4-10/12222

---

## Post #1 by @siaeleni (2020-06-25 20:56 UTC)

<p>Hi all,</p>
<p>I am using “Model To Label Map” built-in module in 4.11 and 4.10 and get different results.</p>
<p>First of all, my Model is saved as “vtk output SPACE=LPS” and at 4.11 I force it to open as LPS, but I realize that when I load the same file in 4.10 and 4.11 the orientation of the model is different, is that what is expected? Does the “by default” Coordinate system for 4.10 is LPS, correct?</p>
<p>Secondly, the output of “Model to Label Map” at 4.11 has “opposite” coordination/orientation.If I load RAS, I will get LPS and vice-versa. Is that what is expected too?</p>
<p>Thanks,<br>
Eleni</p>

---

## Post #2 by @lassoan (2020-06-25 21:48 UTC)

<aside class="quote no-group" data-username="siaeleni" data-post="1" data-topic="12222">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/b4bc9f/48.png" class="avatar"> siaeleni:</div>
<blockquote>
<p>First of all, my Model is saved as “vtk output SPACE=LPS” and at 4.11 I force it to open as LPS,</p>
</blockquote>
</aside>
<p>There should be no need to force anything, since Slicer-4.11 reads the file according to the coordinate system information available in the file. Maybe some older Slicer-4.11 version did not save the coordinate system but recent ones should work well.</p>
<aside class="quote no-group" data-username="siaeleni" data-post="1" data-topic="12222">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/b4bc9f/48.png" class="avatar"> siaeleni:</div>
<blockquote>
<p>output of “Model to Label Map” at 4.11 has “opposite” coordination/orientation.If I load RAS, I will get LPS and vice-versa. Is that what is expected too?</p>
</blockquote>
</aside>
<p>“Opposite” compared to what?<br>
Input image is always LPS. In recent Slicer-4.11 versions, output model is always LPS.</p>
<p>We now save all files in LPS coordinate system (unless they were loaded originally from RAS). I would not recommend to mix usage of Slicer-4.10 and Slicer-4.11 but once you transitioned to Slicer-4.11 keep using that.</p>

---

## Post #3 by @siaeleni (2020-06-25 23:22 UTC)

<p>Thanks! Now works after downloading newer version of Slicer.</p>

---
