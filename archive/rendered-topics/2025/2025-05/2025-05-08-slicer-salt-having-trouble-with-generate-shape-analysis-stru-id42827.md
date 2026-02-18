# SLICER SALT .... having trouble with "Generate Shape Analysis Structure"

**Topic ID**: 42827
**Date**: 2025-05-08
**URL**: https://discourse.slicer.org/t/slicer-salt-having-trouble-with-generate-shape-analysis-structure/42827

---

## Post #1 by @Deep_Learning (2025-05-08 13:31 UTC)

<p>I’m having trouble with data importer, SlicerSalt 6.0.0.</p>
<p>I can import and view the sampledata, but when I try to “Generate Shape Analysis Structure”  I get this error on windows and linux.</p>
<p>Traceback (most recent call last):</p>
<p>File “/xxx/SlicerSALT-6.0.0-linux-amd64/bin/../lib/SlicerSALT-5.9/qt-scripted-modules/DataImporter.py”, line 1457, in onGenerateShapeAnalysisStructure</p>
<p>self.logic.generateShapeAnlaysisStructure(self.inputShapeAnalysisPath)</p>
<p>File “/xxx/SlicerSALT-6.0.0-linux-amd64/bin/../lib/SlicerSALT-5.9/qt-scripted-modules/DataImporter.py”, line 734, in generateShapeAnlaysisStructure</p>
<p>slicer.mrmlScene.RemoveNode(slicer.util.getNode(pattern=full_segmentName+’ LabelMap_ColorTable’))</p>
<p>File “/xxx/SlicerSALT-6.0.0-linux-amd64/bin/Python/slicer/util.py”, line 1614, in getNode</p>
<p>raise MRMLNodeNotFoundException(“could not find nodes in the scene by name or id ‘%s’” % (pattern if (isinstance(pattern, str)) else “”))</p>
<p>slicer.util.MRMLNodeNotFoundException: could not find nodes in the scene by name or id ‘case01_31 LabelMap_ColorTable’</p>

---

## Post #2 by @Jared_Vicory (2025-05-08 15:25 UTC)

<p>Hi, thanks for trying SALT and reporting this issue.</p>
<p>A fix has just been merged here: <a href="https://github.com/Kitware/SlicerSALT/pull/359" class="inline-onebox" rel="noopener nofollow ugc">BUG: Fix crash due to deprecated functionality by vicory · Pull Request #359 · Kitware/SlicerSALT · GitHub</a></p>
<p>It should show up in the nightly builds starting tomorrow. You can find those here: <a href="https://data.kitware.com/#collection/586fbb7b8d777f05f44a5c7b/folder/5bd85a568d777f06b9402dad" class="inline-onebox" rel="noopener nofollow ugc">Kitware Data</a></p>

---

## Post #3 by @Deep_Learning (2025-05-08 17:28 UTC)

<p>looking forward… Thanks…</p>

---

## Post #4 by @Deep_Learning (2025-05-16 12:45 UTC)

<p>working in the nightly</p>

---
