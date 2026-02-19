---
topic_id: 18449
title: "Save Ultrasound Images In Mha Format"
date: 2021-07-01
url: https://discourse.slicer.org/t/18449
---

# Save ultrasound images in mha format

**Topic ID**: 18449
**Date**: 2021-07-01
**URL**: https://discourse.slicer.org/t/save-ultrasound-images-in-mha-format/18449

---

## Post #1 by @Qianqian_Cai (2021-07-01 01:49 UTC)

<p>I loaded my ultrasound frames with the “load data” button and tried to save them with the “save data” button but it doesn’t give the option to save as .mha file.</p>
<p>I checked the format of mha file or mhd file. It looks that I need to write addtional info such as the position of each frame to the text header. How did you save it in the .mha format?</p>

---

## Post #2 by @lassoan (2021-07-09 04:35 UTC)

<p>I think sequence metafile format (.mha file that contains image and and transforms) is for import only. <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> can you confirm?</p>

---

## Post #3 by @Sunderlandkyl (2021-07-09 14:13 UTC)

<p>Yes, sequence metafiles are currently only readable.</p>
<p>We could potentially add a function in SlicerIGSIO that could export sequence browser nodes in that format.</p>

---

## Post #4 by @lassoan (2021-07-09 14:42 UTC)

<p>Why would you like to export to mha format?</p>
<p>You can reconstruct 3D volumes inside Slicer, without exporting the tracked image data.</p>

---
