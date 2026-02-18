# import slicer in a local python/virtualenv and load correctly image orientation

**Topic ID**: 12092
**Date**: 2020-06-18
**URL**: https://discourse.slicer.org/t/import-slicer-in-a-local-python-virtualenv-and-load-correctly-image-orientation/12092

---

## Post #1 by @emiltoft (2020-06-18 11:23 UTC)

<p>Is it possible to use slicer’s python api in a custom made program? Specifically, am I interested in the dicom-image loading due to the correctly dicom volume-image orientation.</p>
<p>I have can see in previous posts that it’s not possible to use the system’s python - is it still the case? -and I guess it is the same using a virtualenv?</p>
<p>I’m currently using vtk’s python api but I’m unable to correctly orienting the dicom volume-images. How does your implementation of vtk work?</p>

---

## Post #2 by @pieper (2020-06-18 17:39 UTC)

<p>Probably best to use the <code>PythonSlicer</code> executable that comes with Slicer.  It’s a pretty complete python distribution with vtk and many other useful things built.  Plus you can pip install most packages.</p>

---
