---
topic_id: 16044
title: "Generaeoverlayimages In Cip Not Working"
date: 2021-02-17
url: https://discourse.slicer.org/t/16044
---

# GeneraeOverlayImages in CIP not working

**Topic ID**: 16044
**Date**: 2021-02-17
**URL**: https://discourse.slicer.org/t/generaeoverlayimages-in-cip-not-working/16044

---

## Post #1 by @akshay_pillai (2021-02-17 22:01 UTC)

<p>Operating system: Windows<br>
Slicer version:4.11<br>
Expected behavior:<br>
Actual behavior:<br>
I’m trying to use Generate Overlay Images cip script in my ubuntu terminal using the CLI command-line tools. Can anyone tell me how to use GenerateOverlayImages in the terminal, I already looked at the help document. I also tried the CIP module in slicer and used generateoverlayimages in the utils module but when I click apply ith just keeps running and doesnt stop. Any tips?</p>

---

## Post #2 by @akshay_pillai (2021-02-17 23:39 UTC)

<p>Same with read dicom write tags (ReadDicomWriteTags). Can someone tell me how to use it in cli like a for example cli line for both GenerateOverlayImages and ReadDicomWriteTags.<br>
This is what I’m using now:<br>
1&gt;GenerateOverlayImages --all --prefix “ILD_303_0verlay” -c cipwd/project/caseID/ct  -l cipwd/project/caseID/lmap.nrrd (keeps running)<br>
2&gt;ReadDicomWriteTags -r /root/Scans/case/* -s 9 -o /root/project/caseID/output.csv</p>

---
