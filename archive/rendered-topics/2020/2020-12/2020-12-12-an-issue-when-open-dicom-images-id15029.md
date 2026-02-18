# An issue when open DICOM images

**Topic ID**: 15029
**Date**: 2020-12-12
**URL**: https://discourse.slicer.org/t/an-issue-when-open-dicom-images/15029

---

## Post #1 by @Magdy (2020-12-12 21:40 UTC)

<p>Hi Colleagues,<br>
Whenever I try to open dicom PET images, the following error persists:<br>
Traceback (most recent call last):<br>
File “D:\Progam Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\DICOMLib\DICOMWidgets.py”, line 737, in getLoadablesFromFileLists<br>
loadablesByPlugin[plugin] = plugin.examine(fileLists)<br>
File “D:/Program Files/Slicer4.10Extension/PETDICOMExtension/lib/Slicer-4.10/qt-scripted-modules/DICOMPETSUVPlugin.py”, line 127, in examine<br>
rwvmFile = self.generateRWVMforFileList(fileList)<br>
File “D:/Program Files/Slicer4.10Extension/PETDICOMExtension/lib/Slicer-4.10/qt-scripted-modules/DICOMPETSUVPlugin.py”, line 169, in generateRWVMforFileList<br>
raise RuntimeError(“SUVFactorCalculator CLI did not complete cleanly”)<br>
RuntimeError: SUVFactorCalculator CLI did not complete cleanly<br>
Warning: Plugin failed: DICOMPETSUVPlugin</p>
<p>It happens in both 3d Slicer 4.10.2 and 4.13. The radiomics module doesn’t seem to work too…<br>
Any help is appreciated…<br>
Thanks</p>
<p>Khalil.</p>

---

## Post #2 by @lassoan (2021-07-22 21:36 UTC)

<p>I just see that no answer was given to this question. Let us know if you still have any questions related to this. In general, problems related to DICOM import can only be investigated if we get (anonymized/phantom/animal) sample image data sets.</p>

---
