---
topic_id: 356
title: "Data Probe Widget Is Empty"
date: 2017-05-21
url: https://discourse.slicer.org/t/356
---

# Data Probe widget is empty

**Topic ID**: 356
**Date**: 2017-05-21
**URL**: https://discourse.slicer.org/t/data-probe-widget-is-empty/356

---

## Post #1 by @lassoan (2017-05-21 18:13 UTC)

<p>(moved from mailing list)</p>
<p>When I try to see the HU units of a CT-scan in Slicer, I don’t anything in the dataprobe, it doesn’t respond.</p>
<p>But When I look at the nightly versions, the dataprobe works perfectly.</p>

---

## Post #2 by @lassoan (2017-05-21 18:17 UTC)

<p>Latest version of Slicer contain many fixes and improvements and it works reliably in general, so probably you’d better use that.</p>
<p>If you must use an older version then you may try to change the viewer layout. As I remember, we’ve fixed a bug some time ago that the Data Probe widget does not work if the layout contains a chart widget on startup. If you switch to another layout (for example, Four-Up layout) and then restart Slicer then it may solve the problem.</p>

---
