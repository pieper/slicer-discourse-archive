---
topic_id: 15665
title: "Dicom Import Error"
date: 2021-01-25
url: https://discourse.slicer.org/t/15665
---

# DICOM Import Error

**Topic ID**: 15665
**Date**: 2021-01-25
**URL**: https://discourse.slicer.org/t/dicom-import-error/15665

---

## Post #1 by @nav (2021-01-25 20:26 UTC)

<p>Problem report for Slicer 4.11.20200930 win-amd64: [please describe expected and actual behavior]</p>
<p>Expected: DICOMs to import<br>
Actual: Getting 0 New Patients, 0 New Studies</p>
<p>Log File:<br>
[DEBUG][Qt] 25.01.2021 13:49:01 [] (unknown:0) - Could not load  “H:/Berbeco Lab/Studies/AGuIX/Ratio_AGuIX-Bi/MRI Data/MRI Linac/MRI_Data_Slicer/Agar.samples.01132021_2021.01.13-15.58.20-STD-1.3.12.2.1107.5.99.3_MR_2021-01-13_155821_T1.phantoms.T1.phantoms_COR.T2_n40__00000/1.3.12.2.1107.5.2.50.175831.30000021011315594330500000046.dcm”<br>
DCMTK says:  No such file or directory<br>
[WARNING][Qt] 25.01.2021 13:49:01 [] (unknown:0) - Could not read DICOM file:H:/Berbeco Lab/Studies/AGuIX/Ratio_AGuIX-Bi/MRI Data/MRI Linac/MRI_Data_Slicer/Agar.samples.01132021_2021.01.13-15.58.20-STD-1.3.12.2.1107.5.99.3_MR_2021-01-13_155821_T1.phantoms.T1.phantoms_COR.T2_n40__00000/1.3.12.2.1107.5.2.50.175831.30000021011315594330500000046.dcm</p>

---

## Post #2 by @pieper (2021-01-25 20:36 UTC)

<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#troubleshooting" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#troubleshooting</a></p>

---

## Post #3 by @lassoan (2021-01-25 20:38 UTC)

<p>Probably file path is too long. You need special programming techniques to access filenames longer than 250 characters on Windows.</p>
<p>Latest Slicer Preview Release is a bit more robust to very long filenames, so  if you use that then it may be enough to move the files from <code>H:/Berbeco Lab/Studies/AGuIX/Ratio_AGuIX-Bi/MRI Data/MRI Linac/MRI_Data_Slicer</code> to <code>C:\tmp</code> and import from there.</p>
<p>If these don’t help then follow instructions in the link that <a class="mention" href="/u/pieper">@pieper</a> provided above.</p>

---

## Post #4 by @nav (2021-01-25 21:43 UTC)

<p>Shortening the file path/file name allowed me to import the data. Thank you!</p>

---
