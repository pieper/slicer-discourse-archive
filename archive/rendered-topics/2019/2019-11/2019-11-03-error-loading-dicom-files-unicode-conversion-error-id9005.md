# Error loading DICOM files - unicode conversion error

**Topic ID**: 9005
**Date**: 2019-11-03
**URL**: https://discourse.slicer.org/t/error-loading-dicom-files-unicode-conversion-error/9005

---

## Post #1 by @dixmos (2019-11-03 13:09 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.10.2</p>
<p>Hello<br>
I have some problems loading my DICOM files. Other DICOM viewrs open my files but the Slicer didnt recognize them.<br>
Could you help me please?</p>
<p>LOG:<br>
DICOM plugin failed to load ‘3: 1.25 ABDOMEN SIMPLE’ as a ‘Scalar Volume’.<br>
Traceback (most recent call last):<br>
File “C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\DICOMLib\DICOMWidgets.py”, line 867, in proceedWithReferencedLoadablesSelection<br>
loadSuccess = plugin.load(loadable)<br>
File “C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py”, line 413, in load<br>
volumeNode = self.loadFilesWithSeriesReader(“GDCM”, loadable.files, loadable.name)<br>
File “C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py”, line 290, in loadFilesWithSeriesReader<br>
reader.SetArchetype(files[0]);<br>
TypeError: SetArchetype argument 1: (unicode conversion error)</p>
<p>DICOM plugin failed to load ‘1: XIFOIDES - imageOrientationPatient 2’ as a ‘Scalar Volume’.<br>
Traceback (most recent call last):<br>
File “C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\DICOMLib\DICOMWidgets.py”, line 867, in proceedWithReferencedLoadablesSelection<br>
loadSuccess = plugin.load(loadable)<br>
File “C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py”, line 413, in load<br>
volumeNode = self.loadFilesWithSeriesReader(“GDCM”, loadable.files, loadable.name)<br>
File “C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py”, line 290, in loadFilesWithSeriesReader<br>
reader.SetArchetype(files[0]);<br>
TypeError: SetArchetype argument 1: (unicode conversion error)</p>
<p>DICOM plugin failed to load ‘1: XIFOIDES’ as a ‘Scalar Volume’.<br>
Traceback (most recent call last):<br>
File “C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\DICOMLib\DICOMWidgets.py”, line 867, in proceedWithReferencedLoadablesSelection<br>
loadSuccess = plugin.load(loadable)<br>
File “C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py”, line 413, in load<br>
volumeNode = self.loadFilesWithSeriesReader(“GDCM”, loadable.files, loadable.name)<br>
File “C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py”, line 290, in loadFilesWithSeriesReader<br>
reader.SetArchetype(files[0]);<br>
TypeError: SetArchetype argument 1: (unicode conversion error)</p>
<p>DICOM plugin failed to load ‘1: XIFOIDES - imageOrientationPatient 1’ as a ‘Scalar Volume’.<br>
Traceback (most recent call last):<br>
File “C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\DICOMLib\DICOMWidgets.py”, line 867, in proceedWithReferencedLoadablesSelection<br>
loadSuccess = plugin.load(loadable)<br>
File “C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py”, line 413, in load<br>
volumeNode = self.loadFilesWithSeriesReader(“GDCM”, loadable.files, loadable.name)<br>
File “C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py”, line 290, in loadFilesWithSeriesReader<br>
reader.SetArchetype(files[0]);<br>
TypeError: SetArchetype argument 1: (unicode conversion error)</p>
<p>Could not load: 3: 1.25 ABDOMEN SIMPLE as a Scalar Volume<br>
Could not load: 1: XIFOIDES - imageOrientationPatient 2 as a Scalar Volume<br>
Could not load: 1: XIFOIDES as a Scalar Volume<br>
Could not load: 1: XIFOIDES - imageOrientationPatient 1 as a Scalar Volume</p>

---

## Post #2 by @lassoan (2019-11-03 13:12 UTC)

<p>It seems that there are special characters in the path. Please make sure that Slicer is installed in a folder that only has ASCII characters in the path and store all data in folders that only contain ASCII characters.</p>

---
