# Missing option "Use mean as template"

**Topic ID**: 1164
**Date**: 2017-10-03
**URL**: https://discourse.slicer.org/t/missing-option-use-mean-as-template/1164

---

## Post #1 by @Olof (2017-10-03 13:11 UTC)

<p>Hi Beatriz,</p>
<p>working furhter with Spharm in Slicer-salt I realise there is two thing that was available before that I cannot find now.</p>
<ol>
<li>Use mean as template,</li>
<li>The possibility to cancel a run when it is started. The only way to cancel now … seems to be to close the program?</li>
</ol>
<p>Are these functions not available?</p>

---

## Post #2 by @laurapascal (2017-10-03 21:37 UTC)

<p>Hi Olof,</p>
<ol>
<li>You are right, this option is not available anymore in the new version of SPHARM-PDM. You could run SPHARM-PDM on your first case, and then run it on all your cases by putting the <em>inputRootname_pp_surf_SPHARM.vtk</em> model, generated during your first run, as your registration template.</li>
<li>Normally to cancel SPHARM-PDM, after clicking on the “Run ShapeAnalysisModule” button, you should be able to cancel it by clicking on the same button (which was transformed from “Run ShapeAnalysisModule” to “Cancel”). Let me know if the button don’t work or if you can’t cancel the run.</li>
</ol>

---
