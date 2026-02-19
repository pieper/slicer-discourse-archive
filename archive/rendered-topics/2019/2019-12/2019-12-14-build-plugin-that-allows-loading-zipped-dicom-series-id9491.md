---
topic_id: 9491
title: "Build Plugin That Allows Loading Zipped Dicom Series"
date: 2019-12-14
url: https://discourse.slicer.org/t/9491
---

# build plugin that allows loading zipped dicom series

**Topic ID**: 9491
**Date**: 2019-12-14
**URL**: https://discourse.slicer.org/t/build-plugin-that-allows-loading-zipped-dicom-series/9491

---

## Post #1 by @jpcenteno80 (2019-12-14 01:34 UTC)

<p>Operating system: Ubuntu 18.04<br>
Slicer version: 4.10.2<br>
Desired behavior: Allow loading dicom directly from a zipped file containing a dicom series. “Add data into the scene” already allows it but the slices can only be viewed individually, not as a volume that can be scrolled.</p>
<p>Do you have some suggestions as to how to get started?</p>

---

## Post #2 by @lassoan (2020-01-15 02:47 UTC)

<p>It would be certainly nice to have this. There have been some <a href="https://discourse.slicer.org/t/proposition-name-volumes-imported-via-data-by-series-description/9779/8">related discussions recently</a> about simplifying DICOM loading (less clicks, avoid the need of cleaning up the database). Maybe after this we can have a look this as a second step.</p>
<p>If you want to get started with it on your own then have a look at the logic in qSlicerDataDialog. It would be nice to modify the zip file to work similarly as general drag-and-drop. That way you could define custom handler, similar to the handler for DICOM data loading (see <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOM/DICOM.py#L321-L392">here</a>).</p>

---
