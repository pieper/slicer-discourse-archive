---
topic_id: 204
title: "Why I Can Not Import Dicom"
date: 2017-04-27
url: https://discourse.slicer.org/t/204
---

# Why I can not import DICOM?

**Topic ID**: 204
**Date**: 2017-04-27
**URL**: https://discourse.slicer.org/t/why-i-can-not-import-dicom/204

---

## Post #1 by @ShyhjenWang (2017-04-27 02:06 UTC)

<p>I try to import a series of DICOM data, but fail.<br>
It shows 0 new patients, 0 studies, …<br>
However, others can import the series with MIMICs.</p>

---

## Post #2 by @lassoan (2017-04-27 02:10 UTC)

<ol>
<li>Use the latest nightly version of Slicer.</li>
<li>Use <code>DICOM Patcher</code> module to fix the DICOM files: Set the input directory to the location where your DICOM files are stored, set the output directory to another directory where the fixed, valid DICOM files will be stored (make sure the directory path doesn’t contain any special characters), click Patch, click Import, and then load the data using the DICOM module.</li>
</ol>

---

## Post #3 by @ShyhjenWang (2017-04-27 03:51 UTC)

<p>Sorry, where to get the DICOM patcher module?</p>

---

## Post #4 by @lassoan (2017-04-27 12:15 UTC)

<p>It’s in Slicer, in the module list, Utilities category.</p>

---

## Post #5 by @carba86 (2018-01-17 00:15 UTC)

<p>I am having the same problem. No way to fix it so far.  Tried Nightly version as well as DICOM patcher with no success.</p>

---

## Post #6 by @lassoan (2018-01-17 00:43 UTC)

<p>What device was used to acquire the image?</p>

---

## Post #7 by @carba86 (2018-01-17 01:31 UTC)

<p>GE Discovery 750 3T magnet. Ive tríed with MRIs from the Cancer Archive<br>
Imaging as …well</p>
<p>escribió:</p>

---

## Post #8 by @lassoan (2018-01-17 01:37 UTC)

<p>Great, this is very useful information. Most likely your DICOM database directory is not set correctly. To confirm this, could you copy-paste here the application log of a failed DICOM import? (log is available in menu: Help / Report a bug)</p>

---

## Post #9 by @carba86 (2018-01-17 01:56 UTC)

