---
topic_id: 6414
title: "How To Reduce Size Of The Stl File Generated Through Python"
date: 2019-04-05
url: https://discourse.slicer.org/t/6414
---

# How to reduce size of the stl file generated through python script?

**Topic ID**: 6414
**Date**: 2019-04-05
**URL**: https://discourse.slicer.org/t/how-to-reduce-size-of-the-stl-file-generated-through-python-script/6414

---

## Post #1 by @Siddharth_Sharma (2019-04-05 21:58 UTC)

<p>i am using <a href="https://gist.github.com/lassoan/1673b25d8e7913cbc245b4f09ed853f9" rel="nofollow noopener">this script</a> to generate a stl file.<br>
i want to reduce the size/quality of the stl file generated through python script. how will i do that?</p>

---

## Post #2 by @techrama (2019-04-09 04:07 UTC)

<p>for example</p>
<pre><code>import numpy
from stl import mesh

# Using an existing stl file:
your_mesh = mesh.Mesh.from_file('some_file.stl')

# Or creating a new mesh (make sure not to overwrite the `mesh` import by
# naming it `mesh`):
VERTICE_COUNT = 100
data = numpy.zeros(VERTICE_COUNT, dtype=mesh.Mesh.dtype)
your_mesh = mesh.Mesh(data, remove_empty_areas=False)

# The mesh normals (calculated automatically)
your_mesh.normals
# The mesh vectors
your_mesh.v0, your_mesh.v1, your_mesh.v2
# Accessing individual points (concatenation of v0, v1 and v2 in triplets)
assert (your_mesh.points[0][0:3] == your_mesh.v0[0]).all()
assert (your_mesh.points[0][3:6] == your_mesh.v1[0]).all()
assert (your_mesh.points[0][6:9] == your_mesh.v2[0]).all()
assert (your_mesh.points[1][0:3] == your_mesh.v0[1]).all()

your_mesh.save('new_stl_file.stl')</code></pre>

---

## Post #3 by @lassoan (2019-04-09 04:23 UTC)

<p><a class="mention" href="/u/techrama">@techrama</a> Would you like to tell us what the code snippet above is supposed to do?</p>
<p><a class="mention" href="/u/siddharth_sharma">@Siddharth_Sharma</a> You can decrease size &amp; quality of the generated mesh by adding this line before <code>CreateClosedSurfaceRepresentation</code> method call:</p>
<pre><code>segmentationNode.GetSegmentation().SetConversionParameter("Decimation factor", "0.9") 
</code></pre>
<p>The parameter value is between 0.0-1.0 and it specifies the fraction points that you would like to remove from the mesh.</p>

---

## Post #4 by @techrama (2019-04-26 15:50 UTC)

<p>Do you still want me to explain or you got it?</p>

---

## Post #5 by @jamesobutler (2019-04-26 16:01 UTC)

<p>Source of <a class="mention" href="/u/techrama">@techrama</a> 's code can be found at <a href="https://numpy-stl.readthedocs.io/en/latest/usage.html#quickstart" rel="nofollow noopener">https://numpy-stl.readthedocs.io/en/latest/usage.html#quickstart</a>, if others want to look more into it. It is listed as a “Quickstart” example set.</p>

---
