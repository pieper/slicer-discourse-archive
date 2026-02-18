# Importing STL files

**Topic ID**: 3209
**Date**: 2018-06-17
**URL**: https://discourse.slicer.org/t/importing-stl-files/3209

---

## Post #1 by @bnathasingh (2018-06-17 18:57 UTC)

<p>Hi,</p>
<p>I am trying to import STL files into 3D slicer with the hope of merging an STL version of a CT and an STL version of an MRI to create a 3D rendering of the entire head (skull, blood vessels, tumor, etc…)</p>
<p>From what I’ve tried I have only been able to import DICOM versions of the CT and MRI and even with that I haven’t been able to merge the two images.</p>
<p>Is anyone able to help me or suggest another software they know of that can achieve what I want?</p>
<p>Thank you!</p>

---

## Post #2 by @cpinter (2018-06-17 19:57 UTC)

<p>STL files contain surface meshes, which typically represent segmentations of regions of interest in an anatomy. They are not “versions of a CT/MR”, but data derived from it. You can simply load an STL by drag&amp;dropping it onto Slicer. You can the convert them to segmentations, and then you can do many operations on them in the Segment Editor module. Not sure what you mean by merging them. Into what?</p>
<p>This page might help in understanding what kind of data there are typically and how to handle them:<br>
<a href="http://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html" class="onebox" target="_blank">http://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html</a></p>

---
