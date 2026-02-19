---
topic_id: 28476
title: "Osirix Roi Sr And Sc To Rtstruct"
date: 2023-03-20
url: https://discourse.slicer.org/t/28476
---

# OsiriX ROI SR and SC to RTSTRUCT?

**Topic ID**: 28476
**Date**: 2023-03-20
**URL**: https://discourse.slicer.org/t/osirix-roi-sr-and-sc-to-rtstruct/28476

---

## Post #1 by @NajaJean (2023-03-20 13:49 UTC)

<p>Hi, thanks for your time!<br>
I have a huge, messy folder containing DICOM images with various modalities, primarily MR. Some of them have been segmented using Osirix and are stored as SC or SR modalities. Although I can view the SC modality images as non-interactive volumes, I am unable to transform them into segmentations. Is it possible to convert these SC/SR format images into a different format such as RTStruct?<br>
I noticed that the sandbox extension has an ‘Import OsiriX ROI’ feature, but as it only accepts .json or .xml formats. As I am new to these formats, please excuse me if my question appears trivial.<br>
Best Regards, Naja</p>

---

## Post #2 by @lassoan (2023-03-21 03:41 UTC)

<p>The OsiriX ROI importer module can load the proprietary files that you can save from OsiriX.</p>
<p>Once you imported these files into Slicer as segmentations, you can export them as DICOM RT Structure Set (not recommend) or as DICOM Segmentation Object.</p>

---

## Post #3 by @NajaJean (2023-03-27 08:29 UTC)

<p>Thanks for the quick answer! I do not have access to OsiriX, so I’m not able to save the segmentations differently</p>

---

## Post #4 by @lassoan (2023-03-27 15:40 UTC)

<p>You can use the free OsiriX Lite for this conversion then you won’t have to use OsiriX ever again.</p>

---

## Post #5 by @kaizhao (2025-04-05 06:16 UTC)

<p>I created a python utility to convert OsiriX SR files into standard formats including DICOM RT struct and NifTi.</p>
<p>Checkout the <a href="https://github.com/intcomp/OsiriXConvert" rel="noopener nofollow ugc">source code</a> and a blog article<br>
<a href="https://kaizhao.net/blog/osirix-convert" class="inline-onebox" rel="noopener nofollow ugc">How to Convert OsiriX ROI to Standard Formats - Kai Zhao</a> .</p>

---

## Post #6 by @lassoan (2025-04-07 04:53 UTC)

<p>Thanks for sharing. Is there a reason why you created the utility when the converter in Slicer has been available already? Have you found any issues or limitations?</p>
<p>You used rt-utils, which has many limitations, including working only with binary masks, while SlicerRT works with polygons (and can create smooth, end-capped, keyhole-aware 3D meshes). It also seems that you need to export the data from OsiriX in a very particular way. Anyway, if you think that your utility is better than what Slicer’s OsiriX importer can do then you may consider submitting it to an extension (e.g., you can submit a pull request to the Sandbox extension) so that users can install it by a few clicks.</p>
<p>I would note here that <a href="https://scholar.google.com/scholar?q=%22Pixmeo%22+OR+%28%22OsiriX%22+AND+%28%22medical%22+OR+%22radiology%22+OR+%22imaging%22%29%29&amp;hl=en&amp;as_sdt=0%2C5&amp;as_ylo=2024&amp;as_yhi=2024">references to OsiriX in publications</a> has been on a steep decline since 2017, which indicates that users are abandoning it. OsiriX had 2460 citations then and 1440 now; while Slicer had 1380 citations then and 5560 now. Therefore, probably it may not worth investing a whole lot of effort into interfacing with OsiriX.</p>

---
