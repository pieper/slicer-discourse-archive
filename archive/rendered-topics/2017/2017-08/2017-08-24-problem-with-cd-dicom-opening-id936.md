---
topic_id: 936
title: "Problem With Cd Dicom Opening"
date: 2017-08-24
url: https://discourse.slicer.org/t/936
---

# Problem with CD DICOM opening

**Topic ID**: 936
**Date**: 2017-08-24
**URL**: https://discourse.slicer.org/t/problem-with-cd-dicom-opening/936

---

## Post #1 by @j.avdeev (2017-08-24 14:44 UTC)

<p>Operating system: GNU Debian 8 x64<br>
Slicer version: 4.6.2 x64<br>
Expected behavior: multi DICOM opening with ability to scroll between slices<br>
Actual behavior: DICOM folder opens, but only 1 single slice in 3D Slicer viewer, without ability to scroll between slices etc. Also it looks like Slicer opens multi DICOM not as sequence, but as single DICOM flies 1 by 1 sequentially: opens 1, than closed it, opens next 1 and so on.</p>
<p>CD with DICOM files has Weasis viewer - and Weasis viewer opens DICOM files from this CD without problems.<br>
Do I have to use any DICOM-converters before open this DICOM files in Slicer?</p>

---

## Post #2 by @pieper (2017-08-24 15:34 UTC)

<p>Did you use the DICOM module in Slicer?</p>
<p>It is described here:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM</a></p>
<p>If you are still having trouble, the FAQ with debugging tips is here:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM</a></p>
<p>Note this suggestion which might be what you are describing in your post:</p>
<blockquote>
<p>Try loading the data by selecting one of the files in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/LoadingData">Add Data Dialog</a>. Note: be sure to turn on Show Options and then turn off the Single File option in order to load the selected series as a volume</p>
</blockquote>

---

## Post #3 by @j.avdeev (2017-08-25 14:13 UTC)

<p>Yes, I use DICOM module.</p>
<p>I tried with Add Data Dialog, but no luck.</p>
<p>Also, project, which I trying to open has DICOMDIR file - does this fact changes anything?</p>

---

## Post #4 by @pieper (2017-08-25 14:25 UTC)

<p>No, the DICOMDIR is ignored by the DICOM module.  Can you try the other<br>
suggestions in the FAQ.</p>

---

## Post #5 by @lassoan (2017-08-25 14:43 UTC)

<p>Try the latest nightly version of Slicer, many issues have been fixed since the last stable version.</p>
<p>I’ve also added a section to the FAQ: <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM#Something_is_displayed.2C_but_it_is_not_what_I_expected">https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM#Something_is_displayed.2C_but_it_is_not_what_I_expected</a></p>
<p>Have you tried the run DICOM patcher on your data set?</p>

---

## Post #6 by @j.avdeev (2017-10-14 14:30 UTC)

<p>Yes, point</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM#Something_is_displayed.2C_but_it_is_not_what_I_expected" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM#Something_is_displayed.2C_but_it_is_not_what_I_expected</a></p>
<p>works for me - thank you.</p>

---
