---
topic_id: 10453
title: "Internal Error Pop Up When Importing Dicom Data"
date: 2020-02-27
url: https://discourse.slicer.org/t/10453
---

# Internal error pop-up when importing DICOM data

**Topic ID**: 10453
**Date**: 2020-02-27
**URL**: https://discourse.slicer.org/t/internal-error-pop-up-when-importing-dicom-data/10453

---

## Post #1 by @Patrick (2020-02-27 04:29 UTC)

<p>Hi,</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6ca53e2aa5e19a11b56408f3e296f816510a5d7b.png" alt="Internal Error" data-base62-sha1="fv7B4xOVYCX8oOHWGVkrSz5JuLp" width="519" height="248"></p>
<p>I am currently trying to import a DICOM file into the program through “Import DICOM files from directory”. Once I have located the file and clicked “Import” the above image appears. This is my first time using the software. Any help is appreciated.</p>
<p>Thanks</p>

---

## Post #2 by @fedorov (2020-02-27 04:33 UTC)

<p>Here are couple of possible common issues:</p>
<ul>
<li>Can you check the folder chosen as location for your DICOM database is writeable?</li>
<li>Can you import some public DICOM dataset that is known to work? (for example, you can try importing the files from <a href="https://github.com/Slicer/Slicer/tree/master/Testing/Data/Input/CTHeadAxialDicom">this directory</a> and see if you still have the crash)</li>
<li>Can you try applying <a href="https://slicer.readthedocs.io/en/latest/user_guide/module_dicompatcher.html">DICOMPatcher</a> to your DICOM dataset before trying to import it?</li>
</ul>

---

## Post #3 by @lassoan (2020-02-27 16:12 UTC)

<p>A post was split to a new topic: <a href="/t/dicom-import-can-be-attempted-before-creating-database/10459">DICOM import can be attempted before creating database</a></p>

---

## Post #4 by @lassoan (2020-02-27 16:13 UTC)

<p>Please try with latest Slicer Preview Release and let us know if you still encounter any issues.</p>

---

## Post #5 by @Patrick (2020-03-04 02:34 UTC)

<p>Hi Andras,</p>
<p>Thank you for your reply and suggestion. I downloaded the Preview Release and dragged the folder in, but nothing appears. It also says no valid DICOM database found in folder.</p>

---

## Post #6 by @lassoan (2020-03-04 02:45 UTC)

<p>Go to DICOM module and click “Create new database” before attempting to import anything.</p>

---

## Post #7 by @muratmaga (2020-03-04 02:54 UTC)

<p>I think this will come up more and more as that message is really quite obscure. I still propose to disable out the import tab until database initialized (or auto create the database first time DICOM module is run).</p>

---

## Post #8 by @Patrick (2020-03-04 06:44 UTC)

<p>I’ve clicked “Create new database” but nothing else happens when I try to import.</p>

---

## Post #9 by @lassoan (2020-03-04 12:18 UTC)

<p>You can find messages about why file s are not imported in the application log (menu: Help / Report a bug). Could you upload it somewhere and post the link here?</p>

---

## Post #10 by @lassoan (2020-03-04 14:41 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="7" data-topic="10453" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I think this will come up more and more as that message is really quite obscure. I still propose to disable out the import tab until database initialized (or auto create the database first time DICOM module is run).</p>
</blockquote>
</aside>
<p>I’ve implemented automatic creation now: if no valid database is available when user drag-and-drops a folder or clicks the import button then a new database is created with default settings. If it fails (e.g., because Slicer cannot find a writeable folder) then an error message is displayed and the user is instructed to resolve the error using options shown in DICOM browser. This will be available in Slicer Preview Releases from tomorrow.</p>

---

## Post #11 by @Patrick (2020-03-05 03:44 UTC)

<p>Hi All,</p>
<p>Thank you for your replies and suggestions. I do have another one:</p>
<p>So I downloaded 3D Slicer onto two other workstations to see if it was going to be a recurring problem. When I drag-and-drop the files in, the images load fine (the DICOM browser window displays the correct BodyPartExamined - which for me is Abd; unlike previously where it would say HeadNeck for the same data set). Are there any suggestions as to why this is and how it can be fixed? (I can post this separately if need be)</p>
<p>Thank you and your help is much appreciated.</p>

