# ShapeAnalysisModule

**Topic ID**: 1869
**Date**: 2018-01-18
**URL**: https://discourse.slicer.org/t/shapeanalysismodule/1869

---

## Post #1 by @bpaniagua (2018-01-18 15:21 UTC)

<p>Dear Beatriz,  I enjoyed using the Slicer application to analyse hippocampal shapes in TLE patients. However, in a few subjects the ShapeAnalysisModule was not working  (5 out of 222 subjects). The files either fail or the Slicer application will keep on running for hours without generating any results. Does it happen more often that certain hippocampi cannot be processed? Could you possibly take a look at those segmentations?  Kind regards,  Tjardo Postma</p>

---

## Post #2 by @bpaniagua (2018-01-18 15:22 UTC)

<p>Hi Tjardo,</p>
<p>Thank you for your question. My first advice is to check for topology issues on your input segmentations.<br>
Check for the presence of holes, or “almost-holes” on those 5 patients.</p>
<p>ShapeAnalysisModule works only on objects that have spherical topology.</p>
<p>Thank you,<br>
Bea</p>

---
