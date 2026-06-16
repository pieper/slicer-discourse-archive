---
topic_id: 47347
title: "Registered SPECT DICOM export issue"
date: 2026-06-15
url: https://discourse.slicer.org/t/47347
last_bumped: 2026-06-15T19:03:09.115Z
---

# Registered SPECT DICOM export issue

**Topic ID**: 47347
**Date**: 2026-06-15
**URL**: https://discourse.slicer.org/t/registered-spect-dicom-export-issue/47347

---

## Post #1 by @Sorawipat_Intamoon (2026-06-15 12:40 UTC)

<p>Dear all,</p>
<p>I am working on image-based internal dosimetry using multiple-time-point quantitative SPECT images.</p>
<p>To align the images across time points, I registered each CT image to a reference CT and then applied the resulting transformation matrix to the corresponding SPECT image. The registration was performed using the Transform module, and the transformed SPECT image was hardened before export.</p>
<p>For exporting, I tried several approaches, including DICOM export through Scalar Volume, RT export, and the “Create a DICOM Series” module with manually entered parameters. However, the exported DICOM images do not contain the rescale information (Rescale Slope and Rescale Intercept).</p>
<p>How can I export the transformed SPECT images while preserving the quantitative information, specifically the rescale parameters?</p>
<p>In the original SPECT DICOM files, the quantitative scaling information is stored in:</p>
<ul>
<li>
<p>(0040,9225) Real World Value Slope</p>
</li>
<li>
<p>(0040,9224) Real World Value Intercept</p>
</li>
</ul>
<p>Any suggestions would be greatly appreciated.</p>
<p>Thank you.</p>

---

## Post #2 by @pieper (2026-06-15 19:03 UTC)

<p>That’s probably not a path that anyone has tried before.  Since you have a good idea what the header needs to have your best bet is to just write a small script that applies the fix.  Creating correct exported dicom for all modalities is a big challenge so Slicer only covers some basic use cases.</p>

---
