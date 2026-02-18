# Load dicom path in unicode

**Topic ID**: 7365
**Date**: 2019-07-01
**URL**: https://discourse.slicer.org/t/load-dicom-path-in-unicode/7365

---

## Post #1 by @Mr.wyr (2019-07-01 09:07 UTC)

<p>i want to load dicom in chinese path, i change CTK source code,and set python defaultencoding to utf-8, now import chinese path is ok, examine is ok, but when click load button,some error:<br>
Loading with imageIOName: GDCM<br>
vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file C:/Users/Dell/Desktop/e3d/数据CT/测试/IMG00282.dcm does not existAlgorithm vtkITKArchetypeImageSeriesScalarReader(000002024FFFD6A0) returned failure for request: vtkInformation (0000020255ECBE20)<br>
Debug: Off<br>
Modified Time: 339515<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_INFORMATION<br>
FORWARD_DIRECTION: 0<br>
ALGORITHM_AFTER_FORWARD: 1</p>
<p>Could not read scalar volume using GDCM approach.  Error is: FileNotFoundError<br>
Loading with imageIOName: DCMTK<br>
vtkITKArchetypeImageSeriesReader::ExecuteInformation: Archetype file C:/Users/Dell/Desktop/e3d/数据CT/测试/IMG00282.dcm does not existAlgorithm vtkITKArchetypeImageSeriesScalarReader(000002024FFF6000) returned failure for request: vtkInformation (000002025EEA2080)<br>
Debug: Off<br>
Modified Time: 339605<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_INFORMATION<br>
FORWARD_DIRECTION: 0<br>
ALGORITHM_AFTER_FORWARD: 1</p>
<p>Could not read scalar volume using DCMTK approach.  Error is: FileNotFoundError</p>
<p>???:3: Body 1.0 CE???Scalar Volume</p>
<p>i found error in DICOMScalarVolumePlugin.py function loadFilesWithSeriesReader(self, imageIOName, files, name), so i print the files[0]:<br>
C:/Users/Dell/Desktop/e3d/êy?YCT/2aê?/IMG00282.dcm<br>
i don’t know what this is,<br>
but i print DICOMWidgets.py function getFileListsForRole(self, uidArgument, role) the return fileLists, it’s get CTK dicomdatabase result,the path is:<br>
u’C:/Users/Dell/Desktop/e3d/\u6570\u636eCT/\u6d4b\u8bd5/IMG00001.dcm’<br>
it’s unicode<br>
how can i do</p>

---

## Post #2 by @lassoan (2019-07-01 12:46 UTC)

<p>Latin1 encoding is assumed at a number of places in CTK and Slicer. Therefore, currently you can only load data from paths that only contain characters in the Latin1 character set. We would like to improve unicode support of Slicer, so if you can fix the problem then we welcome a pull request.</p>

---

## Post #3 by @Chris_Rorden (2019-08-22 21:41 UTC)

<p>@<a href="/u/ljod">ljod</a> perhaps your Dcm2niixGUI module could be extended to support this. Consider a folder containing DICOMs named “/home/chris//数据MR测试/4_me_数据MR测试”. In my testing dcm2niix will process this when run directly from the command line, but when this is set as the input directory in the Slicer Dcm2niixGUI module pressing apply shows the “Running…” option forever (while the same files in “/home/chris/MR/4_me_MR” load just fine.</p>

---
