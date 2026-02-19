---
topic_id: 19969
title: "Brain White Matter Tissue Probability Map As Mask Behaviour"
date: 2021-10-02
url: https://discourse.slicer.org/t/19969
---

# brain white matter tissue probability map as mask - behaviour of pyradiomics

**Topic ID**: 19969
**Date**: 2021-10-02
**URL**: https://discourse.slicer.org/t/brain-white-matter-tissue-probability-map-as-mask-behaviour-of-pyradiomics/19969

---

## Post #1 by @nhaliasos (2021-10-02 14:16 UTC)

<p>greetings to community,</p>
<p>i have a doubt:<br>
when i use spm12 to produce a brain white matter segmentation from a T1 MRI scan the image produced by spm has various intensities from 0 to 1 especially at the edges between the white and grey matter as it is a tissue probability. So when using this image as mask, how does pyradiomics behave with regards to which value of intensity to use for cut-off between the classes?<br>
Ideally the mask should be either 0 or 1 at each point.</p>

---
