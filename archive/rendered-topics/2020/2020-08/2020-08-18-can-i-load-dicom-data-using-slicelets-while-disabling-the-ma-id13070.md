---
topic_id: 13070
title: "Can I Load Dicom Data Using Slicelets While Disabling The Ma"
date: 2020-08-18
url: https://discourse.slicer.org/t/13070
---

# Can I load dicom data using slicelets while disabling the main slicer window (--no-main-window)?

**Topic ID**: 13070
**Date**: 2020-08-18
**URL**: https://discourse.slicer.org/t/can-i-load-dicom-data-using-slicelets-while-disabling-the-main-slicer-window-no-main-window/13070

---

## Post #1 by @rak_shrma (2020-08-18 13:08 UTC)

<p>Operating system: Ubuntu 18.04<br>
Slicer version: 4.10.2<br>
Expected behavior: Dicom loader window should open<br>
Actual behavior: Dicom loader does not open and slicer exits with error</p>

---

## Post #2 by @lassoan (2020-08-18 13:18 UTC)

<p>In Slicer-4.10, DICOM import implementation was not clearly separated from the GUI. If you want to load or convert DICOM images without any GUI then you need to use a recent Slicer-4.11 release, where DICOM processing does not rely on any GUI classes.</p>
<p>Note: A few years ago we thought it could be a good idea to create custom user interfaces by replacing the main window, but  we learned that this is not a good approach. Do not use <code>--main-window</code> if you want to display any kind of GUI. Instead you can keep the main window and customize its content (e.g., hide what you don’t need). See more information here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets</a></p>

---
