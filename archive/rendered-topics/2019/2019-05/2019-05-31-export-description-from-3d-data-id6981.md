# Export description from 3d data

**Topic ID**: 6981
**Date**: 2019-05-31
**URL**: https://discourse.slicer.org/t/export-description-from-3d-data/6981

---

## Post #1 by @safa (2019-05-31 10:25 UTC)

<p>how can I export a description of 3D data (information about this data) in a txt file or binary file ,…?</p>

---

## Post #2 by @lassoan (2019-05-31 10:47 UTC)

<p>Most file formats have some kind of header that store description and you can often add custom fields. What would you like to do exactly?</p>

---

## Post #3 by @safa (2019-05-31 11:41 UTC)

<p>i need matrix presentation<br>
can i export description  as an matrix presentation?</p>

---

## Post #4 by @lassoan (2019-05-31 12:14 UTC)

<p>What do you mean by “matrix representation”? Volume IJK to RAS (or LPS) matrix is already saved in volume files.</p>

---

## Post #6 by @safa (2019-05-31 13:13 UTC)

<p>apart from the image that I’m going to save, I need a descriptive file on this image (txt file , matrix representation, json, …) how can i do this ?<br>
any type of file where i found values</p>

---

## Post #7 by @lassoan (2019-05-31 13:17 UTC)

<p>If you prefer not to store metadata inside your data file then it is even simpler. You can use standard Python commands to write this additional file with any content you need.</p>

---
