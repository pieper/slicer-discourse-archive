# Paint brush behavior

**Topic ID**: 1952
**Date**: 2018-01-27
**URL**: https://discourse.slicer.org/t/paint-brush-behavior/1952

---

## Post #1 by @JanWitowski (2018-01-27 04:46 UTC)

<p>Hi! So this is an issue I’ve seen a few times but still don’t understand why it’s happening. Sometimes I’m doing segmentation and even though I use paint brush on the image, I don’t see the effect on the image slice. However, I can see the changes in 3D view. Also, if I paint something at - let’s say - axial images and see no result there, I still can see changes in sagittal/coronal slices. This happens no matter how large the paint brush is. Also, I’m not changing master volume once it’s set. I’m not sure what’s going on here, unfortunately. Currently I’m running nightly build on Windows but I had this issue multiple times in the past with stable releases too. Am I missing something?</p>
<p>Thanks a lot for your support and great software – it is an exceptional tool in my research<br>
Best</p>

---

## Post #2 by @cpinter (2018-01-27 13:47 UTC)

<p>Thanks for reporting this and for the thorough description! I remember seeing this once or twice, but never managed to reproduce it.</p>
<p>Do you have a certain way of reproducing the problem? If so, then we can fix it, but only if we know what triggers it.</p>

---

## Post #3 by @lillux (2018-01-27 16:15 UTC)

<p>i think i experienced the same problem on the segment editor module. It happened to me somethimes too. when it happened I noticed that It depends on how much zoom you use on the image. If i was to close the painter did not work, if i went back with the zoom i was able to see the painting on the image.</p>
<p>Working on Windows 8.1, Slicer v4.8.1 r26813</p>

---

## Post #4 by @Hamburgerfinger (2018-01-27 16:32 UTC)

<p>This happened to me before, but it was because the volume I was segmenting wasn’t perfectly aligned in plane of the slice viewers, and thus I was really painting on oblique slices sometimes.</p>
<p>Have you tried clicking the “rotate To volume plane” button in the menu beneath the pin at the top left of each slice view?</p>

---

## Post #5 by @lillux (2018-01-27 17:11 UTC)

<p>I think that the problem that i experienced was different, because at the next session i was able to segment the same set of images</p>

---

## Post #6 by @cpinter (2018-01-27 18:59 UTC)

<p>The oblique view issue <a class="mention" href="/u/hamburgerfinger">@Hamburgerfinger</a> is completely reproducible and is independent from this, as in that case you see the staircase artifact, and <a class="mention" href="/u/janwitowski">@JanWitowski</a>’s (and my) case there was no segment visible at all. I had to restart Slicer and it worked. It would be great if we found a way to reproduce it.</p>

---

## Post #7 by @JanWitowski (2018-01-28 00:13 UTC)

<p>Hey thanks for the reply! Unfortunately, I haven’t found a way to reproduce it either, <em>but</em> there is one more interesting thing about this behavior. When I switch brush to sphere brush and paint something, it suddenly shows the sphere I just painted <em>and</em> all the previous non-sphere brushes. When I undo this action, both disappear. So it’s like that single sphere brush added to an image sphere brush + “history” of non-sphere brushes before.<br>
And another one I just noticed: when I’m painting over another, visible layer with “overwrite all segments” setting, I can see that my paint brushes remove parts of the visible layer, but it doesn’t look like it’s painting over until I use sphere paint brush to trigger the “visibility”.</p>

---

## Post #8 by @cpinter (2018-01-28 02:50 UTC)

<p>Hm. Maybe it’s an issue with the displayable manager. <a class="mention" href="/u/lassoan">@lassoan</a> what do you think?</p>

---

## Post #9 by @lassoan (2018-01-28 06:05 UTC)

<p>I haven’t encountered these problems, so it is difficult to tell. Were you able to reproduce some of the problems?</p>

---

## Post #10 by @cpinter (2018-01-28 14:24 UTC)

<p>It happened to me twice. The brush stopped leaving a trace on the slice view after extended usage. Unfortunately I don’t have a way to reproduce, hopefully <a class="mention" href="/u/janwitowski">@JanWitowski</a> can help doing that.</p>

---
