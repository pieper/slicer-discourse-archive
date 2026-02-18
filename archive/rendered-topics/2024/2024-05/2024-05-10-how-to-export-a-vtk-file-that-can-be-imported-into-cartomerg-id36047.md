# How to export a vtk file that can be imported into CARTOMerge

**Topic ID**: 36047
**Date**: 2024-05-10
**URL**: https://discourse.slicer.org/t/how-to-export-a-vtk-file-that-can-be-imported-into-cartomerge/36047

---

## Post #1 by @kasun (2024-05-10 05:15 UTC)

<p>Hi I was wondering if I could get some help with a project. I have a 3D vtk file that I can open on 3D Slicer. I am trying to import this into Carto V6 as a CARTOMERGE file which I can then co-register with the EAM (same as I would an ADAS 3D or InHeart vtk) but when I try and import it I get the following error “Invalid images, image study was not created.” Is there a particular way to export the file in a vtk format that is readable by Carto V6 cartomerge?</p>

---

## Post #2 by @lassoan (2024-05-10 05:16 UTC)

<p>You can use CartoExport module in <a href="https://github.com/SlicerHeart/SlicerHeart">SlicerHeart extension</a>.</p>

---
