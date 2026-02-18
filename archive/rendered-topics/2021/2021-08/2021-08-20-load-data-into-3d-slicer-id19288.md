# Load Data into 3D slicer

**Topic ID**: 19288
**Date**: 2021-08-20
**URL**: https://discourse.slicer.org/t/load-data-into-3d-slicer/19288

---

## Post #1 by @alyssan (2021-08-20 17:15 UTC)

<p>I am new to 3D slicer and would like to load data for segmentation using the python interactor.</p>
<p>I have been using this code to load the sample data:<br>
import SampleData<br>
sampleDataLogic = SampleData.SampleDataLogic()<br>
masterVolumeNode = sampleDataLogic.downloadMRBrainTumor1()<br>
n = getNode(‘MRBrainTumor1’)</p>
<p>I would like this same functionality but using DICOM files stored on my Desktop. I have looked at the documentation but still have some confusion. Any help would be appreciated.</p>

---

## Post #2 by @pieper (2021-08-20 18:02 UTC)

<p>You should have a look through the script repository to see what kind of things are possible.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#load-dicom-files-into-the-scene-from-a-folder" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#load-dicom-files-into-the-scene-from-a-folder</a></p>

---
