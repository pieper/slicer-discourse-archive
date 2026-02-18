# SlicerMarkupsToModel does not build : since Slicer commit 997de030a6

**Topic ID**: 10402
**Date**: 2020-02-23
**URL**: https://discourse.slicer.org/t/slicermarkupstomodel-does-not-build-since-slicer-commit-997de030a6/10402

---

## Post #1 by @chir.set (2020-02-23 10:12 UTC)

<p>Since Slicer commit 997de030a6cd340b9f389c5bf54e8cacb55ddced, SlicerMarkupsToModel fails to build on Linux with missing curveGenerator-&gt;SetInputPoints and curveGenerator-&gt;GetOutputPoints. These are indeed discarded in this commit.</p>
<p>FYI.</p>
<p>Hopefully, SlicerMarkupsToModel update may follow.</p>
<p>Regards.</p>

---

## Post #2 by @lassoan (2020-02-23 15:15 UTC)

<p>Thanks for reporting this. We have made the curve generator a real VTK filter and it seems that we were not careful enough to keep the API fully backward compatible. We’ll fix this soon. <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> can you have a look?</p>

---

## Post #3 by @Sunderlandkyl (2020-02-23 15:31 UTC)

<p>Sure. Is the fix to make the input port optional and re-add the old methods, or just update MarkupsToModel?</p>

---

## Post #4 by @lassoan (2020-02-23 16:59 UTC)

<p>Adding back the methods (that call SetInputData and GetOutput internally, maybe also Update) should work.</p>

---

## Post #5 by @Sunderlandkyl (2020-02-25 17:38 UTC)

<p>MarkupsToModel is now building again in the latest nightly preview.</p>

---

## Post #6 by @chir.set (2020-02-25 19:25 UTC)

<p>Yes, it builds and works. Thanks.</p>

---
