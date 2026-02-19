---
topic_id: 20846
title: "Ai Assisted Segmentation Head And Neck Cancer"
date: 2021-11-30
url: https://discourse.slicer.org/t/20846
---

# AI assisted segmentation-Head and Neck cancer

**Topic ID**: 20846
**Date**: 2021-11-30
**URL**: https://discourse.slicer.org/t/ai-assisted-segmentation-head-and-neck-cancer/20846

---

## Post #1 by @MPhilip (2021-11-30 17:15 UTC)

<p>Operating system: windows 10 enterprise<br>
Slicer version:Slicer 4.13.0-2021-10-25<br>
I would like to implement AI based segmentation on the head and neck PET/CT image dataset. I read about AI assisted segmentation extension <a href="https://discourse.slicer.org/t/ai-assisted-segmentation-extension/9536">here</a> mainly about NVidia, Tomaat etc.<br>
I would like to know whether there is an AI-assisted segmentation extension trained for head and neck cancer?</p>
<p>Any response would be appreciated. Thanks</p>

---

## Post #2 by @lassoan (2021-11-30 17:36 UTC)

<p>I’m not aware of any Slicer extensions or pre-trained MONAILabel or AIAssistedAnnotation models for head&amp;neck CT segmentation. You can reach out to <a href="https://monai.io/community.html">MONAI community</a> if anyone is working on this. You may of also do some googling or literature search to see if anybody claims to have some segmentation tools that you might try.</p>
<p>Regardless of existing models, it would be a good starting point to create accurate segmentations of the structures that are relevant for you, using manual or semi-automatic tools, or AI-integrated tools, such as MONAILabel. You could use these models to validate pre-trained models or train your own models.</p>

---
