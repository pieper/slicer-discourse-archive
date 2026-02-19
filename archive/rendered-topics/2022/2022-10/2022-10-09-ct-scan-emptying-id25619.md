---
topic_id: 25619
title: "Ct Scan Emptying"
date: 2022-10-09
url: https://discourse.slicer.org/t/25619
---

# CT scan emptying

**Topic ID**: 25619
**Date**: 2022-10-09
**URL**: https://discourse.slicer.org/t/ct-scan-emptying/25619

---

## Post #1 by @ermellina_di_bagno (2022-10-09 15:36 UTC)

<p>Operating system: MAC OS MOJAVE<br>
Slicer version: 4.11.2<br>
Expected behavior:<br>
Actual behavior:I uploaded a CT scan of a brown bear skull. the CT scan contains only the bone tissues and I need to keep only the external surface of the skull and eliminate all internal contents. how can I do? after loading the dicom I created a segment in the segment editor and used the threshold to give it an appropriate representation but in doing so the internal contents were also reproduced.</p>

---

## Post #2 by @mau_igna_06 (2022-10-09 20:35 UTC)

<p>Please install the <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify#readme" rel="noopener nofollow ugc">WrapSolidify</a> effect for the segment editor from the extension manager and try to use it.</p>

---
