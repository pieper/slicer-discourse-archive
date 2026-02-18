# Define field of view

**Topic ID**: 12933
**Date**: 2020-08-10
**URL**: https://discourse.slicer.org/t/define-field-of-view/12933

---

## Post #1 by @jj31 (2020-08-10 18:43 UTC)

<p>Hello,</p>
<p>I developed a small simple module to open a VTK/VTU file and perform a series of calculations. Every time I open the file, I need to manually adjust the field of view (zoom and move to the center of the window viewer) for each of the red/yellow/green slice viewers. Is there a way (code) so that the views are automatically adjusted?</p>
<p>Thanks,<br>
JJ</p>

---

## Post #2 by @pieper (2020-08-10 18:56 UTC)

<p>Hi - yes, just search the source code for <code>FitSliceToAll</code>.  There are some variants and options.</p>

---

## Post #3 by @lassoan (2020-08-10 19:08 UTC)

<p>See also this example: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Center_the_3D_View_on_the_Scene">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Center_the_3D_View_on_the_Scene</a></p>

---
