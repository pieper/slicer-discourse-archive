---
topic_id: 46920
title: "Segmentation bounds cropped even when \"cropped to minimum extent\" is unchecked"
date: 2026-05-04
url: https://discourse.slicer.org/t/46920
last_bumped: 2026-05-06T05:36:36.095Z
---

# Segmentation bounds cropped even when "cropped to minimum extent" is unchecked

**Topic ID**: 46920
**Date**: 2026-05-04
**URL**: https://discourse.slicer.org/t/segmentation-bounds-cropped-even-when-cropped-to-minimum-extent-is-unchecked/46920

---

## Post #1 by @hherhold (2026-05-04 18:48 UTC)

<p>Sequence of events:</p>
<ol>
<li>Create segmentation using slicer</li>
<li>modify segmentation in external python script using pynrrd</li>
<li>re-import segmentation into slicer</li>
<li>modify segmentation in slicer</li>
<li>save segmentation</li>
<li>This saved segmentation has been cropped to its minimum extent even though checkbox in save dialog is not checked.</li>
</ol>
<p>I ran this through Claude Opus 4.7 and it had a couple of suggestions, which I did try but did not appear to fix the problem; I haven’t had a chance to investigate further. Just wondering if anyone has run into this before.</p>
<p>The segmentation in question is fed into biomedisa (<a href="https://biomedisa.info/" rel="noopener nofollow ugc">https://biomedisa.info/</a>), which requires the segmentation and the volume data to have the same dimensions.</p>
<p>Anyway, this is an odd corner case and likely hasn’t been a huge issue. I can post Claude Opus’ suggestions if anyone is interested.</p>

---

## Post #2 by @mikebind (2026-05-05 17:06 UTC)

<p>I would suggest checking the segmentation dimensions at each of your steps above.  That may help you narrow down when the issue occurs.  For example, when you modify the segmentation with pynrrd, is it already cropped, or does that occur at the re-import step, etc.  Also, are the middle steps important?  For example, if you just create a segmentation, edit it, and save (without checking the box), is the output correct?  If that works, a workaround might be to set the segment geometry to match the source volume after step 4.</p>

---

## Post #3 by @hherhold (2026-05-05 19:41 UTC)

<p>Hi Mike,</p>
<p>Thanks for the reply. The segmentation bounds determined from looking at the NRRD header are the same until step 5 where I save it from slicer.</p>
<p>Just re-setting the segment geometry isn’t sufficient, I had to write a script to pad out the segmentation bounds to restore it to its original extent. (I can post this if anybody’s interested.)</p>

---

## Post #4 by @mikebind (2026-05-06 05:36 UTC)

<p>OK, those were my quick ideas.  Sounds like a bug, and I’m not sure what’s triggering it; hopefully someone else will be able to help!</p>

---
