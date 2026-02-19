---
topic_id: 26501
title: "Calculating Vector Trigeminal Nerve"
date: 2022-11-30
url: https://discourse.slicer.org/t/26501
---

# Calculating vector trigeminal nerve

**Topic ID**: 26501
**Date**: 2022-11-30
**URL**: https://discourse.slicer.org/t/calculating-vector-trigeminal-nerve/26501

---

## Post #1 by @maudboreel (2022-11-30 00:31 UTC)

<p>For a research project, I am segmenting vestibular schwannomas with the neighbouring trigeminal nerve. The vector of the nerve changes of the years because of mass effect of the vestibular schwannoma. Is there a way to calculate the changing vector of the trigeminal nerve?</p>
<p>Slicer version: 5.0.3</p>

---

## Post #2 by @lassoan (2022-12-01 04:06 UTC)

<p>If you segment the trigeminal nerve then you can get its principal axes directions using Segment Statistics module. If you don’t need to segment the nerve for other reasons then you can get the orientation by drawing a line markup on it.</p>
<p>I would recommend to also define two reference lines (for example one in left-right, another one in anterior-posterior direction). The lines can be based on easily identifiable landmarks (if you use CT images then they can be bones). The two lines specify a coordinate system that you can use as a basis for evaluating the nerve direction.</p>

---
