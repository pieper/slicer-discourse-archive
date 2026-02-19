---
topic_id: 16429
title: "Merge Into Single File Checkbox Value Not Used 4 13 0 2021 0"
date: 2021-03-08
url: https://discourse.slicer.org/t/16429
---

# "Merge into single file" checkbox value not used? (4.13.0-2021-02-17)

**Topic ID**: 16429
**Date**: 2021-03-08
**URL**: https://discourse.slicer.org/t/merge-into-single-file-checkbox-value-not-used-4-13-0-2021-02-17/16429

---

## Post #1 by @hherhold (2021-03-08 13:01 UTC)

<p>It looks like  <code>ExportSegmentsClosedSurfaceRepresentationToFiles()</code> in <code>vtkSlicerSegmentationsModuleLogic</code> ignores the <code>merge</code> parameter and always saves OBJ files as merged. Is this by design?</p>
<p>Thanks!</p>
<p>-Hollister</p>

---

## Post #2 by @lassoan (2021-03-08 13:07 UTC)

<p>Merge option is disabled for OBJ because each segment is exported with a separate material, so segments can be distinguished in viewers and editors.</p>
<p>If for some reason you need to write each segment as a separate mesh then you can export the segments to models by right-clicking on the segmentation in Data module and use menu: File / Save.</p>

---

## Post #3 by @hherhold (2021-03-08 13:09 UTC)

<p>Got it. File/Save is what I’ve been doing all along with saving as PLY but I figured I’d try OBJ.</p>
<p>Thanks!</p>

---
