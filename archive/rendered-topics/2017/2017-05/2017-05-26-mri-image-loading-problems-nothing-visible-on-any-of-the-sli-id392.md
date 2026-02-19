---
topic_id: 392
title: "Mri Image Loading Problems Nothing Visible On Any Of The Sli"
date: 2017-05-26
url: https://discourse.slicer.org/t/392
---

# MRI image loading problems: nothing visible on any of the slicer windows/scenes after loading

**Topic ID**: 392
**Date**: 2017-05-26
**URL**: https://discourse.slicer.org/t/mri-image-loading-problems-nothing-visible-on-any-of-the-slicer-windows-scenes-after-loading/392

---

## Post #1 by @Arif_MBRL (2017-05-26 20:13 UTC)

<p>Operating system: Windows 7<br>
Slicer version: 4.6.2 &amp; 4.5.0-1<br>
Expected behavior: series of MRI images visible on different slices<br>
Actual behavior: I’ve imported the DICOM data on slicer and it takes a while as expected. It shows that the data has been imported successfully. But after loading the data, nothing is showing up on either of the slicer windows (red/yellow/green). It’s not showing any error message, but nothing shows up on screen/slicer windows.</p>
<p>I tried to load the data by choosing the directory of my files (Choose Directory to Add). Slicer window keeps changing while loading the data and seems like it’s loading all the slices (around 2200 slices). But finally it shows only one single slice, not the series of MRI images.</p>
<p>I tried it with two different versions of 3D slicer (4.6.2 &amp; 4.5.0-1), but both of them are showing the similar behavior. It will be great if anyone can help me out.</p>
<p>Thanks in advance!</p>

---

## Post #2 by @pieper (2017-05-26 20:38 UTC)

<p>Hi -</p>
<p>Try reviewing the steps in the FAQ:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM#I_try_to_import_a_directory_of_DICOM_files.2C_but_nothing_shows_up_in_the_browser" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM#I_try_to_import_a_directory_of_DICOM_files.2C_but_nothing_shows_up_in_the_browser</a></p>
<p>If you’re still having trouble, send some more detail about the type of data and the error log (edit out any patient info)</p>
<p>-Steve</p>

---

## Post #3 by @lassoan (2017-05-27 00:33 UTC)

<p>You can also try if the problem is solved in the latest nightly version.</p>

---
