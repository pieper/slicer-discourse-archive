# I can't use TCIA BROWSER

**Topic ID**: 15272
**Date**: 2020-12-29
**URL**: https://discourse.slicer.org/t/i-cant-use-tcia-browser/15272

---

## Post #1 by @Anonymous1 (2020-12-29 15:03 UTC)

<p>Hi,<br>
I’m trying to use TCIA BROWSER, but slicer doesn’t let me.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba6c5b92d88ef85a83aa7f098218d98cd7190f35.jpeg" data-download-href="/uploads/short-url/qBaXOMSZWGXPhdvin9KlnVFVPTL.jpeg?dl=1" title="Captura de pantalla 2020-12-29 a las 9.45.29" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/ba6c5b92d88ef85a83aa7f098218d98cd7190f35_2_690x365.jpeg" alt="Captura de pantalla 2020-12-29 a las 9.45.29" data-base62-sha1="qBaXOMSZWGXPhdvin9KlnVFVPTL" width="690" height="365" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/ba6c5b92d88ef85a83aa7f098218d98cd7190f35_2_690x365.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/ba6c5b92d88ef85a83aa7f098218d98cd7190f35_2_1035x547.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/ba6c5b92d88ef85a83aa7f098218d98cd7190f35_2_1380x730.jpeg 2x" data-dominant-color="2F2E31"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de pantalla 2020-12-29 a las 9.45.29</span><span class="informations">2866×1520 311 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
This is the error that gives, how can I solve it?</p>
<p>Thank you!</p>

---

## Post #2 by @pieper (2020-12-29 15:31 UTC)

<p>Can you provide the whole error log?</p>
<p>Instructions are here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Report_a_problem">https://www.slicer.org/wiki/Documentation/Nightly/Report_a_problem</a></p>

---

## Post #3 by @Anonymous1 (2020-12-29 15:58 UTC)

