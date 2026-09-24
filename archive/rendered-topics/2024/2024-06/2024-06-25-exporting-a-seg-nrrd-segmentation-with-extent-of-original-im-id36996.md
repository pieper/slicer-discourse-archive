---
topic_id: 36996
title: "Exporting a \".seg.nrrd\" Segmentation with Extent of Original Image"
date: 2024-06-25
url: https://discourse.slicer.org/t/36996
last_bumped: 2026-09-24T06:51:42.171Z
---

# Exporting a ".seg.nrrd" Segmentation with Extent of Original Image

**Topic ID**: 36996
**Date**: 2024-06-25
**URL**: https://discourse.slicer.org/t/exporting-a-seg-nrrd-segmentation-with-extent-of-original-image/36996

---

## Post #1 by @sjanko2 (2024-06-25 02:37 UTC)

<p>Hello,</p>
<p>I am new to posting to this forum, so please let me know if this question is in the right place!</p>
<p>I have a labelmapvolume node (“atlas”) and a volume node (“ghost”) within my scene. I’d like to export the labels as a “.seg.nrrd” file type where the header is set up for use with slicerio. I can’t seem to export in this format while maintaing the extent of the original image. Here are some things I have tried:</p>
<p>Per 3D Slicer documentation, I did the following:<br>
1.) Converted the labelmapvolume node to a segmentation node by right clicking &gt; Convert labelmap to segmentation node<br>
2.) Right clicked the segmentation node &gt; Export to file<br>
3.) Selected “.seg.nrrd” as the file format<br>
==&gt; This results in a .seg.nrrd file, but is not the same extent as my original image which is causing me some issues with post processing. I have tried this export method both with the “Crop to minimum extent” option selected and deselected with the same result.</p>
<p><a href="https://discourse.slicer.org/t/why-are-my-segmentations-being-saved-as-only-the-bounding-box-size-rather-than-the-size-of-the-original-image/9909">Per this forum post</a>, I tried to export with my original image set as a reference geometry:<br>
1.) Converted the labelmapvolume node to a segmentation node by right clicking &gt; Convert labelmap to segmentation node<br>
2.) Gone to the Segmentations module, selected my segmentation, set my file format as “NRRD” (there is only options for STL, OBJ, NRRD, and NIFTI), set my Reference volume to be my volume node “ghost”<br>
3.) Selected my preferred color table<br>
==&gt; This results in a .nrrd file with the full extent that I need, but it has no metadata header information that can be used by slicerio as the “.seg.nrrd” files do.</p>
<p>Can someone help me understand what I’m missing? How can I get the full extent for my segmentation relative to reference geometry AND the metadata in the header of my nrrd file?</p>
<p>Thanks so much!</p>
<p>Sam</p>

---

## Post #2 by @Denis_Samatov (2026-09-24 06:51 UTC)

<p>Hi <a class="mention" href="/u/sjanko2">@sjanko2</a> — I revisited your report about needing both the reference image’s full extent and the segment metadata that slicerio reads from `.seg.nrrd`. Your two export paths each preserved only one of those properties, and unchecking “Crop to minimum extent” did not change the result. Did you eventually find a supported way to retain both? If this is still an issue, which Slicer version and reference-geometry setting were involved? I am testing a read-only check that reports physical extent and segment metadata before downstream processing, and your outcome would help decide whether it is useful. A written description or synthetic header is enough; please do not share patient images.</p>

---
