# Adapt segmentation already made

**Topic ID**: 35162
**Date**: 2024-03-29
**URL**: https://discourse.slicer.org/t/adapt-segmentation-already-made/35162

---

## Post #1 by @Andrea_D_Antoni (2024-03-29 12:32 UTC)

<p>Hi,</p>
<p>Recently I’ve used slicer to segment some teeth (4 exactly) from a CT scan that I had to crop.<br>
I have received the task now to segment those teeth again from the same CT but cropped in a different way.</p>
<p>Is there a way to avoid re-segmenting the teeth  from the beginning and use the segmentation that I have already made from the old CT and “adapt” it to the new cropped CT?</p>
<p>Thank you</p>

---

## Post #2 by @pieper (2024-03-29 13:00 UTC)

<p>You should be able to register the two different croppings and then transfer the segmentation via the transform.</p>

---

## Post #3 by @Andrea_D_Antoni (2024-03-29 13:50 UTC)

<p>Thank you so much!</p>
<p>After the manual movement of the segmentation in the transform section is there a way to make the adptation “perfect”?</p>

---

## Post #4 by @pieper (2024-03-29 14:00 UTC)

<p>If the two croppings have the same pixel spacing and orientation then then a binary labelmap should transform losslessly.  However if they vary then there will need to be some resampling.  In this case maybe supersampling (increasing both segmentation grids) might avoid some of the loss.</p>

---
