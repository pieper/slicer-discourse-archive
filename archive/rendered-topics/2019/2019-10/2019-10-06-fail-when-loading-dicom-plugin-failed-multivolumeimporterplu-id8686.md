---
topic_id: 8686
title: "Fail When Loading Dicom Plugin Failed Multivolumeimporterplu"
date: 2019-10-06
url: https://discourse.slicer.org/t/8686
---

# Fail when loading DICOM: Plugin failed: MultiVolumeImporterPlugin

**Topic ID**: 8686
**Date**: 2019-10-06
**URL**: https://discourse.slicer.org/t/fail-when-loading-dicom-plugin-failed-multivolumeimporterplugin/8686

---

## Post #1 by @norus (2019-10-06 16:55 UTC)

<p>Hello cracks,<br>
a simple user see this warning and has no plan what to do:<br>
Warning: Plugin failed: MultiVolumeImporterPlugin</p>
<p>See python console for error message.<br>
DICOM Plugin failed: SetAttribute argument 2: (unicode conversion error)<br>
DICOM plugin failed to load ‘9: Schulter spir. 1.0 B70s’ as a ‘Scalar Volume’.<br>
Traceback (most recent call last):<br>
File “C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\DICOMLib\DICOMWidgets.py”, line 867, in proceedWithReferencedLoadablesSelection<br>
loadSuccess = plugin.load(loadable)<br>
File “C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py”, line 413, in load<br>
volumeNode = self.loadFilesWithSeriesReader(“GDCM”, loadable.files, loadable.name)<br>
File “C:/Program Files/Slicer 4.10.2/bin/…/lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py”, line 290, in loadFilesWithSeriesReader<br>
reader.SetArchetype(files[0]);<br>
TypeError: SetArchetype argument 1: (unicode conversion error)</p>
<p>I found the Plugin at github, but where it has to be placed or integrated?</p>
<p>thanks for help</p>

---

## Post #2 by @lassoan (2019-10-06 17:33 UTC)

<p>It seems that there are special characters in the filename or folder where you want to import fats from. Rename the files/folders to contain only ASCII characters.</p>

---

## Post #3 by @norus (2019-10-06 17:37 UTC)

<p>Just when you was writing i started to do this, and it works. there are some      - ö - in the header.<br>
Thank´s a lot for your help, really great project, I cross my fingers for you.</p>

---
