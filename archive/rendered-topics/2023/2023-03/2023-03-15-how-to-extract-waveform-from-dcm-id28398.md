# How to extract waveform from DCM?

**Topic ID**: 28398
**Date**: 2023-03-15
**URL**: https://discourse.slicer.org/t/how-to-extract-waveform-from-dcm/28398

---

## Post #1 by @LukasKnybel (2023-03-15 15:07 UTC)

<p>Dear Slicer Users,<br>
we have waveforms from 4DCT stored as DICOM files. I am wondering if there is any option in Slicer how to visualize them. I have never work with “non-image” DICOM till now and I am little bit lost <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
Thank you for any suggestions!</p>
<p>Lukas</p>

---

## Post #2 by @pieper (2023-03-15 16:15 UTC)

<p>I don’t think we have anything for that data type right now, but it would be great if someone could write a <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/dicom.html#plugin-architecture">DICOMPlugin</a> that could handle them.  It should be relatively straightforward.</p>

---

## Post #3 by @LukasKnybel (2023-03-15 16:42 UTC)

<p>Dear Steve,thank you for quick respond. I tried to find solution somewhere else without success. Even this type of DCM seems to very common in radiotherapy. If someone would be interested in this,I can share some example.<br>
Thanks!</p>

---
