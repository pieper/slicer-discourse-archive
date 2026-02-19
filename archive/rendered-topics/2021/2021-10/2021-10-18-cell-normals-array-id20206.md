---
topic_id: 20206
title: "Cell Normals Array"
date: 2021-10-18
url: https://discourse.slicer.org/t/20206
---

# Cell Normals Array

**Topic ID**: 20206
**Date**: 2021-10-18
**URL**: https://discourse.slicer.org/t/cell-normals-array/20206

---

## Post #1 by @adamy (2021-10-18 16:01 UTC)

<p>The surface models module creates point normals by default. How can I create an array containing normals of all of the cells (not point normals)?</p>

---

## Post #2 by @mau_igna_06 (2021-10-18 16:20 UTC)

<p>Use the normals filter with this option:<br>
<a href="https://vtk.org/doc/nightly/html/classvtkPolyDataNormals.html#a4c27b2bfa1f4924ada7cffccf5aae643" class="onebox" target="_blank" rel="noopener nofollow ugc">https://vtk.org/doc/nightly/html/classvtkPolyDataNormals.html#a4c27b2bfa1f4924ada7cffccf5aae643</a></p>
<p>Search on the forum (or on google) how to calculate normals if you don’t know how to use this filter. I’m sure there are examples</p>

---
