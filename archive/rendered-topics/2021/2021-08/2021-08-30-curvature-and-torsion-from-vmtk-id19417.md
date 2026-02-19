---
topic_id: 19417
title: "Curvature And Torsion From Vmtk"
date: 2021-08-30
url: https://discourse.slicer.org/t/19417
---

# Curvature and Torsion from VMTK

**Topic ID**: 19417
**Date**: 2021-08-30
**URL**: https://discourse.slicer.org/t/curvature-and-torsion-from-vmtk/19417

---

## Post #1 by @Ge_Tang (2021-08-30 21:07 UTC)

<p>Hi,<br>
I have problems reading the code from the VMTK source code.<br>
I am not sure if the curvature, torsion from the centerline property are calculated by averaging (<a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/e01c4fea8e67d45c646f7c66a1183063dd06bcbb/ExtractCenterline/ExtractCenterline.py#L888" class="inline-onebox" rel="noopener nofollow ugc">SlicerExtension-VMTK/ExtractCenterline.py at e01c4fea8e67d45c646f7c66a1183063dd06bcbb · vmtk/SlicerExtension-VMTK · GitHub</a>)? If so, since torsion has negative values, did they use the absolute value for averaging?<br>
I also checked the code for the network property. It seems the curvature and torsion are the averages of all the points (<a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/e01c4fea8e67d45c646f7c66a1183063dd06bcbb/ExtractCenterline/ExtractCenterline.py#L1028" class="inline-onebox" rel="noopener nofollow ugc">SlicerExtension-VMTK/ExtractCenterline.py at e01c4fea8e67d45c646f7c66a1183063dd06bcbb · vmtk/SlicerExtension-VMTK · GitHub</a>). How does the VMTK deal with torsion? Thank you for your help!<br>
best,<br>
Ge</p>

---
