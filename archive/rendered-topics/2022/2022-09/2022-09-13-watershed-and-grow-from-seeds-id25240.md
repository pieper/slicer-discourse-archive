# Watershed and grow from seeds

**Topic ID**: 25240
**Date**: 2022-09-13
**URL**: https://discourse.slicer.org/t/watershed-and-grow-from-seeds/25240

---

## Post #1 by @MPhilip (2022-09-13 15:44 UTC)

<p>Hi,</p>
<p>I was trying to use watershed and grow from seeds segmentation methods on PET images. But the process of implementing the semi-automatic methods in a 3D slicer seems identical- i.e. labelling(seeds) the tumour and the background as two different segments using paint and applying the watershed or grow from seeds method. I would like to know how exactly these two segmentation methods differ.</p>
<p>I could see that grow from seeds uses a modified grow cut algorithm, which automatically segments the tumour from the background provided the seeds on the PET image. I would like to know what is done in the watershed method similarly. I used the tumour and background labelled using paint for grow from seeds and also for watershed methods. is that right?  I could read that the watershed method applies a smoothing effect to the segmented tumour whereas it is not applied for grow from seeds and the watershed is comparatively slower than grow from seeds.</p>
<p>I would also like to know how the concept of rainwater falling on terrain is implemented in the watershed method available in the 3D slicer. I am quite confused between these two methods.</p>
<p>Hope you would help.</p>
<p>Many thanks.</p>

---
