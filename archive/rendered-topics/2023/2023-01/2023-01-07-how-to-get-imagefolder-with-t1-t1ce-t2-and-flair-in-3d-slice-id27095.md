# how to get imagefolder with t1, t1ce, t2 and flair in 3d slicer extended cli python module

**Topic ID**: 27095
**Date**: 2023-01-07
**URL**: https://discourse.slicer.org/t/how-to-get-imagefolder-with-t1-t1ce-t2-and-flair-in-3d-slicer-extended-cli-python-module/27095

---

## Post #1 by @scotwilli (2023-01-07 13:36 UTC)

<p>Im trying to create a 3d slicer cli python module which can select a patient folder with .nii files of t1, t1c2, t2 and flair. I have a pytorch inference script which takes all four modalities (t1, t1ce, t2, flair) combined input. Not able to understand how to build widget which can fetch patient folder as input in cli python module. Im new to 3d slicer. Please help me.</p>
<p>Thanks in advance</p>

---

## Post #2 by @pieper (2023-01-07 15:52 UTC)

<p>The CLI infrastructure is pretty rigid so you would be better off writing a python scripted module to access the files.</p>

---
