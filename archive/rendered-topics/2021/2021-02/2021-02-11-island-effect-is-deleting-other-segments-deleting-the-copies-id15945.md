# Island Effect is deleting other segments (deleting the copies of my original segment)

**Topic ID**: 15945
**Date**: 2021-02-11
**URL**: https://discourse.slicer.org/t/island-effect-is-deleting-other-segments-deleting-the-copies-of-my-original-segment/15945

---

## Post #1 by @Jezza (2021-02-11 00:40 UTC)

<p>Operating system: macOS Catalina 10.15.7<br>
Slicer version: 4.11 20200930</p>
<p>I managed to duplicate a hollow (vessel wall) version of my model into a solid (blood pool) as described in this post →  <a href="https://discourse.slicer.org/t/how-would-people-extract-center-line-on-a-hollow-model/15927" class="inline-onebox">How would people extract center line on a hollow model?</a></p>
<p>Now, when I apply the Island Effect "keep largest island’ on either the hollow segment or the solid segment, <strong>the other segment gets deleted aswell!</strong></p>
<p>I thought that any effects would <strong>only</strong> apply to the <strong>selected</strong> segment, yet it seems that using the “copy” (logical operator) tool gives both segments the same identity and 3DSlicer treats them both as the same segment? Is there a way to make them separate? I do not want my tools to affect both segments simultaneously when I have only selected one of them.</p>

---

## Post #2 by @lassoan (2021-02-11 00:53 UTC)

<p>Copy does not connects segments in any way, if in masking settings you selected “Allow overlap”.</p>
<p>If overlap is allowed (or the segments do not overlap) and modifying a segment still seem to affect another segment then try to do the same in a recent Slicer Preview Release. There were some related fixes since the Slicer-4.11 20200930 release.</p>

---

## Post #3 by @Jezza (2021-02-11 19:54 UTC)

<p>Thank you, I’ll have a look at that!</p>

---
