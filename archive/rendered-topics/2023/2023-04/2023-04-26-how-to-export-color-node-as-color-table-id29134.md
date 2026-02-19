---
topic_id: 29134
title: "How To Export Color Node As Color Table"
date: 2023-04-26
url: https://discourse.slicer.org/t/29134
---

# How to export color node as color table

**Topic ID**: 29134
**Date**: 2023-04-26
**URL**: https://discourse.slicer.org/t/how-to-export-color-node-as-color-table/29134

---

## Post #1 by @dyollb (2023-04-26 09:01 UTC)

<p>I would like to convert a slicer .seg.nrrd segmentation into a labelmap + color table, so I can use it downstream in other applications. I figured out how to convert the segmentation to a labelmap and I can see the color node under the Data (All nodes) section. Is there a way I can export it to the color table format, described e.g. <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/colors.html#color-table-file-format-txt-ctbl" rel="noopener nofollow ugc">here</a>?</p>
<p>The slicer color table format is easy to parse (and already supported by the tool I am using).</p>

---

## Post #2 by @dyollb (2023-04-27 14:31 UTC)

<p>I guess I could access the labelmap node via <code>getNode("name of node")</code>. I didn’t see what api I could use to export the color table (or more importantly the index and name mapping).</p>
<p>As a workaround I used the <code>slicerio</code> module to export the segmentation as a labelmap and save the color table (by hand):</p>
<pre><code class="lang-python">import slicerio
import nrrd
import random
import numpy as np
from pathlib import Path

input_filename = "/Users/lloyd/Downloads/segIEMap.seg.nrrd"
output_filename = "/Users/lloyd/Downloads/segIEMap.nrrd"

voxels, header = nrrd.read(input_filename)
segmentation_info = slicerio.read_segmentation_info(input_filename)

number_of_segments = len(segmentation_info["segments"])
print(f"Number of segments: {number_of_segments}")

segment_names = slicerio.segment_names(segmentation_info)

segment_names_to_labels = []
for idx, name in enumerate(segment_names, start=1):
    segment_names_to_labels.append((name, idx))

print(segment_names_to_labels)

voxels3, map = slicerio.extract_segments(voxels, header, segmentation_info, segment_names_to_labels)
nrrd.write(output_filename, voxels3)

with open(Path(output_filename).with_suffix(".txt"), "w") as f:
    print("# Color table file", file=f)
    print(f"# {len(segment_names_to_labels) + 1} values", file=f)
    print("0 Background 0 0 0 0", file=f)
    for (name, idx) in segment_names_to_labels:
        print(f"{idx} {name} {random.randint(0, 255)} {random.randint(0, 255)} {random.randint(0, 255)} 255", file=f)
</code></pre>

---
