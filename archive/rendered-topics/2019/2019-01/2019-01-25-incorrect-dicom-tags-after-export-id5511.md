---
topic_id: 5511
title: "Incorrect Dicom Tags After Export"
date: 2019-01-25
url: https://discourse.slicer.org/t/5511
---

# Incorrect DICOM tags after export

**Topic ID**: 5511
**Date**: 2019-01-25
**URL**: https://discourse.slicer.org/t/incorrect-dicom-tags-after-export/5511

---

## Post #1 by @samuelholly (2019-01-25 14:05 UTC)

<p>Operating system: Win 7<br>
Slicer version: 4.8.1<br>
Expected behavior:<br>
Actual behavior: When I export a volume to DICOM as a series, even though the export dialog table list correct DICOM tag values inferred from the parent study, the resulting DICOM files have incorrect tag values for the Study Time (0008,0030) and Patient Birth Date (0010,0030) tags.</p>
<p>Do you have any suggestion?</p>
<p>Many thanks in advance</p>
<p><em>Samuel Holly</em><br>
<em>Imaging Physicist</em><br>
<em>Jessenius Diagnostic Centre</em><br>
<em>Spitalska 6</em><br>
<em>94911 Nitra</em><br>
<em>Slovakia</em></p>

---

## Post #2 by @pieper (2019-01-25 14:17 UTC)

<p>Could you try version 4.10.1 (just released) and confirm if it’s still an issue?</p>

---
