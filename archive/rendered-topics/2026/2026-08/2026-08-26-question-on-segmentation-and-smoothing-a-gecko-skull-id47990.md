---
topic_id: 47990
title: "Question on Segmentation and Smoothing a Gecko Skull"
date: 2026-08-26
url: https://discourse.slicer.org/t/47990
last_bumped: 2026-08-26T18:51:15.525Z
---

# Question on Segmentation and Smoothing a Gecko Skull

**Topic ID**: 47990
**Date**: 2026-08-26
**URL**: https://discourse.slicer.org/t/question-on-segmentation-and-smoothing-a-gecko-skull/47990

---

## Post #1 by @GBurkin (2026-08-26 18:08 UTC)

<p>Hello,</p>
<p>I’m working with CT scans of small geckos, and I’m working on segmenting their skulls and full skeletons. I have mostly taught myself how to segment via YouTube and help pages, but most of these are focused on human (or larger species) anatomy.</p>
<p>Since my bones are so much smaller, I was wondering if I needed to change anything about the larger bone segmentation process?</p>
<p>I have also been trying to figure out what smoothing method would be best for such small bones? I don’t want to lose any of the features or shrink the bones because I want to put landmarks on them later in the process. So I was hoping someone might know the best smoothing tool to use, or if I shouldn’t use one at all.</p>
<p>I’m currently using Slicer version 5.10.0, but also wanted to know if it was better to download the newest version and use that?</p>
<p>Thank you so much for the help, I’m a bit out of my depth at the moment!</p>

---

## Post #2 by @muratmaga (2026-08-26 18:36 UTC)

<p>Most of the time you always want to use the latest stable, which is currently 5.12.3. Once a new stable is cut an older version like 5.10 no longer receives updates, fixes etc…</p>
<p>As long as you properly understand some filters take settings in physical values (like mm), versus some takes voxel values, then the scale of data doesn’t matter. For example, if you specified your smoothing kernel 3x3x3 mm, and your original data is 10 microns, then you practically set it to use 300x300x300 voxels which will crash or stall your computer. I think most filters in segment editor show both, but still be careful.</p>
<p>There is no perfect segmentation, nor there is hard rules about smoothing. Most of the time your landmarking error (going a few times back and trying to mark the same position) are likely at the same scale (or higher) than the geometic changes introduced by smoothing. Obviously if you smoothened the model to the extend that you can no longer find the holes or bumps you are looking for, then that’s too much.</p>
<p>You may want to get familiar with our SlicerMorph extension and its surrounding ecosystem. We have an extensive library of tutorials for people using Slicer for non-medical datasets <a href="https://github.com/SlicerMorph/Tutorials" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerMorph/Tutorials: SlicerMorph module tutorials · GitHub</a>.</p>

---

## Post #3 by @GBurkin (2026-08-26 18:51 UTC)

<p>Thank you so much! I’ll double-check the physical values and look at the SlicerMorph tutorials!</p>

---