<p>[DEBUG][Qt] 29.12.2020 16:50:43 [] (unknown:0) - Session start time …: 2020-12-29 16:50:43<br>
[DEBUG][Qt] 29.12.2020 16:50:43 [] (unknown:0) - Slicer version …: 4.13.0-2020-12-25 (revision 29542 / 210e827) macosx-amd64 - installed release<br>
[DEBUG][Qt] 29.12.2020 16:50:43 [] (unknown:0) - Operating system …: macOS / 11.0.1 / 20B50 - 64-bit<br>
[DEBUG][Qt] 29.12.2020 16:50:43 [] (unknown:0) - Memory …: 8192 MB physical, 1024 MB virtual<br>
[DEBUG][Qt] 29.12.2020 16:50:43 [] (unknown:0) - CPU …: GenuineIntel Intel® Core™ i5-7267U CPU @ 3.10GHz, 2 cores, 4 logical processors<br>
[DEBUG][Qt] 29.12.2020 16:50:43 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, Sequential threading<br>
[DEBUG][Qt] 29.12.2020 16:50:43 [] (unknown:0) - Qt configuration …: version 5.15.1, with SSL, requested OpenGL 3.2 (core profile)<br>
[DEBUG][Qt] 29.12.2020 16:50:43 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 29.12.2020 16:50:43 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 29.12.2020 16:50:43 [] (unknown:0) - Application path …: /Applications/Slicer.app/Contents/MacOS<br>
[DEBUG][Qt] 29.12.2020 16:50:43 [] (unknown:0) - Additional module paths …: /Applications/Slicer.app/Contents/Extensions-29542/TCIABrowser/lib/Slicer-4.13/qt-scripted-modules<br>
[WARNING][Qt] 29.12.2020 16:50:45 [] (unknown:0) - Populating font family aliases took 1313 ms. Replace uses of missing font family “.SF NS Text” with one that exists to avoid this cost.<br>
[DEBUG][Python] 29.12.2020 16:50:47 [Python] (/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/pydicom/datadict.py:432) - Reversing DICOM dictionary so can look up tag from a keyword…<br>
[DEBUG][Python] 29.12.2020 16:50:49 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.13/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 29.12.2020 16:50:49 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.13/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 29.12.2020 16:50:49 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.13/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 29.12.2020 16:50:49 [] (unknown:0) - Switch to module:  “Welcome”<br>
[DEBUG][Qt] 29.12.2020 16:51:01 [] (unknown:0) - Switch to module:  “TCIABrowser”<br>
[DEBUG][Qt] 29.12.2020 16:51:01 [] (unknown:0) - ctkDICOMModelPrivate::generateQuery: query is: SELECT UID as UID, PatientsName as Name, PatientsAge as Age, PatientsBirthDate as Date, PatientID as “Subject ID” FROM Patients ORDER BY “Name” DESC<br>
[DEBUG][Qt] 29.12.2020 16:51:01 [] (unknown:0) - ctkDICOMModelPrivate::updateQueries for Root: query is: SELECT UID as UID, PatientsName as Name, PatientsAge as Age, PatientsBirthDate as Date, PatientID as “Subject ID” FROM Patients ORDER BY “Name” DESC<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[DEBUG][Qt] 29.12.2020 16:51:01 [] (unknown:0) - SQL failed<br>
Bad SQL: SELECT Version from SchemaInfo;<br>
[DEBUG][Qt] 29.12.2020 16:51:01 [] (unknown:0) - Error text:<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[DEBUG][Qt] 29.12.2020 16:51:01 [] (unknown:0) - SQL failed<br>
Bad SQL: SELECT Filename from Images;<br>
[DEBUG][Qt] 29.12.2020 16:51:01 [] (unknown:0) - Error text:<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[DEBUG][Qt] 29.12.2020 16:51:01 [] (unknown:0) - SQL failed<br>
Bad SQL: DROP TABLE IF EXISTS ‘SchemaInfo’;<br>
[DEBUG][Qt] 29.12.2020 16:51:01 [] (unknown:0) - Error text:<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[WARNING][Qt] 29.12.2020 16:51:01 [] (unknown:0) - QSqlQuery::exec: database not open<br>
[DEBUG][Qt] 29.12.2020 16:51:01 [] (unknown:0) - SQL failed<br>
Bad SQL: SELECT SOPInstanceUID, SeriesInstanceUID FROM Images WHERE DisplayedFieldsUpdatedTimestamp IS NULL;<br>
[DEBUG][Qt] 29.12.2020 16:51:01 [] (unknown:0) - Error text:<br>
[CRITICAL][Stream] 29.12.2020 16:51:01 [] (unknown:0) - Traceback (most recent call last):<br>
[CRITICAL][Stream] 29.12.2020 16:51:01 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/Extensions-29542/TCIABrowser/lib/Slicer-4.13/qt-scripted-modules/TCIABrowser.py”, line 95, in <strong>init</strong><br>
[CRITICAL][Stream] 29.12.2020 16:51:01 [] (unknown:0) -     os.makedirs(self.storagePath)<br>
[CRITICAL][Stream] 29.12.2020 16:51:01 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/bin/…/lib/Python/lib/python3.6/os.py”, line 210, in makedirs<br>
[CRITICAL][Stream] 29.12.2020 16:51:02 [] (unknown:0) -     makedirs(head, mode, exist_ok)<br>
[CRITICAL][Stream] 29.12.2020 16:51:02 [] (unknown:0) -   File “/Applications/Slicer.app/Contents/bin/…/lib/Python/lib/python3.6/os.py”, line 220, in makedirs<br>
[CRITICAL][Stream] 29.12.2020 16:51:02 [] (unknown:0) -     mkdir(name, mode)<br>
[CRITICAL][Stream] 29.12.2020 16:51:02 [] (unknown:0) - OSError: [Errno 30] Read-only file system: ‘./ctkDICOM-Database’<br>
[CRITICAL][Qt] 29.12.2020 16:51:02 [] (unknown:0) - qSlicerPythonCppAPI::instantiateClass  - [ “TCIABrowserWidget” ] - Failed to instantiate scripted pythonqt class “TCIABrowserWidget” 0x7f800b2c05f8<br>
[DEBUG][Qt] 29.12.2020 16:51:02 [] (unknown:0) - Warning, the module  “TCIABrowser” has no widget representation<br>
[DEBUG][Qt] 29.12.2020 16:51:02 [] (unknown:0) - Warning, there is no UI for the module “TCIABrowser”</p>

---

## Post #4 by @Anonymous1 (2020-12-29 16:00 UTC)

<p>This is the error log</p>

---

## Post #5 by @lassoan (2020-12-29 19:10 UTC)

<p>TCIA module needs Slicer to have a valid DICOM database. Switch to DICOM module to create and initialize the database (you just need to do it once after you install Slicer on your computer).</p>

---
