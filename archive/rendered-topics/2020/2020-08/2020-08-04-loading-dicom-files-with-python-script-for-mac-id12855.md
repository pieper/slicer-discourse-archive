# Loading DICOM files with python script for Mac

**Topic ID**: 12855
**Date**: 2020-08-04
**URL**: https://discourse.slicer.org/t/loading-dicom-files-with-python-script-for-mac/12855

---

## Post #1 by @epearlstone (2020-08-04 16:52 UTC)

<p>I am having trouble loading in DICOM files using the python script given in the Slicer python script repository. I am using a Mac computer and Slicer 4.11. Does anyone have a solution?</p>
<blockquote>
<p>dicomDataDir = “”~/Users/epstone/Desktop/Dicomdirector/Folder"  # input folder with DICOM files<br>
loadedNodeIDs = <span class="chcklst-box fa fa-square-o fa-fw"></span>  # this list will contain the list of all loaded node IDs</p>
<p>from DICOMLib import DICOMUtils<br>
with DICOMUtils.TemporaryDICOMDatabase() as db:<br>
DICOMUtils.importDicom(dicomDataDir, db)<br>
patientUIDs = db.patients()<br>
for patientUID in patientUIDs:<br>
loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))</p>
</blockquote>

---

## Post #2 by @lassoan (2020-08-04 16:54 UTC)

<p>Can you tell what your trouble is? What do you do, what do you expect to happen, and what happens instead? Do you see any error messages? Does DICOM import via the GUI works well? Have you tried with the very latest Slicer Preview Release?</p>

---

## Post #3 by @epearlstone (2020-08-04 17:43 UTC)

<p>I am expecting my folder full of dcm files to be imported as they would normally when using the DICOM import GUI (which works well. I am simply trying to practice using this scripting method). I am using the latest version of Slicer 4.11.0 and Python 3.6.7. I will attach a picture of my Slicer screen. No error is being given with my current implementation but nothing is happening. No files are loaded.<br>
I am using the script provided in the python script <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_load_DICOM_files_into_the_scene_from_a_folder" rel="noopener nofollow ugc">repository</a> given below:</p>
<blockquote>
<p>How to load DICOM files into the scene from a folder<br>
This code loads all DICOM objects into the scene from a file folder. All the registered plugins are evaluated and the one with the highest confidence will be used to load the data. Files are imported into a temporary DICOM database, so the current Slicer DICOM database is not impacted.</p>
</blockquote>
<pre data-code-wrap="python"><code class="lang-python">dicomDataDir = "c:/my/folder/with/dicom-files"  # input folder with DICOM files
loadedNodeIDs = []  # this list will contain the list of all loaded node IDs
  
from DICOMLib import DICOMUtils
with DICOMUtils.TemporaryDICOMDatabase() as db:
  DICOMUtils.importDicom(dicomDataDir, db)
  patientUIDs = db.patients()
  for patientUID in patientUIDs:
    loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))
</code></pre>

---

## Post #4 by @epearlstone (2020-08-04 17:45 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d404bdb69e163e8bc21b3881711525382af2c0f8.png" data-download-href="/uploads/short-url/ufBnEcvxDpaTheCFOa5QIe8XZl6.png?dl=1" title="Screen Shot 2020-08-04 at 1.40.38 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d404bdb69e163e8bc21b3881711525382af2c0f8_2_686x500.png" alt="Screen Shot 2020-08-04 at 1.40.38 PM" data-base62-sha1="ufBnEcvxDpaTheCFOa5QIe8XZl6" width="686" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d404bdb69e163e8bc21b3881711525382af2c0f8_2_686x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d404bdb69e163e8bc21b3881711525382af2c0f8_2_1029x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d404bdb69e163e8bc21b3881711525382af2c0f8_2_1372x1000.png 2x" data-dominant-color="EFEFF1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-08-04 at 1.40.38 PM</span><span class="informations">2368×1724 573 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @lassoan (2020-08-04 18:00 UTC)

