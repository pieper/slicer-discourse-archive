---
topic_id: 26613
title: "Lungct Analyzer Region Of Interest"
date: 2022-12-06
url: https://discourse.slicer.org/t/26613
---

# LungCT Analyzer (Region of Interest)

**Topic ID**: 26613
**Date**: 2022-12-06
**URL**: https://discourse.slicer.org/t/lungct-analyzer-region-of-interest/26613

---

## Post #1 by @Nima_Yousefi (2022-12-06 19:43 UTC)

<p>Hi all,<br>
In the subject of covid 19 mortality prediction which one of this ROI is important and interpretation must be based on it?</p>
<p>Emphysema,inflated,infiltration,collapsed,vessels</p>

---

## Post #2 by @rbumm (2022-12-06 21:05 UTC)

<p>Hi,</p>
<p>Currently we define</p>
<p><i>% Affected right lung volume (infiltrated + collapsed right volume vs. non-affected right lung volume)<br>
% Affected left lung volume (infiltrated + collapsed left volume vs.  non-affected left lung volume)<br>
% Affected total lung volume (infiltrated + collapsed total volume vs. non-affected total lung volume)</i></p>
<p>which seems to correlate with worse outcomes.</p>
<p>Vessel volume is subtracted from lung volumes, intrapulmonary airways are not subtracted.</p>

---

## Post #3 by @Nima_Yousefi (2022-12-07 08:03 UTC)

<p>Thanks.<br>
And how can I extract radiomics features from this area?<br>
The output always contain those ROI as I mentioned it</p>

---

## Post #4 by @rbumm (2022-12-07 08:40 UTC)

<p>Lung CT Analyzer is based on thresholding basic tissue characteristics by their HU ranges.<br>
It is not using, related to, or directly connected to radiomics or pyradiomics.</p>
<p>However, you can use the lung segmentation, that LCTA creates, as input regions for the Slicer Radiomics extension in order to calculate radiomics features for the right and left lung as well as lobes.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/3/f3cc4d09fc50bed05ba9adeadfd1d683f2fa16f7.png" alt="image" data-base62-sha1="yMJJL48Wx9S9FhP0i01yRJEdqfR" width="656" height="418"></p>

---
