# Write/Read MRB and ACSV files in custom application

**Topic ID**: 30899
**Date**: 2023-08-01
**URL**: https://discourse.slicer.org/t/write-read-mrb-and-acsv-files-in-custom-application/30899

---

## Post #1 by @darabi (2023-08-01 07:29 UTC)

<p>Hello,<br>
in my custom app, I load multiple STL files as segmentations, generate a binary label map and a volume and now would like to store this intermediate result, preferrably as one file.</p>
<p>I tried MRB and got this error:</p>
<pre><code class="lang-auto">Warning: In vtkMRMLAnnotationStorageNode.cxx, line 535
vtkMRMLAnnotationLinesStorageNode (0x55e81517db70): WriteAnnotationTextProperties: annotation text display node is null


Warning: In vtkMRMLAnnotationLinesStorageNode.cxx, line 395
vtkMRMLAnnotationLinesStorageNode (0x55e81517db70): WriteAnnotationDataInternal: with stream: can't call WriteAnnotationDataInternal on superclass, retval = 0


vtkMRMLScene::WriteToMRB: Failed to save .../slicer-wrk/2023-08-01/2023-08-01-Scene.mrb: Failed to save scene to data bundle directory


bool qSlicerCoreIOManager::saveNodes(qSlicerIO::IOFileType, const IOProperties&amp;, vtkMRMLMessageCollection*, vtkMRMLScene*) error: Saving failed with all writers found for file ".../slicer-wrk/2023-08-01/2023-08-01-Scene.mrb" of type "SceneFile"
void qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int, vtkMRMLMessageCollection*, bool) Data save error: "- Error: Failed to save .../slicer-wrk/2023-08-01/2023-08-01-Scene.mrb: Failed to save scene to data bundle directory\n- Error: Failed to save scene as .../slicer-wrk/2023-08-01/2023-08-01-Scene.mrb\n- Error: Saving failed with all writers found for file '.../slicer-wrk/2023-08-01/2023-08-01-Scene.mrb' of type 'SceneFile'.\n"
</code></pre>
<p>then I decided to store them as individual files and got</p>
<pre><code class="lang-auto">Warning: In vtkMRMLAnnotationLinesStorageNode.cxx, line 395
vtkMRMLAnnotationLinesStorageNode (0x55e81517db70): WriteAnnotationDataInternal: with stream: can't call WriteAnnotationDataInternal on superclass, retval = 0


bool qSlicerCoreIOManager::saveNodes(qSlicerIO::IOFileType, const IOProperties&amp;, vtkMRMLMessageCollection*, vtkMRMLScene*) error: Saving failed with all writers found for file ".../slicer-wrk/2023-08-01/CropROI_Geruest_clipped source volume.acsv" of type "ModelFile"
void qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int, vtkMRMLMessageCollection*, bool) Data save error: "Error: Cannot write data file: .../slicer-wrk/2023-08-01/CropROI_Geruest_clipped source volume.acsv.\n"
void qSlicerSaveDataDialogPrivate::updateStatusIconFromMessageCollection(int, vtkMRMLMessageCollection*, bool) Data save information: ""
</code></pre>
<p>There is obviously some I/O module missing from my build.</p>
<p>Can you please help?</p>
<p>Thanks</p>
<p>Kambiz</p>

---

## Post #2 by @lassoan (2023-08-02 04:36 UTC)

<p>Annotation module has been removed some time ago. Annotation files (.acsv) has some limited support for reading (when they are read from file they are immediately converted to markup nodes), but it is no longer supported as an output file format. Instead, you can save markup nodes as .json file, or you can export markups to tables and save tables as .csv or .tsv files.</p>

---
