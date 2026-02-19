---
topic_id: 12324
title: "Slow Dicom Import"
date: 2020-07-01
url: https://discourse.slicer.org/t/12324
---

# Slow DICOM import

**Topic ID**: 12324
**Date**: 2020-07-01
**URL**: https://discourse.slicer.org/t/slow-dicom-import/12324

---

## Post #1 by @IMF-Slicer (2020-07-01 17:12 UTC)

<p>Hello. I’ve read several prior posts about slow DICOM imports, but don’t see a consistent answer, so thanks for letting me ask the question again.<br>
I export a standard CT scan from MIM, about 90 slices, which seems to work fine.<br>
Importing it into Slicer takes about 5 minutes for the 90 slices, which is pretty slow. I’ve tried importing scans of a few hundred slices and it takes a long time.<br>
Do we know why this is happening? Thanks,<br>
IMF</p>

---

## Post #2 by @lassoan (2020-07-01 17:13 UTC)

<p>Please try how long the import takes if you use latest Slicer Preview Release.</p>

---

## Post #3 by @pieper (2020-07-01 21:54 UTC)

<p>Also confirm that you are using the DICOM module and not the Add Data.  A common mistake is to end up loading 90 copies of the same volume by mistake.  If you are still seeing an issue with the latest preview, then please compare with performance against public data and let us know how your data is different (or share it if you can).</p>

---
