---
topic_id: 2274
title: "Nrrd Loading Broken On Windows Since Yesterday Nightly"
date: 2018-03-09
url: https://discourse.slicer.org/t/2274
---

# NRRD loading broken on Windows since yesterday nightly

**Topic ID**: 2274
**Date**: 2018-03-09
**URL**: https://discourse.slicer.org/t/nrrd-loading-broken-on-windows-since-yesterday-nightly/2274

---

## Post #1 by @cpinter (2018-03-09 16:46 UTC)

<p>It seems that NRRD loading has been broken on Windows by a commit made yesterday. I noticed it when I updated my local clone and tried using Slicer afterwards. NRRD files failed to be loaded in both debug and release mode. It’s also the same in the nightly package the factory made, and there are <a href="http://slicer.cdash.org/viewTest.php?onlydelta&amp;buildid=1217121">36 more failing tests on the dashboard</a>, so it’s definitely not a local issue.</p>
<details>
<summary>
Click here to see the error message</summary>
<p>vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open C:/Users/pinter/AppData/Local/Temp/RemoteIO/CT-chest.nrrd. ITK exception info: error in unknown:  Could not create IO object for reading file C:/Users/pinter/AppData/Local/Temp/RemoteIO/CT-chest.nrrd<br>
Tried to create one of the following:<br>
MRMLIDImageIO<br>
You probably failed to set a file suffix, or<br>
set the suffix to an unsupported type.</p>
<p>Algorithm vtkITKArchetypeDiffusionTensorImageReaderFile(00000237CF64BF00) returned failure for request: vtkInformation (00000237D3450AD0)<br>
Debug: Off<br>
Modified Time: 867266<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_INFORMATION<br>
FORWARD_DIRECTION: 0<br>
ALGORITHM_AFTER_FORWARD: 1</p>
<p>vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open C:/Users/pinter/AppData/Local/Temp/RemoteIO/CT-chest.nrrd. ITK exception info: error in unknown:  Could not create IO object for reading file C:/Users/pinter/AppData/Local/Temp/RemoteIO/CT-chest.nrrd<br>
Tried to create one of the following:<br>
MRMLIDImageIO<br>
You probably failed to set a file suffix, or<br>
set the suffix to an unsupported type.</p>
<p>Algorithm vtkITKArchetypeImageSeriesVectorReaderSeries(00000237CF64BF00) returned failure for request: vtkInformation (00000237D344C6B0)<br>
Debug: Off<br>
Modified Time: 868804<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_INFORMATION<br>
FORWARD_DIRECTION: 0<br>
ALGORITHM_AFTER_FORWARD: 1</p>
<p>vtkITKArchetypeImageSeriesReader::ExecuteInformation: Cannot open C:/Users/pinter/AppData/Local/Temp/RemoteIO/CT-chest.nrrd. ITK exception info: error in unknown:  Could not create IO object for reading file C:/Users/pinter/AppData/Local/Temp/RemoteIO/CT-chest.nrrd<br>
Tried to create one of the following:<br>
MRMLIDImageIO<br>
You probably failed to set a file suffix, or<br>
set the suffix to an unsupported type.</p>
<p>Algorithm vtkITKArchetypeImageSeriesScalarReader(00000237CF64CD80) returned failure for request: vtkInformation (00000237D3450260)<br>
Debug: Off<br>
Modified Time: 869571<br>
Reference Count: 1<br>
Registered Events: (none)<br>
Request: REQUEST_INFORMATION<br>
FORWARD_DIRECTION: 0<br>
ALGORITHM_AFTER_FORWARD: 1</p>
<p>ReadData: Cannot read file as a volume of type DiffusionTensorVolume[fullName = C:/Users/pinter/AppData/Local/Temp/RemoteIO/CT-chest.nrrd]<br>
Number of files listed in the node = 0.<br>
File reader says it was able to read 0 files.<br>
File reader used the archetype file name of C:/Users/pinter/AppData/Local/Temp/RemoteIO/CT-chest.nrrd []<br>
FileFormatError</p>
<p>ReadData: MRMLVolumeNode does not match file kind</p>
<p>ReadData: Failed to instantiate a file reader</p>
<p>ReadData: Cannot read file as a volume of type Volume[fullName = C:/Users/pinter/AppData/Local/Temp/RemoteIO/CT-chest.nrrd]<br>
Number of files listed in the node = 0.<br>
File reader says it was able to read 0 files.<br>
File reader used the archetype file name of C:/Users/pinter/AppData/Local/Temp/RemoteIO/CT-chest.nrrd []<br>
FileFormatError</p>
</details>
<p>I cannot see an obvious culprit in the log, so I’m hoping someone has an idea about what caused this.<br>
Thanks!</p>

---

## Post #2 by @lassoan (2018-03-09 17:45 UTC)

<p>This is a quite fundamental problem. <a class="mention" href="/u/jcfr">@jcfr</a> Can you have a look?</p>

---

## Post #3 by @jcfr (2018-03-09 18:55 UTC)

<p>This should be fixed in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27035">r27035</a></p>

---
