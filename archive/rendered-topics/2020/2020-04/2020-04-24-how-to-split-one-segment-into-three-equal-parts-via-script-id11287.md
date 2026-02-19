---
topic_id: 11287
title: "How To Split One Segment Into Three Equal Parts Via Script"
date: 2020-04-24
url: https://discourse.slicer.org/t/11287
---

# How to split one segment into three equal parts via script?

**Topic ID**: 11287
**Date**: 2020-04-24
**URL**: https://discourse.slicer.org/t/how-to-split-one-segment-into-three-equal-parts-via-script/11287

---

## Post #1 by @Ezio_Lanza (2020-04-24 12:23 UTC)

<p>Hi,<br>
I need to create a script that splits one segment (e.g. volume lung) into three equal parts to simulate the three different lung lobes. (upper, mid and lower part).</p>
<p>Is there a good example to start or can you provide advice on the key commands to use?</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2020-04-24 16:05 UTC)

<p>If you want to split to three equal volumes then you can use the new <a href="https://discourse.slicer.org/t/new-module-for-measuring-cross-section-area-of-segments/11293">Segment cross-section area extension</a> to compute cross-sections along slices. You can get the positions as a table and get physical position of 0, 1/3, 2/3, full volume like this:</p>
<pre><code class="lang-python">crossSectionsTable = getNode('Segment cross-section area table')
positions = slicer.util.arrayFromTableColumn(crossSectionsTable, 'Position')
areas = slicer.util.arrayFromTableColumn(crossSectionsTable, 'Segment_1')

import numpy as np
volumeRatio = np.cumsum(areas)/np.sum(areas)
slicePositions = np.interp([0.0, 1.0/3.0, 2.0/3.0, 1.0], volumeRatio, positions[:,3])
print("Slice position along IS axis for zero, 1/3, 2/3, and full volumes: "+str(slicePositions))
</code></pre>

---
