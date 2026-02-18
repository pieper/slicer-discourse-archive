# Using the XNATSlicer plugin

**Topic ID**: 3261
**Date**: 2018-06-21
**URL**: https://discourse.slicer.org/t/using-the-xnatslicer-plugin/3261

---

## Post #1 by @ernandez.santos (2018-06-21 18:54 UTC)

<p>Dear</p>
<p>I really want to use the XNATSlicer plugin, although I can not perform the integration through 3D Slicer 4.8.1, it complains the error below.<br>
I believe I stopped making some steps on the server or on my local machine, do I need to install some library on the server?</p>
<p>Hugs</p>
<p>Ernanez</p>
<pre><code>Python 2.7.13 (default, Dec 20 2017, 00:45:45) [MSC v.1800 64 bit (AMD64)] on win32
&gt;&gt;&gt; 
Traceback (most recent call last):
  File "C:/Users/HU/AppData/Roaming/NA-MIC/Extensions-26813/XNATSlicer/lib/Slicer-4.8/qt-scripted-modules/XnatSlicer.py", line 925, in onLoginButtonClicked
    self.beginXnat()
  File "C:/Users/HU/AppData/Roaming/NA-MIC/Extensions-26813/XNATSlicer/lib/Slicer-4.8/qt-scripted-modules/XnatSlicer.py", line 577, in beginXnat
    self.View.begin()
  File "C:\Users\HU\AppData\Roaming\NA-MIC\Extensions-26813\XNATSlicer\lib\Slicer-4.8\qt-scripted-modules\XnatSlicerLib\ui\View.py", line 111, in begin
    "'HOST_NAME' (HOST_URL):\n%s" %(str(e)))
  File "C:\Users\HU\AppData\Roaming\NA-MIC\Extensions-26813\XNATSlicer\lib\Slicer-4.8\qt-scripted-modules\XnatSlicerLib\ui\View.py", line 150, in showError
    msg.replace('HOST_NAME', hostName).\
UnicodeDecodeError: 'ascii' codec can't decode byte 0xe3 in position 68: ordinal not in range(128)</code></pre>

---

## Post #2 by @lassoan (2018-06-21 18:56 UTC)

<p>It seems that your computer name has special characters in it. Rename your computer to only contain ASCII characters and try again.</p>

---

## Post #3 by @ernandez.santos (2018-06-21 19:49 UTC)

<p>Hi Iasssoan</p>
<p>What exactly would “HOST_NAME” be my user, my domain?<br>
in both cases it has no special character is admin and pacspesquisa.unifesp.br is my domain</p>

---

## Post #4 by @lassoan (2018-06-21 20:10 UTC)

<p>Host name is the name of the computer. It is not the same as name of user or domain.</p>
<p>I don’t know how much the XNat extension is used anymore. <a href="http://girder.readthedocs.io/en/latest/">Girder</a> is a new data management platform that Kitware is actively developing that you might consider as well.</p>

---

## Post #5 by @fedorov (2018-06-22 02:25 UTC)

<p><a class="mention" href="/u/ernandez.santos">@ernandez.santos</a> I was going to suggest that you ask on the XNAT forum, but I see you already did here: <a href="https://groups.google.com/d/topic/xnat_discussion/iPDAXWZ0jms/discussion">https://groups.google.com/d/topic/xnat_discussion/iPDAXWZ0jms/discussion</a>. Based on the lack of responses, it could be that this extension is no longer supported by the XNAT team.</p>

---

## Post #6 by @Saima (2024-03-08 01:20 UTC)

