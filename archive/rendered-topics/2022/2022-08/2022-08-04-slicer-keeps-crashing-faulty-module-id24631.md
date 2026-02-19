---
topic_id: 24631
title: "Slicer Keeps Crashing Faulty Module"
date: 2022-08-04
url: https://discourse.slicer.org/t/24631
---

# Slicer keeps crashing "faulty module"

**Topic ID**: 24631
**Date**: 2022-08-04
**URL**: https://discourse.slicer.org/t/slicer-keeps-crashing-faulty-module/24631

---

## Post #1 by @sannpeterson (2022-08-04 00:34 UTC)

<p>I have both of the latest stable and preview releases installed. Both started crashing immediately after loading a scene. The event viewer shows either one of these errors (below). I have already tried reinstalling but it’s still crashing. Please help</p>
<p>Faulting application name: SlicerApp-real.exe, version: 0.0.0.0, time stamp: 0x62ea0805<br>
Faulting module name: vtkOpenGL-9.1.dll, version: 0.0.0.0, time stamp: 0x62e9f3d1<br>
Exception code: 0xc0000005<br>
Fault offset: 0x0000000000093abc<br>
Faulting process id: 0x1464</p>
<p>Faulting application name: SlicerApp-real.exe, version: 0.0.0.0, time stamp: 0x62ea0805<br>
Faulting module name: vtkCommon-9.1.dll, version: 0.0.0.0, time stamp: 0x62e9ef4f<br>
Exception code: 0xc0000005<br>
Fault offset: 0x000000000010c0c2<br>
Faulting process id: 0x1054</p>

---

## Post #2 by @lassoan (2022-08-04 05:30 UTC)

<p>Could you share the faulty scene with us (upload it to Dropbox, OneDrive, Google drive, etc. and post the link here)?</p>

---

## Post #3 by @sannpeterson (2022-08-06 22:19 UTC)

<p><a href="https://www.dropbox.com/s/n3t77hwhkcoaxfw/2022-07-30-Scene.mrml?dl=0" rel="noopener nofollow ugc">link here</a></p>
<p>Slicer has been crashing periodically. Seems to be happening regardless of what scene I have open. For your testing purposes I’ve included a dropbox link above.</p>
<p>This is the error I get each time:</p>
<p>Faulting application name: SlicerApp-real.exe, version: 0.0.0.0, time stamp: 0x62ea0805<br>
Faulting module name: vtkCommon-9.1.dll, version: 0.0.0.0, time stamp: 0x62e9ef4f<br>
Exception code: 0xc0000005<br>
Fault offset: 0x000000000010c0c2<br>
Faulting process id: 0x28a8<br>
Faulting application start time: 0x01d8a9d12a71876a<br>
Faulting application path: C:\Users\sannpeterson\AppData\Local\NA-MIC\Slicer 5.1.0-2022-07-27\bin\SlicerApp-real.exe<br>
Faulting module path: C:\Users\sannpeterson\AppData\Local\NA-MIC\Slicer 5.1.0-2022-07-27\bin\vtkCommon-9.1.dll<br>
Report Id: 65bcfca0-74a8-49b4-b12a-77f42955138f<br>
Faulting package full name:<br>
Faulting package-relative application ID:</p>

---

## Post #4 by @lassoan (2022-08-13 21:32 UTC)

<p>Thanks for the additional information. To investigate this, I would need the complete scene - saved as an .mrb file. (The .mrml file that you uploaded does not contain any bulk data, such as images, segmentations, markups.)</p>

---

## Post #5 by @sannpeterson (2022-08-13 21:44 UTC)

<p>Here it is: <a href="https://www.dropbox.com/s/eh6usw195m2vjx9/MRA629_crop.mrb?dl=0" rel="noopener nofollow ugc">link to mrb</a></p>

---

## Post #6 by @chir.set (2022-08-14 08:47 UTC)

<p>While not resolving your problem, I could load your MRB file without any issue on Linux.</p>
<p>By the way, it’s a very beautiful segmentation of cerebral arteries. I wonder how much time was spent on this and how you proceeded. For it’s not a trivial exercise.</p>

---
