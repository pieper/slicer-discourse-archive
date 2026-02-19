---
topic_id: 34001
title: "Is There A Guide For 3D Printing Anatomical Structures"
date: 2024-01-27
url: https://discourse.slicer.org/t/34001
---

# Is there a guide for 3D printing anatomical structures?

**Topic ID**: 34001
**Date**: 2024-01-27
**URL**: https://discourse.slicer.org/t/is-there-a-guide-for-3d-printing-anatomical-structures/34001

---

## Post #1 by @bcolbert (2024-01-27 17:05 UTC)

<p>I have very small structures segmented. I typically export these as ply files for analyses but i want to 3D print larger versions of these structures.</p>
<p>Assuming i have access to a printer capable of printing stl and obj files, isv there a good guide to creating print readybfiles in 3Dslicer?</p>

---

## Post #2 by @tsehrhardt (2024-01-28 19:32 UTC)

<p>You can just export STLs from 3D Slicer or convert the PLYs using something free like Meshlab or Meshmixer. Your 3D printer’s slicing software will let you scale the models before printing and many will also repair small errors that may be in your model.</p>

---
