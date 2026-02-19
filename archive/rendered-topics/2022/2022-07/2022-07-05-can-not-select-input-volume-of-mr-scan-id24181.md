---
topic_id: 24181
title: "Can Not Select Input Volume Of Mr Scan"
date: 2022-07-05
url: https://discourse.slicer.org/t/24181
---

# Can not select input volume of MR scan

**Topic ID**: 24181
**Date**: 2022-07-05
**URL**: https://discourse.slicer.org/t/can-not-select-input-volume-of-mr-scan/24181

---

## Post #1 by @francesca_flore (2022-07-05 09:40 UTC)

<p>I can not select input volume of MR scan in all the modules. Only CT scans and not MR scans are displayed in the drop-down menu to select a volume.</p>

---

## Post #2 by @cpinter (2022-07-05 10:00 UTC)

<p>We’ll need much more information. What is the Slicer version, operating system, how did you load the MR images in question, what format it was, screenshot of the Data module and Volumes module etc. Thanks</p>

---

## Post #3 by @francesca_flore (2022-07-05 10:19 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/7000827e07730141e4de1e867c9770871d4312c7.png" data-download-href="/uploads/short-url/fYOzgrstl8q1wlhKplPz1Cyy56L.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/7000827e07730141e4de1e867c9770871d4312c7_2_580x500.png" alt="image" data-base62-sha1="fYOzgrstl8q1wlhKplPz1Cyy56L" width="580" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/0/7000827e07730141e4de1e867c9770871d4312c7_2_580x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/7000827e07730141e4de1e867c9770871d4312c7.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/7000827e07730141e4de1e867c9770871d4312c7.png 2x" data-dominant-color="EFF2F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">867×747 72.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I load it with Load DICOM Data. In the picture you can see the RM and TC loaded. In Volume Module I can see all of them but when I want to select a RM scan in some modules like General Registration module or others specific modules to segment brain I can not see the RM scans, just TC scans.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d04dae552a259234ae3fe94f6b8010035a28f116.png" data-download-href="/uploads/short-url/tIJKaf9aEkYOxzqGiaHHDgeMQf4.png?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d04dae552a259234ae3fe94f6b8010035a28f116.png" alt="Untitled" data-base62-sha1="tIJKaf9aEkYOxzqGiaHHDgeMQf4" width="619" height="500" data-dominant-color="F0F2F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">853×688 38.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2022-07-05 12:28 UTC)

<p>Many modules can only use <em>scalar</em> volume (i.e., that has a single scalar value in each voxel) and not <em>vector</em> or <em>tensor</em> volumes. You can use “Vector to scalar volume” module for conversion.</p>

---

## Post #5 by @francesca_flore (2022-07-05 12:35 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62d16456b371f58ad8d6c33fd0f0cb3af1156e39.png" alt="image" data-base62-sha1="e6bpyOHdDlJhLhJVojFP40c8gch" width="524" height="399"><br>
No input vector volumes finds. They are all scalar volumes.</p>

---

## Post #6 by @lassoan (2022-07-05 15:55 UTC)

<p>I’ve had a closer look at your loaded images and noticed that T1 images were loaded as DWI, which is not correct - they should have been just loaded as scalar volumes. Most likely this issue has been already resolved in the current Slicer Stable Release. If you experience problems with the current Slicer version as well then let us know.</p>

---

## Post #7 by @francesca_flore (2022-07-06 06:51 UTC)

<p>Solved with the current Slicer Stable Release. Thank you!!</p>

---
