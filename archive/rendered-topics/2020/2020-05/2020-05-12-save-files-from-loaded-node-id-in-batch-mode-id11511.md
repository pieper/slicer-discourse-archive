# Save files from loaded node ID in batch mode

**Topic ID**: 11511
**Date**: 2020-05-12
**URL**: https://discourse.slicer.org/t/save-files-from-loaded-node-id-in-batch-mode/11511

---

## Post #1 by @rickychen (2020-05-12 23:55 UTC)

<p>Hi guys,</p>
<p>I’m trying to follow the source codes for loading DICOM files as here:</p>
<p>Example: load all data from a DICOM folder (using a temporary DICOM database)<br>
dicomDataDir = “c:/my/folder/with/dicom-files”  # input folder with DICOM files<br>
loadedNodeIDs = []  # this list will contain the list of all loaded node IDs<br>
from DICOMLib import DICOMUtils<br>
with DICOMUtils.TemporaryDICOMDatabase() as db:<br>
DICOMUtils.importDicom(dicomDataDir, db)<br>
patientUIDs = db.patients()<br>
for patientUID in patientUIDs:<br>
loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))</p>
<p>However, I’m not quite clear what will be the next steps. i.e., how can I use the list of “loadedNodeIDs” to obtain the loadable instances so that I can export to other file format?</p>

---

## Post #2 by @pieper (2020-05-13 00:28 UTC)

<p><a href="https://github.com/QIICR/dcmheat/blob/master/docker/SlicerConvert.py">Here</a> is a slightly older example that just saves one node.  You could extend this to loop over your loaded nodes and save them out.</p>

---

## Post #3 by @lassoan (2020-05-13 02:23 UTC)

<p>You need to do something like this:</p>
<pre><code class="lang-auto">for loadedNodeID in loadedNodeIDs:
    slicer.util.saveNode(slicer.mrmlScene.GetNodeByID(loadedNodeID), ...set a filename here...)
</code></pre>

---

## Post #4 by @rickychen (2020-05-13 04:48 UTC)

<p>Thanks Andras, the syntax is correct, however, for the DICOM series I tested, it says No patient found with DICOM database UID (u’1’,). However, using DICOMScalarVolumePlugin, I can successfully output the correct file. What I did was the following:<br>
plugin = slicer.modules.dicomPlugins<a>’DICOMScalarVolumePlugin’</a><br>
if plugin:<br>
loadables = plugin.examineFiles(fileNames)<br>
volume = plugin.load(loadables[0])<br>
output_path = os.path.join(output_directory,output_filename+output_extension)<br>
try:<br>
slicer.util.saveNode(volume, output_path)<br>
except Exception as e:<br>
print(e)<br>
exit()<br>
I’m not sure if this is robust enough to process most DICOM files as Slicer did.</p>

---

## Post #5 by @lassoan (2020-05-16 22:20 UTC)

<p>Using the scalar volume plugin directly is fine, as long as you only need to load simple 3D volumes (not 4D volumes, structure sets, segmentation objects, registration objects, etc.).</p>

---
