---
topic_id: 36082
title: "Automatic Segmentation Tools For Brain Avm"
date: 2024-05-06
url: https://discourse.slicer.org/t/36082
---

# Automatic segmentation tools for brain AVM?

**Topic ID**: 36082
**Date**: 2024-05-06
**URL**: https://discourse.slicer.org/t/automatic-segmentation-tools-for-brain-avm/36082

---

## Post #1 by @samuelholly (2024-05-06 08:53 UTC)

<p>Dear Slicer team,</p>
<p>Thank you for providing this amazing tool. Is it possible to share some details about the BRATS MEN and BRATS GLI models? Are any of the available models suitable for segmentation of arterio-venous malformations of the brain?</p>
<p>Thank you in advance.</p>
<p>Samuel</p>

---

## Post #2 by @diazandr3s (2024-05-07 20:24 UTC)

<p>Hi <a class="mention" href="/u/samuelholly">@samuelholly</a>,</p>
<p>Thanks for your comment.</p>
<blockquote>
<p>Is it possible to share some details about the BRATS MEN and BRATS GLI models?</p>
</blockquote>
<p>Is there anything in particular you’d like to know about this? We used all cases with BRATS MEN and BRATS GLI annotations to train the Aurto3DSeg. We used the SegResNet architecture as the backbone for these two tasks.</p>
<blockquote>
<p>Are any of the available models suitable for segmentation of arterio-venous malformations of the brain?</p>
</blockquote>
<p>We don’t have a model available now. Do you have a dataset available to train the Auto3DSeg for this task?</p>
<p>Let us know</p>

---

## Post #3 by @samuelholly (2024-05-09 05:21 UTC)

<p>Hi Andres,</p>
<p>thank you for the reply. I was curious what the “MEN” and “GLI” acronyms mean. I suppose MEN means meningeoma (?) and GLI means glioma (?)</p>
<aside class="quote no-group" data-username="diazandr3s" data-post="2" data-topic="36082">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/diazandr3s/48/9973_2.png" class="avatar"> diazandr3s:</div>
<blockquote>
<p>We don’t have a model available now. Do you have a dataset available to train the Auto3DSeg for this task?</p>
</blockquote>
</aside>
<p>Thank you. Unfortunately, not.</p>
<p>Best regards</p>
<p>Samuel</p>

---

## Post #4 by @diazandr3s (2024-05-09 07:00 UTC)

<p>Hi <a class="mention" href="/u/samuelholly">@samuelholly</a>,</p>
<p>oh sorry, yes - MEN is short for meningioma and GLI is short for glioma.</p>

---

## Post #5 by @samuelholly (2024-05-09 07:02 UTC)

<p>Hi, no problem, thank you very much <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