<p>Thanks for the additional information.</p>
<p>By using the code snippet <a href="https://discourse.slicer.org/t/loading-dicom-files-with-python-script-for-mac/12855/3">above</a>, data is imported into a temporary database (note the <code>DICOMUtils.TemporaryDICOMDatabase()</code> command). If you want to import to the Slicer DICOM database then you can use <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_import_DICOM_files_into_the_application.27s_DICOM_database">this code snippet</a>.</p>
<p>If no errors are printed on the console then most likely there is a trivial issue (e.g., wrong input folder, invalid temporary folder). Messages in the application log (menu: Help / Report a bug) may give some hints.</p>

---

## Post #6 by @lassoan (2020-08-04 18:15 UTC)

<p>Your script (with slight simplifications) worked fine for me:</p>
<pre><code class="lang-python">folder = r"c:\D\S4\Testing\Data\Input\CTHeadAxialDicom"

import DICOMLib.DICOMUtils as utils
import DICOMScalarVolumePlugin
result = utils.importDicom(folder)
scalarVolumeReader = DICOMScalarVolumePlugin.DICOMScalarVolumePluginClass()
for patient in db.patients():
  for study in db.studiesForPatient(patient):
    for series in db.seriesForStudy(study):
      print('looking at series ' + series + ' for patient ' + patient)
      files = db.filesForSeries(series)
      loadable = scalarVolumeReader.examineForImport([files])[0]
      scalarVolumeReader.load(loadable)
</code></pre>

---

## Post #7 by @epearlstone (2020-08-04 18:30 UTC)

<p>This worked great. I think my original problem was my directory path was not written correctly because I have tried it all three ways and they all work. I will post all three methods for other’s reference.<br>
For loading the dicom files into a temporary database I used:</p>
<blockquote>
<p>from DICOMScalarVolumePlugin import DICOMScalarVolumePluginClass</p>
<p>import DICOMLib.DICOMUtils as utils<br>
import slicer<br>
import os.path<br>
folder = os.path.expanduser(“/Users/ethanpearlstone/Desktop/Dicomdirector/For Slicer/CT abd 072610/”)<br>
result = utils.importDicom(folder)<br>
DSVPC = DICOMScalarVolumePluginClass()<br>
db = slicer.dicomDatabase<br>
if (db.patients()):<br>
for patient in db.patients():<br>
for study in db.studiesForPatient(patient):<br>
for series in db.seriesForStudy(study):<br>
print('looking at series ’ + str(series) + ’ for patient ’ + str(patient))<br>
files = db.filesForSeries(series)<br>
DSVPC.load(DSVPC.examineForImport([files])[0])</p>
</blockquote>
<p>For importing to the Slicer DICOM database I used:</p>
<blockquote>
<p>slicer.util.selectModule(“DICOM”)<br>
dicomBrowser = slicer.modules.DICOMWidget.browserWidget.dicomBrowser<br>
dicomBrowser.importDirectory(“/Users/ethanpearlstone/Desktop/Dicomdirector/For Slicer/CT abd 072610/”, dicomBrowser.ImportDirectoryAddLink)<br>
dicomBrowser.waitForImportFinished()</p>
</blockquote>
<p>Using the simplified method <a class="mention" href="/u/lassoan">@lassoan</a> provided:</p>
<blockquote>
<p>folder = “/Users/ethanpearlstone/Desktop/Dicomdirector/For Slicer/CT abd 072610/”</p>
<p>import DICOMLib.DICOMUtils as utils<br>
import DICOMScalarVolumePlugin<br>
result = utils.importDicom(folder)<br>
scalarVolumeReader = DICOMScalarVolumePlugin.DICOMScalarVolumePluginClass()<br>
for patient in db.patients():<br>
for study in db.studiesForPatient(patient):<br>
for series in db.seriesForStudy(study):<br>
print('looking at series ’ + series + ’ for patient ’ + patient)<br>
files = db.filesForSeries(series)<br>
loadable = scalarVolumeReader.examineForImport([files])[0]<br>
scalarVolumeReader.load(loadable)</p>
</blockquote>
<p>Thank you for your help!</p>

---