<p>[WARNING][Python] 16.01.2018 22:52:33 [Python] (/private/var/folders/wm/7t6787qs7kb8fp5d8vjlvrnw0000gn/T/AppTranslocation/207F0FF5-0744-420D-8978-17417221E506/d/Slicer.app/Contents/bin/Python/slicer/util.py:955) - The database file path “/Users/leacarballo/Documents/SlicerDICOMDatabase/ctkDICOM.sql” cannot be used.  Directory is not empty and not an existing DICOM database.<br>
Please pick a different database directory using the LocalDatabase button in the DICOM Browser<br>
[DEBUG][Qt] 16.01.2018 22:52:33 [] (unknown:0) - Switch to module:  “DICOM”<br>
[CRITICAL][Stream] 16.01.2018 22:52:33 [] (unknown:0) - The database file path “/Users/leacarballo/Documents/SlicerDICOMDatabase/ctkDICOM.sql” cannot be used.  Directory is not empty and not an existing DICOM database.<br>
[CRITICAL][Stream] 16.01.2018 22:52:33 [] (unknown:0) - Please pick a different database directory using the LocalDatabase button in the DICOM Browser<br>
[CRITICAL][FD] 16.01.2018 22:52:41 [] (unknown:0) - 2018-01-16 22:52:41.135 Slicer[593:70579] modalSession has been exited prematurely - check for a reentrant call to endModalSession:<br>
[WARNING][Qt] 16.01.2018 22:52:41 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[DEBUG][Qt] 16.01.2018 22:52:41 [] (unknown:0) - SQL failed<br>
Bad SQL: SELECT Version from SchemaInfo;<br>
[DEBUG][Qt] 16.01.2018 22:52:41 [] (unknown:0) - Error text:<br>
[WARNING][Qt] 16.01.2018 22:52:41 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[DEBUG][Qt] 16.01.2018 22:52:41 [] (unknown:0) - SQL failed<br>
Bad SQL: CREATE TABLE IF NOT EXISTS main.Filenames_backup (Filename TEXT PRIMARY KEY NOT NULL )<br>
[DEBUG][Qt] 16.01.2018 22:52:41 [] (unknown:0) - Error text:<br>
[WARNING][Qt] 16.01.2018 22:52:41 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[DEBUG][Qt] 16.01.2018 22:52:41 [] (unknown:0) - SQL failed<br>
Bad SQL: INSERT INTO Filenames_backup SELECT Filename FROM Images;<br>
[DEBUG][Qt] 16.01.2018 22:52:41 [] (unknown:0) - Error text:<br>
[WARNING][Qt] 16.01.2018 22:52:41 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[DEBUG][Qt] 16.01.2018 22:52:41 [] (unknown:0) - SQL failed<br>
Bad SQL: DROP TABLE IF EXISTS ‘SchemaInfo’;<br>
[DEBUG][Qt] 16.01.2018 22:52:41 [] (unknown:0) - Error text:<br>
[WARNING][Qt] 16.01.2018 22:52:41 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 16.01.2018 22:52:41 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 16.01.2018 22:52:41 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 16.01.2018 22:52:41 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 16.01.2018 22:52:41 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 16.01.2018 22:52:41 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 16.01.2018 22:52:41 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 16.01.2018 22:52:41 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 16.01.2018 22:52:41 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 16.01.2018 22:52:41 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 16.01.2018 22:52:41 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 16.01.2018 22:52:41 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 16.01.2018 22:52:41 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 16.01.2018 22:52:41 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 16.01.2018 22:52:41 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 16.01.2018 22:52:41 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 16.01.2018 22:52:41 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 16.01.2018 22:52:41 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 16.01.2018 22:52:41 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 16.01.2018 22:52:41 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 16.01.2018 22:52:41 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 16.01.2018 22:52:41 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[DEBUG][Qt] 16.01.2018 22:52:41 [] (unknown:0) - SQL failed<br>
Bad SQL: SELECT Filename from Filenames_backup ;<br>
[DEBUG][Qt] 16.01.2018 22:52:41 [] (unknown:0) - Error text:<br>
[WARNING][Qt] 16.01.2018 22:52:41 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[DEBUG][Qt] 16.01.2018 22:52:41 [] (unknown:0) - SQL failed<br>
Bad SQL: DROP TABLE main.Filenames_backup;<br>
[DEBUG][Qt] 16.01.2018 22:52:41 [] (unknown:0) - Error text:<br>
[WARNING][Qt] 16.01.2018 22:52:41 [] (unknown:0) - QSqlQuery::prepare: database not open<br>
[WARNING][Qt] 16.01.2018 22:52:58 [] (unknown:0) - QSqlQuery::prepare: database not open<br>
[DEBUG][Qt] 16.01.2018 22:52:58 [] (unknown:0) - SQL failed<br>
Bad SQL:<br>
[DEBUG][Qt] 16.01.2018 22:52:58 [] (unknown:0) - Error text:  Parameter count mismatch<br>
[WARNING][Qt] 16.01.2018 22:52:58 [] (unknown:0) - QSqlQuery::prepare: database not open<br>
[CRITICAL][Qt] 16.01.2018 22:52:58 [] (unknown:0) - SQLITE ERROR: Parameter count mismatch<br>
[WARNING][Qt] 16.01.2018 22:52:58 [] (unknown:0) - QSqlQuery::prepare: database not open<br>
[DEBUG][Qt] 16.01.2018 22:52:58 [] (unknown:0) - SQL failed</p>

