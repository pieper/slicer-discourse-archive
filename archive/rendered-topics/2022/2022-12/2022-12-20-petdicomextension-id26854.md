---
topic_id: 26854
title: "Petdicomextension"
date: 2022-12-20
url: https://discourse.slicer.org/t/26854
---

# PETDICOMExtension

**Topic ID**: 26854
**Date**: 2022-12-20
**URL**: https://discourse.slicer.org/t/petdicomextension/26854

---

## Post #1 by @Mahdieh_Jajroudi (2022-12-20 16:41 UTC)

<p>When I loaded PET DICOM, I found this error what is meaning and what should i do?</p>
<p>Traceback (most recent call last):<br>
File “G:\3d slicer\Slicer 5.1.0-2022-07-26\lib\Slicer-5.1\qt-scripted-modules\DICOMLib\DICOMUtils.py”, line 748, in getLoadablesFromFileLists<br>
loadablesByPlugin[plugin] = plugin.examine(fileLists)<br>
File “G:/3d slicer/Slicer 5.1.0-2022-07-26/NA-MIC/Extensions-31096/PETDICOMExtension/lib/Slicer-5.1/qt-scripted-modules/DICOMPETSUVPlugin.py”, line 127, in examine<br>
rwvmFile = self.generateRWVMforFileList(fileList)<br>
File “G:/3d slicer/Slicer 5.1.0-2022-07-26/NA-MIC/Extensions-31096/PETDICOMExtension/lib/Slicer-5.1/qt-scripted-modules/DICOMPETSUVPlugin.py”, line 169, in generateRWVMforFileList<br>
raise RuntimeError(“SUVFactorCalculator CLI did not complete cleanly”)<br>
RuntimeError: SUVFactorCalculator CLI did not complete cleanly<br>
DICOM Plugin failed: SUVFactorCalculator CLI did not complete cleanly</p>

---
