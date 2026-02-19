---
topic_id: 41437
title: "How Can I Burn Or Hardcode Some Anotations Into A Dicom File"
date: 2025-02-01
url: https://discourse.slicer.org/t/41437
---

# How can I burn or hardcode some anotations into a dicom files (multiple frames-files))

**Topic ID**: 41437
**Date**: 2025-02-01
**URL**: https://discourse.slicer.org/t/how-can-i-burn-or-hardcode-some-anotations-into-a-dicom-files-multiple-frames-files/41437

---

## Post #1 by @eyado (2025-02-01 00:52 UTC)

<p>Hello, I am very new to 3dslicer, i used it only once before. I am looking for a way to hard code information (burn) into the dicom files i had from a cbct machine.<br>
I am doing a study on extracted teeth, i embedded them in silicone and scanned them in batches using a cbct machine, that gave me for each batch a folder with multiple files inside. In each scan i have multiple teeth, i want to give them numbers so that i can assign the same number in the silicon so i can unmount them from silicone, save them in individual boxes with special liquid and remount them later for another scan, so i need to know each tooth by sample number. I cannot do the scan again to add any number physically. I just need to assign these numbers on scan so i can save the file put the teeth in numbered boxes and sleep in peace before any disaster</p>

---

## Post #2 by @pieper (2025-02-10 23:12 UTC)

<p>Do you mean you want to put numbers into the pixel data of each image or do you want to put a number into the dicom headers?  Either is possible, but the latter is easier (look at the DICOM Patcher source code for ideas).  Or you could just rename the files or directories with the numbers.</p>

---

## Post #3 by @nadayoda59 (2025-02-11 01:08 UTC)

<p>Try and identify patient UIDs, study UIDs, series UIDs and isolates and classify them according to UIDs</p>

---
