# Importing DICOM 4D volumes as Multi Volume or Volume Sequence

**Topic ID**: 34554
**Date**: 2024-02-26
**URL**: https://discourse.slicer.org/t/importing-dicom-4d-volumes-as-multi-volume-or-volume-sequence/34554

---

## Post #1 by @giovform (2024-02-26 20:54 UTC)

<p>What defines which module Slicer will use to interact with a 4D volume? I am experiencing a behavior where on two different computers, with the same Slicer version and the same DICOM data, in one, the data is a Multi Volume, and on another the data is a Volume Sequence, after importing using the Add DICOM Data module.</p>

---

## Post #2 by @pieper (2024-02-26 21:51 UTC)

<p>If you go into the Advanced mode of the dicom module you can select which to use.  Also there’s a plugins panel on the bottom left that you can open up and check/uncheck the methods you want to use.</p>

---
