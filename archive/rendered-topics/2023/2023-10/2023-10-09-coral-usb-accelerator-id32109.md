---
topic_id: 32109
title: "Coral Usb Accelerator"
date: 2023-10-09
url: https://discourse.slicer.org/t/32109
---

# Coral USB accelerator

**Topic ID**: 32109
**Date**: 2023-10-09
**URL**: https://discourse.slicer.org/t/coral-usb-accelerator/32109

---

## Post #1 by @Cris (2023-10-09 04:12 UTC)

<p>Can I use the Coral usb accelerator from Google for the 3d slicer?</p>

---

## Post #2 by @lassoan (2023-10-09 04:44 UTC)

<p>It makes sense to use the Coral for what it has been designed for: accelerate a raspberry pi or similar edge device to process 2D images by running tiny models that are specifically designed to run on this hardware.</p>
<p>However, you typically run Slicer on a laptop or desktop computer that has CPUs that are much more powerful than a Coral (even for neural network inference). If your computer has a CUDA-capable GPU then the Coral’s computing power becomes negligible.</p>
<p>Another issue is that the Coral can only run very small TensorFlow Lite models, while the medical image computing community has pretty much standardized on PyTorch and most models are large.</p>
<p>Therefore, while you could use TensorFlow Lite models in Slicer, running on a Coral; it would be a lot of work for you to develop these models, and the results most likely would be worse than what you can get from larger models running on your CPU or GPU.</p>

---

## Post #3 by @Cris (2023-10-09 05:11 UTC)

<p>Thank you very much for the detailed answer. I will put together a Linux PC with an Nvidia graphics card. As a visceral surgeon, I am particularly interested in imaging liver tumors for surgical planning.</p>

---

## Post #4 by @lassoan (2023-10-09 11:53 UTC)

<p>Sounds good. Note that there are large liver tumour training datasets and even trained segmentation models that you can use.</p>

---

## Post #5 by @Cris (2023-10-09 13:12 UTC)

<p>Thanks for the tip <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #6 by @JohnClark (2023-11-20 12:55 UTC)

<p>Thanks for answering, you made my day <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
