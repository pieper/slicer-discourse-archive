# Validity of the 3D slicer software

**Topic ID**: 3341
**Date**: 2018-06-29
**URL**: https://discourse.slicer.org/t/validity-of-the-3d-slicer-software/3341

---

## Post #1 by @Mohamed1982 (2018-06-29 21:40 UTC)

<p>Hi</p>
<p>I have a project about the 3D slicer software in the assessment of the olfactory bulb volume,<br>
but I want to ask if there is any article for the validation of this software and if there are studies comparing results of 3D slicer software method with conventional manual planimetric countouring.</p>
<p>Thanks in advance</p>

---

## Post #2 by @lassoan (2018-06-30 13:38 UTC)

<p>We are not aware of any specific issue that would make volume or surface computation of segmented structures incorrect.</p>
<p>However, it is always recommended to validate your complete analysis workflow against your specific requirements. Errors may be introduced in data preparation steps (e.g., incorrectly implemented DICOM anonymization, corrupt/missing file during copying many files) and there is always a chance that due to special properties of your data or processing methods that you choose you run into unexpected errors (e.g., you resample your data on a very coarse grid, apply very strong surface smoothing,…).</p>

---
