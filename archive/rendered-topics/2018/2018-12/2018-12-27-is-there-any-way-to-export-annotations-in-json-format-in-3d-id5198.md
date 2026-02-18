# Is there any way to export annotations in Json format in 3D slicer?

**Topic ID**: 5198
**Date**: 2018-12-27
**URL**: https://discourse.slicer.org/t/is-there-any-way-to-export-annotations-in-json-format-in-3d-slicer/5198

---

## Post #1 by @akhila_perumalla (2018-12-27 04:31 UTC)

<p>Operating system: WIndows<br>
Slicer version: 4.10.0<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2018-12-27 05:10 UTC)

<p>Yes, you can do it by a few lines of Python code (that you can either copy-paste to the Python console, in a Jupyter notebook, or in a scripted module). For example, export markup fiducials into a json file:</p>
<pre><code class="lang-auto">markupNode = getNode('F')
outputFileName = 'c:/tmp/test.json'

data = []
for fidIndex in range(markupNode.GetNumberOfFiducials()):
  coords=[0,0,0]
  markupNode.GetNthFiducialPosition(fidIndex,coords)
  data.append({'label': markupNode.GetNthFiducialLabel(), 'position': coords})

import json
with open(outputFileName, 'w') as outfile:
  json.dump(data, outfile)
</code></pre>

---

## Post #3 by @akhila_perumalla (2018-12-28 01:46 UTC)

<p>Hi, Can I export segmentation results into json file?</p>

---

## Post #4 by @lassoan (2018-12-28 02:25 UTC)

<p>Do you mean writing the 3D voxel array? Of course, it is easily doable, but it would be terribly inefficient.</p>

---
