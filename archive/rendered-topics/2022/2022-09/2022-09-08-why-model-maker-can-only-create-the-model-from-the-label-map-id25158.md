# Why model maker can only create the model from the label map in range 0 to 255?

**Topic ID**: 25158
**Date**: 2022-09-08
**URL**: https://discourse.slicer.org/t/why-model-maker-can-only-create-the-model-from-the-label-map-in-range-0-to-255/25158

---

## Post #1 by @wpgao (2022-09-08 14:11 UTC)

<p>In some atlases, there may be more than 255 structures were labeled or some structures were labeled larger than 255. ModelMaker cannot create the models with label larger than 255. Is there any solution? Thanks!</p>

---

## Post #2 by @muratmaga (2022-09-08 16:22 UTC)

<p>Model maker is a very old module, and I am not sure if it is maintained. Use the segmentations module to first convert your atlases to segmentation objects and then export the segmentation as models.</p>

---

## Post #3 by @wpgao (2022-09-10 15:08 UTC)

<p>Thanks!<br>
It works. However, when the label is larger than 255, the segment name shows “invalid” in the segmentation module.</p>

---
