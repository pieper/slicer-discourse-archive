---
topic_id: 2109
title: "Add Data Does Not Load"
date: 2018-02-18
url: https://discourse.slicer.org/t/2109
---

# Add DATA - does not load

**Topic ID**: 2109
**Date**: 2018-02-18
**URL**: https://discourse.slicer.org/t/add-data-does-not-load/2109

---

## Post #1 by @MSilent (2018-02-18 16:15 UTC)

<p>Operating system:Windows 10<br>
Slicer version:4.8.1<br>
Expected behavior: choose directory/fie to add.<br>
Actual behavior: I choose the directory I wish to add and nothing happens. It does not show up on the dialog box.  After a while a get a message that it is not responding and I have to shut it down.<br>
Data that is already loaded I also cannot get to show up on the screen. I can select the file I want but when I press load it does not load.<br>
The new data that I wanted to import is a patched DICOM file.</p>

---

## Post #2 by @lassoan (2018-02-18 17:49 UTC)

<p>Drag-and-drop the folder that contains your files, choose to import as DICOM, then use DICOM module to load the image into the scene.</p>

---

## Post #3 by @MSilent (2018-02-18 20:54 UTC)

<p>I tried that.  But it is just sitting there, saying 0% done, for about the last hour.<br>
Which directory should I try to load? I have DICOM/pa001.  It is recognising it as a DICOM file.</p>

---

## Post #4 by @lassoan (2018-02-18 21:59 UTC)

<p>Drag-and-drop pa001 folder. If it fails to load then please post the application log (menu: Help/Report a bug) or share the data set (make sure it is properly anonymized if it is human data).</p>

---

## Post #5 by @danagood (2018-02-18 23:12 UTC)

<p>I’ve seen this happen when a zombie Slicer process is still running. Close<br>
your current instance, then check your task manager-&gt; processes and kill<br>
any lingerers.</p>

---

## Post #6 by @MSilent (2018-02-19 08:20 UTC)

<p>Ton of error message</p>
<p>SQL failed<br>
Bad SQL: SELECT InsertTimestamp FROM Images WHERE Filename == ?<br>
Error text: database disk image is malformed Unable to fetch row</p>
<p>A later message is</p>
<p>C:/Users/pg13t/Desktop/3D Ortho Prints/TROH84507_fixed/DICOM/pa001/st000/se000/ct000.dcmC:/Users/pg13t/Desktop/3D Ortho Prints/TROH84507_fixed/DICOM/pa001/st000/se000/ct001.dcmC:/Users/pg13t/Desktop/3D Ortho Prints/TROH84507_fixed/DICOM/pa001/st000/se000/ct002.dcmC:/Users/pg13t/Desktop/3D Ortho Prints/TROH84507_fixed/DICOM/pa001/st000/se000/ct003.dcmC:/Users/pg13t/Desktop/3D Ortho Prints/TROH84507_fixed/DICOM/pa001/st000/se000/ct004.dcmC:/Users/pg13t/Desktop/3D Ortho Prints/TROH84507_fixed/DICOM/pa001/st000/se000/ct005.dcmC:/Users/pg13t/Desktop/3D Ortho Prints/TROH84507_fixed/DICOM/pa001/st000/se000/ct006.dcmC:/Users/pg13t/Desktop/3D Ortho Prints/TROH84507_fixed/DICOM/pa001/st000/se000/ct007.dcmC:/Users/pg13t/Desktop/3D Ortho Prints/TROH84507_fixed/DICOM/pa001/st000/se000/ct008.dcmImported a DICOM directory, checking for extensions</p>
<p>The final one<br>
Traceback (most recent call last):<br>
File “C:\Program Files\Slicer 4.8.1\lib\Slicer-4.8\qt-scripted-modules\DICOMLib\DICOMWidgets.py”, line 413, in timerCallback<br>
self.promptForExtensions()<br>
File “C:\Program Files\Slicer 4.8.1\lib\Slicer-4.8\qt-scripted-modules\DICOMLib\DICOMWidgets.py”, line 418, in promptForExtensions<br>
extensionsToOffer = self.checkForExtensions()<br>
File “C:\Program Files\Slicer 4.8.1\lib\Slicer-4.8\qt-scripted-modules\DICOMLib\DICOMWidgets.py”, line 481, in checkForExtensions<br>
instance0 = slicer.dicomDatabase.filesForSeries(series)[0]<br>
IndexError: tuple index out of range</p>
<p>I cancel the import as it does not do anything.  It doesn’t give me a %update on this one</p>

---

## Post #7 by @MSilent (2018-02-19 08:40 UTC)

