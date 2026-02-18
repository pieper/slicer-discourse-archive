# Extract connected components from polydata structures

**Topic ID**: 12673
**Date**: 2020-07-22
**URL**: https://discourse.slicer.org/t/extract-connected-components-from-polydata-structures/12673

---

## Post #1 by @loubna (2020-07-22 09:33 UTC)

<p>Hi;</p>
<p>Is there any way to extract connected components from a set of planar contours (polydata)?</p>
<p>As shown in attached figure, I have two structures and I want to extract each of them as one component.</p>
<p>I have found this filter vtkPolydataConnectivityFilter, but it seems like it works on meshes.</p>
<p>Thank’s in advance</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/80b256288f21c8e9f485344432f2dd628c392e9f.png" alt="components" data-base62-sha1="imvcqPhS7HVklpyViEhvatyLwNV" width="220" height="274"></p>

---

## Post #2 by @lassoan (2020-07-22 14:18 UTC)

<p>Polydata = surface mesh, so vtkPolydataConnectivityFilter is the right filter to use. Of course you need to connect the planar contours to form closed surfaces.</p>

---
