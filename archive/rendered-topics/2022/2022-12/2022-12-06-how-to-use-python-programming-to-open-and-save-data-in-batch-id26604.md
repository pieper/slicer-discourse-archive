---
topic_id: 26604
title: "How To Use Python Programming To Open And Save Data In Batch"
date: 2022-12-06
url: https://discourse.slicer.org/t/26604
---

# How to use python programming to open and save data in batches?

**Topic ID**: 26604
**Date**: 2022-12-06
**URL**: https://discourse.slicer.org/t/how-to-use-python-programming-to-open-and-save-data-in-batches/26604

---

## Post #1 by @lyh-ecnu (2022-12-06 15:11 UTC)

<p>I tried to write a program to open the folder and read several cases inside，but after I run it, only the data of the first case can be successfully loaded, and the following cases will report errors。My code and error message are as follows：<br>
My code:</p>
<pre><code class="lang-python">dicomDataDir = r"D:/test" #my folder
loadedNodeIDs = [] # this list will contain the list of all loaded node IDs
from DICOMLib import DICOMUtils
with DICOMUtils.TemporaryDICOMDatabase() as db:
  DICOMUtils.importDicom(dicomDataDir, db)
  patientUIDs = db.patients()
  for patientUID in patientUIDs:
    loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))
</code></pre>
<p>error message :</p>
<pre><code class="lang-auto">Loading with imageIOName: GDCM
Could not read scalar volume using GDCM approach.  Error is: FileNotFoundError
Loading with imageIOName: DCMTK
Could not read scalar volume using DCMTK approach.  Error is: FileNotFoundError
Failed to read a multivolume: Volume frame 0 is invalid - Reference image in series does not contain geometry information. Please use caution.
Traceback (most recent call last):
  File "C:/Users/18729/AppData/Local/NA-MIC/Slicer 5.0.3/bin/../lib/Slicer-5.0/qt-scripted-modules/MultiVolumeImporterPlugin.py", line 639, in load
    raise OSError(f"Volume frame {frameNumber} is invalid - {svLoadables[0].warning}")
OSError: Volume frame 0 is invalid - Reference image in series does not contain geometry information. Please use caution.
</code></pre>
<p>The problem seems to be that the program doesn’t read the file.But the first file can be opened normally.anyone can help me?thanks!</p>

---

## Post #3 by @lassoan (2022-12-06 16:29 UTC)

<p>Can you load data sets using the DICOM module GUI?</p>

---

## Post #4 by @lyh-ecnu (2022-12-07 02:02 UTC)

<p>yes,individual files open fine, but not with this code</p>

---

## Post #5 by @lassoan (2022-12-07 12:27 UTC)

<p>Did you use the DICOM module or just the “Add data” window? “Add data” should not be used because it does not do any geometry checks.</p>
<p>Can you share the data set? (upload somewhere and post the download link here; make sure it does not contain patient information)</p>

---

## Post #6 by @lyh-ecnu (2022-12-09 06:54 UTC)

<p>thanks,butl dont know what impact will geometry checks have.l use dicom library upload three data(By the way, lt’s upload speed is too slow, is there any good anonymized upload solution?)，I put them in the same folder when I use，and run my code trying to open them.The download link is as follows：<br>
<a href="https://www.dicomlibrary.com?requestType=WADO&amp;studyUID=1.3.6.1.4.1.44316.6.102.1.202212091317352.4411468198218093536139&amp;manage=c06965fa4641dc8493e7fe635047d58f&amp;token=94c7c87523e6750c370bee8837c8fbc0" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.dicomlibrary.com?requestType=WADO&amp;studyUID=1.3.6.1.4.1.44316.6.102.1.202212091317352.4411468198218093536139&amp;manage=c06965fa4641dc8493e7fe635047d58f&amp;token=94c7c87523e6750c370bee8837c8fbc0</a><br>
<a href="https://www.dicomlibrary.com?requestType=WADO&amp;studyUID=1.3.6.1.4.1.44316.6.102.1.20221209135222936.37252472383452532849&amp;manage=cf12dfb851db42146c9a02f90a7811de&amp;token=9345b0eeef371789711f503695e8094f" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.dicomlibrary.com?requestType=WADO&amp;studyUID=1.3.6.1.4.1.44316.6.102.1.20221209135222936.37252472383452532849&amp;manage=cf12dfb851db42146c9a02f90a7811de&amp;token=9345b0eeef371789711f503695e8094f</a><br>
<a href="https://www.dicomlibrary.com?requestType=WADO&amp;studyUID=1.3.6.1.4.1.44316.6.102.1.20221209141950624.15861645053471484630&amp;manage=2d6e48d4dea24f252a01ec479a02176a&amp;token=2f409b7a6fbf1a7243dd33ff5bb26ad9" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.dicomlibrary.com?requestType=WADO&amp;studyUID=1.3.6.1.4.1.44316.6.102.1.20221209141950624.15861645053471484630&amp;manage=2d6e48d4dea24f252a01ec479a02176a&amp;token=2f409b7a6fbf1a7243dd33ff5bb26ad9</a></p>

---
