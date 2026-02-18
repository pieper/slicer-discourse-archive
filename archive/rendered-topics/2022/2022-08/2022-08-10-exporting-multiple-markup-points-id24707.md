# Exporting multiple markup points

**Topic ID**: 24707
**Date**: 2022-08-10
**URL**: https://discourse.slicer.org/t/exporting-multiple-markup-points/24707

---

## Post #1 by @AMK (2022-08-10 09:01 UTC)

<p>Hi,</p>
<p>I am trying to export multiple markup points from my slicer window to an excel sheet. I tried to use the script provided in the script repository.</p>
<p>markupsNode = slicer.util.getNode(‘F’)<br>
slicer.modules.markups.logic().ExportControlPointsToCSV(markupsNode, “/path/to/MyControlPoints.csv”)</p>
<p>But it (quite understandably) only exports the last point, as on each step it overrides the previous point.  How can I export multiple points using “python interactor”?</p>

---
