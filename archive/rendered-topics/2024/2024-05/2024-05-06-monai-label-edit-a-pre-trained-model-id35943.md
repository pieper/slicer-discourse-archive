# Monai label - edit a pre-trained model

**Topic ID**: 35943
**Date**: 2024-05-06
**URL**: https://discourse.slicer.org/t/monai-label-edit-a-pre-trained-model/35943

---

## Post #1 by @ILB (2024-05-06 13:37 UTC)

<p>Hi there!<br>
I’ve recently started working with Monai Label on 3D Slicer to train a new model from scratch.<br>
My question is: would it be possible to use an already trained model, such as the "“wholeBody_ct_segmentation” and somehow add an extra trainning of something that doesn’t have, like blood vessels?</p>
<p>I think this approach is better than create a new one with organs and vessels, since this way we can take advantage of the already automated organ segmentations. Is it feasible?</p>
<p>Thank you!</p>

---

## Post #2 by @LeidyMoraV (2024-05-17 22:38 UTC)

<p>I’m not an expert, however, I think ‘tranfer learning’ form one model to another is similar to what do you want to do, MONAI talks a little about it <a href="https://docs.monai.io/en/0.9.0/highlights.html" rel="noopener nofollow ugc">Modules Overview — MONAI 0.9.0 Documentation</a></p>

---
