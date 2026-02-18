# Issue with the Hollow command when exported in GMSH

**Topic ID**: 14121
**Date**: 2020-10-18
**URL**: https://discourse.slicer.org/t/issue-with-the-hollow-command-when-exported-in-gmsh/14121

---

## Post #1 by @nmirzaei (2020-10-18 19:10 UTC)

<p>Hi,</p>
<p>I have an issue when I want to re-mesh a hollowed out colon section with GMSH. I used the hollow button in Slicer and it created a hollowed colon section with two boundary surfaces. I need to save this as .stl with two separate surfaces so that GMSH can create a volume in between them. Is there an easy way to do this?</p>
<p>Best,</p>

---

## Post #2 by @lassoan (2020-10-18 19:14 UTC)

<p>If you need the internal and external surface separately then you can use Dynamic Modeler module to cut off all vessel endpoints (and keep the internal or external surface only). You may also create a volumetric mesh directly, using SegmentMesher extension.</p>

---
