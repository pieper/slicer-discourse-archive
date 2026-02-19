---
topic_id: 27272
title: "Vessel Segmentation For Carotid Artery With Stenosis"
date: 2023-01-16
url: https://discourse.slicer.org/t/27272
---

# Vessel Segmentation for carotid artery with stenosis

**Topic ID**: 27272
**Date**: 2023-01-16
**URL**: https://discourse.slicer.org/t/vessel-segmentation-for-carotid-artery-with-stenosis/27272

---

## Post #1 by @hoochupapa (2023-01-16 19:02 UTC)

<p>Hi all,</p>
<p>I am pretty new to 3D slicer, and would very much appreciate your help <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>I am trying to segment and export a .stl file of the carotid artery with stenosis based on CT images with contrast.<br>
Since I am planning on handling 100+ patients’ data, I am trying my best to automate the process as much as possible ( and minimize user variability).</p>
<p>Granted, I have tried flood-filling / grow from seeds, and scissor-ing from the 3D view (threshold 235-600 HU). For all 3 methods, I need to manually erase/paint the lumen for each image due to the plaque and stenosis. Due to the low resolution when zoomed-in and the small cross-sectional area at the region of stenosis, this erase/paint process always leads to high variability.</p>
<p>Is there a more sophisticated way to achieve this? Or is there a guideline that I could follow?</p>
<p>Any guidance or information would be deeply appreciated.</p>
<p>Thank you!</p>

---

## Post #2 by @pieper (2023-01-16 20:03 UTC)

<p>Yes, it’s a hard problem.  In terms of improving the consistency for small vessels, you can try increasing the segmentation resolution (use the segmentation geometry button) so that the labelmap has more pixels to define the shape.  Also it’s likely that a machine learning algorithm like those in MONAI Label could be trained to do this task, although I haven’t seen it done yet.</p>

---

## Post #3 by @chir.set (2023-01-16 22:59 UTC)

<p>Can you post your worst case anonymized dataset?</p>

---

## Post #4 by @hoochupapa (2023-01-16 23:02 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f3c977b7bc55118d37fc55b78a641e6b594b20f.png" alt="image" data-base62-sha1="fS2OCezn7ArTr0xYNG5MfloN1VB" width="321" height="229"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0de569268e8dbedbfe89e9aefd1188b06d535799.png" alt="image" data-base62-sha1="1YVItzbxagWQYPxjn2wak0peyox" width="355" height="239"></p>
<p>Here is an example of the carotid artery at the site of stenosis. The white blob is the plaque.<br>
This is a result of scissoring, and as you can see it reads the plaque as part of the lumen, which isn’t something I want. Moreover, it is difficult to discern where the limits of the lumen/vessel are at.</p>

---

## Post #5 by @hoochupapa (2023-01-17 06:05 UTC)

<p>Thanks for the reply.</p>
<ol>
<li>
<p>The segmentation geometry was insufficient to overcome this problem.</p>
</li>
<li>
<p>I am looking into MONAI label. Would it run with Python 3.10.9 on Windows 10???</p>
</li>
</ol>

---

## Post #6 by @hoochupapa (2023-01-17 07:23 UTC)

<p>Can I use flood filling in MONAI label module? Or does it have to be grow from seeds?</p>

---

## Post #7 by @chir.set (2023-01-17 07:27 UTC)

<aside class="quote no-group" data-username="hoochupapa" data-post="4" data-topic="27272">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/9dc877/48.png" class="avatar"> hoochupapa:</div>
<blockquote>
<p>an example of the carotid</p>
</blockquote>
</aside>
<p>I meant, a worst case sample volume as NRRD or anonymized DICOM, through a hosting link.</p>

---

## Post #8 by @hoochupapa (2023-01-17 07:30 UTC)

<p>Oh I see. I can’t share that due to my company’s IP policy <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=12" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20"></p>

---

## Post #9 by @gaoyi.cn (2023-01-17 07:34 UTC)

<p>what OS are you using? I can build an extension for vessel segmentation for you so you can try on your data.</p>

---

## Post #10 by @hoochupapa (2023-01-17 07:35 UTC)

<p>That sounds wonderful! I am running on Windows 10. I have plenty of RAM and GPU, thankfully.</p>

---
