# Weird Error but everything looks okay

**Topic ID**: 21939
**Date**: 2022-02-12
**URL**: https://discourse.slicer.org/t/weird-error-but-everything-looks-okay/21939

---

## Post #1 by @NoobForSlicer (2022-02-12 17:41 UTC)

<p>I get this error but the models and segmentations I imported look really good… Is there something wrong?</p>
<p>SetConversionParameter: Conversion parameter ‘Default slice thickness’ not found in converter rules!</p>

---

## Post #2 by @NoobForSlicer (2022-02-13 10:48 UTC)

<p>anyone? Please help?</p>
<p>What does this error even mean</p>

---

## Post #3 by @lassoan (2022-02-13 13:47 UTC)

<p>This just means that the segmentation was created with an earlier Slicer version or the <code>Default slice thickness</code> parameter is missing for some other reason.</p>
<p>The parameter may be needed for planar contour to closed surface conversion if contours are not defined for every slice.</p>
<p>Most likely you can ignore this warning.</p>

---
