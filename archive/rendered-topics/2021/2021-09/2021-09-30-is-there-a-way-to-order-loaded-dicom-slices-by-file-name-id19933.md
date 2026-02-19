---
topic_id: 19933
title: "Is There A Way To Order Loaded Dicom Slices By File Name"
date: 2021-09-30
url: https://discourse.slicer.org/t/19933
---

# Is there a way to order loaded dicom slices by file name?

**Topic ID**: 19933
**Date**: 2021-09-30
**URL**: https://discourse.slicer.org/t/is-there-a-way-to-order-loaded-dicom-slices-by-file-name/19933

---

## Post #1 by @Rafael_Bravo (2021-09-30 12:43 UTC)

<p>When I load my dicom series into 3Dslicer the z order is shuffled, meaning that the slice location values are probably incorrect. however if I use other software to load them in order by the dicom file names, they are properly ordered. is there a way to get 3Dslicer to order slices based on their file names?</p>
<p>Thanks,</p>
<ul>
<li>Rafael Bravo</li>
</ul>

---

## Post #2 by @lassoan (2021-09-30 13:21 UTC)

<p>Filenames must be ignored when a volume is reconstructed from frames stored in DICOM file format. The only information that matters is the image position and orientation tags.</p>
<p>Do you have any problems when you <a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html#dicom-data">load the image using the DICOM module</a>?</p>

---
