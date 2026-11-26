---
topic_id: 49101
title: "Automatic segmentation of renal arteries and veins in MRI"
date: 2026-11-25
url: https://discourse.slicer.org/t/49101
last_bumped: 2026-11-26T02:07:26.031Z
---

# Automatic segmentation of renal arteries and veins in MRI

**Topic ID**: 49101
**Date**: 2026-11-25
**URL**: https://discourse.slicer.org/t/automatic-segmentation-of-renal-arteries-and-veins-in-mri/49101

---

## Post #1 by @sertacaksoy (2026-11-25 18:27 UTC)

<p>We are trying to build an agent that segment <strong>renal arteries and veins</strong> automatically from <strong>abdominal MRI</strong> scans with TotalSegmentator, and haven’t found a reliable automated solution yet. We have used TotalSegmentator for CT scans and worked wonders. But for the case of MRI, it could not do the branching of the veins, also Total_MR did not resolved the issue too . We have tried brush tool to work out the issue, but there was no significant improvement. Is there a way or a tool to solve this problem?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0487349616677b017cab5d6aaea0d203c4ae61a.jpeg" data-download-href="/uploads/short-url/rr0THGhz89WSy73XJyUFShO0kMG.jpeg?dl=1" title="Image 2026-11-25 at 21.20.55" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0487349616677b017cab5d6aaea0d203c4ae61a.jpeg" alt="Image 2026-11-25 at 21.20.55" data-base62-sha1="rr0THGhz89WSy73XJyUFShO0kMG" width="690" height="482" data-dominant-color="353230"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Image 2026-11-25 at 21.20.55</span><span class="informations">1176×822 37.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks in advance for the suggestions.</p>

---

## Post #2 by @zhousy5310 (2026-11-26 02:07 UTC)

<aside class="quote no-group" data-username="sertacaksoy" data-post="1" data-topic="49101">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sertacaksoy/48/14091_2.png" class="avatar"> sertacaksoy:</div>
<blockquote>
<p><strong>renal arteries and veins</strong> automatically from <strong>abdominal MRI</strong></p>
</blockquote>
</aside>
<p>Hi sertac,</p>
<p>May i ask if the agent’s only goal is to “segment out renal arteries and veins automatically from abdominal MRI”? If so, maybe it’s better to train a task-speicifc model for that, via some segmented dataset.</p>
<p>Could you share a bit more details on this?</p>

---