---

## Post #10 by @lassoan (2018-01-17 02:11 UTC)

<p>This log message describes the problem and suggested solution:</p>
<aside class="quote no-group" data-username="carba86" data-post="9" data-topic="204">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/carba86/48/3943_2.png" class="avatar"> carba86:</div>
<blockquote>
<p>The database file path “/Users/leacarballo/Documents/SlicerDICOMDatabase/ctkDICOM.sql” cannot be used.  Directory is not empty and not an existing DICOM database.</p>
<p>Please pick a different database directory using the LocalDatabase button in the DICOM Browser</p>
</blockquote>
</aside>
<p>Please set an empty folder for DICOM database that you have write access to, try DICOM import again, and let us know if it fixed the DICOM importing.</p>

---

## Post #11 by @timeanddoctor (2018-01-17 12:15 UTC)

<p>If the system language is Chinese, the folder name of DICOM files should be named by English.<br>
I think this problem will be fixed in the futrue.</p>

---

## Post #12 by @carba86 (2018-01-17 12:44 UTC)

<p>Thank you Andras, you were right…it was the DICOM database directory indeed. I appreciate your help.</p>

---

## Post #13 by @Syed_Faiz_Ali (2019-02-16 14:20 UTC)

<p>Simply, just copy/cut the dcm file folder to some other location. It will work just fine… it did work fine in my case.</p>

---

## Post #14 by @markyang19 (2020-02-21 12:34 UTC)

<p>I have the same problem. After changing the folder name from Chinese to English, this problem was fixed.</p>

---

## Post #15 by @lassoan (2020-02-21 14:49 UTC)

<p>Starting from today, Slicer Preview Release (revision 28783) should be able to import DICOM files from any folder. See announcement and more details here: <a href="https://discourse.slicer.org/t/special-characters-in-filenames-and-strings-are-now-allowed/10375" class="inline-onebox">Special characters in filenames and strings are now allowed</a></p>
<p>It is all very new and probably it will take a while to get all problems ironed out, but it should work.</p>

---

## Post #16 by @Pablo_Montes (2020-05-12 20:02 UTC)

<p>Hi. I also have an internal error while loading dicom<br>
The message detail is:<br>
Exception thrown in event: calling methods on uninitialized ctkDICOMItem</p>
<p>Any suggestions? Thanks</p>

---

## Post #17 by @lassoan (2020-05-12 20:05 UTC)

<p>Could you please try with the latest Slicer Preview Release?</p>

---

## Post #18 by @Varsha (2021-03-10 06:41 UTC)

<p>I am facing a similar problem importing DICOM files. The message displayed is import completed: 0 patients, 0 studies. I tried installing quantitative reporting as well as copying the images to another folder but both don’t seem to be working. Even DICOM patcher is not solving the issue at hand. How can I load the images?</p>

---

## Post #19 by @lassoan (2021-03-11 04:16 UTC)

<p>Please follow <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#i-try-to-import-a-directory-of-dicom-files-but-nothing-shows-up-in-the-browser">these instructions</a>.</p>

---

## Post #20 by @Julien_D (2023-06-02 20:56 UTC)

<p>Hi, I had a similar problem (imported 0 new patient, 0 new studies) but copying/pasting all the dcm files in a new folder seems to have solved the issue. I can’t share the log because it shows the patient’s name in some places but I’ll gladly provide more info if needed.</p>

---

## Post #21 by @lassoan (2023-06-02 23:26 UTC)

<aside class="quote no-group" data-username="Julien_D" data-post="20" data-topic="204">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/julien_d/48/66125_2.png" class="avatar"> Julien_D:</div>
<blockquote>
<p>copying/pasting all the dcm files in a new folder seems to have solved the issue</p>
</blockquote>
</aside>
<p>Sounds like the original folder contained special characters in the name, was too long overall path, or was a virtual file system (google, box, etc. virtual drive).</p>

---
