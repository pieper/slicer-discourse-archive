# Simple Undo button

**Topic ID**: 10995
**Date**: 2020-04-05
**URL**: https://discourse.slicer.org/t/simple-undo-button/10995

---

## Post #1 by @mimi (2020-04-05 00:50 UTC)

<p>Is there a simple undo button in case I make mistakes in registration or segmentation? Closing and reopening the study from the latest saved version is quite cumbersome. Thank you</p>

---

## Post #2 by @lassoan (2020-04-05 01:16 UTC)

<p>There is a simple undo button for segmentation (actually, you have more: undo/redo buttons that allow going back and forward several steps).</p>
<p>Most other operations are not destructive, therefore undo is not applicable. For example, if registration result is not satisfactory then just adjust parameters and re-run the registration.</p>

---

## Post #3 by @mimi (2020-04-05 01:21 UTC)

<p>Thank you, but where are these undo buttons. I could not find any info on the in the documentation. I am new to slicer and quite desperate at the moment <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=9" title=":frowning:" class="emoji" alt=":frowning:"></p>

---

## Post #4 by @lassoan (2020-04-05 01:24 UTC)

<p>Undo/Redo buttons are in Segment Editor module (near button). See <a href="https://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html">documentation</a> and <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation">tutorials</a> for more details.</p>

---

## Post #5 by @mimi (2020-04-05 01:27 UTC)

<p>Found it. Thx. Is there an Undo button for registration as well?</p>

---

## Post #6 by @lassoan (2020-04-05 01:39 UTC)

<aside class="quote no-group" data-username="mimi" data-post="5" data-topic="10995">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/9fc348/48.png" class="avatar"> mimi:</div>
<blockquote>
<p>Is there an Undo button for registration as well?</p>
</blockquote>
</aside>
<p>See my answer above.</p>

---

## Post #7 by @SOFIA_R (2023-08-31 16:17 UTC)

<p>Hello, I’m doing a manual segmentation in 3D slicer and I made a mistake with the brush tool, how can i undo this action? There’s a yellow button in the segmentation module that seems to be an “undo option” but it doesn’t erase what I just drew in the image, there has to be a way to erase what you draw, just like in paint. Please help.</p>

---

## Post #8 by @jamesobutler (2023-08-31 17:13 UTC)

<p>If you press the “undo” option and then move your mouse do you see it undo in the slice views? I have observed cases where pressing undo does not update the slice view until you move your mouse.</p>

---
