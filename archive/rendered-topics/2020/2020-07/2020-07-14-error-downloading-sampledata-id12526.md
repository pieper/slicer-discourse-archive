---
topic_id: 12526
title: "Error Downloading Sampledata"
date: 2020-07-14
url: https://discourse.slicer.org/t/12526
---

# Error downloading SampleData

**Topic ID**: 12526
**Date**: 2020-07-14
**URL**: https://discourse.slicer.org/t/error-downloading-sampledata/12526

---

## Post #1 by @vertebra (2020-07-14 12:56 UTC)

<p>Hello, when I try and download SampleData, I get this error:</p>
<p>Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SampleData.py”, line 356, in <br>
b.connect(‘clicked()’, lambda s=source: logic.downloadFromSource(s))<br>
File “/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SampleData.py”, line 677, in downloadFromSource<br>
loadedNode = self.loadNode(filePath, nodeName, loadFileType, source.loadFileProperties.copy())<br>
File “/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SampleData.py”, line 886, in loadNode<br>
success = slicer.app.coreIOManager().loadNodes(fileType, fileProperties, loadedNodes)<br>
ValueError: Could not find matching overload for given arguments:<br>
(‘VolumeFile’, {‘fileName’: ‘/private/var/folders/7w/1j_y25px3zb6x2kd4xdp2_7r0000gn/T/Slicer-KBEHL360/RemoteIO/CTA-cardio.nrrd’, ‘name’: ‘CTACardio’}, (vtkCommonCorePython.vtkCollection)0x156c61408)<br>
The following slots are available:<br>
loadNodes(qSlicerIO::IOFileType fileType, qSlicerIO::IOProperties parameters, vtkCollection loadedNodes) -&gt; bool<br>
loadNodes(qSlicerIO::IOFileType fileType, qSlicerIO::IOProperties parameters) -&gt; bool<br>
loadNodes(qSlicerIO::IOFileType fileType, qSlicerIO::IOProperties parameters, vtkCollection loadedNodes) -&gt; bool<br>
loadNodes(qSlicerIO::IOFileType fileType, qSlicerIO::IOProperties parameters) -&gt; bool</p>
<p>Can anyone help?</p>

---

## Post #2 by @lassoan (2020-07-14 13:21 UTC)

<p>Is this a new problem? Could you try a Slicer version from two weeks and one month ago?<br>
You can download older versions by specifying <code>offset</code> or <code>date</code> argument on the download page (see <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/General#Where_can_I_download_Slicer.3F">here</a>).</p>

---

## Post #3 by @vertebra (2020-07-14 13:24 UTC)

<p>Yes, it had been working for the last week. This is version 4.11(the preview I think). I’ll try again then.</p>

---
