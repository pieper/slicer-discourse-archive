---
topic_id: 9047
title: "Error Loading Ct Images"
date: 2019-11-06
url: https://discourse.slicer.org/t/9047
---

# Error loading CT images

**Topic ID**: 9047
**Date**: 2019-11-06
**URL**: https://discourse.slicer.org/t/error-loading-ct-images/9047

---

## Post #1 by @INVESTIGACION_Y_DESA (2019-11-06 19:27 UTC)

<p>DICOM plugin failed to load ‘3: Óseo 0.63  H70s’ as a ‘Scalar Volume’.<br>
Traceback (most recent call last):<br>
File “C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\DICOMLib\DICOMWidgets.py”, line 867, in proceedWithReferencedLoadablesSelection<br>
loadSuccess = plugin.load(loadable)<br>
File “C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py”, line 417, in load<br>
volumeNode = self.loadFilesWithSeriesReader(readerApproach, loadable.files, loadable.name)<br>
File “C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py”, line 290, in loadFilesWithSeriesReader<br>
reader.SetArchetype(files[0]);<br>
TypeError: SetArchetype argument 1: (unicode conversion error)</p>
<p>Could not load: 3: Óseo 0.63  H70s as a Scalar Volume<br>
Traceback (most recent call last):<br>
File “C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\DICOMLib\DICOMWidgets.py”, line 737, in getLoadablesFromFileLists<br>
loadablesByPlugin[plugin] = plugin.examine(fileLists)<br>
File “C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py”, line 106, in examine<br>
loadables += self.examineFiles(files)<br>
File “C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py”, line 493, in examineFiles<br>
mvNodes = self.initMultiVolumes(subseriesLists[key])<br>
File “C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py”, line 885, in initMultiVolumes<br>
mvNode.SetAttribute(‘MultiVolume.FrameFileList’, frameFileListStr)<br>
TypeError: SetAttribute argument 2: (unicode conversion error)<br>
Warning: Plugin failed: MultiVolumeImporterPlugin</p>
<p>See python console for error message.<br>
DICOM Plugin failed: SetAttribute argument 2: (unicode conversion error)<br>
Traceback (most recent call last):<br>
File “C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\DICOMLib\DICOMWidgets.py”, line 737, in getLoadablesFromFileLists<br>
loadablesByPlugin[plugin] = plugin.examine(fileLists)<br>
File “C:/Users/Investigacion/AppData/Roaming/NA-MIC/Extensions-28257/SlicerRT/lib/Slicer-4.10/qt-scripted-modules/DicomSroImportPlugin.py”, line 35, in examine<br>
fileList.InsertNextValue(f)<br>
TypeError: InsertNextValue argument 1: (unicode conversion error)<br>
Warning: Plugin failed: DicomSroImportPlugin</p>
<p>See python console for error message.<br>
DICOM Plugin failed: InsertNextValue argument 1: (unicode conversion error)<br>
DICOM plugin failed to load ‘3: Óseo 0.63  H70s’ as a ‘Scalar Volume’.<br>
Traceback (most recent call last):<br>
File “C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\DICOMLib\DICOMWidgets.py”, line 867, in proceedWithReferencedLoadablesSelection<br>
loadSuccess = plugin.load(loadable)<br>
File “C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py”, line 417, in load<br>
volumeNode = self.loadFilesWithSeriesReader(readerApproach, loadable.files, loadable.name)<br>
File “C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py”, line 290, in loadFilesWithSeriesReader<br>
reader.SetArchetype(files[0]);<br>
TypeError: SetArchetype argument 1: (unicode conversion error)</p>

---

## Post #2 by @lassoan (2019-11-06 19:33 UTC)

<p>Currently, Slicer only supports DICOM import from files and folders that do not contain any special (non-ASCII) characters. See <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM">DICOM FAQ</a> for solution: “Try moving the data and the database directory to a path that includes only US English characters (ASCII) to avoid possible parsing errors. No special, international characters are allowed.”</p>

---
