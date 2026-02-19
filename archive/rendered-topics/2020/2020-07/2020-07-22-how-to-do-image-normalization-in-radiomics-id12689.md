---
topic_id: 12689
title: "How To Do Image Normalization In Radiomics"
date: 2020-07-22
url: https://discourse.slicer.org/t/12689
---

# How to do image normalization in Radiomics

**Topic ID**: 12689
**Date**: 2020-07-22
**URL**: https://discourse.slicer.org/t/how-to-do-image-normalization-in-radiomics/12689

---

## Post #1 by @danceward (2020-07-22 14:05 UTC)

<p>Hello<br>
I am doing some work about texture analysis using Radiomics package and how  can I do image normalization before texture analysis? Thanks</p>

---

## Post #2 by @fedorov (2020-07-30 20:46 UTC)

<p>This section in the documentation may be helpful:</p>
<p><a href="https://pyradiomics.readthedocs.io/en/latest/customization.html?highlight=normalization#feature-extractor-level" class="onebox" target="_blank">https://pyradiomics.readthedocs.io/en/latest/customization.html?highlight=normalization#feature-extractor-level</a></p>

---

## Post #3 by @danceward (2020-08-18 12:57 UTC)

<p>Thank you for your help <img src="https://emoji.discourse-cdn.com/twitter/slightly_smiling_face.png?v=9" title=":slightly_smiling_face:" class="emoji" alt=":slightly_smiling_face:"></p>

---

## Post #4 by @zzhan127 (2021-05-25 18:26 UTC)

<p>Hi Fedorov, thank you for the answer. I noticed that pyradiomics normalizes the whole image instead of the ROI. Is it possible to normalize the gray level of ROI? Thank you!</p>

---

## Post #5 by @fedorov (2021-05-25 18:36 UTC)

<p>No, I don’t think this is possible.</p>

---

## Post #6 by @MachadoL (2021-07-10 13:50 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a>, and others,</p>
<p>does radiomics has any guideline on normalizing the whole image then extracting features from ROI image or cropping ROI image and then normalizing?</p>

---

## Post #7 by @fedorov (2021-08-12 15:26 UTC)

<p>I don’t think there is a formal recommendation, but some suggested settings for normalization are available in this folder of the repo: <a href="https://github.com/AIM-Harvard/pyradiomics/tree/master/examples/exampleSettings" class="inline-onebox">pyradiomics/examples/exampleSettings at master · AIM-Harvard/pyradiomics · GitHub</a>.</p>
<p>We also explored the effects of normalization choices on reproducibility of features extracted from prostate MRI in this paper: <a href="https://www.nature.com/articles/s41598-019-45766-z" class="inline-onebox">Repeatability of Multiparametric Prostate MRI Radiomics Features | Scientific Reports</a> (a lot more things that were explored but didn’t fit into the peer-reviewed paper are discussed in the preprint: <a href="https://arxiv.org/abs/1807.06089" class="inline-onebox">[1807.06089] Repeatability of Multiparametric Prostate MRI Radiomics Features</a>).</p>

---

## Post #8 by @firatoz (2021-08-29 05:41 UTC)

<p>Thanks for your answers, but I don’t know coding. How can I do image normalization in 3d slicer without using code? I am doing radiomics work using ct images and I want to normalize with 3 sigma technique</p>

---

## Post #9 by @razie_aqeli (2022-01-09 15:54 UTC)

<p>It is my question tOO!</p>

---

## Post #10 by @JoostJM (2022-01-11 11:41 UTC)

<p>If you look at the PyRadiomics documentation suggested above you can enable normalization using sigma technique. If you add a resegmenatation range on [-3, 3], this ensures you only include voxels in the range -3 sigma to +3 sigma.</p>

---

## Post #12 by @LauraC (2023-11-26 01:59 UTC)

<p>Hi,</p>
<p>this a little confusing for me, sorry if I say a nonsense. So if we configure resegmentation with mode ‘sigma’ and range [-3, 3] we’ll keep only the voxels of the ROI inside that range and the rest will be considered as non-roi pixels for the calculation of the features, but I am not sure if it is exactly the 3sigma normalization does. Because what pyradiomics does is not a normalization where the voxels are transformed to a new range of values, they are just erased.</p>

---
