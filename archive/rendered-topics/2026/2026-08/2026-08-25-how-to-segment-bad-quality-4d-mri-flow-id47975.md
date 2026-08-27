---
topic_id: 47975
title: "How to segment bad quality 4D MRI FLOW"
date: 2026-08-25
url: https://discourse.slicer.org/t/47975
last_bumped: 2026-08-26T13:24:14.804Z
---

# How to segment bad quality 4D MRI FLOW

**Topic ID**: 47975
**Date**: 2026-08-25
**URL**: https://discourse.slicer.org/t/how-to-segment-bad-quality-4d-mri-flow/47975

---

## Post #1 by @VERRUCKT (2026-08-25 12:48 UTC)

<p>Hi everyone <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=15" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>I’m working on aortic segmentation from 4D flow MRI. I’ve been using TotalSegmentator but results are poor, I assume mostly a domain issue, since it’s CT-trained, plus the low SNR of my data.</p>
<p>Two things I’d love input on:</p>
<p><strong>1. Anything off-the-shelf?</strong> A pretrained model or pipeline I could run directly on my volumes, without annotating or training anything. Has anyone tried the MR variant of TotalSegmentator, or a pretrained nnU-Net for the aorta, on 4D flow data?</p>
<p><strong>2. If not, what’s the standard workflow?</strong> I’d rather follow an established approach than improvise. Do people segment the magnitude images directly, or reconstruct a PC-MRA first? How many annotated volumes are realistically needed to fine-tune something usable? Any public 4D flow dataset with aortic labels?</p>
<p>Happy to write up whatever ends up working, in case it’s useful to others.</p>
<p>Thanks a lot!</p>

---

## Post #2 by @Deep_Learning (2026-08-26 13:24 UTC)

<p>nninteractive.  there is an extension</p>

---
