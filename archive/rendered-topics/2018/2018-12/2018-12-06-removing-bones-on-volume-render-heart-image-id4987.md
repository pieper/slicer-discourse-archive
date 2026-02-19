---
topic_id: 4987
title: "Removing Bones On Volume Render Heart Image"
date: 2018-12-06
url: https://discourse.slicer.org/t/4987
---

# Removing bones on Volume render Heart image

**Topic ID**: 4987
**Date**: 2018-12-06
**URL**: https://discourse.slicer.org/t/removing-bones-on-volume-render-heart-image/4987

---

## Post #1 by @sarvpriya1985 (2018-12-06 14:16 UTC)

<p>Operating system: windows 10<br>
Slicer version:4.10<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hi,<br>
How can I get rid of unnecessary bones on volume rendered heart images. I used clipping box to remove as much bone as possible and also used threshholding. But still something still remains.</p>
<p>Other thing is can I view these volume rendered images through my mixed reality headset. I tried the segmented one but not sure how and if I can view Volume rendered images as well.<br>
Would appreciate thoughts on these.</p>
<p>Thanks,<br>
Sarv</p>

---

## Post #2 by @lassoan (2018-12-06 15:47 UTC)

<p>You can use Mask volume module to blank out arbitrary sections of the image (ribs, etc.) as <a href="https://www.youtube.com/watch?v=xZwyW6SaoM4&amp;t=88s" rel="nofollow noopener">shown in this video</a>.</p>
<p>You can see the same content in virtual reality as on the desktop monitor, including segmentations, volume rendering, etc. You can choose which view volume rendering appears in by going to Volume rendering module, Inputs section, and checking/unchecking boxes in the View combobox.</p>

---

## Post #3 by @sarvpriya1985 (2018-12-06 15:52 UTC)

<p>That’s wonderful. Thanks a lot.</p>
<p>Sarv</p>

---

## Post #4 by @mhalle (2018-12-06 16:16 UTC)

<p>If it’s volume rendered, can’t you edit a transfer function that renders the bones transparent?</p>
<p>–Mike</p>

---

## Post #5 by @sarvpriya1985 (2018-12-06 16:45 UTC)

<p>Hi Mike,<br>
I am not aware of that. Can you explain it.</p>
<p>Thanks,<br>
Sarv</p>

---

## Post #6 by @sarvpriya1985 (2018-12-06 20:22 UTC)

<p>Hi Andras,<br>
I did use mask volume. But there are some regions where I need to manually cut bone as it was too close or included in the mask range. I am struggling to remove that from final 3d view. Attached is snapshot. Is there anything else that can be done.</p>
<p>Thanks,<br>
Sarv<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/4895cc4742e3135a36748c78cf9187184ab5a05f.jpeg" data-download-href="/uploads/short-url/am7jKpMZCwfAWWxmnlkYeuSXtHV.jpeg?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4895cc4742e3135a36748c78cf9187184ab5a05f_2_491x500.jpeg" alt="Capture" data-base62-sha1="am7jKpMZCwfAWWxmnlkYeuSXtHV" width="491" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4895cc4742e3135a36748c78cf9187184ab5a05f_2_491x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/4895cc4742e3135a36748c78cf9187184ab5a05f.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/4895cc4742e3135a36748c78cf9187184ab5a05f.jpeg 2x" data-dominant-color="9E88A6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">670×682 51.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @lassoan (2018-12-08 19:20 UTC)

<p>You can create/edit the mask segment using any tools. You can very easily get rid of all bones by initializing the mask segment using Threshold effect (you’ll get all the bones and contrast-filled vessels in the segment), then remove large irrelevant parts using Scissors effect, and finally get rid of all floating bone segments by using Islands effect / Keep largest island method. You may grow the mask a little bit with Margin effect. If you want to include heart muscles in the mask then you can add that region using Surface cut effect.</p>

---
