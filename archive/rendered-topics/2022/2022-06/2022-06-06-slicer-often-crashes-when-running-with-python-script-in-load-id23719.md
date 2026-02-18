# Slicer often crashes when running with python-script in loading

**Topic ID**: 23719
**Date**: 2022-06-06
**URL**: https://discourse.slicer.org/t/slicer-often-crashes-when-running-with-python-script-in-loading/23719

---

## Post #1 by @gzt036 (2022-06-06 01:07 UTC)

<p>Operating system: windows<br>
Slicer version: 5.0.2 or 5.1.0<br>
Expected behavior: stable<br>
Actual behavior: crashes almost always.</p>
<pre><code class="lang-auto">import os
import sys

from DICOMLib import DICOMUtils
import DICOMScalarVolumePlugin

def importDicomDir(dicomDataDir):	
	loadedNodeIDs = []
	patientUIDs = []
	with DICOMUtils.TemporaryDICOMDatabase() as db:
		DICOMUtils.importDicom(dicomDataDir, db)
		patientUIDs = db.patients()
		for patientUID in patientUIDs:
			loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))
	patientUID = patientUIDs[0]			
	return loadedNodeIDs,patientUID

dicomDataDir = 'D:\\data\\dicoms\\CT_data\\CHENG_XIAO_MEI_F 48y 腰椎\\ABDOMEN_0ABDOMENIV3PHASE_CUSTOMIZED_(ADUL_20150921_142302_995000\\ABDOMNC_1_5_B30F_0006'
loadedNodeIDs,patientUID = importDicomDir(dicomDataDir)
</code></pre>
<p>If I run it line by line interactively, it mostly works. However, if I run it using command line<br>
“C:\Users\zgan\AppData\Local\NA-MIC\Slicer 5.1.0-2022-06-01\Slicer.exe” --python-script “c:/zjsproj/slicer/t1.py”<br>
, it almost always crashes.</p>

---

## Post #2 by @gzt036 (2022-06-06 01:11 UTC)

<p>sometimes it works, most times it will say ‘no responding’ on the title bar and then crashes when loading files.<br>
Is there a better and more stable routine to load the files? Thanks!</p>

---

## Post #3 by @gzt036 (2022-06-06 01:17 UTC)

<p>checking the error logs I see these</p>
<pre><code class="lang-auto">Input port 0 of algorithm vtkImageMapToWindowLevelColors(0000022062EEB510) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageThreshold(0000022062EE8BA0) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageMapToWindowLevelColors(0000022062EEB510) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageMapToWindowLevelColors(0000022062EE9B90) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageThreshold(0000022062EE9750) has 0 connections but is not optional.


Input port 0 of algorithm vtkImageMapToWindowLevelColors(0000022062EE9B90) has 0 connections but is not optional.

</code></pre>
<p>Is that the reason for crashing? how to fix it then while loading?</p>

---

## Post #4 by @gzt036 (2022-06-07 00:27 UTC)

<p>Could someone help to look at what is wrong with this script?  How do you load a DICOM directory into Slicer with Python script?  The script sometimes works but most times fails. Also, a successful load may also show the error message above, so I am not sure that was the cause of the failure.</p>
<p>If possible, could someone provide a working script that loads a DICOM directory into Slicer? Thanks!!!</p>

---

## Post #5 by @mau_igna_06 (2022-06-07 09:12 UTC)

<p>I guess it’s a temporal logix errror. Just add the line<br>
Slicer.appp.ProcessEvents()<br>
A few times along your code<br>
Or add timers that execute that funxtion you want like<br>
Timer.aingleshot(callback)</p>
<p>I’m sending this from my device sorry if it is not clear</p>

---

## Post #6 by @gzt036 (2022-06-07 10:27 UTC)

<p>Thanks Mauro.</p>
<p>slicer.app.processEvents()  indeed helped. It does not crash as often and if I add enough of this line I can run my script to completion.</p>
<p>However, I still think this is an error/bug on the Slicer’s part. As every python statement ( or function call ) should be synchronized already.  there is no reason to add this synchronization calls all over the places.</p>
<p>Hope someone can fix it!</p>

---

## Post #7 by @pieper (2022-06-07 13:39 UTC)

<p><a class="mention" href="/u/gzt036">@gzt036</a> does the crashing depend on which data is loaded?</p>

---

## Post #8 by @Nadya_Shusharina (2023-02-17 16:50 UTC)

