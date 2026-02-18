# How to cite individual modules in 3D Slicer

**Topic ID**: 12354
**Date**: 2020-07-03
**URL**: https://discourse.slicer.org/t/how-to-cite-individual-modules-in-3d-slicer/12354

---

## Post #1 by @Saima (2020-07-03 12:02 UTC)

<p>How to cite individual modules like model maker and threshold filters.</p>
<p>Please guide in this.</p>

---

## Post #2 by @pieper (2020-07-03 18:05 UTC)

<p>It depends a bit on your goal.  For scientific reproducibility it is important to document the exact version of the software and how you use it together with any other details you might reasonably imagine someone would need to know.</p>
<p>For allocating academic credit, it’s enough to <a href="https://www.slicer.org/wiki/CitingSlicer">cite the overall project</a>.  If you use an extension, you might find extra citation requests.</p>
<p>If you are citing in order to help readers learn more about your process, then it’s probably worth looking at the implementation and providing citations to the original algorithms and describing how you make use of them.  E.g. for <code>Model Maker</code> you might cite Lorensen and Cline and for <code>Threshold</code> you might cite Otsu.</p>

---
