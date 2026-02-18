# Batch Processing error (output folder empty)

**Topic ID**: 27702
**Date**: 2023-02-08
**URL**: https://discourse.slicer.org/t/batch-processing-error-output-folder-empty/27702

---

## Post #1 by @ahtang617 (2023-02-08 11:25 UTC)

<p>Hi, I am trying to use batch processing but somehow run into some errors that I dont know how to solve.</p>
<p>At first, I tried to run the script with my database and patitents were loaded but the output folders were all empty. I then checked if my dicom are readable and they were fine when loading into Slicer.</p>
<p>And somehoe, this error keeps coming up and nothing could be saved as output.</p>
<p>[VTK] Generic Warning: In D:\D\S\S-0\Libs\MRML\Core\vtkDataFileFormatHelper.cxx, line 237</p>
<p>[VTK] vtkDataFileFormatHelper::GetFileExtensionFromFormatString: please update deprecated extension-only format specifier to ‘File format name (.ext)’ format! Current format string: .nrrd</p>
<p>[VTK] vtkMRMLVolumeArchetypeStorageNode::WriteDataInternal: Error renaming file to C:/Users/Documents/output/3/0 RTSTRUCT MRI_1_HR-CTV.nrrd, renameReturn = -1</p>
<p>[VTK] Generic Warning: In D:\D\S\S-0\Libs\MRML\Core\vtkDataFileFormatHelper.cxx, line 237</p>
<p>[VTK] vtkDataFileFormatHelper::GetFileExtensionFromFormatString: please update deprecated extension-only format specifier to ‘File format name (.ext)’ format! Current format string: .nrrd</p>
<p>[Qt] bool __cdecl qSlicerCoreIOManager::saveNodes(class QString,const class QMap&lt;class QString,class QVariant&gt; &amp;,class vtkMRMLMessageCollection *,class vtkMRMLScene *) error: Saving failed with all writers found for file “output\3/0 RTSTRUCT MRI_1_HR-CTV.nrrd” of type “VolumeFile”</p>
<p>[Python] Failed to save node to file: output\3/0 RTSTRUCT MRI_1_HR-CTV.nrrd</p>
<p>[Python] - Error: Error renaming file to C:/Users/Documents/output/3/0 RTSTRUCT MRI_1_HR-CTV.nrrd, renameReturn = -1</p>
<p>[Python] - Error: Saving failed with all writers found for file ‘output\3/0 RTSTRUCT MRI_1_HR-CTV.nrrd’ of type ‘VolumeFile’.</p>
<p>[Python] Failed to save labelmap: output\3/0 RTSTRUCT MRI_1_HR-CTV.nrrd</p>
<p>What should I do to solve this error?<br>
Tahnk you very much.</p>

---

## Post #2 by @lassoan (2023-02-08 11:27 UTC)

<p>The problem is that the <code>C:/Users/Documents/output/3/0 RTSTRUCT MRI_1_HR-CTV.nrrd</code> file is not writable. Probably you specified incirrect folder - it sends that the username is missing from the path.</p>

---

## Post #3 by @ahtang617 (2023-02-08 17:01 UTC)

<p>I’m sorry if I confused you, I removed user name just in case of privacy but the new folders were created in output path specified except they are all empty folders.</p>
<p>I just wanted to convert dicom to label map and nrrd file.</p>

---
