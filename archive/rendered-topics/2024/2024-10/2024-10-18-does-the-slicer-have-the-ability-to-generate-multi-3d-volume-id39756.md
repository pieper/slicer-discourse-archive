# Does the slicer have the ability to generate multi 3D volumes within the 3D slicer and operate it under specific limitations?

**Topic ID**: 39756
**Date**: 2024-10-18
**URL**: https://discourse.slicer.org/t/does-the-slicer-have-the-ability-to-generate-multi-3d-volumes-within-the-3d-slicer-and-operate-it-under-specific-limitations/39756

---

## Post #1 by @Ming_Lei (2024-10-18 18:21 UTC)

<p>I’m working on an extension that requests that numerous 3D volumes be loaded or created and then moved toward MRI and CT volumes according to particular regulations. Because I need to record the transformation results in a matrix. I have two options for doing it right now. One, use SolidWorks to produce the 3D model and then import it into 3D Slicer, or use VTK to create it and then manage it.  As a result, I wanted to know which approach 3D Slicer could use.</p>

---

## Post #2 by @lassoan (2024-10-18 18:23 UTC)

<p>Yes, Slicer can work with any number of 3D volumes (limited only by the amount of memory and disk space you have).</p>
<p>3D Slicer includes VTK, so if you need to use VTK then you can run the Python script in Slicer’s Python interpreter or create a Python or C++ Slicer module.</p>

---