---

## Post #12 by @lassoan (2020-03-05 05:14 UTC)

<p>From this much information we cannot even guess what behavior you see on your computers and why.</p>
<p>If you find that on any computer the latest Slicer Preview Release does not load any DICOM data correctly then send us anonymized/animal/phantom sample data (preferred) or at least send the application log of DICOM import and loading (menu: Help / Report a bug).</p>

---

## Post #13 by @Patrick (2020-03-05 05:31 UTC)

<p>[DEBUG][Qt] 05.03.2020 16:27:55 [] (unknown:0) - Session start time …: 2020-03-05 16:27:55<br>
[DEBUG][Qt] 05.03.2020 16:27:55 [] (unknown:0) - Slicer version …: 4.11.0-2020-03-01 (revision 28798) win-amd64 - installed release<br>
[DEBUG][Qt] 05.03.2020 16:27:55 [] (unknown:0) - Operating system …: Windows / 7 / (Build 7601, Code Page 1252) - 64-bit<br>
[DEBUG][Qt] 05.03.2020 16:27:55 [] (unknown:0) - Memory …: 8103 MB physical, 16205 MB virtual<br>
[DEBUG][Qt] 05.03.2020 16:27:55 [] (unknown:0) - CPU …: GenuineIntel , 4 cores, 4 logical processors<br>
[DEBUG][Qt] 05.03.2020 16:27:55 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, TBB threading<br>
[DEBUG][Qt] 05.03.2020 16:27:55 [] (unknown:0) - Qt configuration …: version 5.10.1, with SSL, requested OpenGL 3.2 (compatibility profile)<br>
[DEBUG][Qt] 05.03.2020 16:27:55 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 05.03.2020 16:27:55 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 05.03.2020 16:27:55 [] (unknown:0) - Application path …: C:/Users/z3461313/AppData/Local/NA-MIC/Slicer 4.11.0-2020-03-01/bin<br>
[DEBUG][Qt] 05.03.2020 16:27:55 [] (unknown:0) - Additional module paths …: (none)<br>
[DEBUG][Python] 05.03.2020 16:28:00 [Python] (C:\Users\z3461313\AppData\Local\NA-MIC\Slicer 4.11.0-2020-03-01\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 05.03.2020 16:28:01 [Python] (C:\Users\z3461313\AppData\Local\NA-MIC\Slicer 4.11.0-2020-03-01\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 05.03.2020 16:28:01 [Python] (C:\Users\z3461313\AppData\Local\NA-MIC\Slicer 4.11.0-2020-03-01\lib\Slicer-4.11\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 05.03.2020 16:28:01 [] (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 05.03.2020 16:28:24 [] (unknown:0) - Switch to module:  “DICOM”<br>
[CRITICAL][Stream] 05.03.2020 16:28:24 [] (unknown:0) - Database folder does not contain ctkDICOM.sql file: <a href="//INFPWFS219.ad.unsw.edu.au/Student038%24/z3461313/SlicerDICOMDatabase_8" rel="nofollow noopener">//INFPWFS219.ad.unsw.edu.au/Student038$/z3461313/SlicerDICOMDatabase_8</a><br>
[WARNING][Qt] 05.03.2020 16:28:25 [] (unknown:0) - QSqlQuery::prepare: database not open<br>
[DEBUG][Qt] 05.03.2020 16:28:25 [] (unknown:0) - SQL failed<br>
Bad SQL:<br>
[DEBUG][Qt] 05.03.2020 16:28:25 [] (unknown:0) - Error text: No query Unable to fetch row</p>

---

## Post #14 by @lassoan (2020-03-05 13:32 UTC)

<p>It seems that the database could not be created at the default location, because it was a virtual/network drive. Change the database location to a local folder that your user has write access to. It can even be a folder used for temporary files.</p>
<p>If you download today’s Slicer Preview Release then you should get an informative error popup about what is wrong and what you should do to fix it.</p>

---
