---
topic_id: 5121
title: "Arrayfromvolume"
date: 2018-12-18
url: https://discourse.slicer.org/t/5121
---

# arrayFromVolume

**Topic ID**: 5121
**Date**: 2018-12-18
**URL**: https://discourse.slicer.org/t/arrayfromvolume/5121

---

## Post #1 by @Abdelkhalek (2018-12-18 10:14 UTC)

<p>Hi everyone, could you please tell me how can I find the equation or the mathematical procedure which is behind the arrayFromVolume?<br>
Thank you in advance.</p>

---

## Post #2 by @Sam_Horvath (2018-12-18 13:37 UTC)

<p>The code for arrayFromVolume is here: <a href="https://github.com/Slicer/Slicer/blob/5d70815798b8f324b2a14ad6e9cfa1634edf9ba9/Base/Python/slicer/util.py#L739" rel="nofollow noopener">https://github.com/Slicer/Slicer/blob/5d70815798b8f324b2a14ad6e9cfa1634edf9ba9/Base/Python/slicer/util.py#L739</a></p>
<p>It basicly just provides a numpy view into memory managed by VTK</p>

---

## Post #3 by @Abdelkhalek (2018-12-19 11:18 UTC)

<p>Thank you Sam_Horvath for your reply. However, I am looking for the mathematical procedure(e.g., equations etc…).</p>

---

## Post #4 by @lassoan (2018-12-19 14:46 UTC)

<p>There is no mathematical procedure in <code>arrayFromVolume</code>. If you need to describe it as an equation: <em>voxelValueInArray</em> = <em>voxelValueInVolumeNode</em>.</p>

---
