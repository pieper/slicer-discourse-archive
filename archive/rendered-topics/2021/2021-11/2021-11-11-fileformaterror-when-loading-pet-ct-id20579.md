---
topic_id: 20579
title: "Fileformaterror When Loading Pet Ct"
date: 2021-11-11
url: https://discourse.slicer.org/t/20579
---

# FileFormatError when loading PET CT

**Topic ID**: 20579
**Date**: 2021-11-11
**URL**: https://discourse.slicer.org/t/fileformaterror-when-loading-pet-ct/20579

---

## Post #1 by @rbumm (2021-11-11 13:53 UTC)

<p>Hi,<br>
I would like to load PET CT images into Slicer 3.13, DICOM import works, but clicking the axial 512x512 PET image series results in:</p>
<pre><code class="lang-auto">Could not read scalar volume using GDCM approach. Error is: FileFormatError
Loading with imageIOName: DCMTK
Could not read scalar volume using DCMTK approach. Error is: FileFormatError
Could not load: 552: TK axial as a Scalar Volume
</code></pre>
<p>The PETDICOMExtension is installed. Any ideas?</p>
<p>Thank you.</p>

---

## Post #2 by @rbumm (2021-11-11 14:30 UTC)

<p>Addition:<br>
There is a b/w 128x128 PET image series with modality “PT” that can be loaded, but the colored PET-CT images with modality “OT” can not.</p>

---

## Post #3 by @lassoan (2021-11-11 14:58 UTC)

<p>“OT” modality means other, it is an unidentified blob of data. It can be safely ignored.</p>

---

## Post #4 by @rbumm (2021-11-11 17:46 UTC)

<p>That makes sense, and I am now able to display the “TK AC”  b/w series and the “TK 3D” color series.</p>

---
