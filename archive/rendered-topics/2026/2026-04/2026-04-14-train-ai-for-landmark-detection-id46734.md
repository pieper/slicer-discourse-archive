---
topic_id: 46734
title: "Train Ai For Landmark Detection"
date: 2026-04-14
url: https://discourse.slicer.org/t/46734
---

# Train AI for landmark detection

**Topic ID**: 46734
**Date**: 2026-04-14
**URL**: https://discourse.slicer.org/t/train-ai-for-landmark-detection/46734

---

## Post #1 by @mau_igna_06 (2026-04-14 18:29 UTC)

<p>Hi,</p>
<p>I’d like to ask here which are community suggestions about selecting an AI model and setting up training data for a medical landmark detection task.</p>
<p>In my use case, I need to detect the superior tip of healthy kidneys on CBCTs. I have a training dataset with around 150 CBCTs with the corresponding landmarks (CBCT on .nrrd files and points in .mrk.json files). I think my training data (i.e. sup kidney tips) could have till a 1cm error. Current training shows 70% accuracy and I don’t expect it to get higher. So I assume the model won’t work after training but that will have to wait a few days (till the training ends)</p>
<p>More information: same use case with same AI model but targeting CTs instead of CBCTs for training, even with halve of training data (e.g. around 70 CTs), had 95% accuracy during training and my tests show it working</p>

---
