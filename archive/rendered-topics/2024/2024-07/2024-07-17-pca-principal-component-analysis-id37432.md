# PCA Principal component analysis

**Topic ID**: 37432
**Date**: 2024-07-17
**URL**: https://discourse.slicer.org/t/pca-principal-component-analysis/37432

---

## Post #1 by @Dani98 (2024-07-17 16:12 UTC)

<p>How can I understand the deviation standard of the principal component analysis based on the chosen scaling factors?</p>

---

## Post #2 by @muratmaga (2024-07-17 16:27 UTC)

<p>When you are posting questions, please do indicate which module/extension you are referring to. Otherwise PCA is a generic statistical tool, which multiple modules use for different reasons.</p>
<p>I assume you are asking this in context of SlicerMorph’s GPA module. If that’s the case the answer is, they are not in the units of SD. PC visualization scaling factor are in the same direction of the corresponding eigenvector, but they are arbitrarily scaled to create a visual effect in 3D.</p>

---
