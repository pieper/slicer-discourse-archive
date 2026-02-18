# Using paint function results in segmentation on adjacent slice

**Topic ID**: 10912
**Date**: 2020-03-30
**URL**: https://discourse.slicer.org/t/using-paint-function-results-in-segmentation-on-adjacent-slice/10912

---

## Post #1 by @cydneyma (2020-03-30 19:55 UTC)

<p>Hi all,</p>
<p>New to the forum here. I am experiencing an issue wherein every time I try to “paint” a given slice, it paints the adjacent slice instead. I have checked that I don’t have “sphere brush” selected. I have also looked at the original solution to this question (<a href="https://discourse.slicer.org/t/segmentation-editor-how-to-disable-painting-on-adjacent-slices/1459/4" class="inline-onebox">Segmentation Editor - How to disable painting on adjacent slices?</a>) but was unable to figure out how to navigate to ‘rotate to volume plane’. Would appreciate any guidance on how to proceed here!</p>
<p>Thanks in advance!</p>
<p>Cydney</p>

---

## Post #2 by @lassoan (2020-03-30 20:02 UTC)

<aside class="quote no-group" data-username="cydneyma" data-post="1" data-topic="10912">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cydneyma/48/6403_2.png" class="avatar"> cydneyma:</div>
<blockquote>
<p>I have checked that I don’t have “sphere brush” selected. I have also looked at the original solution to this question (<a href="https://discourse.slicer.org/t/segmentation-editor-how-to-disable-painting-on-adjacent-slices/1459/4">Segmentation Editor - How to disable painting on adjacent slices?</a>)</p>
</blockquote>
</aside>
<p>I’ve added detailed instructions there about what exactly to click.</p>
<p>You may find it easier to click the “warning” icon next to the segmentation node selector to align all the slice views to volume axes automatically. See more details here: <a href="https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/" class="inline-onebox">Overview | 3D Slicer segmentation recipes</a></p>

---

## Post #3 by @cydneyma (2020-03-30 22:30 UTC)

<p>Ok great - thanks, Andras! The issue has been resolved.</p>

---
