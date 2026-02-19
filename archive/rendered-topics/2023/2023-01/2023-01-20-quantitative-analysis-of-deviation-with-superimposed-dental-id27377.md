---
topic_id: 27377
title: "Quantitative Analysis Of Deviation With Superimposed Dental"
date: 2023-01-20
url: https://discourse.slicer.org/t/27377
---

# Quantitative analysis of deviation with superimposed dental arches

**Topic ID**: 27377
**Date**: 2023-01-20
**URL**: https://discourse.slicer.org/t/quantitative-analysis-of-deviation-with-superimposed-dental-arches/27377

---

## Post #1 by @PaVo (2023-01-20 13:12 UTC)

<p>Hello everyone<br>
I’m quite new to the slicer software, so please be kind to the rookie <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=12" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20"><br>
I’m doing my master thesis in the field of orthodontic tooth movement. One of my tasks is to quantitatively analyze dental arches. This means I have for example an intraoral scan (STL file) of the patients teeth (one for upper and one for lower arch) before and treatment happened, and a scan after the treatment. What I want to know is how much did every single tooth move. For this, I need to set a global coordinate system which should be the same for the compared (before and after treatment) arches. Looking at literature, there are various ways to do this. I was able to superimpose two STL models with some manually set reference points. This works quite well. I was also able to generate a deviation map. But this only indicates a more qualitative analysis. Is there a package/method where I can do the segmentation for teeth/gingiva where I get local coordinte systems for each tooth, and then calculate the translational matrix for each tooth between initial and post-treatment state? Let’s say by doing a least square fit for the corresponding teeth.</p>

---

## Post #2 by @Husam_Soboh (2023-11-12 23:47 UTC)

<p>Hey, did you manage to find a proper way to do it? I need to do something similar and im encountering issues, the learning curve is huge.</p>

---
