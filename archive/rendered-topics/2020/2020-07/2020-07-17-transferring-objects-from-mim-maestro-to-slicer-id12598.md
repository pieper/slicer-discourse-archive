---
topic_id: 12598
title: "Transferring Objects From Mim Maestro To Slicer"
date: 2020-07-17
url: https://discourse.slicer.org/t/12598
---

# transferring objects from MIM Maestro to Slicer

**Topic ID**: 12598
**Date**: 2020-07-17
**URL**: https://discourse.slicer.org/t/transferring-objects-from-mim-maestro-to-slicer/12598

---

## Post #1 by @briannawhitener (2020-07-17 14:28 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.10.2<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hello,<br>
I’d like to be able to create objects in MIM, then save to a shared folder and open them in Slicer. I’ve been able to open images in Slicer, but not the RTstruct. Someone else posted about RTstruct not coming over correctly (and solved the issue) but i don’t see anything on how to get the structures to associate w the images and then open up as segments in Slicer! Anyone familiar?</p>

---

## Post #2 by @lassoan (2020-07-17 15:37 UTC)

<p>You need to install SlicerRT extension to be able to import RT structure sets (and RT plan, image, dose, etc. information objects).</p>

---

## Post #3 by @briannawhitener (2020-07-17 18:57 UTC)

<p>And then what’s the process of exporting/importing the RTstruc from MIM to slicer? Don’t see this anywhere in the SlicerRT tutorial info i could find.</p>
<p>Thanks</p>

---

## Post #4 by @lassoan (2020-07-17 19:16 UTC)

<p>After you install SlicerRT extension, you can read/write RT information objects as any other DICOM objects. If you use a recent Slicer Preview Release: go to DICOM module, drag and drop your DICOM folder to the Slicer application window, wait for import to complete, then double-click on anything you want to load.</p>

---
