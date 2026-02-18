# Unable to add DICOM data

**Topic ID**: 46156
**Date**: 2026-02-14
**URL**: https://discourse.slicer.org/t/unable-to-add-dicom-data/46156

---

## Post #1 by @Akash_Raj_G_P (2026-02-14 04:24 UTC)

<p>When I click on the ‘Add DICOM data’ button on the homepage I get an error message that says ‘Unfortunately this requested module is not available in this Slicer session‘. I have not seen this error occur for anybody else, and I’m working on a Macbook Air. I don’t have a DICOM data option in the Welcome to Slicer drop-down menu either. I have installed the DCMQI and DICOMwebbrowser extensions although I don’t think that should matter. Everybody I work with followed the same instructions, so I believe it is either an installation/laptop hardware issue. How can I resolve this?</p>

---

## Post #2 by @lassoan (2026-02-14 04:49 UTC)

<p>It means that Python is not available, most likely because there was an error during application startup. You can get a hint about what module or extension causes it in the application log (the first error message is the most relevant, all the subsequent ones may be a consequence of the first one).</p>

---

## Post #3 by @pieper (2026-02-14 15:38 UTC)

<p>Or if you built from source on mac silicon using the current draft dicom support is currently broken.  I’m sure it’s fixable but nobody has has a chance to look into it yet.</p>
<p>For now, use the standard x86 builds on mac silicon. They work fine.</p>

---
