---
topic_id: 9218
title: "Slicer Segmentation Statistics Values"
date: 2019-11-19
url: https://discourse.slicer.org/t/9218
---

# Slicer Segmentation Statistics Values

**Topic ID**: 9218
**Date**: 2019-11-19
**URL**: https://discourse.slicer.org/t/slicer-segmentation-statistics-values/9218

---

## Post #1 by @rsheth (2019-11-19 17:10 UTC)

<p>Hello,</p>
<p>I am having some trouble with the segmentation statistics tool in Slicer. I have been working at segmenting a lung in a uCT image series. I have been using the segmentation tool and the “fill between segments” feature. After reconstructing my lung, I wanted to measure the volume of the segment, however, the volume appears to be too high, somewhere in the range of 854 cm^3. Based on the information found in literature, my lung should be somewhere in the neighborhood of 2 mm^3. I wanted to know if there is something wrong with the scale in slicer, and if I can change it in any way?</p>
<p>Thank You!</p>

---

## Post #2 by @lassoan (2019-11-20 05:29 UTC)

<p>If you measure a known distance using the annotation ruler, do you get correct value? If not then most likely the distance unit in the uCT was not set to millimeter and you need to correct the volume measurements accordingly.</p>

---

## Post #3 by @rsheth (2020-01-17 18:28 UTC)

<p>Hi Lassoan,</p>
<p>The files are from a third party, and so I do not know the known distances. How do I correct the volume measurements?</p>

---

## Post #4 by @lassoan (2020-01-17 19:00 UTC)

<p>Can you share an example data set so that we can see if it contains any additional scaling information that could be used or there is anything suspicious in the DICOM header? If not, then probably the only choice remaining is to ask the third party or report the problem to the imaging device manufacturer.</p>

---

## Post #5 by @rsheth (2020-01-17 19:23 UTC)

<p>Hi,</p>
<p>Is there an email that I can share the data with? What is the best way to share it?</p>
<p>Best,<br>
Ram</p>

---

## Post #6 by @rsheth (2020-01-17 19:25 UTC)

<p><a href="https://studentuml-my.sharepoint.com/:f:/g/personal/ram_sheth_student_uml_edu/ErbYRi5B_ERChLlWYOoX11EBBzzV4uwV4ueDordrFMYLXQ?e=VvBMEz" class="onebox" target="_blank" rel="nofollow noopener">https://studentuml-my.sharepoint.com/:f:/g/personal/ram_sheth_student_uml_edu/ErbYRi5B_ERChLlWYOoX11EBBzzV4uwV4ueDordrFMYLXQ?e=VvBMEz</a></p>
<p>Please let me know if this link works</p>

---

## Post #7 by @lassoan (2020-01-17 19:34 UTC)

<p>We would need the original DICOM files. If there is any issue with spacing, then it is due to problems while creating or importing the DICOM files.</p>

---
