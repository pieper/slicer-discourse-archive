---
topic_id: 36540
title: "Load Data Header Modified By Pynrrd Without Writing"
date: 2024-06-01
url: https://discourse.slicer.org/t/36540
---

# Load data, header modified by pynrrd without writing

**Topic ID**: 36540
**Date**: 2024-06-01
**URL**: https://discourse.slicer.org/t/load-data-header-modified-by-pynrrd-without-writing/36540

---

## Post #1 by @Djanbo (2024-06-01 18:58 UTC)

<p>Hello,</p>
<p>I updated a labelmap and correpsonding header retrieved from a pynrrd file, how could i load it to 3d slicer without writting it?</p>
<p>Thanks in advance !</p>

---

## Post #2 by @Djanbo (2024-06-03 18:45 UTC)

<p>Hello, to give more context, let say i save my array long the header     <code>nrrd.write(nrrd_file, array, header)</code></p>
<p>i also want to load the transformed label map but without re-reading it:</p>
<pre><code class="lang-auto">label_map_node = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")
slicer.util.updateVolumeFromArray(label_map_node, array)
image_data = slicer.util.arrayFromVolume(label_map_node)
</code></pre>
<p>What i need to do after to correct the spacing, origin with the help of the header dict?</p>
<p>Thanks !</p>

---
