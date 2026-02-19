---
topic_id: 20265
title: "Import External Segmentation Map"
date: 2021-10-20
url: https://discourse.slicer.org/t/20265
---

# Import external segmentation map

**Topic ID**: 20265
**Date**: 2021-10-20
**URL**: https://discourse.slicer.org/t/import-external-segmentation-map/20265

---

## Post #1 by @Han_Liu (2021-10-20 15:09 UTC)

<p>Hi all,</p>
<p>I am working on a deep learning project where the network generates a semantically segmented mask from .dcm CT input. For instance, if I want to separate out the kidneys, with the input being a 200x512x512 3D array, the output would be a 3D array of the same shape and all the voxel of the kidneys would be labelled 1 and everything else would be labelled 0 in that array.</p>
<p>The problem that I am having is that when I import this .seg.nrrd mask into Slicer, the mask doesn’t overlap on top of the original CT scan. It seems to have been shifted and truncated in the depth dimension as well. Does anyone have experience with this? Any pointers would be greatly appreciated. Thanks in advance.</p>

---

## Post #2 by @lassoan (2021-10-20 15:11 UTC)

<p>How do you compute the origin, spacing, axis directions, and extent of the .seg.nrrd file that you generate?</p>

---

## Post #3 by @Han_Liu (2021-10-20 18:16 UTC)

<p>Hi,<br>
I just save the numpy matrix using nrrd.write(). Is there a Python package with which I can specify these attributes when saving?</p>

---

## Post #4 by @lassoan (2021-10-20 18:32 UTC)

<p>You need to <a href="https://pynrrd.readthedocs.io/en/latest/user-guide.html#writing-nrrd-files">specify the correct origin, spacing, and axis directions</a> by setting the <code>space origin</code> and <code>space directions</code> fields. You can load a nrrd file using pynrrd to see how exactly these fields are stored in Python.</p>

---
