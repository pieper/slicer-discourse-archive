---
topic_id: 4493
title: "Mismatch Of Image And Segmentation Volume"
date: 2018-10-23
url: https://discourse.slicer.org/t/4493
---

# Mismatch of image and segmentation volume

**Topic ID**: 4493
**Date**: 2018-10-23
**URL**: https://discourse.slicer.org/t/mismatch-of-image-and-segmentation-volume/4493

---

## Post #1 by @Gargi.Kothari (2018-10-23 03:36 UTC)

<p>Operating system: Windows 7<br>
Slicer version: 4.9.0<br>
Expected behavior:<br>
Actual behavior: For some of the image datasets, the segmentation volume and CT sets are not registered correctly, but should have been on the original datasets. Is there a way to fix this?</p>

---

## Post #2 by @lassoan (2018-10-23 03:37 UTC)

<p>What software did you use for segmentation? Did you apply a transformation on the CT or the segmentation before they were saved? Can you share the data set?</p>

---

## Post #3 by @Gargi.Kothari (2018-10-23 04:13 UTC)

<p>The CT images and segmentation volumes were downloaded from a publicly available dataset (<a href="https://wiki.cancerimagingarchive.net/display/Public/NSCLC-Radiomics" rel="nofollow noopener">https://wiki.cancerimagingarchive.net/display/Public/NSCLC-Radiomics</a>). I’m not sure if a transformation was applied before the CT scans were saved. I’d be happy to share the datasets that I’m having trouble with - what would be the best way to do this?</p>
<p>Thanks</p>

---

## Post #4 by @lassoan (2018-10-23 10:43 UTC)

<p>If I remember correctly, Steve Pieper told me that there were corrupted data sets in this collection (some transformations that were applied to the CT scans before segmentation were not saved in the archive). <a class="mention" href="/u/pieper">@pieper</a> can you confirm?</p>

---

## Post #5 by @pieper (2018-10-23 12:40 UTC)

<p>Yes, I had started working on <a href="https://github.com/pieper/Converters/tree/master/SlicerRT">some batch converter code</a> based on earler work by <a class="mention" href="/u/cpinter">@cpinter</a>, but I was told by one of the people who uploaded that data that there were some corrections done at treatement time for some patients (like the table height being adjusted) so the data was not consistent.  Apparently the best you can hope to do is manually adjust the rtstructs to an approximate position.</p>

---

## Post #6 by @Gargi.Kothari (2018-10-23 21:24 UTC)

<p>Thanks - that’s really helpful to know now. Did you also find that some of the segmentation files/ RTSTRUCT files were missing on that dataset? Were you able to recover any of these? Thanks.</p>

---

## Post #7 by @pieper (2018-10-23 21:46 UTC)

<p>No, from what I was told there wasn’t any further data available.  I decided that particular dataset wasn’t worth the effort.</p>
<p>If you are looking in general for image data with good segmentation then the QIN Head and Neck PET/CT dataset on TCIA is good.  If you are looking specifically for lung or for NSCLC data then I’m not sure where to look.</p>

---
