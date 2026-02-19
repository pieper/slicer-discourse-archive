---
topic_id: 43764
title: "Pancreatic Cta Vascular Reconstruction"
date: 2025-07-17
url: https://discourse.slicer.org/t/43764
---

# Pancreatic CTA Vascular Reconstruction

**Topic ID**: 43764
**Date**: 2025-07-17
**URL**: https://discourse.slicer.org/t/pancreatic-cta-vascular-reconstruction/43764

---

## Post #1 by @HenryClein (2025-07-17 21:45 UTC)

<p>Dear R&amp;D staff, the blood vessels around the pancreas are very complex and it is very easy to have massive bleeding during surgery. I hope to build a vascular reconstruction model. Is there a good learning tutorial? Thank you.</p>

---

## Post #2 by @mau_igna_06 (2025-07-18 00:01 UTC)

<p>This may provide some initial guidance for you:</p>
<ol>
<li>You need to gather segmentations as training data (I think at least 30 or 40 examples). You can get the data from someone or generate it yourself using Slicer or other tools</li>
<li>You need to select a good AI model such nnunet or segresnet</li>
<li>You need to train the model in a computer with powerful GPU</li>
<li>You need to deploy the trained model for inference on a computer that could have less powerful GPU</li>
</ol>
<p>HIH</p>

---
