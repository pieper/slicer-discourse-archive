---
topic_id: 32874
title: "How To Use Split Volume Segmenteditorextraeffects Effect"
date: 2023-11-17
url: https://discourse.slicer.org/t/32874
---

# How to use "split volume" (SegmentEditorExtraEffects Effect)

**Topic ID**: 32874
**Date**: 2023-11-17
**URL**: https://discourse.slicer.org/t/how-to-use-split-volume-segmenteditorextraeffects-effect/32874

---

## Post #1 by @Lara (2023-11-17 11:55 UTC)

<p>I am a biomedical engineering student and I’m doing a project using 3D Slicer. I downloaded the extension SegmentEditorExtraEffects and I need to use the tool “split volume” to isolate the jaw from the rest of the skull, but I can’t make it work. Can anyone make a step by step tutorial on how to use this tool to split one segmentation into two different segments?</p>

---

## Post #2 by @muratmaga (2023-11-17 23:26 UTC)

<aside class="quote no-group" data-username="Lara" data-post="1" data-topic="32874">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/e274bd/48.png" class="avatar"> Lara:</div>
<blockquote>
<p>split one segmentation into two different segments</p>
</blockquote>
</aside>
<p>Split volume helps you create subvolumes of the original image by saving the image contents of each segment to a different volume. It doesn’t split a segmentation into two segments.</p>
<p>You can already do that by using the existing tools within Slicer and a little bit careful masking.</p>

---

## Post #3 by @Lara (2023-11-20 11:55 UTC)

<p>Thank you for clarifying what Split Volume actually does. I still need to learn how to use it. Could you explain how to create the mandible subvolume starting from the skull volume using Split Volume? I could really use a step-by-step guide but I can’t find it anywhere</p>

---

## Post #4 by @lassoan (2023-11-20 17:07 UTC)

<p>You can split segments using Scissors effect as shown in <a href="https://lassoan.github.io/SlicerSegmentationRecipes/Craniotomy/">this segmentation recipe</a>.</p>

---

## Post #5 by @Lara (2023-11-21 10:32 UTC)

<p>Thank you, I’ve read that recipe already and I managed to split the segments using different tools. Now my professor wants me to learn how to use Split Volume instead, so if anyone could write a step-by-step tutorial I would be very grateful.</p>

---

## Post #6 by @lassoan (2023-11-21 11:55 UTC)

<p>One your have created the two segments by following the recipe, you can use Split Volume effect to create two volumes from it.</p>

---
