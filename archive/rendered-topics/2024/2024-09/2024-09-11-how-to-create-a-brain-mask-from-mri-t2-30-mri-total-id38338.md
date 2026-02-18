# How to create a brain mask from MRI T2 (30 MRI total)

**Topic ID**: 38338
**Date**: 2024-09-11
**URL**: https://discourse.slicer.org/t/how-to-create-a-brain-mask-from-mri-t2-30-mri-total/38338

---

## Post #1 by @jegiron (2024-09-11 21:54 UTC)

<p>I have MRI T2 weighed images and need to create a mask to remove skull and others. I have a total of 30 MRI models and need ultimately need to measure infarct volume percentage. I also need to do spatial normalization. How to do this as if I’ve never used 3d slicer (true).</p>

---

## Post #2 by @pieper (2024-09-12 00:30 UTC)

<p>There are lots of neuroimaging tools you can use to do things that - I’m not sure Slicer is the best for doing a batch of 30 cases since it’s more geared for interactive use where others can be used from a script or command line. When you say infarct I guess you mean stroke and I don’t think we have an extension for that, but I’ll bet something exists out there outside of Slicer if you do a literature search.</p>

---

## Post #3 by @jegiron (2024-09-13 19:28 UTC)

<p>Hi Steve,<br>
Ok. Would ITK-snap be a better option to do this? Or which neuroimaging tool would you recommend?<br>
Thanks,<br>
Joe</p>

---

## Post #4 by @pieper (2024-09-13 19:36 UTC)

<p>Not ITKSnap, something more like FSL or a tool in the freesurfer suite.  I’m not familiar with a specific tool for stroke, but there must be something out there.</p>

---
