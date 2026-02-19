---
topic_id: 35320
title: "Slicer Reports Error When There Is A Decimal In The Name Of"
date: 2024-04-06
url: https://discourse.slicer.org/t/35320
---

# Slicer reports error when there is a decimal in the name of the nrrd file.

**Topic ID**: 35320
**Date**: 2024-04-06
**URL**: https://discourse.slicer.org/t/slicer-reports-error-when-there-is-a-decimal-in-the-name-of-the-nrrd-file/35320

---

## Post #1 by @kkwst2 (2024-04-06 03:43 UTC)

<p>Problem report for Slicer 5.7.0-2024-01-08 win-amd64: [please describe expected and actual behavior]</p>
<p>It does actually save the file if I unbundle them.  However, if I try to bundle it as an mrb, it seems to prevents the mrb file from saving at all.  Since the name is derived from the imported DICOM names, and most of our DICOM names have the acquired resolution as a decimal, it makes most of our projects unable to be saved automatically as an mrb.  I’m sure there’s some easy workaround to this but I haven’t figured it out yet.</p>

---

## Post #2 by @lassoan (2024-04-06 04:01 UTC)

<p>Thanks for reporting. I would recommend to upgrade to recent Slicer Preview Release, as this seems to have been already fixed there (see <a href="https://github.com/Slicer/Slicer/commit/a70999314022f47e01e014b544edcb7102d19991" class="inline-onebox">BUG: Fixed saving of NRRD files of certain filenames · Slicer/Slicer@a709993 · GitHub</a>).</p>

---
