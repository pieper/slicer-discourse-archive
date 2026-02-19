---
topic_id: 34573
title: "Centerline Calculation Warning Vmtkcenterlineviewer"
date: 2024-02-27
url: https://discourse.slicer.org/t/34573
---

# Centerline calculation warning (vmtkcenterlineviewer)

**Topic ID**: 34573
**Date**: 2024-02-27
**URL**: https://discourse.slicer.org/t/centerline-calculation-warning-vmtkcenterlineviewer/34573

---

## Post #1 by @MicheleIng (2024-02-27 15:50 UTC)

<p>Once I import the stl file (the stl file is a vessel that has two bifurcations), vmtk doesn’t generate centerlines for me but it generates this warning message.</p>
<blockquote>
<p>Warning: In …\vtkVmtk\ComputationalGeometry\vtkvmtkSteepestDescentLineTracer.cxx, line 240<br>
vtkvmtkSteepestDescentLineTracer (0000029D027E98B0): Degenerate descent detected. Target not reached.</p>
</blockquote>
<p>In other stl generates a partial centerline with the same message type but the number inside the parenthesis is different. For example:</p>
<p>000001EFE2DB4AB0<br>
000002D4278FF8D0</p>
<p>Can anyone explain why?</p>

---

## Post #2 by @MicheleIng (2024-03-10 18:39 UTC)

<p>code:</p>
<blockquote>
<p><em>vmtkcenterlines -ifile “C:/Users/…/…/file.stl” -endpoints 1 -ofile “C:/Users/…/…/file_CL.vtp”</em><br>
*vmtkbranchextractor -ifile  C:/Users/…/…/file_CL.vtp" -ofile “C:/Users/…/…/file_CL_split.vtp” -radiusarray MaximumInscribedSphereRadius *<br>
<em>vmtkcenterlineviewer -ifile “C:/Users/…/…/file_CL_split.vtp”  -cellarray CenterlineIds --pipe vmtkcenterlineviewer -cellarray TractIds --pipe vmtkcenterlineviewer -cellarray GroupIds --pipe vmtkcenterlineviewer -cellarray Blanking</em></p>
</blockquote>
<p>Warning:</p>
<blockquote>
<p>Warning: In …\vtkVmtk\ComputationalGeometry\vtkvmtkSteepestDescentLineTracer.cxx, line 240</p>
<p>vtkvmtkSteepestDescentLineTracer (0000019A2108A180): Degenerate descent detected. Target not reached.</p>
<p>Warning: In …\vtkVmtk\ComputationalGeometry\vtkvmtkSteepestDescentLineTracer.cxx, line 240</p>
<p>vtkvmtkSteepestDescentLineTracer (0000019A2108A180): Degenerate descent detected. Target not reached.</p>
</blockquote>

---

## Post #3 by @THartman (2024-04-09 00:24 UTC)

<p>Best I can tell, it is reading the vessel as turning too sharply, or gets too narrow at some point, though I could be incorrect in this.</p>
<p>The different strings in the errors are (as far as I can tell) memory addresses in hexadecimal.  Assuming this is the case, it is likely just something that is occuring at different points in the process based on your inputs.</p>

---

## Post #4 by @lassoan (2024-04-09 03:36 UTC)

<p>The problem is that the endpoint is not reachable from any of the starting points. It is usually due to too small vessel diameter or the points are not close enough to the centerline (note that the vessel surface can be quite far from its centerline). You can fix the error by moving the start/end point closer to the centerline.</p>

---
