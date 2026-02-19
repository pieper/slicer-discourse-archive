---
topic_id: 12198
title: "How To Automatically Segment Multiple Lumbar Vertebrae Thoru"
date: 2020-06-24
url: https://discourse.slicer.org/t/12198
---

# How to automatically segment multiple lumbar vertebrae thorugh the Python Interactor?

**Topic ID**: 12198
**Date**: 2020-06-24
**URL**: https://discourse.slicer.org/t/how-to-automatically-segment-multiple-lumbar-vertebrae-thorugh-the-python-interactor/12198

---

## Post #1 by @vertebra (2020-06-24 14:31 UTC)

<p>We have been researching and able to finally segment all the lumbar vertebrae manually(but we used scissors and erase, something Python cannot do on a case by case basis). We seek assistance in now automating that process. Do we need to add extensions for flood fill? If so, how do we do download those extensions to the extension wizard?</p>

---

## Post #2 by @lassoan (2020-06-24 15:20 UTC)

<aside class="quote no-group" data-username="vertebra" data-post="1" data-topic="12198">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vertebra/48/7475_2.png" class="avatar"> vertebra:</div>
<blockquote>
<p>Do we need to add extensions for flood fill?</p>
</blockquote>
</aside>
<p>You can find Flood fill and other effects in SegmentEditorExtraEffects extension.</p>
<aside class="quote no-group" data-username="vertebra" data-post="1" data-topic="12198">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vertebra/48/7475_2.png" class="avatar"> vertebra:</div>
<blockquote>
<p>We have been researching and able to finally segment all the lumbar vertebrae manually(but we used scissors and erase, something Python cannot do on a case by case basis). We seek assistance in now automating that process.</p>
</blockquote>
</aside>
<p>In the last 20-30 years, hundreds of researchers tried to implement fully automatic method for individual vertebra segmentation on CT images using “classic” methods, but they all mostly failed. So, I would not recommend to try to automate your current semi-automatic workflow by trying to replace the remaining manual steps.</p>
<p>If you need to segment a few hundred cases then probably the fastest is to use your current semi-automatic segmentation workflow. Maybe tune it a it further to ensure that it is as convenient as possible (if you describe your current workflow in detail and the main pain points then I can give advice for streamlining it).</p>
<p>If you need to segment thousands or tens of thousands of cases (or you just want to have a fully automatic segmentation method for other reasons), then you can use the first few hundred semi-automatic segmentation results to train a neural network, which can then automate the remaining cases fully automatically. This is of course not as simple as it sounds, but is still the most promising approach known to date.</p>

---

## Post #3 by @vertebra (2020-06-25 14:20 UTC)

<p>Thank you! One last question, we realized that the process only needs to be semi-automatic as the user will identify a point on the lumbar to segment that singular vertebra. Is there a way using the Python Interactor to mark points at certain coordinates with black space between the vertebrae?</p>

---

## Post #4 by @lassoan (2020-06-26 02:04 UTC)

<p>Yes, you can easily add a button to your module’s user interface that allows the user to place a markup point. See examples in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Switching_to_markup_fiducial_placement_mode">script repository</a>.</p>

---
