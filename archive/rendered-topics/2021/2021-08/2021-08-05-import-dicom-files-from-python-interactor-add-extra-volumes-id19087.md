---
topic_id: 19087
title: "Import Dicom Files From Python Interactor Add Extra Volumes"
date: 2021-08-05
url: https://discourse.slicer.org/t/19087
---

# Import DICOM files from python interactor add extra volumes and nodes

**Topic ID**: 19087
**Date**: 2021-08-05
**URL**: https://discourse.slicer.org/t/import-dicom-files-from-python-interactor-add-extra-volumes-and-nodes/19087

---

## Post #1 by @hotsen (2021-08-05 17:22 UTC)

<p>Operating system: win10<br>
Slicer version: stable version 4.11.20210226<br>
Expected behavior: Manually loading works fine<br>
Actual behavior: python interactor add extra volumes and nodes</p>
<p>Hi all,</p>
<p>I am new to Slicer. I got 5 folders of DICOM files with one folder contains CT and other four folders contains MRI and DWI. All files ending with .dcm</p>
<p>If I load these folders using DCM module, everything works fine. But I need to develop a script to do this in the python Interactor. Here is what I found online:</p>
<pre data-code-wrap="python"><code class="lang-python">dicomDataDir = r"C:\MyDicomFoldercontainsFivefolders"
from DICOMLib import DICOMUtils
DICOMUtils.importDicom(dicomDataDir)
patientUIDs = slicer.dicomDatabase.patients()
for patientUID in patientUIDs:
    loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))   
</code></pre>
<p>This code will import all the data and some extra volumes named “Sequence” (just one slice of image) and some extra nodes with “browser” in the name. Checked the source code of DICOMUtils, really can’t figure out where went wrong.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/37e499f1e30c09d50fa470450f43b99685b6d3e5.png" alt="Capture" data-base62-sha1="7Ys2ieE8VT6DoERGmyEJwWYKhFz" width="573" height="187"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2ad8d0835cdd702e8ca5bbabba3749fbb4810334.png" alt="Capture1" data-base62-sha1="672zKNUAcMlB3K8IymRP7pHVyrq" width="203" height="313"></p>
<p>Any advice? Thanks.</p>
<p>Hotsen</p>

---

## Post #2 by @hotsen (2021-08-06 15:06 UTC)

<p>Just an update. Not sure this is possible, I am thinking to call “Load” function (Load button) in DCM module using code. Now I can import the DICOM files into DICOMdatabase using the following code:</p>
<pre><code class="lang-python">dicomFilesDirectory = r"C:\MyDicomFoldercontainsFivefolders"
slicer.util.selectModule("DICOM")
dicomBrowser = slicer.modules.DICOMWidget.browserWidget.dicomBrowser
# use dicomBrowser.ImportDirectoryCopy to make a copy of the files (useful for importing data from removable storage)
dicomBrowser.importDirectory(dicomFilesDirectory, dicomBrowser.ImportDirectoryAddLink)
# wait for import to finish before proceeding (optional, if removed then import runs in the background)
dicomBrowser.waitForImportFinished()
</code></pre>
<p>After checking the source code of DICOMBrowser.py, I found that “Load” button is calling “loadCheckedLoadables” function, but I cannot call this function using “dicomBrowser.loadCheckedLoadables()”. Any suggestion on how to do that?</p>
<p>Thank you!</p>

---

## Post #3 by @lassoan (2021-08-07 17:25 UTC)

<p>Thanks for reporting this. When using <code>loadSeriesByUID</code> from Python, the function loaded all possible interpretations of the series. It makes more sense to use only the highest-confidence loadable by default (as it is done when using the DICOM browser in the non-advanced mode). I’ve <a href="https://github.com/Slicer/Slicer/commit/b7f6be2b6d61bc4703d40fbe0243e16f7a790a3a">changed the function</a> accordingly - the update will be available in Slicer Preview Releases from tomorrow.</p>

---

## Post #4 by @hotsen (2021-08-09 19:52 UTC)

<p>Thank you, Andras. The Preview Release solved the problem!</p>

---

## Post #5 by @lassoan (2021-08-09 23:20 UTC)

<p>A post was split to a new topic: <a href="/t/radiomics-error-no-module-named-pywt/19128">Radiomics error - No module named ‘pywt’</a></p>

---
