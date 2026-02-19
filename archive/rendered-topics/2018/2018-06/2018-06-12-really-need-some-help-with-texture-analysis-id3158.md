---
topic_id: 3158
title: "Really Need Some Help With Texture Analysis"
date: 2018-06-12
url: https://discourse.slicer.org/t/3158
---

# Really need some help with texture analysis!

**Topic ID**: 3158
**Date**: 2018-06-12
**URL**: https://discourse.slicer.org/t/really-need-some-help-with-texture-analysis/3158

---

## Post #1 by @geoderis (2018-06-12 19:37 UTC)

<p>Hello everyone, I am really asking for some help here as I am not very familiar with the software.<br>
I am trying to perform texture analysis on tumors in order to quantify their heterogeneity. (4.8.1 version)<br>
I will write down the exact process I am following, so you can make any necessary corrections.</p>
<p>First I go to segment editor. I choose the right volume and then I add my segment. I use the brush to paint the entire tumor. Then I export it and go to heterogeneity CAD.<br>
On input node I add segmentation label.<br>
On label map ROI I add segmentation label.<br>
Then I apply Heterogeneity CAD.</p>
<p>I am concerned that the process I am following is not correct because there are considerable discrepancies when I make repeated measurements of the same tumor. Plus, most of the values in the first order statistics (eg kurtosis, skewness, etc) are 0 , 1 or -3.<br>
Moreover, when I tried to make single slice measurements in fat and muscle, the values were exactly the same.</p>
<p>Please give some advice to resolve this confusion!</p>
<p>Thank you in advance.</p>

---

## Post #2 by @fedorov (2018-06-12 20:05 UTC)

<p>You could also consider using SlicerRadiomics extension: <a href="https://github.com/Radiomics/SlicerRadiomics/blob/master/README.md" class="inline-onebox">SlicerRadiomics/README.md at master · AIM-Harvard/SlicerRadiomics · GitHub</a></p>
<aside class="quote no-group" data-username="geoderis" data-post="1" data-topic="3158">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/a587f6/48.png" class="avatar"> geoderis:</div>
<blockquote>
<p>I am concerned that the process I am following is not correct because there are considerable discrepancies when I make repeated measurements of the same tumor.</p>
</blockquote>
</aside>
<p>At least with SlicerRadiomics, if you extract the features using the same image and the same segmentation repeatedly, you should be getting identical values (to the machine precision). If this is not the case, let us know.</p>

---

## Post #3 by @geoderis (2018-06-13 15:53 UTC)

<p>Thank you very much! This extension seems to be a lot more helpful.</p>

---
