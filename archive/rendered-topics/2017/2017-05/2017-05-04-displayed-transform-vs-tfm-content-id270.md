---
topic_id: 270
title: "Displayed Transform Vs Tfm Content"
date: 2017-05-04
url: https://discourse.slicer.org/t/270
---

# Displayed transform vs .tfm content

**Topic ID**: 270
**Date**: 2017-05-04
**URL**: https://discourse.slicer.org/t/displayed-transform-vs-tfm-content/270

---

## Post #1 by @muratmaga (2017-05-04 22:16 UTC)

<p>Hi,<br>
I created a transform in slicer. The information part of the Transform modules shows it like this;</p>
<pre><code class="lang-auto">Transform to parent:
Linear
-0.12 -0.96 0.26 **710** 
0.99 -0.1 0.1 **19** 
-0.07 0.27 0.96 -**58** 
0 0 0 1 
</code></pre>
<p>When I save this as a .tfm, the resultant file contains this transformation:</p>
<pre><code class="lang-auto">#Insight Transform File V1.0
#Transform 0
Transform: AffineTransform_double_3_3
Parameters: -0.12281062601468536 0.9902729990354874 0.06989222618721933 -0.9559259621663395 -0.0968506562880039 -0.26898522478338405 -0.2598992353790456 -0.09944665326067206 0.9609182640368552 **-64.32660836989362 -696.1487386450094 -130.6846842169375**
FixedParameters: 0 0 0
</code></pre>
<p>While I worked out the sign changes and transposition of the matrix, I don’t know why my translations changed so much? I need to this outside of the Slicer and save each transform as a .tfm. Is there a formula I can follow?<br>
Thanks,<br>
M</p>

---

## Post #2 by @lassoan (2017-05-04 23:25 UTC)

<p>It’s a base transform between RAS/LPS and an inversion (rendering vs. resampling transform), as <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Transforms#Transform_files">described in the Transform module documentation</a>.</p>

---

## Post #3 by @hbraunDSP (2020-09-30 22:15 UTC)

<p>I know this thread is old, but it’s what came up when I searched. <a class="mention" href="/u/lassoan">@lassoan</a> I think the python code in your link is misleading as it’s only valid for rigid transforms, where the transpose of the 3x3 rotation matrix is its inverse. If there is scaling (or, I assume, shear) this condition will not be met and the answer will be wrong.  For anyone else looking at this, know that the line <code>mt[:3,3] = mt[:3,:3] @ mt[:3,3]</code> is incorrect for non-rigid transforms, and a full inverse needs to be calculated.</p>

---
