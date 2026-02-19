---
topic_id: 21639
title: "Tips For Choice Of Automated Brain Tumor Mri Segmentation Al"
date: 2022-01-26
url: https://discourse.slicer.org/t/21639
---

# Tips for choice of automated brain tumor MRI segmentation algorithms

**Topic ID**: 21639
**Date**: 2022-01-26
**URL**: https://discourse.slicer.org/t/tips-for-choice-of-automated-brain-tumor-mri-segmentation-algorithms/21639

---

## Post #1 by @paullane (2022-01-26 17:00 UTC)

<p>I am a student and I need to develop a python script to automate brain tumor segmentation of MRI DICOM images.<br>
My question is what are some simple but popular algorithms available to do this task? or is deep learning the preferred route? I am currently going through the PerkLab’s bootcamp and script repository.</p>

---

## Post #2 by @lassoan (2022-01-27 03:13 UTC)

<p>Many automatic brain segmentation algorithms have been developed over the years, but recent neural network based methods can usually achieve similar quality results at a fraction of computation time (if you have a fast GPU). In addition to the good performance, all funding and attention is directed to neural networks in the last few years, so it probably does not make sense to go back to classic methods.</p>
<p>See this topic on advice on automatic brain segmentation tools: <a href="https://discourse.slicer.org/t/whole-brain-automate-segmentation/21225" class="inline-onebox">Whole brain automate segmentation</a>. You can run all of them from Python.</p>

---
