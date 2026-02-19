---
topic_id: 16468
title: "Slicerdmri Tractography Measurements"
date: 2021-03-10
url: https://discourse.slicer.org/t/16468
---

# SlicerDMRI tractography measurements

**Topic ID**: 16468
**Date**: 2021-03-10
**URL**: https://discourse.slicer.org/t/slicerdmri-tractography-measurements/16468

---

## Post #1 by @amymanson (2021-03-10 14:05 UTC)

<p>Hi, I was wondering if anyone could clarify the meaning of one of the measurement results produced when running Diffusion-&gt;Quantify-&gt;Tractography Measurements on DTI data?</p>
<p>The measurements produced are (among others) Num_Fibres and Mean_Length.</p>
<p>Presumably the Mean_Length would be the mean length of the fibres measured. But I was wondering if Num_Fibres was the total number of fibres picked up in the tractography or just the number which were sampled for mean length?</p>
<p>Thanks!<br>
Amy</p>

---

## Post #2 by @zhangfanmark (2021-03-10 17:57 UTC)

<p>Hi!</p>
<p>Num_Fibers is the total number fiber streamlines of the input tractography file.<br>
Mean_Length is the mean of the fiber lengths across all the fiber streamlines.<br>
There is no fiber sampling process here.</p>
<p>Regards,<br>
Fan</p>

---

## Post #3 by @amymanson (2021-03-11 10:42 UTC)

<p>Great, thank you!<br>
Amy</p>

---