<p>If I use the DICOM button to load previously used data sets I get the message:</p>
<p>Traceback (most recent call last):<br>
File “C:\Program Files\Slicer 4.8.1\lib\Slicer-4.8\qt-scripted-modules\DICOMLib\DICOMWidgets.py”, line 766, in loadCheckedLoadables<br>
self.examineForLoading()<br>
File “C:\Program Files\Slicer 4.8.1\lib\Slicer-4.8\qt-scripted-modules\DICOMLib\DICOMWidgets.py”, line 677, in examineForLoading<br>
self.loadablesByPlugin, loadEnabled = self.getLoadablesFromFileLists(self.fileLists)<br>
TypeError: ‘NoneType’ object is not iterable<br>
Traceback (most recent call last):<br>
File “C:\Program Files\Slicer 4.8.1\lib\Slicer-4.8\qt-scripted-modules\DICOMLib\DICOMWidgets.py”, line 766, in loadCheckedLoadables<br>
self.examineForLoading()<br>
File “C:\Program Files\Slicer 4.8.1\lib\Slicer-4.8\qt-scripted-modules\DICOMLib\DICOMWidgets.py”, line 677, in examineForLoading<br>
self.loadablesByPlugin, loadEnabled = self.getLoadablesFromFileLists(self.fileLists)<br>
TypeError: ‘NoneType’ object is not iterable<br>
Traceback (most recent call last):<br>
File “C:\Program Files\Slicer 4.8.1\lib\Slicer-4.8\qt-scripted-modules\DICOMLib\DICOMWidgets.py”, line 766, in loadCheckedLoadables<br>
self.examineForLoading()<br>
File “C:\Program Files\Slicer 4.8.1\lib\Slicer-4.8\qt-scripted-modules\DICOMLib\DICOMWidgets.py”, line 677, in examineForLoading<br>
self.loadablesByPlugin, loadEnabled = self.getLoadablesFromFileLists(self.fileLists)<br>
TypeError: ‘NoneType’ object is not iterable</p>

---

## Post #8 by @lassoan (2018-02-19 12:46 UTC)

<p>The DICOM database sem to be corrupted or in an incorrect location (not writeable by current user). Please try the solution described here: <a href="https://discourse.slicer.org/t/why-i-can-not-import-dicom/204/10?u=lassoan">Why I can not import DICOM?</a></p>

---

## Post #9 by @MSilent (2018-02-21 20:06 UTC)

<p>I tried patching it again, then importing.  I can’t see any problem on the patch log, but the import log says this</p>
<p>W: DcmItem: Non-standard VR ’  ’ (0a\00) encountered while parsing element (0004,1130), assuming 2 byte length field<br>
W: DcmItem: Non-standard VR ‘16’ (31\36) encountered while parsing element (5346,3959), assuming 2 byte length field<br>
W: DcmItem: Length of element (5346,3959) is odd<br>
W: DcmItem: Non-standard VR ’ 5’ (00\35) encountered while parsing element (0200,0000), assuming 2 byte length field<br>
W: DcmItem: Length of element (0200,0000) is odd<br>
W: DcmItem: Dataset not in ascending tag order, at element (0200,0000)<br>
W: DcmItem: Non-standard VR ‘CO’ (43\4f) encountered while parsing element (0000,4944), assuming 4 byte length field<br>
W: DcmItem: Length of element (0000,4944) is odd<br>
E: DcmElement: Unknown Tag &amp; Data (0000,4944) larger (808464467) than remaining bytes in file<br>
W: DcmItem: Dataset not in ascending tag order, at element (0000,4944)</p>

---

## Post #10 by @lassoan (2018-02-21 22:05 UTC)

<p>This seems like an invalid/corrupted DICOM file. What did produce this file?</p>

---

## Post #11 by @MSilent (2018-02-22 07:56 UTC)

<p>It was produced by DICOM patcher</p>

---

## Post #12 by @MSilent (2018-02-22 08:06 UTC)

<p>There were no error messages on the patched files.  The problem came when I tried to load it.</p>

---

## Post #13 by @lassoan (2018-02-22 19:35 UTC)

<aside class="quote no-group" data-username="MSilent" data-post="11" data-topic="2109" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/eb8c5e/48.png" class="avatar"> MSilent:</div>
<blockquote>
<p>It was produced by DICOM patcher</p>
</blockquote>
</aside>
<p>Where does the original data comes from (that you feed into DICOM patcher)?<br>
The DICOM patcher should not introduce those invalid tags that are reported to be found when you try to import the data.</p>
<p>You can also try all 3 available DICOM parsers (GDCM, DCMTK, archetype) and see if any of them is insensitive to the presence of invalid tags.</p>

---

## Post #14 by @MSilent (2018-02-22 19:38 UTC)

<p>I’ve also tried to delete data sets from DICOM browser and it’s not letting me delete those.  I try REMOVE or DELETE and neither works.<br>
It seems to be DICOM browser that I’m specifically having problems with</p>

---

## Post #15 by @lassoan (2018-02-22 19:58 UTC)

<p>If you have trouble deleting the DICOM database content then you can clear the DICOM database folder or choose an empty folder (DICOM browser, &gt;&gt; icon in the top-right, <code>LocalDatabase</code>).</p>

---

## Post #16 by @MSilent (2018-02-22 20:31 UTC)

<p>I rebooted the computer and that has fixed a lot of the problems.  I’m guessing there was a background process going on.  Thanks for the help</p>

---
