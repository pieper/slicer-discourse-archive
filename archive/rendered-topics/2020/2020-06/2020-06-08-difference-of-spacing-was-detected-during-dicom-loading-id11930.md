# Difference of spacing was detected during DICOM loading

**Topic ID**: 11930
**Date**: 2020-06-08
**URL**: https://discourse.slicer.org/t/difference-of-spacing-was-detected-during-dicom-loading/11930

---

## Post #1 by @Jeff_S (2020-06-08 13:10 UTC)

<p>Thank you very much for your reply!<br>
Now I have another problem wit the DICOM-data and I get this error:<br>
“Images are no spaced (a difference of 60.5 vs 0.5 spacing was detected) If loaded image appears ditored, enable “Acquisition regularization” in Applications setting…”<br>
I followed the instructions and enabled the Acquisition regularization but first the error still eccured and the data was even more distored then before. Do you know what I can do or how I can align the slices better? Thank you very much for your help in advance!</p>

---

## Post #2 by @lassoan (2020-06-08 14:22 UTC)

<aside class="quote no-group" data-username="Jeff_S" data-post="1" data-topic="11930">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jeff_s/48/6146_2.png" class="avatar"> Jeff_S:</div>
<blockquote>
<p>a difference of 60.5 vs 0.5 spacing was detected</p>
</blockquote>
</aside>
<p>This is a large difference. Probably your volume has an extra slice or slices are mixed up.</p>
<p>Try the latest Slicer preview release, as we added some more filtering of invalid slices in there. After loading, harden the transform on the volume.</p>

---

## Post #3 by @Jeff_S (2020-06-08 16:10 UTC)

<p>Thank you for your reply,<br>
yeah thats probabbly the case, that the slices got mixed up.<br>
Do you mean the new version 4.11.0?</p>

---
