# Unable to use DICOMUtils to load dicom files

**Topic ID**: 41290
**Date**: 2025-01-26
**URL**: https://discourse.slicer.org/t/unable-to-use-dicomutils-to-load-dicom-files/41290

---

## Post #1 by @slicerpy (2025-01-26 09:50 UTC)

<p>I am trying use the below sample code from vscode  , but getting the error captured below.<br>
from DICOMLib import DICOMUtils<br>
with DICOMUtils.TemporaryDICOMDatabase() as db:<br>
DICOMUtils.importDicom(dicomDataDir, db)<br>
patientUIDs = db.patients()<br>
for patientUID in patientUIDs:<br>
loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))</p>
<p>Error<br>
<strong>No module named ‘logic’</strong><br>
3.9.10 (main, Jan 23 2025, 23:04:06) [MSC v.1942 64 bit (AMD64)]<br>
Traceback (most recent call last):<br>
File “c:\Users\praveen.selvaraj\Downloads\Slicer-5.6.2-Win\bin\import sys.py”, line 10, in <br>
from DICOMLib import DICOMUtils<br>
File “C:\Users\praveen.selvaraj\AppData\Local\slicer.org\Slicer 5.8.0\lib\Slicer-5.8\qt-scripted-modules\DICOMLib_<em>init</em>_.py”, line 1, in <br>
from .DICOMProcesses import *<br>
File “C:\Users\praveen.selvaraj\AppData\Local\slicer.org\Slicer 5.8.0\lib\Slicer-5.8\qt-scripted-modules\DICOMLib\DICOMProcesses.py”, line 38, in <br>
class DICOMProcess:<br>
File “C:\Users\praveen.selvaraj\AppData\Local\slicer.org\Slicer 5.8.0\lib\Slicer-5.8\qt-scripted-modules\DICOMLib\DICOMProcesses.py”, line 84, in DICOMProcess<br>
def start(self, cmd: str, args: list[str]) → qt.QProcess:<br>
<strong>AttributeError: module ‘qt’ has no attribute ‘QProcess’</strong></p>

---

## Post #2 by @pieper (2025-01-26 10:24 UTC)

<p>The DICOM module is set up to work in the Slicer environment, not other python environments. If you want to dig into the code it’s likely that a large part could be factored out.</p>

---

## Post #3 by @slicerpy (2025-01-27 20:17 UTC)

<p>Thank you pieper. So I am looking to automate manual segmentation , so It is recommended and potentially possible(without refactor) only from slicer python console ?</p>

---

## Post #4 by @pieper (2025-01-27 22:45 UTC)

<p>If you want to use Slicer’s features for now you need to use Slicer’s python environment, which you can do with <code>--no-main-window</code> and specify a python script. If you want to factor out some features to use outside of Slicer you can, but it means doing some coding work.  Slicer’s python is basically just python, but with extra features enabled to support the GUI app.</p>

---
