# Apply and save a transformation on an mha file

**Topic ID**: 26499
**Date**: 2022-11-29
**URL**: https://discourse.slicer.org/t/apply-and-save-a-transformation-on-an-mha-file/26499

---

## Post #1 by @rggelel (2022-11-29 19:38 UTC)

<p>Hello everyone,<br>
I have a question about the mha file. I have an mha file that has a basic transform written in the file. But, I would like to change this transform with another one and save it in the file. Do you know a way to do this and even automate it afterwards? Thanks for your help.</p>

---

## Post #2 by @lassoan (2022-12-01 06:00 UTC)

<p>You can <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#load-volume-from-file">load the image file as a volume node</a>, set the IJK to RAS matrix (origin, spacing, axis directions) by calling methods on the volume node, and then <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#save-volume-to-file">save the volume node</a>.</p>

---
