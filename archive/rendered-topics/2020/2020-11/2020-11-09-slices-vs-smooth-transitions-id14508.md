# Slices vs smooth transitions

**Topic ID**: 14508
**Date**: 2020-11-09
**URL**: https://discourse.slicer.org/t/slices-vs-smooth-transitions/14508

---

## Post #1 by @11katie (2020-11-09 14:48 UTC)

<p>I am calculating volume of lesions on brain MRI data and for some scans that I upload into 3D slicer the slices appear in a smooth transition between them, creating hundreds of ‘slices’ making segmentation very difficult. On other software the data does appear as 30 slices or so but on 3D slicer there are hundreds. Is there a way to change the data on 3D slicer to only see the 30 slices?</p>

---

## Post #2 by @lassoan (2020-11-09 19:12 UTC)

<p>Step size when you iterate through the volume using the slice offset slider or the arrow keys should match the volume spacing along that axis.</p>
<p>Maybe the slice view is not aligned to the image axes. Click on <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view">“Rotate to volume plane” button</a> to see if you get the expected step size then.</p>

---
