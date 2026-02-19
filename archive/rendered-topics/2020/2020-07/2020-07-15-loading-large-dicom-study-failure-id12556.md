---
topic_id: 12556
title: "Loading Large Dicom Study Failure"
date: 2020-07-15
url: https://discourse.slicer.org/t/12556
---

# loading  large dicom study failure 

**Topic ID**: 12556
**Date**: 2020-07-15
**URL**: https://discourse.slicer.org/t/loading-large-dicom-study-failure/12556

---

## Post #1 by @Anand_Mulay (2020-07-15 14:55 UTC)

<p>today i tried to load up a study which is 3.6Gb in size , it took 3 hours to show up in DCM database , but failed to load in slicer as a volume , i can view that study in other Dicom viewer but cant load it in slicer.<br>
is there any size limitation or smoothing to load it in slicer?</p>

---

## Post #2 by @lassoan (2020-07-15 14:58 UTC)

<p>We have greatly improved DICOM import and loading in Slicer-4.11. Let us know if you have any difficulties when you use the most recent Slicer Preview Release.</p>

---

## Post #3 by @Anand_Mulay (2020-07-16 09:45 UTC)

<p>i tried the latest nightly build , but still cant load the whole study probably due to the size. i also tried to load few images and that worked , but i need to load the whole study.</p>

---

## Post #4 by @lassoan (2020-07-16 12:52 UTC)

<p>In general, it is recommended to have 5-10x more memory than your base data size. So, if you want to load an entire 3.6GB study then ideally you should have 36GB physical RAM in your computer, but at the minimum, allocate 36GB virtual memory.</p>

---

## Post #5 by @Anand_Mulay (2020-07-21 10:14 UTC)

<p>I tried to load this on my 32GB RAM machine, but still diditn work, i also monitored the memory usage of slicer and it doesn’t exceeds 10GB , and usually it takes hardly 4Gb of memory.</p>

---

## Post #6 by @lassoan (2020-07-22 14:04 UTC)

<p>Please try with latest Slicer Preview Release and if you still have issues then upload the application log (menu: Help/Report a bug) somewhere and post thr link here so that we can investigate.</p>

---
