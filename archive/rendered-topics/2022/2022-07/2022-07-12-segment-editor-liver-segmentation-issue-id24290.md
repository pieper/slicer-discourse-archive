# Segment Editor - Liver segmentation issue

**Topic ID**: 24290
**Date**: 2022-07-12
**URL**: https://discourse.slicer.org/t/segment-editor-liver-segmentation-issue/24290

---

## Post #1 by @suranga (2022-07-12 18:07 UTC)

<p>Hi,</p>
<p>To segment the liver, I simply utilised the Segment Editor tool. However, after using the grow from seed effect, I observed that there are extra boundaries and regions that do not belong to the liver region. How do I get rid of them so that I can get a clean liver segmentation in 3D slicer? Should I go through each slice or frame manually by moving the views?</p>
<p>I here attached a screen shot for your further reference</p>
<p>Please help me in resolving this matter.</p>

---

## Post #2 by @muratmaga (2022-07-12 18:30 UTC)

<p>From your screenshot it is hard to tell, what you shared might be the preview of the current seeds. Did you actually hit the apply button, which finalizes the segmentation.</p>
<p>After that you might also consider running a smoothing filter (e.g., median filter) to take care of any remaining jagged edges.</p>

---

## Post #4 by @lassoan (2022-07-12 20:46 UTC)

<p>You can undo the “Grow from seeds” (so that you see the seeds instead of the grown regions), initialize the region growing (so that you see the preview results), adjust the seeds until everything looks good.</p>
<p>Liver segmentation is quite tedious job, even using semi-automatic segmentation tools. Fortunately, there are freely available fully automatic liver segmentation tools in Slicer. The easiest to use is <a href="https://github.com/NVIDIA/ai-assisted-annotation-client/blob/master/slicer-plugin/README.md#nvidia-ai-assisted-annotation-aiaa-for-3d-slicer">NVIDIA-AI-assisted annotation</a>.</p>

---

## Post #5 by @diazandr3s (2022-07-14 00:03 UTC)

<p><a class="mention" href="/u/suranga">@suranga</a> you may be interested in using MONAI Label <a href="https://github.com/Project-MONAI/MONAILabel" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Project-MONAI/MONAILabel: MONAI Label is an intelligent open source image labeling and learning tool.</a></p>
<p>By default, the Deepedit model automatically segments the liver and other abdominal organs.</p>
<p>I’d suggest you give it a try and let us know how that goes on your PC.</p>
<p>Here is a video showing how to install MONAI Label <a href="https://youtube.com/playlist?list=PLtoSVSQ2XzyD4lc-lAacFBzOdv5Ou-9IA" class="inline-onebox" rel="noopener nofollow ugc">MONAI Label Deep Dive Series - YouTube</a></p>
<p>More videos are coming later this week.</p>
<p>Stay tuned. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #7 by @diazandr3s (2022-07-14 09:58 UTC)

<p>Hi <a class="mention" href="/u/suranga">@suranga</a>,</p>
<p>We’ve previously had this issue with this Slicer version: <a href="https://github.com/Project-MONAI/MONAILabel/issues/852" class="inline-onebox" rel="noopener nofollow ugc">Segmentation_[anatomy] model does not show up under Auto Segmentation header. · Issue #852 · Project-MONAI/MONAILabel · GitHub</a></p>
<p>Please try again with the latest Preview Slicer version and let us know if this is still the case.</p>
<p>Solution: <a href="https://github.com/Project-MONAI/MONAILabel/issues/852#issuecomment-1172436198" class="inline-onebox" rel="noopener nofollow ugc">Segmentation_[anatomy] model does not show up under Auto Segmentation header. · Issue #852 · Project-MONAI/MONAILabel · GitHub</a></p>
<p>Hope this helps,</p>
<p>Andres</p>

---

## Post #8 by @kopachini (2022-07-18 17:07 UTC)

<p>You have seed locality and higher numbers reduce spilling over the seeding.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1af971cd63eceb0dd4a79f6f5ba274019cf4c60c.jpeg" alt="1" data-base62-sha1="3QCQuGYXYxJchy1DRMLcFV0RHsw" width="621" height="408"></p>

---
