---
topic_id: 34285
title: "Create Labelmap Nrrd File From Numpy Array"
date: 2024-02-13
url: https://discourse.slicer.org/t/34285
---

# Create labelmap nrrd file from numpy array

**Topic ID**: 34285
**Date**: 2024-02-13
**URL**: https://discourse.slicer.org/t/create-labelmap-nrrd-file-from-numpy-array/34285

---

## Post #1 by @Elias_Kim (2024-02-13 12:40 UTC)

<p>Hi,</p>
<p>I’m interested in converting a numpy array into a .nrrd file that functions as a label map in 3D slicer.</p>
<p>This numpy array represents the output of a custom semantic segmentation model, containing 33 distinct classes by integer values.</p>
<p>I wonder if I could transform this prediction mask into a label map file format that is compatible with 3D slicer.</p>
<p>I would really appreciate some help. Thank you.</p>

---

## Post #2 by @muratmaga (2024-02-13 17:00 UTC)

<p>See this:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.addVolumeFromArray">slicer.util.addVolumeFromArray</a></p>

---
