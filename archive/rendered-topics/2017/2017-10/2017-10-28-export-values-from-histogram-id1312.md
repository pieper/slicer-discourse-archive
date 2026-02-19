---
topic_id: 1312
title: "Export Values From Histogram"
date: 2017-10-28
url: https://discourse.slicer.org/t/1312
---

# Export values from histogram?

**Topic ID**: 1312
**Date**: 2017-10-28
**URL**: https://discourse.slicer.org/t/export-values-from-histogram/1312

---

## Post #1 by @hherhold (2017-10-28 12:26 UTC)

<p>Is there a way to export values from the histogram in the Volumes module? There are instances where I need to make a histogram in R or something to export for publication.</p>
<p>If not, I was thinking of adding it - It looks doable, looking at qSlicerScalarVolumeDisplayWidget.cxx - once the Histogram is fed the data array and it generates the histogram, I can call value() for each of the bins to get the data. (I think.)</p>
<p>Comments/opinions/complaints?</p>
<p>Thanks!</p>
<p>-Hollister</p>

---

## Post #2 by @lassoan (2017-10-28 12:55 UTC)

<p>You can compute histogram using numpy:</p>
<pre><code>import numpy as np
histogram = np.histogram(arrayFromVolume(getNode('MRHead')))</code></pre>

---

## Post #3 by @hherhold (2017-10-28 13:13 UTC)

<p>Wow, that’s a lot simpler! Thanks!</p>

---
