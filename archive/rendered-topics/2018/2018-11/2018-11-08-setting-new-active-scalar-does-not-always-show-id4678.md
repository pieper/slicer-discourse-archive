---
topic_id: 4678
title: "Setting New Active Scalar Does Not Always Show"
date: 2018-11-08
url: https://discourse.slicer.org/t/4678
---

# Setting new active scalar does not always show

**Topic ID**: 4678
**Date**: 2018-11-08
**URL**: https://discourse.slicer.org/t/setting-new-active-scalar-does-not-always-show/4678

---

## Post #1 by @Niels (2018-11-08 10:48 UTC)

<p>In python I change the scalar of my new model. this works fine at first, but when I regenerate the model and scalar values it does not show directly the second time. In the model UI I see the correct scalar being selected, but I have to first select another and then back to the one I prefer to make the changes have effect. The scalar values must be correct and python code to select the scalar as well, but I think I am missing something. An update maybe?</p>
<p>modelDisplayNode.SetActiveScalarName(“Normal”) # do. this to make the new/next scalar to show<br>
modelDisplayNode.SetActiveScalarName(“RGB”)</p>
<p>I already tried calling Modified for the scalarArray, modelNode and DisplayNode.</p>

---

## Post #2 by @pieper (2018-11-08 12:47 UTC)

<p>Yes, this sounds like a bug - can you adapt your code to make a short script that exactly replicates the issue (creates a model, sets the scalars, etc) to facilitate debugging?</p>

---

## Post #3 by @lassoan (2018-11-08 14:15 UTC)

<p>You need to set up a few more things (enable scalar display, set range, color node, etc.) see example in <a href="https://discourse.slicer.org/t/is-there-any-way-to-draw-hundreds-of-balls-with-different-colors/572/7?u=lassoan">this post</a>. Let us know if you have still have issues.</p>

---
