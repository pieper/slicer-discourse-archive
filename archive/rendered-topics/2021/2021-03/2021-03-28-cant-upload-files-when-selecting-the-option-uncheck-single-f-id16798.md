---
topic_id: 16798
title: "Cant Upload Files When Selecting The Option Uncheck Single F"
date: 2021-03-28
url: https://discourse.slicer.org/t/16798
---

# Can't upload files when selecting the “Option” -> Uncheck “Single File”

**Topic ID**: 16798
**Date**: 2021-03-28
**URL**: https://discourse.slicer.org/t/cant-upload-files-when-selecting-the-option-uncheck-single-file/16798

---

## Post #1 by @Pseudoceros (2021-03-28 14:38 UTC)

<p>Hi all,</p>
<p>I’m trying to create a 3D image out of a series of histological sections. I have a .czi file of each slide which I separated into the individual slices and saved as different formats (.tif, .png., .jpeg., .czi) to try to import them into Slicer. Problem is, I can load them without issue the normal way but when I try to load them unchecking “Single File” under “Show Options” (as it’s specified on the tutorial) it fails with a generic error message and I’m at my wits end on what to do.</p>
<p>This is the error I get - Error: Loading H:/Slides/Slide scans/Cestoplana-03/Cestoplana-03_s01.tif -  load failed.</p>
<p>Could anyone give me a hand with this?</p>
<p>Thank you in advance.</p>

---

## Post #2 by @pieper (2021-03-28 15:59 UTC)

<p>You can try ImageStacks from the SlicerMorph extension. <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ImageStacks" class="inline-onebox">SlicerMorph/Docs/ImageStacks at master · SlicerMorph/SlicerMorph · GitHub</a></p>

---

## Post #3 by @Pseudoceros (2021-03-30 03:11 UTC)

<p>Thank you that worked!</p>

---
