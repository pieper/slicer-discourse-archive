# Slicer source code for stl file extraction

**Topic ID**: 18636
**Date**: 2021-07-12
**URL**: https://discourse.slicer.org/t/slicer-source-code-for-stl-file-extraction/18636

---

## Post #1 by @11116 (2021-07-12 07:15 UTC)

<p>Hi,<br>
I want to see 3d slicer source code for the STL file extraction of  a multi label image in python.Where can i find it? I want to extract an aggregated mess for all labels.</p>
<p>Thank you in advance for your help,<br>
Spyridoula Zagkou</p>

---

## Post #2 by @lassoan (2021-07-12 14:14 UTC)

<p>The implementation is available here: <a href="https://github.com/Slicer/Slicer/blob/master/Libs/vtkSegmentationCore/vtkBinaryLabelmapToClosedSurfaceConversionRule.cxx" class="inline-onebox">Slicer/vtkBinaryLabelmapToClosedSurfaceConversionRule.cxx at master · Slicer/Slicer · GitHub</a></p>
<p>Note that you can use Slicer without graphical user interface in batch processing, you can run your processing script in Slicer’s Python environment or using Slicer as Jupyter Notebook kernel - so it should not be necessary to copy-paste code from Slicer. But if you have a use case that is not covered by these then let us know and we may give more specific advice.</p>

---

## Post #3 by @11116 (2021-07-12 16:22 UTC)

<p>Yes,I’m sorry for misunderstanding.I’m searching the python scrip for this process without GUI.</p>
<p>.</p>

---

## Post #4 by @lassoan (2021-07-12 17:36 UTC)

<p>You can find lots of examples how to manipulate segmentations using Python scripting in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#segmentations">script repository</a>.</p>

---