<p>I have the exact same problem with Slicer 5.0.2 on Linux (no_vnc container), trying to load DICOM from a script. Adding slicer.app.processEvents() in between every single line of script seemed to help. Like in the original question, my script without processEvents occasionally worked. Slicer 5.0.2 on Ubuntu 22 (not containerized) worked fine without processEvents, but I only tested it on one dataset.</p>
<p>Are there any plans to investigate and fix permanently?<br>
Thank you!</p>

---

## Post #9 by @pieper (2023-02-17 16:59 UTC)

<p>I use scripts like this all the time and Slicer doesn’t crash.  For example I just iterated through about 35 thousand dicom files yesterday with no problem using a current build.  <a class="mention" href="/u/nadya_shusharina">@Nadya_Shusharina</a> If you are having crashes please report the exact data and code so it can be investigated.  If you can’t share your data, try to replicate using public data, e.g. from IDC.</p>

---

## Post #10 by @Nadya_Shusharina (2023-02-17 17:21 UTC)

<p>The data is public. What is the best way to share? Also, the container where the errors happened for me is an Ubuntu 20.04.5 LTS, 16GB RAM and low on memory, 4-core CPU.</p>

---

## Post #11 by @pieper (2023-02-17 17:52 UTC)

<p>The ideal would be to put the data someplace like a public google drive folder or pull them from IDC and then provide a python script that downloads the data and then runs the simplest script that replicates the crash you are seeing.  This way it would be possible to see if the issue is with the data, the script, the docker configuration or something else.</p>
<p>For example, here’s the task I did yesterday to make nifti files and screen grabs for all the files in the <a href="https://doi.org/10.7937/djg7-gz87">CBM-CRC collection</a> on IDC.  This pulls down more data than we’d want for trying to replicate the crash, but it should give you an idea how to make a reproducible example.</p>
<p>First I got the list of URLs:</p>
<pre><code class="lang-auto">bq query -n 50000 --format=csv --use_legacy_sql=false \
  'SELECT gcs_url FROM `bigquery-public-data.idc_current.dicom_all` WHERE collection_id = "cmb_crc" LIMIT 50000' \
    &gt; cbm_crc-urls.csv
</code></pre>
<p>Then I downloaded them all to a local directory:</p>
<pre><code class="lang-auto">mkdir cbm_crc
cat cbm_crc-urls.csv| tail -n +2 | gsutil -m cp -I cbm_crc
</code></pre>
<p>In Slicer, I imported that directory into a new dicom database and then ran this script:</p>
<pre><code class="lang-auto">from DICOMLib import DICOMUtils

niiDir = "/opt/data/idc/cbm_crc-nii"

db = slicer.dicomDatabase
for patient in db.patients():
    for study in db.studiesForPatient(patient):
        accessionNumber = db.fieldForStudy("AccessionNumber", study)
        if accessionNumber == "":
            accessionNumber = study
        for series in db.seriesForStudy(study):
            slicer.mrmlScene.Clear()
            loadedNodeIDs = DICOMUtils.loadSeriesByUID([series])
            if len(loadedNodeIDs) != 1:
                print(f"Skipping {series} because it generated {len(loadedNodeIDs)} nodes")
                continue
            seriesDescription = db.fieldForSeries("SeriesDescription", series)
            seriesDescription = seriesDescription.replace(" ", "_").replace("/","-")
            seriesNumber = int(db.fieldForSeries("SeriesNumber", series))
            niiPath = f"{niiDir}/{accessionNumber}_{seriesNumber}_{seriesDescription}.nii.gz"
            pngPath = f"{niiDir}/{accessionNumber}_{seriesNumber}_{seriesDescription}.png"
            slicer.util.delayDisplay(niiPath, 100)
            print(niiPath)
            slicer.util.saveNode(slicer.util.getNode(loadedNodeIDs[0]), niiPath)
            slicer.util.mainWindow().centralWidget().grab().toImage().save(pngPath)
</code></pre>
<p>The whole process took a few hours but no crashes.</p>

---

## Post #12 by @fedorov (2023-02-23 22:44 UTC)

<p>I agree with Steve. I used startup scripts as well in the past, and never had issues like that.</p>
<p><a class="mention" href="/u/nadya_shusharina">@Nadya_Shusharina</a> please add the script to a public branch of a kaapana fork, and share the pointer here. Fortunately, all of our development is open source, and we don’t have any constraints sharing intermediate artifacts.</p>

---
