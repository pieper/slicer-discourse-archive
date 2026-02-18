# How to insert Dicom files from an nhs disk

**Topic ID**: 29237
**Date**: 2023-05-02
**URL**: https://discourse.slicer.org/t/how-to-insert-dicom-files-from-an-nhs-disk/29237

---

## Post #1 by @Amanghir (2023-05-02 01:25 UTC)

<p>Hi</p>
<p>I have an NHS encrypted disk with mri scans of my brain. I am very new to this so I am not even sure if I am doing this right. When I click on the load data button, and then choose a directory there are lots of files to choose from and I don’t know what to do from here. My end goal is to try and 3D print my brain.</p>
<p>These are the kind of things i’m seeing:</p>
<p>D:/7z.dll<br>
D:/7zG.exe<br>
D:/_start_here.bat<br>
D:/autorun.bat<br>
D:/autorun.inf<br>
D:/BLANK.JPG<br>
D:/CONTENT.ZIP<br>
D:filesize.bat<br>
D:/launch.bat<br>
D:/Read Me first - V1.4.pdf<br>
D:/Read Me First.txt<br>
D:/start.bat</p>
<p>Any help is appreciated!</p>
<p>Operating system: Windows<br>
Slicer version:5.2.2<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @pearsonm (2023-05-02 04:53 UTC)

<p>The data files are most likely in the compressed file CONTENT.ZIP and will need to be decompressed before they can be loaded into Slicer. If you open the zip file you should be asked for the password and then be able to save the files into a local directory.</p>

---
