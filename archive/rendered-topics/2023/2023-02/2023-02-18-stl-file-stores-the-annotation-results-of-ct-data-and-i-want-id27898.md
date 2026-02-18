# stl file stores the annotation results of CT data, and I want to convert it to nii format for deep learning.

**Topic ID**: 27898
**Date**: 2023-02-18
**URL**: https://discourse.slicer.org/t/stl-file-stores-the-annotation-results-of-ct-data-and-i-want-to-convert-it-to-nii-format-for-deep-learning/27898

---

## Post #1 by @missile (2023-02-18 04:53 UTC)

<p>Operating system:Hii,<br>
I am having trouble applying the module in slicer 5.0.2. My situation is the stl file stores the annotation results of CT data, and I want to convert it to nii format for deep learning.<br>
When i press apply, it saysreferenceVolumeNode = slicer.util.loadVolume(reference_volume_path), which keeps giving me an error about not being able to load noad from file.2<br>
Detailed error:<br>
Traceback (most recent call last):<br>
File “”, line 7, in <br>
File “D:\Slicer 5.0.2\bin\Python\slicer\util.py”, line 908, in loadVolume<br>
return loadNodeFromFile(filename, filetype, properties, returnNode)<br>
File “D:\Slicer 5.0.2\bin\Python\slicer\util.py”, line 681, in loadNodeFromFile<br>
raise RuntimeError(errorMessage)<br>
RuntimeError: Failed to load node from file: D:\change\dicom\2.nii.gz</p>
<p>Below is my code</p>
<p>import os<br>
import slicer<br>
stl_path = r"D:\change\stl"<br>
image_path = r"D:\change\dicom"<br>
out_path = r"D:\change\nii"<br>
patients = os.listdir(stl_path)<br>
for patient in patients:<br>
patient_path = os.path.join(stl_path, patient)<br>
stl_files = os.listdir(patient_path)<br>
output_file_path = os.path.join(out_path, patient)<br>
os.makedirs(output_file_path, exist_ok=True)<br>
reference_volume_path = os.path.join(image_path, patient+“.nii.gz”)<br>
referenceVolumeNode = slicer.util.loadVolume(reference_volume_path)<br>
for stl_file in stl_files:<br>
stl_file_name = os.path.join(patient_path, stl_file)<br>
output_file_name = os.path.join(output_file_path, stl_file[0:-4] + “.nii.gz”)<br>
segmentationNode = slicer.util.loadSegmentation(stl_file_name)<br>
outputLabelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLLabelMapVolumeNode’)<br>
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, outputLabelmapVolumeNode,<br>
referenceVolumeNode)<br>
slicer.util.saveNode(outputLabelmapVolumeNode, output_file_name)<br>
slicer.mrmlScene.Clear(0)<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @missile (2023-02-17 17:18 UTC)

<p>Hello sir, I don’t know if you have time, but I would like to ask you a question.</p>
<p>My situation is the same as yours, the stl file stores the annotation results of CT data, and I want to convert it to nii format for deep learning. I reproduced the code from your post into the Python interactor in slicer, but I keep getting</p>
<p>referenceVolumeNode = slicer.util.loadVolume(reference_volume_path), which keeps giving me an error about not being able to load noad from file.</p>
<p>I’m very confused and I’m looking forward to your help when you have time.</p>
<p>Below is my code</p>
<p>import os<br>
import slicer<br>
stl_path = r"D:\change\stl"<br>
image_path = r"D:\change\dicom"<br>
out_path = r"D:\change\nii"<br>
patients = os.listdir(stl_path)<br>
for patient in patients:<br>
patient_path = os.path.join(stl_path, patient)<br>
stl_files = os.listdir(patient_path)<br>
output_file_path = os.path.join(out_path, patient)<br>
os.makedirs(output_file_path, exist_ok=True)<br>
reference_volume_path = os.path.join(image_path, patient+“.nii.gz”)<br>
referenceVolumeNode = slicer.util.loadVolume(reference_volume_path)<br>
for stl_file in stl_files:<br>
stl_file_name = os.path.join(patient_path, stl_file)<br>
output_file_name = os.path.join(output_file_path, stl_file[0:-4] + “.nii.gz”)<br>
segmentationNode = slicer.util.loadSegmentation(stl_file_name)<br>
outputLabelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLLabelMapVolumeNode’)<br>
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, outputLabelmapVolumeNode,<br>
referenceVolumeNode)<br>
slicer.util.saveNode(outputLabelmapVolumeNode, output_file_name)<br>
slicer.mrmlScene.Clear(0)</p>

---
