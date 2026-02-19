---
topic_id: 7005
title: "Segmentation Export Nrrd Data Open Python"
date: 2019-06-03
url: https://discourse.slicer.org/t/7005
---

# Segmentation(export nrrd) Data Open python

**Topic ID**: 7005
**Date**: 2019-06-03
**URL**: https://discourse.slicer.org/t/segmentation-export-nrrd-data-open-python/7005

---

## Post #1 by @kscript (2019-06-03 10:31 UTC)

<p>Hi<br>
I segmented using 3D Slicer and saved it with the nrrd extension.<br>
I opened this saved data in Python and I get the following error:<br>
Algorithm vtkNrrdReader returned failure for request:<br>
I did not have a problem because I saved the dicom file as nrrd and open it in Python.<br>
How can I solve this?</p>

---

## Post #2 by @lassoan (2019-06-03 14:10 UTC)

<p>By default, segmentation is saved into a 4D nrrd file (to allow saving overlapping segments). If you nrrd reader cannot cope with that and your segments do not overlap then you can <a href="https://discourse.slicer.org/t/get-label-map-node-from-segmentation-node/1137">export the segmentation to labelmap</a> and save that to nrrd file (that will be a simple 3D volume).</p>

---

## Post #4 by @kscript (2019-06-04 01:53 UTC)

<p>Oh i solve using your advice!</p>
<p>really Thanks!!</p>

---
