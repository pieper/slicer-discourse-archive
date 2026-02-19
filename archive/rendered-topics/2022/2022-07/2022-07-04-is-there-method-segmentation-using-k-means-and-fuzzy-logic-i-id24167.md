---
topic_id: 24167
title: "Is There Method Segmentation Using K Means And Fuzzy Logic I"
date: 2022-07-04
url: https://discourse.slicer.org/t/24167
---

# Is there method segmentation using K-means and Fuzzy logic in 3D Slicer

**Topic ID**: 24167
**Date**: 2022-07-04
**URL**: https://discourse.slicer.org/t/is-there-method-segmentation-using-k-means-and-fuzzy-logic-in-3d-slicer/24167

---

## Post #1 by @akmal871026 (2022-07-04 05:08 UTC)

<p>Dear all,</p>
<p>Anyone know in 3D slicer, is it have the method of fuzzy logic and K-means for tumor/lesion segmentation?</p>

---

## Post #2 by @lassoan (2022-07-04 12:01 UTC)

<p>Over the years many segmentation algorithms were added, but only some of them proven to be practically useful: that are not just accurate enough but also fast enough and allow the user to make corrections but not require too much user inputs.</p>
<p>We can say that the winner is fast grow cut method (available as “Grow from seeds” effect in Segment Editor). Fast marching, watershed, robust flood full, morphological interpolation are also available in Segment Editor and can be useful in some special cases (e.g., for very easy or very hard segmentation tasks).</p>
<p>ITK library that is included in Slicer has meant additional algorithms but none of them seem to be so good that people would ask for making them available in the Slicer GUI; or they asked for them, we evaluated them, and concluded that they are not good enough compared to already existing tools; or they were added at some point but then they were not maintained and got removed. Your can try some of these methods by using “Simple Filters” module or using a little Python scripting.</p>
<p>However, manual and, classic semi-automatic tools nowadays do not get much attention, as they are mostly used for training deep learning networks.</p>
<p>While you can re-evaluate classic segmentation methods, such as K-means or Fuzzy C-means, most likely they will not perform better than other classic methods and so a better use of your time would be to use existing tools for producing high-quality training data for deep learning based tools (such as <a href="https://github.com/Project-MONAI/MONAILabel">MONAILabel extension</a>).</p>

---
