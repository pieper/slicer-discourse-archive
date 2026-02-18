# Is it possible to read the displacement field?

**Topic ID**: 40356
**Date**: 2024-11-24
**URL**: https://discourse.slicer.org/t/is-it-possible-to-read-the-displacement-field/40356

---

## Post #1 by @Chuan (2024-11-24 14:31 UTC)

<p>Hi all,</p>
<p>Multiple registration methods integrated in Slicer3D allow the generation of displacement fields. However, the output is typically in binary formats such as .nii or .mhd, with the core displacement data stored in .raw files. Neither format is readily usable for reading the displacement field, for example, to determine the new location of a specific node after displacement. Could anyone advise on how to access and process these displacement fields in Matlab or Python? I mean not visualization but reading the displacement field data of one specific point.</p>
<p>Best regards,<br>
Chuan</p>

---

## Post #2 by @pieper (2024-11-25 14:51 UTC)

<p>Hi - you can use <code>arrayFromGridTransform</code> to get a numpy array of vectors representing the displacement field.  You can use this together with the rest of the <a href="https://apidocs.slicer.org/main/classvtkMRMLTransformNode.html">vtkMRMLTransfornNode</a> api to determine whatever you need to know.</p>

---
