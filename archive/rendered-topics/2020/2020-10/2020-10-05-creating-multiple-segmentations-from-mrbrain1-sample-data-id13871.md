---
topic_id: 13871
title: "Creating Multiple Segmentations From Mrbrain1 Sample Data"
date: 2020-10-05
url: https://discourse.slicer.org/t/13871
---

# Creating multiple segmentations from MRBrain1 sample data

**Topic ID**: 13871
**Date**: 2020-10-05
**URL**: https://discourse.slicer.org/t/creating-multiple-segmentations-from-mrbrain1-sample-data/13871

---

## Post #1 by @dayanjan (2020-10-05 20:11 UTC)

<p>Hi All,</p>
<p>I have been trying to do a multiple segmentation with MRBrain1 sample data, but have not had much luck in getting exactly what I want. Hoping you guys can help.</p>
<p>I want to create multiple segments in the following order</p>
<ol>
<li>Skin (or something approximating it) that determines the external boundary</li>
<li>The bones of the skull</li>
<li>The brain alone without the tumor</li>
<li>The tumour by itself</li>
</ol>
<p>I have been trying various combination of swissskullstripper based segmentation and coupling it to other methods, but so far have not hit upon the correct combination to achieve this. Does anyone know how best to achieve this goal?</p>
<p>Kind Regards,</p>
<p>-Dayanjan</p>

---

## Post #2 by @lassoan (2020-10-05 20:41 UTC)

<p>This neurosurgical planning tutorial should be a good starting point: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Neurosurgical_Planning_Tutorial">https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Neurosurgical_Planning_Tutorial</a></p>
<p>Skin segmentation should be trivial, using thresholding and with optional solidification. See recipe here: <a href="https://lassoan.github.io/SlicerSegmentationRecipes/SkinSurface2/">https://lassoan.github.io/SlicerSegmentationRecipes/SkinSurface2/</a></p>
<p>Skull: since bones are not visible on MRI, this can be hard (depending on what kind of images you have, how noisy they are, what accuracy you need, etc.). We don’t see much interest in skull segmentation in MRI, but many people are exploring special bone sequences for spine and other MSK imaging, which might be applicable for head imaging, too.</p>
<p>Brain: Swiss skull stripper usually gives acceptable results.</p>
<p>Tumor: Usually Grow from seeds method works well (see neurosurgical planning tutorial for details). For highly visible tumors, fully automatic AI segmentation may save a few minutes (see tutorial <a href="https://github.com/NVIDIA/ai-assisted-annotation-client/tree/master/slicer-plugin#nvidia-ai-assisted-annotation-aiaa-for-3d-slicer">here</a>).</p>

---

## Post #3 by @dayanjan (2020-10-05 20:53 UTC)

<p>Many thanks Andras! The challenge I had with the swissskullstripper is that once it is run, the skull is gone. Thus while I had the brain segmented out nicely, I would have liked to have another segment containing everything other than the brain. Do you know of a way to combine the swissskullstripper with another tool so I can have the brain as one segment and everything other than the brain as a separate segment?</p>
<p>As always, your advice and help is much appreciated by all of us!</p>
<p>Regards,</p>
<p>Dayanjan</p>

---

## Post #4 by @lassoan (2020-10-06 19:49 UTC)

<aside class="quote no-group" data-username="dayanjan" data-post="3" data-topic="13871">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dayanjan/48/12889_2.png" class="avatar"> dayanjan:</div>
<blockquote>
<p>The challenge I had with the swissskullstripper is that once it is run, the skull is gone</p>
</blockquote>
</aside>
<p>You still have the original image, so you can use that to extract skin surface, etc. You can subtract brain from head (skin surface) using “Logical operators” effect in Segment Editor.</p>

---

## Post #5 by @dayanjan (2020-10-06 23:36 UTC)

<p>Thanks Andras!</p>
<p>-Dayanjan</p>

---
