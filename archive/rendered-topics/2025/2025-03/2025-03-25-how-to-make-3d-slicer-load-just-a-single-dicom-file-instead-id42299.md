# How to make 3D Slicer load just a single DICOM file instead of automatically loading the full series?

**Topic ID**: 42299
**Date**: 2025-03-25
**URL**: https://discourse.slicer.org/t/how-to-make-3d-slicer-load-just-a-single-dicom-file-instead-of-automatically-loading-the-full-series/42299

---

## Post #1 by @shahzadali (2025-03-25 16:24 UTC)

<p>In 3D Slicer (v5.6.2), how can I restrict it to load only a single DICOM (.dcm) file without automatically loading the entire image series it belongs to? I’m trying to inspect just one particular slice, but Slicer keeps importing all files from the same DICOM series (even when they are in a subdirectory). Is there a way to turn off this automatic grouping behavior or force it to treat a DICOM file as a standalone image?</p>

---

## Post #2 by @lassoan (2025-03-25 16:25 UTC)

<p>You can have a look at a single slice if you right-click on the series in DICOM module and click “View DICOM metadata”.</p>
<p>What is your overall goal?</p>

---

## Post #3 by @shahzadali (2025-03-25 17:39 UTC)

<p>I have a large number of DICOM series stored within a directory. The default behavior of recursively loading all DCM files from this directory and its subdirectories is time-consuming. It significantly delays and complicates locating and inspecting a specific slice, especially when I can’t rely solely on filenames and must instead verify a slice using metadata.</p>
<p>P.S. Moving a slice to a new folder before loading into Slicer works, but I would appreciate it if a user could control how Slicer loads slices.</p>

---

## Post #4 by @lassoan (2025-03-25 17:57 UTC)

<p>The recently introduced <a href="https://discourse.slicer.org/t/new-feature-visual-dicom-browser/33874">visual dicom browser</a> achieves low “time to first image” (thumbnail). Then you can right-click to browse all the slices (using “view metadata”), but at this point double-clicking to load all the slices and browse in the slice viewers does not add too much time (and it allows you to see reformatted views).</p>
<p>If you want to browse faster then an alternative is to convert DICOM to NRRD and go through many series using CaseIterator extension.</p>

---
