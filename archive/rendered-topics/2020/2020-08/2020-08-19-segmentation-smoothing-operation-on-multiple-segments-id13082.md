# Segmentation smoothing operation on multiple segments

**Topic ID**: 13082
**Date**: 2020-08-19
**URL**: https://discourse.slicer.org/t/segmentation-smoothing-operation-on-multiple-segments/13082

---

## Post #1 by @pr4deepr (2020-08-19 04:44 UTC)

<p>Hi guys<br>
I would like to apply smoothing operations, such as opening or closing to multiple segments. I can select multiple segments in the “segmentation” module, but not in “segment editor”.</p>
<p>Also, when importing segments as a binary labelmap, after a certain number of segments, the name of the segment becomes “invalid” instead of a number. Is there a limit on the number?</p>
<p>I have been using 3D Slicer for annotating and segmenting microscopy data. Its interface is quite intuitive, easy to navigate, and I plan to use it to generate ground truth data for machine learning purposes for image segmentation.</p>
<p>Cheers<br>
Pradeep</p>

---

## Post #2 by @lassoan (2020-08-19 05:00 UTC)

<aside class="quote no-group" data-username="pr4deepr" data-post="1" data-topic="13082">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pr4deepr/48/8810_2.png" class="avatar"> pr4deepr:</div>
<blockquote>
<p>I would like to apply smoothing operations, such as opening or closing to multiple segments.</p>
</blockquote>
</aside>
<p>You can apply smoothing to all visible segments by using “Joint smoothing” method in Smoothing effect. All the others may modify other segments and the result could depend on the order of segments, so they are not intended to be applied to many segments at once.</p>
<aside class="quote no-group" data-username="pr4deepr" data-post="1" data-topic="13082">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pr4deepr/48/8810_2.png" class="avatar"> pr4deepr:</div>
<blockquote>
<p>Also, when importing segments as a binary labelmap, after a certain number of segments, the name of the segment becomes “invalid” instead of a number. Is there a limit on the number?</p>
</blockquote>
</aside>
<p>Please try latest Slicer Preview Release and let us know if you still find issues with importing labelmaps. Note that you can load a labelmap volume directly as segmentation (from nrrd and nifti formats) by choosing “Segmentation” in Description column in Add data dialog.</p>

---

## Post #3 by @pr4deepr (2020-08-19 05:14 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a><br>
Thanks for your reply. I do use “Joint Smoothing” but was wondering if thre are ways to apply smoothing for each segment. Is this possible via scripting?</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="13082">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Please try latest Slicer Preview Release and let us know if you still find issues with importing labelmaps. Note that you can load a labelmap volume directly as segmentation (from nrrd and nifti formats) by choosing “Segmentation” in Description column in Add data dialog.</p>
</blockquote>
</aside>
<p>Thanks, I’ll give this a try. I may get segmentation files which are already binary labelmaps which I subsequently correct or edit using 3D Slicer hence the reason to import labelmaps as “Segmentation”.</p>
<p>Cheers<br>
Pradeep</p>

---

## Post #4 by @lassoan (2020-08-19 05:16 UTC)

<aside class="quote no-group" data-username="pr4deepr" data-post="3" data-topic="13082">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pr4deepr/48/8810_2.png" class="avatar"> pr4deepr:</div>
<blockquote>
<p>was wondering if thre are ways to apply smoothing for each segment. Is this possible via scripting?</p>
</blockquote>
</aside>
<p>Yes, of course, you can automate this. See lots of examples here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script" class="inline-onebox">Documentation/Nightly/ScriptRepository - Slicer Wiki</a></p>

---

## Post #5 by @pr4deepr (2020-08-19 06:26 UTC)

<p>Awesome!<br>
Thank you…</p>

---
