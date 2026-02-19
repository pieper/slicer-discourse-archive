---
topic_id: 9732
title: "German Umlaut In Nii File Names"
date: 2020-01-08
url: https://discourse.slicer.org/t/9732
---

# german umlaut in .nii file names

**Topic ID**: 9732
**Date**: 2020-01-08
**URL**: https://discourse.slicer.org/t/german-umlaut-in-nii-file-names/9732

---

## Post #1 by @tsinesh (2020-01-08 01:34 UTC)

<p>Problem report for Slicer 4.11.0-2019-12-06 win-amd64: [please describe expected and actual behavior]</p>
<p>If a file name contain german umlaute (e.g. fred_lütte.nii) the “load data” =&gt; “choose filet o add”  function can not load or show the file.</p>
<p>the log contain:</p>
<p>vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file C:/Users/noname/Documents/tmp/fred_lütte.nii.nii does not exist.</p>
<p>Algorithm vtkITKArchetypeDiffusionTensorImageReaderFile(00000175F06C7DE0) returned failure for request: vtkInformation (0000017591AD5DD0)<br>
Debug: Off<br>
Modified Time: 26086432<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_INFORMATION<br>
FORWARD_DIRECTION: 0<br>
ALGORITHM_AFTER_FORWARD: 1</p>

---

## Post #2 by @lassoan (2020-01-08 03:04 UTC)

<p>Currently, Slicer is only guaranteed to be able save/load files that only has ASCII characters in their full path.</p>

---
