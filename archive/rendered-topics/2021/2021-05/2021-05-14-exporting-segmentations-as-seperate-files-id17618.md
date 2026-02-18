# Exporting segmentations as seperate files

**Topic ID**: 17618
**Date**: 2021-05-14
**URL**: https://discourse.slicer.org/t/exporting-segmentations-as-seperate-files/17618

---

## Post #1 by @Josef_Yu (2021-05-14 12:59 UTC)

<p>Hello folks,</p>
<p>I have delineated several organs / bones inside a filed, on Slicer3D they are shown as different segmentations, however I wanted to export each segmentation one by one.</p>
<p>Maybe there is already a solution, but I haven’t found a sophisticated way to conquer this task. Can anyone help me?</p>
<p>in Short:<br>
Inside a project file: brain, liver, lung as segmentations</p>
<p>what I would like to have: save each segmentation as niftii</p>
<p>cheers</p>

---

## Post #2 by @lassoan (2021-05-14 23:16 UTC)

<p>This is not a functionality that we would add to the user interface, you can easily implement it in Python.</p>
<p>I would recommend to perform this conversion as a preprocessing/normalization step of your data processing workflow. You can <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-information-from-segmentation-nrrd-file-header">use this code snippet</a> in any Python environment (not just in Slicer) to parse a segmentation (.seg.nrrd) file and extract one or more segments as numpy array, write to file, etc. Using this script allows you to archive your segmentation data with all metadata (segment names, DICOM terminology, display properties, etc. in a project-independent way) in seg.nrrd file and create training data for your network fully automatically, in any format you need for your specific project.</p>
<p>You can of course easily do the conversion in Slicer, too by <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-labelmap-node-from-segmentation-node">exporting selected segment to labelmap volume</a> and then <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#save-volume-to-file">saving the volume to file</a>.</p>

---
