---
topic_id: 11416
title: "A Way To Automatically Export Stl Files From Many Mrb Files"
date: 2020-05-05
url: https://discourse.slicer.org/t/11416
---

# A way to automatically export stl files from many mrb files?

**Topic ID**: 11416
**Date**: 2020-05-05
**URL**: https://discourse.slicer.org/t/a-way-to-automatically-export-stl-files-from-many-mrb-files/11416

---

## Post #1 by @Aoz (2020-05-05 14:01 UTC)

<p>Hi,</p>
<p>I have got a bunch of mrb files (&gt;100), generated using 3DSlicer v4.1.1. For each of those files, I can export the stl files corresponding to the included segmentations.</p>
<p>But is there a way to process all the mrb files at once?</p>
<p>Thank you!</p>

---

## Post #2 by @pieper (2020-05-05 15:36 UTC)

<p>It would take just a little scripting.  The mrb files are just .zip files and they will have models in a vtk format that would be easy to convert to stl.</p>

---
