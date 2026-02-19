---
topic_id: 34049
title: "How To Get The Segmentation Data"
date: 2024-01-30
url: https://discourse.slicer.org/t/34049
---

# How to get the segmentation data?

**Topic ID**: 34049
**Date**: 2024-01-30
**URL**: https://discourse.slicer.org/t/how-to-get-the-segmentation-data/34049

---

## Post #1 by @tueboesen (2024-01-30 13:39 UTC)

<p>I am still learning my way around slicer 3D.</p>
<p>I have learned that I can get the data volume in numpy format as:<br>
data_vol = getNode(‘Data’)<br>
data_vol_np = slicer.utils.arrayFromVolume(data_vol)</p>
<p>Now I would like to be able to get the segmentations as well somehow.</p>
<p>I can get the segmentation node as:<br>
b = getNode(‘Segmentation’)</p>
<p>and in that I can get the actual segmentations as:<br>
c = b.GetSegmentation()</p>
<p>and under that I can get the n’th segmentation layer as:</p>
<p>d=c.GetNthSegment(n)</p>
<p>But how do I actually get a numpy dataset of the segmentations? I still haven’t found that in all this.</p>

---

## Post #2 by @pieper (2024-01-30 15:47 UTC)

<p>The script repository is always worth looking through:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#read-and-write-a-segment-as-a-numpy-array">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#read-and-write-a-segment-as-a-numpy-array</a></p>

---
