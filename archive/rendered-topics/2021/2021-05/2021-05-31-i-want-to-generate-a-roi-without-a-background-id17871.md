# I want to generate a ROI without a background

**Topic ID**: 17871
**Date**: 2021-05-31
**URL**: https://discourse.slicer.org/t/i-want-to-generate-a-roi-without-a-background/17871

---

## Post #1 by @pardisz (2021-05-31 00:51 UTC)

<p>I have created an ROI and exported it as a nifti file on 3Dslicer v4. When I try to overlay the ROI to a template on mricron I can see that the nifti file from slicer doesn’t only include the ROI, but also a black background that covers the template. How can I get rid of the black box and only save the ROI?</p>

---

## Post #2 by @lassoan (2021-05-31 23:35 UTC)

<p>You can export the segmentation using many different volumes, with different geometries. By default the geometry of the first selected volume is used for export, but you can choose any other volume as reference volume. See more information <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#export-segmentation-to-labelmap-volume-file">here</a>.</p>

---

## Post #3 by @Hamoun_Rozati (2022-05-03 10:25 UTC)

<p>Hello, I am also having the same issue. ROIs in MRIcron have a black background, although when I use ITK snap it doesn’t appear to be an issue. I’ve tried changing the settings as advised but no luck. This only occurs with ROIs extracted from DICOM data, and not with ROIs I have constructed myself in Slicer. Any help would be greatly appreciated</p>

---

## Post #4 by @lassoan (2022-05-03 23:05 UTC)

<p>It is hard to guess what problem MRIcron has with certain segmentations. Maybe <a class="mention" href="/u/chris_rorden">@Chris_Rorden</a> has some ideas.</p>

---