<p>Hi Andras,<br>
i was able to connect properly to the xnat and its showing me the data in the left window but when I try to load one of the data into slicer window on the right its giving me error as follow:</p>
<p>[Qt] QSqlQuery::prepare: database not open<br>
[Qt] SQL failed:<br>
[Qt]<br>
[Qt] Error:<br>
[Qt] No query Unable to fetch row<br>
[Qt] Failed to find patient with PatientsName=APT240 and PatientID=APT240<br>
[Qt] Failed to find patient for SOP Instance UID = 1.3.46.670589.11.42221.5.0.8048.2022112109125589081<br>
[Qt] Failed to find patient with PatientsName=APT240 and PatientID=APT240<br>
[Qt] Failed to find patient for SOP Instance UID = 1.3.46.670589.11.42221.5.0.8048.2022112109090012081<br>
[Qt] Failed to find patient with PatientsName=APT240 and PatientID=APT240<br>
[Qt] Failed to find patient for SOP Instance UID = 1.3.46.670589.11.42221.5.0.8048.2022112109082171394<br>
[Qt] Failed to find patient with PatientsName=APT240 and PatientID=APT240<br>
[Qt] Failed to find patient for SOP Instance UID = 1.3.46.670589.11.42221.5.0.8048.2022112109134992983<br>
[Qt] Failed to find patient with PatientsName=APT240 and PatientID=APT240<br>
[Qt] Failed to find patient for SOP Instance UID = 1.3.46.670589.11.42221.5.0.8048.2022112109082131353<br>
[Qt] Required information (patient name, patient ID, study instance UID) is missing from dataset<br>
[Qt] Failed to find patient with PatientsName=APT240 and PatientID=APT240<br>
[Qt] Failed to find patient for SOP Instance UID = 1.3.46.670589.11.42221.5.0.8048.2022112109132302540<br>
[Qt] Required information (patient name, patient ID, study instance UID) is missing from dataset<br>
[Qt] Required information (patient name, patient ID, study instance UID) is missing from dataset<br>
[Qt] Required information (patient name, patient ID, study instance UID) is missing from dataset<br>
[Qt] Required information (patient name, patient ID, study instance UID) is missing from dataset<br>
[Qt] Required information (patient name, patient ID, study instance UID) is missing from dataset<br>
[Qt] Required information (patient name, patient ID, study instance UID) is missing from dataset<br>
[Qt] Required information (patient name, patient ID, study instance UID) is missing from dataset<br>
[Qt] Required information (patient name, patient ID, study instance UID) is missing from dataset<br>
[Qt] Failed to find patient with PatientsName= and PatientID=<br>
Traceback (most recent call last):<br>
File “/home/useradmin/Downloads/Slicer-5.7.0-2024-02-06-linux-amd64/slicer.org/Extensions-32706/XNATSlicer/lib/Slicer-5.7/qt-scripted-modules/XnatSlicerLib/io/Workflow_Load.py”, line 225, in __clearSceneButtonClicked<br>
self.beginWorkflow()<br>
File “/home/useradmin/Downloads/Slicer-5.7.0-2024-02-06-linux-amd64/slicer.org/Extensions-32706/XNATSlicer/lib/Slicer-5.7/qt-scripted-modules/XnatSlicerLib/io/Workflow_Load.py”, line 317, in beginWorkflow<br>
self.MODULE.XnatIo.startDownloadQueue()<br>
File “/home/useradmin/Downloads/Slicer-5.7.0-2024-02-06-linux-amd64/slicer.org/Extensions-32706/XNATSlicer/lib/Slicer-5.7/qt-scripted-modules/XnatSlicerLib/ext/Xnat/Xnat.py”, line 681, in startDownloadQueue<br>
self.runEventCallbacks(‘downloadQueueFinished’)<br>
File “/home/useradmin/Downloads/Slicer-5.7.0-2024-02-06-linux-amd64/slicer.org/Extensions-32706/XNATSlicer/lib/Slicer-5.7/qt-scripted-modules/XnatSlicerLib/ext/Xnat/Xnat.py”, line 617, in runEventCallbacks<br>
callback(*args)<br>
File “/home/useradmin/Downloads/Slicer-5.7.0-2024-02-06-linux-amd64/slicer.org/Extensions-32706/XNATSlicer/lib/Slicer-5.7/qt-scripted-modules/XnatSlicerLib/io/Workflow_Load.py”, line 283, in onDownloadFinished<br>
loader.load()<br>
File “/home/useradmin/Downloads/Slicer-5.7.0-2024-02-06-linux-amd64/slicer.org/Extensions-32706/XNATSlicer/lib/Slicer-5.7/qt-scripted-modules/XnatSlicerLib/io/Loader_Dicom.py”, line 169, in load<br>
return self.loadDicomsFromDatabase(self.extractedFiles)<br>
File “/home/useradmin/Downloads/Slicer-5.7.0-2024-02-06-linux-amd64/slicer.org/Extensions-32706/XNATSlicer/lib/Slicer-5.7/qt-scripted-modules/XnatSlicerLib/io/Loader_Dicom.py”, line 223, in loadDicomsFromDatabase<br>
loadables = dicomScalarVolumePlugin.examine([matchedDatabaseFiles])<br>
File “/home/useradmin/Downloads/Slicer-5.7.0-2024-02-06-linux-amd64/lib/Slicer-5.7/qt-scripted-modules/DICOMLib/DICOMPlugin.py”, line 157, in examine<br>
return self.examineForImport(fileList)<br>
File “/home/useradmin/Downloads/Slicer-5.7.0-2024-02-06-linux-amd64/bin/…/lib/Slicer-5.7/qt-scripted-modules/DICOMScalarVolumePlugin.py”, line 166, in examineForImport<br>
loadablesForFiles = self.examineFiles(files)<br>
File “/home/useradmin/Downloads/Slicer-5.7.0-2024-02-06-linux-amd64/bin/…/lib/Slicer-5.7/qt-scripted-modules/DICOMScalarVolumePlugin.py”, line 193, in examineFiles<br>
seriesUID = slicer.dicomDatabase.fileValue(files[0], self.tags[“seriesUID”])<br>
IndexError: list index out of range<br>
[Qt] QSqlQuery::prepare: database not open</p>
<p>what could be the reason. for every data i try to load i get the same error.</p>
<p>thank you</p>
<p>regards,<br>
Saima</p>

---

## Post #7 by @lassoan (2024-03-08 01:48 UTC)

<p>Please go to the DICOM module and check that the DICOM database has been created (no yellow message is shown near the top-right of the Slicer application window.</p>

---

## Post #8 by @Saima (2024-03-08 02:22 UTC)

<p>yup did it. Its running perfectly fine. thanks alot</p>

---
