# MarkupsToModel : should we replace SetCurveIsLoop by SetCurveIsClosed?

**Topic ID**: 14488
**Date**: 2020-11-08
**URL**: https://discourse.slicer.org/t/markupstomodel-should-we-replace-setcurveisloop-by-setcurveisclosed/14488

---

## Post #1 by @chir.set (2020-11-08 14:26 UTC)

<p>Building MarkupsToModel with Slicer/VTK9 on Linux failed (I’m aware VTK9 build is not yet ready for use).</p>
<p>gcc hinted at using SetCurveIsClosed instead of SetCurveIsLoop in MarkupsToModel/Logic/vtkSlicerMarkupsToModelLogic.cxx. After the substitution, MarkupsToModel builds and is packaged.</p>
<p>Is it the right fix?</p>
<p>Thanks.</p>

---

## Post #2 by @jamesobutler (2020-11-08 15:20 UTC)

<p>That seems correct based on recent changes made in Slicer core in <a href="https://github.com/Slicer/Slicer/commit/d51f4218cce131bbbafb9b0f3ba5ef230c87b798" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/commit/d51f4218cce131bbbafb9b0f3ba5ef230c87b798</a></p>

---

## Post #3 by @lassoan (2020-11-08 17:09 UTC)

<p>Good point. We should have just deprecated the old method name instead of immediately removing it. I’ve restored the old method names for giving more time for module/extension developers to update their code.</p>

---
