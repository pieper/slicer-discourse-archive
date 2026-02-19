---
topic_id: 26711
title: "Brain Segmentation Mask"
date: 2022-12-13
url: https://discourse.slicer.org/t/26711
---

# brain segmentation mask

**Topic ID**: 26711
**Date**: 2022-12-13
**URL**: https://discourse.slicer.org/t/brain-segmentation-mask/26711

---

## Post #1 by @Albulena_Bajrami (2022-12-13 14:34 UTC)

<p>Hi I was working on manual segmentation of some kind of lesions in the brain.<br>
I have to do one first segmentation on a certain sequence, afterwards have to use the same one and modify it and save as a new NIFTI file.<br>
I got how to save the first mask as nifti and upload with the new sequence. I can modify it for example erasing some parte, then I am not able to save it again as a new segmentation in NIFTI without deleting the previous file. It is saving with the same name, overwriting the first one.</p>
<p>How can I save it as a new mask</p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2022-12-13 14:46 UTC)

<p>The output filename in “Export to files” feature is set automatically from the segmentation’s name (the output is set as a folder instead of a filename because with some file formats the output consists of multiple files).</p>
<p>If you want to create different variations for a segmentation then I would recommend to keep all of them in the scene, with different names. You can clone a segmentation using the right-click menu in Data module.</p>
<p>You can of course save a modified segmentation with different name (rename the existing segmentation file on disk before writing the new one; or you can change the name of the segmentation node in Slicer before exporting; or you can also specify a different output folder; or you can export the segmentation to labelmap (using the right-click menu in Data module) and then save it with any filename). But then you would not preserve the original segmentations, only some NIFTI exports, which cannot store all metadata (such as segment names, colors, terminology).</p>

---
