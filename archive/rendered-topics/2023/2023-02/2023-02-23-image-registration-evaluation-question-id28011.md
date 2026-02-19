---
topic_id: 28011
title: "Image Registration Evaluation Question"
date: 2023-02-23
url: https://discourse.slicer.org/t/28011
---

# Image registration evaluation question

**Topic ID**: 28011
**Date**: 2023-02-23
**URL**: https://discourse.slicer.org/t/image-registration-evaluation-question/28011

---

## Post #1 by @Young_Wang (2023-02-23 13:38 UTC)

<p>Hi everyone, I’m working on an image registration-related project. I want to evaluate its performance between different 3-4 final registration results (fused image) regarding readability.  The approach I’m taking is to</p>
<ol>
<li>fuse images</li>
<li>segmentation of the fused images</li>
<li>calculate the DICE and Hausdorff between segmentation_fused_1 and segmentation_fused_2</li>
</ol>
<p>I wonder if this is the correct approach?</p>

---

## Post #2 by @muratmaga (2023-02-23 16:21 UTC)

<p>I am not sure what you mean by fused image?</p>
<p>In general evaluation of registration algorithms require some sort of an independent metric. For example if you have manual segmentations of the same structure in two images, you can register them, apply the registration to segmentation and then calculate how similar the registered segmentation is to the manual one (DICE coefficient like you said).</p>
<p>You can also do this with landmarks or distance measurements…</p>

---

## Post #3 by @Young_Wang (2023-02-23 20:31 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> sorry I should be more specific. I’m working with co-registration with two image modalities. CT and OCT. CT has a bigger FOV and OCT has a smaller FOV.<br>
And the fused image here refers to a composite image of OCT + CT.</p>

---

## Post #4 by @muratmaga (2023-02-24 04:34 UTC)

<p>OK. But the idea still applies. You need to have a some kind of independent way of assessing the outcome of the registration. You can’t do that by looking at the DICE or hausdorff distance between two sets of fused images.</p>
<p>Maybe landmark a few points that exists both in OCT and CT images independently (in original images) and then see what the error in landmark placement in the fused image. Then you can choose the registration protocol that minimizes this error. Might be sufficient for a first-order pass.</p>

---

## Post #5 by @Young_Wang (2023-02-24 18:51 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a>, thank you. I forgot to specify the performance here only refers to the repeatability. But I totally agree that to assess the accuracy, I need to use landmark pairs.</p>

---

## Post #6 by @gcsharp (2023-02-24 20:29 UTC)

<p>Verification of registration remains a subject of research and debate.  My 2 cents:</p>
<ul>
<li>Visual inspection remains the gold standard for patient-specific verification.</li>
<li>Landmark distance or segmentation metrics (Dice, surface distance, etc.) are necessary and sufficient.  If clearly defined landmarks are not available, segmentation metrics are completely valid.</li>
<li>Transitivity analysis is useful, but by itself is insufficient.</li>
<li>Recovery of artificial warps (for deformable) is useful, but by itself is insufficient.</li>
<li>Smoothness analysis (for deformable) such as Jacobian determinant is useful, but by itself is insufficient.</li>
</ul>

---

## Post #7 by @Young_Wang (2023-02-24 20:43 UTC)

<p><a class="mention" href="/u/gcsharp">@gcsharp</a> thank you for the helpful discussion!</p>

---
