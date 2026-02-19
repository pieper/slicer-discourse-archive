---
topic_id: 21817
title: "Matching Segmentation With The Input Data"
date: 2022-02-06
url: https://discourse.slicer.org/t/21817
---

# Matching segmentation with the input data

**Topic ID**: 21817
**Date**: 2022-02-06
**URL**: https://discourse.slicer.org/t/matching-segmentation-with-the-input-data/21817

---

## Post #1 by @WojtekL (2022-02-06 01:24 UTC)

<p>Hello,</p>
<p>as I create the segmentation of the organ that’s spanning over 60 slices of the base image, let’s say slices 4-64, I’d like to save the segmentation in the way that the segmentation slice would match the number of the base image slice.</p>
<p>When I export the segmentation to DICOM, the mask starts right at the first slice, even though the first slices of input file do not contain the examined organ. Is there any way to create the segmentation of the size of the base image?</p>
<p>After a deep research on this case, I made following observations.<br>
Let’s say, that the segmented organ appears from slice 4 to 64, on a study of 200 slices in total:</p>
<ul>
<li>after saving the mask as DICOM, slice no. 64 (last one of the mask) gets displayed as slice no. 1 of the segmentation file and then every following slice contains the next part of the mask in a ascending order finishing at slice no.60 with the slice that represents the 1st slice of the mask (assuming we run through the input file from top to bottom).</li>
<li>following the mask in the reversed order, there are saved the empty slices until the end of the input file</li>
<li>the segmentation file is 196 slices in total, instead of the expected 200 (I’d really like to have those first four slices empty, but still displayed)</li>
</ul>
<p>What I’d like to achieve is having the same order of slices (running top to bottom, just as in the input file) with the first four slices empty, next 60 containing the mask in the descending order (displaying the topmost part from the input file as the topmost part of the mask) and then the rest of slices empty, until slice no. 200 where the file should end.</p>
<p>Any help would be highly appreciated.<br>
Cheers</p>

---

## Post #2 by @cpinter (2022-02-07 15:19 UTC)

<p>To clarify the question the modality used is DICOM SEG, see related topic <a href="https://discourse.slicer.org/t/saving-segmentation-as-dicom/21576/5" class="inline-onebox">Saving segmentation as DICOM - #5 by WojtekL</a>.</p>
<p>I do not have experience with the internals of DICOM SEG export, so I defer to those who have.</p>

---
