# OpenCAD segmentation issue

**Topic ID**: 22585
**Date**: 2022-03-18
**URL**: https://discourse.slicer.org/t/opencad-segmentation-issue/22585

---

## Post #1 by @malcolmlim (2022-03-18 14:10 UTC)

<p>Hello all,</p>
<p>I am having issue with OpenCad extension and occured during the the final steps of “Tumor Segmentation from DCE-MRI" tutorial</p>
<p>After designating the sample volumes (Pre, 1st-4th timepoints after DCE), I clicked Apply SegmentCAD and this log message came up:</p>
<p>Traceback (most recent call last):<br>
File “C:/Users/uqmlim3/AppData/Roaming/NA-MIC/Extensions-28257/OpenCAD/lib/Slicer-4.10/qt-scripted-modules/SegmentCAD.py”, line 619, in onSegmentCADButtonClicked<br>
self.logic.renderLabelMap()<br>
File “C:\Users\uqmlim3\AppData\Roaming\NA-MIC\Extensions-28257\OpenCAD\lib\Slicer-4.10\qt-scripted-modules\SegmentCADLogic\SegmentCADLogic.py”, line 112, in renderLabelMap<br>
SegmentCADLabelMapImageData.SetScalarTypeToShort()<br>
AttributeError: ‘vtkCommonDataModelPython.vtkImageData’ object has no attribute ‘SetScalarTypeToShort’</p>
<p>I tried to follow the remedy in a similar post, but being very new I am not sure how to go about replacing the ‘SegmentCADLogic.py’ with the fixed version. I tried searching the file ‘SegmentCADlogic’ in Slicer 4.10.2 Folder but nothing comes up. I can see other .py files but no SegmentCADlogic, as such am at the limit of my capabilities. Can anyone enlighten on how do i go about getting this fix please?</p>
<p>Slicer version: 4.10.1<br>
Extension i’m facing issues: OpenCAD (Published on Wed Jun 02 2021) <a href="https://www.slicer.org/w/index.php/Documentation/4.3/Extensions/OpenCAD" class="inline-onebox" rel="noopener nofollow ugc">Documentation/4.3/Extensions/OpenCAD - Slicer Wiki</a><br>
System: Windows PC</p>

---

## Post #2 by @pieper (2022-03-18 19:54 UTC)

<p>This is a pretty old extension written for Slicer 4.3 and I don’t know if it ever worked with 4.10.2.  You might get what you need by using SlicerRadiomics in 4.11.</p>

---
