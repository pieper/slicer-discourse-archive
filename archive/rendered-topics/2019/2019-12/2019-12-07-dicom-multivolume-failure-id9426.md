# Dicom multivolume failure

**Topic ID**: 9426
**Date**: 2019-12-07
**URL**: https://discourse.slicer.org/t/dicom-multivolume-failure/9426

---

## Post #1 by @Jainey (2019-12-07 20:05 UTC)

<p>I got the following error message while loading a dynamic ct scan</p>
<p>File “/Applications/Slicer 2.app/Contents/Extensions-28257/SlicerRT/lib/Slicer-4.10/qt-scripted-modules/DicomRtImportExportPlugin.py”, line 41, in examineForImport<br>
slicer.modules.dicomrtimportexport.logic().ExamineForLoad(vtkFileList, loadablesCollection)<br>
AttributeError: ‘module’ object has no attribute ‘dicomrtimportexport’<br>
Warning: Plugin failed: DicomRtImportExportPlugin</p>
<p>See python console for error message.<br>
DICOM Plugin failed: ‘module’ object has no attribute ‘dicomrtimportexport’</p>
<p>Slicer 4.10 stable (This happened with nightly few days ago and I installed the stable)</p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2019-12-09 05:34 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> can you check this? It may be due to recent SlicerRT DICOM related changes (or DICOM browser changes in Slicer core a bit earlier).</p>

---
