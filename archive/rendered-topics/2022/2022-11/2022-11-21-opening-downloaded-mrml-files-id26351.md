# Opening Downloaded '.mrml' Files

**Topic ID**: 26351
**Date**: 2022-11-21
**URL**: https://discourse.slicer.org/t/opening-downloaded-mrml-files/26351

---

## Post #1 by @JacobD (2022-11-21 16:18 UTC)

<p>Regarding ‘.mrml’ files downloaded from a Google Drive folder, when attempting to load them to view completed segmentations, the segmentation does not appear, and only a section of the scanned image appears.</p>
<p>When attempting to load the files from the original saved location from the computer that it was created on, the ‘.mrml’ file and respective segmentation loads appropriately.</p>
<p>I was wondering what the appropriate process would be to access the downloaded ‘.mrml’ file from Google Drive. Please feel free to let me know if any other information is requested. Thank you!</p>

---

## Post #2 by @pieper (2022-11-21 19:08 UTC)

<p>External cloud drives like Google Drive or OneDrive sometimes play tricks that break mrml save/restore.  Best practice is to save to local disk and copy to cloud drive.  Also be sure all files are reachable from the same directory tree.  For example if your mrml file has references to an externally mounted drive it can’t make relative paths for reloading and will embed the absolute path.  The easiest way to manage this is to save <code>.mrb</code> files so that all data is in the single file.  This works well if your input data is small and you don’t mind having copies in each <code>.mrb</code>.</p>

---

## Post #3 by @JacobD (2023-01-11 21:51 UTC)

<p>Thank you for the information! Saving the files as <code>.mrb</code> files and storing them on an external hard drive seems to work well. I appreciate the assistance!</p>

---
