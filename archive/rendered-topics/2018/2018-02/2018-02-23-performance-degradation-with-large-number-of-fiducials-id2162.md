---
topic_id: 2162
title: "Performance Degradation With Large Number Of Fiducials"
date: 2018-02-23
url: https://discourse.slicer.org/t/2162
---

# Performance degradation with large number of fiducials

**Topic ID**: 2162
**Date**: 2018-02-23
**URL**: https://discourse.slicer.org/t/performance-degradation-with-large-number-of-fiducials/2162

---

## Post #1 by @muratmaga (2018-02-23 21:19 UTC)

<p>I loaded a dataset with ~2K fiducials.</p>
<p>Operating system: Linux (Centos 7)<br>
Slicer version: 4.8.1<br>
Expected behavior:<br>
Actual behavior: Overall slow operations (zoom in/out in slices, 3d rotation etc). Settings in markup module does not get reflected on the actual fiducials (e.g., set the text scale to 0, but text labels are still being displayed).</p>

---

## Post #2 by @lassoan (2018-02-23 22:47 UTC)

<p>Currently, Markups module only practical to use up to a few hundred points. Above that, it is better to use model nodes. In working on a new generation of Markups that will work efficiently, but it will take least a couple of more weeks to complete it.</p>

---
