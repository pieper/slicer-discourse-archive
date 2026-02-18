# Convert .PTS landmarks coordinates in .fcsv or .LPS format

**Topic ID**: 37303
**Date**: 2024-07-10
**URL**: https://discourse.slicer.org/t/convert-pts-landmarks-coordinates-in-fcsv-or-lps-format/37303

---

## Post #1 by @ATroyelli (2024-07-10 13:53 UTC)

<p>Hi!</p>
<p>Is it possible to transform a file of .PTS landmark coordinates into .fcsv or .LPS/.RAS format? I have landmarks coordinated in .TPS to use as templates in ALPACA.</p>
<p>Thank you very much in advance</p>
<p>Adrian</p>
<p>Operating system: Windows 10 (x64)<br>
Slicer version: 5.6.2<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @muratmaga (2024-07-10 15:28 UTC)

<p>There is nothing that will automatically do this in Slicer. You can of course develop a python script to do that.</p>
<p>If you are using R, I think geomorph reads TPS files, and you can then use SlicerMorphR to write them as fcsv. Although I highly encourage you switch to JSON (both functions are available in SlicerMorph write.markups.fcsv, or write.markups.json)</p>

---

## Post #3 by @ATroyelli (2024-07-10 21:29 UTC)

<p>Thank you very much! Anyway, I ´ll try to develop an algorithm to obtain this trasnformation</p>

---

## Post #4 by @muratmaga (2024-07-10 21:40 UTC)

<p>If you know the PTS format, this should be simple. Read the landmark coordinates as a numpy array, and write them as a mrk.json one specimen at a time. For a basic mrk.json example see with 3 landmarks:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/markups.html#markups-json-file-format-mrk-json" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/modules/markups.html#markups-json-file-format-mrk-json</a></p>

---

## Post #5 by @ATroyelli (2024-07-18 19:05 UTC)

<p>Great!. I´ll try that.</p>
<p>Thank you so much!</p>

---
