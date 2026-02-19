---
topic_id: 8904
title: "Resample Pet Image"
date: 2019-10-25
url: https://discourse.slicer.org/t/8904
---

# Resample PET image

**Topic ID**: 8904
**Date**: 2019-10-25
**URL**: https://discourse.slicer.org/t/resample-pet-image/8904

---

## Post #1 by @zahiraabdala (2019-10-25 15:28 UTC)

<p>Hi all, I need to resample my PET image and I have a problem.<br>
When I resample my image in Slicer using the Resample Image (Brains) module, the image ends up correctly resampled except its image activity information, it´s show a different values of the original image. Someone know which could be a problem?<br>
Thanks.</p>

---

## Post #2 by @pieper (2019-10-25 16:04 UTC)

<p>How different are the values?  Some small amount of difference is expected due to filtering.</p>

---

## Post #3 by @zahiraabdala (2019-10-25 16:15 UTC)

<p>Before at resample the image activity it´s  more than 20000 Bq/ml and after resampling it´s 3000 Bq/ml</p>

---

## Post #4 by @pieper (2019-10-25 17:07 UTC)

<p>That sounds pretty big - is there anyway this can be reproduced using shareable data?  E.g. what happens if you use <a href="https://wiki.cancerimagingarchive.net/display/Public/QIN-HEADNECK">public PET data</a>?</p>

---

## Post #5 by @zahiraabdala (2019-10-25 18:05 UTC)

<p>I don´t know how to use this public PET data, I´m in the webside but I don´t know where are the example. Can you help me with this?</p>

---

## Post #6 by @pieper (2019-10-25 18:33 UTC)

<p>There’s sample PET data and instructions as part of this tutorial:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.10/Training#Slicer4_Quantitative_Imaging_tutorial" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.10/Training#Slicer4_Quantitative_Imaging_tutorial</a></p>

---
