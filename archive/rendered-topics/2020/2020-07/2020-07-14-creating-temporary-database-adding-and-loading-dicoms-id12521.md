---
topic_id: 12521
title: "Creating Temporary Database Adding And Loading Dicoms"
date: 2020-07-14
url: https://discourse.slicer.org/t/12521
---

# Creating temporary database, adding and loading Dicoms

**Topic ID**: 12521
**Date**: 2020-07-14
**URL**: https://discourse.slicer.org/t/creating-temporary-database-adding-and-loading-dicoms/12521

---

## Post #1 by @sogo (2020-07-14 07:05 UTC)

<p>I have a question regarding creating temporary database, I got the script from ‘ScriptRepository’ of creating temporary database and loading DICOMs to slicer " <strong>How to load DICOM files into the scene from a folder</strong>" . My issue is that when I populates the database using “importDicom” function, the database is still empty. I’m working on c++ loadable module in which I want to load DICOM files into temporary database and as loader is python based module, I have to process python script in c++. Here is what this code looks like:</p>
<blockquote>
<p>PythonQt::init();<br>
PythonQtObjectPtr context = PythonQt::self()-&gt;getMainModule();<br>
context.addVariable(“folderName”, d-&gt;folderName);<br>
context.evalScript(QString(“import os,sys,slicer,random\n”<br>
“from pathlib import Path\n”<br>
“dicomDataDir=folderName\n”<br>
“directory=‘TEMP’\n”<br>
“from DICOMLib import DICOMUtils\n”<br>
“with DICOMUtils.TemporaryDICOMDatabase(directory) as db:\n”<br>
" DICOMUtils.clearDatabase(db)\n"<br>
" DICOMUtils.importDicom(dicomDataDir, db)\n"<br>
" patientUIDs = db.patients()\n"<br>
" for patientUID in patientUIDs:\n"<br>
"  DICOMUtils.loadPatientByUID(patientUID)"));</p>
</blockquote>
<p>The above code is called on click of button and “folderName” variable has all the dicom files. When this evalScript is done, in separate function in c++, I’m opening the database using following code but it shows empty output for patientsUIDs:</p>
<blockquote>
<pre><code>ctkDICOMDatabase *data;
data-&gt;openDatabase("/tmp/SlicerCAT-user/TEMP/ctkDICOM.sql"); //This is where temporary database is
QStringList patients = data-&gt;patients();
qDebug() &lt;&lt; "Patients UIDs" &lt;&lt; patients;
qDebug() &lt;&lt; "StudyList" &lt;&lt; data-&gt;studiesForPatient(patients[0]);
</code></pre>
</blockquote>
<p>My question is that does the temporary database is cleared automatically when “evalScript” is run and finishes. During evalScript, I printed the studyList of loaded Dicoms and it shows correct output.</p>

---

## Post #2 by @lassoan (2020-07-14 13:41 UTC)

<p>Loading data into Slicer’s persistent DICOM database is even simpler: replace</p>
<pre><code>with DICOMUtils.TemporaryDICOMDatabase() as db
</code></pre>
<p>by this:</p>
<pre><code>db = slicer.dicomDatabase
</code></pre>
<p>Alternatively, you can use this code snippet to import:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_import_DICOM_files_into_the_application.27s_DICOM_database" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_import_DICOM_files_into_the_application.27s_DICOM_database</a></p>

---

## Post #3 by @sogo (2020-07-15 23:24 UTC)

<p>So there is no definite way to make persistent temporary database. I think temporary is not a good word to describe what I’m looking for. I am looking for a separate database for my application at my given location directory, separate from slicer’s default database. I was thinking of creating temporary database and using ctkDicomIndexer to populate and ctkDicomDatabase to open it. Sorry for late response, I was just figuring somethings out</p>

---

## Post #4 by @pieper (2020-07-15 23:55 UTC)

<p>You can pick any database directory you want and tell Slicer to use it.  If you want the user to have their own config, you just need to remember to set if back if to their setting after they use your module.  The temporary dicom database utilities are handy because they do that cleanup for you automatically after a transient operation.</p>

---

## Post #6 by @lassoan (2023-09-14 19:56 UTC)

<p>A post was split to a new topic: <a href="/t/finding-a-dicom-series-based-on-series-description/31726">Finding a DICOM series based on series description</a></p>

---
