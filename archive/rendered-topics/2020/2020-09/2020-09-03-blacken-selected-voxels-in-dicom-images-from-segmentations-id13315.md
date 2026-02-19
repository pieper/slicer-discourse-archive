---
topic_id: 13315
title: "Blacken Selected Voxels In Dicom Images From Segmentations"
date: 2020-09-03
url: https://discourse.slicer.org/t/13315
---

# "Blacken" selected voxels in DICOM images (from Segmentations)

**Topic ID**: 13315
**Date**: 2020-09-03
**URL**: https://discourse.slicer.org/t/blacken-selected-voxels-in-dicom-images-from-segmentations/13315

---

## Post #1 by @Philipp_Mayer (2020-09-03 11:59 UTC)

<p>Hi everybody,<br>
I am new to this forum. I am an Abdominal Radiologist at a German University Hospital.<br>
I have got a question about manipulating the intensity values of selected voxels in DICOM files.<br>
We want to generate Volume Rendering Images from abdominal CT scans with the Siemens syngo.via tool (syngo.via offers some special “Cinematic Volume Rendering” options). Unfortunately, the options in syngo.via to exclude certain areas from the rendered image are limited.<br>
Therefore, I thought I could maybe “prepare” the DICOM files with 3D Slicer.<br>
Is it possible to change the intensity of selected voxels in DICOM files to black, using 3D Slicer?<br>
If I segment certain organs using the segmentation tool, is there a way to “erase” the voxels within the segmentation (by setting the intensity values to black) and then save the result as manipulated DICOM images?</p>
<p>Thank you very much for your help,<br>
Philipp</p>

---

## Post #2 by @cpinter (2020-09-03 12:32 UTC)

<p>Hi Philipp,<br>
Absolutely, this is possible with Slicer. Please check out the “Mask Volume” tool in Segment Editor. This <a href="https://discourse.slicer.org/t/new-segment-editor-effects-mask-volume-and-surface-cut/699">topic introducing the feature</a> should help, but more information about it can be found on this forum and in the documentation. Let us know how it goes!</p>

---

## Post #3 by @pieper (2020-09-03 12:39 UTC)

<p>I agree with the approach <a class="mention" href="/u/cpinter">@cpinter</a> suggested and also look forward to seeing the results.  If things work well it would be interesting if you could share some examples and describe your methods.</p>

---

## Post #4 by @Philipp_Mayer (2020-09-03 13:23 UTC)

<p>Thank you so much! It seems to work.<br>
I will try to import the modified DICOM files to syngo.via this evening and hope I can show you some results soon <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=9" title=":wink:" class="emoji" alt=":wink:"></p>

---
