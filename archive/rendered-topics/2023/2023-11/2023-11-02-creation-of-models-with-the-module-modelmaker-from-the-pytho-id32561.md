---
topic_id: 32561
title: "Creation Of Models With The Module Modelmaker From The Pytho"
date: 2023-11-02
url: https://discourse.slicer.org/t/32561
---

# Creation of Models with the Module ModelMaker from the Python console

**Topic ID**: 32561
**Date**: 2023-11-02
**URL**: https://discourse.slicer.org/t/creation-of-models-with-the-module-modelmaker-from-the-python-console/32561

---

## Post #1 by @jhernandezr (2023-11-02 15:34 UTC)

<p>Hello!<br>
My team and I are working on the study of segmentations as vtk volumes, however we are trying to automatize the process with the python console from slicer. We have thought that, once we have loaded the nifti volumes as labels, we should be able to use the Model Maker Module, however we were not able to do so. I will be adding the code that we were using for this task. we executed each line separately in the python console:</p>
<p>slicer.util.loadLabelVolume(‘path_of_the_nifti’)<br>
labelVolume = slicer.util.getNode(‘SMALL_015’)<br>
single_label_volume = slicer.vtkMRMLLabelMapVolumeNode()<br>
single_label_volume.SetName(‘Name_of_the_label’)<br>
slicer.mrml.AddNode(single_label_volume)<br>
single_label_volume.CopyOrientation(labelVolume)<br>
single_label_volume.SetOrigin(labelVolume.GetOrigin())<br>
single_label_volume.SetSpacing(labelVolume.GetSpacing())<br>
label_array = slicer.util.array(labelVolume.GetID())<br>
single_label_array = (label_array == label_value).astype(‘uint8’)<br>
slicer.util.updateVolumeFromArray(single_label_volume, single_label_array)</p>
<p>This way, I achieved an isolated structure from my segmentations, and now I tried creating a node with vtkMRMLModelMakerNode but we were not able to manage how to use it.</p>
<p>We appreciate the help beforehand!</p>

---
