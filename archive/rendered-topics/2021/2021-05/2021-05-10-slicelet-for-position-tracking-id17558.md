# Slicelet for position tracking

**Topic ID**: 17558
**Date**: 2021-05-10
**URL**: https://discourse.slicer.org/t/slicelet-for-position-tracking/17558

---

## Post #1 by @szlaci (2021-05-10 05:03 UTC)

<p>Hi Everyone,</p>
<p>I was wondering what could be a limitation of a slicelet ?</p>
<p>An application with:</p>
<ul>
<li>custom layouts</li>
<li>connected Atracsys tracker</li>
<li>own patient db</li>
</ul>
<p>could be achievable with a slicelet, or the better approach would be to build everything up from scratch in this case ?</p>

---

## Post #2 by @lassoan (2021-05-11 04:44 UTC)

<p>Using 3D Sicer + SlicerIGT + Plus toolkit for building navigation system using Atracsys tracker should be fairly straightforward, once you got to know these components.</p>
<p>You can build a complete navigation system without writing a single line of code, which should be sufficient for phantom experiments. You can create a slicelet if you have the complete workflow sorted out and ready to do patient cases (or phantom experiments with time constraints).</p>
<p>Check out <a href="http://www.slicerigt.org/wp/">SlicerIGT tutorials</a> and let us know if you have any specific questions.</p>

---
