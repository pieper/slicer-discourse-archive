# save segmentation  

**Topic ID**: 13923
**Date**: 2020-10-07
**URL**: https://discourse.slicer.org/t/save-segmentation/13923

---

## Post #1 by @Eslam_Abdo (2020-10-07 14:45 UTC)

<p>Operating system: MACOS<br>
Slicer version: 4.10.2</p>
<p>I saved my segmentation as labelmap and I read it from python<br>
and I need to know the structure of the data to use it in my deep learning model</p>

---

## Post #2 by @lassoan (2020-10-07 19:59 UTC)

<p>There are two different approaches you can use.</p>
<p>A. Write your segmentation to numpy array directly in Slicer’s Python environment. You can use tools available in Slicer to preprocess, normalize, augment your data, using GUI, Python scripts, or <a href="https://github.com/Slicer/SlicerJupyter">Jupyter Notebooks</a>. There is an example script <a href="https://discourse.slicer.org/t/generating-augmented-training-data-from-nrrd-file-using-random-translations-rotations-and-deformations/11810/8">here</a> that shows how to do 3D image augmentation with random deformations in Slicer.</p>
<p>B. You can load the segmentation (.seg.nrrd) file and process it using any tools (e.g., <a href="https://pypi.org/project/torchio/">torchio</a>). Segmentation is stored in standard .nrrd file, so you can use any Python nrrd reader to read it as a numpy array. You can find specification of custom fields <a href="http://apidocs.slicer.org/master/classvtkMRMLSegmentationStorageNode.html#details">here</a> and an example Python code snippet (that does not require Slicer’s Python environment) <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_information_from_segmentation_nrrd_file_header">here</a>.</p>

---
