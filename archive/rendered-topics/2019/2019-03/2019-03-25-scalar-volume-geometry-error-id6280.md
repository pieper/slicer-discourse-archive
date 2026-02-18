# Scalar volume geometry error

**Topic ID**: 6280
**Date**: 2019-03-25
**URL**: https://discourse.slicer.org/t/scalar-volume-geometry-error/6280

---

## Post #1 by @tself96 (2019-03-25 15:53 UTC)

<p>Operating System: MacOS Majave<br>
Modality: CT</p>
<p>When trying to load DICOM slices I get the warning “reference image in series does not contain geometry information”, I proceed to load anyway and two dimensions are stretched. This may be due to a recent update to the imaging reconstruction software. I am not sure how to resolve this issue or if there is another way to load the slices.</p>

---

## Post #2 by @lassoan (2019-03-25 16:05 UTC)

<p>The problem seems to be that the image does not contain geometry information (origin, spacing, axis directions). It may be a secondary capture image (screenshot) or the required DICOM fields are missing.</p>
<p>You can inspect what fields are present in the DICOM file by clicking “Metadata” button in the DICOM browser.</p>
<p>What software did you use to generate the image?</p>

---

## Post #3 by @tself96 (2019-03-25 17:50 UTC)

<p>Thank you for responding. Which required DICOM fields should I check?<br>
The software used to generate the images is North Star Imaging.</p>

---

## Post #4 by @lassoan (2019-03-25 18:35 UTC)

<aside class="quote no-group" data-username="tself96" data-post="3" data-topic="6280">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/779978/48.png" class="avatar"> tself96:</div>
<blockquote>
<p>The software used to generate the images is North Star Imaging.</p>
</blockquote>
</aside>
<p>Industrial CTs are known to have lots of DICOM standard compliance issues.</p>
<p>You may try running your data set through Slicer’s “DICOM Patcher” module, which fixes some common mistakes.</p>
<aside class="quote no-group" data-username="tself96" data-post="3" data-topic="6280">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/779978/48.png" class="avatar"> tself96:</div>
<blockquote>
<p>Thank you for responding. Which required DICOM fields should I check?</p>
</blockquote>
</aside>
<p>In <a href="http://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_A.3.3.html">CT image IOD</a>, it is mandatory to have <a href="http://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.6.2.html#table_C.7-10">image plane module</a>, with required (type 1) fields: <strong>pixel spacing</strong>, <strong>image orientation</strong>, and <strong>image position</strong>.</p>

---

## Post #5 by @tself96 (2019-03-25 20:08 UTC)

<p>Running the data set through DICOM Patcher prompts an error with tag (0020, 0012). I have an unknown acquisition number. Also, following the links you posted, tag (0020, 0037) is missing. Not sure if it accompanies another image that is misplaced. I will scroll through the other slices to see if it is out of order.</p>

---

## Post #6 by @lassoan (2019-03-27 13:42 UTC)

<p>The image won’t load if image orientation tag (0020, 0037) is missing. Is it missing from all slices or just a few? If only missing from a few then you can delete those, clean up the database, re-import, and see if you get a complete volume from the rest of the slices.</p>

---

## Post #7 by @tself96 (2019-03-27 14:28 UTC)

<p>Tag (0020, 0037) is missing from all slices, not sure what to do about that. However, I now have X, Y, Z tiff slices to try and load. I have no idea what to expect, I am going to try them this evening. I’m confident the error is with the image reconstruction software, I am trying to hash it out with their support.</p>

---
