---
topic_id: 36929
title: "Monai Auto3Dseg Inference Sources"
date: 2024-06-20
url: https://discourse.slicer.org/t/36929
---

# MONAI Auto3DSeg inference sources

**Topic ID**: 36929
**Date**: 2024-06-20
**URL**: https://discourse.slicer.org/t/monai-auto3dseg-inference-sources/36929

---

## Post #1 by @wesselk (2024-06-20 21:31 UTC)

<p>Hi all,</p>
<p>I have been working with the new MONAI Auto3DSeg and have a few questions if someone could help me out:</p>
<p>1- Where can I find the source for the models used?  For example, “Madiastinal anatomy TS2” is not in MONAI’s <a href="https://monai.io/model-zoo" rel="noopener nofollow ugc">model zoo</a> and it’s also not an available subtask or roi_subset in <a href="https://github.com/wasserth/TotalSegmentator" rel="noopener nofollow ugc">Total Segmentator</a>.</p>
<p>2- Were some of these models trained by Slicer community contributors?</p>
<p>3- Is there a way to run Auto3DSeg’s inference from cmd line without launching Slicer and switching modules?</p>
<p>Thanks in advance for any help!</p>

---

## Post #2 by @lassoan (2024-06-21 19:32 UTC)

<p>Most models that you can find online in various model zoos are not <a href="https://github.com/lassoan/SlicerMONAIAuto3DSeg/tree/main?tab=readme-ov-file#general-guidelines">optimized for real-world usage</a>. We created these models with <a class="mention" href="/u/diazandr3s">@diazandr3s</a> specifically to make them practically, clinically useful.</p>
<p>You can download these models and run them without Slicer GUI, from the command-line or via network requests within Slicer’s Python environment; or even completely independently from Slicer. To make it really easy to use without Slicer, we have separated the inference script into a <a href="https://github.com/lassoan/SlicerMONAIAuto3DSeg/blob/main/MONAIAuto3DSeg/Scripts/auto3dseg_segresnet_inference.py">standalone Python file</a>.</p>

---
