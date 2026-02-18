# DICOM Browser does not work in latest nightly

**Topic ID**: 676
**Date**: 2017-07-12
**URL**: https://discourse.slicer.org/t/dicom-browser-does-not-work-in-latest-nightly/676

---

## Post #1 by @yannick_s (2017-07-12 13:47 UTC)

<p><strong>Operating system:</strong> Ubuntu 16.04 LTS<br>
<strong>Slicer version</strong>: 4.7.0-2017-07-10 r26150<br>
<strong>Expected behavio</strong>r: DICOMs can be imported using the DICOM browser<br>
<strong>Actual behavior</strong>: DICOM browser stays empty</p>
<p>Dear all,</p>
<p>I  moved from Slicer version 4.7.0-2017-06-03 r26072 to the latest nightly (4.7.0-2017-07-10 r26150) and I cannot import DICOMS via the DICOM browser anymore. If I open the DICOM browser -&gt; Import and select the directory I want to import, the progress bar appears. After It’s seemingly finished, the DICOM browser is still empty. In the error log appears a critical Qt error: “SQLITE ERROR: Parameter count mismatch”. The browser worked without any issues in 4.7.0-2017-06-03 r26072.</p>
<p>Best,</p>
<p>Yannick</p>

---

## Post #2 by @cpinter (2017-07-12 14:09 UTC)

<p>Can you try deleting the Slicer.ini file? On Mac it’s in the folder /Users/[username]/.config/www.na-mic.org, so I expect it will be /home/[username]/.config/www.na-mic.org on linux.</p>

---

## Post #3 by @yannick_s (2017-07-12 14:13 UTC)

<p>Thanks Csaba, that fixed it</p>

---
