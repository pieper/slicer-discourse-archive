# Nifti segmentation to dicom-seg in a batch with python

**Topic ID**: 32488
**Date**: 2023-10-30
**URL**: https://discourse.slicer.org/t/nifti-segmentation-to-dicom-seg-in-a-batch-with-python/32488

---

## Post #1 by @gdvp (2023-10-30 17:08 UTC)

<p>Hi,</p>
<p>I use 3D slicer for a while, but am rather new with the python usage in slicer.<br>
I have to convert a lot of nifti files to dicom-seg format, which is a cumbersome task, so I wanted to do that in a batch as the nifti files with every CT dicom are named the same.</p>
<p>I tried first to do it with one scan and used the following code:<br>
‘’’<br>
import slicer<br>
from DICOMLib import DICOMUtils<br>
import DICOMScalarVolumePlugin<br>
import DICOMSegmentationPlugin</p>
<p>segmentationNode = r’path_to_segmentation_in_nifti’<br>
dicomDataDir = r’path_to_CT_in_dicom’<br>
outputFolder = r’path_to_output_folder’</p>
<p>loadedNodeIDs = <span class="chcklst-box fa fa-square-o fa-fw"></span> # this list will contain the list of all loaded node IDs<br>
with DICOMUtils.TemporaryDICOMDatabase() as db:<br>
DICOMUtils.importDicom(dicomDataDir, db)<br>
patientUIDs = db.patients()<br>
for patientUID in patientUIDs:<br>
loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))</p>
<h1><a name="p-102536-associate-segmentation-node-with-a-reference-volume-node-1" class="anchor" href="#p-102536-associate-segmentation-node-with-a-reference-volume-node-1" aria-label="Heading link"></a>Associate segmentation node with a reference volume node</h1>
<p>shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)<br>
referenceVolumeShItem = shNode.GetItemByDataNode(loadedNodeIDs)<br>
studyShItem = shNode.GetItemParent(referenceVolumeShItem)<br>
segmentationShItem = shNode.GetItemByDataNode(segmentationNode)<br>
shNode.SetItemParent(segmentationShItem, studyShItem)</p>
<h1><a name="p-102536-export-to-dicom-2" class="anchor" href="#p-102536-export-to-dicom-2" aria-label="Heading link"></a>Export to DICOM</h1>
<p>exporter = DICOMSegmentationPlugin.DICOMSegmentationPluginClass()<br>
exportables = exporter.examineForExport(segmentationShItem)<br>
for exp in exportables:<br>
exp.directory = outputFolder<br>
exporter.export(exportables)<br>
‘’’</p>
<p>But I get an error when trying to read in the referenceVolume:<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
TypeError: GetItemByDataNode argument 1: method requires a VTK object</p>
<p>I’m not sure how to get this NodeIDs into a VTK object. Could anyone help me give the golden tip.</p>
<p>Thanks!</p>

---

## Post #2 by @mikebind (2023-10-30 22:04 UTC)

<p>I think the issue is likely that <code>loadedNodeIDs</code> is a list of ID strings of image volume nodes, whereas <code>GetItemByDataNode()</code> expects its input to be a node, rather than a node ID. If you change the erroring line to</p>
<pre><code class="lang-auto"># Get the image node by its ID string
referenceVolumeNode = slicer.mrmlScene.GetNodeByID(loadedNodeIDs[0])
# Get the subject hierarchy item id corresponding to the 
referenceVolumeShItem = shNode.GetItemByDataNode(referenceVolumeNode)
</code></pre>

---

## Post #3 by @gdvp (2023-10-31 11:00 UTC)

<p>Perfect! That really helped.<br>
I now updated the code to:</p>
<p>import slicer<br>
from DICOMLib import DICOMUtils<br>
import DICOMScalarVolumePlugin<br>
import DICOMSegmentationPlugin</p>
<p>niftiPath = r’path_to_segmentation_in_nifti’<br>
dicomDataDir = r’path_to_CT_in_dicom’<br>
outputFolder = r’path_to_output_folder’</p>
<p><span class="hashtag-raw">#Load</span> the NIfTI segmentation<br>
segmentationNode = slicer.util.loadSegmentation(niftiPath)<br>
segmentationNode.SetAttribute(‘DICOM.SeriesDescription’, ‘Segmentation Series Description’) # Customize the description<br>
segmentationNode.SetAttribute(‘DICOM.Modality’, ‘SEG’)</p>
<p>loadedNodeIDs = <span class="chcklst-box fa fa-square-o fa-fw"></span> # this list will contain the list of all loaded node IDs<br>
db = slicer.dicomDatabase<br>
DICOMUtils.importDicom(dicomDataDir, db)<br>
patientUIDs = db.patients()<br>
for patientUID in patientUIDs:<br>
loadedNodeIDs.extend(DICOMUtils.loadPatientByUID(patientUID))</p>
<p><span class="hashtag-raw">#Associate</span> segmentation node with a reference volume node<br>
shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)<br>
referenceVolumeNode = slicer.mrmlScene.GetNodeByID(loadedNodeIDs[0])<br>
referenceVolumeShItem = shNode.GetItemByDataNode(referenceVolumeNode)</p>
<p><span class="hashtag-raw">#Set</span> the reference volume for the segmentation<br>
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(referenceVolumeNode)<br>
studyShItem = shNode.GetItemParent(referenceVolumeShItem)<br>
segmentationShItem = shNode.GetItemByDataNode(segmentationNode)<br>
shNode.SetItemParent(segmentationShItem, studyShItem)</p>
<p><span class="hashtag-raw">#Export</span> to DICOM<br>
exporter = DICOMSegmentationPlugin.DICOMSegmentationPluginClass()<br>
exportables = exporter.examineForExport(segmentationShItem)<br>
for exp in exportables:<br>
exp.directory = outputFolder</p>
<p>exporter.export(exportables)</p>
<p>However, the export does not seem to work properly yet. The modality is not set to SEG, and if I want to open it in a different software program, it is not recognized as a segmentation.</p>
<p>What I do manually is, create a new subject with a new study, link the CT and the segmentations. Then, in segment editor I change the source geometry of the segmentations to the CT, and then export the segmentations with the DICOMSegmentationPlugin.</p>
<p>I cannot really find a way to do that with Python. Does someone have a suggestion?</p>

---
