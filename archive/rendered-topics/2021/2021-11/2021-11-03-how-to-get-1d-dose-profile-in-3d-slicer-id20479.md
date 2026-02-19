---
topic_id: 20479
title: "How To Get 1D Dose Profile In 3D Slicer"
date: 2021-11-03
url: https://discourse.slicer.org/t/20479
---

# How to get 1D dose profile in 3D slicer

**Topic ID**: 20479
**Date**: 2021-11-03
**URL**: https://discourse.slicer.org/t/how-to-get-1d-dose-profile-in-3d-slicer/20479

---

## Post #1 by @syxz0628 (2021-11-03 17:35 UTC)

<p>Operating system: LINUX<br>
Slicer version: 4.8.1</p>
<p>Hello,<br>
I have loaded DICOM RTdose in Slicer.<br>
I want to check the 1D dose profile and if it is possible also want to export the data.<br>
Is it possible?</p>

---

## Post #2 by @lassoan (2021-11-03 19:56 UTC)

<p>You can use the “Line profile” module in the Sandbox extension to get intensity profile of a volume along a straight line.</p>

---

## Post #3 by @syxz0628 (2021-11-04 15:45 UTC)

<p>I am sorry. I cannot find the extension named: “Sandbox” in the online extensions.<br>
I do find a “Line” function in the toolbar of Slicer (Markups), However, I could not find the view of 1D dose profile or export it through this “Line”.</p>

---

## Post #4 by @lassoan (2021-11-04 16:51 UTC)

<p>I’ve just checked and Sandbox extension appears for latest Slicer Preview Release. Let us know if you have trouble finding it there.</p>

---

## Post #5 by @syxz0628 (2021-11-07 13:35 UTC)

<p>I have found the sandbox extension in Preview Release version Slicer 4.13.0.<br>
However, in this version, the SlicerRT extension is not available, which I also needed.</p>
<p>I have tried to copy the SlicerRT extension from a folder of Slicer 4.11 to the folder of Slicer 4.13.0, seems it cannot work properly.</p>
<p>Is there any version that has both the SlicerRT and the Sndbox extensions available?</p>
<p>Thank you.</p>

---

## Post #6 by @lassoan (2021-11-07 14:51 UTC)

<p>SlicerRT is available for Slicer Preview Releases there was just a build error introduced a few days ago that prevented it from showing up. Until we fix this, you can download a Slicer Preview Release created a week ago: <a href="https://download.slicer.org/?offset=-7">https://download.slicer.org/?offset=-7</a></p>

---

## Post #7 by @syxz0628 (2021-11-07 15:34 UTC)

<p>I got both the SlicerRT and the Sandbox in the version you suggested.</p>
<p>Thank you very much!</p>

---

## Post #8 by @lassoan (2021-11-07 18:39 UTC)

<p>I’ve pushed a fix to SlicerRT so it should be available again in the latest Slicer Preview Release from tomorrow.</p>

---
