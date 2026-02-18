# Save data as ASCII

**Topic ID**: 5623
**Date**: 2019-02-03
**URL**: https://discourse.slicer.org/t/save-data-as-ascii/5623

---

## Post #1 by @Hamburgerfinger (2019-02-03 04:48 UTC)

<p>Is there an option to save data as ASCII instead of binary?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2019-02-03 05:13 UTC)

<p>You can get the voxel data as numpy array and write that to a text file. But it would terribly inefficient, van be 10-100x slower read/write than binary.</p>

---

## Post #3 by @timeanddoctor (2019-06-28 07:04 UTC)

<p>Thanks, professor Lassoan. Is there any python code for numpy to read a stl file in 3d slicer?</p>

---

## Post #4 by @lassoan (2019-06-28 15:45 UTC)

<p>You can load STL file using <code>slicer.util.loadModel()</code> and then get point coordinates or scalar values as numpy array by calling <code>slicer.util.arrayFromModelPoints()</code> and <code>slicer.util.arrayFromModelPointData()</code>.</p>

---
