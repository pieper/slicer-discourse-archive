---
topic_id: 34934
title: "Local Threshold No Longer Works"
date: 2024-03-17
url: https://discourse.slicer.org/t/34934
---

# Local threshold no longer works

**Topic ID**: 34934
**Date**: 2024-03-17
**URL**: https://discourse.slicer.org/t/local-threshold-no-longer-works/34934

---

## Post #1 by @chir.set (2024-03-17 13:20 UTC)

<p>On latest Slicer preview in Linux, nothing happens in the slice views after selecting ‘Local threshold’ in the ‘Segment editor’. My oldest build is 5.7.0-2024-02-29 r32739 / c7fe865 where it does not work either. The result is the same under X11 or Wayland. No particular error message can be read.<br>
The other effects of ‘SegmentEditorExtraEffects’ do not have issues.</p>
<p>Can someone confirm this is an issue?</p>
<p>Thank you.</p>

---

## Post #2 by @Sunderlandkyl (2024-03-18 14:11 UTC)

<p>To confirm, the issue is that the preview does not show up?</p>
<p>I just tested on Windows, and while I can’t see the preview, CTRL + click still added the region to the segment.</p>
<p>It could be that there was an update in the base threshold effect that broke the local threshold. I’ll take a look at it.</p>

---

## Post #3 by @chir.set (2024-03-18 15:58 UTC)

<aside class="quote no-group" data-username="Sunderlandkyl" data-post="2" data-topic="34934">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar"> Sunderlandkyl:</div>
<blockquote>
<p>the issue is that the preview does not show up?</p>
</blockquote>
</aside>
<p>Yes, there is no preview.</p>
<aside class="quote no-group" data-username="Sunderlandkyl" data-post="2" data-topic="34934">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar"> Sunderlandkyl:</div>
<blockquote>
<p>CTRL + click still added the region to the segment</p>
</blockquote>
</aside>
<p>Yes, it the specified threshold range, manually.</p>
<aside class="quote no-group" data-username="Sunderlandkyl" data-post="2" data-topic="34934">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar"> Sunderlandkyl:</div>
<blockquote>
<p>an update in the base threshold effect</p>
</blockquote>
</aside>
<p>Probably, thanks for having a look.</p>
<p>I reported because it came as a surprise; I don’t use it very often and there are alternatives.</p>

---
