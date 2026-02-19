---
topic_id: 11512
title: "Is It Possible To Use Margin Tool Only Inside A Roi"
date: 2020-05-13
url: https://discourse.slicer.org/t/11512
---

# Is it possible to use margin tool only inside a ROI?

**Topic ID**: 11512
**Date**: 2020-05-13
**URL**: https://discourse.slicer.org/t/is-it-possible-to-use-margin-tool-only-inside-a-roi/11512

---

## Post #1 by @Mohammad_Tanjib_Rahm (2020-05-13 02:00 UTC)

<p>Hi,<br>
I am trying to shrink the margin of the segmentation by couple millimetres. However I want to do it only inside the specified annotation ROI. I tried setting the source geometry as the annotation ROI and then using the shrink tool. But it shrinks the whole segmentation.</p>
<p>Is it possible to shrink the segmentation just inside the ROI?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/7451c142db01a44464c221da1565bd36080c2971.jpeg" data-download-href="/uploads/short-url/gB0xPEawsrFAdzeHnGGAtk3q4Kt.jpeg?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7451c142db01a44464c221da1565bd36080c2971_2_369x500.jpeg" alt="Capture" data-base62-sha1="gB0xPEawsrFAdzeHnGGAtk3q4Kt" width="369" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7451c142db01a44464c221da1565bd36080c2971_2_369x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7451c142db01a44464c221da1565bd36080c2971_2_553x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/7451c142db01a44464c221da1565bd36080c2971.jpeg 2x" data-dominant-color="1A1B18"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">686×928 50.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2020-05-13 02:18 UTC)

<p>You need to specify editable region using a segment and specify that segment in the masking options section in Segment Editor.</p>

---

## Post #3 by @Mohammad_Tanjib_Rahm (2020-05-13 02:47 UTC)

<p>Do you mean I should create another segment for the portion I want to edit, select that segment as editable region in masking and then apply shrink? Is there anyway I can edit only inside the ROI and not anywhere else?</p>

---

## Post #4 by @lassoan (2020-05-13 02:59 UTC)

<aside class="quote no-group" data-username="Mohammad_Tanjib_Rahm" data-post="3" data-topic="11512">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mohammad_tanjib_rahm/48/5934_2.png" class="avatar"> Mohammad_Tanjib_Rahm:</div>
<blockquote>
<p>Do you mean I should create another segment for the portion I want to edit, select that segment as editable region in masking and then apply shrink?</p>
</blockquote>
</aside>
<p>Yes. Make sure to allow overlap so that the mask segment can overlap with segments you want to modify.</p>
<aside class="quote no-group" data-username="Mohammad_Tanjib_Rahm" data-post="3" data-topic="11512">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mohammad_tanjib_rahm/48/5934_2.png" class="avatar"> Mohammad_Tanjib_Rahm:</div>
<blockquote>
<p>Is there anyway I can edit only inside the ROI and not anywhere else?</p>
</blockquote>
</aside>
<p>That’s exactly how it works. Once you set a segment as editable region, you can only modify inside that region.</p>

---
