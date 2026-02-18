# Segment Mesher Module in Slicer 5.0.3

**Topic ID**: 24731
**Date**: 2022-08-12
**URL**: https://discourse.slicer.org/t/segment-mesher-module-in-slicer-5-0-3/24731

---

## Post #1 by @F.A (2022-08-12 18:44 UTC)

<p>Hi,<br>
I was using “Segment Mesher” module in slicer 4.13 to get the volumetric mesh with the capability of extracting material properties using “Prob Volume with Model”, but I can’t find it in Slicer 5.0.3. I appreciate your help.<br>
Thanks</p>

---

## Post #2 by @pieper (2022-08-12 19:10 UTC)

<p>The <a href="https://slicer.cdash.org/index.php?project=SlicerStable">dashboard</a> says SegmentMesher is building fine for windows and linux.  Maybe you need to install the extension.</p>

---

## Post #3 by @F.A (2022-08-12 19:25 UTC)

<p>I’ve already installed the extension for previous versions and in Slicer4.13, it works.<br>
Moreover, after creating volume meshes, I was using<br>
slicer.util.arrayFromModelPointData(“my nodes”, ‘NRRDImage’) to get the HU of each node, but now it contains just 0 and 1.</p>

---
