# Pick and Paint SyntaxError

**Topic ID**: 10924
**Date**: 2020-03-31
**URL**: https://discourse.slicer.org/t/pick-and-paint-syntaxerror/10924

---

## Post #1 by @Maila_Portes (2020-03-31 00:14 UTC)

<p>Operating system: win10<br>
Slicer version: 4.10.2<br>
Expected behavior:<br>
Actual behavior:<br>
I´ve installed the extesion PickAndPaint but this error message appears<br>
File “C:/Users/myuser/AppData/Roaming/NA-MIC/Extensions-28257/PickAndPaintExtension/lib/Slicer-4.10/qt-scripted-modules/PickAndPaint.py”, line 569<br>
landmarks.SetAttribute(“arrayName”, f’{model.GetName()}_{landmarks.GetName()}_ROI’)<br>
^<br>
SyntaxError: invalid syntax</p>

---

## Post #2 by @lassoan (2020-03-31 03:07 UTC)

<p>Pick and Paint extension was updated to be compatible with Slicer-4.11 and these changes were not compatible with Slicer-4.10 anymore. I’ve now updated the extension index to use the old version for Slicer-4.10 and the current version for Slicer-4.11.</p>
<p>You can use Pick and Paint extension in Slicer-4.11 now. If you reinstall Pick and Paint extension in Slicer-4.10 tomorrow then it should work, too.</p>

---
