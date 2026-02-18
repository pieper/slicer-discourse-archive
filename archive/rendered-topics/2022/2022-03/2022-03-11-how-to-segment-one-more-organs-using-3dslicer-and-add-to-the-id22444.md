# How to segment one/more organs using 3DSlicer and add to the existing segmentation file?

**Topic ID**: 22444
**Date**: 2022-03-11
**URL**: https://discourse.slicer.org/t/how-to-segment-one-more-organs-using-3dslicer-and-add-to-the-existing-segmentation-file/22444

---

## Post #1 by @Js165 (2022-03-11 03:12 UTC)

<p>I have original CT scans (.nii format) and a corresponding segmentation file (.nii format). Now I want to manually segment one/more organs using 3DSlicer and add to the existing segmentation file (.nii format). I am not sure how to perform this task. It will be helpful if you kindly suggest me the procedure.</p>

---

## Post #2 by @muratmaga (2022-03-11 05:12 UTC)

<p>If you can successfully import the existing segmentation into Slicer and the CT scan, then all you need is to create a new empty segmentation layer for your new organ segmentation, and continue from there.</p>

---

## Post #3 by @Js165 (2022-03-11 18:47 UTC)

<p>Thanks a lot! It worked. <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20"></p>

---
