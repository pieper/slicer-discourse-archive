---
topic_id: 34408
title: "How To Crop A Segmentation"
date: 2024-02-19
url: https://discourse.slicer.org/t/34408
---

# How to crop a segmentation?

**Topic ID**: 34408
**Date**: 2024-02-19
**URL**: https://discourse.slicer.org/t/how-to-crop-a-segmentation/34408

---

## Post #1 by @harad (2024-02-19 20:17 UTC)

<p>I need the tumor segmentation exported as a separate, standalone DICOM file. This cannot be done by crop volume because only rectangular shapes can be cropped in this way. All attempts to export a segmentation end up only with boundaries without the image arrays. Thanks for your help!</p>

---

## Post #2 by @muratmaga (2024-02-20 00:33 UTC)

<p>If you are going to save a file, you need to have rectangular dimensions. THe volume has to have a fixed sized grid.</p>
<aside class="quote no-group" data-username="harad" data-post="1" data-topic="34408">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/harad/48/14934_2.png" class="avatar"> harad:</div>
<blockquote>
<p>All attempts to export a segmentation end up only with boundaries without the image arrays</p>
</blockquote>
</aside>
<p>Not sure what you mean by that.</p>

---

## Post #3 by @harad (2024-02-20 07:18 UTC)

<p>Many thanks for your prompt answer. Exporting a VOI with its tumour shape and full image array would simplify the analysis by CNN that I intend to do because it would avoid a sequential upload of a full DICOM file and a segmentation file. From your answer, I conclude that exporting a tumour VOI with its irregular border and image area, as a standalone DICOM file, is not possible.   My last sentence meant that whenever I successfully export a segmentation, with its irregular borders, in any of the available file formats,  it is always a shallow shape, containing only borders (delineation) data, without the image array.</p>

---

## Post #4 by @muratmaga (2024-02-20 08:06 UTC)

<p>I am still not entirely following what you want to do. Do you want to save only the contents of volume under the VOI?</p>
<p>If that’s the case you can use the Mask Volume or Split Volume (if you want to reduce it to its smallest extend) effects in Segment Editor. Split Volume is in another extension called SegmentEditorExtraEffects.</p>

---

## Post #5 by @harad (2024-02-20 09:11 UTC)

<p>Many thanks again. I simply only need to analyse the tumour VOI,  the rest of the image is irrelevant. So, I want to avoid the complication in the code of importing the DICOM file with the entire scan and then subsequently importing the segmentation.nrrd file to restrict the analysis only to the tumour VOI segmentation. Of course, it is simpler if I only have a VOI in the DICOM file. Your advice was golden, by using Mask volume, I actually managed to export a DICOM file that has only VOI, with the rest of the area masked. I sense that this approach is very uncommon, maybe because I am not comfortable with coding and then always try to simplify the coding as much as possible.</p>

---
