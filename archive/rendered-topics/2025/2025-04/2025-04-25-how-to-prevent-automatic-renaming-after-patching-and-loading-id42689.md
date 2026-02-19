---
topic_id: 42689
title: "How To Prevent Automatic Renaming After Patching And Loading"
date: 2025-04-25
url: https://discourse.slicer.org/t/42689
---

# How to prevent automatic renaming after patching and loading echcardiograms?

**Topic ID**: 42689
**Date**: 2025-04-25
**URL**: https://discourse.slicer.org/t/how-to-prevent-automatic-renaming-after-patching-and-loading-echcardiograms/42689

---

## Post #1 by @Maeva (2025-04-25 16:08 UTC)

<p>Hello,<br>
I am doing a research in which I model 3D hearts of neonates. I have downloaded the images to DICOM cartesian maps, and all works. Then, using the cardiac drop down botton (provided by the HeartSlicer extension), I patch all the 5-6 DICOM images per patient in a folder for each patient. Then, when I click on the upload DCM data botton, and the program uploads the patched files from the folder, it automatically renames them all to US, US_1,US_2, but not in the order in which they appear from top to bottom in the folder. Therefore, for each US (ultrasound), I can’t know from which unpatched DCM image it came from, which would be needed for my research. Is there anyway to program the order of uploading (and therefore of naming) or an option so that the files (even after being patched and uploaded) maintain all the same original names?</p>
<p>Thank you to anyone who might want to help me out! Have a good day! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @lassoan (2025-04-25 16:18 UTC)

<p>Order of files in a folder is not a reliable way to identify data sets. If you don’t anonymize your data sets then they will show up in the Data module under the correct patient. If you anonymize your data sets then I would recommend to enable NRRD file export instead and identify data sets based on filename.</p>

---

## Post #3 by @Maeva (2025-04-30 21:53 UTC)

<p>Thank you for the reply. How do I anonymize?</p>

---

## Post #4 by @lassoan (2025-04-30 22:22 UTC)

<p>If your data does not leave hospital computers and everyone who works with the data is trained to handle protected health information then you may not need to anonymize.</p>
<p>Otherwise, probably the data was already anonymized by the time you got it. In this case, you can simply use the exported NRRD files. The only metadata in these Cartesian US DICOM files is the patient information, so if the files are anonymized, then the only information they contain is the image data, which NRRD stores more conveniently.</p>

---
