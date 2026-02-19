---
topic_id: 25032
title: "Export Transformed 4D Image As Nifti"
date: 2022-08-31
url: https://discourse.slicer.org/t/25032
---

# Export transformed 4D image as nifti?

**Topic ID**: 25032
**Date**: 2022-08-31
**URL**: https://discourse.slicer.org/t/export-transformed-4d-image-as-nifti/25032

---

## Post #1 by @ch-n (2022-08-31 19:27 UTC)

<p>Hi I would like to apply a bspline transformation I generated with the plastimatch plugin to a 4D image.<br>
That works all fine but afterwards I can no longer export the image in nifti format.<br>
I need the image for further work as nifti.<br>
Is there a way to export as nifti?<br>
I tried to convert the nrrd file afterwards to the nifti format using SimpleITK, but the 4D image becomes a 5D image with an empty fourth dim and the actual forth in the fifth.<br>
I just loaded de nrrd with sitk.ReadImage and saved with sitk.WriteImage.</p>
<p>Thanks for your help,<br>
Chris</p>

---

## Post #2 by @ebrahim (2022-08-31 19:43 UTC)

<p>Are you using Slicer to load the image? You can right click on the node and there should be an option to export. Then you can choose nifti as the export format.</p>
<p>The sitk problem sounds like some dim being misinterpreted as a channel</p>

---

## Post #3 by @ch-n (2022-09-01 07:29 UTC)

<p>Hi <a class="mention" href="/u/ebrahim">@ebrahim</a>, thanks for the tip, but there is only the option to export as DICOM and in the save manue I can just select nrrd and nhrd.</p>
<p>I guess that should be the problem with sitk.<br>
Do you have any knowledge about the meta information in the nrrd file?<br>
I’m not to 100% sure to which key they translate in the nifti format.</p>

---

## Post #4 by @ebrahim (2022-09-01 12:54 UTC)

<p>I’m not familiar with the meta info off the top of my head but feel free to share an example file if you’d like me to poke around</p>

---
