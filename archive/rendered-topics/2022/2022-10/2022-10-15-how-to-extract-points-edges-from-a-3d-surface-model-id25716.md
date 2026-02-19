---
topic_id: 25716
title: "How To Extract Points Edges From A 3D Surface Model"
date: 2022-10-15
url: https://discourse.slicer.org/t/25716
---

# How to extract points(edges) from a 3D surface model?

**Topic ID**: 25716
**Date**: 2022-10-15
**URL**: https://discourse.slicer.org/t/how-to-extract-points-edges-from-a-3d-surface-model/25716

---

## Post #1 by @Chm (2022-10-15 07:36 UTC)

<p>Dear all,</p>
<p>I have hollow 3D objects and i need to to extract all the points(edges) from their surfuces in order to calculate the mean distance.</p>
<p>How can i extract all these points ?</p>
<p>Thanks a lot,<br>
Chris</p>

---

## Post #2 by @jumbojing (2022-10-15 12:45 UTC)

<p>slicer.util.array(“modelName”)</p>

---

## Post #3 by @lassoan (2022-10-15 17:20 UTC)

<p>Do you yoy ant to compute distance between two surface meshes?</p>

---

## Post #4 by @Chm (2022-10-15 17:26 UTC)

<p>Yes correct, the mean distance between all the surfaces points of the two models.<br>
Thanks<br>
Chris</p>

---

## Post #5 by @lassoan (2022-10-15 18:41 UTC)

<p>You can use ModelToModelDistance extension for this.</p>

---

## Post #6 by @Chm (2022-10-15 22:34 UTC)

<p>Thanks a lot Andras<br>
I will check it</p>

---

## Post #7 by @jumbojing (2022-10-16 00:31 UTC)

<p>e.g.:</p>
<pre><code class="lang-auto">mod1Arr = slicer.util.array("model1Name")
mod2Arr = slicer.util.array("model2Name")
#  the mean distance can be calculated by the center of mass
mod1Cen = np.mean(mod1Arr, axis=0)
mod2Cen = np.mean(mod2Arr, axis=0)
meanDist = np.linalg.norm(mod2Cen - mod1Cen)
</code></pre>
<p>The nearest distance may be found by “ModelToModelDistance extension” as followed by <a class="mention" href="/u/lassoan">@lassoan</a> …</p>

---
