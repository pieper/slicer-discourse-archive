# How to divide a volume with another volume

**Topic ID**: 32952
**Date**: 2023-11-22
**URL**: https://discourse.slicer.org/t/how-to-divide-a-volume-with-another-volume/32952

---

## Post #1 by @hu_nathan (2023-11-22 12:07 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 5.2.2</p>
<p>Hi there,</p>
<p>I am trying to divide one dose volume with another.<br>
Using the filtering → arithmetic function, I am able to add, subtract and multiply but cannot divide.<br>
Any help would be greatly appreciated.<br>
Many thanks,</p>

---

## Post #2 by @lassoan (2023-11-22 12:10 UTC)

<p>You can easily combine voxels of two volumes that have the same geometry (origin, spacing, axis directions, and extents) using numpy. See complete example in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#combine-multiple-volumes-into-one">script repository</a>.</p>

---

## Post #3 by @hu_nathan (2023-11-27 04:46 UTC)

<p>Thank you very much for your quick response.<br>
Greatly appreciate it.</p>

---
