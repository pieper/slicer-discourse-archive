# Renaming fiducial control points in the slice view window

**Topic ID**: 24922
**Date**: 2022-08-25
**URL**: https://discourse.slicer.org/t/renaming-fiducial-control-points-in-the-slice-view-window/24922

---

## Post #1 by @AMK (2022-08-25 14:12 UTC)

<p>Hi,</p>
<p>I am trying to automate the naming of the fiducial control points in the slice view window. The user selects the markup points. Now, I am able to rename the points in the data module. But the name remains the same in the slice window. I am aware that I can rename the points in the slice window by right clicking the repective fiducial point and then selecting the “rename the control point…” option. But I can’t find a way to automate this process. Any help is appreciated.</p>

---

## Post #2 by @AMK (2022-08-26 21:08 UTC)

<p>Hi,</p>
<p>I have been able to move forward with the problem. The following line of code helps in renaming the point.</p>
<p>slicer.modules.markups.logic().RenameAllMarkupsFromCurrentFormat(slicer.mrmlScene.GetFirstNodeByName(“PSIS_L”))</p>
<p>ALthough it renames the point, but it also adds a suffix to it. For example, I wanted the name to be ‘PSIS_L’, but it renames it to ‘PSIS_L-0’.</p>
<p>Does any one knows how I can use the Slicer functionality to rename it exactly as desired.</p>

---
